"""Offline tests for G0b.3 players builder."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

from backend.export.builders.players import build_players_for_game, build_players_from_teams
from backend.export.builders.teams import build_teams_from_schedule_rows
from backend.export.mlb_game_feed import merge_roster_players
from backend.export.mlb_schedule import parse_schedule_rows

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _feed():
    return json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))


def _roster():
    return json.loads((FIXTURES / "roster_sample.json").read_text(encoding="utf-8"))


def _teams():
    schedule = json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8"))
    rows, _ = parse_schedule_rows(schedule, slate_date="2026-07-19")
    return build_teams_from_schedule_rows(rows, feeds_by_pk={822786: _feed()}).teams


def test_game_feed_player_identity() -> None:
    result = build_players_for_game(
        game_pk=822786,
        side="away",
        team_id=145,
        feed=_feed(),
    )
    ids = {player.player_id for player in result.players}
    assert 7000001 in ids
    assert all(player.full_name for player in result.players)


def test_roster_merge_without_name_only_collision() -> None:
    feed_players = _feed()["liveData"]["boxscore"]["teams"]["away"]["players"]
    parsed = [
        {
            "player_id": 7000001,
            "full_name": "Player One",
            "display_name": "Player One",
            "primary_position": "DH",
            "bats": "L",
            "throws": "R",
            "roster_status": "Active",
        }
    ]
    merged = merge_roster_players(parsed, _roster())
    assert any(row["player_id"] == 7000999 for row in merged)
    assert len({row["player_id"] for row in merged}) == len(merged)


def test_duplicate_names_different_ids_remain_distinct() -> None:
    feed = deepcopy(_feed())
    dup = feed["liveData"]["boxscore"]["teams"]["away"]["players"]["ID7000002"]
    dup_id = feed["liveData"]["boxscore"]["teams"]["away"]["players"]["ID7000001"]
    dup["person"]["fullName"] = dup_id["person"]["fullName"]
    result = build_players_for_game(game_pk=822786, side="away", team_id=145, feed=feed)
    names = [player.full_name for player in result.players if player.player_id in {7000001, 7000002}]
    assert len(names) == 2


def _handedness_by_id(side: str, team_id: int, feed: dict | None = None) -> dict[int, tuple]:
    result = build_players_for_game(
        game_pk=822786, side=side, team_id=team_id, feed=feed or _feed()
    )
    return {p.player_id: (p.bats, p.throws) for p in result.players}


def test_hitter_bats_survive_feed_to_export() -> None:
    away = _handedness_by_id("away", 145)
    home = _handedness_by_id("home", 141)
    assert away[7000001][0] == "L"
    assert home[7000003][0] == "R"


def test_switch_hitter_preserved_as_switch() -> None:
    away = _handedness_by_id("away", 145)
    assert away[7000002][0] == "S"


def test_pitcher_throws_survive_feed_to_export() -> None:
    away = _handedness_by_id("away", 145)
    assert away[680732][1] == "R"
    assert away[7000101][1] == "L"


def test_missing_handedness_stays_null() -> None:
    feed = deepcopy(_feed())
    feed["gameData"]["players"]["ID7000001"].pop("batSide", None)
    feed["gameData"]["players"].pop("ID7000101", None)
    away = _handedness_by_id("away", 145, feed)
    assert away[7000001][0] is None
    assert away[7000001][1] == "R"
    assert away[7000101] == (None, None)


def test_handedness_keyed_by_mlb_id_not_name() -> None:
    """A name collision must not move handedness between distinct MLB IDs."""
    feed = deepcopy(_feed())
    feed["gameData"]["players"]["ID7000002"]["fullName"] = "Player One"
    feed["liveData"]["boxscore"]["teams"]["away"]["players"]["ID7000002"]["person"][
        "fullName"
    ] = "Player One"
    away = _handedness_by_id("away", 145, feed)
    assert away[7000001] == ("L", "R")
    assert away[7000002] == ("S", "R")


def test_player_ids_unchanged_by_handedness_lookup() -> None:
    result = build_players_for_game(game_pk=822786, side="away", team_id=145, feed=_feed())
    assert {p.player_id for p in result.players} == {680732, 7000001, 7000002, 7000101}


def test_missing_position_stays_null() -> None:
    feed = deepcopy(_feed())
    player = feed["liveData"]["boxscore"]["teams"]["away"]["players"]["ID7000001"]
    player.pop("position", None)
    result = build_players_for_game(game_pk=822786, side="away", team_id=145, feed=feed)
    one = next(p for p in result.players if p.player_id == 7000001)
    assert one.primary_position is None


def test_probable_and_actual_starter_flags() -> None:
    result = build_players_for_game(game_pk=822786, side="away", team_id=145, feed=_feed())
    starter = next(p for p in result.players if p.player_id == 680732)
    assert starter.is_probable_starter is True
    assert starter.is_actual_starter is True
    assert starter.lineup_slot == 1


def test_bench_and_bullpen_roles() -> None:
    result = build_players_for_game(game_pk=822786, side="away", team_id=145, feed=_feed())
    roles = {player.player_id: player.role for player in result.players}
    assert roles[7000001] == "lineup"
    assert roles[7000101] == "bullpen"


def test_build_players_from_teams_fixture() -> None:
    teams = [team for team in _teams() if team.game_pk == 822786]
    result = build_players_from_teams(teams, feeds_by_pk={822786: _feed()}, rosters_by_team_id={145: _roster()})
    assert result.players
    assert all(player.player_id for player in result.players)


def test_deterministic_output() -> None:
    teams = [team for team in _teams() if team.game_pk == 822786]
    first = build_players_from_teams(teams, feeds_by_pk={822786: _feed()}).players
    second = build_players_from_teams(teams, feeds_by_pk={822786: _feed()}).players
    assert [p.model_dump() for p in first] == [p.model_dump() for p in second]
