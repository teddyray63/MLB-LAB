#!/usr/bin/env python3
"""Read-only MLB-LAB repository health scanner."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path
from typing import Any, Callable


SCAN_VERSION = "1.0.0"

KNOWN_UNTRACKED = ("evidence/mlb/game-995731-feed-live.metadata.txt",)


def matches_known_untracked(path: str) -> bool:
    if path in KNOWN_UNTRACKED:
        return True
    normalized = path.rstrip("/")
    for known in KNOWN_UNTRACKED:
        if known.startswith(f"{normalized}/"):
            return True
        if normalized == Path(known).parent.as_posix():
            return True
    return False

REQUIRED_RULES = (
    ".cursor/rules/evidence-first.mdc",
    ".cursor/rules/mlb-lab-baseline.mdc",
    ".cursor/rules/repository-safety.mdc",
    ".cursor/rules/scope-and-verification.mdc",
    ".cursor/rules/session-preflight.mdc",
)

TASK_CONTRACT_MARKERS = (
    "CONTRACT_ID",
    "AUTHORITY_LEVEL",
    "CURRENT STATE",
    "AUTHORIZED PATHS",
    "AUTHORIZED ACTIONS",
    "PROHIBITED ACTIONS",
    "MUTATION OWNER",
    "LOCKS HELD",
    "CHECKPOINT REQUIREMENT",
)

AGENTS_MARKERS = (
    "orchestration",
    "task-contract",
    "task contract",
)

RAW_EVIDENCE_GITIGNORE = "evidence/**/*.raw.json"


class Severity(IntEnum):
    INFO = 0
    PASS = 1
    WARN = 2
    FAIL = 3
    SKIP = 4
    ERROR = 5


SEVERITY_TO_EXIT = {
    Severity.INFO: 0,
    Severity.PASS: 0,
    Severity.WARN: 1,
    Severity.FAIL: 2,
    Severity.SKIP: 0,
    Severity.ERROR: 3,
}

SEVERITY_LABEL = {
    Severity.INFO: "info",
    Severity.PASS: "pass",
    Severity.WARN: "warn",
    Severity.FAIL: "fail",
    Severity.SKIP: "skip",
    Severity.ERROR: "error",
}


@dataclass
class Finding:
    code: str
    severity: Severity
    message: str
    expected: str | None = None
    observed: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "severity": SEVERITY_LABEL[self.severity],
            "message": self.message,
            "expected": self.expected,
            "observed": self.observed,
        }


@dataclass
class CategoryResult:
    id: str
    title: str
    findings: list[Finding] = field(default_factory=list)

    @property
    def status(self) -> Severity:
        if not self.findings:
            return Severity.PASS
        contributing = [
            f.severity
            for f in self.findings
            if f.severity not in (Severity.INFO, Severity.SKIP)
        ]
        if not contributing:
            return Severity.PASS
        return max(contributing, key=lambda s: s.value)

    def add(self, finding: Finding) -> None:
        self.findings.append(finding)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "status": SEVERITY_LABEL[self.status],
            "findings": [f.to_dict() for f in self.findings],
        }


@dataclass
class ScanOptions:
    mode: str
    json_output: bool
    no_fetch: bool
    no_network: bool
    expect_branch: str | None
    verbose: bool
    dry_run: bool
    repo_root: Path


@dataclass
class ScanResult:
    options: ScanOptions
    categories: list[CategoryResult] = field(default_factory=list)
    duration_seconds: float = 0.0
    scan_error: bool = False

    @property
    def overall(self) -> Severity:
        if self.scan_error:
            return Severity.ERROR
        if not self.categories:
            return Severity.PASS
        statuses = [cat.status for cat in self.categories]
        if Severity.ERROR in statuses:
            return Severity.ERROR
        if Severity.FAIL in statuses:
            return Severity.FAIL
        if Severity.WARN in statuses:
            return Severity.WARN
        return Severity.PASS

    @property
    def exit_code(self) -> int:
        return SEVERITY_TO_EXIT[self.overall]

    def category(self, cat_id: str, title: str) -> CategoryResult:
        cat = CategoryResult(id=cat_id, title=title)
        self.categories.append(cat)
        return cat


def run_cmd(
    repo_root: Path,
    args: list[str],
    *,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
    timeout: int = 600,
) -> tuple[int, str, str]:
    merged_env = None
    if env is not None:
        merged_env = {**os.environ, **env}
    result = subprocess.run(
        args,
        cwd=cwd or repo_root,
        capture_output=True,
        text=True,
        check=False,
        timeout=timeout,
        env=merged_env,
    )
    return result.returncode, result.stdout, result.stderr


def git(repo_root: Path, *args: str) -> tuple[int, str, str]:
    return run_cmd(repo_root, ["git", *args])


def normalize_commit(repo_root: Path, ref: str | None) -> str | None:
    if not ref:
        return None
    code, stdout, _ = git(repo_root, "rev-parse", "--verify", f"{ref}^{{commit}}")
    if code != 0:
        code, stdout, _ = git(repo_root, "rev-parse", "--verify", ref)
    if code != 0:
        return None
    return stdout.strip()


def commits_match(repo_root: Path, documented: str | None, live: str | None) -> bool:
    if not documented or not live:
        return documented == live
    doc_full = normalize_commit(repo_root, documented)
    live_full = normalize_commit(repo_root, live)
    if doc_full and live_full:
        return doc_full == live_full
    return documented.lower().startswith(live[: len(documented)].lower()) or live.startswith(
        documented
    )


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def find_heading_index(lines: list[str], heading_text: str) -> int | None:
    for index, line in enumerate(lines):
        if line.startswith("## ") and heading_text in line:
            return index
    return None


def first_content_after_heading(lines: list[str], heading: str) -> str | None:
    marker = f"## {heading}"
    for index, line in enumerate(lines):
        if line.strip() != marker:
            continue
        for follow in lines[index + 1 :]:
            stripped = follow.strip()
            if not stripped:
                continue
            if stripped.startswith("##"):
                break
            return stripped.strip("`").strip()
    return None


def section_body(lines: list[str], heading_substring: str) -> list[str]:
    start = find_heading_index(lines, heading_substring)
    if start is None:
        return []
    body: list[str] = []
    for line in lines[start + 1 :]:
        if line.startswith("## "):
            break
        body.append(line)
    return body


def strip_md(text: str) -> str:
    return text.replace("**", "").replace("`", "").strip()


def parse_table_rows(lines: list[str], start_index: int) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in lines[start_index:]:
        stripped = line.strip()
        if not stripped.startswith("|"):
            if rows:
                break
            continue
        if set(stripped.replace("|", "").replace("-", "").replace(":", "").strip()) == set():
            continue
        rows.append([cell.strip() for cell in stripped.strip("|").split("|")])
    return rows


def parse_git_state_table(lines: list[str]) -> dict[str, str]:
    body = section_body(lines, "CURRENT BRANCH / GIT STATE")
    for index, line in enumerate(body):
        if line.strip().startswith("|"):
            rows = parse_table_rows(body, index)
            result: dict[str, str] = {}
            for row in rows[1:]:
                if len(row) < 2:
                    continue
                key = strip_md(row[0])
                value = strip_md(row[1])
                result[key] = value
            return result
    return {}


def parse_documented_head(section_lines: list[str]) -> str | None:
    for line in section_lines:
        stripped = line.strip()
        if stripped.startswith("**HEAD:**"):
            remainder = stripped.split("**HEAD:**", 1)[1].strip()
            if "`" in remainder:
                return remainder.split("`", 2)[1]
    return None


def is_normative_main_head_key(key: str) -> bool:
    return strip_md(key).lower() == "main head"


def is_normative_origin_main_key(key: str) -> bool:
    return strip_md(key).lower() == "origin/main head"


def is_untracked_line(line: str) -> bool:
    return len(line) >= 3 and line[:2] == "??"


def is_staged_line(line: str) -> bool:
    return len(line) >= 2 and line[0] in "MADRCU"


def is_dirty_tracked_line(line: str) -> bool:
    if len(line) < 2:
        return False
    x, y = line[0], line[1]
    if x == "?" and y == "?":
        return False
    if x != " " and x != "?":
        return True
    return y != " " and y != "?"


def path_is_ignored(repo_root: Path, relative_path: str) -> bool:
    code, _, _ = git(repo_root, "check-ignore", "-q", "--", relative_path)
    return code == 0


def check_manifest() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []

    def add(check_id: str, category: str, mode: str, network: bool, command: str | None) -> None:
        entries.append(
            {
                "id": check_id,
                "category": category,
                "mode": mode,
                "network": network,
                "command": command,
            }
        )

    for check_id in (
        "git_branch",
        "git_head",
        "git_main_origin_parity",
        "git_ahead_behind",
        "git_remote_ls_remote",
    ):
        add(check_id, "git_sync", "fast", check_id == "git_remote_ls_remote", None)

    for check_id in (
        "worktree_staged",
        "worktree_tracked",
        "worktree_untracked",
    ):
        add(check_id, "worktree", "fast", False, None)

    add("project_state_drift", "project_state", "fast", False, None)
    add("ci_static_verify_g0b", "ci_static", "fast", False, None)
    add("pre_commit_config", "pre_commit", "fast", False, "pre-commit validate-config")
    add("rules_presence", "rules", "fast", False, None)
    add("governance_structure", "governance", "fast", False, None)
    add("evidence_policy", "evidence_policy", "fast", False, None)
    add("workflow_safety", "workflow_safety", "fast", False, None)
    add("pytest", "python_tests", "standard", False, "python3 -m pytest tests/ -q")
    add(
        "export_validation",
        "export_validation",
        "standard",
        False,
        "python3 scripts/build_daily_export.py --validate-existing tests/fixtures/reference_export_pre_promotion.json",
    )
    add("frontend_test", "frontend_tests", "standard", False, "npm test")
    add("frontend_build", "frontend_build", "standard", False, "npm run build")
    add("ci_dynamic", "ci_dynamic", "deep", True, "GitHub REST workflow runs")
    return entries


def check_git_sync(options: ScanOptions, result: ScanResult) -> None:
    cat = result.category("git_sync", "GIT SYNC")
    repo = options.repo_root
    expected_branch = options.expect_branch or "main"

    code, branch_out, _ = git(repo, "branch", "--show-current")
    branch = branch_out.strip() if code == 0 else ""
    if not branch:
        code, head_out, _ = git(repo, "rev-parse", "--abbrev-ref", "HEAD")
        branch = head_out.strip() if code == 0 else "unknown"

    head = normalize_commit(repo, "HEAD")
    main_sha = normalize_commit(repo, "main")
    origin_main_sha = normalize_commit(repo, "origin/main")

    if branch != expected_branch:
        cat.add(
            Finding(
                code="GIT_BRANCH_UNEXPECTED",
                severity=Severity.WARN,
                message=f"current branch is {branch!r}, expected {expected_branch!r}",
                expected=expected_branch,
                observed=branch,
            )
        )
    else:
        cat.add(
            Finding(
                code="GIT_BRANCH_EXPECTED",
                severity=Severity.INFO,
                message=f"on expected branch {branch!r}",
                expected=expected_branch,
                observed=branch,
            )
        )

    if branch == "HEAD" or not branch:
        cat.add(
            Finding(
                code="GIT_HEAD_DETACHED",
                severity=Severity.WARN,
                message="repository appears to be in detached HEAD state",
            )
        )

    if main_sha and origin_main_sha and main_sha != origin_main_sha:
        cat.add(
            Finding(
                code="GIT_MAIN_ORIGIN_MISMATCH",
                severity=Severity.FAIL,
                message="local main differs from origin/main",
                expected=origin_main_sha,
                observed=main_sha,
            )
        )

    if main_sha and origin_main_sha:
        code, ahead_behind, _ = git(repo, "rev-list", "--left-right", "--count", "main...origin/main")
        if code == 0:
            parts = ahead_behind.strip().split()
            if len(parts) == 2 and parts != ["0", "0"]:
                cat.add(
                    Finding(
                        code="GIT_AHEAD_BEHIND",
                        severity=Severity.FAIL,
                        message=f"main...origin/main ahead/behind = {parts[0]}/{parts[1]}",
                        expected="0/0",
                        observed=f"{parts[0]}/{parts[1]}",
                    )
                )

    if not options.no_network and not options.dry_run:
        code, remote_out, err = run_cmd(repo, ["git", "ls-remote", "origin", "refs/heads/main"])
        if code != 0:
            cat.add(
                Finding(
                    code="NETWORK_UNAVAILABLE",
                    severity=Severity.WARN,
                    message="git ls-remote origin refs/heads/main failed",
                    observed=(err or remote_out).strip() or f"exit {code}",
                )
            )
        else:
            remote_line = remote_out.strip().splitlines()
            remote_sha = remote_line[0].split()[0] if remote_line else None
            if remote_sha and origin_main_sha and remote_sha != origin_main_sha:
                cat.add(
                    Finding(
                        code="GIT_REMOTE_LS_REMOTE_MISMATCH",
                        severity=Severity.WARN,
                        message="local origin/main ref differs from live remote main (local refs not updated)",
                        expected=remote_sha,
                        observed=origin_main_sha,
                    )
                )
            elif remote_sha and main_sha and remote_sha != main_sha:
                cat.add(
                    Finding(
                        code="GIT_MAIN_ORIGIN_MISMATCH",
                        severity=Severity.FAIL,
                        message="local main differs from live remote main",
                        expected=remote_sha,
                        observed=main_sha,
                    )
                )
    elif options.no_network:
        cat.add(
            Finding(
                code="NETWORK_UNAVAILABLE",
                severity=Severity.INFO,
                message="remote ls-remote skipped (--no-network); using local origin/main only",
            )
        )


def check_worktree(options: ScanOptions, result: ScanResult) -> None:
    cat = result.category("worktree", "WORKTREE")
    repo = options.repo_root

    _, status_out, _ = git(repo, "status", "--porcelain")
    status_lines = [line for line in status_out.splitlines() if line.strip()]

    _, staged_out, _ = git(repo, "diff", "--cached", "--name-only")
    staged_files = [line.strip() for line in staged_out.splitlines() if line.strip()]

    for path in staged_files:
        cat.add(
            Finding(
                code="WORKTREE_STAGED_CHANGE",
                severity=Severity.FAIL,
                message=f"staged file: {path}",
                observed=path,
            )
        )

    for line in status_lines:
        if not is_dirty_tracked_line(line):
            continue
        path = line[3:].strip()
        cat.add(
            Finding(
                code="WORKTREE_TRACKED_MODIFICATION",
                severity=Severity.FAIL,
                message=f"tracked modification: {path}",
                observed=path,
            )
        )

    for line in status_lines:
        if not is_untracked_line(line):
            continue
        path = line[3:].strip()
        if matches_known_untracked(path):
            cat.add(
                Finding(
                    code="WORKTREE_KNOWN_EVIDENCE",
                    severity=Severity.INFO,
                    message=f"known untracked evidence metadata: {path}",
                    observed=path,
                )
            )
            continue
        if path.startswith("evidence/"):
            cat.add(
                Finding(
                    code="WORKTREE_UNEXPECTED_EVIDENCE",
                    severity=Severity.WARN,
                    message=f"unexpected untracked evidence path: {path}",
                    observed=path,
                )
            )
            continue
        if path_is_ignored(repo, path):
            cat.add(
                Finding(
                    code="WORKTREE_IGNORED_ARTIFACT",
                    severity=Severity.INFO,
                    message=f"untracked gitignored artifact: {path}",
                    observed=path,
                )
            )
            continue
        cat.add(
            Finding(
                code="WORKTREE_UNEXPECTED_UNTRACKED",
                severity=Severity.WARN,
                message=f"unexpected untracked non-ignored file: {path}",
                observed=path,
            )
        )


def check_project_state(options: ScanOptions, result: ScanResult) -> None:
    cat = result.category("project_state", "PROJECT_STATE")
    repo = options.repo_root
    path = repo / "PROJECT_STATE.md"
    if not path.is_file():
        cat.add(
            Finding(
                code="PROJECT_STATE_MISSING",
                severity=Severity.FAIL,
                message="PROJECT_STATE.md is missing",
            )
        )
        return

    lines = read_lines(path)
    verified_section = section_body(lines, "VERIFIED CURRENT STATE")
    git_table = parse_git_state_table(lines)

    live_branch = None
    code, branch_out, _ = git(repo, "branch", "--show-current")
    if code == 0:
        live_branch = branch_out.strip()

    documented_active_branch = first_content_after_heading(lines, "Active Branch")
    documented_head = parse_documented_head(verified_section)
    documented_worktree = None
    deprecated_normative_claims: list[str] = []

    if documented_head:
        deprecated_normative_claims.append(
            "**HEAD:** normative claim in VERIFIED CURRENT STATE"
        )

    for key, value in git_table.items():
        lower = key.lower()
        if is_normative_main_head_key(key):
            deprecated_normative_claims.append("`main` HEAD table row")
        elif is_normative_origin_main_key(key):
            deprecated_normative_claims.append("`origin/main` HEAD table row")
        elif "working tree" in lower:
            documented_worktree = value

    for claim in deprecated_normative_claims:
        cat.add(
            Finding(
                code="PROJECT_STATE_NORMATIVE_HEAD_DEPRECATED",
                severity=Severity.WARN,
                message="deprecated exact-SHA live HEAD claim; Git is authoritative",
                observed=claim,
            )
        )

    if documented_active_branch and live_branch:
        active = documented_active_branch.strip("`")
        if active != live_branch:
            cat.add(
                Finding(
                    code="PROJECT_STATE_BRANCH_MISMATCH",
                    severity=Severity.FAIL,
                    message="Active Branch claim differs from live branch",
                    expected=live_branch,
                    observed=active,
                )
            )

    if documented_worktree:
        _, status_out, _ = git(repo, "status", "--porcelain")
        has_tracked = any(is_dirty_tracked_line(line) for line in status_out.splitlines())
        has_staged = any(is_staged_line(line) for line in status_out.splitlines())
        untracked = [
            line[3:].strip()
            for line in status_out.splitlines()
            if is_untracked_line(line)
        ]
        claim = documented_worktree.lower()
        if "clean" in claim and (has_tracked or has_staged):
            cat.add(
                Finding(
                    code="PROJECT_STATE_WORKTREE_MISMATCH",
                    severity=Severity.FAIL,
                    message="PROJECT_STATE claims clean working tree but tracked changes exist",
                    expected=documented_worktree,
                    observed="dirty tracked tree",
                )
            )
        elif "clean except untracked" in claim:
            allowed = re.findall(r"`([^`]+)`", documented_worktree)
            unexpected = [
                p
                for p in untracked
                if p not in allowed
                and not matches_known_untracked(p)
            ]
            if has_tracked or has_staged:
                cat.add(
                    Finding(
                        code="PROJECT_STATE_WORKTREE_MISMATCH",
                        severity=Severity.FAIL,
                        message="PROJECT_STATE worktree claim conflicts with live git status",
                        expected=documented_worktree,
                        observed="tracked or staged changes present",
                    )
                )
            elif unexpected:
                cat.add(
                    Finding(
                        code="PROJECT_STATE_WORKTREE_MISMATCH",
                        severity=Severity.WARN,
                        message="PROJECT_STATE worktree claim omits unexpected untracked paths",
                        expected=documented_worktree,
                        observed=", ".join(unexpected),
                    )
                )


def check_ci_static(options: ScanOptions, result: ScanResult) -> None:
    cat = result.category("ci_static", "CI STATIC")
    workflow = options.repo_root / ".github/workflows/verify-g0b.yml"
    if not workflow.is_file():
        cat.add(
            Finding(
                code="CI_WORKFLOW_MISSING",
                severity=Severity.FAIL,
                message="verify-g0b workflow is missing",
            )
        )
        return

    text = workflow.read_text(encoding="utf-8")
    if "permissions:" not in text or "contents: read" not in text:
        cat.add(
            Finding(
                code="CI_PERMISSIONS_UNSAFE",
                severity=Severity.FAIL,
                message="verify-g0b workflow missing contents: read permission",
            )
        )
    if "contents: write" in text:
        cat.add(
            Finding(
                code="CI_PERMISSIONS_UNSAFE",
                severity=Severity.FAIL,
                message="verify-g0b workflow contains contents: write",
            )
        )

    for needle, step_code in (
        ("pytest", "CI_STEP_MISSING"),
        ("--validate-existing", "CI_STEP_MISSING"),
        ("npm run build", "CI_STEP_MISSING"),
    ):
        if needle not in text:
            cat.add(
                Finding(
                    code=step_code,
                    severity=Severity.FAIL,
                    message=f"verify-g0b workflow missing {needle!r} step",
                )
            )

    if "branches: [main]" not in text.replace(" ", "") and "branches:[main]" not in text.replace(
        " ", ""
    ):
        if "branches:" not in text or "main" not in text:
            cat.add(
                Finding(
                    code="CI_TRIGGER_MISSING",
                    severity=Severity.FAIL,
                    message="verify-g0b workflow missing main branch trigger",
                )
            )


def check_pre_commit(options: ScanOptions, result: ScanResult) -> None:
    cat = result.category("pre_commit", "PRE-COMMIT")
    repo = options.repo_root
    config = repo / ".pre-commit-config.yaml"
    if not config.is_file():
        cat.add(
            Finding(
                code="PRE_COMMIT_CONFIG_MISSING",
                severity=Severity.FAIL,
                message=".pre-commit-config.yaml is missing",
            )
        )
        return

    hook = repo / ".git/hooks/pre-commit"
    if not hook.is_file():
        cat.add(
            Finding(
                code="PRE_COMMIT_HOOK_MISSING",
                severity=Severity.WARN,
                message="local .git/hooks/pre-commit is missing",
            )
        )

    pre_commit = shutil.which("pre-commit")
    if not pre_commit:
        cat.add(
            Finding(
                code="PRE_COMMIT_CLI_MISSING",
                severity=Severity.WARN,
                message="pre-commit executable not found in PATH",
            )
        )
        return

    if options.dry_run:
        cat.add(
            Finding(
                code="PRE_COMMIT_VALIDATE_PLANNED",
                severity=Severity.INFO,
                message="pre-commit validate-config planned",
            )
        )
        return

    try:
        code, stdout, stderr = run_cmd(repo, [pre_commit, "validate-config", str(config)])
    except (OSError, subprocess.TimeoutExpired) as exc:
        cat.add(
            Finding(
                code="PRE_COMMIT_VALIDATE_UNAVAILABLE",
                severity=Severity.WARN,
                message=f"pre-commit validate-config could not run: {exc}",
            )
        )
        return

    if code != 0:
        detail = (stderr or stdout).strip()
        if "PermissionError" in detail or "Operation not permitted" in detail:
            cat.add(
                Finding(
                    code="PRE_COMMIT_VALIDATE_UNAVAILABLE",
                    severity=Severity.WARN,
                    message="pre-commit validate-config unavailable in this environment",
                    observed=detail.splitlines()[-1] if detail else f"exit {code}",
                )
            )
            return
        cat.add(
            Finding(
                code="PRE_COMMIT_CONFIG_INVALID",
                severity=Severity.FAIL,
                message="pre-commit validate-config failed",
                observed=detail or f"exit {code}",
            )
        )


def parse_rule_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    front = text[3:end]
    data: dict[str, str] = {}
    for line in front.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def check_rules(options: ScanOptions, result: ScanResult) -> None:
    cat = result.category("rules", "RULES")
    repo = options.repo_root
    for relative in REQUIRED_RULES:
        path = repo / relative
        if not path.is_file():
            cat.add(
                Finding(
                    code="RULE_MISSING",
                    severity=Severity.FAIL,
                    message=f"required rule file missing: {relative}",
                )
            )
            continue
        front = parse_rule_frontmatter(path)
        always_apply = front.get("alwaysApply", "").lower()
        if always_apply != "true":
            cat.add(
                Finding(
                    code="RULE_ALWAYS_APPLY_DRIFT",
                    severity=Severity.WARN,
                    message=f"{relative} alwaysApply is not true",
                    expected="true",
                    observed=always_apply or "missing",
                )
            )


def check_governance(options: ScanOptions, result: ScanResult) -> None:
    cat = result.category("governance", "GOVERNANCE")
    repo = options.repo_root
    agents = repo / "AGENTS.md"
    contract = repo / ".cursor/templates/task-contract.md"

    if not agents.is_file():
        cat.add(
            Finding(
                code="GOVERNANCE_FILE_MISSING",
                severity=Severity.FAIL,
                message="AGENTS.md is missing",
            )
        )
    else:
        agents_text = agents.read_text(encoding="utf-8").lower()
        if not any(marker in agents_text for marker in AGENTS_MARKERS):
            cat.add(
                Finding(
                    code="GOVERNANCE_STRUCTURE_MISSING",
                    severity=Severity.FAIL,
                    message="AGENTS.md missing orchestration/task-contract references",
                )
            )

    if not contract.is_file():
        cat.add(
            Finding(
                code="GOVERNANCE_FILE_MISSING",
                severity=Severity.FAIL,
                message="task-contract template is missing",
            )
        )
    else:
        contract_text = contract.read_text(encoding="utf-8")
        missing = [marker for marker in TASK_CONTRACT_MARKERS if marker not in contract_text]
        if missing:
            cat.add(
                Finding(
                    code="GOVERNANCE_STRUCTURE_MISSING",
                    severity=Severity.FAIL,
                    message=f"task-contract missing markers: {', '.join(missing)}",
                    observed=", ".join(missing),
                )
            )


def check_evidence_policy(options: ScanOptions, result: ScanResult) -> None:
    cat = result.category("evidence_policy", "EVIDENCE POLICY")
    repo = options.repo_root

    gitignore = repo / ".gitignore"
    if not gitignore.is_file() or RAW_EVIDENCE_GITIGNORE not in gitignore.read_text(
        encoding="utf-8"
    ):
        cat.add(
            Finding(
                code="EVIDENCE_GITIGNORE_MISSING",
                severity=Severity.FAIL,
                message=f".gitignore missing {RAW_EVIDENCE_GITIGNORE!r} rule",
            )
        )

    _, tracked_out, _ = git(repo, "ls-files", "evidence")
    for path in tracked_out.splitlines():
        if path.endswith(".raw.json"):
            cat.add(
                Finding(
                    code="EVIDENCE_RAW_TRACKED",
                    severity=Severity.FAIL,
                    message=f"tracked raw evidence file: {path}",
                    observed=path,
                )
            )

    _, staged_out, _ = git(repo, "diff", "--cached", "--name-only", "--", "evidence")
    for path in staged_out.splitlines():
        if path.endswith(".raw.json"):
            cat.add(
                Finding(
                    code="EVIDENCE_RAW_STAGED",
                    severity=Severity.FAIL,
                    message=f"staged raw evidence file: {path}",
                    observed=path,
                )
            )


def check_workflow_safety(options: ScanOptions, result: ScanResult) -> None:
    cat = result.category("workflow_safety", "WORKFLOW SAFETY")
    repo = options.repo_root
    workflows = {
        "verify-g0b.yml": repo / ".github/workflows/verify-g0b.yml",
        "daily-run.yml": repo / ".github/workflows/daily-run.yml",
        "run-mlb-lab.yml": repo / ".github/workflows/run-mlb-lab.yml",
    }

    verify = workflows["verify-g0b.yml"]
    if verify.is_file():
        text = verify.read_text(encoding="utf-8")
        if re.search(r"contents:\s*write", text):
            cat.add(
                Finding(
                    code="WORKFLOW_VERIFY_WRITE_PERMS",
                    severity=Severity.FAIL,
                    message="verify-g0b workflow has write permissions",
                )
            )

    for name in ("daily-run.yml", "run-mlb-lab.yml"):
        path = workflows[name]
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8").lower()
        if "git push" in text or "git commit" in text:
            cat.add(
                Finding(
                    code="WORKFLOW_LEGACY_MUTATING",
                    severity=Severity.WARN,
                    message=f"{name} contains repository mutation behavior (commit/push)",
                    observed=name,
                )
            )


def run_verification_command(
    options: ScanOptions,
    cat: CategoryResult,
    *,
    check_id: str,
    command: list[str],
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
    fail_code: str,
    skip_code: str,
    skip_message: str | None = None,
    skip_if: Callable[[], bool] | None = None,
) -> None:
    if skip_if and skip_if():
        cat.add(
            Finding(
                code=skip_code,
                severity=Severity.SKIP,
                message=skip_message or f"{check_id} skipped",
            )
        )
        return

    if options.dry_run:
        cat.add(
            Finding(
                code=f"{check_id.upper()}_PLANNED",
                severity=Severity.INFO,
                message=f"planned command: {' '.join(command)}",
            )
        )
        return

    try:
        code, stdout, stderr = run_cmd(options.repo_root, command, cwd=cwd, env=env)
    except (OSError, subprocess.TimeoutExpired) as exc:
        cat.add(
            Finding(
                code="SCAN_SUBPROCESS_ERROR",
                severity=Severity.ERROR,
                message=f"{check_id} subprocess failed: {exc}",
            )
        )
        return

    if code != 0:
        detail = (stderr or stdout).strip()
        cat.add(
            Finding(
                code=fail_code,
                severity=Severity.FAIL,
                message=f"{check_id} failed",
                observed=detail or f"exit {code}",
            )
        )
        if options.verbose and detail:
            print(detail, file=sys.stderr)


def check_standard_verifications(options: ScanOptions, result: ScanResult) -> None:
    repo = options.repo_root
    pytest_cat = result.category("python_tests", "PYTEST")
    export_cat = result.category("export_validation", "EXPORT VALIDATION")
    frontend_test_cat = result.category("frontend_tests", "FRONTEND TESTS")
    frontend_build_cat = result.category("frontend_build", "FRONTEND BUILD")

    fixture = repo / "tests/fixtures/reference_export_pre_promotion.json"
    export_cmd = [
        sys.executable,
        str(repo / "scripts/build_daily_export.py"),
        "--validate-existing",
        str(fixture),
    ]

    with tempfile.TemporaryDirectory(prefix="repo-health-pytest-") as tmp:
        pytest_env = {
            "PYTHONDONTWRITEBYTECODE": "1",
        }
        pytest_cmd = [
            sys.executable,
            "-m",
            "pytest",
            "tests/",
            "-q",
            "--basetemp",
            tmp,
        ]
        run_verification_command(
            options,
            pytest_cat,
            check_id="pytest",
            command=pytest_cmd,
            env=pytest_env,
            fail_code="PYTEST_FAIL",
            skip_code="PYTEST_SKIP",
            skip_message="pytest unavailable",
            skip_if=lambda: shutil.which(sys.executable) is None,
        )

    run_verification_command(
        options,
        export_cat,
        check_id="export_validation",
        command=export_cmd,
        fail_code="EXPORT_VALIDATION_FAIL",
        skip_code="EXPORT_VALIDATION_SKIP",
        skip_if=lambda: not fixture.is_file(),
        skip_message="export fixture missing",
    )

    dashboard = repo / "web-dashboard"
    node_modules = dashboard / "node_modules"
    npm = shutil.which("npm")

    def frontend_skip() -> bool:
        if not npm:
            return True
        if not node_modules.is_dir():
            return True
        return False

    if frontend_skip():
        msg = "npm not found in PATH" if not npm else "web-dashboard/node_modules missing; npm ci not run by scanner"
        frontend_test_cat.add(
            Finding(code="FRONTEND_TEST_SKIP", severity=Severity.SKIP, message=msg)
        )
        frontend_build_cat.add(
            Finding(
                code="FRONTEND_BUILD_SKIP",
                severity=Severity.SKIP,
                message=f"{msg}; build also mutates dist/ and public/data",
            )
        )
    else:
        run_verification_command(
            options,
            frontend_test_cat,
            check_id="frontend_test",
            command=[npm, "test"],
            cwd=dashboard,
            fail_code="FRONTEND_TEST_FAIL",
            skip_code="FRONTEND_TEST_SKIP",
            skip_message="frontend tests skipped",
        )
        frontend_build_cat.add(
            Finding(
                code="FRONTEND_BUILD_SKIP",
                severity=Severity.SKIP,
                message="npm run build skipped: prebuild sync-data mutates web-dashboard/public/data and dist/",
            )
        )


def fetch_github_json(url: str, timeout: int = 15) -> dict[str, Any] | None:
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "mlb-lab-repo-health"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, TimeoutError):
        return None


def check_ci_dynamic(options: ScanOptions, result: ScanResult) -> None:
    cat = result.category("ci_dynamic", "CI DYNAMIC")
    if options.no_network:
        cat.add(
            Finding(
                code="NETWORK_UNAVAILABLE",
                severity=Severity.INFO,
                message="CI dynamic checks skipped (--no-network)",
            )
        )
        return

    remote_url_code, remote_url, _ = git(options.repo_root, "remote", "get-url", "origin")
    if remote_url_code != 0:
        cat.add(
            Finding(
                code="NETWORK_UNAVAILABLE",
                severity=Severity.WARN,
                message="unable to determine origin remote URL",
            )
        )
        return

    match = re.search(r"github\.com[:/](?P<owner>[^/]+)/(?P<repo>[^/.]+)", remote_url.strip())
    if not match:
        cat.add(
            Finding(
                code="NETWORK_UNAVAILABLE",
                severity=Severity.INFO,
                message="origin is not a GitHub repository URL; skipping workflow API checks",
            )
        )
        return

    owner = match.group("owner")
    repo_name = match.group("repo")
    head = normalize_commit(options.repo_root, "HEAD")
    if not head:
        return

    commit_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits/{head}"
    commit_data = fetch_github_json(commit_url)
    if commit_data and isinstance(commit_data, dict) and commit_data.get("sha", "").startswith(head[:12]):
        cat.add(
            Finding(
                code="CI_DYNAMIC_PASS",
                severity=Severity.INFO,
                message="remote GitHub main commit matches local HEAD prefix",
                observed=commit_data.get("sha"),
            )
        )

    runs_url = (
        f"https://api.github.com/repos/{owner}/{repo_name}/actions/workflows/"
        "verify-g0b.yml/runs?branch=main&per_page=1"
    )
    runs_data = fetch_github_json(runs_url)
    if not runs_data:
        cat.add(
            Finding(
                code="NETWORK_UNAVAILABLE",
                severity=Severity.WARN,
                message="unable to fetch Verify G0b workflow runs from GitHub API",
            )
        )
        return

    runs = runs_data.get("workflow_runs", [])
    if not runs:
        cat.add(
            Finding(
                code="CI_DYNAMIC_WARN",
                severity=Severity.WARN,
                message="no Verify G0b workflow runs found for main",
            )
        )
        return

    latest = runs[0]
    conclusion = latest.get("conclusion")
    if conclusion == "success":
        cat.add(
            Finding(
                code="CI_DYNAMIC_PASS",
                severity=Severity.INFO,
                message="latest Verify G0b workflow run succeeded",
                observed=str(latest.get("html_url") or conclusion),
            )
        )
    elif conclusion in (None, "pending", "in_progress", "queued"):
        cat.add(
            Finding(
                code="CI_DYNAMIC_WARN",
                severity=Severity.WARN,
                message=f"latest Verify G0b workflow run is {conclusion or 'incomplete'}",
            )
        )
    else:
        cat.add(
            Finding(
                code="CI_DYNAMIC_FAIL",
                severity=Severity.FAIL,
                message=f"latest Verify G0b workflow run conclusion is {conclusion}",
                observed=str(latest.get("html_url") or conclusion),
            )
        )


def run_scan(options: ScanOptions) -> ScanResult:
    started = time.monotonic()
    result = ScanResult(options=options)

    fast_checks = (
        check_git_sync,
        check_worktree,
        check_project_state,
        check_ci_static,
        check_pre_commit,
        check_rules,
        check_governance,
        check_evidence_policy,
        check_workflow_safety,
    )

    for check in fast_checks:
        try:
            check(options, result)
        except Exception as exc:  # noqa: BLE001 - convert to scan error
            cat = result.category("scan_error", "SCAN ERROR")
            cat.add(
                Finding(
                    code="SCAN_SUBPROCESS_ERROR",
                    severity=Severity.ERROR,
                    message=f"{check.__name__} raised {exc!r}",
                )
            )
            result.scan_error = True

    if options.mode in {"standard", "deep"}:
        try:
            check_standard_verifications(options, result)
        except Exception as exc:  # noqa: BLE001
            cat = result.category("scan_error", "SCAN ERROR")
            cat.add(
                Finding(
                    code="SCAN_SUBPROCESS_ERROR",
                    severity=Severity.ERROR,
                    message=f"standard verification raised {exc!r}",
                )
            )
            result.scan_error = True

    if options.mode == "deep":
        try:
            check_ci_dynamic(options, result)
        except Exception as exc:  # noqa: BLE001
            cat = result.category("scan_error", "SCAN ERROR")
            cat.add(
                Finding(
                    code="SCAN_SUBPROCESS_ERROR",
                    severity=Severity.ERROR,
                    message=f"ci dynamic raised {exc!r}",
                )
            )
            result.scan_error = True

    result.duration_seconds = round(time.monotonic() - started, 3)
    return result


def print_human(result: ScanResult) -> None:
    print("MLB-LAB HEALTH SCAN")
    print()
    for cat in result.categories:
        label = cat.title.upper()
        status = SEVERITY_LABEL[cat.status].upper()
        dots = max(1, 24 - len(label))
        print(f"{label} {'.' * dots} {status}")

    print()
    print(f"OVERALL {'.' * 17} {SEVERITY_LABEL[result.overall].upper()}")
    print()

    actionable = [
        f
        for cat in result.categories
        for f in cat.findings
        if f.severity in (Severity.WARN, Severity.FAIL, Severity.ERROR, Severity.SKIP)
    ]
    if actionable:
        print("Findings:")
        for finding in actionable:
            suffix = ""
            if finding.expected or finding.observed:
                parts = []
                if finding.expected:
                    parts.append(f"expected={finding.expected}")
                if finding.observed:
                    parts.append(f"observed={finding.observed}")
                suffix = f" ({', '.join(parts)})"
            print(f"- [{finding.code}] {finding.message}{suffix}")


def print_json(result: ScanResult) -> None:
    payload = {
        "scan_version": SCAN_VERSION,
        "mode": result.options.mode,
        "overall": SEVERITY_LABEL[result.overall],
        "exit_code": result.exit_code,
        "duration_seconds": result.duration_seconds,
        "categories": [cat.to_dict() for cat in result.categories],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


def print_manifest() -> None:
    print(json.dumps({"scan_version": SCAN_VERSION, "checks": check_manifest()}, indent=2))


def print_dry_run(options: ScanOptions) -> None:
    print("MLB-LAB HEALTH SCAN (dry-run)")
    for entry in check_manifest():
        if entry["mode"] == "fast":
            include = options.mode == "fast"
        elif entry["mode"] == "standard":
            include = options.mode in {"standard", "deep"}
        else:
            include = options.mode == "deep"
        if not include:
            continue
        if entry["network"] and options.no_network:
            status = "skipped (--no-network)"
        else:
            status = entry["command"] or "static inspection"
        print(f"- {entry['id']} [{entry['category']}]: {status}")


def find_repo_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    raise FileNotFoundError("unable to locate git repository root")


def parse_args(argv: list[str] | None = None) -> ScanOptions:
    parser = argparse.ArgumentParser(description="Read-only MLB-LAB repository health scanner")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--fast", action="store_const", const="fast", dest="scan_mode")
    mode.add_argument("--standard", action="store_const", const="standard", dest="scan_mode")
    mode.add_argument("--deep", action="store_const", const="deep", dest="scan_mode")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--no-fetch", action="store_true", help="never update remote-tracking refs")
    parser.add_argument("--no-network", action="store_true", help="disable network/API checks")
    parser.add_argument("--expect-branch", default=None, help="expected current branch")
    parser.add_argument("--verbose", action="store_true", help="include subprocess details")
    parser.add_argument("--version", action="store_true", help="print scanner version")
    parser.add_argument("--manifest", action="store_true", help="print check manifest JSON")
    parser.add_argument("--dry-run", action="store_true", help="print planned commands only")
    parser.add_argument(
        "--repo-root",
        default=None,
        help="repository root (defaults to current git root)",
    )
    args = parser.parse_args(argv)

    if args.version:
        print(SCAN_VERSION)
        raise SystemExit(0)
    if args.manifest:
        print_manifest()
        raise SystemExit(0)

    repo_root = Path(args.repo_root).resolve() if args.repo_root else find_repo_root()
    return ScanOptions(
        mode=args.scan_mode or "fast",
        json_output=args.json,
        no_fetch=args.no_fetch,
        no_network=args.no_network,
        expect_branch=args.expect_branch,
        verbose=args.verbose,
        dry_run=args.dry_run,
        repo_root=repo_root,
    )


def main(argv: list[str] | None = None) -> int:
    options = parse_args(argv)
    if options.dry_run and not options.json_output:
        print_dry_run(options)
        return 0

    result = run_scan(options)
    if options.json_output:
        print_json(result)
    else:
        print_human(result)

    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
