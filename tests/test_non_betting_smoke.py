"""Smoke tests after betting-stack removal."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SELF = Path(__file__).resolve()

PROHIBITED_PATTERNS = [
    r"\bbetting\b",
    r"\bsportsbook\b",
    r"kelly_fraction",
    r"expected_value",
    r"implied_probability",
    r"\bclosing_line\b",
    r"\bclv\b",
    r"edge_from_odds",
    r"backend\.odds",
    r"betting_engine",
    r"import_odds",
    r"build_odds_exports",
    r"record_sportsbook",
]

ALLOWED_SUBSTRINGS = (
    "avg_ev",
    "max_ev",
)


def _tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [ROOT / line for line in result.stdout.splitlines() if line.strip()]


def _scan_file(path: Path) -> list[str]:
    if path.resolve() == SELF:
        return []
    if not path.is_file():
        return []
    if path.suffix not in {".py", ".md", ".json", ".ts", ".tsx", ".js", ".jsx", ".yml", ".yaml"}:
        return []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    hits: list[str] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        lower = line.lower()
        if any(token in lower for token in ALLOWED_SUBSTRINGS):
            continue
        for pattern in PROHIBITED_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                hits.append(f"{path.relative_to(ROOT)}:{line_no}: {line.strip()}")
                break
    return hits


def test_non_betting_modules_import():
    import backend.build_all  # noqa: F401
    import backend.doctor.doctor  # noqa: F401
    import backend.doctor.repair  # noqa: F401
    import backend.main  # noqa: F401
    import backend.mlb_lab_doctor  # noqa: F401


def test_doctor_has_no_betting_export_expectations():
    from backend.doctor.doctor import REQUIRED_EXPORTS

    exports = " ".join(REQUIRED_EXPORTS).lower()
    assert "betting" not in exports
    assert "odds" not in exports
    assert "value_edges" not in exports
    assert REQUIRED_EXPORTS == ["data/daily_export.json"]


def test_repair_points_to_primary_runner():
    from backend.doctor.doctor import run_doctor
    from backend.doctor.repair import suggest_repairs

    suggestions = suggest_repairs({"issues": ["Missing export: data/daily_export.json"]})
    assert any("mlb_lab_runner.py" in item for item in suggestions)
    assert not any("command_center.py" in item for item in suggestions)

    result = run_doctor()
    assert not any("odds" in warning.lower() for warning in result.get("warnings", []))


def test_tracked_sources_exclude_prohibited_betting_terms():
    violations: list[str] = []
    for path in _tracked_files():
        violations.extend(_scan_file(path))

    assert not violations, "Prohibited betting terms found:\n" + "\n".join(violations[:20])


def test_mlb_lab_runner_has_no_betting_hooks():
    source = (ROOT / "scripts" / "mlb_lab_runner.py").read_text(encoding="utf-8").lower()
    assert "betting_engine" not in source
    assert "backend.odds" not in source
    assert "sportsbook" not in source
