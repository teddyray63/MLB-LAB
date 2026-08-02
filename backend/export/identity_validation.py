"""Relationship validation for G0b.3 identity graph."""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.export.daily_export_models import Game, GameDetail
from backend.export.identity_models import ExportLineup, ExportPlayer, ExportTeam


@dataclass
class IdentityValidationReport:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    counts: dict[str, int | float | str] = field(default_factory=dict)
    coverage: dict[str, float | int | str] = field(default_factory=dict)


def validate_identity_graph(
    *,
    games: list[Game],
    game_details: list[GameDetail],
    teams: list[ExportTeam],
    players: list[ExportPlayer],
    lineups: list[ExportLineup],
    builder_warnings: list[str] | None = None,
) -> IdentityValidationReport:
    errors: list[str] = []
    warnings: list[str] = list(builder_warnings or [])

    game_pks = {game.game_pk for game in games if game.game_pk is not None}
    team_keys = {(team.game_pk, team.team_id) for team in teams}
    player_keys = {(player.game_pk, player.player_id) for player in players}

    counts = {
        "games": len(games),
        "game_details": len(game_details),
        "teams": len(teams),
        "players": len(players),
        "lineups": len(lineups),
    }

    if len(games) != len(game_details):
        errors.append(
            f"game_details count ({len(game_details)}) must equal games count ({len(games)})"
        )

    canonical_teams: set[tuple[int, int]] = set()
    for team in teams:
        if team.game_pk not in game_pks:
            errors.append(f"Team {team.team_id} references orphan game_pk {team.game_pk}")
        key = (team.game_pk, team.team_id)
        if key in canonical_teams:
            errors.append(f"Duplicate canonical team record for game_pk/team_id {key}")
        canonical_teams.add(key)

    canonical_players: set[tuple[int, int]] = set()
    for player in players:
        if player.game_pk not in game_pks:
            errors.append(
                f"Player {player.player_id} references orphan game_pk {player.game_pk}"
            )
        if (player.game_pk, player.team_id) not in team_keys:
            errors.append(
                f"Player {player.player_id} references orphan team_id {player.team_id} "
                f"in game_pk {player.game_pk}"
            )
        key = (player.game_pk, player.player_id)
        if key in canonical_players:
            errors.append(f"Duplicate canonical player record for game_pk/player_id {key}")
        canonical_players.add(key)

    missing_lineups = 0
    missing_starting_pitchers = 0
    orphan_lineup_players = 0
    orphan_lineup_teams = 0

    for lineup in lineups:
        if lineup.game_pk not in game_pks:
            errors.append(f"Lineup references orphan game_pk {lineup.game_pk}")
            orphan_lineup_teams += 1
        if (lineup.game_pk, lineup.team_id) not in team_keys:
            errors.append(
                f"Lineup references orphan team_id {lineup.team_id} in game_pk {lineup.game_pk}"
            )
            orphan_lineup_teams += 1

        if not lineup.published:
            missing_lineups += 1
            warnings.append(
                f"Missing published lineup for game_pk {lineup.game_pk} side {lineup.side}"
            )

        for player_id in lineup.batting_order_player_ids:
            if (lineup.game_pk, player_id) not in player_keys:
                errors.append(
                    f"Lineup player_id {player_id} missing from players for game_pk {lineup.game_pk}"
                )
                orphan_lineup_players += 1

        if lineup.starting_pitcher_id is not None:
            if (lineup.game_pk, lineup.starting_pitcher_id) not in player_keys:
                errors.append(
                    f"Starting pitcher {lineup.starting_pitcher_id} missing from players "
                    f"for game_pk {lineup.game_pk} side {lineup.side}"
                )
                missing_starting_pitchers += 1
        else:
            missing_starting_pitchers += 1
            warnings.append(
                f"Missing starting pitcher for game_pk {lineup.game_pk} side {lineup.side}"
            )

    games_with_both_lineups = sum(
        1
        for pk in game_pks
        if any(l.game_pk == pk and l.side == "away" and l.published for l in lineups)
        and any(l.game_pk == pk and l.side == "home" and l.published for l in lineups)
    )

    coverage = {
        "games_with_both_lineups_pct": round(
            (games_with_both_lineups / len(game_pks) * 100) if game_pks else 0,
            1,
        ),
        "missing_lineups": missing_lineups,
        "missing_starting_pitchers": missing_starting_pitchers,
        "orphan_lineup_players": orphan_lineup_players,
        "orphan_team_references": orphan_lineup_teams,
    }
    counts.update(coverage)

    return IdentityValidationReport(
        valid=not errors,
        errors=errors,
        warnings=_dedupe(warnings),
        counts=counts,
        coverage=coverage,
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
