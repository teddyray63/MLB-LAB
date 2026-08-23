# MLB-LAB Project State

Last Updated: 2026-08-23

Canonical operational snapshot for agents and operators. Historical design documents
(`BUILD_PLAN.md`, early README paths) may describe aspirational or superseded
architecture — see sections below for what is verified today.

## Stable Milestone

G0b export pipeline complete; first manual Cloudflare Pages deploy verified (2026-08-15)

## Active Branch

main

## Active Phase

Post-reconciliation stabilization — canonical baseline on `main`

---

## 1. VERIFIED CURRENT STATE

**Branch:** `main`

**Live commit identity:** not pinned in this document — verified live from Git by the
repository health monitor (`GIT SYNC` category).

**Verified on this machine (2026-08-15):**

| Check | Result |
|-------|--------|
| `python3 -m pytest tests/ -q` | **219 passed** |
| `web-dashboard` `npm run build` | **success** |
| Manual remote deployment (Cloudflare Pages) | **VERIFIED** |
| `data/daily_export.json` present locally | **yes** |

**Remote deployment (verified 2026-08-15):**

| Field | Value |
|-------|-------|
| Host | Cloudflare Pages |
| Site | `mlbworkspace90.pages.dev` |
| Model | Manual drag-and-drop of locally verified `web-dashboard/dist/` |
| Deployed artifact | `web-dashboard/dist/` |
| Deployed export slate | `2026-08-14` |
| Deployed export SHA256 | `d73cd29001c2e8e26c3bbfc43186f979c1d8afefb8138c2107d4b13d6328d509` |

**Deployment status:**

| Capability | State |
|------------|-------|
| Manual first deployment to Cloudflare Pages | **IMPLEMENTED — VERIFIED** |
| Deployment automation | **NOT IMPLEMENTED** |
| Custom domain | **NOT CONFIGURED** |
| CI/CD deployment | **NOT IMPLEMENTED** |

**Post-deploy smoke verification (public site):**

- Cloudflare Pages deployment reported success.
- React application loaded from `mlbworkspace90.pages.dev`.
- Export date displayed `2026-08-14`.
- `/data/daily_export.json` loaded through the application.
- `/research` loaded successfully.
- Max Muncy resolved from promoted `player_logs` data; season recent form visible.
- Selecting Last 5 changed recent-form output to the L5 window.
- Browser refresh on `/research` succeeded without SPA 404.

**Current local promoted export** (`data/daily_export.json`):

| Field | Value |
|-------|-------|
| Slate date | `2026-08-14` |
| Games | `14` |
| `player_logs` entries (hitter keys) | `251` |
| SHA256 | `d73cd29001c2e8e26c3bbfc43186f979c1d8afefb8138c2107d4b13d6328d509` |

**Prior live export** (backed up before most recent promotion):

| Field | Value |
|-------|-------|
| Backup file | `data/backups/daily_export.20260815T123520Z.a87d894fc905.json` |
| Slate date | `2026-08-01` |
| SHA256 | `a87d894fc905f88dd9f4141370fd6342bc94037dddedd6192863e707445e36d6` |

**Dashboard data contract:** React/Vite SPA loads static `daily_export.json` at
runtime from `/data/daily_export.json` (bundled via prebuild sync). See
`web-dashboard/src/data/loadExport.ts`.

**Known product state (accepted):**

- `top_plays` and `category_boards` export arrays are **empty** (DEC-005).
- Leaderboards render empty states; no fabricated rankings.
- Legacy routes remain at `/legacy/*` (DEC-001).

---

## 2. CURRENT ARCHITECTURE

**Production-intent dashboard path (verified on `main`):**

```
MLB Stats API + pybaseball
        ↓
scripts/build_daily_export.py
        ↓
candidate validation
        ↓
promotion
        ↓
data/daily_export.json
        ↓
scripts/prepare_export_for_build.sh  (optional SHA pin for deploy)
        ↓
web-dashboard npm run build  (prebuild: sync-data)
        ↓
web-dashboard/dist/
        ↓
Cloudflare Pages  (manual drag-and-drop — VERIFIED at mlbworkspace90.pages.dev)
```

**Dashboard runtime:**

- Vite static SPA — no FastAPI/backend service for the React dashboard.
- Single data source: promoted `daily_export.json`.
- Fetch path: `/data/daily_export.json` (`loadExport.ts`).

**New information architecture (canonical routes):**

- `/today`, `/research`, `/leaderboards`, `/data-status`, `/settings`
- Shared `GameContextProvider` + `FilterContextProvider` inside `ResearchProviders`
  (DEC-004, `web-dashboard/ARCHITECTURE.md`)
- URL-synchronized research navigation (`RESEARCH_SCHEMA_VERSION = 2`)
- Legacy dashboard preserved at `/legacy/*` until explicit parity sign-off

**Aspirational architecture (historical — NOT current dashboard path):**

`BUILD_PLAN.md` describes:

```
Collectors → SQLite Database → Feature Engine → FastAPI Backend → React Frontend
```

That pipeline is **not** what the current dashboard consumes. Treat `BUILD_PLAN.md`
as roadmap/history, not operational truth.

---

## 3. COMPLETED PHASES

### Dashboard IA (on `main` via merge `54ca81a`)

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 0 | Complete | Export foundation |
| Phase A | Complete | Shared GameContext / FilterContext |
| Phase B | Complete | Today workspace |
| Phase B.5 | Complete | Centralized research navigation |
| Phase C | Complete | Research workspace |
| Phase D | Complete | Leaderboards workspace |
| Phase E | Complete | Navigation cleanup |
| Phase F | **Implemented** (`ff6b798`) | F1–F3 visual polish; orphaned pages removed; `LEGACY_PARITY_MATRIX.md` added |

Phase F commit message: *"Complete Phase F visual polish and cleanup"*. Formal Codex
sign-off is **not recorded** in git or decision log — see §4.

### Export pipeline G0b (on `main`)

| Milestone | Status | Key commits / artifacts |
|-----------|--------|-------------------------|
| G0b schema + validation | Complete | `e7b5cf5` |
| Schedule / games shell | Complete | `5019805`, `6436383` |
| Identity layer (teams, players, lineups) | Complete | `215e925` |
| Matchup / Statcast enrichment | Complete | `a052e33` |
| Full candidate assembler | Complete | `efd27f7` |
| Promotion / backup / rollback | Complete | `c2d1867` |
| Player logs in candidate builds | Complete | `f871ef5` |
| Research L5/L10 wiring (player logs) | Complete | `37775e8`, `gameLogSlice.ts` |
| Static deployment preparation | Complete | `f0141f4`, `docs/DEPLOYMENT.md`, `prepare_export_for_build.sh` |
| Manual Cloudflare Pages deploy | **Verified** | `mlbworkspace90.pages.dev`; export SHA `d73cd290…`; 2026-08-15 |

### First production promotion (historical record)

| Field | Value |
|-------|-------|
| Decision date | `2026-08-03` |
| Branch | `cursor/phase-g` |
| Promotion commit baseline | `c2d1867` |
| Promoted slate date | `2026-08-01` |
| Promoted SHA256 | `a87d894fc905f88dd9f4141370fd6342bc94037dddedd6192863e707445e36d6` |
| Result | SUCCESS |

Superseded locally by 2026-08-14 promotion (§1). Policy unchanged (DEC-002).

---

## 4. PARTIAL / UNVERIFIED WORK

| Item | State |
|------|-------|
| Phase F formal sign-off | F1–F3 **implemented**; Codex/product sign-off **not documented** |
| Legacy route retirement | **Deferred** — all seven `/legacy/*` routes assessed **Partial** parity (`docs/LEGACY_PARITY_MATRIX.md`, DEC-001) |
| Deployment automation | Manual Cloudflare drag-and-drop only; **automation not implemented** |
| Custom domain | **Not configured** |
| Leaderboard timeframe/situation filters | Honesty notes shown; pre-aggregated export rows **do not recompute** by filter |
| BVP (“vs Today’s SP”) team split | Available on `/legacy/splits`; **not exposed** in new-IA Today Team Splits tab |
| Browser Back behavior | **Not fully verified** |
| `top_plays` / `category_boards` formulas | **Unavailable** — empty arrays accepted (DEC-005) |
| CI alignment with export pipeline | Canonical CI (`verify-g0b.yml`) validates G0b export path; legacy `mlb_lab_runner.py` **not in CI** |

**L5/L10 clarification:** Timeframe slicing **is implemented** for Research workspace
player game logs (`player_logs` export + `sliceGameLogByTimeframe` in
`gameLogSlice.ts`, wired via `useResearchPlayerData.ts`, commit `37775e8`). It does
**not** apply to leaderboard pre-aggregated export sections.

---

## 5. CURRENT DATA PIPELINE

**Production-intent export CLI:** `scripts/build_daily_export.py`

Primary subcommands / flags (non-exhaustive):

- `--build-games`, `--build-lineups`, `--build-matchups` — layered dry-run builds
- `--build-full-candidate` — assemble validated candidate (writes to `--output`, never live)
- `--build-player-logs` / `--no-player-logs` — player log layer control
- `--validate-existing`, `--validate-only` — read-only validation
- `--promote`, `--promotion-dry-run`, `--candidate`, `--candidate-sha256`, `--yes-promote`
- `--rollback-from-backup` — restore from `data/backups/`

**Sources:** MLB Stats API (`backend/export/mlb_schedule.py`, `mlb_game_feed.py`) +
pybaseball Statcast enrichment.

**Promotion Policy (v1)** — DEC-002:

- Promote only the most recent slate where every scheduled game has reached a recognized terminal status.
- Walk backward mechanically from the current date until a fully terminal slate is found.
- In-progress, warmup, scheduled, postponed, suspended, or otherwise non-terminal slates are ineligible.
- Rolling/intraday promotion remains out of scope.

**Deploy injection:** `scripts/prepare_export_for_build.sh EXPECTED_SHA256 SOURCE_PATH`
→ copies verified export to `data/daily_export.json` → `web-dashboard` prebuild sync.

**Test fixtures:** Reference-behavior tests use frozen fixtures under `tests/fixtures/`,
not the mutable live export (DEC-003).

---

## 6. LEGACY / PARALLEL SYSTEMS

**Parallel legacy runner (separate from dashboard export path):**

```
scripts/mlb_lab_runner.py
        ↓
reports/  (markdown + Excel)
```

- Uses MLB Stats API + pybaseball + openpyxl.
- Outputs to `reports/mlb-lab-v5-matchup-engine.md` and `.xlsx`.
- Does **not** produce `daily_export.json`.
- GitHub-hosted legacy workflows **retired** (Upgrade 8: `daily-run.yml` PR #8;
  `run-mlb-lab.yml` Phase 2b). Local/ad-hoc execution only:
  `python3 scripts/mlb_lab_runner.py`.

**Legacy dashboard routes:** `/legacy/*` frozen until parity sign-off (DEC-001).
Parity matrix: `docs/LEGACY_PARITY_MATRIX.md` (last updated 2026-08-02 on branch
`cursor/fix-dashboard-blank-panels` — matrix content not refreshed on
`sports-resource-hub`; assessment may predate G0b player_logs work).

**Documentation drift (not corrected in this reconciliation):**

- `BUILD_PLAN.md` still describes FastAPI → React as primary architecture.

---

## 7. CURRENT BRANCH / GIT STATE

| Item | Value |
|------|-------|
| Canonical branch | `main` |
| Live commit identity | determined from Git at scan/runtime (health monitor `GIT SYNC`; not pinned here) |
| Local branches | `main`, `review/phase-d` (local review/reference only) |
| Remote branches | `origin/main` only |
| Archive recovery tags | `archive/pre-dashboard-merge-2026-07-16`; 2026-08-02 recovery tag (object `72891ca1b19ab1f9a4e2a6fdaf1b7ffec71d7d76`, peeled `54ca81af23a01fcf001e30ba084ae372d8617acc`); `archive/claude-odds-engine-experiment-2026-06-30` |
| Branch/archive policy | `docs/BRANCH_ARCHIVE_POLICY.md` (DEC-008) |
| `sports-resource-hub` | **Retired** — reconciled into `main` (2026-08-18); branch deleted during Upgrade 9; tip was `8a2ba23` |
| Reconciliation | **Complete** — 22 commits fast-forwarded from `54ca81a` to `8a2ba23` on 2026-08-18 |
| Upgrade 9 branch cleanup | **Complete** (2026-08-23) — merged/backup/experiment branches removed; archive tags retained |
| Upgrade 7 health monitor | PR #5 merged to `main` at `cff0ceb` (2026-08-22); `scripts/repo_health.py` present |
| Upgrade 7 PROJECT_STATE reconciliation | PR #6 source `1adb5be` (2026-08-23); documentation-only |
| Upgrade 8 legacy workflow retirement | PR #8 merged `daily-run.yml`; Phase 2b retires `run-mlb-lab.yml` |
| Index | empty |
| Working tree | clean except untracked `evidence/mlb/game-995731-feed-live.metadata.txt` (SHA256 `29c9635f376100332bef248bdc5c12063ca1d1c230e3938a062e9e5d11624c95`) |

**Recent commits on `main`:**

```
b885d56 Merge pull request #6 from teddyray63/infra/project-state-reconciliation
1adb5be docs: reconcile project state with live repository
cff0ceb Merge pull request #5 from teddyray63/infra/repo-health-monitor
e142f9b chore: add repository health monitor
c612df2 Merge pull request #4 from teddyray63/infra/upgrade6-agent-orchestration
```

**Stable GitHub artifacts (historical):**

- Draft PR: MLB-LAB React Dashboard Foundation (Phases 0–C)
- Tag: `mlb-dashboard-phase-c`

---

## 8. TEST / VERIFICATION STATE

| Check | Result | When verified |
|-------|--------|---------------|
| Python test suite | **219 passed** | 2026-08-15 |
| Dashboard production build | **success** | 2026-08-15 |
| Export validation CLI | implemented | code on branch |
| Promotion / rollback CLI | implemented | code on branch |
| Remote deploy smoke test | **passed** (manual Cloudflare Pages) | 2026-08-15 |
| Legacy route browser regression | **incomplete** per parity matrix | — |

Post-promotion test migration (DEC-003): five tests decoupled from mutable live export;
frozen fixtures used instead.

---

## 9. KNOWN CONTRADICTIONS / TECHNICAL DEBT

Documented here for agent awareness. **This reconciliation updates PROJECT_STATE only**
— other docs preserved as historical record.

| Contradiction | Resolution in PROJECT_STATE | Other docs (unchanged) |
|---------------|----------------------------|------------------------|
| Stale active branch (`cursor/fix-dashboard-blank-panels`) | Updated to `main` | `LEGACY_PARITY_MATRIX.md` header still references old branch |
| L5/L10 “not fully implemented” | Clarified: **yes** for Research player logs; **no** for leaderboard export rows | — |
| Old promotion record (2026-08-01) as “current” | Updated current export to 2026-08-14; prior promotion kept as history | DEC-002 evidence cites old PROJECT_STATE text |
| Phase F “in progress” | Marked **implemented**; sign-off **unverified** | — |
| FastAPI path as active dashboard | Labeled aspirational in §2 | `BUILD_PLAN.md` |
| CI runs legacy runner | Resolved — legacy GitHub workflows retired; Verify G0b canonical | `.github/workflows/verify-g0b.yml` |
| README points to wrong export script | Corrected in stabilization (2026-08-18) | — |
| Empty leaderboard arrays | Still accepted (DEC-005) | — |
| Duplicate `game_pk` export warning | Still present | — |
| Misleading legacy subtitles on empty sections | Partially addressed (`2bdaab1`); UI-copy cleanup may remain | — |

---

## 10. UNRESOLVED DECISIONS

Do **not** decide these without explicit stakeholder approval:

1. **Cloudflare deployment automation** — whether/how to automate deploys while preserving SHA-pinned export promotion semantics (provider selected: Cloudflare Pages; first manual deploy complete).
2. **Retirement of `mlb_lab_runner.py`** — parallel legacy script; GitHub Actions
   invocation retired (Upgrade 8). Local/ad-hoc use and tracked `reports/` remain.
3. **Restoration of leaderboard formulas** — `top_plays` / `category_boards` empty.
4. **Retirement of legacy routes** — deferred pending parity sign-off (DEC-001).
5. **CI redesign** — legacy mutating workflows retired; Verify G0b canonical. Deploy
   automation and optional artifact-only legacy report workflows unresolved.
6. **Phase F formal sign-off** — implementation complete; approval not recorded.

Recorded decisions: `docs/DECISIONS.md` (DEC-001 through DEC-008).

---

## 11. CURRENT OBJECTIVE

Maintain the reconciled canonical baseline on `main` and choose the next bounded
MLB-LAB product task.

---

## 12. EXACT NEXT ACTION

Choose the next bounded product task — `/today` → `/research` handoff or another
backlog item from §10.

Do not start without explicit authorization for the chosen task.

---

## 13. DO-NOT-CHANGE CONSTRAINTS

Unless explicitly authorized in a new task:

- Do **not** modify application behavior.
- Do **not** modify export schemas.
- Do **not** modify promotion policy (DEC-002).
- Do **not** delete legacy routes (DEC-001).
- Do **not** change `.gitignore`.
- Do **not** fabricate leaderboard data (DEC-005).
- Do **not** deploy remotely without explicit deploy task.
- Do **not** merge branches without explicit merge task.

---

## Notes for New Agents

Read these first:

1. `PROJECT_STATE.md` (this file)
2. `web-dashboard/ARCHITECTURE.md`
3. `docs/DECISIONS.md`
4. `docs/BRANCH_ARCHIVE_POLICY.md` (branch cleanup and archive tags, DEC-008)
5. `docs/DEPLOYMENT.md` (static deploy; export injection before build)
6. `docs/LEGACY_PARITY_MATRIX.md` (legacy retirement gate)

Do not modify export logic or shared context without understanding the architecture.

Use deterministic inspection before inferring JSON semantics:

```bash
python scripts/evidence.py <json-file>
python3 scripts/repo_context.py
```
