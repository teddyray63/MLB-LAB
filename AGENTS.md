# Agent Instructions

This file provides repository-level guidance for AI coding agents working in MLB-LAB.

## Implementation context

When applicable, consult:

- `PROJECT_STATE.md`
- relevant architecture documentation (for example `web-dashboard/ARCHITECTURE.md`)
- `docs/DECISIONS.md`
- `docs/DEPLOYMENT.md` (static dashboard deploy; export injection before build)

## Decision log

Before reopening a previously settled architectural or behavioral question,
check `docs/DECISIONS.md`.

Do not treat a recorded decision as immutable.

Reopen it only when:

- new verified evidence contradicts its basis,
- requirements changed,
- constraints changed, or
- the decision explicitly states a revisit condition that has occurred.

When superseding a decision, preserve the old entry and link it to the new
decision rather than deleting history.

Do not add routine implementation choices, temporary debugging choices, or
speculative conclusions to the decision log.

## Evidence-First Investigation Policy

Agents must reason from directly observed evidence. Do not enter speculative investigation loops.

### Core rules

- Never promote inference to evidence.
- Never invent JSON paths, fields, values, schemas, endpoint semantics, or representative examples and later treat them as observations.
- Generated examples are never evidence.
- Historical behavior is not evidence of current behavior unless explicitly verified.
- Prefer deterministic inspection tools before LLM interpretation.
- For structured data, mechanically extract facts with tools such as Python, jq, rg, git, AST inspection, or database queries as appropriate.
- Separate **FACT**, **INTERPRETATION**, and **HYPOTHESIS**.
- Only directly observed information may be labeled **FACT**.
- If new evidence contradicts an earlier claim, invalidate the earlier claim immediately.
- Never create another investigation phase merely to reconcile an unsupported earlier narrative.
- Do not repeat an investigation whose decisive observation has already been made.
- Exhaust local evidence before requesting external evidence.
- Do not implement production behavior from speculative semantics.
- Prefer one decisive mechanical observation over another reasoning phase.

### Evidence ledger

For nontrivial investigations, maintain an evidence ledger:

```
PROVEN:
NOT PROVEN:
DISPROVEN:
NEXT UNKNOWN:
```

### Before each investigation step

Answer internally:

1. **WHAT EXACT UNKNOWN REMAINS?**
2. **WHAT SINGLE OBSERVATION WOULD RESOLVE IT?**
3. **HAS THAT OBSERVATION ALREADY BEEN MADE?**

Do not proceed if the decisive observation already exists.

### Investigation budget

A single unresolved question may receive at most:

1. repository inspection
2. deterministic artifact inspection
3. one explicitly authorized external observation, only if local evidence cannot resolve the question

After those steps, **STOP** and report unresolved uncertainty rather than creating recursive forensic phases.

Do not create recursively numbered investigation phases solely because evidence remains uncertain.

### Investigation task completion format

For investigation tasks, finish with:

```
CURRENT VERIFIED STATE:
ONE UNRESOLVED QUESTION:
NEXT ACTION:
```

### Local JSON inspection

Use the dependency-free utility for deterministic JSON structure extraction:

```bash
python scripts/evidence.py <json-file>
python scripts/evidence.py <json-file> --match <term> [<term> ...]
```

Never infer JSON paths or field values when this tool or equivalent mechanical inspection can establish them.

### Repository context

Before non-trivial investigation or implementation, agents should prefer:

```bash
python3 scripts/repo_context.py
```

Use:

```bash
python3 scripts/repo_context.py --json
```

when machine-readable context is useful.

Do not make this mandatory for trivial edits.

### Task contract

For non-trivial implementation or investigation, agents should begin by mentally or explicitly filling out the task contract before editing.

Template: `.cursor/templates/task-contract.md`

The task contract is not required for trivial edits.

It should be used to prevent:

- scope drift
- speculative semantics
- unnecessary repository-wide investigation
- repeated evidence collection
- unrelated cleanup

Do not treat the task contract as mandatory for every task.

### Evidence artifacts

External captures used for investigation live under `evidence/`.

- Raw captures (`evidence/**/*.raw.json`) are **ignored by default** and stay local.
- Metadata/manifests (`evidence/**/*.metadata.txt`) **may be committed**.
- Metadata should record provenance sufficient to identify and verify the raw
  artifact: request method, request URL, capture timestamp, HTTP status,
  content type, raw artifact filename, byte count, and SHA256 when available.
- Do not promote raw captures to test fixtures automatically.
- If a capture becomes a durable test fixture, that requires an explicit
  task/decision and the fixture belongs under repository fixture conventions
  (for example `tests/fixtures/`), not silent commit from `evidence/`.
- Metadata proves provenance and integrity information only. It is not proof of
  unrecorded payload semantics inside an unavailable raw artifact.
