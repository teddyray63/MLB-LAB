"""Tests for G0b.5b daily export promotion, backup, and rollback."""

from __future__ import annotations

import hashlib
import json
import os
import stat
from pathlib import Path
from unittest import mock

import pytest

from backend.export.build_daily_export_document import (
    build_daily_export_document,
    export_to_dict,
    write_candidate_export,
)
from backend.export.daily_export_validation import ValidationReport, validate_export_dict
from backend.export.promote_daily_export import (
    DEFAULT_RETENTION_COUNT,
    PromotionStatus,
    _backup_filename,
    compute_sha256,
    create_validated_backup,
    normalize_sha256_hex,
    promote_candidate,
    prune_backups,
    rollback_from_backup,
    run_promotion_preflight,
    validate_candidate_for_promotion,
    validate_sha256_format,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"
ROOT = Path(__file__).resolve().parents[1]
LIVE_EXPORT = ROOT / "data" / "daily_export.json"
DB_PATH = ROOT / "database" / "mlb_lab.db"


def _schedule() -> dict:
    return json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8"))


def _feeds() -> dict:
    return {822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))}


def _document():
    return build_daily_export_document(
        _schedule(),
        slate_date="2026-07-19",
        feeds_by_pk=_feeds(),
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )


def _write_candidate(tmp_path: Path, name: str = "candidate.json") -> tuple[Path, str]:
    doc = _document()
    path = tmp_path / name
    result = write_candidate_export(doc.export, path)
    return path, result.sha256


def _write_live(tmp_path: Path, name: str = "daily_export.json") -> tuple[Path, str]:
    """Write a valid live export (same builder, distinct path)."""
    return _write_candidate(tmp_path, name)


def _layout(tmp_path: Path) -> dict[str, Path]:
    live_dir = tmp_path / "data"
    live_dir.mkdir(parents=True)
    backup_dir = tmp_path / "backups"
    backup_dir.mkdir(parents=True)
    live_path, live_sha = _write_live(live_dir)
    candidate_path, candidate_sha = _write_candidate(tmp_path / "candidates")
    return {
        "live": live_path,
        "live_sha": live_sha,
        "candidate": candidate_path,
        "candidate_sha": candidate_sha,
        "backup_dir": backup_dir,
        "live_dir": live_dir,
    }


# ---------------------------------------------------------------------------
# PREFLIGHT
# ---------------------------------------------------------------------------


def test_valid_dry_run_preflight(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    result = run_promotion_preflight(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.status == PromotionStatus.DRY_RUN_READY.value
    assert result.candidate_sha256_actual == ctx["candidate_sha"]
    assert result.original_live_sha256 == ctx["live_sha"]
    assert result.planned_actions


def test_dry_run_creates_no_backup(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        dry_run=True,
    )
    assert list(ctx["backup_dir"].iterdir()) == []


def test_dry_run_leaves_live_file_unchanged(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    before = ctx["live"].read_bytes()
    promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        dry_run=True,
    )
    assert ctx["live"].read_bytes() == before


def test_dry_run_does_not_prune(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    old_backup = ctx["backup_dir"] / _backup_filename(ctx["live_sha"], timestamp="20260101T000000Z")
    old_backup.write_bytes(ctx["live"].read_bytes())
    promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        dry_run=True,
    )
    assert old_backup.exists()


def test_invalid_candidate_rejected(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    bad = tmp_path / "bad.json"
    bad.write_text('{"date": "not-valid"}', encoding="utf-8")
    result = run_promotion_preflight(
        candidate_path=bad,
        expected_sha256="a" * 64,
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.status == PromotionStatus.CANDIDATE_VALIDATION_FAILED.value


def test_malformed_sha256_rejected(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    ok, err = validate_sha256_format("abc")
    assert ok is False
    result = run_promotion_preflight(
        candidate_path=ctx["candidate"],
        expected_sha256="not-a-valid-digest",
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.status == PromotionStatus.MALFORMED_SHA256.value


def test_sha256_mismatch_rejected(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    result = run_promotion_preflight(
        candidate_path=ctx["candidate"],
        expected_sha256="b" * 64,
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.status == PromotionStatus.HASH_MISMATCH.value


def test_missing_live_file_rejected(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    missing_live = tmp_path / "missing" / "daily_export.json"
    result = run_promotion_preflight(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=missing_live,
        backup_dir=ctx["backup_dir"],
    )
    assert result.status == PromotionStatus.PREFLIGHT_FAILED.value
    assert "not found" in (result.error or "").lower()


def test_unwritable_backup_directory_rejected(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    readonly = tmp_path / "readonly_backups"
    readonly.mkdir()
    os.chmod(readonly, stat.S_IRUSR | stat.S_IXUSR)
    try:
        result = run_promotion_preflight(
            candidate_path=ctx["candidate"],
            expected_sha256=ctx["candidate_sha"],
            live_path=ctx["live"],
            backup_dir=readonly,
        )
        assert result.status == PromotionStatus.PREFLIGHT_FAILED.value
        assert "not writable" in (result.error or "").lower()
    finally:
        os.chmod(readonly, stat.S_IRWXU)


def test_unwritable_live_directory_rejected(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    readonly_dir = tmp_path / "readonly_live"
    readonly_dir.mkdir()
    live_in_readonly = readonly_dir / "daily_export.json"
    live_in_readonly.write_bytes(ctx["live"].read_bytes())
    os.chmod(readonly_dir, stat.S_IRUSR | stat.S_IXUSR)
    try:
        result = run_promotion_preflight(
            candidate_path=ctx["candidate"],
            expected_sha256=ctx["candidate_sha"],
            live_path=live_in_readonly,
            backup_dir=ctx["backup_dir"],
        )
        assert result.status == PromotionStatus.PREFLIGHT_FAILED.value
        assert "not writable" in (result.error or "").lower()
    finally:
        os.chmod(readonly_dir, stat.S_IRWXU)


# ---------------------------------------------------------------------------
# BACKUP
# ---------------------------------------------------------------------------


def test_backup_created_before_promotion(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    backup_created = {"done": False}
    real_create = create_validated_backup

    def track_backup(*args, **kwargs):
        backup_created["done"] = True
        return real_create(*args, **kwargs)

    replace_calls: list[tuple[Path, Path]] = []
    real_replace = os.replace

    def spy_replace(src, dst):
        if backup_created["done"]:
            replace_calls.append((Path(src), Path(dst)))
        real_replace(src, dst)

    monkeypatch.setattr(
        "backend.export.promote_daily_export.create_validated_backup",
        track_backup,
    )
    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", spy_replace)

    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )
    assert backup_created["done"] is True
    assert result.status == PromotionStatus.PROMOTION_SUCCEEDED.value
    assert result.backup_path
    assert Path(result.backup_path).exists()
    live_replaces = [c for c in replace_calls if Path(c[1]) == ctx["live"]]
    assert len(live_replaces) == 1


def test_backup_bytes_equal_original_live_bytes(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    before = ctx["live"].read_bytes()
    backup_path, _ = create_validated_backup(ctx["live"], ctx["backup_dir"])
    assert backup_path.read_bytes() == before


def test_backup_sha256_equals_original_live_sha256(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    backup_path, backup_sha = create_validated_backup(ctx["live"], ctx["backup_dir"])
    assert backup_sha == ctx["live_sha"]
    assert compute_sha256(backup_path) == ctx["live_sha"]


def test_backup_validation_required(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    ctx = _layout(tmp_path)
    real_validate = validate_export_dict

    def fail_on_backup(payload: dict) -> ValidationReport:
        if payload.get("date") == "2026-07-19":
            return ValidationReport(valid=False, errors=["injected backup validation failure"])
        return real_validate(payload)

    monkeypatch.setattr(
        "backend.export.promote_daily_export.validate_export_dict",
        fail_on_backup,
    )
    with pytest.raises(Exception):
        create_validated_backup(ctx["live"], ctx["backup_dir"])


def test_backup_failure_blocks_promotion(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    before = ctx["live"].read_bytes()

    def fail_backup(*_a, **_k):
        raise OSError("injected backup failure")

    monkeypatch.setattr(
        "backend.export.promote_daily_export.create_validated_backup",
        fail_backup,
    )
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.status == PromotionStatus.BACKUP_FAILED.value
    assert ctx["live"].read_bytes() == before


def test_backup_temp_cleaned_after_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    real_replace = os.replace

    def fail_backup_replace(src, dst):
        if str(dst).endswith(".json") and "daily_export." in str(dst):
            raise OSError("injected backup rename failure")
        real_replace(src, dst)

    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", fail_backup_replace)
    with pytest.raises(OSError):
        create_validated_backup(ctx["live"], ctx["backup_dir"])
    assert list(ctx["backup_dir"].glob("*.tmp")) == []


def test_backup_uses_os_replace_exactly_once(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    replace_calls: list[tuple[Path, Path]] = []
    real_replace = os.replace

    def spy_replace(src, dst):
        replace_calls.append((Path(src), Path(dst)))
        real_replace(src, dst)

    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", spy_replace)
    create_validated_backup(ctx["live"], ctx["backup_dir"], timestamp="20260802T120000Z")
    backup_replaces = [c for c in replace_calls if "daily_export." in Path(c[1]).name]
    assert len(backup_replaces) == 1


def test_backup_naming_uses_utc_timestamp_and_live_hash_prefix(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    ts = "20260802T213045Z"
    backup_path, _ = create_validated_backup(
        ctx["live"], ctx["backup_dir"], timestamp=ts
    )
    assert backup_path.name == f"daily_export.{ts}.{ctx['live_sha'][:12]}.json"


# ---------------------------------------------------------------------------
# PROMOTION
# ---------------------------------------------------------------------------


def test_successful_promotion_uses_os_replace_once_for_live(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    replace_calls: list[tuple[Path, Path]] = []
    real_replace = os.replace

    def spy_replace(src, dst):
        replace_calls.append((Path(src), Path(dst)))
        real_replace(src, dst)

    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", spy_replace)
    promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )
    live_replaces = [c for c in replace_calls if Path(c[1]) == ctx["live"]]
    assert len(live_replaces) == 1


def test_temp_live_path_resides_in_live_parent_directory(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    temp_paths: list[Path] = []
    real_mkstemp = tempfile_mkstemp = __import__("tempfile").mkstemp

    def track_mkstemp(*args, **kwargs):
        fd, name = real_mkstemp(*args, **kwargs)
        temp_paths.append(Path(name))
        return fd, name

    monkeypatch.setattr("backend.export.promote_daily_export.tempfile.mkstemp", track_mkstemp)
    promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )
    live_temps = [p for p in temp_paths if p.parent == ctx["live"].parent]
    assert live_temps


def test_validation_occurs_before_live_replace(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    validated = {"done": False}
    real_validate = validate_export_dict

    def track_validation(payload: dict) -> ValidationReport:
        report = real_validate(payload)
        if payload.get("date") == "2026-07-19":
            validated["done"] = True
        return report

    replace_calls: list[tuple[Path, Path]] = []
    real_replace = os.replace

    def spy_replace(src, dst):
        if Path(dst) == ctx["live"]:
            assert validated["done"] is True
        replace_calls.append((Path(src), Path(dst)))
        real_replace(src, dst)

    monkeypatch.setattr(
        "backend.export.promote_daily_export.validate_export_dict",
        track_validation,
    )
    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", spy_replace)
    promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )


def test_final_live_bytes_equal_candidate_bytes(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    candidate_bytes = ctx["candidate"].read_bytes()
    promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )
    assert ctx["live"].read_bytes() == candidate_bytes


def test_final_live_sha256_equals_candidate_sha256(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )
    assert result.promoted_live_sha256 == ctx["candidate_sha"]
    assert compute_sha256(ctx["live"]) == ctx["candidate_sha"]


def test_no_partial_live_file_after_forced_failure_before_replace(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    before = ctx["live"].read_bytes()
    real_replace = os.replace

    def fail_live_replace(src, dst):
        if Path(dst) == ctx["live"]:
            raise OSError("injected live replace failure")
        real_replace(src, dst)

    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", fail_live_replace)
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.status == PromotionStatus.ATOMIC_REPLACE_FAILED.value
    assert ctx["live"].read_bytes() == before


def test_live_file_unchanged_if_candidate_validation_fails(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    before = ctx["live"].read_bytes()
    bad = tmp_path / "bad.json"
    bad.write_text("{}", encoding="utf-8")
    result = promote_candidate(
        candidate_path=bad,
        expected_sha256="a" * 64,
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.status == PromotionStatus.CANDIDATE_VALIDATION_FAILED.value
    assert ctx["live"].read_bytes() == before


def test_live_file_unchanged_if_backup_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    before = ctx["live"].read_bytes()

    def fail_backup(*_a, **_k):
        raise ValueError("injected backup failure")

    monkeypatch.setattr(
        "backend.export.promote_daily_export.create_validated_backup",
        fail_backup,
    )
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.status == PromotionStatus.BACKUP_FAILED.value
    assert ctx["live"].read_bytes() == before


def test_live_file_unchanged_if_temp_live_validation_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    before = ctx["live"].read_bytes()
    real_copy = __import__(
        "backend.export.promote_daily_export", fromlist=["_atomic_copy_with_validation"]
    )._atomic_copy_with_validation

    def fail_live_temp(source, dest_dir, **kwargs):
        if Path(dest_dir).resolve() == ctx["live"].parent.resolve():
            raise ValueError("injected temp live failure")
        return real_copy(source, dest_dir, **kwargs)

    monkeypatch.setattr(
        "backend.export.promote_daily_export._atomic_copy_with_validation",
        fail_live_temp,
    )
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.status == PromotionStatus.BACKUP_VALIDATION_FAILED.value
    assert ctx["live"].read_bytes() == before


def test_temporary_live_file_cleaned_after_pre_replace_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    real_replace = os.replace

    def fail_live_replace(src, dst):
        if Path(dst) == ctx["live"]:
            assert Path(src).exists()
            raise OSError("injected live replace failure")
        real_replace(src, dst)

    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", fail_live_replace)
    promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert list(ctx["live_dir"].glob("daily_export_promote_*.tmp")) == []


# ---------------------------------------------------------------------------
# POST-PROMOTION FAILURE AND ROLLBACK
# ---------------------------------------------------------------------------


def test_forced_post_promotion_validation_failure_triggers_rollback(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    replace_calls: list[tuple[Path, Path]] = []
    state = {"live_replaces": 0, "fail_next_validate": False}
    real_validate = validate_export_dict
    real_replace = os.replace

    def spy_replace(src, dst):
        replace_calls.append((Path(src), Path(dst)))
        if Path(dst).resolve() == ctx["live"].resolve():
            state["live_replaces"] += 1
            if state["live_replaces"] == 1:
                state["fail_next_validate"] = True
        real_replace(src, dst)

    def conditional_validate(payload: dict) -> ValidationReport:
        if state["fail_next_validate"]:
            state["fail_next_validate"] = False
            return ValidationReport(
                valid=False,
                errors=["injected post-promotion failure"],
            )
        return real_validate(payload)

    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", spy_replace)
    monkeypatch.setattr(
        "backend.export.promote_daily_export.validate_export_dict",
        conditional_validate,
    )
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )
    assert result.rollback_attempted is True
    assert result.rollback_succeeded is True
    assert result.status == PromotionStatus.ROLLBACK_SUCCEEDED.value
    live_replaces = [c for c in replace_calls if Path(c[1]) == ctx["live"]]
    assert len(live_replaces) >= 2


def test_rollback_restores_original_live_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    original = ctx["live"].read_bytes()
    _inject_post_promotion_failure(monkeypatch, ctx["live"])
    promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )
    assert ctx["live"].read_bytes() == original


def test_rollback_restores_original_sha256(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    _inject_post_promotion_failure(monkeypatch, ctx["live"])
    promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )
    assert compute_sha256(ctx["live"]) == ctx["live_sha"]


def test_rollback_uses_os_replace(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    replace_calls: list[tuple[Path, Path]] = []
    real_replace = os.replace

    def spy_replace(src, dst):
        replace_calls.append((Path(src), Path(dst)))
        real_replace(src, dst)

    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", spy_replace)
    _inject_post_promotion_failure(monkeypatch, ctx["live"])
    promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )
    rollback_replaces = [
        c for c in replace_calls if Path(c[1]) == ctx["live"] and c[1] != c[0]
    ]
    assert len(rollback_replaces) >= 2


def test_rollback_result_records_attempted_succeeded(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    _inject_post_promotion_failure(monkeypatch, ctx["live"])
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )
    assert result.rollback_attempted is True
    assert result.rollback_succeeded is True


def test_failed_rollback_reports_critical_and_never_success(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    _inject_post_promotion_failure(monkeypatch, ctx["live"])

    real_replace = os.replace
    rollback_attempt = {"n": 0}

    def fail_rollback_replace(src, dst):
        if Path(dst) == ctx["live"]:
            rollback_attempt["n"] += 1
            if rollback_attempt["n"] >= 2:
                raise OSError("injected rollback replace failure")
        real_replace(src, dst)

    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", fail_rollback_replace)
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        prune=False,
    )
    assert result.status == PromotionStatus.CRITICAL.value
    assert result.rollback_attempted is True
    assert result.rollback_succeeded is False
    assert result.status != PromotionStatus.PROMOTION_SUCCEEDED.value


def test_failed_rollback_does_not_prune_backups(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    old_backup = ctx["backup_dir"] / _backup_filename(ctx["live_sha"], timestamp="20260101T000000Z")
    old_backup.write_bytes(ctx["live"].read_bytes())
    _inject_post_promotion_failure(monkeypatch, ctx["live"])

    real_replace = os.replace
    rollback_attempt = {"n": 0}

    def fail_rollback_replace(src, dst):
        if Path(dst) == ctx["live"]:
            rollback_attempt["n"] += 1
            if rollback_attempt["n"] >= 2:
                raise OSError("injected rollback replace failure")
        real_replace(src, dst)

    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", fail_rollback_replace)
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert old_backup.exists()
    assert result.pruned_backups == []


# ---------------------------------------------------------------------------
# MANUAL ROLLBACK
# ---------------------------------------------------------------------------


def test_valid_explicit_rollback(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    backup_path, backup_sha = create_validated_backup(ctx["live"], ctx["backup_dir"])
    ctx["live"].write_text('{"broken": true}', encoding="utf-8")
    result = rollback_from_backup(
        backup_path=backup_path,
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.rollback_succeeded is True
    assert compute_sha256(ctx["live"]) == backup_sha


def test_invalid_backup_rejected(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    bad_backup = ctx["backup_dir"] / "daily_export.20260802T120000Z.abc123456789.json"
    bad_backup.write_text("{}", encoding="utf-8")
    result = rollback_from_backup(
        backup_path=bad_backup,
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.rollback_succeeded is False
    assert result.status == PromotionStatus.ROLLBACK_FAILED.value


def test_explicit_rollback_backs_up_current_live_first(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    backup_path, _ = create_validated_backup(ctx["live"], ctx["backup_dir"])
    ctx["live"].write_text('{"broken": true}', encoding="utf-8")
    before_backups = set(ctx["backup_dir"].iterdir())
    rollback_from_backup(
        backup_path=backup_path,
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    after_backups = set(ctx["backup_dir"].iterdir())
    assert len(after_backups) > len(before_backups)


def test_explicit_rollback_preserves_selected_backup(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    backup_path, _ = create_validated_backup(ctx["live"], ctx["backup_dir"])
    backup_before = backup_path.read_bytes()
    ctx["live"].write_text('{"broken": true}', encoding="utf-8")
    rollback_from_backup(
        backup_path=backup_path,
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert backup_path.read_bytes() == backup_before


def test_explicit_rollback_validates_restored_live_file(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    backup_path, backup_sha = create_validated_backup(ctx["live"], ctx["backup_dir"])
    ctx["live"].write_text('{"broken": true}', encoding="utf-8")
    result = rollback_from_backup(
        backup_path=backup_path,
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.promoted_live_sha256 == backup_sha
    assert validate_export_dict(json.loads(ctx["live"].read_text(encoding="utf-8"))).valid


# ---------------------------------------------------------------------------
# RETENTION
# ---------------------------------------------------------------------------


def _seed_backups(backup_dir: Path, live_path: Path, count: int) -> list[Path]:
    paths: list[Path] = []
    for index in range(count):
        ts = f"2026010{index % 10}T{index:02d}0000Z"
        name = _backup_filename(compute_sha256(live_path), timestamp=ts)
        path = backup_dir / name
        path.write_bytes(live_path.read_bytes())
        paths.append(path)
    return paths


def test_default_keeps_10_newest_validated_backups(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    seeded = _seed_backups(ctx["backup_dir"], ctx["live"], 15)
    pruned, _ = prune_backups(ctx["backup_dir"], retention_count=DEFAULT_RETENTION_COUNT)
    remaining = list(ctx["backup_dir"].glob("daily_export.*.json"))
    assert len(remaining) == DEFAULT_RETENTION_COUNT
    assert len(pruned) == 5


def test_custom_retention_count_works(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    _seed_backups(ctx["backup_dir"], ctx["live"], 8)
    pruned, _ = prune_backups(ctx["backup_dir"], retention_count=3)
    remaining = list(ctx["backup_dir"].glob("daily_export.*.json"))
    assert len(remaining) == 3
    assert len(pruned) == 5


def test_nonmatching_files_are_never_pruned(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    other = ctx["backup_dir"] / "notes.txt"
    other.write_text("keep me", encoding="utf-8")
    _seed_backups(ctx["backup_dir"], ctx["live"], 12)
    prune_backups(ctx["backup_dir"], retention_count=5)
    assert other.exists()


def test_current_run_backup_is_never_pruned(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    _seed_backups(ctx["backup_dir"], ctx["live"], 12)
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        retention_count=5,
    )
    assert result.backup_path
    assert Path(result.backup_path).exists()


def test_pruning_happens_only_after_successful_post_promotion_validation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    _seed_backups(ctx["backup_dir"], ctx["live"], 12)
    _inject_post_promotion_failure(monkeypatch, ctx["live"])
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        retention_count=5,
    )
    assert result.pruned_backups == []
    assert len(list(ctx["backup_dir"].glob("daily_export.*.json"))) >= 12


def test_pruning_failure_warns_without_falsifying_promotion_status(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ctx = _layout(tmp_path)
    _seed_backups(ctx["backup_dir"], ctx["live"], 12)

    def fail_prune(*_a, **_k):
        raise OSError("injected prune failure")

    monkeypatch.setattr("backend.export.promote_daily_export.prune_backups", fail_prune)
    result = promote_candidate(
        candidate_path=ctx["candidate"],
        expected_sha256=ctx["candidate_sha"],
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
        retention_count=5,
    )
    assert result.status == PromotionStatus.PROMOTION_SUCCEEDED.value
    assert any("pruning failed" in w.lower() for w in result.warnings)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def test_cli_promote_requires_candidate() -> None:
    from scripts.build_daily_export import main

    with pytest.raises(SystemExit, match="--promote requires --candidate"):
        main(["--promote", "--candidate-sha256", "a" * 64, "--yes-promote"])


def test_cli_promote_requires_candidate_sha256() -> None:
    from scripts.build_daily_export import main

    with pytest.raises(SystemExit, match="--promote requires --candidate-sha256"):
        main(["--promote", "--candidate", "data/candidates/x.json", "--yes-promote"])


def test_cli_real_promotion_requires_yes_promote(tmp_path: Path) -> None:
    from scripts.build_daily_export import main

    ctx = _layout(tmp_path)
    with pytest.raises(SystemExit, match="Real promotion requires --yes-promote"):
        main(
            [
                "--promote",
                "--candidate",
                str(ctx["candidate"]),
                "--candidate-sha256",
                ctx["candidate_sha"],
            ]
        )


def test_cli_dry_run_does_not_require_yes_promote(tmp_path: Path) -> None:
    from scripts.build_daily_export import main

    ctx = _layout(tmp_path)
    code = main(
        [
            "--promote",
            "--promotion-dry-run",
            "--candidate",
            str(ctx["candidate"]),
            "--candidate-sha256",
            ctx["candidate_sha"],
            "--json-result",
        ]
    )
    assert code == 0


def test_cli_rollback_requires_yes_promote(tmp_path: Path) -> None:
    from scripts.build_daily_export import main

    ctx = _layout(tmp_path)
    backup_path, _ = create_validated_backup(ctx["live"], ctx["backup_dir"])
    with pytest.raises(SystemExit, match="Manual rollback requires --yes-promote"):
        main(["--rollback-backup", str(backup_path)])


def test_cli_promote_and_rollback_conflict_rejected() -> None:
    from scripts.build_daily_export import main

    with pytest.raises(SystemExit, match="mutually exclusive"):
        main(
            [
                "--promote",
                "--rollback-backup",
                "data/backups/x.json",
                "--candidate",
                "data/candidates/x.json",
                "--candidate-sha256",
                "a" * 64,
                "--yes-promote",
            ]
        )


def test_cli_existing_non_promotion_behavior_unchanged() -> None:
    from scripts.build_daily_export import main

    with pytest.raises(SystemExit):
        main([])


# ---------------------------------------------------------------------------
# SIDE EFFECTS
# ---------------------------------------------------------------------------


def test_repository_db_unchanged() -> None:
    if not DB_PATH.exists():
        pytest.skip("database not present")
    before = hashlib.sha256(DB_PATH.read_bytes()).hexdigest()
    _document()
    after = hashlib.sha256(DB_PATH.read_bytes()).hexdigest()
    assert before == after


def test_repository_live_export_unchanged_during_tests() -> None:
    if not LIVE_EXPORT.exists():
        pytest.skip("live export not present")
    before = LIVE_EXPORT.read_bytes()
    _document()
    assert LIVE_EXPORT.read_bytes() == before


def test_no_network(monkeypatch: pytest.MonkeyPatch) -> None:
    def block_network(*_a, **_k):
        raise RuntimeError("network access blocked in promotion tests")

    monkeypatch.setattr("urllib.request.urlopen", block_network)
    valid, _, digest = validate_candidate_for_promotion(
        FIXTURES / "schedule_sample.json"
    )
    assert valid is False or digest is not None


def test_no_protected_runner_import_or_execution() -> None:
    runner_path = ROOT / "scripts" / "mlb_lab_runner.py"
    assert runner_path.exists()
    promote_source = (ROOT / "backend" / "export" / "promote_daily_export.py").read_text()
    assert "mlb_lab_runner" not in promote_source


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------


def _inject_post_promotion_failure(
    monkeypatch: pytest.MonkeyPatch,
    live_path: Path,
) -> None:
    state = {"live_replaces": 0, "fail_next_validate": False}
    real_validate = validate_export_dict
    real_replace = os.replace

    def spy_replace(src, dst):
        if Path(dst).resolve() == live_path.resolve():
            state["live_replaces"] += 1
            if state["live_replaces"] == 1:
                state["fail_next_validate"] = True
        real_replace(src, dst)

    def conditional_validate(payload: dict) -> ValidationReport:
        if state["fail_next_validate"]:
            state["fail_next_validate"] = False
            return ValidationReport(
                valid=False,
                errors=["injected post-promotion failure"],
            )
        return real_validate(payload)

    monkeypatch.setattr(
        "backend.export.promote_daily_export.validate_export_dict",
        conditional_validate,
    )
    monkeypatch.setattr("backend.export.promote_daily_export.os.replace", spy_replace)


def test_sha256_normalization_accepts_uppercase(tmp_path: Path) -> None:
    ctx = _layout(tmp_path)
    upper = ctx["candidate_sha"].upper()
    result = run_promotion_preflight(
        candidate_path=ctx["candidate"],
        expected_sha256=upper,
        live_path=ctx["live"],
        backup_dir=ctx["backup_dir"],
    )
    assert result.status == PromotionStatus.DRY_RUN_READY.value
    assert normalize_sha256_hex(upper) == ctx["candidate_sha"]
