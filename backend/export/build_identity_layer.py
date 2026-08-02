"""Orchestrate G0b.3 identity-layer builders."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from backend.export.builders.game_details import build_game_details_shell
from backend.export.builders.games import GamesBuildResult, build_games_from_schedule_json
from backend.export.builders.lineups import LineupsBuildResult, apply_lineups_to_game_details, build_lineups_from_teams
from backend.export.builders.players import PlayersBuildResult, build_players_from_teams
from backend.export.builders.teams import TeamsBuildResult, build_teams_from_schedule_rows
from backend.export.daily_export_models import Game, GameDetail
from backend.export.identity_models import ExportLineup, ExportPlayer, ExportTeam
from backend.export.identity_validation import IdentityValidationReport, validate_identity_graph
from backend.export.mlb_schedule import parse_schedule_rows


@dataclass
class IdentityLayerResult:
    games: list[Game]
    game_details: list[GameDetail]
    teams: list[ExportTeam]
    players: list[ExportPlayer]
    lineups: list[ExportLineup]
    warnings: list[str] = field(default_factory=list)
    games_coverage: dict[str, int | str | None] = field(default_factory=dict)
    validation: IdentityValidationReport | None = None


def build_identity_layer(
    schedule_json: dict[str, Any],
    *,
    slate_date: str,
    feeds_by_pk: dict[int, dict] | None = None,
    rosters_by_team_id: dict[int, dict] | None = None,
) -> IdentityLayerResult:
    feeds_by_pk = feeds_by_pk or {}
    games_result: GamesBuildResult = build_games_from_schedule_json(schedule_json, slate_date=slate_date)
    rows, _ = parse_schedule_rows(schedule_json, slate_date=slate_date)

    teams_result: TeamsBuildResult = build_teams_from_schedule_rows(rows, feeds_by_pk=feeds_by_pk)
    players_result: PlayersBuildResult = build_players_from_teams(
        teams_result.teams,
        feeds_by_pk=feeds_by_pk,
        rosters_by_team_id=rosters_by_team_id,
    )
    lineups_result: LineupsBuildResult = build_lineups_from_teams(
        teams_result.teams,
        feeds_by_pk=feeds_by_pk,
    )

    game_details = build_game_details_shell(games_result.games)
    game_details = apply_lineups_to_game_details(
        game_details,
        lineups_result.lineups,
        players_result.players,
    )

    warnings = _dedupe(
        games_result.warnings
        + teams_result.warnings
        + players_result.warnings
        + lineups_result.warnings
    )

    validation = validate_identity_graph(
        games=games_result.games,
        game_details=game_details,
        teams=teams_result.teams,
        players=players_result.players,
        lineups=lineups_result.lineups,
        builder_warnings=warnings,
    )

    return IdentityLayerResult(
        games=games_result.games,
        game_details=game_details,
        teams=teams_result.teams,
        players=players_result.players,
        lineups=lineups_result.lineups,
        warnings=warnings,
        games_coverage=games_result.coverage,
        validation=validation,
    )


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
