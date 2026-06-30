import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.engine.warehouse import (
    ensure_warehouse_tables,
    generate_performance,
    query_warehouse,
    record_recommendation,
    record_result,
    record_sportsbook_line,
)


def test_warehouse_stores_and_queries_betting_data(tmp_path, monkeypatch):
    db_path = tmp_path / "warehouse.db"
    monkeypatch.setenv("MLB_LAB_DB_PATH", str(db_path))

    ensure_warehouse_tables()

    record_recommendation(
        {
            "player": "Judge, Aaron",
            "team": "Yankees",
            "market": "singles",
            "confidence": 82.0,
            "edge": 11.0,
            "sportsbook": "DraftKings",
            "line": -110,
            "details": "strong edge",
            "implied_probability": 0.45,
            "clv": None,
            "park_adjusted_ev": 6.5,
            "kelly_fraction": None,
            "stake_pct": None,
            "roi": None,
        },
        event_date="2026-06-28",
    )
    record_sportsbook_line(
        {
            "player": "Judge, Aaron",
            "team": "Yankees",
            "market": "singles",
            "sportsbook": "FanDuel",
            "line": 105,
            "confidence": 80.0,
            "edge": 10.0,
        },
        event_date="2026-06-28",
    )
    record_result(
        {
            "player": "Judge, Aaron",
            "team": "Yankees",
            "market": "singles",
            "sportsbook": "DraftKings",
            "date": "2026-06-28",
            "result": "win",
            "profit": 100.0,
            "roi": 0.2,
            "ev": 0.12,
            "clv": 0.08,
            "confidence": 82.0,
            "edge": 11.0,
            "closing_line": -115,
        }
    )
    generate_performance()

    history_rows = query_warehouse(player="Judge", market="singles", date="2026-06-28")
    assert history_rows
    assert any(row["event_type"] == "recommendation" for row in history_rows)
    assert any(row["event_type"] == "line" for row in history_rows)

    perf_rows = query_warehouse(table="performance", player="Judge", market="singles", date="2026-06-28")
    assert perf_rows
    assert perf_rows[0]["wins"] >= 1

    bet_rows = query_warehouse(table="bets", player="Judge", market="singles", date="2026-06-28")
    assert bet_rows
    assert bet_rows[0]["park_adjusted_ev"] == 6.5
    assert bet_rows[0]["implied_probability"] == 0.45
    assert bet_rows[0]["roi"] is None
    assert bet_rows[0]["kelly_fraction"] is None
