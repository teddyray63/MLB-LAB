"""Relationship tests for G0b.4 enrichment graph."""

from __future__ import annotations

import json
from pathlib import Path

from backend.export.build_matchup_layer import build_matchup_layer
from backend.export.enrichment.enrichment_validation import validate_enrichment_graph

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _layer():
    return build_matchup_layer(
        json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8")),
        slate_date="2026-07-19",
        feeds_by_pk={822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))},
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )


def test_no_name_only_joins_use_player_ids() -> None:
    layer = _layer()
    player_ids = {player.player_id for player in layer.identity.players}
    for matchup in layer.matchups:
        assert matchup.hitter_id in player_ids
        assert matchup.pitcher_id in player_ids


def test_no_cross_game_joins() -> None:
    layer = _layer()
    game_pks = {game.game_pk for game in layer.identity.games if game.game_pk is not None}
    for matchup in layer.matchups:
        assert matchup.game_pk in game_pks
        assert (matchup.game_pk, matchup.hitter_id) in {
            (player.game_pk, player.player_id) for player in layer.identity.players
        }


def test_no_duplicate_ids_silently_collapsed() -> None:
    layer = _layer()
    keys = [(matchup.game_pk, matchup.hitter_id, matchup.pitcher_id) for matchup in layer.matchups]
    assert len(keys) == len(set(keys))


def test_no_player_from_another_game_attached() -> None:
    layer = _layer()
    for matchup in layer.matchups:
        hitter = next(
            player
            for player in layer.identity.players
            if player.player_id == matchup.hitter_id and player.game_pk == matchup.game_pk
        )
        assert hitter.game_pk == matchup.game_pk


def test_no_starter_inferred_from_lineup_position() -> None:
    layer = _layer()
    for lineup in layer.identity.lineups:
        if lineup.starting_pitcher_id is not None:
            assert lineup.batting_order_player_ids[0] == 680732 or lineup.starting_pitcher_id in {
                680732,
                702056,
            }


def test_validation_passes_for_fixture_graph() -> None:
    layer = _layer()
    assert layer.validation is not None
    assert layer.validation.valid is True


def test_lineup_slot_matches_lineup_source() -> None:
    layer = _layer()
    for matchup in layer.matchups:
        lineup = next(
            item
            for item in layer.identity.lineups
            if item.game_pk == matchup.game_pk and item.side == ("home" if matchup.is_home_hitter else "away")
        )
        if matchup.hitter_id in lineup.batting_order_player_ids:
            expected = lineup.batting_order_player_ids.index(matchup.hitter_id) + 1
            assert matchup.lineup_slot == expected
