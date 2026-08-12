"""Offline tests for G0b.7 hitter player logs."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from backend.export.enrichment.statcast_formulas import filter_rows
from backend.export.enrichment.statcast_source import events_from_fixture
from backend.export.identity_models import ExportPlayer, ExportTeam
from backend.export.player_logs.hitter_logs import build_hitter_game_log, build_hitter_logs
from backend.export.player_logs.models import HitterGameLog
from backend.export.player_logs.validation import validate_hitter_logs

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _events():
    return events_from_fixture(FIXTURES / "statcast_hitter_sample.json")


def _sample_players() -> list[ExportPlayer]:
    return [
        ExportPlayer(
            player_id=7000001,
            full_name="Player One",
            game_pk=822786,
            team_id=145,
            role="lineup",
            lineup_slot=2,
        ),
        ExportPlayer(
            player_id=7000002,
            full_name="Player Two",
            game_pk=822786,
            team_id=145,
            role="lineup",
            lineup_slot=3,
        ),
    ]


def test_valid_single_game_log() -> None:
    rows = filter_rows(_events(), batter_id=7000001, game_dates={"2026-07-08"})
    log = build_hitter_game_log(7000001, "2026-07-08", rows)
    assert log is not None
    assert log.pa == 2
    assert log.h == 1
    assert log.singles == 1
    assert log.hr == 0
    assert log.total_bases == 1


def test_multiple_games_sorted_deterministically() -> None:
    result = build_hitter_logs(_events(), _sample_players(), target_player_ids={7000001})
    dates = [log.game_date for log in result.logs if log.player_id == 7000001]
    assert dates == sorted(dates, reverse=True)
    assert len(dates) >= 2


def test_missing_lineup_slot_preserved_null() -> None:
    rows = filter_rows(_events(), batter_id=7000001, game_dates={"2026-07-08"})
    log = build_hitter_game_log(7000001, "2026-07-08", rows, lineup_slot=None)
    assert log is not None
    assert log.lineup_slot is None


def test_zero_stat_game_from_explicit_source_zeros() -> None:
    rows = filter_rows(_events(), batter_id=7000001, game_dates={"2026-07-08"})
    log = build_hitter_game_log(7000001, "2026-07-08", rows)
    assert log is not None
    assert log.hr == 0
    assert log.barrels == 0


def test_missing_stats_remain_null_without_events() -> None:
    log = build_hitter_game_log(7000001, "2026-07-01", [], batting_stats={"runs": 1})
    assert log is None


def test_duplicate_player_game_rejected_by_validation() -> None:
    rows = filter_rows(_events(), batter_id=7000001, game_dates={"2026-07-08"})
    base = build_hitter_game_log(7000001, "2026-07-08", rows)
    assert base is not None
    duplicate = base.model_copy()
    report = validate_hitter_logs(
        [base, duplicate],
        players=_sample_players(),
        teams=[],
        games=[],
    )
    assert report.valid is False
    assert any("duplicate" in error for error in report.errors)


def test_deterministic_output() -> None:
    first = build_hitter_logs(_events(), _sample_players(), target_player_ids={7000001})
    second = build_hitter_logs(_events(), _sample_players(), target_player_ids={7000001})
    assert [log.model_dump() for log in first.logs] == [log.model_dump() for log in second.logs]


def test_relationship_failure_unknown_player() -> None:
    rows = filter_rows(_events(), batter_id=7000001, game_dates={"2026-07-08"})
    log = build_hitter_game_log(9999999, "2026-07-08", rows)
    assert log is not None
    report = validate_hitter_logs(
        [log],
        players=_sample_players(),
        teams=[],
        games=[],
        known_player_ids={7000001},
    )
    assert report.valid is False


def test_rate_calculation_correctness() -> None:
    rows = filter_rows(_events(), batter_id=7000001, game_dates={"2026-07-10"})
    log = build_hitter_game_log(7000001, "2026-07-10", rows)
    assert log is not None
    assert log.pa == 9
    assert log.h == 5
    assert log.hr == 1
    assert log.total_bases == 9
    assert log.avg == pytest.approx(0.625)
    assert log.avg_ev is not None


def test_fixture_sample_rows_validate() -> None:
    payload = json.loads((FIXTURES / "hitter_game_logs_sample.json").read_text(encoding="utf-8"))
    logs = [HitterGameLog.model_validate(row) for row in payload]
    teams = [
        ExportTeam(team_id=145, team_name="White Sox", game_pk=822786, side="away"),
        ExportTeam(team_id=141, team_name="Blue Jays", game_pk=822786, side="home"),
    ]
    report = validate_hitter_logs(logs, players=_sample_players(), teams=teams, games=[])
    assert report.valid is True
