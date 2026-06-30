import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _use_temp_db(tmp_path: str) -> None:
    os.environ["MLB_LAB_DB_PATH"] = tmp_path


def test_get_history_summary_empty():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        tmp = f.name
    _use_temp_db(tmp)
    # re-import after env var set so get_connection picks up new path
    import importlib
    import backend.database.database as dbmod
    dbmod.DB_PATH = Path(tmp)
    from backend.engine.warehouse import get_history_summary
    result = get_history_summary()
    assert isinstance(result, dict)
    assert result["total_recommendations"] == 0
    assert result["open"] == 0
    assert result["settled"] == 0
    assert result["wins"] == 0
    assert result["win_rate"] is None
    assert isinstance(result["by_market"], dict)
    assert "date_range" in result
    os.unlink(tmp)


def test_get_history_summary_with_data():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        tmp = f.name
    _use_temp_db(tmp)
    import importlib
    import backend.database.database as dbmod
    dbmod.DB_PATH = Path(tmp)
    from backend.engine.warehouse import record_recommendation, get_history_summary

    record_recommendation({"player": "A", "team": "NYY", "market": "singles", "confidence": 70.0, "edge": 8.0, "grade": "A", "risk": "low"}, event_date="2026-06-01")
    record_recommendation({"player": "B", "team": "BOS", "market": "singles", "confidence": 55.0, "edge": 3.0, "grade": "B", "risk": "medium"}, event_date="2026-06-01")
    record_recommendation({"player": "C", "team": "LAD", "market": "total_bases", "confidence": 65.0, "edge": 5.0, "grade": "A-", "risk": "medium"}, event_date="2026-06-01")

    result = get_history_summary()
    assert result["total_recommendations"] == 3
    assert result["open"] == 3
    assert result["settled"] == 0
    assert result["win_rate"] is None
    assert "singles" in result["by_market"]
    assert result["by_market"]["singles"]["count"] == 2
    assert "total_bases" in result["by_market"]
    assert result["by_market"]["total_bases"]["count"] == 1
    assert result["avg_confidence"] is not None
    os.unlink(tmp)


def test_get_history_summary_date_filter():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        tmp = f.name
    _use_temp_db(tmp)
    import backend.database.database as dbmod
    dbmod.DB_PATH = Path(tmp)
    from backend.engine.warehouse import record_recommendation, get_history_summary

    record_recommendation({"player": "A", "team": "NYY", "market": "singles", "confidence": 70.0}, event_date="2026-05-01")
    record_recommendation({"player": "B", "team": "BOS", "market": "singles", "confidence": 60.0}, event_date="2026-06-15")

    result = get_history_summary(start_date="2026-06-01")
    assert result["total_recommendations"] == 1
    os.unlink(tmp)
