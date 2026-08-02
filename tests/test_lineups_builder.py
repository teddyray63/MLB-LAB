"""Offline tests for G0b.3 lineups builder and identity validation."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pytest

from backend.export.build_identity_layer import build_identity_layer
from backend.export.builders.games import build_games_from_schedule_json
from backend.export.builders.lineups import apply_lineups_to_game_details, build_lineups_from_teams
from backend.export.builders.players import build_players_from_teams
from backend.export.builders.teams import build_teams_from_schedule_rows
from backend.export.builders.game_details import build_game_details_shell
from backend.export.identity_validation import validate_identity_graph

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _schedule():
    return json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8"))


def _feed():
    return json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))


def _identity_bundle():
    schedule = _schedule()
    feeds = {822786: _feed()}
    result = build_identity_layer(schedule, slate_date="2026-07-19", feeds_by_pk=feeds)
    return result


def test_full_published_lineup_preserves_order() -> None:
    result = _identity_bundle()
    away = next(
        lineup for lineup in result.lineups if lineup.game_pk == 822786 and lineup.side == "away"
    )
    assert away.batting_order_player_ids == [680732, 7000001, 7000002]


def test_missing_lineup_warns_not_fabricates() -> None:
    feed = deepcopy(_feed())
    feed["liveData"]["boxscore"]["teams"]["home"]["battingOrder"] = []
    schedule = {"dates": [{"date": "2026-07-19", "games": [_schedule()["dates"][0]["games"][0]]}]}
    rows, _ = __import__("backend.export.mlb_schedule", fromlist=["parse_schedule_rows"]).parse_schedule_rows(
        schedule, slate_date="2026-07-19"
    )
    teams = build_teams_from_schedule_rows(rows, feeds_by_pk={822786: feed}).teams
    lineups = build_lineups_from_teams(teams, feeds_by_pk={822786: feed})
    home = next(lineup for lineup in lineups.lineups if lineup.side == "home")
    assert home.published is False
    assert any("Missing published lineup" in warning for warning in lineups.warnings)


def test_partial_lineup_keeps_available_rows_only() -> None:
    result = _identity_bundle()
    detail = next(d for d in result.game_details if d.game_pk == 822786)
    assert detail.away_lineup is not None
    assert len(detail.away_lineup) == 3


def test_missing_lineup_source_empty() -> None:
    feed = deepcopy(_feed())
    feed["liveData"]["boxscore"]["teams"]["away"]["battingOrder"] = []
    schedule = {"dates": [{"date": "2026-07-19", "games": [_schedule()["dates"][0]["games"][0]]}]}
    built = build_identity_layer(schedule, slate_date="2026-07-19", feeds_by_pk={822786: feed})
    detail = built.game_details[0]
    assert detail.away_lineup is None
    assert detail.away_lineup_source == "empty"


def test_broken_game_pk_relationship_fails_validation() -> None:
    result = _identity_bundle()
    broken_players = [player.model_copy(update={"game_pk": 999999}) for player in result.players[:1]] + result.players[1:]
    report = validate_identity_graph(
        games=result.games,
        game_details=result.game_details,
        teams=result.teams,
        players=broken_players,
        lineups=result.lineups,
    )
    assert not report.valid
    assert any("references orphan game_pk" in error for error in report.errors)


def test_orphan_lineup_player_reference_fails() -> None:
    result = _identity_bundle()
    broken_lineups = deepcopy(result.lineups)
    broken_lineups[0] = broken_lineups[0].model_copy(
        update={"batting_order_player_ids": [999999]}
    )
    report = validate_identity_graph(
        games=result.games,
        game_details=result.game_details,
        teams=result.teams,
        players=result.players,
        lineups=broken_lineups,
    )
    assert not report.valid


def test_game_details_count_equals_games_count() -> None:
    result = _identity_bundle()
    assert len(result.game_details) == len(result.games)


def test_deterministic_output() -> None:
    first = _identity_bundle()
    second = _identity_bundle()
    assert [g.model_dump() for g in first.games] == [g.model_dump() for g in second.games]
    assert [l.model_dump() for l in first.lineups] == [l.model_dump() for l in second.lineups]


def test_identity_graph_valid_for_fixture() -> None:
    result = _identity_bundle()
    assert result.validation is not None
    assert result.validation.valid
