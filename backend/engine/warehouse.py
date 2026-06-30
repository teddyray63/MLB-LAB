import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from backend.database.database import get_connection


def _connect() -> sqlite3.Connection:
    return get_connection()


def ensure_warehouse_tables() -> None:
    """Create all warehouse tables (bets, history, sportsbook_lines, results) if absent."""
    conn = _connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player TEXT,
        team TEXT,
        market TEXT,
        date TEXT,
        sportsbook TEXT,
        odds TEXT,
        line REAL,
        confidence REAL,
        edge REAL,
        ev REAL,
        clv REAL,
        wager_amount REAL,
        status TEXT,
        created_at TEXT,
        grade TEXT,
        risk TEXT,
        implied_probability REAL,
        reasons_json TEXT
    )
    """)
    # Migrate existing bets table that may lack the newer columns
    for col, col_type in [("grade", "TEXT"), ("risk", "TEXT"), ("implied_probability", "REAL"), ("reasons_json", "TEXT")]:
        try:
            cur.execute(f"ALTER TABLE bets ADD COLUMN {col} {col_type}")
        except Exception:
            pass  # column already exists

    cur.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player TEXT,
        team TEXT,
        market TEXT,
        date TEXT,
        sportsbook TEXT,
        result TEXT,
        profit REAL,
        roi REAL,
        ev REAL,
        clv REAL,
        confidence REAL,
        edge REAL,
        closing_line REAL,
        created_at TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS performance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player TEXT,
        team TEXT,
        market TEXT,
        date TEXT,
        sportsbook TEXT,
        bets_count INTEGER,
        wins INTEGER,
        losses INTEGER,
        pushes INTEGER,
        total_profit REAL,
        total_roi REAL,
        avg_ev REAL,
        avg_clv REAL,
        avg_confidence REAL,
        avg_edge REAL,
        created_at TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type TEXT,
        player TEXT,
        team TEXT,
        market TEXT,
        date TEXT,
        sportsbook TEXT,
        payload TEXT,
        created_at TEXT
    )
    """)

    cur.execute("""
    CREATE UNIQUE INDEX IF NOT EXISTS idx_performance_key
    ON performance (player, team, market, date, sportsbook)
    """)

    conn.commit()
    conn.close()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def record_recommendation(payload: Dict[str, Any], event_date: Optional[str] = None) -> Dict[str, Any]:
    """Persist a daily recommendation to the bets and history tables."""
    ensure_warehouse_tables()
    conn = _connect()
    cur = conn.cursor()
    dt = event_date or payload.get("date") or datetime.now(timezone.utc).date().isoformat()
    reasons = payload.get("details") or payload.get("reasons") or []
    row = {
        "player": payload.get("player", ""),
        "team": payload.get("team", ""),
        "market": payload.get("market", ""),
        "date": dt,
        "sportsbook": payload.get("sportsbook", ""),
        "odds": payload.get("odds", ""),
        "line": payload.get("line"),
        "confidence": payload.get("confidence"),
        "edge": payload.get("edge"),
        "ev": payload.get("ev"),
        "clv": payload.get("clv"),
        "wager_amount": payload.get("wager_amount"),
        "status": payload.get("status", "open"),
        "created_at": _now(),
        "grade": payload.get("grade", ""),
        "risk": payload.get("risk", ""),
        "implied_probability": payload.get("implied_probability"),
        "reasons_json": json.dumps(reasons) if isinstance(reasons, list) else str(reasons),
    }
    cur.execute(
        """
        INSERT INTO bets (player, team, market, date, sportsbook, odds, line, confidence, edge, ev, clv, wager_amount, status, created_at, grade, risk, implied_probability, reasons_json)
        VALUES (:player, :team, :market, :date, :sportsbook, :odds, :line, :confidence, :edge, :ev, :clv, :wager_amount, :status, :created_at, :grade, :risk, :implied_probability, :reasons_json)
        """,
        row,
    )
    cur.execute(
        """
        INSERT INTO history (event_type, player, team, market, date, sportsbook, payload, created_at)
        VALUES ('recommendation', :player, :team, :market, :date, :sportsbook, :payload, :created_at)
        """,
        {"player": row["player"], "team": row["team"], "market": row["market"], "date": dt, "sportsbook": row["sportsbook"], "payload": str(payload), "created_at": row["created_at"]},
    )
    conn.commit()
    conn.close()
    return row


def record_sportsbook_line(payload: Dict[str, Any], event_date: Optional[str] = None) -> Dict[str, Any]:
    """Store a sportsbook odds line for later edge analysis."""
    ensure_warehouse_tables()
    conn = _connect()
    cur = conn.cursor()
    dt = event_date or payload.get("date") or datetime.now(timezone.utc).date().isoformat()
    row = {
        "player": payload.get("player", ""),
        "team": payload.get("team", ""),
        "market": payload.get("market", ""),
        "date": dt,
        "sportsbook": payload.get("sportsbook", ""),
        "line": payload.get("line"),
        "confidence": payload.get("confidence"),
        "edge": payload.get("edge"),
        "created_at": _now(),
    }
    cur.execute(
        """
        INSERT INTO history (event_type, player, team, market, date, sportsbook, payload, created_at)
        VALUES ('line', :player, :team, :market, :date, :sportsbook, :payload, :created_at)
        """,
        {"player": row["player"], "team": row["team"], "market": row["market"], "date": dt, "sportsbook": row["sportsbook"], "payload": str(payload), "created_at": row["created_at"]},
    )
    conn.commit()
    conn.close()
    return row


def record_result(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Record an actual game outcome and mark the matching bet as won or lost."""
    ensure_warehouse_tables()
    conn = _connect()
    cur = conn.cursor()
    dt = payload.get("date") or datetime.now(timezone.utc).date().isoformat()
    row = {
        "player": payload.get("player", ""),
        "team": payload.get("team", ""),
        "market": payload.get("market", ""),
        "date": dt,
        "sportsbook": payload.get("sportsbook", ""),
        "result": payload.get("result", "pending"),
        "profit": payload.get("profit"),
        "roi": payload.get("roi"),
        "ev": payload.get("ev"),
        "clv": payload.get("clv"),
        "confidence": payload.get("confidence"),
        "edge": payload.get("edge"),
        "closing_line": payload.get("closing_line"),
        "created_at": _now(),
    }
    cur.execute(
        """
        INSERT INTO results (player, team, market, date, sportsbook, result, profit, roi, ev, clv, confidence, edge, closing_line, created_at)
        VALUES (:player, :team, :market, :date, :sportsbook, :result, :profit, :roi, :ev, :clv, :confidence, :edge, :closing_line, :created_at)
        """,
        row,
    )
    cur.execute(
        """
        INSERT INTO history (event_type, player, team, market, date, sportsbook, payload, created_at)
        VALUES ('result', :player, :team, :market, :date, :sportsbook, :payload, :created_at)
        """,
        {"player": row["player"], "team": row["team"], "market": row["market"], "date": dt, "sportsbook": row["sportsbook"], "payload": str(payload), "created_at": row["created_at"]},
    )
    conn.commit()
    conn.close()
    return row


def generate_performance() -> List[Dict[str, Any]]:
    """Aggregate historical bets into win-rate and ROI performance metrics."""
    ensure_warehouse_tables()
    conn = _connect()
    cur = conn.cursor()
    cur.execute("SELECT player, team, market, date, sportsbook FROM results")
    rows = cur.fetchall()
    for row in rows:
        key = (row["player"], row["team"], row["market"], row["date"], row["sportsbook"])
        cur.execute(
            "SELECT COUNT(*) AS bets_count, SUM(CASE WHEN result='win' THEN 1 ELSE 0 END) AS wins, SUM(CASE WHEN result='loss' THEN 1 ELSE 0 END) AS losses, SUM(CASE WHEN result='push' THEN 1 ELSE 0 END) AS pushes, SUM(profit) AS total_profit, AVG(roi) AS total_roi, AVG(ev) AS avg_ev, AVG(clv) AS avg_clv, AVG(confidence) AS avg_confidence, AVG(edge) AS avg_edge FROM results WHERE player=? AND team=? AND market=? AND date=? AND sportsbook=?",
            key,
        )
        stats = cur.fetchone()
        cur.execute(
            "SELECT COUNT(*) FROM bets WHERE player=? AND team=? AND market=? AND date=? AND sportsbook=?",
            key,
        )
        bets_count = cur.fetchone()[0]
        insert_row = {
            "player": row["player"],
            "team": row["team"],
            "market": row["market"],
            "date": row["date"],
            "sportsbook": row["sportsbook"],
            "bets_count": bets_count or 0,
            "wins": stats["wins"] or 0,
            "losses": stats["losses"] or 0,
            "pushes": stats["pushes"] or 0,
            "total_profit": stats["total_profit"] or 0.0,
            "total_roi": stats["total_roi"] or 0.0,
            "avg_ev": stats["avg_ev"] or 0.0,
            "avg_clv": stats["avg_clv"] or 0.0,
            "avg_confidence": stats["avg_confidence"] or 0.0,
            "avg_edge": stats["avg_edge"] or 0.0,
            "created_at": _now(),
        }
        cur.execute(
            """
            INSERT INTO performance (player, team, market, date, sportsbook, bets_count, wins, losses, pushes, total_profit, total_roi, avg_ev, avg_clv, avg_confidence, avg_edge, created_at)
            VALUES (:player, :team, :market, :date, :sportsbook, :bets_count, :wins, :losses, :pushes, :total_profit, :total_roi, :avg_ev, :avg_clv, :avg_confidence, :avg_edge, :created_at)
            ON CONFLICT(player, team, market, date, sportsbook) DO UPDATE SET
                bets_count = excluded.bets_count,
                wins = excluded.wins,
                losses = excluded.losses,
                pushes = excluded.pushes,
                total_profit = excluded.total_profit,
                total_roi = excluded.total_roi,
                avg_ev = excluded.avg_ev,
                avg_clv = excluded.avg_clv,
                avg_confidence = excluded.avg_confidence,
                avg_edge = excluded.avg_edge,
                created_at = excluded.created_at
            """,
            insert_row,
        )
    conn.commit()
    conn.close()
    return [dict(row) for row in rows]


def get_history_summary(start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict[str, Any]:
    """Return aggregated recommendation history: totals, open/settled, win rate, ROI, grouped by market."""
    ensure_warehouse_tables()
    conn = _connect()
    cur = conn.cursor()

    where_clauses = []
    params: List[Any] = []
    if start_date:
        where_clauses.append("date >= ?")
        params.append(start_date)
    if end_date:
        where_clauses.append("date <= ?")
        params.append(end_date)
    where_sql = ("WHERE " + " AND ".join(where_clauses)) if where_clauses else ""

    cur.execute(f"SELECT COUNT(*) FROM bets {where_sql}", params)
    total = cur.fetchone()[0]

    cur.execute(f"SELECT COUNT(*) FROM bets {where_sql} AND status='open'" if where_clauses else "SELECT COUNT(*) FROM bets WHERE status='open'", params)
    open_count = cur.fetchone()[0]

    cur.execute(
        f"SELECT COUNT(*) FROM bets {where_sql} AND status IN ('win','loss','push')" if where_clauses else "SELECT COUNT(*) FROM bets WHERE status IN ('win','loss','push')",
        params,
    )
    settled = cur.fetchone()[0]

    cur.execute(
        f"SELECT COUNT(*) FROM bets {where_sql} AND status='win'" if where_clauses else "SELECT COUNT(*) FROM bets WHERE status='win'",
        params,
    )
    wins = cur.fetchone()[0]

    win_rate = round(wins / settled, 4) if settled else None

    cur.execute(f"SELECT AVG(confidence) FROM bets {where_sql}", params)
    avg_conf_row = cur.fetchone()
    avg_confidence = round(avg_conf_row[0], 2) if avg_conf_row and avg_conf_row[0] is not None else None

    cur.execute(f"SELECT AVG(edge) FROM bets {where_sql}", params)
    avg_edge_row = cur.fetchone()
    avg_edge = round(avg_edge_row[0], 2) if avg_edge_row and avg_edge_row[0] is not None else None

    cur.execute(
        f"SELECT market, COUNT(*) as cnt, AVG(confidence) as avg_conf, AVG(edge) as avg_edge, SUM(CASE WHEN status='win' THEN 1 ELSE 0 END) as wins, SUM(CASE WHEN status IN ('win','loss','push') THEN 1 ELSE 0 END) as settled FROM bets {where_sql} GROUP BY market",
        params,
    )
    by_market: Dict[str, Dict[str, Any]] = {}
    for row in cur.fetchall():
        mkt = row[0] or "unknown"
        s = row[4]
        w = row[3]
        by_market[mkt] = {
            "count": row[1],
            "avg_confidence": round(row[2], 2) if row[2] is not None else None,
            "avg_edge": round(w, 2) if w is not None else None,
            "settled": s,
            "wins": row[4],
            "win_rate": round(row[4] / s, 4) if s else None,
        }

    conn.close()
    return {
        "total_recommendations": total,
        "open": open_count,
        "settled": settled,
        "wins": wins,
        "win_rate": win_rate,
        "avg_confidence": avg_confidence,
        "avg_edge": avg_edge,
        "by_market": by_market,
        "date_range": {"start": start_date, "end": end_date},
    }


def query_warehouse(table: str = "history", player: Optional[str] = None, market: Optional[str] = None, date: Optional[str] = None, team: Optional[str] = None, sportsbook: Optional[str] = None, confidence: Optional[float] = None) -> List[Dict[str, Any]]:
    """Query the warehouse with optional filters; returns matching rows as dicts."""
    ensure_warehouse_tables()
    conn = _connect()
    cur = conn.cursor()
    where = []
    params: List[Any] = []
    if player:
        where.append("player LIKE ?")
        params.append(f"%{player}%")
    if market:
        where.append("market LIKE ?")
        params.append(f"%{market}%")
    if date:
        where.append("date = ?")
        params.append(date)
    if team:
        where.append("team LIKE ?")
        params.append(f"%{team}%")
    if sportsbook:
        where.append("sportsbook LIKE ?")
        params.append(f"%{sportsbook}%")
    if confidence is not None:
        if table == "performance":
            where.append("avg_confidence >= ?")
        else:
            where.append("confidence >= ?")
        params.append(confidence)
    sql = f"SELECT * FROM {table}"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY date DESC, created_at DESC"
    cur.execute(sql, params)
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows
