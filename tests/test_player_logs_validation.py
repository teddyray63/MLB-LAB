"""Offline tests for G0b.7 player_logs validation."""

from __future__ import annotations

import json
from pathlib import Path

from backend.export.daily_export_models import Game
from backend.export.identity_models import ExportPlayer, ExportTeam
from backend.export.player_logs.models import HitterGameLog, PitcherGameLog
from backend.export.player_logs.validation import validate_player_logs_bundle

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def test_bundle_validates_complete_sample() -> None:
    hitters = [
        HitterGameLog.model_validate(row)
        for row in json.loads((FIXTURES / "hitter_game_logs_sample.json").read_text(encoding="utf-8"))
    ]
    pitcher_fixture = json.loads((FIXTURES / "pitcher_game_logs_sample.json").read_text(encoding="utf-8"))
    pitchers = [PitcherGameLog.model_validate(row) for row in pitcher_fixture["appearances"]]

    players = [
        ExportPlayer(player_id=7000001, full_name="Player One", game_pk=822786, team_id=145),
        ExportPlayer(player_id=680732, full_name="Sean Burke", game_pk=822786, team_id=145),
        ExportPlayer(player_id=7000101, full_name="Reliever One", game_pk=822786, team_id=145),
    ]
    teams = [
        ExportTeam(team_id=145, team_name="White Sox", game_pk=822786, side="away"),
        ExportTeam(team_id=141, team_name="Blue Jays", game_pk=822786, side="home"),
    ]
    games = [
        Game(
            game_id="Away @ Home",
            game_pk=822786,
            away_team="Away",
            home_team="Home",
            away_sp="SP A",
            home_sp="SP H",
            away_sp_id=680732,
            home_sp_id=702056,
        )
    ]

    report = validate_player_logs_bundle(
        hitter_logs=hitters,
        pitcher_logs=pitchers,
        players=players,
        teams=teams,
        games=games,
        matchup_hitter_names={"Player One"},
    )
    assert report.valid is True
    assert report.counts["hitter_logs"] == 2
    assert report.counts["pitcher_logs"] == 2


def test_invalid_lineup_slot_fails() -> None:
    log = HitterGameLog(
        player_id=7000001,
        game_date="2026-07-10",
        lineup_slot=10,
        pa=1,
    )
    from backend.export.player_logs.validation import validate_hitter_logs

    report = validate_hitter_logs(
        [log],
        players=[ExportPlayer(player_id=7000001, full_name="Player One", game_pk=822786, team_id=145)],
        teams=[],
        games=[],
    )
    assert report.valid is False


def test_invalid_innings_format_fails() -> None:
    log = PitcherGameLog(
        player_id=680732,
        game_date="2026-07-19",
        appearance_type="start",
        innings_pitched="5.3",
        innings_pitched_decimal=None,
        pitches=1,
    )
    from backend.export.player_logs.validation import validate_pitcher_logs

    report = validate_pitcher_logs(
        [log],
        players=[ExportPlayer(player_id=680732, full_name="Sean Burke", game_pk=822786, team_id=145)],
        teams=[],
        games=[],
    )
    assert report.valid is False
