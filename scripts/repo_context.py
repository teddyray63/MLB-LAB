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

HERMES_SCHEMA_VERSION = "0.1"

HERMES_SOURCE_FILES = (
    "PROJECT_STATE.md",
    "docs/DECISIONS.md",
    "AGENTS.md",
    "git",
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
    parser.add_argument(
        "--hermes-json",
        action="store_true",
        help="Emit Hermes project-context v0.1 JSON (stdout only)",
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


def git_head(repo_root: Path) -> str | None:
    code, stdout, _ = run_git(repo_root, "rev-parse", "HEAD")
    if code != 0:
        return None
    head = stdout.strip()
    return head if head else None


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


def read_project_state_lines(repo_root: Path) -> list[str]:
    path = repo_root / "PROJECT_STATE.md"
    if not path.is_file():
        raise FileNotFoundError(f"PROJECT_STATE.md not found under {repo_root}")
    return path.read_text(encoding="utf-8").splitlines()


def project_state_summary(repo_root: Path) -> str | None:
    try:
        lines = read_project_state_lines(repo_root)
    except FileNotFoundError:
        return None

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


def _find_heading_index(lines: list[str], heading_text: str) -> int | None:
    for index, line in enumerate(lines):
        if line.startswith("## ") and heading_text in line:
            return index
    return None


def _first_content_line_after_heading(lines: list[str], heading: str) -> str | None:
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
            return stripped
    return None


def _section_body_lines(lines: list[str], heading_substring: str) -> list[str]:
    start = _find_heading_index(lines, heading_substring)
    if start is None:
        return []
    body: list[str] = []
    for line in lines[start + 1 :]:
        if line.startswith("## "):
            break
        body.append(line)
    return body


def _strip_markdown_emphasis(text: str) -> str:
    return text.replace("**", "").replace("`", "").strip()


def _parse_markdown_table_rows(lines: list[str], start_index: int) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in lines[start_index:]:
        stripped = line.strip()
        if not stripped.startswith("|"):
            if rows:
                break
            continue
        if set(stripped.replace("|", "").replace("-", "").replace(":", "").strip()) == set():
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        rows.append(cells)
    return rows


def _table_after_marker(lines: list[str], marker: str) -> dict[str, str]:
    for index, line in enumerate(lines):
        if marker not in line:
            continue
        for offset, candidate in enumerate(lines[index: index + 8]):
            if candidate.strip().startswith("|"):
                rows = _parse_markdown_table_rows(lines, index + offset)
                if len(rows) < 2:
                    return {}
                result: dict[str, str] = {}
                for row in rows[1:]:
                    if len(row) >= 2:
                        key = _strip_markdown_emphasis(row[0])
                        value = _strip_markdown_emphasis(row[1])
                        result[key] = value
                return result
    return {}


def _paragraph_from_section_body(body: list[str]) -> str | None:
    parts: list[str] = []
    for line in body:
        stripped = line.strip()
        if not stripped or stripped == "---":
            continue
        if stripped.startswith("|") or stripped.startswith("- ") or stripped.startswith("```"):
            continue
        if stripped.startswith("Do not start"):
            continue
        parts.append(_strip_markdown_emphasis(stripped))
    if not parts:
        return None
    return " ".join(parts)


def _parse_numbered_items(body: list[str]) -> list[str]:
    items: list[str] = []
    for line in body:
        stripped = line.strip()
        if not stripped or not stripped[0].isdigit():
            continue
        dot_index = stripped.find(".")
        if dot_index == -1:
            continue
        items.append(_strip_markdown_emphasis(stripped[dot_index + 1 :].strip()))
    return items


def _parse_do_not_change(body: list[str]) -> list[str]:
    items: list[str] = []
    prefix = "- Do **not**"
    for line in body:
        stripped = line.strip()
        if not stripped.startswith(prefix):
            continue
        text = stripped[len("- Do **not**") :].strip()
        if text.endswith("."):
            text = text[:-1]
        items.append(text.strip())
    return items


def _parse_project_name(lines: list[str]) -> str | None:
    if not lines:
        return None
    first = lines[0].strip()
    suffix = " Project State"
    if first.startswith("# ") and first.endswith(suffix):
        return first[2 : -len(suffix)].strip() or None
    return None


def _parse_last_updated(lines: list[str]) -> str | None:
    for line in lines[:20]:
        stripped = line.strip()
        if stripped.startswith("Last Updated:"):
            return stripped.split(":", 1)[1].strip() or None
    return None


def _parse_documented_head(section_lines: list[str]) -> str | None:
    for line in section_lines:
        stripped = line.strip()
        if stripped.startswith("**HEAD:**"):
            remainder = stripped.split("**HEAD:**", 1)[1].strip()
            if remainder.startswith("`") and "`" in remainder[1:]:
                return remainder.split("`", 2)[1]
    return None


def _parse_verified_checks(section_lines: list[str]) -> dict[str, str]:
    for index, line in enumerate(section_lines):
        if "**Verified on this machine" in line:
            rows = _parse_markdown_table_rows(section_lines, index + 1)
            if len(rows) < 2:
                return {}
            checks: dict[str, str] = {}
            for row in rows[1:]:
                if len(row) >= 2:
                    checks[_strip_markdown_emphasis(row[0])] = _strip_markdown_emphasis(row[1])
            return checks
    return {}


def _parse_test_state_table(lines: list[str]) -> dict[str, dict[str, str | None]]:
    start = _find_heading_index(lines, "TEST / VERIFICATION STATE")
    if start is None:
        return {}
    rows = _parse_markdown_table_rows(lines, start + 1)
    if len(rows) < 2:
        return {}
    result: dict[str, dict[str, str | None]] = {}
    for row in rows[1:]:
        if len(row) < 2:
            continue
        key = _strip_markdown_emphasis(row[0])
        entry: dict[str, str | None] = {"result": _strip_markdown_emphasis(row[1])}
        if len(row) >= 3:
            when = _strip_markdown_emphasis(row[2])
            entry["when_verified"] = when if when != "—" else None
        result[key] = entry
    return result


def _parse_blockers(lines: list[str]) -> list[str]:
    start = _find_heading_index(lines, "PARTIAL / UNVERIFIED WORK")
    if start is None:
        return []
    rows = _parse_markdown_table_rows(lines, start + 1)
    if len(rows) < 2:
        return []
    return [_strip_markdown_emphasis(row[0]) for row in rows[1:] if row]


def _capability_flag(value: str, needle: str) -> bool:
    return needle.lower() in value.lower()


def build_hermes_context(repo_root: Path) -> dict[str, Any]:
    lines = read_project_state_lines(repo_root)
    status_lines = git_status_short(repo_root)
    branch = git_branch(repo_root)
    head = git_head(repo_root)

    project = _parse_project_name(lines)
    if project is None:
        raise ValueError("unable to parse project name from PROJECT_STATE.md")

    verified_section = _section_body_lines(lines, "VERIFIED CURRENT STATE")
    remote = _table_after_marker(lines, "**Remote deployment")
    capabilities = _table_after_marker(lines, "**Deployment status:**")
    promoted_export = _table_after_marker(lines, "**Current local promoted export**")

    manual_verified = any(
        _capability_flag(value, "IMPLEMENTED — VERIFIED")
        for value in capabilities.values()
    )
    automation_implemented = not any(
        key.lower() == "deployment automation"
        and _capability_flag(value, "NOT IMPLEMENTED")
        for key, value in capabilities.items()
    )

    objective_body = _section_body_lines(lines, "CURRENT OBJECTIVE")
    next_action_body = _section_body_lines(lines, "EXACT NEXT ACTION")
    unresolved_body = _section_body_lines(lines, "UNRESOLVED DECISIONS")
    constraints_body = _section_body_lines(lines, "DO-NOT-CHANGE CONSTRAINTS")

    untracked_paths = [
        line[3:].strip() for line in status_lines if is_untracked_status_line(line)
    ]

    return {
        "schema_version": HERMES_SCHEMA_VERSION,
        "project": project,
        "repository_root": str(repo_root),
        "branch": branch,
        "head": head,
        "stable_milestone": _first_content_line_after_heading(lines, "Stable Milestone"),
        "active_phase": _first_content_line_after_heading(lines, "Active Phase"),
        "current_objective": _paragraph_from_section_body(objective_body),
        "next_action": _paragraph_from_section_body(next_action_body),
        "verified_state": {
            "last_updated": _parse_last_updated(lines),
            "checks": _parse_verified_checks(verified_section),
            "promoted_export": promoted_export,
            "head_documented": _parse_documented_head(verified_section),
        },
        "test_state": _parse_test_state_table(lines),
        "deployment_state": {
            "remote": remote,
            "capabilities": capabilities,
            "manual_deploy_verified": manual_verified,
            "automation_implemented": automation_implemented,
            "custom_domain_configured": capabilities.get("Custom domain", "").lower()
            != "not configured"
            if capabilities
            else None,
            "cicd_deploy_implemented": not any(
                key.lower() == "ci/cd deployment"
                and _capability_flag(value, "NOT IMPLEMENTED")
                for key, value in capabilities.items()
            )
            if capabilities
            else None,
        },
        "working_tree_state": {
            "dirty": any(is_dirty_status_line(line) for line in status_lines),
            "untracked": any(is_untracked_status_line(line) for line in status_lines),
            "untracked_paths": untracked_paths,
            "status_lines": status_lines,
        },
        "blockers": _parse_blockers(lines),
        "unresolved_decisions": _parse_numbered_items(unresolved_body),
        "do_not_change": _parse_do_not_change(constraints_body),
        "source_files": list(HERMES_SOURCE_FILES),
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


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

    if args.hermes_json:
        try:
            hermes_context = build_hermes_context(repo_root)
        except FileNotFoundError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        print(json.dumps(hermes_context, indent=2, sort_keys=True))
        return 0

    context = build_context(repo_root)
    if args.json:
        print(json.dumps(context, indent=2, sort_keys=True))
    else:
        print_text(context)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
