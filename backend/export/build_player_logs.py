"""Orchestrate hitter and pitcher game-log builders for the daily export pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.export.daily_export_models import Game, GameLogEntry, HitterRow
from backend.export.enrichment.statcast_source import StatcastEvents
from backend.export.identity_models import ExportPlayer, ExportTeam
from backend.export.player_logs.hitter_logs import HitterLogsBuildResult, build_hitter_logs
from backend.export.player_logs.models import HitterGameLog, PitcherGameLog, hitter_log_to_export_entry
from backend.export.player_logs.pitcher_logs import PitcherLogsBuildResult, build_pitcher_logs
from backend.export.player_logs.validation import PlayerLogsValidationReport, validate_player_logs_bundle


@dataclass
class PlayerLogsLayerResult:
    hitter_logs: list[HitterGameLog] = field(default_factory=list)
    pitcher_logs: list[PitcherGameLog] = field(default_factory=list)
    export_player_logs: dict[str, list[GameLogEntry]] | None = None
    warnings: list[str] = field(default_factory=list)
    validation: PlayerLogsValidationReport | None = None
    counts: dict[str, int | float | str] = field(default_factory=dict)


def _matchup_hitter_ids(matchups: list[HitterRow], players: list[ExportPlayer]) -> set[int]:
    names = {row.hitter for row in matchups}
    lower_names = {name.lower() for name in names}
    ids: set[int] = set()
    for player in players:
        if player.full_name in names or player.full_name.lower() in lower_names:
            ids.add(player.player_id)
    return ids


def _lineup_slot_index(players: list[ExportPlayer]) -> dict[tuple[int, int], int]:
    slots: dict[tuple[int, int], int] = {}
    for player in players:
        if player.lineup_slot is not None:
            slots[(player.game_pk, player.player_id)] = player.lineup_slot
    return slots


def build_player_logs_layer(
    *,
    events: StatcastEvents,
    players: list[ExportPlayer],
    teams: list[ExportTeam],
    games: list[Game],
    matchups: list[HitterRow],
    feeds_by_pk: dict[int, dict] | None = None,
    feed_dates_by_pk: dict[int, str] | None = None,
    max_games_per_player: int = 20,
) -> PlayerLogsLayerResult:
    target_hitter_ids = _matchup_hitter_ids(matchups, players)
    starter_and_reliever_ids = {
        player.player_id
        for player in players
        if player.role in {"starting_pitcher", "probable_starter", "bullpen"}
        or player.primary_position == "P"
        or player.is_actual_starter
        or player.is_probable_starter
    }

    hitter_result: HitterLogsBuildResult = build_hitter_logs(
        events,
        players,
        target_player_ids=target_hitter_ids,
        max_games_per_player=max_games_per_player,
        lineup_slot_by_player_game=_lineup_slot_index(players),
    )
    pitcher_result: PitcherLogsBuildResult = build_pitcher_logs(
        events,
        players,
        feeds_by_pk=feeds_by_pk,
        feed_dates_by_pk=feed_dates_by_pk,
        target_player_ids=starter_and_reliever_ids,
        max_appearances_per_player=max_games_per_player,
    )

    validation = validate_player_logs_bundle(
        hitter_logs=hitter_result.logs,
        pitcher_logs=pitcher_result.logs,
        players=players,
        teams=teams,
        games=games,
        matchup_hitter_names={row.hitter for row in matchups},
        builder_warnings=hitter_result.warnings + pitcher_result.warnings,
    )

    export_logs = _export_player_logs(hitter_result.logs, players, matchups)

    counts = {
        **validation.counts,
        "export_player_log_hitters": len(export_logs),
        "export_player_log_rows": sum(len(rows) for rows in export_logs.values()),
        "games_covered_hitter": len({(log.player_id, log.game_date) for log in hitter_result.logs}),
        "games_covered_pitcher": len(
            {(log.player_id, log.game_date, log.appearance_type) for log in pitcher_result.logs}
        ),
    }

    warnings = _dedupe(hitter_result.warnings + pitcher_result.warnings + validation.warnings)
    if validation.errors:
        warnings.append("player_logs validation reported relationship errors")

    return PlayerLogsLayerResult(
        hitter_logs=hitter_result.logs,
        pitcher_logs=pitcher_result.logs,
        export_player_logs=export_logs or None,
        warnings=warnings,
        validation=validation,
        counts=counts,
    )


def _export_player_logs(
    hitter_logs: list[HitterGameLog],
    players: list[ExportPlayer],
    matchups: list[HitterRow],
) -> dict[str, list[GameLogEntry]]:
    """Map internal hitter logs to export contract keyed by matchup hitter name."""
    name_by_id: dict[int, str] = {}
    for player in players:
        name_by_id[player.player_id] = player.full_name

    matchup_names = {row.hitter for row in matchups}
    lower_matchup = {name.lower(): name for name in matchup_names}

    by_name: dict[str, list[GameLogEntry]] = {}
    for log in hitter_logs:
        name = name_by_id.get(log.player_id)
        if not name:
            continue
        export_name = name
        if name not in matchup_names:
            export_name = lower_matchup.get(name.lower(), name)
        by_name.setdefault(export_name, []).append(hitter_log_to_export_entry(log))

    for name, entries in by_name.items():
        entries.sort(key=lambda row: row.date, reverse=True)
        by_name[name] = entries

    return by_name


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
