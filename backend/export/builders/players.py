"""Build export player identity records from game feed and roster data."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from backend.export.identity_models import ExportPlayer, ExportTeam, PlayerRole
from backend.export.mlb_game_feed import merge_roster_players, parse_game_feed_side


@dataclass
class PlayersBuildResult:
    players: list[ExportPlayer]
    warnings: list[str] = field(default_factory=list)


def build_players_for_game(
    *,
    game_pk: int,
    side: str,
    team_id: int,
    feed: dict[str, Any],
    roster_json: dict[str, Any] | None = None,
) -> PlayersBuildResult:
    side_data = parse_game_feed_side(feed, side)
    merged_rows = merge_roster_players(side_data["players"], roster_json)
    batting_order = set(side_data["batting_order"])
    bench_ids = {
        row["player_id"]
        for row in merged_rows
        if row["player_id"] not in batting_order
        and (row.get("primary_position") or "").upper() not in {"P", "SP"}
    }
    bullpen_ids = set(side_data["bullpen_pitcher_ids"])
    probable_id = side_data["probable_pitcher_id"]
    starter_id = side_data["starting_pitcher_id"]

    players: list[ExportPlayer] = []
    warnings: list[str] = []
    by_id: dict[int, ExportPlayer] = {}

    for row in merged_rows:
        player_id = row["player_id"]
        if player_id in by_id:
            warnings.append(f"Duplicate player_id {player_id} in game_pk {game_pk} side {side}")
            continue

        role: PlayerRole = "unknown"
        lineup_slot = None
        if player_id in batting_order:
            role = "lineup"
            lineup_slot = side_data["batting_order"].index(player_id) + 1
        elif player_id == starter_id:
            role = "starting_pitcher"
        elif player_id in bullpen_ids:
            role = "bullpen"
        elif player_id in bench_ids:
            role = "bench"

        player = ExportPlayer(
            player_id=player_id,
            full_name=row["full_name"],
            display_name=row.get("display_name"),
            game_pk=game_pk,
            team_id=team_id,
            primary_position=row.get("primary_position"),
            bats=row.get("bats"),
            throws=row.get("throws"),
            roster_status=row.get("roster_status"),
            role=role,
            lineup_slot=lineup_slot,
            is_probable_starter=player_id == probable_id,
            is_actual_starter=player_id == starter_id,
        )
        by_id[player_id] = player
        players.append(player)

    if probable_id is not None and probable_id not in by_id:
        warnings.append(
            f"Probable starter player_id {probable_id} missing from player list "
            f"for game_pk {game_pk} side {side}"
        )

    return PlayersBuildResult(players=players, warnings=warnings)


def build_players_from_teams(
    teams: list[ExportTeam],
    *,
    feeds_by_pk: dict[int, dict],
    rosters_by_team_id: dict[int, dict] | None = None,
) -> PlayersBuildResult:
    rosters_by_team_id = rosters_by_team_id or {}
    all_players: list[ExportPlayer] = []
    warnings: list[str] = []
    global_seen: dict[tuple[int, int], ExportPlayer] = {}

    for team in teams:
        feed = feeds_by_pk.get(team.game_pk, {})
        if not feed:
            warnings.append(f"No game feed for game_pk {team.game_pk} — skipping players for {team.side}")
            continue
        result = build_players_for_game(
            game_pk=team.game_pk,
            side=team.side,
            team_id=team.team_id,
            feed=feed,
            roster_json=rosters_by_team_id.get(team.team_id),
        )
        warnings.extend(result.warnings)
        for player in result.players:
            key = (player.game_pk, player.player_id)
            if key in global_seen:
                existing = global_seen[key]
                if existing.team_id != player.team_id or existing.full_name != player.full_name:
                    warnings.append(
                        f"Conflicting player identity for player_id {player.player_id} "
                        f"in game_pk {player.game_pk}"
                    )
                continue
            global_seen[key] = player
            all_players.append(player)

    return PlayersBuildResult(players=all_players, warnings=_dedupe(warnings))


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
