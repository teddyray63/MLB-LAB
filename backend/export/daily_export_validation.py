"""Cross-field validation for daily export JSON."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from pydantic import ValidationError

from backend.export.daily_export_models import (
    DAILY_EXPORT_SCHEMA_VERSION,
    PLAY_CATEGORIES,
    DailyExport,
    FilterSupportEntry,
    FilterSupportMetadata,
    HitterRow,
    parse_daily_export,
)

REQUIRED_TOP_LEVEL_KEYS = frozenset(
    {
        "date",
        "games",
        "game_details",
        "matchups",
        "top_plays",
        "category_boards",
    }
)

OPTIONAL_TOP_LEVEL_KEYS = frozenset(
    {
        "export_meta",
        "schema_version",
        "player_logs",
        "batted_balls",
        "batted_ball_profiles",
        "player_day_night_splits",
        "player_zone_heatmaps",
    }
)

KNOWN_TOP_LEVEL_KEYS = REQUIRED_TOP_LEVEL_KEYS | OPTIONAL_TOP_LEVEL_KEYS


@dataclass
class ValidationReport:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    counts: dict[str, int | float | str] = field(default_factory=dict)
    filter_support: FilterSupportMetadata | None = None

    @property
    def all_warnings(self) -> list[str]:
        export_warnings = self.counts.get("export_meta_warnings")
        combined = list(self.warnings)
        if isinstance(export_warnings, list):
            combined.extend(export_warnings)
        return combined


def _parse_iso_timestamp(value: str) -> datetime | None:
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed


def _game_pk_set(games: list) -> set[int]:
    return {game.game_pk for game in games if game.game_pk is not None}


def _matchup_hitter_names(matchups: list[HitterRow]) -> set[str]:
    return {row.hitter for row in matchups}


def build_filter_support_metadata(export: DailyExport) -> FilterSupportMetadata:
    """Mirror web-dashboard/src/lib/filterSupport.ts support matrix."""
    matchup_hitters = _matchup_hitter_names(export.matchups)
    player_logs = export.player_logs or {}
    log_hitters = set(player_logs.keys())

    def has_logs_for_any_matchup_hitter() -> bool:
        if not log_hitters:
            return False
        lower_map = {name.lower(): name for name in log_hitters}
        for hitter in matchup_hitters:
            if hitter in log_hitters or hitter.lower() in lower_map:
                return True
        return False

    has_any_logs = has_logs_for_any_matchup_hitter()

    def timeframe_entry(key: str) -> FilterSupportEntry:
        if key == "season":
            return FilterSupportEntry(supported=True, source="export")
        if has_any_logs:
            return FilterSupportEntry(supported=True, source="client-slice")
        if key == "l20":
            return FilterSupportEntry(
                supported=False,
                source="unsupported",
                reason="Game logs available for top-board hitters only (Phase 0)",
            )
        return FilterSupportEntry(
            supported=False,
            source="unsupported",
            reason="Requires game log data for selected player",
        )

    def situation_entry(key: str) -> FilterSupportEntry:
        if key in {"overall", "day", "night", "vlhp", "vrhp"}:
            return FilterSupportEntry(supported=True, source="export")
        return FilterSupportEntry(
            supported=False,
            source="unsupported",
            reason="Hitter home/away splits not in export — pitcher panels only",
        )

    return FilterSupportMetadata(
        timeframe={key: timeframe_entry(key) for key in ("season", "l20", "l15", "l10", "l7", "l5")},
        situation={
            key: situation_entry(key)
            for key in ("overall", "home", "away", "day", "night", "vlhp", "vrhp")
        },
        pitch_type=FilterSupportEntry(supported=True, source="export"),
    )


def validate_export(export: DailyExport) -> ValidationReport:
    errors: list[str] = []
    warnings: list[str] = []
    counts: dict[str, int | float | str] = {}

    counts["date"] = export.date
    counts["games"] = len(export.games)
    counts["game_details"] = len(export.game_details)
    counts["matchups"] = len(export.matchups)
    counts["unique_matchup_hitters"] = len(_matchup_hitter_names(export.matchups))
    counts["player_logs"] = len(export.player_logs or {})
    counts["player_day_night_splits"] = len(export.player_day_night_splits or {})
    counts["player_zone_heatmaps"] = len(export.player_zone_heatmaps or {})
    counts["batted_balls"] = len(export.batted_balls or {})
    counts["batted_ball_profiles"] = len(export.batted_ball_profiles or {})

    for category in PLAY_CATEGORIES:
        top_rows = getattr(export.top_plays, category)
        board_rows = getattr(export.category_boards, category)
        counts[f"top_plays.{category}"] = len(top_rows)
        counts[f"category_boards.{category}"] = len(board_rows)
        if len(board_rows) > 20:
            errors.append(f"category_boards.{category} has {len(board_rows)} rows (max 20)")

    if export.schema_version is not None and str(export.schema_version) != str(
        DAILY_EXPORT_SCHEMA_VERSION
    ):
        warnings.append(
            "schema_version "
            f"{export.schema_version!r} differs from exporter schema "
            f"{DAILY_EXPORT_SCHEMA_VERSION}"
        )
    elif export.schema_version is None:
        warnings.append(
            f"schema_version missing — new exports should set {DAILY_EXPORT_SCHEMA_VERSION}"
        )

    meta = export.export_meta
    if meta is None:
        warnings.append("export_meta missing — Data Status workspace expects metadata")
    else:
        counts["export_meta.runner_version"] = meta.runner_version
        counts["export_meta.statcast_window"] = f"{meta.statcast_start} – {meta.statcast_end}"
        counts["export_meta_warnings"] = list(meta.warnings)

        generated = _parse_iso_timestamp(meta.generated_at)
        if generated is None:
            errors.append(f"export_meta.generated_at is not a valid ISO timestamp: {meta.generated_at!r}")
        else:
            counts["export_meta.generated_at"] = meta.generated_at

        if not meta.statcast_start or not meta.statcast_end:
            errors.append("export_meta.statcast_start and statcast_end are required")

    game_pks = _game_pk_set(export.games)
    games_with_pk = sum(1 for game in export.games if game.game_pk is not None)
    counts["games_with_game_pk"] = games_with_pk
    if games_with_pk < len(export.games):
        warnings.append(
            f"{len(export.games) - games_with_pk}/{len(export.games)} games missing game_pk"
        )

    pk_counts: dict[int, int] = {}
    for game in export.games:
        if game.game_pk is None:
            continue
        pk_counts[game.game_pk] = pk_counts.get(game.game_pk, 0) + 1

    duplicate_pks = sorted(pk for pk, count in pk_counts.items() if count > 1)
    counts["duplicate_game_pk_count"] = len(duplicate_pks)
    for pk in duplicate_pks:
        warnings.append(f"Duplicate game_pk {pk} appears {pk_counts[pk]} times in games[]")

    detail_pks = {detail.game_pk for detail in export.game_details if detail.game_pk is not None}
    for pk in sorted(detail_pks - game_pks):
        errors.append(f"game_details references game_pk {pk} not present in games[]")

    for index, detail in enumerate(export.game_details):
        if detail.game_pk is None:
            warnings.append(f"game_details[{index}] missing game_pk ({detail.game_id})")

    matchup_missing_pk = sum(1 for row in export.matchups if row.game_pk is None)
    counts["matchups_missing_game_pk"] = matchup_missing_pk
    if matchup_missing_pk:
        warnings.append(
            f"{matchup_missing_pk}/{len(export.matchups)} matchup rows missing game_pk"
        )

    for index, row in enumerate(export.matchups):
        if row.game_pk is not None and row.game_pk not in game_pks:
            errors.append(
                f"matchups[{index}] game_pk {row.game_pk} not found in games[] "
                f"({row.hitter})"
            )

    game_id_by_pk = {game.game_pk: game.game_id for game in export.games if game.game_pk is not None}
    for category in PLAY_CATEGORIES:
        for index, play in enumerate(getattr(export.top_plays, category)):
            if play.game_pk is not None and play.game_pk not in game_pks:
                errors.append(
                    f"top_plays.{category}[{index}] game_pk {play.game_pk} not in games[]"
                )
            elif play.game_pk is not None:
                expected = game_id_by_pk.get(play.game_pk)
                if expected and play.game != expected:
                    warnings.append(
                        f"top_plays.{category}[{index}] game string {play.game!r} "
                        f"does not match games[] game_id {expected!r} for pk {play.game_pk}"
                    )

    lineup_warnings = _validate_lineup_relationships(export, game_pks)
    warnings.extend(lineup_warnings)

    player_map_warnings = _validate_player_map_relationships(export)
    warnings.extend(player_map_warnings)

    filter_support = build_filter_support_metadata(export)

    return ValidationReport(
        valid=not errors,
        errors=errors,
        warnings=warnings,
        counts=counts,
        filter_support=filter_support,
    )


def _validate_lineup_relationships(export: DailyExport, game_pks: set[int]) -> list[str]:
    warnings: list[str] = []
    matchup_index = {
        (row.game_pk, row.team, row.hitter)
        for row in export.matchups
        if row.game_pk is not None
    }

    for detail in export.game_details:
        pool_hitters = {h.hitter for h in detail.away_hitters} | {h.hitter for h in detail.home_hitters}
        for side, lineup, team in (
            ("away", detail.away_lineup, detail.away_team),
            ("home", detail.home_lineup, detail.home_team),
        ):
            if not lineup:
                continue
            for batter in lineup:
                if batter.hitter not in pool_hitters:
                    warnings.append(
                        f"{detail.game_id} {side}_lineup batter {batter.hitter!r} "
                        "not found in team hitter pool"
                    )
                key = (detail.game_pk, team, batter.hitter)
                if detail.game_pk is not None and key not in matchup_index:
                    warnings.append(
                        f"{detail.game_id} {side}_lineup batter {batter.hitter!r} "
                        "has no matchup row for this game/team"
                    )
        if detail.game_pk is not None and detail.game_pk not in game_pks:
            warnings.append(f"game_details game_pk {detail.game_pk} missing from games[]")
    return warnings


def _validate_player_map_relationships(export: DailyExport) -> list[str]:
    warnings: list[str] = []
    matchup_hitters = _matchup_hitter_names(export.matchups)
    lower_matchup = {name.lower() for name in matchup_hitters}

    def check_map(name: str, keys: set[str], policy: str) -> None:
        extras = sorted(
            key
            for key in keys
            if key not in matchup_hitters and key.lower() not in lower_matchup
        )
        if extras:
            warnings.append(
                f"{name} contains {len(extras)} hitters outside matchups[] "
                f"({policy}); e.g. {extras[0]!r}"
            )

    if export.player_logs:
        check_map(
            "player_logs",
            set(export.player_logs.keys()),
            "expected subset of top-board hitters",
        )
    if export.batted_balls:
        check_map(
            "batted_balls",
            set(export.batted_balls.keys()),
            "expected subset of top-board hitters",
        )
    if export.batted_ball_profiles:
        check_map(
            "batted_ball_profiles",
            set(export.batted_ball_profiles.keys()),
            "expected subset of top-board hitters",
        )

    for map_name, data in (
        ("player_day_night_splits", export.player_day_night_splits),
        ("player_zone_heatmaps", export.player_zone_heatmaps),
    ):
        if not data:
            continue
        missing = sorted(
            hitter
            for hitter in matchup_hitters
            if hitter not in data and hitter.lower() not in {k.lower() for k in data}
        )
        if missing:
            warnings.append(
                f"{map_name} missing {len(missing)}/{len(matchup_hitters)} matchup hitters"
            )

    return warnings


def validate_export_dict(data: dict[str, Any]) -> ValidationReport:
    """Validate raw export JSON: required keys, Pydantic schema, and cross-field rules."""
    errors: list[str] = []

    if not isinstance(data, dict):
        return ValidationReport(valid=False, errors=["Export root must be a JSON object"])

    unknown_keys = sorted(set(data.keys()) - KNOWN_TOP_LEVEL_KEYS)
    if unknown_keys:
        warnings = [f"Unknown top-level keys (ignored by schema): {', '.join(unknown_keys)}"]
    else:
        warnings = []

    missing_required = sorted(REQUIRED_TOP_LEVEL_KEYS - set(data.keys()))
    if missing_required:
        errors.extend(f"Missing required top-level key: {key}" for key in missing_required)
        return ValidationReport(valid=False, errors=errors, warnings=warnings)

    try:
        export = parse_daily_export(data)
    except ValidationError as exc:
        for issue in exc.errors():
            location = ".".join(str(part) for part in issue.get("loc", ()))
            message = issue.get("msg", "validation error")
            errors.append(f"{location}: {message}" if location else message)
        return ValidationReport(valid=False, errors=errors, warnings=warnings)

    report = validate_export(export)
    report.warnings = warnings + report.warnings
    if errors:
        report.errors = errors + report.errors
        report.valid = False
    return report
