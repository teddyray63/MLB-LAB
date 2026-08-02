"""Offline tests for G0b.2 games + game_details shell builders."""

from __future__ import annotations

import json
import sys
from copy import deepcopy
from pathlib import Path

import pytest

from backend.export.builders.game_details import build_game_details_shell
from backend.export.builders.games import build_games_from_schedule_json, build_games_from_schedule_rows
from backend.export.daily_export_models import Game, GameDetail
from backend.export.daily_export_validation import validate_games_shell, validate_games_shell_dict
from backend.export.mlb_schedule import ScheduleGameRow, parse_schedule_rows

ROOT = Path(__file__).resolve().parent.parent
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "schedule_sample.json"
DB_PATH = ROOT / "database" / "mlb_lab.db"


@pytest.fixture(scope="module")
def schedule_sample() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def db_bytes_before() -> bytes:
    return DB_PATH.read_bytes()


def _single_game_schedule(**overrides) -> dict:
    game = {
        "gamePk": 900001,
        "gameDate": "2026-07-19T18:00:00Z",
        "status": {"detailedState": "Scheduled", "abstractGameState": "Preview"},
        "teams": {
            "away": {
                "team": {"id": 111, "name": "Boston Red Sox"},
                "probablePitcher": {"id": 1, "fullName": "Test Away SP"},
            },
            "home": {
                "team": {"id": 222, "name": "Tampa Bay Rays"},
                "probablePitcher": {"id": 2, "fullName": "Test Home SP"},
            },
        },
        "venue": {"name": "Fenway Park"},
    }
    game.update(overrides)
    return {"dates": [{"date": "2026-07-19", "games": [game]}]}


def test_valid_single_game_builds_and_validates() -> None:
    result = build_games_from_schedule_json(_single_game_schedule(), slate_date="2026-07-19")
    details = build_game_details_shell(result.games)
    report = validate_games_shell(
        slate_date="2026-07-19",
        games=result.games,
        game_details=details,
        builder_warnings=result.warnings,
    )
    assert report.valid
    assert len(result.games) == 1
    assert result.games[0].game_pk == 900001


def test_multiple_games_from_fixture(schedule_sample: dict) -> None:
    result = build_games_from_schedule_json(schedule_sample, slate_date="2026-07-19")
    details = build_game_details_shell(result.games)
    assert len(result.games) == 3
    assert len(details) == 3
    report = validate_games_shell(
        slate_date="2026-07-19",
        games=result.games,
        game_details=details,
        builder_warnings=result.warnings,
    )
    assert report.valid


def test_duplicate_game_pk_surfaces_warning_not_deduped(schedule_sample: dict) -> None:
    result = build_games_from_schedule_json(schedule_sample, slate_date="2026-07-19")
    pks = [game.game_pk for game in result.games]
    assert pks.count(823523) == 2
    assert any("Duplicate game_pk" in warning for warning in result.warnings)


def test_missing_required_game_identity_warns() -> None:
    payload = _single_game_schedule()
    payload["dates"][0]["games"][0].pop("gamePk")
    rows, warnings = parse_schedule_rows(payload, slate_date="2026-07-19")
    assert any("missing gamePk" in warning for warning in warnings)
    result = build_games_from_schedule_rows(rows)
    assert result.games[0].game_pk is None


def test_missing_probable_pitchers_use_tbd() -> None:
    payload = _single_game_schedule()
    payload["dates"][0]["games"][0]["teams"]["away"].pop("probablePitcher")
    payload["dates"][0]["games"][0]["teams"]["home"].pop("probablePitcher")
    result = build_games_from_schedule_json(payload, slate_date="2026-07-19")
    assert result.games[0].away_sp == "TBD"
    assert result.games[0].home_sp == "TBD"
    assert result.games[0].away_sp_id is None
    assert any("No probable away pitcher" in warning for warning in result.warnings)
    assert any("No probable home pitcher" in warning for warning in result.warnings)


def test_missing_lineups_remain_absent_in_shell(schedule_sample: dict) -> None:
    details = build_game_details_shell(
        build_games_from_schedule_json(schedule_sample, slate_date="2026-07-19").games
    )
    for detail in details:
        assert detail.away_lineup is None
        assert detail.home_lineup is None
        assert detail.away_hitters == []
        assert detail.home_hitters == []


def test_malformed_timestamp_surfaces_warning() -> None:
    payload = _single_game_schedule(gameDate="not-an-iso-time")
    rows, warnings = parse_schedule_rows(payload, slate_date="2026-07-19")
    combined = list(rows[0].warnings) + warnings
    assert any("Malformed start time" in warning for warning in combined)


def test_unknown_venue_surfaces_warning() -> None:
    payload = _single_game_schedule()
    payload["dates"][0]["games"][0].pop("venue")
    rows, _ = parse_schedule_rows(payload, slate_date="2026-07-19")
    assert any("Unknown or missing venue" in warning for warning in rows[0].warnings)


def test_score_present_in_coverage_absent_from_game_model(schedule_sample: dict) -> None:
    result = build_games_from_schedule_json(schedule_sample, slate_date="2026-07-19")
    assert result.coverage["schedule_rows_with_score"] >= 2
    assert not hasattr(result.games[0], "away_score")


def test_score_absent_does_not_fabricate_values() -> None:
    payload = _single_game_schedule()
    result = build_games_from_schedule_json(payload, slate_date="2026-07-19")
    assert result.coverage["schedule_rows_with_score"] == 0


def test_broken_game_details_relationship_fails_validation(schedule_sample: dict) -> None:
    games = build_games_from_schedule_json(schedule_sample, slate_date="2026-07-19").games
    details = build_game_details_shell(games)
    broken = deepcopy(details)
    broken[0] = broken[0].model_copy(update={"game_pk": 999999})
    report = validate_games_shell(
        slate_date="2026-07-19",
        games=games,
        game_details=broken,
    )
    assert not report.valid
    assert any("not found in games[]" in error for error in report.errors)


def test_nullable_weather_not_in_shell(schedule_sample: dict) -> None:
    details = build_game_details_shell(
        build_games_from_schedule_json(schedule_sample, slate_date="2026-07-19").games
    )
    for detail in details:
        assert detail.context is None


def test_deterministic_output(schedule_sample: dict) -> None:
    first = build_games_from_schedule_json(schedule_sample, slate_date="2026-07-19")
    second = build_games_from_schedule_json(schedule_sample, slate_date="2026-07-19")
    assert [game.model_dump() for game in first.games] == [game.model_dump() for game in second.games]


def test_game_details_count_equals_games_count(schedule_sample: dict) -> None:
    games = build_games_from_schedule_json(schedule_sample, slate_date="2026-07-19").games
    details = build_game_details_shell(games)
    assert len(details) == len(games)


def test_builder_import_does_not_import_runner() -> None:
    runner_key = "scripts.mlb_lab_runner"
    sys.modules.pop(runner_key, None)
    import backend.export.builders.games  # noqa: F401
    import backend.export.builders.game_details  # noqa: F401
    import backend.export.mlb_schedule  # noqa: F401

    assert runner_key not in sys.modules


def test_no_production_database_mutation(db_bytes_before: bytes) -> None:
    schedule = json.loads(FIXTURE.read_text(encoding="utf-8"))
    games = build_games_from_schedule_json(schedule, slate_date="2026-07-19").games
    build_game_details_shell(games)
    assert DB_PATH.read_bytes() == db_bytes_before


def test_validate_games_shell_dict_round_trip(schedule_sample: dict) -> None:
    games_result = build_games_from_schedule_json(schedule_sample, slate_date="2026-07-19")
    details = build_game_details_shell(games_result.games)
    payload = {
        "date": "2026-07-19",
        "games": [game.model_dump() for game in games_result.games],
        "game_details": [detail.model_dump() for detail in details],
        "builder_warnings": games_result.warnings,
    }
    report = validate_games_shell_dict(payload)
    assert report.valid


def test_schedule_row_direct_build() -> None:
    row = ScheduleGameRow(
        slate_date="2026-07-19",
        game_pk=1,
        game_id="A @ B",
        away_team="A",
        home_team="B",
        away_team_id=1,
        home_team_id=2,
        away_sp="TBD",
        home_sp="TBD",
        away_sp_id=None,
        home_sp_id=None,
        start_time_utc="2026-07-19T18:00:00Z",
        status="Scheduled",
        venue="Test Park",
    )
    result = build_games_from_schedule_rows([row])
    detail = build_game_details_shell(result.games)[0]
    assert isinstance(result.games[0], Game)
    assert isinstance(detail, GameDetail)
