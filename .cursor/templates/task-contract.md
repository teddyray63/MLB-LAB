# TASK CONTRACT

Fill before non-trivial orchestrated work. The orchestrator owns this document;
**subagents may not change immutable fields**.

## Contract identity

**CONTRACT_ID:** Unique id for this task (orchestrator-generated)

**ROLE:** orchestrator | researcher | implementer | verifier | security-reviewer

**AUTHORITY_LEVEL:** 0 | 1 | 2 | 3 | 4

**PROJECT_MODEL:** A-software | B-teddy-os | C-trading | D-study

## Objective

State exactly what is being changed or proven.

## Task

One-line task label for handoff tracking.

## Goal

Outcome the user requested.

## CURRENT STATE

Live facts only: branch, HEAD, `git status` summary, staged/untracked notes.
Do not copy stale `PROJECT_STATE.md` branch/worktree claims without verification.

## Allowed Scope

List files, directories, modules, or behaviors the task may touch.

## AUTHORIZED PATHS

Exact paths the Implementer may edit/create. Empty if Level 0 only.

## AUTHORIZED ACTIONS

Explicit allowed operations (e.g. run `npm run test`, read QMD, `git diff`).

## PROHIBITED ACTIONS

Explicit denials (e.g. stage, commit, touch `/legacy/*`, MCP install).

## Out of Scope

List nearby areas that must not be changed.

## Known Facts

Only repository-proven or directly observed facts.

## Open Unknowns

Only unknowns that actually block the task.

## Evidence Required

For each blocking unknown:

- exact question
- preferred source
- one decisive observation that would resolve it

## RETRIEVAL CONTEXT

Notes/paths already retrieved; retrieval policy pointer if needed.

## MUTATION OWNER

`none` | `implementer` — exactly one writer role when mutation is allowed.

## LOCKS HELD

Files, git-index, install, or config locks (e.g. protect pre-existing staged work).

## CHECKPOINT REQUIREMENT

`none` | `ask-user` | `explicit-phrase-required` — Level 2+ never implied.

## Acceptance Criteria

List concrete conditions for completion.

## Safety Constraints

Examples:

- no network unless explicitly authorized
- no database mutation unless explicitly authorized
- no unrelated refactors
- no dependency changes unless required
- preserve existing public behavior unless the task says otherwise
- preserve unrelated staged/untracked work

## Stop Conditions

Stop and report if:

- the requested behavior cannot be defined from available evidence
- a required dependency or source is unavailable
- the task requires out-of-scope changes
- a contradiction invalidates the task assumptions
- unauthorized path touched or index lock violated

## Immutable fields (subagents)

Subagents must not modify: **TASK**, **Goal**, **AUTHORIZED PATHS**,
**AUTHORIZED ACTIONS**, **PROHIBITED ACTIONS**, **AUTHORITY_LEVEL**,
**CHECKPOINT REQUIREMENT**, **MUTATION OWNER**, **LOCKS HELD**, **CONTRACT_ID**.

Contract conflict → `UNRESOLVED: contract-conflict` and stop.

## Standard handoff (specialists return)

```
ROLE:
TASK:
CONTRACT_ID:
AUTHORITY_LEVEL:
SCOPE:
FILES READ:
FILES MODIFIED:
EVIDENCE:
FINDINGS:
RISKS:
TESTS:
UNRESOLVED:
RECOMMENDATION:    continue | stop | escalate | ready-for-user-checkpoint
MUTATION STATUS:   none | authorized-edits | unauthorized-touch | lock-violation
INDEX STATUS:      untouched | dirty-before-task | changed-during-task
```

## Completion Report

At completion, report only:

- files changed
- tests run
- result
- unresolved issues
- whether scope was exceeded

Policy: `~/teddy-os-infrastructure/docs/agent-orchestration.md`
