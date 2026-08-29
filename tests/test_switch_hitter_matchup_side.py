"""DEC-009 switch-hitter matchup-effective side tests."""

from __future__ import annotations

import json
from pathlib import Path

from backend.export.builders.lineups import apply_lineups_to_game_details
from backend.export.builders.players import build_players_for_game
from backend.export.daily_export_models import Game, GameDetail, LineupBatter
from backend.export.enrichment.enrichment_models import (
    CountBlock,
    HitterEnrichment,
    PitchMixSummary,
    PitcherEnrichment,
    RateBlock,
    SplitBlock,
)
from backend.export.enrichment.matchups import _matchup_effective_bats, build_matchups
from backend.export.identity_models import ExportLineup, ExportPlayer, ExportTeam

FIXTURES = Path(__file__).resolve().parent / "fixtures"
GAME_PK = 822786
SWITCH_ID = 7000999
HOME_STARTER_ID = 702056


def _split(name: str, pa: int = 50) -> SplitBlock:
    return SplitBlock(
        split=name,  # type: ignore[arg-type]
        counts=CountBlock(pa=pa),
        rates=RateBlock(woba=0.320),
    )


def _switch_matchup(*, pitcher_throws: str | None):
    feed = json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))
    away_players = build_players_for_game(
        game_pk=GAME_PK, side="away", team_id=145, feed=feed
    ).players
    switch = ExportPlayer(
        player_id=SWITCH_ID,
        full_name="Switch Hitter",
        game_pk=GAME_PK,
        team_id=145,
        bats="S",
        throws=None,
        role="lineup",
        lineup_slot=2,
    )
    home_starter = ExportPlayer(
        player_id=HOME_STARTER_ID,
        full_name="Trey Yesavage",
        game_pk=GAME_PK,
        team_id=141,
        bats="R",
        throws=pitcher_throws,
        role="starting_pitcher",
        is_probable_starter=True,
        is_actual_starter=True,
    )
    players = [p for p in away_players if p.player_id != 7000002] + [switch, home_starter]

    teams = [
        ExportTeam(team_id=145, team_name="Away", game_pk=GAME_PK, side="away"),
        ExportTeam(team_id=141, team_name="Home", game_pk=GAME_PK, side="home"),
    ]
    lineups = [
        ExportLineup(
            game_pk=GAME_PK,
            team_id=145,
            side="away",
            batting_order_player_ids=[680732, SWITCH_ID],
            starting_pitcher_id=680732,
            published=True,
        ),
        ExportLineup(
            game_pk=GAME_PK,
            team_id=141,
            side="home",
            batting_order_player_ids=[HOME_STARTER_ID, 7000003],
            starting_pitcher_id=HOME_STARTER_ID,
            published=True,
        ),
    ]
    games = [
        Game(
            game_pk=GAME_PK,
            game_id="fixture",
            away_team="Away",
            home_team="Home",
            away_sp="Sean Burke",
            home_sp="Trey Yesavage",
            away_sp_id=680732,
            home_sp_id=HOME_STARTER_ID,
        )
    ]
    details = [
        GameDetail(
            game_pk=GAME_PK,
            game_id="fixture",
            away_team="Away",
            home_team="Home",
            away_sp="Sean Burke",
            home_sp="Trey Yesavage",
            away_hitters=[],
            home_hitters=[],
            away_pitch_mix=[],
            home_pitch_mix=[],
            away_bullpen=[],
            home_bullpen=[],
            away_lineup=[
                LineupBatter(order=1, hitter="Sean Burke", hand="R"),
                LineupBatter(order=2, hitter="Switch Hitter", hand="S"),
            ],
            home_lineup=[
                LineupBatter(order=1, hitter="Trey Yesavage", hand="R"),
                LineupBatter(order=2, hitter="Player Three", hand="R"),
            ],
        )
    ]
    details = apply_lineups_to_game_details(details, lineups, players)

    hitter_enrichments = [
        HitterEnrichment(
            player_id=SWITCH_ID,
            game_pk=GAME_PK,
            team_id=145,
            opponent_team_id=141,
            opponent_starter_id=HOME_STARTER_ID,
            lineup_slot=2,
            bats="S",
            splits={
                "overall": _split("overall"),
                "vs_lhp": _split("vs_lhp", pa=40),
                "vs_rhp": _split("vs_rhp", pa=60),
            },
        )
    ]
    pitcher_splits = {
        "overall": _split("overall"),
        "vs_lhb": _split("vs_lhb", pa=30),
        "vs_rhb": _split("vs_rhb", pa=70),
    }
    pitcher_enrichments = [
        PitcherEnrichment(
            player_id=HOME_STARTER_ID,
            game_pk=GAME_PK,
            team_id=141,
            opponent_team_id=145,
            throws=pitcher_throws,
            splits=pitcher_splits,
        )
    ]
    pitch_mix = [PitchMixSummary(pitcher_id=HOME_STARTER_ID, game_pk=GAME_PK, entries=[])]

    result = build_matchups(
        games=games,
        game_details=details,
        teams=teams,
        players=players,
        lineups=lineups,
        hitter_enrichments=hitter_enrichments,
        pitcher_enrichments=pitcher_enrichments,
        pitch_mix_summaries=pitch_mix,
        events=[],
    )
    return next(m for m in result.matchups if m.hitter_id == SWITCH_ID)


def test_effective_bats_helper_l_r_unchanged() -> None:
    assert _matchup_effective_bats("L", "R") == "L"
    assert _matchup_effective_bats("R", "L") == "R"


def test_effective_bats_switch_vs_rhp() -> None:
    assert _matchup_effective_bats("S", "R") == "L"


def test_effective_bats_switch_vs_lhp() -> None:
    assert _matchup_effective_bats("S", "L") == "R"


def test_effective_bats_switch_unknown_pitcher_throws() -> None:
    assert _matchup_effective_bats("S", None) is None
    assert _matchup_effective_bats("S", "X") is None


def test_effective_bats_unknown_hitter_bats() -> None:
    assert _matchup_effective_bats(None, "R") is None


def test_switch_vs_rhp_selects_vs_lhb() -> None:
    matchup = _switch_matchup(pitcher_throws="R")
    assert matchup.hitter_bats == "S"
    assert matchup.matchup_effective_bats == "L"
    assert matchup.pitcher_split_vs_hitter_side is not None
    assert matchup.pitcher_split_vs_hitter_side.split == "vs_lhb"
    assert matchup.pitcher_split_vs_hitter_side.counts.pa == 30
    assert matchup.hitter_split_vs_pitcher_hand is not None
    assert matchup.hitter_split_vs_pitcher_hand.split == "vs_rhp"


def test_switch_vs_lhp_selects_vs_rhb() -> None:
    matchup = _switch_matchup(pitcher_throws="L")
    assert matchup.hitter_bats == "S"
    assert matchup.matchup_effective_bats == "R"
    assert matchup.pitcher_split_vs_hitter_side is not None
    assert matchup.pitcher_split_vs_hitter_side.split == "vs_rhb"
    assert matchup.pitcher_split_vs_hitter_side.counts.pa == 70
    assert matchup.hitter_split_vs_pitcher_hand is not None
    assert matchup.hitter_split_vs_pitcher_hand.split == "vs_lhp"


def test_switch_vs_unknown_pitcher_throws_null_effective_and_split() -> None:
    assert _matchup_effective_bats("S", None) is None
    matchup = _switch_matchup(pitcher_throws=None)
    assert matchup.hitter_bats == "S"
    assert matchup.matchup_effective_bats is None
    assert matchup.pitcher_split_vs_hitter_side is None


def test_l_hitter_effective_equals_canonical() -> None:
    assert _matchup_effective_bats("L", "R") == "L"
    assert _matchup_effective_bats("R", "L") == "R"


def test_export_player_bats_remains_s() -> None:
    feed = json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))
    feed["gameData"]["players"]["ID7000002"]["batSide"] = {"code": "S", "description": "Switch"}
    players = build_players_for_game(game_pk=GAME_PK, side="away", team_id=145, feed=feed).players
    assert next(p for p in players if p.player_id == 7000002).bats == "S"


def test_lineup_batter_hand_remains_s_from_player_identity() -> None:
    feed = json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))
    feed["gameData"]["players"]["ID7000002"]["batSide"] = {"code": "S", "description": "Switch"}
    players = build_players_for_game(game_pk=GAME_PK, side="away", team_id=145, feed=feed).players
    lineups = [
        ExportLineup(
            game_pk=GAME_PK,
            team_id=145,
            side="away",
            batting_order_player_ids=[680732, 7000002],
            starting_pitcher_id=680732,
            published=True,
        )
    ]
    details = apply_lineups_to_game_details(
        [
            GameDetail(
                game_pk=GAME_PK,
                game_id="fixture",
                away_team="Away",
                home_team="Home",
                away_sp="Sean Burke",
                home_sp="Trey Yesavage",
                away_hitters=[],
                home_hitters=[],
                away_pitch_mix=[],
                home_pitch_mix=[],
                away_bullpen=[],
                home_bullpen=[],
            )
        ],
        lineups,
        players,
    )
    assert details[0].away_lineup is not None
    assert next(b for b in details[0].away_lineup if b.hitter == "Player Two").hand == "S"


def test_bvp_unchanged_for_switch_hitter() -> None:
    matchup = _switch_matchup(pitcher_throws="R")
    assert matchup.head_to_head is not None
    assert matchup.head_to_head.hitter_id == SWITCH_ID
    assert matchup.head_to_head.pitcher_id == HOME_STARTER_ID


def test_non_switch_layer_regression() -> None:
    from backend.export.build_matchup_layer import build_matchup_layer

    layer = build_matchup_layer(
        json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8")),
        slate_date="2026-07-19",
        feeds_by_pk={822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))},
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )
    for matchup in layer.matchups:
        if matchup.hitter_bats in ("L", "R"):
            assert matchup.matchup_effective_bats == matchup.hitter_bats
        assert matchup.hitter_bats not in ("L", "R") or matchup.pitcher_split_vs_hitter_side is not None or matchup.pitcher_throws is None
