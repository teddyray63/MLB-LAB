"""Tests for scripts/repo_health.py."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import repo_health  # noqa: E402


FIXTURES = REPO_ROOT / "tests/fixtures/repo_health"


def run_git(cwd: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True)


def init_repo(base: Path) -> Path:
    repo = base / "repo"
    repo.mkdir()
    run_git(repo, "init", "-b", "main")
    run_git(repo, "config", "user.email", "health@test.local")
    run_git(repo, "config", "user.name", "Health Test")
    return repo


def write_minimal_repo(repo: Path, *, project_state: str | None = None, include_legacy_daily: bool = False) -> None:
    (repo / "AGENTS.md").write_text(
        "orchestration policy\nTask contracts (.cursor/templates/task-contract.md)\n",
        encoding="utf-8",
    )
    (repo / ".gitignore").write_text("evidence/**/*.raw.json\n", encoding="utf-8")
    (repo / "PROJECT_STATE.md").write_text(
        project_state
        or (FIXTURES / "project_state_minimal.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (repo / ".pre-commit-config.yaml").write_text("repos: []\n", encoding="utf-8")
    (repo / ".cursor/rules").mkdir(parents=True)
    for name in (
        "evidence-first.mdc",
        "mlb-lab-baseline.mdc",
        "repository-safety.mdc",
        "scope-and-verification.mdc",
        "session-preflight.mdc",
    ):
        (repo / ".cursor/rules" / name).write_text(
            "---\nalwaysApply: true\n---\nrule\n",
            encoding="utf-8",
        )
    (repo / ".cursor/templates").mkdir(parents=True)
    contract = "\n".join(
        [
            "CONTRACT_ID",
            "AUTHORITY_LEVEL",
            "CURRENT STATE",
            "AUTHORIZED PATHS",
            "AUTHORIZED ACTIONS",
            "PROHIBITED ACTIONS",
            "MUTATION OWNER",
            "LOCKS HELD",
            "CHECKPOINT REQUIREMENT",
        ]
    )
    (repo / ".cursor/templates/task-contract.md").write_text(contract, encoding="utf-8")
    (repo / ".github/workflows").mkdir(parents=True)
    (repo / ".github/workflows/verify-g0b.yml").write_text(
        textwrap.dedent(
            """
            name: Verify G0b
            on:
              push:
                branches: [main]
              pull_request:
                branches: [main]
            permissions:
              contents: read
            jobs:
              verify:
                steps:
                  - run: python3 -m pytest tests/ -q
                  - run: python3 scripts/build_daily_export.py --validate-existing tests/fixtures/reference_export_pre_promotion.json
                  - run: npm run build
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )
    if include_legacy_daily:
        (repo / ".github/workflows/daily-run.yml").write_text("git push\n", encoding="utf-8")
    (repo / "README.md").write_text("test\n", encoding="utf-8")
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "initial")


def scan_repo(repo: Path, **kwargs) -> repo_health.ScanResult:
    options = repo_health.ScanOptions(
        mode=kwargs.get("mode", "fast"),
        json_output=kwargs.get("json_output", False),
        no_fetch=True,
        no_network=kwargs.get("no_network", True),
        expect_branch=kwargs.get("expect_branch"),
        verbose=False,
        dry_run=kwargs.get("dry_run", False),
        repo_root=repo,
    )
    return repo_health.run_scan(options)


def findings_by_code(result: repo_health.ScanResult) -> dict[str, list[repo_health.Finding]]:
    grouped: dict[str, list[repo_health.Finding]] = {}
    for cat in result.categories:
        for finding in cat.findings:
            grouped.setdefault(finding.code, []).append(finding)
    return grouped


class RepoHealthTests(unittest.TestCase):
    def test_durable_project_state_passes_on_main(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(
                repo,
                project_state=(FIXTURES / "project_state_durable.md").read_text(encoding="utf-8"),
            )
            result = scan_repo(repo)
            codes = findings_by_code(result)
            self.assertNotIn("PROJECT_STATE_HEAD_MISMATCH", codes)
            self.assertNotIn("PROJECT_STATE_MAIN_HEAD_MISMATCH", codes)
            self.assertNotIn("PROJECT_STATE_ORIGIN_MAIN_MISMATCH", codes)
            self.assertNotIn("PROJECT_STATE_BRANCH_MISMATCH", codes)
            project_state = next(cat for cat in result.categories if cat.id == "project_state")
            self.assertEqual(project_state.status, repo_health.Severity.PASS)

    def test_project_state_survives_head_advance_after_reconciliation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(
                repo,
                project_state=(FIXTURES / "project_state_durable.md").read_text(encoding="utf-8"),
            )
            checkpoint = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
            run_git(repo, "commit", "--allow-empty", "-m", "simulate PROJECT_STATE merge advance")
            advanced = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
            self.assertNotEqual(checkpoint, advanced)
            result = scan_repo(repo)
            codes = findings_by_code(result)
            self.assertNotIn("PROJECT_STATE_HEAD_MISMATCH", codes)
            self.assertNotIn("PROJECT_STATE_MAIN_HEAD_MISMATCH", codes)
            self.assertNotIn("PROJECT_STATE_ORIGIN_MAIN_MISMATCH", codes)
            project_state = next(cat for cat in result.categories if cat.id == "project_state")
            self.assertEqual(project_state.status, repo_health.Severity.PASS)

    def test_deprecated_normative_head_claim_warns(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo, project_state=(FIXTURES / "project_state_stale.md").read_text())
            result = scan_repo(repo)
            codes = findings_by_code(result)
            self.assertIn("PROJECT_STATE_NORMATIVE_HEAD_DEPRECATED", codes)
            self.assertNotIn("PROJECT_STATE_HEAD_MISMATCH", codes)
            self.assertNotIn("PROJECT_STATE_MAIN_HEAD_MISMATCH", codes)
            self.assertNotIn("PROJECT_STATE_ORIGIN_MAIN_MISMATCH", codes)
            self.assertGreaterEqual(result.exit_code, 1)

    def test_historical_milestone_sha_does_not_trigger_head_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(
                repo,
                project_state=(FIXTURES / "project_state_durable.md").read_text(encoding="utf-8"),
            )
            result = scan_repo(repo)
            codes = findings_by_code(result)
            self.assertNotIn("PROJECT_STATE_HEAD_MISMATCH", codes)
            self.assertNotIn("PROJECT_STATE_MAIN_HEAD_MISMATCH", codes)
            self.assertNotIn("PROJECT_STATE_ORIGIN_MAIN_MISMATCH", codes)
            project_state = next(cat for cat in result.categories if cat.id == "project_state")
            self.assertEqual(project_state.status, repo_health.Severity.PASS)

    def test_branch_mismatch_warns(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            state = (repo / "PROJECT_STATE.md").read_text(encoding="utf-8")
            state = state.replace("## Active Branch\n\nmain", "## Active Branch\n\nfeature/test")
            (repo / "PROJECT_STATE.md").write_text(state, encoding="utf-8")
            run_git(repo, "add", "PROJECT_STATE.md")
            run_git(repo, "commit", "-m", "align active branch doc")
            run_git(repo, "checkout", "-b", "feature/test")
            result = scan_repo(repo)
            self.assertIn("GIT_BRANCH_UNEXPECTED", findings_by_code(result))
            self.assertGreaterEqual(result.exit_code, 1)

    def test_missing_verify_workflow_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            (repo / ".github/workflows/verify-g0b.yml").unlink()
            result = scan_repo(repo)
            self.assertIn("CI_WORKFLOW_MISSING", findings_by_code(result))

    def test_verify_unsafe_permissions_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            path = repo / ".github/workflows/verify-g0b.yml"
            path.write_text(path.read_text(encoding="utf-8").replace("read", "write"), encoding="utf-8")
            result = scan_repo(repo)
            self.assertIn("CI_PERMISSIONS_UNSAFE", findings_by_code(result))

    def test_known_untracked_evidence_is_info(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            evidence = repo / "evidence/mlb/game-995731-feed-live.metadata.txt"
            evidence.parent.mkdir(parents=True)
            evidence.write_text("metadata\n", encoding="utf-8")
            result = scan_repo(repo)
            codes = findings_by_code(result)
            self.assertIn("WORKTREE_KNOWN_EVIDENCE", codes)
            self.assertNotIn("WORKTREE_UNEXPECTED_UNTRACKED", codes)

    def test_unexpected_untracked_warns(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            (repo / "unexpected.txt").write_text("x\n", encoding="utf-8")
            result = scan_repo(repo)
            self.assertIn("WORKTREE_UNEXPECTED_UNTRACKED", findings_by_code(result))

    def test_tracked_raw_evidence_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            raw = repo / "evidence/mlb/sample.raw.json"
            raw.parent.mkdir(parents=True)
            raw.write_text("{}\n", encoding="utf-8")
            run_git(repo, "add", "-f", "evidence/mlb/sample.raw.json")
            run_git(repo, "commit", "-m", "bad evidence")
            result = scan_repo(repo)
            self.assertIn("EVIDENCE_RAW_TRACKED", findings_by_code(result))

    def test_staged_raw_evidence_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            raw = repo / "evidence/mlb/sample.raw.json"
            raw.parent.mkdir(parents=True)
            raw.write_text("{}\n", encoding="utf-8")
            run_git(repo, "add", "-f", "evidence/mlb/sample.raw.json")
            result = scan_repo(repo)
            codes = findings_by_code(result)
            self.assertTrue(
                "EVIDENCE_RAW_STAGED" in codes or "WORKTREE_STAGED_CHANGE" in codes
            )

    def test_missing_governance_file_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            (repo / "AGENTS.md").unlink()
            result = scan_repo(repo)
            self.assertIn("GOVERNANCE_FILE_MISSING", findings_by_code(result))

    def test_rule_always_apply_drift_warns(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            (repo / ".cursor/rules/evidence-first.mdc").write_text(
                "---\nalwaysApply: false\n---\n",
                encoding="utf-8",
            )
            result = scan_repo(repo)
            self.assertIn("RULE_ALWAYS_APPLY_DRIFT", findings_by_code(result))

    def test_exit_code_aggregation_warn_over_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo, include_legacy_daily=True)
            result = scan_repo(repo)
            self.assertEqual(result.exit_code, 1)
            self.assertIn("WORKFLOW_LEGACY_MUTATING", findings_by_code(result))

    def test_json_schema_basics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo, project_state=(FIXTURES / "project_state_stale.md").read_text())
            result = scan_repo(repo, json_output=True)
            payload = {
                "scan_version": repo_health.SCAN_VERSION,
                "mode": result.options.mode,
                "overall": repo_health.SEVERITY_LABEL[result.overall],
                "exit_code": result.exit_code,
                "duration_seconds": result.duration_seconds,
                "categories": [cat.to_dict() for cat in result.categories],
            }
            self.assertTrue(payload["scan_version"])
            self.assertEqual(payload["mode"], "fast")
            self.assertGreaterEqual(payload["exit_code"], 1)
            self.assertIsInstance(payload["categories"], list)
            json.dumps(payload)

    def test_subprocess_failure_sets_scan_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            with mock.patch.object(repo_health, "git", side_effect=RuntimeError("boom")):
                result = scan_repo(repo)
            self.assertTrue(result.scan_error)
            self.assertEqual(result.exit_code, 3)

    def test_network_disabled_skips_ls_remote(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            result = scan_repo(repo, no_network=True)
            codes = findings_by_code(result)
            self.assertIn("NETWORK_UNAVAILABLE", codes)
            self.assertNotIn("GIT_REMOTE_LS_REMOTE_MISMATCH", codes)

    def test_ahead_behind_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            run_git(repo, "commit", "--allow-empty", "-m", "ahead")
            run_git(repo, "update-ref", "refs/remotes/origin/main", "HEAD~1")
            result = scan_repo(repo)
            codes = findings_by_code(result)
            self.assertTrue(
                "GIT_MAIN_ORIGIN_MISMATCH" in codes or "GIT_AHEAD_BEHIND" in codes
            )

    def test_manifest_lists_checks(self) -> None:
        manifest = repo_health.check_manifest()
        ids = {entry["id"] for entry in manifest}
        self.assertIn("git_branch", ids)
        self.assertIn("project_state_drift", ids)
        self.assertIn("pytest", ids)

    def test_dry_run_does_not_execute_pre_commit_validate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = init_repo(Path(tmp))
            write_minimal_repo(repo)
            with mock.patch.object(repo_health, "run_cmd", side_effect=AssertionError("should not run")):
                options = repo_health.ScanOptions(
                    mode="standard",
                    json_output=False,
                    no_fetch=True,
                    no_network=True,
                    expect_branch=None,
                    verbose=False,
                    dry_run=True,
                    repo_root=repo,
                )
                result = repo_health.run_scan(options)
            codes = findings_by_code(result)
            self.assertTrue(any(code.endswith("_PLANNED") for code in codes))

    def test_production_fast_scan_project_state_has_no_normative_head_failures(self) -> None:
        options = repo_health.ScanOptions(
            mode="fast",
            json_output=False,
            no_fetch=True,
            no_network=True,
            expect_branch="main",
            verbose=False,
            dry_run=False,
            repo_root=REPO_ROOT,
        )
        result = repo_health.run_scan(options)
        codes = findings_by_code(result)
        self.assertNotIn("PROJECT_STATE_HEAD_MISMATCH", codes)
        self.assertNotIn("PROJECT_STATE_MAIN_HEAD_MISMATCH", codes)
        self.assertNotIn("PROJECT_STATE_ORIGIN_MAIN_MISMATCH", codes)


if __name__ == "__main__":
    unittest.main()
