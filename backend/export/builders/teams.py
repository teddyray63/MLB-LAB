"""Build export team identity records from schedule and game feed data."""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.export.daily_export_models import Game
from backend.export.identity_models import ExportTeam, TeamSide
from backend.export.mlb_game_feed import parse_game_feed_side
from backend.export.mlb_schedule import ScheduleGameRow


@dataclass
class TeamsBuildResult:
    teams: list[ExportTeam]
    warnings: list[str] = field(default_factory=list)


def build_teams_from_schedule_rows(
    rows: list[ScheduleGameRow],
    *,
    feeds_by_pk: dict[int, dict] | None = None,
) -> TeamsBuildResult:
    feeds_by_pk = feeds_by_pk or {}
    teams: list[ExportTeam] = []
    warnings: list[str] = []
    seen: set[tuple[int, int, TeamSide]] = set()

    for row in rows:
        if row.game_pk is None:
            warnings.append(f"Skipping team build for game missing game_pk: {row.game_id}")
            continue

        feed = feeds_by_pk.get(row.game_pk, {})
        for side, team_id, team_name in (
            ("away", row.away_team_id, row.away_team),
            ("home", row.home_team_id, row.home_team),
        ):
            side_data = parse_game_feed_side(feed, side) if feed else {}
            resolved_team_id = side_data.get("team_id") or team_id
            if resolved_team_id is None:
                warnings.append(f"Missing team_id for {team_name} in game_pk {row.game_pk}")
                continue

            key = (row.game_pk, int(resolved_team_id), side)
            if key in seen:
                warnings.append(
                    f"Duplicate team identity for game_pk {row.game_pk} side {side} "
                    f"team_id {resolved_team_id}"
                )
                continue
            seen.add(key)

            abbreviation = side_data.get("abbreviation")
            if not abbreviation:
                warnings.append(
                    f"Missing abbreviation for team_id {resolved_team_id} in game_pk {row.game_pk}"
                )

            teams.append(
                ExportTeam(
                    team_id=int(resolved_team_id),
                    team_name=side_data.get("team_name") or team_name,
                    game_pk=row.game_pk,
                    side=side,
                    abbreviation=abbreviation,
                    league=side_data.get("league"),
                    division=side_data.get("division"),
                    venue=row.venue,
                )
            )

    return TeamsBuildResult(teams=teams, warnings=_dedupe(warnings))


def validate_team_game_relationships(
    teams: list[ExportTeam],
    games: list[Game],
) -> list[str]:
    errors: list[str] = []
    games_by_pk = {game.game_pk: game for game in games if game.game_pk is not None}
    for team in teams:
        game = games_by_pk.get(team.game_pk)
        if game is None:
            errors.append(f"Team {team.team_id} references missing game_pk {team.game_pk}")
            continue
        expected_name = game.away_team if team.side == "away" else game.home_team
        if team.team_name != expected_name:
            errors.append(
                f"Team name mismatch for game_pk {team.game_pk} side {team.side}: "
                f"{team.team_name!r} vs schedule {expected_name!r}"
            )
    return errors


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
