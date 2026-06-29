from backend.engine.backtest import run_backtest


def test_backtest_no_data():
    """run_backtest must succeed gracefully when the DB has no resolved bets."""
    result = run_backtest()
    assert isinstance(result, dict)
    assert "bet_count" in result
    assert "hit_rate" in result
    assert "date_range" in result
    assert "by_market" in result
    assert result["resolved_count"] == 0 or result["hit_rate"] is None or isinstance(result["hit_rate"], float)
