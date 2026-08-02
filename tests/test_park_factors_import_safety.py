"""Ensure backend.collectors.park_factors is import-safe."""

from __future__ import annotations

import importlib
import sqlite3
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
PRODUCTION_DB = ROOT / "database" / "mlb_lab.db"
MODULE_NAME = "backend.collectors.park_factors"


@pytest.fixture()
def production_db_bytes() -> bytes:
    return PRODUCTION_DB.read_bytes()


def test_import_does_not_mutate_production_database(production_db_bytes: bytes) -> None:
    sys.modules.pop(MODULE_NAME, None)
    before = production_db_bytes

    import backend.collectors.park_factors as park_factors  # noqa: F401

    after = PRODUCTION_DB.read_bytes()
    assert after == before
    assert not hasattr(park_factors, "conn")


def test_import_does_not_open_module_level_sqlite_connection(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple] = []

    def tracked_connect(*args, **kwargs):
        calls.append((args, kwargs))
        raise AssertionError("sqlite3.connect should not run on import")

    monkeypatch.setattr(sqlite3, "connect", tracked_connect)
    sys.modules.pop(MODULE_NAME, None)

    importlib.import_module(MODULE_NAME)

    assert calls == []


def test_load_park_factors_writes_isolated_database(tmp_path: Path) -> None:
    from backend.collectors.park_factors import PARKS, load_park_factors, lookup_park_factors

    db_path = tmp_path / "park_factors.db"
    count = load_park_factors(db_path)

    assert count == len(PARKS)
    factors = lookup_park_factors("Rogers Centre", db_path)
    assert factors == {"run_factor": 102, "hit_factor": 101, "hr_factor": 105}


def test_lookup_park_factors_unknown_venue_returns_nullable_factors(tmp_path: Path) -> None:
    from backend.collectors.park_factors import load_park_factors, lookup_park_factors

    db_path = tmp_path / "park_factors.db"
    load_park_factors(db_path)

    assert lookup_park_factors("Unknown Park", db_path) == {
        "run_factor": None,
        "hit_factor": None,
        "hr_factor": None,
    }


def test_list_park_factors_reads_isolated_database(tmp_path: Path) -> None:
    from backend.collectors.park_factors import PARKS, list_park_factors, load_park_factors

    db_path = tmp_path / "park_factors.db"
    load_park_factors(db_path)

    rows = list_park_factors(db_path)
    assert len(rows) == len(PARKS)
    assert rows[0]["venue"]
