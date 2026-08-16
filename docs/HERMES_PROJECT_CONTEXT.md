# Hermes Project Context — MLB-LAB v0.1

Minimal read-only contract for machine-readable project snapshots suitable for
Hermes. This is a **repository-local adapter**, not a Hermes-wide integration.

**Generator command:**

```bash
python3 scripts/repo_context.py --hermes-json
```

**Schema version:** `0.1`

---

## Design rules

1. **Verified facts** live in `verified_state`, `test_state`, and factual fields
   inside `deployment_state` / `working_tree_state`.
2. **Unresolved questions** live only in `unresolved_decisions` (from
   `PROJECT_STATE.md` §10). Do not promote them to verified facts.
3. **`do_not_change`** comes from `PROJECT_STATE.md` §13 and accepted decisions
   referenced there (DEC-001, DEC-002, DEC-005).
4. **`generated_at`** reflects generator execution time (only non-deterministic
   field).
5. Missing or unparsable optional fields are `null` or `[]` — never fabricated.
6. Core fields are extracted by deterministic rules — no LLM interpretation.

Existing `repo_context.py` default text output and `--json` output are unchanged.

---

## v0.1 JSON schema

| Field | Type | Description |
|-------|------|-------------|
| `schema_version` | string | Always `"0.1"` for this contract |
| `project` | string \| null | Project name from `PROJECT_STATE.md` H1 |
| `repository_root` | string | Absolute path from git root discovery |
| `branch` | string | `git branch --show-current` |
| `head` | string \| null | `git rev-parse HEAD` (full SHA) |
| `stable_milestone` | string \| null | First content line under `## Stable Milestone` |
| `active_phase` | string \| null | First content line under `## Active Phase` |
| `current_objective` | string \| null | Paragraph text under `## 11. CURRENT OBJECTIVE` |
| `next_action` | string \| null | Paragraph text under `## 12. EXACT NEXT ACTION` |
| `verified_state` | object | Verified facts from `PROJECT_STATE.md` §1 |
| `test_state` | object | Checks from `PROJECT_STATE.md` §8 table |
| `deployment_state` | object | Deployment facts from `PROJECT_STATE.md` §1 tables |
| `working_tree_state` | object | Git status summary |
| `blockers` | array[string] | Item names from `PROJECT_STATE.md` §4 table |
| `unresolved_decisions` | array[string] | Numbered items from `PROJECT_STATE.md` §10 |
| `do_not_change` | array[string] | Bullets from `PROJECT_STATE.md` §13 |
| `source_files` | array[string] | Authoritative inputs read by generator |
| `generated_at` | string | ISO-8601 UTC timestamp at generation time |

---

## Field source mapping

### `schema_version`

- **SOURCE:** constant in `scripts/repo_context.py`
- **PARSING RULE:** emit `"0.1"`

### `project`

- **SOURCE:** `PROJECT_STATE.md` line 1
- **PARSING RULE:** `# MLB-LAB Project State` → extract `MLB-LAB` (text between `# ` and ` Project State`). If pattern mismatch, `null`.

### `repository_root`

- **SOURCE:** git root discovery (`find_repo_root`)
- **PARSING RULE:** absolute path string

### `branch`

- **SOURCE:** `git branch --show-current`
- **PARSING RULE:** stdout stripped; `"unknown"` if command fails

### `head`

- **SOURCE:** `git rev-parse HEAD`
- **PARSING RULE:** full 40-char hex SHA; `null` if command fails

### `stable_milestone`

- **SOURCE:** `PROJECT_STATE.md` → `## Stable Milestone`
- **PARSING RULE:** first non-empty line after heading until next `##` heading

### `active_phase`

- **SOURCE:** `PROJECT_STATE.md` → `## Active Phase`
- **PARSING RULE:** same as `stable_milestone`

### `current_objective`

- **SOURCE:** `PROJECT_STATE.md` → section heading containing `CURRENT OBJECTIVE`
- **PARSING RULE:** join non-empty, non-table, non-list lines until next `##`; strip markdown emphasis

### `next_action`

- **SOURCE:** `PROJECT_STATE.md` → section heading containing `EXACT NEXT ACTION`
- **PARSING RULE:** same as `current_objective`

### `verified_state`

- **SOURCE:** `PROJECT_STATE.md` §1 (`VERIFIED CURRENT STATE`)
- **PARSING RULE:**
  - `last_updated` from `Last Updated: YYYY-MM-DD` near file top
  - `checks` from first markdown table under `**Verified on this machine`
  - `promoted_export` from table under `**Current local promoted export**`
  - `head_documented` from `**HEAD:**` line in §1 (informational; may differ from git `head`)

### `test_state`

- **SOURCE:** `PROJECT_STATE.md` §8 table (`TEST / VERIFICATION STATE`)
- **PARSING RULE:** markdown table → `{check: {result, when_verified}}` keyed by Check column

### `deployment_state`

- **SOURCE:** `PROJECT_STATE.md` §1 deployment tables
- **PARSING RULE:**
  - `remote` from `**Remote deployment` table (Field → Value)
  - `capabilities` from `**Deployment status:**` table (Capability → State)
  - booleans derived mechanically: `manual_deploy_verified` true if any capability value contains `IMPLEMENTED — VERIFIED` (case-insensitive); `automation_implemented` false if Deployment automation row contains `NOT IMPLEMENTED`

### `working_tree_state`

- **SOURCE:** `git status --short`
- **PARSING RULE:**
  - `dirty`: any tracked modification line
  - `untracked`: any `??` line
  - `untracked_paths`: paths from `??` lines
  - `status_lines`: raw short status lines

### `blockers`

- **SOURCE:** `PROJECT_STATE.md` §4 (`PARTIAL / UNVERIFIED WORK`) table
- **PARSING RULE:** first column (`Item`) for each table row

### `unresolved_decisions`

- **SOURCE:** `PROJECT_STATE.md` §10 numbered list
- **PARSING RULE:** lines matching `^\d+\.\s+` — strip number prefix; preserve full text

### `do_not_change`

- **SOURCE:** `PROJECT_STATE.md` §13 bullet list
- **PARSING RULE:** lines starting with `- Do **not**` — strip prefix and trailing period

### `source_files`

- **SOURCE:** constant list in generator
- **PARSING RULE:** `["PROJECT_STATE.md", "docs/DECISIONS.md", "AGENTS.md"]` plus `"git"` for branch/HEAD/status

### `generated_at`

- **SOURCE:** `datetime.now(timezone.utc)`
- **PARSING RULE:** ISO-8601 UTC string

---

## Error handling

- Not inside a git repository → exit code `1`, message on stderr
- `PROJECT_STATE.md` missing → exit code `1`, message on stderr
- Unrecoverable parse failure for required Hermes fields (`project`, `branch`) → exit code `2`

`docs/DECISIONS.md` and `AGENTS.md` are listed in `source_files` for contract
traceability; v0.1 core field extraction is driven primarily by `PROJECT_STATE.md`
and git.

---

## Backward compatibility

These interfaces must remain unchanged:

```bash
python3 scripts/repo_context.py          # human text
python3 scripts/repo_context.py --json   # existing repo context JSON
python3 scripts/repo_context.py --hermes-json   # Hermes v0.1 JSON (stdout only)
```
