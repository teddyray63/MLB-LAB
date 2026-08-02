"""Build lineup relationship records and apply them to game_details."""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.export.daily_export_models import GameDetail, LineupBatter, LineupSource
from backend.export.identity_models import ExportLineup, ExportPlayer, ExportTeam
from backend.export.mlb_game_feed import parse_game_feed_side


@dataclass
class LineupsBuildResult:
    lineups: list[ExportLineup]
    warnings: list[str] = field(default_factory=list)


def build_lineups_from_teams(
    teams: list[ExportTeam],
    *,
    feeds_by_pk: dict[int, dict],
) -> LineupsBuildResult:
    lineups: list[ExportLineup] = []
    warnings: list[str] = []

    for team in teams:
        feed = feeds_by_pk.get(team.game_pk, {})
        if not feed:
            warnings.append(f"Missing lineup feed for game_pk {team.game_pk} side {team.side}")
            lineups.append(
                ExportLineup(
                    game_pk=team.game_pk,
                    team_id=team.team_id,
                    side=team.side,
                    published=False,
                    status="unavailable",
                )
            )
            continue

        side_data = parse_game_feed_side(feed, team.side)
        batting_order = side_data["batting_order"]
        if not batting_order:
            warnings.append(f"Missing published lineup for game_pk {team.game_pk} side {team.side}")

        all_player_ids = {row["player_id"] for row in side_data["players"]}
        unknown_in_order = [pid for pid in batting_order if pid not in all_player_ids]
        for pid in unknown_in_order:
            warnings.append(
                f"Lineup references unknown player_id {pid} in game_pk {team.game_pk} side {team.side}"
            )

        bench_ids = sorted(
            pid
            for pid in all_player_ids
            if pid not in batting_order and pid not in side_data["bullpen_pitcher_ids"]
            and pid != side_data["starting_pitcher_id"]
        )

        lineups.append(
            ExportLineup(
                game_pk=team.game_pk,
                team_id=team.team_id,
                side=team.side,
                batting_order_player_ids=batting_order,
                bench_player_ids=bench_ids,
                starting_pitcher_id=side_data["starting_pitcher_id"],
                bullpen_player_ids=side_data["bullpen_pitcher_ids"],
                published=bool(batting_order),
                status="published" if batting_order else "missing",
            )
        )

    return LineupsBuildResult(lineups=lineups, warnings=_dedupe(warnings))


def apply_lineups_to_game_details(
    game_details: list[GameDetail],
    lineups: list[ExportLineup],
    players: list[ExportPlayer],
) -> list[GameDetail]:
    players_by_game: dict[tuple[int, int], ExportPlayer] = {
        (player.game_pk, player.player_id): player for player in players
    }
    lineups_by_key = {(lineup.game_pk, lineup.side): lineup for lineup in lineups}
    updated: list[GameDetail] = []

    for detail in game_details:
        if detail.game_pk is None:
            updated.append(detail)
            continue

        away_lineup = _lineup_batters_for_side(
            detail.game_pk,
            "away",
            lineups_by_key,
            players_by_game,
        )
        home_lineup = _lineup_batters_for_side(
            detail.game_pk,
            "home",
            lineups_by_key,
            players_by_game,
        )
        updated.append(
            detail.model_copy(
                update={
                    "away_lineup": away_lineup.rows,
                    "home_lineup": home_lineup.rows,
                    "away_lineup_source": away_lineup.source,
                    "home_lineup_source": home_lineup.source,
                }
            )
        )

    return updated


@dataclass
class _AppliedLineup:
    rows: list[LineupBatter] | None
    source: LineupSource | None


def _lineup_batters_for_side(
    game_pk: int,
    side: str,
    lineups_by_key: dict[tuple[int, str], ExportLineup],
    players_by_game: dict[tuple[int, int], ExportPlayer],
) -> _AppliedLineup:
    lineup = lineups_by_key.get((game_pk, side))
    if lineup is None or not lineup.published:
        return _AppliedLineup(rows=None, source="empty")

    rows: list[LineupBatter] = []
    for order, player_id in enumerate(lineup.batting_order_player_ids, start=1):
        player = players_by_game.get((game_pk, player_id))
        if player is None:
            continue
        rows.append(
            LineupBatter(
                order=order,
                hitter=player.full_name,
                hand=player.bats,
                status=lineup.status,
            )
        )

    if not rows:
        return _AppliedLineup(rows=None, source="empty")
    return _AppliedLineup(rows=rows, source="override")


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
