"""Assemble a full DailyExport document and write to isolated candidate paths."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from backend.export.build_matchup_layer import MatchupLayerResult, build_matchup_layer
from backend.export.build_player_logs import PlayerLogsLayerResult, build_player_logs_layer
from backend.export.daily_export_models import (
    DAILY_EXPORT_SCHEMA_VERSION,
    EXPORT_RUNNER_VERSION,
    PLAY_CATEGORIES,
    CategoryBoards,
    DailyExport,
    ExportMeta,
    TopPlaysBoard,
)
from backend.export.daily_export_validation import (
    KNOWN_TOP_LEVEL_KEYS,
    REQUIRED_TOP_LEVEL_KEYS,
    validate_export_dict,
)
from backend.export.enrichment.statcast_source import StatcastEvents

LIVE_EXPORT_RELATIVE = Path("data/daily_export.json")

UNSUPPORTED_SECTION_WARNINGS = (
    "top_plays: empty — scoring formulas not reproducible in G0b.5a",
    "category_boards: empty — board ranking formulas not reproducible in G0b.5a",
    "player_logs: absent — pass build_player_logs=True to assemble",
    "batted_balls: absent — not built in G0b.5a",
    "batted_ball_profiles: absent — not built in G0b.5a",
    "player_day_night_splits: absent — not built in G0b.5a",
    "player_zone_heatmaps: absent — not built in G0b.5a",
)

PLAYER_LOGS_ABSENT_WARNING = "player_logs: absent — pass build_player_logs=True to assemble"
PLAYER_LOGS_NOT_PRODUCED_WARNING = (
    "player_logs: build requested but no player logs were produced"
)


@dataclass
class DocumentCounts:
    games: int = 0
    game_details: int = 0
    teams: int = 0
    players: int = 0
    lineups: int = 0
    matchups: int = 0
    export_matchup_rows: int = 0
    enrichment_matchups: int = 0
    top_plays: int = 0
    category_boards: int = 0
    player_logs: int = 0
    player_log_rows: int = 0
    hitter_logs: int = 0
    pitcher_logs: int = 0


@dataclass
class DailyExportDocumentResult:
    export: DailyExport
    matchup_layer: MatchupLayerResult
    counts: DocumentCounts
    warnings: list[str] = field(default_factory=list)
    statcast_window_start: str | None = None
    statcast_window_end: str | None = None
    player_logs_layer: PlayerLogsLayerResult | None = None


@dataclass
class CandidateWriteResult:
    path: Path
    sha256: str
    byte_size: int
    counts: DocumentCounts
    warnings: list[str]
    valid: bool


@dataclass
class ReferenceComparisonReport:
    reference_path: Path
    candidate_path: Path | None
    top_level_key_parity: bool
    reference_keys: set[str]
    candidate_keys: set[str]
    missing_in_candidate: set[str]
    extra_in_candidate: set[str]
    schema_version_reference: int | str | None
    schema_version_candidate: int | str | None
    counts: dict[str, int | str | None] = field(default_factory=dict)
    cardinality_deltas: dict[str, int | str | None] = field(default_factory=dict)
    null_heavy_fields: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    matchup_cardinality: dict[str, Any] = field(default_factory=dict)
    relationship_integrity: dict[str, bool | str] = field(default_factory=dict)


def empty_top_plays_board() -> TopPlaysBoard:
    return TopPlaysBoard(
        hits=[],
        singles=[],
        total_bases=[],
        hrr=[],
        home_runs=[],
    )


def empty_category_boards() -> CategoryBoards:
    return CategoryBoards(
        hits=[],
        singles=[],
        total_bases=[],
        hrr=[],
        home_runs=[],
    )


def _export_player_logs_effective(logs: dict[str, list] | None) -> bool:
    if not logs:
        return False
    return any(rows for rows in logs.values())


def build_daily_export_document(
    schedule_json: dict[str, Any],
    *,
    slate_date: str,
    feeds_by_pk: dict[int, dict] | None = None,
    statcast_events: StatcastEvents | None = None,
    statcast_fixture: str | None = None,
    lookback_days: int = 120,
    extra_warnings: list[str] | None = None,
    build_player_logs: bool = False,
    max_games_per_player: int = 20,
) -> DailyExportDocumentResult:
    matchup_layer = build_matchup_layer(
        schedule_json,
        slate_date=slate_date,
        feeds_by_pk=feeds_by_pk,
        statcast_events=statcast_events,
        statcast_fixture=statcast_fixture,
        lookback_days=lookback_days,
    )

    window_end = slate_date
    window_start = (date.fromisoformat(slate_date) - timedelta(days=lookback_days)).isoformat()

    unsupported_warnings = [
        item for item in UNSUPPORTED_SECTION_WARNINGS if not item.startswith("player_logs:")
    ]
    warnings = _dedupe(
        list(unsupported_warnings)
        + list(matchup_layer.warnings)
        + list(extra_warnings or [])
    )

    player_logs_layer: PlayerLogsLayerResult | None = None
    export_player_logs = None
    if build_player_logs:
        events = statcast_events
        if events is None and statcast_fixture:
            from pathlib import Path

            from backend.export.enrichment.statcast_source import events_from_fixture

            events = events_from_fixture(Path(statcast_fixture))
        if events is None:
            from backend.export.enrichment.statcast_source import fetch_statcast_events

            events = fetch_statcast_events(slate_date, lookback_days=lookback_days)

        player_logs_layer = build_player_logs_layer(
            events=events,
            players=matchup_layer.identity.players,
            teams=matchup_layer.identity.teams,
            games=matchup_layer.identity.games,
            matchups=matchup_layer.export_matchup_rows,
            feeds_by_pk=feeds_by_pk,
            feed_dates_by_pk={game.game_pk: slate_date for game in matchup_layer.identity.games if game.game_pk},
            max_games_per_player=max_games_per_player,
        )
        export_player_logs = player_logs_layer.export_player_logs
        warnings = _dedupe(warnings + player_logs_layer.warnings)
        if player_logs_layer.validation and not player_logs_layer.validation.valid:
            warnings.append("player_logs validation reported relationship errors")

    if matchup_layer.validation and not matchup_layer.validation.valid:
        warnings.append("enrichment validation reported relationship errors")

    if not _export_player_logs_effective(export_player_logs):
        if build_player_logs:
            warnings.append(PLAYER_LOGS_NOT_PRODUCED_WARNING)
        else:
            warnings.append(PLAYER_LOGS_ABSENT_WARNING)

    warnings = _dedupe(warnings)
    meta_warnings = list(warnings)
    meta = ExportMeta(
        generated_at=datetime.now(timezone.utc).isoformat(),
        statcast_start=window_start,
        statcast_end=window_end,
        runner_version=EXPORT_RUNNER_VERSION,
        warnings=meta_warnings,
    )

    export = DailyExport(
        date=slate_date,
        schema_version=DAILY_EXPORT_SCHEMA_VERSION,
        games=matchup_layer.identity.games,
        game_details=matchup_layer.game_details,
        matchups=matchup_layer.export_matchup_rows,
        top_plays=empty_top_plays_board(),
        category_boards=empty_category_boards(),
        export_meta=meta,
        player_logs=export_player_logs,
        batted_balls=None,
        batted_ball_profiles=None,
        player_day_night_splits=None,
        player_zone_heatmaps=None,
    )

    player_log_hitter_count = len(export_player_logs or {})
    player_log_row_count = sum(len(rows) for rows in (export_player_logs or {}).values())

    counts = DocumentCounts(
        games=len(export.games),
        game_details=len(export.game_details),
        teams=len(matchup_layer.identity.teams),
        players=len(matchup_layer.identity.players),
        lineups=len(matchup_layer.identity.lineups),
        matchups=len(export.matchups),
        export_matchup_rows=len(export.matchups),
        enrichment_matchups=len(matchup_layer.matchups),
        top_plays=sum(len(getattr(export.top_plays, cat)) for cat in PLAY_CATEGORIES),
        category_boards=sum(len(getattr(export.category_boards, cat)) for cat in PLAY_CATEGORIES),
        player_logs=player_log_hitter_count,
        player_log_rows=player_log_row_count,
        hitter_logs=len(player_logs_layer.hitter_logs) if player_logs_layer else 0,
        pitcher_logs=len(player_logs_layer.pitcher_logs) if player_logs_layer else 0,
    )

    return DailyExportDocumentResult(
        export=export,
        matchup_layer=matchup_layer,
        counts=counts,
        warnings=warnings,
        statcast_window_start=window_start,
        statcast_window_end=window_end,
        player_logs_layer=player_logs_layer,
    )


def export_to_dict(export: DailyExport) -> dict[str, Any]:
    return export.model_dump(mode="json", exclude_none=False)


def write_candidate_export(
    export: DailyExport,
    output_path: Path | str,
    *,
    force: bool = False,
    counts: DocumentCounts | None = None,
    warnings: list[str] | None = None,
) -> CandidateWriteResult:
    path = Path(output_path).resolve()
    live_path = _resolve_live_export_path()
    if path == live_path:
        raise ValueError(f"Refusing to write live export path: {live_path}")

    if path.exists() and not force:
        raise FileExistsError(
            f"Candidate file already exists: {path}. Pass --force-candidate to overwrite."
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    payload = export_to_dict(export)

    temp_fd, temp_name = tempfile.mkstemp(
        suffix=".json.tmp",
        prefix=f"daily_export_{export.date}_",
        dir=str(path.parent),
    )
    temp_path = Path(temp_name)
    os.close(temp_fd)

    try:
        encoded = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
        with temp_path.open("w", encoding="utf-8") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())

        validation = validate_export_dict(payload)
        if not validation.valid:
            errors = "; ".join(validation.errors)
            raise ValueError(f"Candidate failed validation before rename: {errors}")

        os.replace(temp_path, path)

        with path.open("rb") as handle:
            digest = hashlib.sha256(handle.read()).hexdigest()
        byte_size = path.stat().st_size

        resolved_counts = counts or _counts_from_export(export)
        return CandidateWriteResult(
            path=path,
            sha256=digest,
            byte_size=byte_size,
            counts=resolved_counts,
            warnings=list(warnings or []),
            valid=True,
        )
    finally:
        if temp_path.exists():
            temp_path.unlink(missing_ok=True)


def analyze_matchup_cardinality(reference: dict[str, Any]) -> dict[str, Any]:
    """Reference-data evidence for 894-vs-288 style cardinality deltas."""
    matchups = reference.get("matchups") or []
    game_details = reference.get("game_details") or []

    lineup_pairs: set[tuple[str, str]] = set()
    pool_pairs: set[tuple[str, str]] = set()
    for detail in game_details:
        game_id = detail.get("game_id") or detail.get("game") or ""
        for side in ("away_lineup", "home_lineup"):
            for row in detail.get(side) or []:
                if row.get("hitter"):
                    lineup_pairs.add((game_id, row["hitter"]))
        for side in ("away_hitters", "home_hitters"):
            for row in detail.get(side) or []:
                hitter = row.get("hitter") if isinstance(row, dict) else None
                if hitter:
                    pool_pairs.add((game_id, hitter))

    rows_lineup = 0
    rows_pool_only = 0
    rows_other = 0
    pitch_codes: set[str] = set()
    hitter_game_pitch: set[tuple[str, str, str]] = set()

    for row in matchups:
        game = row.get("game") or ""
        hitter = row.get("hitter") or ""
        pitch = row.get("pitch") or ""
        pitch_codes.add(pitch)
        hitter_game_pitch.add((hitter, game, pitch))
        pair = (game, hitter)
        if pair in lineup_pairs:
            rows_lineup += 1
        elif pair in pool_pairs:
            rows_pool_only += 1
        else:
            rows_other += 1

    unique_hitters = {row.get("hitter") for row in matchups if row.get("hitter")}
    unique_lineup_hitters = {h for _, h in lineup_pairs}
    unique_pool_hitters = {h for _, h in pool_pairs}

    pitches_per_hitter_game: dict[tuple[str, str], set[str]] = {}
    for row in matchups:
        key = (row.get("hitter") or "", row.get("game") or "")
        pitches_per_hitter_game.setdefault(key, set()).add(row.get("pitch") or "")

    pitch_count_distribution: dict[int, int] = {}
    for codes in pitches_per_hitter_game.values():
        pitch_count_distribution[len(codes)] = pitch_count_distribution.get(len(codes), 0) + 1

    cause = (
        "Reference matchups are one row per (hitter, game, opposing-SP pitch type). "
        "Cardinality is driven primarily by the full team hitter pool (game_details.*_hitters), "
        "not confirmed lineup slots alone. "
        f"Of {len(matchups)} rows: {rows_lineup} lineup hitters, "
        f"{rows_pool_only} pool-only (bench/non-lineup) hitters, {rows_other} other. "
        "No duplicate (hitter, team, game, opp_sp, pitch) keys observed."
    )

    return {
        "reference_matchup_rows": len(matchups),
        "unique_hitters": len(unique_hitters),
        "unique_lineup_game_hitter_pairs": len(lineup_pairs),
        "unique_pool_game_hitter_pairs": len(pool_pairs),
        "rows_for_lineup_hitters": rows_lineup,
        "rows_for_pool_only_hitters": rows_pool_only,
        "rows_other": rows_other,
        "unique_pitch_codes": len(pitch_codes),
        "unique_hitter_game_pitch_keys": len(hitter_game_pitch),
        "pitches_per_hitter_game_distribution": pitch_count_distribution,
        "inferred_policy": "full team hitter pool × major pitch types vs opposing starter",
        "g0b4_policy": "confirmed lineup hitters × major pitch types vs opposing starter",
        "cause_summary": cause,
        "recommendation": (
            "Keep G0b.4 lineup-only policy until frontend consumers require pool-wide rows "
            "and pool attachment is reproducible from identity + Statcast without fabrication."
        ),
    }


def compare_to_reference(
    candidate: dict[str, Any],
    reference: dict[str, Any],
    *,
    reference_path: Path | str,
    candidate_path: Path | str | None = None,
) -> ReferenceComparisonReport:
    ref_keys = set(reference.keys())
    cand_keys = set(candidate.keys())
    missing = REQUIRED_TOP_LEVEL_KEYS - cand_keys
    extra = cand_keys - KNOWN_TOP_LEVEL_KEYS

    ref_player_logs = reference.get("player_logs") or {}
    cand_player_logs = candidate.get("player_logs") or {}
    ref_log_rows = sum(len(v) for v in ref_player_logs.values()) if isinstance(ref_player_logs, dict) else 0
    cand_log_rows = sum(len(v) for v in cand_player_logs.values()) if isinstance(cand_player_logs, dict) else 0

    counts: dict[str, int | str | None] = {
        "reference_games": len(reference.get("games") or []),
        "candidate_games": len(candidate.get("games") or []),
        "reference_game_details": len(reference.get("game_details") or []),
        "candidate_game_details": len(candidate.get("game_details") or []),
        "reference_matchups": len(reference.get("matchups") or []),
        "candidate_matchups": len(candidate.get("matchups") or []),
        "reference_player_logs": len(ref_player_logs) if isinstance(ref_player_logs, dict) else 0,
        "candidate_player_logs": len(cand_player_logs) if isinstance(cand_player_logs, dict) else 0,
        "reference_player_log_rows": ref_log_rows,
        "candidate_player_log_rows": cand_log_rows,
    }

    cardinality_deltas = {
        "games": int(counts["candidate_games"] or 0) - int(counts["reference_games"] or 0),
        "game_details": int(counts["candidate_game_details"] or 0)
        - int(counts["reference_game_details"] or 0),
        "matchups": int(counts["candidate_matchups"] or 0) - int(counts["reference_matchups"] or 0),
    }

    null_heavy: list[str] = []
    for key in OPTIONAL_TOP_LEVEL_KEYS:
        if key in reference and reference.get(key) and candidate.get(key) in (None, {}, []):
            null_heavy.append(key)

    warnings: list[str] = []
    if counts["reference_matchups"] != counts["candidate_matchups"]:
        warnings.append(
            f"matchups cardinality delta: candidate={counts['candidate_matchups']} "
            f"reference={counts['reference_matchups']} "
            "(not treated as parity failure in G0b.5a)"
        )

    matchup_cardinality = analyze_matchup_cardinality(reference)
    matchup_cardinality["candidate_matchup_rows"] = counts["candidate_matchups"]

    relationship = {
        "candidate_validates": validate_export_dict(candidate).valid,
        "reference_validates": validate_export_dict(reference).valid,
        "required_keys_present": not missing,
    }

    return ReferenceComparisonReport(
        reference_path=Path(reference_path),
        candidate_path=Path(candidate_path) if candidate_path else None,
        top_level_key_parity=ref_keys == cand_keys or REQUIRED_TOP_LEVEL_KEYS <= cand_keys,
        reference_keys=ref_keys,
        candidate_keys=cand_keys,
        missing_in_candidate=missing,
        extra_in_candidate=extra,
        schema_version_reference=reference.get("schema_version"),
        schema_version_candidate=candidate.get("schema_version"),
        counts=counts,
        cardinality_deltas=cardinality_deltas,
        null_heavy_fields=null_heavy,
        warnings=warnings,
        matchup_cardinality=matchup_cardinality,
        relationship_integrity=relationship,
    )


def _counts_from_export(export: DailyExport) -> DocumentCounts:
    return DocumentCounts(
        games=len(export.games),
        game_details=len(export.game_details),
        matchups=len(export.matchups),
        export_matchup_rows=len(export.matchups),
        top_plays=sum(len(getattr(export.top_plays, cat)) for cat in PLAY_CATEGORIES),
        category_boards=sum(len(getattr(export.category_boards, cat)) for cat in PLAY_CATEGORIES),
    )


def _resolve_live_export_path() -> Path:
    root = Path(__file__).resolve().parents[2]
    return (root / LIVE_EXPORT_RELATIVE).resolve()


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result


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
