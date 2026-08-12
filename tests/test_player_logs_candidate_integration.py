"""Offline integration tests for player_logs in daily export candidates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from backend.export.build_daily_export_document import build_daily_export_document, write_candidate_export
from backend.export.daily_export_validation import validate_export_dict

FIXTURES = Path(__file__).resolve().parent / "fixtures"
ROOT = Path(__file__).resolve().parents[1]
LIVE_EXPORT = ROOT / "data" / "daily_export.json"


def _schedule():
    return json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8"))


def _feeds():
    return {822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))}


def _document(*, build_player_logs: bool = True):
    return build_daily_export_document(
        _schedule(),
        slate_date="2026-07-19",
        feeds_by_pk=_feeds(),
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
        build_player_logs=build_player_logs,
    )


def test_candidate_includes_player_logs() -> None:
    document = _document()
    assert document.export.player_logs is not None
    assert len(document.export.player_logs) >= 1
    assert document.counts.player_logs >= 1
    assert document.counts.player_log_rows >= 1


def test_candidate_validates_with_player_logs() -> None:
    document = _document()
    report = validate_export_dict(document.export.model_dump(mode="json"))
    assert report.valid is True
    assert report.counts["player_logs"] >= 1


def test_empty_logs_handled_when_not_built() -> None:
    document = _document(build_player_logs=False)
    assert document.export.player_logs is None


def test_player_logs_count_reported() -> None:
    document = _document()
    layer = document.player_logs_layer
    assert layer is not None
    assert layer.counts["export_player_log_hitters"] == document.counts.player_logs
    assert layer.counts["hitter_logs"] == document.counts.hitter_logs


def test_no_live_export_modification(tmp_path: Path) -> None:
    if not LIVE_EXPORT.exists():
        pytest.skip("live export not present")
    before = LIVE_EXPORT.read_bytes()
    document = _document()
    output = tmp_path / "candidate.json"
    write_candidate_export(document.export, output)
    assert LIVE_EXPORT.read_bytes() == before


def test_no_production_db_mutation() -> None:
    db_path = ROOT / "database" / "mlb_lab.db"
    if not db_path.exists():
        pytest.skip("database not present")
    before = hashlib.sha256(db_path.read_bytes()).hexdigest()
    _document()
    after = hashlib.sha256(db_path.read_bytes()).hexdigest()
    assert before == after


def test_no_network_in_pytest(monkeypatch: pytest.MonkeyPatch) -> None:
    def fail_fetch(*_args, **_kwargs):
        raise AssertionError("network fetch should not run when statcast_fixture is provided")

    monkeypatch.setattr(
        "backend.export.enrichment.statcast_source.fetch_statcast_events",
        fail_fetch,
    )
    document = _document()
    assert document.export.player_logs is not None
