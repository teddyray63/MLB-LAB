"""Offline tests for G0b.5a daily export candidate assembly."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import pytest

from backend.export.build_daily_export_document import (
    analyze_matchup_cardinality,
    build_daily_export_document,
    compare_to_reference,
    empty_category_boards,
    empty_top_plays_board,
    export_to_dict,
    write_candidate_export,
)
from backend.export.daily_export_validation import ValidationReport, validate_export_dict

FIXTURES = Path(__file__).resolve().parent / "fixtures"
ROOT = Path(__file__).resolve().parents[1]
LIVE_EXPORT = ROOT / "data" / "daily_export.json"
REFERENCE_EXPORT = LIVE_EXPORT


def _schedule():
    return json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8"))


def _feeds():
    return {822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))}


def _document():
    return build_daily_export_document(
        _schedule(),
        slate_date="2026-07-19",
        feeds_by_pk=_feeds(),
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )


def test_valid_assembled_candidate(tmp_path: Path) -> None:
    document = _document()
    output = tmp_path / "daily_export.2026-07-19.json"
    result = write_candidate_export(document.export, output)
    assert result.valid is True
    assert output.exists()
    report = validate_export_dict(json.loads(output.read_text(encoding="utf-8")))
    assert report.valid is True
    assert document.counts.games >= 1
    assert document.counts.matchups >= 1


def test_missing_required_section_fails_validation() -> None:
    document = _document()
    payload = export_to_dict(document.export)
    del payload["matchups"]
    report = validate_export_dict(payload)
    assert report.valid is False


def test_invalid_relationship_blocks_candidate_write(tmp_path: Path) -> None:
    document = _document()
    broken = document.export.model_copy(update={"date": "not-a-date"})
    output = tmp_path / "broken.json"
    with pytest.raises(ValueError, match="Candidate failed validation"):
        write_candidate_export(broken, output)


def test_candidate_path_write_and_temp_cleanup(tmp_path: Path) -> None:
    document = _document()
    output = tmp_path / "candidate.json"
    write_candidate_export(document.export, output)
    leftovers = list(tmp_path.glob("*.tmp"))
    assert leftovers == []
    assert output.read_text(encoding="utf-8").startswith("{\n")


def test_refuse_overwrite_without_force(tmp_path: Path) -> None:
    document = _document()
    output = tmp_path / "candidate.json"
    write_candidate_export(document.export, output)
    with pytest.raises(FileExistsError):
        write_candidate_export(document.export, output, force=False)


def test_forced_candidate_overwrite(tmp_path: Path) -> None:
    document = _document()
    output = tmp_path / "candidate.json"
    first = write_candidate_export(document.export, output)
    second = write_candidate_export(document.export, output, force=True)
    assert first.sha256 == second.sha256


def test_sha256_generation(tmp_path: Path) -> None:
    document = _document()
    output = tmp_path / "candidate.json"
    result = write_candidate_export(document.export, output)
    expected = hashlib.sha256(output.read_bytes()).hexdigest()
    assert result.sha256 == expected


def test_deterministic_output(tmp_path: Path) -> None:
    first = export_to_dict(_document().export)
    second = export_to_dict(_document().export)
    assert first["date"] == second["date"]
    assert first["games"] == second["games"]
    assert first["matchups"] == second["matchups"]


def test_reference_comparison() -> None:
    if not REFERENCE_EXPORT.exists():
        pytest.skip("reference export not present")
    reference = json.loads(REFERENCE_EXPORT.read_text(encoding="utf-8"))
    candidate = export_to_dict(_document().export)
    report = compare_to_reference(
        candidate,
        reference,
        reference_path=REFERENCE_EXPORT,
        candidate_path=Path("data/candidates/example.json"),
    )
    assert report.counts["reference_matchups"] == 894
    assert report.matchup_cardinality["reference_matchup_rows"] == 894
    assert "matchups cardinality delta" in report.warnings[0]


def test_unsupported_sections_empty_or_null() -> None:
    document = _document()
    assert empty_top_plays_board().hits == []
    assert empty_category_boards().hits == []
    assert document.export.player_logs is None
    assert document.export.player_zone_heatmaps is None
    assert any("top_plays: empty" in warning for warning in document.warnings)


def test_matchup_cardinality_reporting() -> None:
    if not REFERENCE_EXPORT.exists():
        pytest.skip("reference export not present")
    reference = json.loads(REFERENCE_EXPORT.read_text(encoding="utf-8"))
    analysis = analyze_matchup_cardinality(reference)
    assert analysis["reference_matchup_rows"] == 894
    assert analysis["rows_for_pool_only_hitters"] > 0
    assert analysis["unique_hitter_game_pitch_keys"] == 894


def test_no_live_export_modification(tmp_path: Path) -> None:
    if not LIVE_EXPORT.exists():
        pytest.skip("live export not present")
    before = LIVE_EXPORT.read_bytes()
    document = _document()
    output = tmp_path / "candidate.json"
    write_candidate_export(document.export, output)
    assert LIVE_EXPORT.read_bytes() == before


def test_refuse_live_export_path() -> None:
    document = _document()
    with pytest.raises(ValueError, match="Refusing to write live export path"):
        write_candidate_export(document.export, LIVE_EXPORT)


def test_no_db_modification() -> None:
    db_path = ROOT / "database" / "mlb_lab.db"
    if not db_path.exists():
        pytest.skip("database not present")
    before = hashlib.sha256(db_path.read_bytes()).hexdigest()
    _document()
    after = hashlib.sha256(db_path.read_bytes()).hexdigest()
    assert before == after


def test_export_meta_fields() -> None:
    document = _document()
    meta = document.export.export_meta
    assert meta is not None
    assert meta.runner_version
    assert meta.statcast_start
    assert meta.statcast_end
    assert meta.generated_at
    assert isinstance(meta.warnings, list)


def test_schema_version_set() -> None:
    document = _document()
    assert document.export.schema_version == 1


def test_failure_path_removes_temp_and_leaves_no_final_candidate(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Temp file is created and written before validation; failure must not promote."""
    document = _document()
    output = tmp_path / "candidate.json"
    live_before = LIVE_EXPORT.read_bytes() if LIVE_EXPORT.exists() else None
    db_path = ROOT / "database" / "mlb_lab.db"
    db_before = hashlib.sha256(db_path.read_bytes()).hexdigest() if db_path.exists() else None

    def fail_validation(_payload: dict) -> ValidationReport:
        return ValidationReport(valid=False, errors=["injected validation failure for test"])

    monkeypatch.setattr(
        "backend.export.build_daily_export_document.validate_export_dict",
        fail_validation,
    )

    with pytest.raises(ValueError, match="Candidate failed validation before rename"):
        write_candidate_export(document.export, output)

    assert not output.exists()
    assert list(tmp_path.glob("daily_export_*.json.tmp")) == []
    assert list(tmp_path.glob("*.tmp")) == []

    if live_before is not None:
        assert LIVE_EXPORT.read_bytes() == live_before
    if db_before is not None:
        assert hashlib.sha256(db_path.read_bytes()).hexdigest() == db_before


def test_atomic_promotion_uses_os_replace_once(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Successful write promotes temp → final via os.replace after validation."""
    document = _document()
    output = tmp_path / "candidate.json"
    replace_calls: list[tuple[Path, Path]] = []
    validated = {"done": False}
    real_replace = os.replace
    real_validate = validate_export_dict

    def track_validation(payload: dict) -> ValidationReport:
        report = real_validate(payload)
        validated["done"] = True
        return report

    def spy_replace(src: os.PathLike[str] | str, dst: os.PathLike[str] | str) -> None:
        assert validated["done"] is True, "os.replace must run only after validation succeeds"
        replace_calls.append((Path(src), Path(dst)))
        real_replace(src, dst)

    monkeypatch.setattr(
        "backend.export.build_daily_export_document.validate_export_dict",
        track_validation,
    )
    monkeypatch.setattr(
        "backend.export.build_daily_export_document.os.replace",
        spy_replace,
    )

    result = write_candidate_export(document.export, output)

    assert len(replace_calls) == 1
    src, dst = replace_calls[0]
    assert src.parent == output.parent.resolve()
    assert "daily_export_" in src.name
    assert src.name.endswith(".json.tmp")
    assert dst.resolve() == output.resolve()
    assert output.exists()
    assert not src.exists()
    assert list(tmp_path.glob("*.tmp")) == []
    assert result.valid is True
