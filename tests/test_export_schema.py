"""Tests for daily export schema models and validation (Phase G0b.1)."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
from pydantic import ValidationError

from backend.export.daily_export_models import (
    DAILY_EXPORT_SCHEMA_VERSION,
    PLAY_CATEGORIES,
    DailyExport,
    export_top_level_keys,
    parse_daily_export,
)
from backend.export.daily_export_validation import (
    REQUIRED_TOP_LEVEL_KEYS,
    validate_export,
    validate_export_dict,
)

ROOT = Path(__file__).resolve().parent.parent
REFERENCE_EXPORT = ROOT / "data" / "daily_export.json"
SLATE_TS = ROOT / "web-dashboard" / "src" / "types" / "slate.ts"


@pytest.fixture(scope="module")
def reference_export() -> dict:
    if not REFERENCE_EXPORT.exists():
        pytest.skip(f"Reference export missing: {REFERENCE_EXPORT}")
    return json.loads(REFERENCE_EXPORT.read_text(encoding="utf-8"))


def test_reference_export_parses(reference_export: dict) -> None:
    export = parse_daily_export(reference_export)
    assert export.date == reference_export["date"]
    assert len(export.games) == len(reference_export["games"])


def test_reference_export_validate_dict(reference_export: dict) -> None:
    report = validate_export_dict(reference_export)
    assert report.valid, report.errors
    assert report.counts["games"] == len(reference_export["games"])
    assert report.filter_support is not None
    assert report.filter_support.pitch_type.supported is True


def test_reference_export_has_expected_top_level_keys(reference_export: dict) -> None:
    assert REQUIRED_TOP_LEVEL_KEYS.issubset(reference_export.keys())


def test_slate_ts_daily_export_key_parity() -> None:
    if not SLATE_TS.exists():
        pytest.skip(f"Missing slate contract: {SLATE_TS}")

    text = SLATE_TS.read_text(encoding="utf-8")
    match = re.search(r"export interface DailyExport\s*\{([^}]+)\}", text, re.S)
    assert match, "DailyExport interface not found in slate.ts"

    ts_keys = set(re.findall(r"^\s*(\w+)\??:", match.group(1), re.M))
    model_keys = set(export_top_level_keys())

    missing_in_python = sorted(ts_keys - model_keys)
    extra_in_python = sorted(model_keys - ts_keys - {"schema_version"})

    assert not missing_in_python, f"Pydantic missing TS keys: {missing_in_python}"
    assert not extra_in_python, f"Pydantic has extra keys vs TS: {extra_in_python}"


def test_play_categories_match_slate_ts() -> None:
    if not SLATE_TS.exists():
        pytest.skip(f"Missing slate contract: {SLATE_TS}")

    text = SLATE_TS.read_text(encoding="utf-8")
    match = re.search(
        r"export const PLAY_CATEGORIES.*?=\s*\[(.*?)\]",
        text,
        re.S,
    )
    assert match
    ts_categories = re.findall(r"'([^']+)'", match.group(1))
    assert list(PLAY_CATEGORIES) == ts_categories


def test_missing_required_top_level_key_fails(reference_export: dict) -> None:
    broken = dict(reference_export)
    del broken["matchups"]
    report = validate_export_dict(broken)
    assert not report.valid
    assert any("matchups" in error for error in report.errors)


def test_invalid_date_fails(reference_export: dict) -> None:
    broken = dict(reference_export)
    broken["date"] = "not-a-date"
    with pytest.raises(ValidationError):
        parse_daily_export(broken)


def test_duplicate_game_pk_is_warning_not_error(reference_export: dict) -> None:
    export = parse_daily_export(reference_export)
    report = validate_export(export)
    assert report.valid
    assert any("Duplicate game_pk" in warning for warning in report.warnings)


def test_schema_version_warning_when_missing(reference_export: dict) -> None:
    export = parse_daily_export(reference_export)
    report = validate_export(export)
    assert any("schema_version missing" in warning for warning in report.warnings)


def test_new_schema_version_constant() -> None:
    assert DAILY_EXPORT_SCHEMA_VERSION == 1


def test_category_board_max_rows_enforced(reference_export: dict) -> None:
    export = parse_daily_export(reference_export)
    broken = export.model_copy(deep=True)
    category = PLAY_CATEGORIES[0]
    rows = list(getattr(broken.category_boards, category))
    rows.extend(rows)
    setattr(broken.category_boards, category, rows)
    report = validate_export(broken)
    assert not report.valid
    assert any("max 20" in error for error in report.errors)
