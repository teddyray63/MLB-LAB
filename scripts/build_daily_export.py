#!/usr/bin/env python3
"""Dry-run CLI for the daily export pipeline (Phase G0b)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from backend.export.build_daily_export_document import (  # noqa: E402
    compare_to_reference,
    build_daily_export_document,
    write_candidate_export,
)
from backend.export.build_matchup_layer import build_matchup_layer  # noqa: E402
from backend.export.build_identity_layer import build_identity_layer  # noqa: E402
from backend.export.builders.game_details import build_game_details_shell  # noqa: E402
from backend.export.builders.games import build_games_from_schedule_json  # noqa: E402
from backend.export.daily_export_validation import (  # noqa: E402
    ValidationReport,
    validate_export_dict,
    validate_games_shell,
)
from backend.export.mlb_game_feed import fetch_game_feed_json  # noqa: E402
from backend.export.mlb_schedule import fetch_schedule_json, parse_schedule_rows  # noqa: E402
from backend.export.promote_daily_export import (  # noqa: E402
    DEFAULT_BACKUP_DIR,
    DEFAULT_RETENTION_COUNT,
    PromotionStatus,
    promote_candidate,
    rollback_from_backup,
)

DEFAULT_REFERENCE = ROOT / "data" / "daily_export.json"


def _load_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Export file not found: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise SystemExit(f"Expected JSON object in {path}")
    return payload


def _print_report(path: Path | str, report: ValidationReport) -> None:
    print(f"Validated: {path}")
    print(f"Status: {'OK' if report.valid else 'FAILED'}")
    print("")
    print("Counts:")
    for key in sorted(report.counts):
        if key == "export_meta_warnings":
            continue
        print(f"  {key}: {report.counts[key]}")

    export_warnings = report.counts.get("export_meta_warnings")
    if isinstance(export_warnings, list):
        print(f"  export_meta.warnings: {len(export_warnings)}")

    if report.filter_support is not None:
        supported_timeframes = sum(
            1 for entry in report.filter_support.timeframe.values() if entry.supported
        )
        supported_situations = sum(
            1 for entry in report.filter_support.situation.values() if entry.supported
        )
        print("")
        print("Filter support (derived):")
        print(f"  timeframe dimensions supported: {supported_timeframes}/6")
        print(f"  situation dimensions supported: {supported_situations}/7")
        print(
            f"  pitch type supported: {report.filter_support.pitch_type.supported} "
            f"({report.filter_support.pitch_type.source})"
        )

    if report.errors:
        print("")
        print("Errors:")
        for message in report.errors:
            print(f"  - {message}")

    all_warnings = report.all_warnings if hasattr(report, "all_warnings") else report.warnings
    if all_warnings:
        print("")
        print(f"Warnings ({len(all_warnings)}):")
        for message in all_warnings:
            print(f"  - {message}")


def _print_coverage(coverage: dict[str, int | str | None]) -> None:
    print("")
    print("Coverage:")
    for key in sorted(coverage):
        print(f"  {key}: {coverage[key]}")


def _run_build_games(
    slate_date: str,
    *,
    schedule_fixture: Path | None = None,
) -> int:
    if schedule_fixture is not None:
        schedule_json = _load_json(schedule_fixture)
        source_label = str(schedule_fixture.resolve())
    else:
        schedule_json = fetch_schedule_json(slate_date)
        source_label = f"MLB schedule API ({slate_date})"

    games_result = build_games_from_schedule_json(schedule_json, slate_date=slate_date)
    game_details = build_game_details_shell(games_result.games)
    report = validate_games_shell(
        slate_date=slate_date,
        games=games_result.games,
        game_details=game_details,
        builder_warnings=games_result.warnings,
    )

    print(f"Built games shell from: {source_label}")
    print(f"Slate date: {slate_date}")
    print(f"Status: {'OK' if report.valid else 'FAILED'}")
    print("")
    print("Counts:")
    print(f"  games: {len(games_result.games)}")
    print(f"  game_details: {len(game_details)}")
    for key, value in sorted(report.counts.items()):
        if key in {"date", "games", "game_details"}:
            continue
        print(f"  {key}: {value}")

    _print_coverage(games_result.coverage)

    if report.errors:
        print("")
        print("Errors:")
        for message in report.errors:
            print(f"  - {message}")

    if report.warnings:
        print("")
        print(f"Warnings ({len(report.warnings)}):")
        for message in report.warnings:
            print(f"  - {message}")

    return 0 if report.valid else 1


def _load_game_feed_fixtures(directory: Path) -> dict[int, dict]:
    feeds: dict[int, dict] = {}
    for path in sorted(directory.glob("*.json")):
        try:
            game_pk = int(path.stem)
        except ValueError as exc:
            raise SystemExit(f"Game feed fixture filename must be {{game_pk}}.json: {path}") from exc
        feeds[game_pk] = _load_json(path)
    return feeds


def _fetch_feeds_for_schedule(schedule_json: dict, slate_date: str) -> dict[int, dict]:
    rows, _ = parse_schedule_rows(schedule_json, slate_date=slate_date)
    feeds: dict[int, dict] = {}
    for row in rows:
        if row.game_pk is None:
            continue
        feeds[row.game_pk] = fetch_game_feed_json(row.game_pk)
    return feeds


def _run_build_lineups(
    slate_date: str,
    *,
    schedule_fixture: Path | None = None,
    game_feed_fixtures: Path | None = None,
) -> int:
    if schedule_fixture is not None:
        schedule_json = _load_json(schedule_fixture)
        source_label = str(schedule_fixture.resolve())
    else:
        schedule_json = fetch_schedule_json(slate_date)
        source_label = f"MLB schedule API ({slate_date})"

    if game_feed_fixtures is not None:
        feeds_by_pk = _load_game_feed_fixtures(game_feed_fixtures)
        feed_source = str(game_feed_fixtures.resolve())
    elif schedule_fixture is not None:
        feeds_by_pk = {}
        feed_source = "none (offline schedule without game feeds)"
    else:
        feeds_by_pk = _fetch_feeds_for_schedule(schedule_json, slate_date)
        feed_source = f"MLB game feed API ({slate_date})"

    result = build_identity_layer(
        schedule_json,
        slate_date=slate_date,
        feeds_by_pk=feeds_by_pk,
    )
    validation = result.validation
    if validation is None:
        raise SystemExit("Identity validation did not run")

    print(f"Built identity layer from: {source_label}")
    print(f"Game feeds: {feed_source}")
    print(f"Slate date: {slate_date}")
    print(f"Status: {'OK' if validation.valid else 'FAILED'}")
    print("")
    print("Counts:")
    for key in (
        "games",
        "game_details",
        "teams",
        "players",
        "lineups",
        "missing_lineups",
        "missing_starting_pitchers",
        "orphan_lineup_players",
        "orphan_team_references",
    ):
        print(f"  {key}: {validation.counts.get(key, 0)}")

    print("")
    print("Coverage:")
    for key, value in sorted(validation.coverage.items()):
        print(f"  {key}: {value}")

    _print_coverage(result.games_coverage)

    if validation.errors:
        print("")
        print("Errors:")
        for message in validation.errors:
            print(f"  - {message}")

    if result.warnings or validation.warnings:
        combined = list(dict.fromkeys(result.warnings + validation.warnings))
        print("")
        print(f"Warnings ({len(combined)}):")
        for message in combined:
            print(f"  - {message}")

    return 0 if validation.valid else 1


def _run_build_matchups(
    slate_date: str,
    *,
    schedule_fixture: Path | None = None,
    game_feed_fixtures: Path | None = None,
    statcast_fixture: Path | None = None,
) -> int:
    if schedule_fixture is not None:
        schedule_json = _load_json(schedule_fixture)
        source_label = str(schedule_fixture.resolve())
    else:
        schedule_json = fetch_schedule_json(slate_date)
        source_label = f"MLB schedule API ({slate_date})"

    if game_feed_fixtures is not None:
        feeds_by_pk = _load_game_feed_fixtures(game_feed_fixtures)
        feed_source = str(game_feed_fixtures.resolve())
    elif schedule_fixture is not None:
        feeds_by_pk = {}
        feed_source = "none (offline schedule without game feeds)"
    else:
        feeds_by_pk = _fetch_feeds_for_schedule(schedule_json, slate_date)
        feed_source = f"MLB game feed API ({slate_date})"

    statcast_source = (
        str(statcast_fixture.resolve())
        if statcast_fixture is not None
        else f"pybaseball Statcast ({slate_date})"
    )

    result = build_matchup_layer(
        schedule_json,
        slate_date=slate_date,
        feeds_by_pk=feeds_by_pk,
        statcast_fixture=str(statcast_fixture) if statcast_fixture else None,
    )
    validation = result.validation
    if validation is None:
        raise SystemExit("Enrichment validation did not run")

    print(f"Built matchup layer from: {source_label}")
    print(f"Game feeds: {feed_source}")
    print(f"Statcast source: {statcast_source}")
    print(f"Slate date: {slate_date}")
    print(f"Status: {'OK' if validation.valid else 'FAILED'}")
    print("")
    print("Counts:")
    for key in (
        "games",
        "lineups",
        "players",
        "matchups",
        "hitters_enriched",
        "starters_enriched",
        "pitch_types_found",
        "missing_stat_blocks",
        "missing_starters",
        "missing_pitch_mix",
        "orphan_references",
        "duplicate_matchups",
    ):
        print(f"  {key}: {validation.counts.get(key, 0)}")

    print("")
    print("Coverage:")
    for key, value in sorted(validation.coverage.items()):
        print(f"  {key}: {value}")

    if validation.errors:
        print("")
        print("Errors:")
        for message in validation.errors:
            print(f"  - {message}")

    combined_warnings = list(dict.fromkeys(result.warnings + validation.warnings))
    if combined_warnings:
        print("")
        print(f"Warnings ({len(combined_warnings)}):")
        for message in combined_warnings:
            print(f"  - {message}")

    return 0 if validation.valid else 1


def _print_candidate_write(result) -> None:
    print(f"Wrote candidate: {result.path}")
    print(f"SHA256: {result.sha256}")
    print(f"Bytes: {result.byte_size}")
    print("")
    print("Counts:")
    for key in (
        "games",
        "game_details",
        "teams",
        "players",
        "lineups",
        "matchups",
        "export_matchup_rows",
        "enrichment_matchups",
        "top_plays",
        "category_boards",
    ):
        print(f"  {key}: {getattr(result.counts, key, 0)}")
    if result.warnings:
        print("")
        print(f"Warnings ({len(result.warnings)}):")
        for message in result.warnings:
            print(f"  - {message}")


def _print_comparison(report) -> None:
    print("")
    print("Reference comparison:")
    print(f"  reference: {report.reference_path}")
    if report.candidate_path:
        print(f"  candidate: {report.candidate_path}")
    print(f"  top_level_key_parity: {report.top_level_key_parity}")
    print(f"  schema_version reference: {report.schema_version_reference}")
    print(f"  schema_version candidate: {report.schema_version_candidate}")
    if report.missing_in_candidate:
        print(f"  missing_in_candidate: {sorted(report.missing_in_candidate)}")
    if report.extra_in_candidate:
        print(f"  extra_in_candidate: {sorted(report.extra_in_candidate)}")
    print("")
    print("Counts:")
    for key, value in sorted(report.counts.items()):
        print(f"  {key}: {value}")
    print("")
    print("Cardinality deltas:")
    for key, value in sorted(report.cardinality_deltas.items()):
        print(f"  {key}: {value}")
    if report.null_heavy_fields:
        print("")
        print("Null-heavy vs reference:")
        for field_name in report.null_heavy_fields:
            print(f"  - {field_name}")
    print("")
    print("Matchup cardinality analysis:")
    for key, value in report.matchup_cardinality.items():
        if key == "pitches_per_hitter_game_distribution":
            print(f"  {key}: {value}")
        elif key == "cause_summary":
            print(f"  {key}:")
            print(f"    {value}")
        else:
            print(f"  {key}: {value}")
    print("")
    print("Relationship integrity:")
    for key, value in report.relationship_integrity.items():
        print(f"  {key}: {value}")
    if report.warnings:
        print("")
        print(f"Comparison warnings ({len(report.warnings)}):")
        for message in report.warnings:
            print(f"  - {message}")


def _run_build_full_candidate(
    slate_date: str,
    output: Path,
    *,
    schedule_fixture: Path | None = None,
    game_feed_fixtures: Path | None = None,
    statcast_fixture: Path | None = None,
    force_candidate: bool = False,
    compare_reference: Path | None = None,
    validate_only: bool = False,
) -> int:
    live_export = (ROOT / "data" / "daily_export.json").resolve()
    if output.resolve() == live_export:
        raise SystemExit(f"Refusing to write live export path: {live_export}")

    if validate_only:
        if not output.exists():
            raise SystemExit(f"Candidate file not found for --validate-only: {output}")
        payload = _load_json(output)
        report = validate_export_dict(payload)
        _print_report(output, report)
        return 0 if report.valid else 1

    if schedule_fixture is not None:
        schedule_json = _load_json(schedule_fixture)
        source_label = str(schedule_fixture.resolve())
    else:
        schedule_json = fetch_schedule_json(slate_date)
        source_label = f"MLB schedule API ({slate_date})"

    if game_feed_fixtures is not None:
        feeds_by_pk = _load_game_feed_fixtures(game_feed_fixtures)
        feed_source = str(game_feed_fixtures.resolve())
    elif schedule_fixture is not None:
        feeds_by_pk = {}
        feed_source = "none (offline schedule without game feeds)"
    else:
        feeds_by_pk = _fetch_feeds_for_schedule(schedule_json, slate_date)
        feed_source = f"MLB game feed API ({slate_date})"

    statcast_source = (
        str(statcast_fixture.resolve())
        if statcast_fixture is not None
        else f"pybaseball Statcast ({slate_date})"
    )

    document = build_daily_export_document(
        schedule_json,
        slate_date=slate_date,
        feeds_by_pk=feeds_by_pk,
        statcast_fixture=str(statcast_fixture) if statcast_fixture else None,
    )

    validation = document.matchup_layer.validation
    if validation is None:
        raise SystemExit("Enrichment validation did not run")

    write_result = write_candidate_export(
        document.export,
        output,
        force=force_candidate,
        counts=document.counts,
        warnings=document.warnings,
    )

    print(f"Built full candidate from: {source_label}")
    print(f"Game feeds: {feed_source}")
    print(f"Statcast source: {statcast_source}")
    print(f"Slate date: {slate_date}")
    print(f"Status: {'OK' if validation.valid and write_result.valid else 'FAILED'}")
    _print_candidate_write(write_result)

    if compare_reference is not None:
        reference_payload = _load_json(compare_reference)
        candidate_payload = _load_json(output)
        comparison = compare_to_reference(
            candidate_payload,
            reference_payload,
            reference_path=compare_reference,
            candidate_path=output,
        )
        _print_comparison(comparison)

    if validation.errors:
        print("")
        print("Errors:")
        for message in validation.errors:
            print(f"  - {message}")
        return 1

    return 0 if write_result.valid else 1


def _print_promotion_result(result, *, json_result: bool = False) -> None:
    if json_result:
        print(json.dumps(result.to_dict(), indent=2))
        return

    print(f"Mode: {result.mode}")
    print(f"Dry run: {result.dry_run}")
    print(f"Status: {result.status}")
    if result.candidate_path:
        print(f"Candidate: {result.candidate_path}")
    if result.candidate_sha256_expected:
        print(f"Expected SHA256: {result.candidate_sha256_expected}")
    if result.candidate_sha256_actual:
        print(f"Actual SHA256: {result.candidate_sha256_actual}")
    if result.live_path:
        print(f"Live path: {result.live_path}")
    if result.original_live_sha256:
        print(f"Original live SHA256: {result.original_live_sha256}")
    if result.backup_path:
        print(f"Backup path: {result.backup_path}")
    if result.backup_sha256:
        print(f"Backup SHA256: {result.backup_sha256}")
    if result.promoted_live_sha256:
        print(f"Promoted live SHA256: {result.promoted_live_sha256}")
    print(f"Rollback attempted: {result.rollback_attempted}")
    print(f"Rollback succeeded: {result.rollback_succeeded}")
    print(f"Retention count: {result.retention_count}")
    if result.pruned_backups:
        print(f"Pruned backups ({len(result.pruned_backups)}):")
        for path in result.pruned_backups:
            print(f"  - {path}")
    if result.planned_actions:
        print("")
        print("Planned actions:")
        for action in result.planned_actions:
            print(f"  - {action}")
    if result.error:
        print("")
        print(f"Error: {result.error}")
    if result.warnings:
        print("")
        print(f"Warnings ({len(result.warnings)}):")
        for message in result.warnings:
            print(f"  - {message}")


def _run_promotion(args: argparse.Namespace) -> int:
    if args.promote and args.rollback_backup:
        raise SystemExit("--promote and --rollback-backup are mutually exclusive")

    if args.rollback_backup:
        if not args.yes_promote:
            raise SystemExit("Manual rollback requires --yes-promote")
        result = rollback_from_backup(
            backup_path=args.rollback_backup,
            backup_dir=args.backup_dir or DEFAULT_BACKUP_DIR,
        )
        _print_promotion_result(result, json_result=args.json_result)
        if result.status == PromotionStatus.CRITICAL.value:
            return 2
        return 0 if result.rollback_succeeded or result.status == PromotionStatus.PROMOTION_SUCCEEDED.value else 1

    if not args.promote:
        return -1

    if not args.candidate:
        raise SystemExit("--promote requires --candidate PATH")
    if not args.candidate_sha256:
        raise SystemExit("--promote requires --candidate-sha256 DIGEST")

    dry_run = args.promotion_dry_run
    if not dry_run and not args.yes_promote:
        raise SystemExit("Real promotion requires --yes-promote (or use --promotion-dry-run)")

    result = promote_candidate(
        candidate_path=args.candidate,
        expected_sha256=args.candidate_sha256,
        backup_dir=args.backup_dir or DEFAULT_BACKUP_DIR,
        retention_count=args.backup_retention_count or DEFAULT_RETENTION_COUNT,
        dry_run=dry_run,
        prune=not args.no_prune_backups,
    )
    _print_promotion_result(result, json_result=args.json_result)

    if result.status == PromotionStatus.CRITICAL.value:
        return 2
    if dry_run:
        return 0 if result.status == PromotionStatus.DRY_RUN_READY.value else 1
    return 0 if result.status == PromotionStatus.PROMOTION_SUCCEEDED.value else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate or build daily export JSON against the G0b schema.",
    )
    parser.add_argument(
        "--validate-existing",
        type=Path,
        metavar="PATH",
        help="Validate an existing export file (read-only).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Alias for validating the reference export at data/daily_export.json.",
    )
    parser.add_argument(
        "--build-games",
        action="store_true",
        help="Build and validate games[] + game_details[] shell for --date (no writes).",
    )
    parser.add_argument(
        "--date",
        type=str,
        metavar="YYYY-MM-DD",
        help="Slate date for --build-games.",
    )
    parser.add_argument(
        "--schedule-fixture",
        type=Path,
        metavar="PATH",
        help="Offline schedule JSON fixture for --build-games / --build-lineups.",
    )
    parser.add_argument(
        "--build-lineups",
        action="store_true",
        help=(
            "Build and validate games, game_details, teams, players, and lineups "
            "for --date (no writes)."
        ),
    )
    parser.add_argument(
        "--build-matchups",
        action="store_true",
        help=(
            "Build and validate games, identity, enrichment, and matchups "
            "for --date (no writes)."
        ),
    )
    parser.add_argument(
        "--statcast-fixture",
        type=Path,
        metavar="PATH",
        help="Offline Statcast events JSON fixture for --build-matchups.",
    )
    parser.add_argument(
        "--build-full-candidate",
        action="store_true",
        help="Assemble and write a validated DailyExport candidate file (never writes live export).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        metavar="PATH",
        help="Candidate output path for --build-full-candidate.",
    )
    parser.add_argument(
        "--force-candidate",
        action="store_true",
        help="Overwrite an existing candidate file.",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate --output candidate without rebuilding.",
    )
    parser.add_argument(
        "--compare-reference",
        type=Path,
        metavar="PATH",
        help="Compare candidate to a reference export after build.",
    )
    parser.add_argument(
        "--game-feed-fixtures",
        type=Path,
        metavar="DIR",
        help="Directory of {game_pk}.json game feed fixtures for offline --build-lineups / --build-matchups.",
    )
    parser.add_argument(
        "--promote",
        action="store_true",
        help="Promote a validated candidate export to the live export path.",
    )
    parser.add_argument(
        "--promotion-dry-run",
        action="store_true",
        help="Run promotion preflight without modifying live export or backups.",
    )
    parser.add_argument(
        "--candidate",
        type=Path,
        metavar="PATH",
        help="Candidate export path for --promote.",
    )
    parser.add_argument(
        "--candidate-sha256",
        type=str,
        metavar="DIGEST",
        help="Expected SHA256 digest of --candidate (64 hex chars).",
    )
    parser.add_argument(
        "--yes-promote",
        action="store_true",
        help="Confirm real promotion or manual rollback.",
    )
    parser.add_argument(
        "--backup-dir",
        type=Path,
        metavar="DIR",
        help=f"Backup directory (default: {DEFAULT_BACKUP_DIR}).",
    )
    parser.add_argument(
        "--backup-retention-count",
        type=int,
        metavar="N",
        help=f"Number of validated backups to retain (default: {DEFAULT_RETENTION_COUNT}).",
    )
    parser.add_argument(
        "--rollback-backup",
        type=Path,
        metavar="PATH",
        help="Explicit manual rollback from a backup file.",
    )
    parser.add_argument(
        "--no-prune-backups",
        action="store_true",
        help="Skip backup pruning after successful promotion.",
    )
    parser.add_argument(
        "--json-result",
        action="store_true",
        help="Emit structured promotion result as JSON.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.promote or args.rollback_backup:
        return _run_promotion(args)

    if args.build_full_candidate or args.validate_only:
        if not args.output:
            parser.error("--build-full-candidate and --validate-only require --output PATH")
        if not args.date and not args.validate_only:
            parser.error("--build-full-candidate requires --date YYYY-MM-DD")
        return _run_build_full_candidate(
            args.date or "",
            args.output,
            schedule_fixture=args.schedule_fixture,
            game_feed_fixtures=args.game_feed_fixtures,
            statcast_fixture=args.statcast_fixture,
            force_candidate=args.force_candidate,
            compare_reference=args.compare_reference,
            validate_only=args.validate_only,
        )

    if args.build_games:
        if not args.date:
            parser.error("--build-games requires --date YYYY-MM-DD")
        return _run_build_games(args.date, schedule_fixture=args.schedule_fixture)

    if args.build_matchups:
        if not args.date:
            parser.error("--build-matchups requires --date YYYY-MM-DD")
        return _run_build_matchups(
            args.date,
            schedule_fixture=args.schedule_fixture,
            game_feed_fixtures=args.game_feed_fixtures,
            statcast_fixture=args.statcast_fixture,
        )

    if args.build_lineups:
        if not args.date:
            parser.error("--build-lineups requires --date YYYY-MM-DD")
        return _run_build_lineups(
            args.date,
            schedule_fixture=args.schedule_fixture,
            game_feed_fixtures=args.game_feed_fixtures,
        )

    if args.validate_existing:
        target = args.validate_existing
    elif args.dry_run:
        target = DEFAULT_REFERENCE
    else:
        parser.error(
            "Specify --validate-existing PATH, --dry-run, --build-games --date YYYY-MM-DD, "
            "--build-lineups --date YYYY-MM-DD, --build-matchups --date YYYY-MM-DD, "
            "or --build-full-candidate --date YYYY-MM-DD --output PATH"
        )

    target = target.resolve()
    payload = _load_json(target)
    report = validate_export_dict(payload)
    _print_report(target, report)
    return 0 if report.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
