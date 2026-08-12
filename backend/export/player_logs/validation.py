"""Relationship validation for player game logs."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from backend.export.daily_export_models import Game
from backend.export.identity_models import ExportPlayer, ExportTeam
from backend.export.player_logs.models import HitterGameLog, PitcherGameLog


@dataclass
class PlayerLogsValidationReport:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    counts: dict[str, int | float | str] = field(default_factory=dict)
    coverage: dict[str, float | int | str] = field(default_factory=dict)


def _valid_date(value: str) -> bool:
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_hitter_logs(
    logs: list[HitterGameLog],
    *,
    players: list[ExportPlayer],
    teams: list[ExportTeam],
    games: list[Game],
    known_player_ids: set[int] | None = None,
) -> PlayerLogsValidationReport:
    errors: list[str] = []
    warnings: list[str] = []

    player_ids = known_player_ids or {player.player_id for player in players}
    team_ids = {team.team_id for team in teams}
    slate_game_pks = {game.game_pk for game in games if game.game_pk is not None}

    seen: set[tuple[int, int | None, str]] = set()
    for index, log in enumerate(logs):
        prefix = f"hitter_logs[{index}]"

        if log.player_id not in player_ids:
            errors.append(f"{prefix} player_id {log.player_id} not in players graph")

        if not _valid_date(log.game_date):
            errors.append(f"{prefix} invalid game_date {log.game_date!r}")

        if log.team_id is not None and log.team_id not in team_ids:
            errors.append(f"{prefix} team_id {log.team_id} not in teams graph")

        if log.opponent_team_id is not None and log.opponent_team_id not in team_ids:
            errors.append(f"{prefix} opponent_team_id {log.opponent_team_id} not in teams graph")

        if log.game_pk is not None and log.game_pk in slate_game_pks:
            player_on_slate = any(
                player.player_id == log.player_id and player.game_pk == log.game_pk
                for player in players
            )
            if not player_on_slate:
                errors.append(
                    f"{prefix} player_id {log.player_id} not attached to slate game_pk {log.game_pk}"
                )

        dup_key = (log.player_id, log.game_pk, log.game_date)
        if dup_key in seen:
            errors.append(f"{prefix} duplicate player_id + game_pk + game_date row")
        seen.add(dup_key)

        if log.lineup_slot is not None and not (1 <= log.lineup_slot <= 9):
            errors.append(f"{prefix} lineup_slot {log.lineup_slot} out of range 1-9")

        for field_name in ("pa", "ab", "h", "hr", "bb", "so", "tb", "singles", "barrels"):
            value = getattr(log, field_name if field_name != "tb" else "total_bases", None)
            if value is not None and value < 0:
                errors.append(f"{prefix} negative {field_name}: {value}")

        for rate_name in ("avg", "obp", "slg", "ops"):
            rate = getattr(log, rate_name)
            if rate is not None and (rate < 0 or rate > 4):
                warnings.append(f"{prefix} {rate_name}={rate} outside expected range")

        if log.avg_ev is not None and (log.avg_ev < 0 or log.avg_ev > 130):
            warnings.append(f"{prefix} avg_ev={log.avg_ev} outside expected range")

        if log.pa is not None and log.h is not None and log.h > log.pa:
            errors.append(f"{prefix} hits ({log.h}) exceed PA ({log.pa})")

    counts = {
        "hitter_logs": len(logs),
        "unique_hitter_log_players": len({log.player_id for log in logs}),
        "hitter_logs_with_game_pk": sum(1 for log in logs if log.game_pk is not None),
    }

    return PlayerLogsValidationReport(
        valid=not errors,
        errors=errors,
        warnings=warnings,
        counts=counts,
    )


def validate_pitcher_logs(
    logs: list[PitcherGameLog],
    *,
    players: list[ExportPlayer],
    teams: list[ExportTeam],
    games: list[Game],
    known_player_ids: set[int] | None = None,
) -> PlayerLogsValidationReport:
    errors: list[str] = []
    warnings: list[str] = []

    player_ids = known_player_ids or {player.player_id for player in players}
    team_ids = {team.team_id for team in teams}
    slate_game_pks = {game.game_pk for game in games if game.game_pk is not None}

    seen: set[tuple[int, int | None, str, str | None]] = set()
    for index, log in enumerate(logs):
        prefix = f"pitcher_logs[{index}]"

        if log.player_id not in player_ids:
            errors.append(f"{prefix} player_id {log.player_id} not in players graph")

        if not _valid_date(log.game_date):
            errors.append(f"{prefix} invalid game_date {log.game_date!r}")

        if log.team_id is not None and log.team_id not in team_ids:
            errors.append(f"{prefix} team_id {log.team_id} not in teams graph")

        if log.opponent_team_id is not None and log.opponent_team_id not in team_ids:
            errors.append(f"{prefix} opponent_team_id {log.opponent_team_id} not in teams graph")

        if log.game_pk is not None and log.game_pk in slate_game_pks:
            player_on_slate = any(
                player.player_id == log.player_id and player.game_pk == log.game_pk
                for player in players
            )
            if not player_on_slate and log.team_id is not None:
                team_on_slate = any(
                    team.team_id == log.team_id and team.game_pk == log.game_pk for team in teams
                )
                if not team_on_slate:
                    errors.append(
                        f"{prefix} pitcher team_id {log.team_id} not attached to slate game_pk {log.game_pk}"
                    )

        appearance = log.appearance_type or "unknown"
        dup_key = (log.player_id, log.game_pk, log.game_date, appearance)
        if dup_key in seen:
            errors.append(f"{prefix} duplicate player_id + game_pk + game_date + appearance_type row")
        seen.add(dup_key)

        if log.innings_pitched is not None and log.innings_pitched_decimal is None:
            errors.append(f"{prefix} invalid innings_pitched format {log.innings_pitched!r}")

        for count_name in (
            "batters_faced",
            "hits",
            "runs",
            "earned_runs",
            "walks",
            "strikeouts",
            "home_runs",
            "pitches",
            "strikes",
        ):
            value = getattr(log, count_name)
            if value is not None and value < 0:
                errors.append(f"{prefix} negative {count_name}: {value}")

        if log.innings_pitched_decimal is not None and log.innings_pitched_decimal < 0:
            errors.append(f"{prefix} negative innings_pitched_decimal")

        if log.is_start is True and log.is_relief is True:
            errors.append(f"{prefix} cannot be both start and relief")

        if log.pitches is None and log.innings_pitched is None and log.batters_faced is None:
            warnings.append(f"{prefix} sparse pitching line — limited source coverage")

    counts = {
        "pitcher_logs": len(logs),
        "unique_pitcher_log_players": len({log.player_id for log in logs}),
        "pitcher_starts": sum(1 for log in logs if log.is_start),
        "pitcher_relief": sum(1 for log in logs if log.is_relief),
    }

    return PlayerLogsValidationReport(
        valid=not errors,
        errors=errors,
        warnings=warnings,
        counts=counts,
    )


def validate_player_logs_bundle(
    *,
    hitter_logs: list[HitterGameLog],
    pitcher_logs: list[PitcherGameLog],
    players: list[ExportPlayer],
    teams: list[ExportTeam],
    games: list[Game],
    matchup_hitter_names: set[str] | None = None,
    builder_warnings: list[str] | None = None,
) -> PlayerLogsValidationReport:
    hitter_report = validate_hitter_logs(
        hitter_logs,
        players=players,
        teams=teams,
        games=games,
    )
    pitcher_report = validate_pitcher_logs(
        pitcher_logs,
        players=players,
        teams=teams,
        games=games,
    )

    errors = hitter_report.errors + pitcher_report.errors
    warnings = list(builder_warnings or []) + hitter_report.warnings + pitcher_report.warnings

    counts = {**hitter_report.counts, **pitcher_report.counts}
    coverage = {
        "hitter_log_games": len({(log.player_id, log.game_date) for log in hitter_logs}),
        "pitcher_log_games": len({(log.player_id, log.game_date, log.appearance_type) for log in pitcher_logs}),
    }

    if matchup_hitter_names is not None and hitter_logs:
        id_to_name = {player.player_id: player.full_name for player in players}
        export_names = {id_to_name.get(log.player_id, str(log.player_id)) for log in hitter_logs}
        lower_matchup = {name.lower() for name in matchup_hitter_names}
        extras = sorted(
            name
            for name in export_names
            if name not in matchup_hitter_names and name.lower() not in lower_matchup
        )
        if extras:
            warnings.append(
                f"player_logs export will include {len(extras)} hitters outside matchups[]; e.g. {extras[0]!r}"
            )

    return PlayerLogsValidationReport(
        valid=not errors,
        errors=errors,
        warnings=warnings,
        counts=counts,
        coverage=coverage,
    )
