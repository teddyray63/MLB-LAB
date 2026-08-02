"""Ensure backend.build_all is import-safe."""

from __future__ import annotations

import ast
import importlib
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parent.parent
PRODUCTION_DB = ROOT / "database" / "mlb_lab.db"
MODULE_NAME = "backend.build_all"
BUILD_ALL_PATH = ROOT / "backend" / "build_all.py"


@pytest.fixture()
def production_db_bytes() -> bytes:
    return PRODUCTION_DB.read_bytes()


def _fresh_import(monkeypatch: pytest.MonkeyPatch) -> list[list[str]]:
    calls: list[list[str]] = []

    def tracked_run(args, *more_args, **kwargs):
        calls.append(list(args))
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(subprocess, "run", tracked_run)
    sys.modules.pop(MODULE_NAME, None)
    return calls


def test_import_does_not_execute_subprocesses(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _fresh_import(monkeypatch)

    import backend.build_all  # noqa: F401

    assert calls == []


def test_reload_does_not_execute_subprocesses(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _fresh_import(monkeypatch)

    module = importlib.import_module(MODULE_NAME)
    importlib.reload(module)

    assert calls == []


def test_import_does_not_mutate_production_database(production_db_bytes: bytes) -> None:
    sys.modules.pop(MODULE_NAME, None)
    before = production_db_bytes

    import backend.build_all  # noqa: F401

    after = PRODUCTION_DB.read_bytes()
    assert after == before


def test_module_exposes_callable_main() -> None:
    import backend.build_all as build_all

    assert hasattr(build_all, "main")
    assert callable(build_all.main)


def test_cli_delegates_to_main_under_main_guard() -> None:
    tree = ast.parse(BUILD_ALL_PATH.read_text(encoding="utf-8"))
    main_guard_calls_main = False

    for node in tree.body:
        if not isinstance(node, ast.If):
            continue
        test = node.test
        if not isinstance(test, ast.Compare):
            continue
        if not (
            isinstance(test.left, ast.Name)
            and test.left.id == "__name__"
            and len(test.comparators) == 1
            and isinstance(test.comparators[0], ast.Constant)
            and test.comparators[0].value == "__main__"
        ):
            continue
        for stmt in node.body:
            if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                func = stmt.value.func
                if isinstance(func, ast.Name) and func.id == "main":
                    main_guard_calls_main = True

    assert main_guard_calls_main, "Expected if __name__ == '__main__': main()"


def test_main_executes_expected_subprocess_steps_when_called(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[list[str]] = []

    def tracked_run(args, *more_args, **kwargs):
        calls.append(list(args))
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(subprocess, "run", tracked_run)
    sys.modules.pop(MODULE_NAME, None)

    import backend.build_all as build_all

    build_all.main()

    assert [call[-1] for call in calls] == build_all.steps
