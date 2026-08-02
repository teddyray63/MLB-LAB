#!/usr/bin/env python3
"""Dry-run CLI for the daily export pipeline (Phase G0b.1 — validation only)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from backend.export.daily_export_validation import ValidationReport, validate_export_dict  # noqa: E402

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


def _print_report(path: Path, report: ValidationReport) -> None:
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

    all_warnings = report.all_warnings
    if all_warnings:
        print("")
        print(f"Warnings ({len(all_warnings)}):")
        preview = all_warnings[:10]
        for message in preview:
            print(f"  - {message}")
        if len(all_warnings) > 10:
            print(f"  ... and {len(all_warnings) - 10} more")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate daily export JSON against the G0b schema (dry-run only).",
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
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.validate_existing:
        target = args.validate_existing
    elif args.dry_run:
        target = DEFAULT_REFERENCE
    else:
        parser.error("Specify --validate-existing PATH or --dry-run")

    target = target.resolve()
    payload = _load_json(target)
    report = validate_export_dict(payload)
    _print_report(target, report)
    return 0 if report.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
