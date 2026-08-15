#!/usr/bin/env python3
"""Deterministic read-only repository context summary for AI coding agents."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


IMPORTANT_FILES = (
    "AGENTS.md",
    "PROJECT_STATE.md",
    "README.md",
)

IMPORTANT_DIRS = (
    "docs",
    ".cursor/rules",
)

TEST_CONFIG_FILES = (
    "pytest.ini",
    "pyproject.toml",
    "tox.ini",
    "setup.cfg",
)

EVIDENCE_DIRS = (
    "data",
    "tmp",
    "artifacts",
)

STATUS_HEADINGS = (
    "Stable Milestone",
    "Active Phase",
    "Active Branch",
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Emit a deterministic read-only summary of repository context."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the same information as JSON",
    )
    return parser.parse_args(argv)


def run_git(repo_root: Path, *args: str) -> tuple[int, str, str]:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode, result.stdout, result.stderr


def find_repo_root(start: Path) -> Path | None:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


def git_branch(repo_root: Path) -> str:
    code, stdout, _ = run_git(repo_root, "branch", "--show-current")
    if code != 0:
        return "unknown"
    branch = stdout.strip()
    return branch if branch else "unknown"


def git_status_short(repo_root: Path) -> list[str]:
    code, stdout, _ = run_git(repo_root, "status", "--short")
    if code != 0:
        return []
    return [line for line in stdout.splitlines() if line.strip()]


def git_recent_commits(repo_root: Path, count: int = 5) -> list[dict[str, str]]:
    code, stdout, _ = run_git(
        repo_root,
        "log",
        f"-{count}",
        "--format=%H|%h|%s",
    )
    if code != 0:
        return []

    commits: list[dict[str, str]] = []
    for line in stdout.splitlines():
        if not line.strip():
            continue
        full_hash, short_hash, subject = line.split("|", 2)
        commits.append(
            {
                "hash": short_hash,
                "full_hash": full_hash,
                "subject": subject,
            }
        )
    return commits


def path_exists(repo_root: Path, relative: str) -> bool:
    return (repo_root / relative).exists()


def project_state_summary(repo_root: Path) -> str | None:
    path = repo_root / "PROJECT_STATE.md"
    if not path.is_file():
        return None

    lines = path.read_text(encoding="utf-8").splitlines()
    for heading in STATUS_HEADINGS:
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
                return f"{heading}: {stripped}"
    return None


def detect_test_configs(repo_root: Path) -> dict[str, bool]:
    return {name: path_exists(repo_root, name) for name in TEST_CONFIG_FILES}


def is_untracked_status_line(line: str) -> bool:
    return line.startswith("??")


def is_dirty_status_line(line: str) -> bool:
    if is_untracked_status_line(line):
        return False
    status = line[:2]
    return any(marker in status for marker in ("M", "A", "D", "R", "C", "U"))


def untracked_evidence_artifacts(
    repo_root: Path, status_lines: list[str]
) -> dict[str, list[str]]:
    findings: dict[str, list[str]] = {}
    for directory in EVIDENCE_DIRS:
        prefix = f"{directory}/"
        matches = []
        for line in status_lines:
            if not is_untracked_status_line(line):
                continue
            path = line[3:].strip()
            if path == directory or path.startswith(prefix):
                matches.append(path)
        findings[directory] = sorted(matches)
    return findings


def is_evidence_related(relative_path: str) -> bool:
    lowered = relative_path.lower()
    if "evidence" in lowered:
        return True
    for directory in EVIDENCE_DIRS:
        if lowered == directory or lowered.startswith(f"{directory}/"):
            return True
    return False


def recent_evidence_files(repo_root: Path, limit: int = 10) -> list[dict[str, str]]:
    candidates: list[tuple[float, str, Path]] = []

    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(repo_root).as_posix()
        if relative.startswith(".git/"):
            continue
        if not is_evidence_related(relative):
            continue
        candidates.append((path.stat().st_mtime, relative, path))

    candidates.sort(key=lambda item: (-item[0], item[1]))

    recent: list[dict[str, str]] = []
    for mtime, relative, _ in candidates[:limit]:
        timestamp = datetime.fromtimestamp(mtime, tz=timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        recent.append({"path": relative, "modified_utc": timestamp})
    return recent


def build_context(repo_root: Path) -> dict[str, Any]:
    status_lines = git_status_short(repo_root)
    dirty = any(is_dirty_status_line(line) for line in status_lines)
    untracked = any(is_untracked_status_line(line) for line in status_lines)

    important_files = {name: path_exists(repo_root, name) for name in IMPORTANT_FILES}
    important_dirs = {name: path_exists(repo_root, name) for name in IMPORTANT_DIRS}

    project_state_present = important_files["PROJECT_STATE.md"]
    agent_rules_present = (
        important_files["AGENTS.md"] and important_dirs[".cursor/rules"]
    )

    evidence_untracked = untracked_evidence_artifacts(repo_root, status_lines)
    recent_evidence = recent_evidence_files(repo_root)

    ready_for_review = project_state_present and agent_rules_present

    return {
        "repository_root": str(repo_root),
        "branch": git_branch(repo_root),
        "git_status_short": status_lines,
        "recent_commits": git_recent_commits(repo_root),
        "important_files": important_files,
        "important_dirs": important_dirs,
        "project_state_summary": project_state_summary(repo_root),
        "test_configs": detect_test_configs(repo_root),
        "untracked_evidence_artifacts": evidence_untracked,
        "recent_evidence_files": recent_evidence,
        "repo_context_status": {
            "branch": git_branch(repo_root),
            "dirty": dirty,
            "untracked": untracked,
            "project_state_present": project_state_present,
            "agent_rules_present": agent_rules_present,
            "recent_evidence_artifacts": len(recent_evidence),
            "ready_for_implementation_review": ready_for_review,
        },
    }


def print_text(context: dict[str, Any]) -> None:
    print(f"Repository root: {context['repository_root']}")
    print(f"Current branch: {context['branch']}")
    print()
    print("Git status --short:")
    if context["git_status_short"]:
        for line in context["git_status_short"]:
            print(line)
    else:
        print("(clean)")
    print()
    print("Recent commits:")
    for commit in context["recent_commits"]:
        print(f"  {commit['hash']} {commit['subject']}")
    if not context["recent_commits"]:
        print("  (none)")
    print()
    print("Important project files:")
    for name, present in context["important_files"].items():
        print(f"  {name}: {'present' if present else 'missing'}")
    print()
    print("Important project directories:")
    for name, present in context["important_dirs"].items():
        print(f"  {name}/: {'present' if present else 'missing'}")
    print()
    print("PROJECT_STATE summary:")
    summary = context["project_state_summary"]
    print(f"  {summary if summary else '(not available)'}")
    print()
    print("Test configuration:")
    for name, present in context["test_configs"].items():
        print(f"  {name}: {'present' if present else 'missing'}")
    print()
    print("Untracked evidence artifacts:")
    for directory, paths in context["untracked_evidence_artifacts"].items():
        if paths:
            print(f"  {directory}/:")
            for path in paths:
                print(f"    {path}")
        else:
            print(f"  {directory}/: (none)")
    print()
    print("Recent evidence-related files:")
    if context["recent_evidence_files"]:
        for item in context["recent_evidence_files"]:
            print(f"  {item['modified_utc']} {item['path']}")
    else:
        print("  (none)")
    print()
    status = context["repo_context_status"]
    print("REPO_CONTEXT_STATUS")
    print(f"BRANCH: {status['branch']}")
    print(f"DIRTY: {'YES' if status['dirty'] else 'NO'}")
    print(f"UNTRACKED: {'YES' if status['untracked'] else 'NO'}")
    print(f"PROJECT_STATE_PRESENT: {'YES' if status['project_state_present'] else 'NO'}")
    print(f"AGENT_RULES_PRESENT: {'YES' if status['agent_rules_present'] else 'NO'}")
    print(f"RECENT_EVIDENCE_ARTIFACTS: {status['recent_evidence_artifacts']}")
    print(
        "READY_FOR_IMPLEMENTATION_REVIEW: "
        f"{'YES' if status['ready_for_implementation_review'] else 'NO'}"
    )


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repo_root = find_repo_root(Path.cwd())
    if repo_root is None:
        print("error: not inside a git repository", file=sys.stderr)
        return 1

    context = build_context(repo_root)
    if args.json:
        print(json.dumps(context, indent=2, sort_keys=True))
    else:
        print_text(context)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
