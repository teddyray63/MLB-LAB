"""Offline tests for G0b.3 teams builder."""

from __future__ import annotations

import json
from pathlib import Path

from backend.export.builders.games import build_games_from_schedule_json
from backend.export.builders.teams import build_teams_from_schedule_rows, validate_team_game_relationships
from backend.export.mlb_schedule import parse_schedule_rows

FIXTURES = Path(__file__).resolve().parent / "fixtures"
SCHEDULE = FIXTURES / "schedule_sample.json"
LINEUPS = FIXTURES / "lineups_sample.json"


def _schedule():
    return json.loads(SCHEDULE.read_text(encoding="utf-8"))


def _feed():
    return json.loads(LINEUPS.read_text(encoding="utf-8"))


def test_one_game_two_teams() -> None:
    schedule = {
        "dates": [
            {
                "date": "2026-07-19",
                "games": [_schedule()["dates"][0]["games"][0]],
            }
        ]
    }
    rows, _ = parse_schedule_rows(schedule, slate_date="2026-07-19")
    result = build_teams_from_schedule_rows(rows, feeds_by_pk={822786: _feed()})
    assert len(result.teams) == 2
    sides = {team.side for team in result.teams}
    assert sides == {"away", "home"}


def test_multiple_games_from_schedule_fixture() -> None:
    rows, _ = parse_schedule_rows(_schedule(), slate_date="2026-07-19")
    result = build_teams_from_schedule_rows(rows, feeds_by_pk={822786: _feed()})
    assert len(result.teams) == 4
    game_pks = {team.game_pk for team in result.teams}
    assert game_pks == {822786, 823523}
    assert any("Duplicate team identity" in warning for warning in result.warnings)


def test_duplicate_team_identities_warn() -> None:
    schedule = _schedule()
    rows, _ = parse_schedule_rows(schedule, slate_date="2026-07-19")
    duplicate_rows = rows + [rows[0]]
    result = build_teams_from_schedule_rows(duplicate_rows, feeds_by_pk={822786: _feed()})
    assert any("Duplicate team identity" in warning for warning in result.warnings)


def test_missing_abbreviation_warns() -> None:
    feed = _feed()
    feed["gameData"]["teams"]["away"].pop("teamCode", None)
    feed["gameData"]["teams"]["away"].pop("fileCode", None)
    schedule = {"dates": [{"date": "2026-07-19", "games": [_schedule()["dates"][0]["games"][0]]}]}
    rows, _ = parse_schedule_rows(schedule, slate_date="2026-07-19")
    result = build_teams_from_schedule_rows(rows, feeds_by_pk={822786: feed})
    assert any("Missing abbreviation" in warning for warning in result.warnings)


def test_missing_league_division_allowed() -> None:
    feed = _feed()
    feed["gameData"]["teams"]["away"].pop("league", None)
    feed["gameData"]["teams"]["away"].pop("division", None)
    schedule = {"dates": [{"date": "2026-07-19", "games": [_schedule()["dates"][0]["games"][0]]}]}
    rows, _ = parse_schedule_rows(schedule, slate_date="2026-07-19")
    away = next(team for team in build_teams_from_schedule_rows(rows, feeds_by_pk={822786: feed}).teams if team.side == "away")
    assert away.league is None
    assert away.division is None


def test_deterministic_output() -> None:
    rows, _ = parse_schedule_rows(_schedule(), slate_date="2026-07-19")
    first = build_teams_from_schedule_rows(rows, feeds_by_pk={822786: _feed()}).teams
    second = build_teams_from_schedule_rows(rows, feeds_by_pk={822786: _feed()}).teams
    assert [team.model_dump() for team in first] == [team.model_dump() for team in second]


def test_valid_home_away_relationships() -> None:
    games = build_games_from_schedule_json(_schedule(), slate_date="2026-07-19").games
    rows, _ = parse_schedule_rows(_schedule(), slate_date="2026-07-19")
    teams = build_teams_from_schedule_rows(rows, feeds_by_pk={822786: _feed()}).teams
    assert validate_team_game_relationships(teams, games) == []
