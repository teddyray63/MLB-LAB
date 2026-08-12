"""Offline tests for G0b.7 pitcher player logs."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from backend.export.enrichment.statcast_source import events_from_fixture
from backend.export.identity_models import ExportPlayer
from backend.export.player_logs.pitcher_logs import (
    build_pitcher_game_log,
    build_pitcher_logs,
    extract_pitcher_appearances_from_feed,
    format_innings_pitched,
    parse_innings_pitched,
)
from backend.export.player_logs.models import PitcherGameLog
from backend.export.player_logs.validation import validate_pitcher_logs

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _pitcher_fixture() -> dict:
    return json.loads((FIXTURES / "pitcher_game_logs_sample.json").read_text(encoding="utf-8"))


def _sample_pitchers() -> list[ExportPlayer]:
    return [
        ExportPlayer(
            player_id=680732,
            full_name="Sean Burke",
            game_pk=822786,
            team_id=145,
            role="starting_pitcher",
            primary_position="P",
            is_actual_starter=True,
        ),
        ExportPlayer(
            player_id=7000101,
            full_name="Reliever One",
            game_pk=822786,
            team_id=145,
            role="bullpen",
            primary_position="P",
        ),
        ExportPlayer(
            player_id=702056,
            full_name="Trey Yesavage",
            game_pk=822786,
            team_id=141,
            role="starting_pitcher",
            primary_position="P",
            is_actual_starter=True,
        ),
    ]


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("0.1", 1 / 3),
        ("0.2", 2 / 3),
        ("1.0", 1.0),
        ("5.2", 5 + 2 / 3),
    ],
)
def test_innings_parsing(raw: str, expected: float) -> None:
    assert parse_innings_pitched(raw) == pytest.approx(expected)
    assert format_innings_pitched(expected) == raw


def test_valid_start_from_feed() -> None:
    fixture = _pitcher_fixture()
    appearances = extract_pitcher_appearances_from_feed(fixture["feed"], game_date=fixture["game_date"])
    starter = next(item for item in appearances if item["player_id"] == 680732)
    log = build_pitcher_game_log(
        starter["player_id"],
        starter["game_date"],
        appearance_type="start",
        box=starter,
    )
    assert log is not None
    assert log.is_start is True
    assert log.is_relief is False
    assert log.innings_pitched == "5.2"
    assert log.pitches == 87
    assert log.decision == "W"


def test_valid_relief_appearance() -> None:
    fixture = _pitcher_fixture()
    appearances = extract_pitcher_appearances_from_feed(fixture["feed"], game_date=fixture["game_date"])
    relief = next(item for item in appearances if item["player_id"] == 7000101)
    log = build_pitcher_game_log(
        relief["player_id"],
        relief["game_date"],
        appearance_type="relief",
        box=relief,
    )
    assert log is not None
    assert log.is_relief is True
    assert log.appearance_type == "relief"
    assert log.decision == "H"


def test_multiple_appearances_from_feed() -> None:
    fixture = _pitcher_fixture()
    feeds = {fixture["game_pk"]: fixture["feed"]}
    result = build_pitcher_logs(
        [],
        _sample_pitchers(),
        feeds_by_pk=feeds,
        feed_dates_by_pk={fixture["game_pk"]: fixture["game_date"]},
    )
    assert len(result.logs) == 3


def test_missing_pitch_count_statcast_only() -> None:
    events = events_from_fixture(FIXTURES / "statcast_hitter_sample.json")
    result = build_pitcher_logs(events, _sample_pitchers(), target_player_ids={702056})
    log = next((row for row in result.logs if row.player_id == 702056), None)
    assert log is not None
    assert log.pitches is not None
    assert log.innings_pitched is None


def test_duplicate_appearance_rejected() -> None:
    fixture = _pitcher_fixture()
    appearances = extract_pitcher_appearances_from_feed(fixture["feed"], game_date=fixture["game_date"])
    starter = next(item for item in appearances if item["player_id"] == 680732)
    log = build_pitcher_game_log(
        starter["player_id"],
        starter["game_date"],
        appearance_type="start",
        box=starter,
    )
    assert log is not None
    report = validate_pitcher_logs(
        [log, log.model_copy()],
        players=_sample_pitchers(),
        teams=[],
        games=[],
    )
    assert report.valid is False


def test_deterministic_output() -> None:
    fixture = _pitcher_fixture()
    feeds = {fixture["game_pk"]: fixture["feed"]}
    first = build_pitcher_logs([], _sample_pitchers(), feeds_by_pk=feeds)
    second = build_pitcher_logs([], _sample_pitchers(), feeds_by_pk=feeds)
    assert [log.model_dump() for log in first.logs] == [log.model_dump() for log in second.logs]


def test_relationship_failure_unknown_pitcher() -> None:
    log = PitcherGameLog(
        player_id=999999,
        game_date="2026-07-19",
        appearance_type="start",
        is_start=True,
        is_relief=False,
        innings_pitched="1.0",
        innings_pitched_decimal=1.0,
        pitches=10,
    )
    report = validate_pitcher_logs([log], players=_sample_pitchers(), teams=[], games=[])
    assert report.valid is False
