"""Minimal backtester: compares past recommendations against recorded results."""
from __future__ import annotations

import logging
import sys
from pathlib import Path

# Allow running as `python backend/engine/backtest.py` from the repo root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from datetime import date
from typing import Any, Dict, List, Optional

from backend.database.database import get_connection

logger = logging.getLogger(__name__)


def _table_exists(cur: Any, table: str) -> bool:
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,))
    return cur.fetchone() is not None


def run_backtest(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    market: Optional[str] = None,
) -> Dict[str, Any]:
    """Compare recommendations in the bets table against results.

    Returns hit_rate, roi_placeholder, bet_count, and date_range.
    Gracefully returns an empty summary when tables or data are missing.
    """
    empty = {
        "bet_count": 0,
        "resolved_count": 0,
        "open_count": 0,
        "hit_rate": None,
        "roi_placeholder": None,
        "date_range": {"start": start_date, "end": end_date},
        "by_market": {},
        "note": "No historical data available.",
    }

    conn = get_connection()
    try:
        cur = conn.cursor()

        if not _table_exists(cur, "bets"):
            logger.warning("backtest: bets table not found")
            return empty

        # Build query
        where: List[str] = ["status IN ('win','loss','push')"]
        params: List[Any] = []
        if start_date:
            where.append("date >= ?")
            params.append(start_date)
        if end_date:
            where.append("date <= ?")
            params.append(end_date)
        if market:
            where.append("market = ?")
            params.append(market)

        clause = " AND ".join(where)
        cur.execute(
            f"SELECT player, team, market, date, status, odds FROM bets WHERE {clause} ORDER BY date",
            params,
        )
        resolved = cur.fetchall()

        # Total bets (including open)
        count_where = []
        count_params: List[Any] = []
        if start_date:
            count_where.append("date >= ?")
            count_params.append(start_date)
        if end_date:
            count_where.append("date <= ?")
            count_params.append(end_date)
        if market:
            count_where.append("market = ?")
            count_params.append(market)
        count_clause = " AND ".join(count_where) if count_where else "1"
        cur.execute(f"SELECT COUNT(*) FROM bets WHERE {count_clause}", count_params)
        bet_count = cur.fetchone()[0]

    finally:
        conn.close()

    if not resolved:
        empty["bet_count"] = bet_count
        empty["open_count"] = bet_count
        empty["note"] = f"{bet_count} bets found, none resolved yet." if bet_count else "No bets recorded."
        return empty

    rows = [dict(r) for r in resolved]
    wins = sum(1 for r in rows if r["status"] == "win")
    losses = sum(1 for r in rows if r["status"] == "loss")
    resolved_count = len(rows)
    hit_rate = round(wins / resolved_count * 100, 1) if resolved_count else None

    # Simple ROI: assume -110 standard odds when no odds stored
    roi_units = 0.0
    for r in rows:
        try:
            american = float(r.get("odds") or -110)
        except (TypeError, ValueError):
            american = -110.0
        if r["status"] == "win":
            roi_units += (100.0 / abs(american)) if american < 0 else (american / 100.0)
        elif r["status"] == "loss":
            roi_units -= 1.0
    roi_pct = round(roi_units / resolved_count * 100, 1) if resolved_count else None

    # Per-market breakdown
    by_market: Dict[str, Dict[str, Any]] = {}
    for r in rows:
        m = r["market"] or "unknown"
        bucket = by_market.setdefault(m, {"wins": 0, "losses": 0, "pushes": 0})
        if r["status"] == "win":
            bucket["wins"] += 1
        elif r["status"] == "loss":
            bucket["losses"] += 1
        else:
            bucket["pushes"] += 1
    for m, bucket in by_market.items():
        total = bucket["wins"] + bucket["losses"] + bucket["pushes"]
        bucket["hit_rate"] = round(bucket["wins"] / total * 100, 1) if total else None

    dates = [r["date"] for r in rows if r.get("date")]
    return {
        "bet_count": bet_count,
        "resolved_count": resolved_count,
        "open_count": bet_count - resolved_count,
        "wins": wins,
        "losses": losses,
        "hit_rate": hit_rate,
        "roi_placeholder": roi_pct,
        "date_range": {
            "start": min(dates) if dates else start_date,
            "end": max(dates) if dates else end_date,
        },
        "by_market": by_market,
        "note": "ROI assumes -110 when no odds are stored.",
    }


def print_backtest_report(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    market: Optional[str] = None,
) -> None:
    """Print a plain-text backtest summary to stdout."""
    result = run_backtest(start_date=start_date, end_date=end_date, market=market)
    dr = result["date_range"]
    print("\n===== MLB-LAB BACKTEST REPORT =====")
    print(f"Date range : {dr['start'] or 'all'} → {dr['end'] or 'all'}")
    print(f"Total bets : {result['bet_count']}")
    print(f"Resolved   : {result['resolved_count']}")
    print(f"Open       : {result['open_count']}")
    if result["hit_rate"] is not None:
        print(f"Hit rate   : {result['hit_rate']}%")
        print(f"ROI (est.) : {result['roi_placeholder']}%")
    if result.get("by_market"):
        print("\nBy market:")
        for m, stats in result["by_market"].items():
            print(f"  {m:15s}  W:{stats['wins']}  L:{stats['losses']}  P:{stats['pushes']}  HR:{stats.get('hit_rate','—')}%")
    print(f"\nNote: {result['note']}")
    print("===================================\n")


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
    start = sys.argv[1] if len(sys.argv) > 1 else None
    end = sys.argv[2] if len(sys.argv) > 2 else None
    mkt = sys.argv[3] if len(sys.argv) > 3 else None
    print_backtest_report(start_date=start, end_date=end, market=mkt)
