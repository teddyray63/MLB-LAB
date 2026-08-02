"""Safe promotion, backup, and rollback for data/daily_export.json."""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any

from backend.export.build_daily_export_document import LIVE_EXPORT_RELATIVE
from backend.export.daily_export_validation import validate_export_dict

DEFAULT_BACKUP_DIR = Path("data/backups")
DEFAULT_RETENTION_COUNT = 10
SHA256_HEX_LEN = 64
SHA256_HEX_RE = re.compile(r"^[0-9a-fA-F]{64}$")
BACKUP_FILENAME_RE = re.compile(
    r"^daily_export\.\d{8}T\d{6}Z\.[0-9a-f]{12}\.json$"
)


class PromotionStatus(str, Enum):
    PREFLIGHT_FAILED = "preflight_failed"
    CANDIDATE_VALIDATION_FAILED = "candidate_validation_failed"
    HASH_MISMATCH = "hash_mismatch"
    MALFORMED_SHA256 = "malformed_sha256"
    BACKUP_FAILED = "backup_failed"
    BACKUP_VALIDATION_FAILED = "backup_validation_failed"
    ATOMIC_REPLACE_FAILED = "atomic_replace_failed"
    POST_PROMOTION_VALIDATION_FAILED = "post_promotion_validation_failed"
    ROLLBACK_SUCCEEDED = "rollback_succeeded"
    ROLLBACK_FAILED = "rollback_failed"
    PROMOTION_SUCCEEDED = "promotion_succeeded"
    DRY_RUN_READY = "dry_run_ready"
    CRITICAL = "critical"


@dataclass
class PromotionResult:
    mode: str
    dry_run: bool
    candidate_path: str | None = None
    candidate_sha256_expected: str | None = None
    candidate_sha256_actual: str | None = None
    live_path: str | None = None
    original_live_sha256: str | None = None
    backup_path: str | None = None
    backup_sha256: str | None = None
    promoted_live_sha256: str | None = None
    rollback_attempted: bool = False
    rollback_succeeded: bool = False
    retention_count: int = DEFAULT_RETENTION_COUNT
    pruned_backups: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    status: str = PromotionStatus.PREFLIGHT_FAILED.value
    timestamps: dict[str, str] = field(default_factory=dict)
    planned_actions: list[str] = field(default_factory=list)
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def resolve_live_export_path(root: Path | None = None) -> Path:
    if root is None:
        root = Path(__file__).resolve().parents[2]
    return (root / LIVE_EXPORT_RELATIVE).resolve()


def compute_sha256(path: Path | str) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_sha256_hex(value: str) -> str:
    return value.strip().lower()


def validate_sha256_format(value: str) -> tuple[bool, str | None]:
    if not SHA256_HEX_RE.match(value):
        return False, (
            f"Expected exactly {SHA256_HEX_LEN} hexadecimal characters, "
            f"got {len(value.strip())}"
        )
    return True, None


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _backup_filename(live_sha256: str, timestamp: str | None = None) -> str:
    ts = timestamp or _utc_timestamp()
    prefix = live_sha256[:12]
    return f"daily_export.{ts}.{prefix}.json"


def _load_json_dict(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return payload


def _fsync_file(path: Path) -> None:
    with path.open("rb") as handle:
        os.fsync(handle.fileno())


def _fsync_parent_dir(path: Path) -> None:
    parent = path.parent
    if not parent.exists():
        return
    fd = os.open(str(parent), os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _is_writable_dir(path: Path) -> bool:
    path.mkdir(parents=True, exist_ok=True)
    probe = path / f".write_probe_{os.getpid()}"
    try:
        probe.write_text("", encoding="utf-8")
        probe.unlink(missing_ok=True)
        return True
    except OSError:
        return False


def validate_candidate_for_promotion(path: Path | str) -> tuple[bool, str | None, str | None]:
    candidate = Path(path).resolve()
    if not candidate.exists():
        return False, f"Candidate file not found: {candidate}", None
    if not candidate.is_file():
        return False, f"Candidate path is not a file: {candidate}", None
    try:
        payload = _load_json_dict(candidate)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return False, f"Failed to read candidate: {exc}", None
    report = validate_export_dict(payload)
    if not report.valid:
        errors = "; ".join(report.errors)
        return False, f"Candidate validation failed: {errors}", None
    digest = compute_sha256(candidate)
    return True, None, digest


def _atomic_copy_with_validation(
    source: Path,
    dest_dir: Path,
    *,
    expected_sha256: str | None = None,
    validate: bool = True,
) -> Path:
    """Copy source bytes to a temp file in dest_dir, validate, return temp path."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    temp_fd, temp_name = tempfile.mkstemp(
        suffix=".json.tmp",
        prefix="daily_export_promote_",
        dir=str(dest_dir),
    )
    temp_path = Path(temp_name)
    os.close(temp_fd)
    try:
        data = source.read_bytes()
        with temp_path.open("wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        digest = compute_sha256(temp_path)
        if expected_sha256 is not None and digest != expected_sha256:
            raise ValueError(
                f"Temp file SHA256 mismatch: expected {expected_sha256}, got {digest}"
            )
        if validate:
            payload = json.loads(temp_path.read_text(encoding="utf-8"))
            report = validate_export_dict(payload)
            if not report.valid:
                errors = "; ".join(report.errors)
                raise ValueError(f"Validation failed: {errors}")
        return temp_path
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise


def _create_raw_backup(
    live_path: Path | str,
    backup_dir: Path | str,
    *,
    timestamp: str | None = None,
) -> tuple[Path, str]:
    """Copy live bytes to backup without schema validation (pre-rollback safety net)."""
    live = Path(live_path).resolve()
    backup_root = Path(backup_dir).resolve()
    if not live.exists():
        raise FileNotFoundError(f"Live export not found: {live}")
    live_sha256 = compute_sha256(live)
    final_name = _backup_filename(live_sha256, timestamp=timestamp)
    final_path = backup_root / final_name
    backup_root.mkdir(parents=True, exist_ok=True)
    temp_fd, temp_name = tempfile.mkstemp(
        suffix=".json.tmp",
        prefix="daily_export_promote_",
        dir=str(backup_root),
    )
    temp_path = Path(temp_name)
    os.close(temp_fd)
    try:
        data = live.read_bytes()
        with temp_path.open("wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        if compute_sha256(temp_path) != live_sha256:
            raise ValueError("Raw backup SHA256 mismatch")
        os.replace(temp_path, final_path)
        _fsync_parent_dir(final_path)
        return final_path, live_sha256
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise


def create_validated_backup(
    live_path: Path | str,
    backup_dir: Path | str,
    *,
    timestamp: str | None = None,
) -> tuple[Path, str]:
    """Create a validated byte-identical backup of the live export."""
    live = Path(live_path).resolve()
    backup_root = Path(backup_dir).resolve()

    if not live.exists():
        raise FileNotFoundError(f"Live export not found: {live}")

    live_sha256 = compute_sha256(live)
    live_payload = _load_json_dict(live)
    live_report = validate_export_dict(live_payload)
    if not live_report.valid:
        errors = "; ".join(live_report.errors)
        raise ValueError(f"Live export validation failed: {errors}")

    final_name = _backup_filename(live_sha256, timestamp=timestamp)
    final_path = backup_root / final_name

    temp_path = _atomic_copy_with_validation(
        live,
        backup_root,
        expected_sha256=live_sha256,
        validate=True,
    )
    try:
        backup_digest = compute_sha256(temp_path)
        if backup_digest != live_sha256:
            raise ValueError(
                f"Backup SHA256 {backup_digest} != live SHA256 {live_sha256}"
            )
        os.replace(temp_path, final_path)
        _fsync_parent_dir(final_path)
        if not final_path.exists():
            raise OSError(f"Backup file missing after rename: {final_path}")
        final_digest = compute_sha256(final_path)
        if final_digest != live_sha256:
            raise ValueError(
                f"Final backup SHA256 {final_digest} != live SHA256 {live_sha256}"
            )
        final_report = validate_export_dict(_load_json_dict(final_path))
        if not final_report.valid:
            errors = "; ".join(final_report.errors)
            raise ValueError(f"Final backup validation failed: {errors}")
        return final_path, live_sha256
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise


def prune_backups(
    backup_dir: Path | str,
    *,
    retention_count: int,
    exclude: Path | str | None = None,
) -> tuple[list[str], list[str]]:
    """Prune old backups; return (pruned_paths, warnings)."""
    if retention_count < 1:
        raise ValueError("retention_count must be a positive integer")

    root = Path(backup_dir).resolve()
    if not root.exists():
        return [], []

    exclude_resolved = Path(exclude).resolve() if exclude else None
    warnings: list[str] = []
    candidates: list[Path] = []

    for entry in root.iterdir():
        if not entry.is_file():
            continue
        if not BACKUP_FILENAME_RE.match(entry.name):
            continue
        if exclude_resolved and entry.resolve() == exclude_resolved:
            continue
        try:
            payload = _load_json_dict(entry)
            report = validate_export_dict(payload)
            if not report.valid:
                warnings.append(f"Skipping invalid backup for pruning: {entry.name}")
                continue
        except (OSError, json.JSONDecodeError, ValueError):
            warnings.append(f"Skipping unreadable backup for pruning: {entry.name}")
            continue
        candidates.append(entry)

    candidates.sort(key=lambda p: p.name, reverse=True)
    to_prune = candidates[retention_count:]
    pruned: list[str] = []

    for path in to_prune:
        try:
            path.unlink()
            pruned.append(str(path))
        except OSError as exc:
            warnings.append(f"Failed to prune {path.name}: {exc}")

    return pruned, warnings


def run_promotion_preflight(
    *,
    candidate_path: Path | str,
    expected_sha256: str,
    live_path: Path | str | None = None,
    backup_dir: Path | str = DEFAULT_BACKUP_DIR,
    retention_count: int = DEFAULT_RETENTION_COUNT,
    root: Path | None = None,
) -> PromotionResult:
    now = datetime.now(timezone.utc).isoformat()
    live = Path(live_path).resolve() if live_path else resolve_live_export_path(root)
    candidate = Path(candidate_path).resolve()
    backup_root = Path(backup_dir).resolve()

    result = PromotionResult(
        mode="preflight",
        dry_run=True,
        candidate_path=str(candidate),
        candidate_sha256_expected=normalize_sha256_hex(expected_sha256),
        live_path=str(live),
        retention_count=retention_count,
        timestamps={"started_at": now},
    )

    ok, err = validate_sha256_format(expected_sha256)
    if not ok:
        result.status = PromotionStatus.MALFORMED_SHA256.value
        result.error = err
        return result

    valid, err, actual_digest = validate_candidate_for_promotion(candidate)
    result.candidate_sha256_actual = actual_digest
    if not valid:
        result.status = PromotionStatus.CANDIDATE_VALIDATION_FAILED.value
        result.error = err
        return result

    if actual_digest != result.candidate_sha256_expected:
        result.status = PromotionStatus.HASH_MISMATCH.value
        result.error = (
            f"Candidate SHA256 mismatch: expected {result.candidate_sha256_expected}, "
            f"got {actual_digest}"
        )
        return result

    if not live.exists():
        result.status = PromotionStatus.PREFLIGHT_FAILED.value
        result.error = f"Live export not found: {live}"
        return result

    try:
        result.original_live_sha256 = compute_sha256(live)
        live_report = validate_export_dict(_load_json_dict(live))
        if not live_report.valid:
            result.status = PromotionStatus.PREFLIGHT_FAILED.value
            result.error = f"Live export validation failed: {'; '.join(live_report.errors)}"
            return result
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        result.status = PromotionStatus.PREFLIGHT_FAILED.value
        result.error = f"Failed to read live export: {exc}"
        return result

    if not os.access(live.parent, os.W_OK):
        result.status = PromotionStatus.PREFLIGHT_FAILED.value
        result.error = f"Live export directory not writable: {live.parent}"
        return result

    if not _is_writable_dir(backup_root):
        result.status = PromotionStatus.PREFLIGHT_FAILED.value
        result.error = f"Backup directory not writable: {backup_root}"
        return result

    planned_backup = backup_root / _backup_filename(result.original_live_sha256)
    result.backup_path = str(planned_backup)
    result.planned_actions = [
        f"Validate candidate: {candidate}",
        f"Confirm candidate SHA256: {actual_digest}",
        f"Validate live export: {live}",
        f"Create backup: {planned_backup}",
        f"Atomically replace live export at {live}",
        f"Validate promoted live export",
        f"Prune backups in {backup_root} (retain {retention_count} newest)",
    ]
    result.status = PromotionStatus.DRY_RUN_READY.value
    result.timestamps["completed_at"] = datetime.now(timezone.utc).isoformat()
    return result


def promote_candidate(
    *,
    candidate_path: Path | str,
    expected_sha256: str,
    live_path: Path | str | None = None,
    backup_dir: Path | str = DEFAULT_BACKUP_DIR,
    retention_count: int = DEFAULT_RETENTION_COUNT,
    dry_run: bool = False,
    prune: bool = True,
    root: Path | None = None,
) -> PromotionResult:
    now = datetime.now(timezone.utc).isoformat()
    live = Path(live_path).resolve() if live_path else resolve_live_export_path(root)
    candidate = Path(candidate_path).resolve()
    backup_root = Path(backup_dir).resolve()

    result = PromotionResult(
        mode="promote",
        dry_run=dry_run,
        candidate_path=str(candidate),
        candidate_sha256_expected=normalize_sha256_hex(expected_sha256),
        live_path=str(live),
        retention_count=retention_count,
        timestamps={"started_at": now},
    )

    if dry_run:
        preflight = run_promotion_preflight(
            candidate_path=candidate,
            expected_sha256=expected_sha256,
            live_path=live,
            backup_dir=backup_root,
            retention_count=retention_count,
            root=root,
        )
        result.candidate_sha256_actual = preflight.candidate_sha256_actual
        result.original_live_sha256 = preflight.original_live_sha256
        result.backup_path = preflight.backup_path
        result.planned_actions = preflight.planned_actions
        result.status = preflight.status
        result.error = preflight.error
        result.timestamps["completed_at"] = datetime.now(timezone.utc).isoformat()
        return result

    ok, err = validate_sha256_format(expected_sha256)
    if not ok:
        result.status = PromotionStatus.MALFORMED_SHA256.value
        result.error = err
        return result

    valid, err, actual_digest = validate_candidate_for_promotion(candidate)
    result.candidate_sha256_actual = actual_digest
    if not valid:
        result.status = PromotionStatus.CANDIDATE_VALIDATION_FAILED.value
        result.error = err
        return result

    if actual_digest != result.candidate_sha256_expected:
        result.status = PromotionStatus.HASH_MISMATCH.value
        result.error = (
            f"Candidate SHA256 mismatch: expected {result.candidate_sha256_expected}, "
            f"got {actual_digest}"
        )
        return result

    if not live.exists():
        result.status = PromotionStatus.PREFLIGHT_FAILED.value
        result.error = f"Live export not found: {live}"
        return result

    try:
        result.original_live_sha256 = compute_sha256(live)
        live_report = validate_export_dict(_load_json_dict(live))
        if not live_report.valid:
            result.status = PromotionStatus.PREFLIGHT_FAILED.value
            result.error = f"Live export validation failed: {'; '.join(live_report.errors)}"
            return result
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        result.status = PromotionStatus.PREFLIGHT_FAILED.value
        result.error = f"Failed to read live export: {exc}"
        return result

    backup_path: Path | None = None
    try:
        backup_path, backup_sha = create_validated_backup(live, backup_root)
        result.backup_path = str(backup_path)
        result.backup_sha256 = backup_sha
    except Exception as exc:
        result.status = PromotionStatus.BACKUP_FAILED.value
        result.error = f"Backup creation failed: {exc}"
        return result

    temp_live: Path | None = None
    try:
        temp_live = _atomic_copy_with_validation(
            candidate,
            live.parent,
            expected_sha256=actual_digest,
            validate=True,
        )
    except Exception as exc:
        result.status = PromotionStatus.BACKUP_VALIDATION_FAILED.value
        result.error = f"Temp live validation failed: {exc}"
        return result

    try:
        os.replace(temp_live, live)
        temp_live = None
        _fsync_parent_dir(live)
    except OSError as exc:
        if temp_live and temp_live.exists():
            temp_live.unlink(missing_ok=True)
        result.status = PromotionStatus.ATOMIC_REPLACE_FAILED.value
        result.error = f"Atomic replace failed: {exc}"
        return result

    try:
        promoted_digest = compute_sha256(live)
        if promoted_digest != actual_digest:
            raise ValueError(
                f"Promoted SHA256 {promoted_digest} != candidate SHA256 {actual_digest}"
            )
        promoted_report = validate_export_dict(_load_json_dict(live))
        if not promoted_report.valid:
            errors = "; ".join(promoted_report.errors)
            raise ValueError(f"Post-promotion validation failed: {errors}")
        result.promoted_live_sha256 = promoted_digest
    except Exception as exc:
        result.status = PromotionStatus.POST_PROMOTION_VALIDATION_FAILED.value
        result.error = str(exc)
        result.rollback_attempted = True
        rollback_result = rollback_from_backup(
            backup_path=backup_path,
            live_path=live,
            backup_dir=backup_root,
            automatic=True,
        )
        result.rollback_succeeded = rollback_result.rollback_succeeded
        if rollback_result.rollback_succeeded:
            result.status = PromotionStatus.ROLLBACK_SUCCEEDED.value
            result.promoted_live_sha256 = rollback_result.promoted_live_sha256
        else:
            result.status = PromotionStatus.CRITICAL.value
            result.error = (
                f"{result.error}; rollback failed: {rollback_result.error}"
            )
        result.timestamps["completed_at"] = datetime.now(timezone.utc).isoformat()
        return result

    result.status = PromotionStatus.PROMOTION_SUCCEEDED.value
    result.timestamps["completed_at"] = datetime.now(timezone.utc).isoformat()

    if prune:
        try:
            pruned, prune_warnings = prune_backups(
                backup_root,
                retention_count=retention_count,
                exclude=backup_path,
            )
            result.pruned_backups = pruned
            result.warnings.extend(prune_warnings)
        except Exception as exc:
            result.warnings.append(f"Backup pruning failed (promotion still succeeded): {exc}")

    return result


def rollback_from_backup(
    *,
    backup_path: Path | str,
    live_path: Path | str | None = None,
    backup_dir: Path | str = DEFAULT_BACKUP_DIR,
    automatic: bool = False,
    root: Path | None = None,
) -> PromotionResult:
    now = datetime.now(timezone.utc).isoformat()
    live = Path(live_path).resolve() if live_path else resolve_live_export_path(root)
    source_backup = Path(backup_path).resolve()
    backup_root = Path(backup_dir).resolve()

    result = PromotionResult(
        mode="rollback",
        dry_run=False,
        live_path=str(live),
        backup_path=str(source_backup),
        rollback_attempted=True,
        timestamps={"started_at": now},
    )

    if not source_backup.exists():
        result.status = PromotionStatus.ROLLBACK_FAILED.value
        result.error = f"Backup file not found: {source_backup}"
        return result

    try:
        backup_payload = _load_json_dict(source_backup)
        backup_report = validate_export_dict(backup_payload)
        if not backup_report.valid:
            result.status = PromotionStatus.ROLLBACK_FAILED.value
            result.error = f"Backup validation failed: {'; '.join(backup_report.errors)}"
            return result
        backup_sha = compute_sha256(source_backup)
        result.backup_sha256 = backup_sha
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        result.status = PromotionStatus.ROLLBACK_FAILED.value
        result.error = f"Failed to read backup: {exc}"
        return result

    if live.exists():
        try:
            result.original_live_sha256 = compute_sha256(live)
            live_report = validate_export_dict(_load_json_dict(live))
            if live_report.valid:
                pre_rollback_backup, _ = create_validated_backup(live, backup_root)
            else:
                pre_rollback_backup, _ = _create_raw_backup(live, backup_root)
            result.warnings.append(
                f"Pre-rollback backup created: {pre_rollback_backup}"
            )
        except Exception as exc:
            if not automatic:
                result.status = PromotionStatus.ROLLBACK_FAILED.value
                result.error = f"Pre-rollback backup failed: {exc}"
                return result
            result.warnings.append(f"Pre-rollback backup skipped in automatic mode: {exc}")

    temp_live: Path | None = None
    try:
        temp_live = _atomic_copy_with_validation(
            source_backup,
            live.parent,
            expected_sha256=backup_sha,
            validate=True,
        )
    except Exception as exc:
        result.status = PromotionStatus.ROLLBACK_FAILED.value
        result.error = f"Rollback temp validation failed: {exc}"
        return result

    try:
        os.replace(temp_live, live)
        temp_live = None
        _fsync_parent_dir(live)
    except OSError as exc:
        if temp_live and temp_live.exists():
            temp_live.unlink(missing_ok=True)
        result.status = PromotionStatus.CRITICAL.value
        result.error = f"Rollback atomic replace failed: {exc}"
        return result

    try:
        restored_digest = compute_sha256(live)
        if restored_digest != backup_sha:
            raise ValueError(
                f"Restored SHA256 {restored_digest} != backup SHA256 {backup_sha}"
            )
        restored_report = validate_export_dict(_load_json_dict(live))
        if not restored_report.valid:
            errors = "; ".join(restored_report.errors)
            raise ValueError(f"Restored live validation failed: {errors}")
        result.promoted_live_sha256 = restored_digest
        result.rollback_succeeded = True
        result.status = (
            PromotionStatus.ROLLBACK_SUCCEEDED.value
            if automatic
            else PromotionStatus.PROMOTION_SUCCEEDED.value
        )
    except Exception as exc:
        result.status = PromotionStatus.CRITICAL.value
        result.error = f"Rollback post-replace validation failed: {exc}"
        return result

    result.timestamps["completed_at"] = datetime.now(timezone.utc).isoformat()
    return result
