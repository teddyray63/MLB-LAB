#!/usr/bin/env python3
"""Dry-run CLI for the daily export pipeline (Phase G0b)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from backend.export.builders.game_details import build_game_details_shell  # noqa: E402
from backend.export.builders.games import build_games_from_schedule_json  # noqa: E402
from backend.export.daily_export_validation import (  # noqa: E402
    ValidationReport,
    validate_export_dict,
    validate_games_shell,
)
from backend.export.mlb_schedule import fetch_schedule_json  # noqa: E402

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
        help="Offline schedule JSON fixture for --build-games (skips live API).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.build_games:
        if not args.date:
            parser.error("--build-games requires --date YYYY-MM-DD")
        return _run_build_games(args.date, schedule_fixture=args.schedule_fixture)

    if args.validate_existing:
        target = args.validate_existing
    elif args.dry_run:
        target = DEFAULT_REFERENCE
    else:
        parser.error(
            "Specify --validate-existing PATH, --dry-run, or --build-games --date YYYY-MM-DD"
        )

    target = target.resolve()
    payload = _load_json(target)
    report = validate_export_dict(payload)
    _print_report(target, report)
    return 0 if report.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
