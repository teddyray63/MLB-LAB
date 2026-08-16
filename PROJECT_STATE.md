# MLB-LAB Project State

Last Updated: 2026-08-15

Canonical operational snapshot for agents and operators. Historical design documents
(`BUILD_PLAN.md`, early README paths) may describe aspirational or superseded
architecture — see sections below for what is verified today.

## Stable Milestone

G0b export pipeline complete; first manual Cloudflare Pages deploy verified (2026-08-15)

## Active Branch

sports-resource-hub

## Active Phase

Post-deployment stabilization — branch and operational ownership reconciliation

---

## 1. VERIFIED CURRENT STATE

**Branch:** `sports-resource-hub`

**HEAD:** `f0141f4` (`chore: add manual static deployment workflow`)

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

**Production-intent dashboard path (verified on `sports-resource-hub`):**

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

### Export pipeline G0b (on `sports-resource-hub`, **not on `main`**)

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
| CI alignment with export pipeline | CI still runs `mlb_lab_runner.py` — **not verified** against G0b path |
| `sports-resource-hub` → `main` merge | **Not performed** — 20 commits ahead of `main` |

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
- Still invoked by GitHub Actions (`.github/workflows/daily-run.yml`,
  `.github/workflows/run-mlb-lab.yml`).

**Legacy dashboard routes:** `/legacy/*` frozen until parity sign-off (DEC-001).
Parity matrix: `docs/LEGACY_PARITY_MATRIX.md` (last updated 2026-08-02 on branch
`cursor/fix-dashboard-blank-panels` — matrix content not refreshed on
`sports-resource-hub`; assessment may predate G0b player_logs work).

**Documentation drift (not corrected in this reconciliation):**

- `web-dashboard/README.md` still instructs `mlb_lab_runner.py` → `daily_export.json`.
- `BUILD_PLAN.md` still describes FastAPI → React as primary architecture.

---

## 7. CURRENT BRANCH / GIT STATE

| Item | Value |
|------|-------|
| Active branch | `sports-resource-hub` |
| HEAD | `f0141f4b8083b0d3f55380d69c91ba283eb49a30` |
| `main` HEAD | `54ca81a` (`Merge branch 'cursor/fix-dashboard-blank-panels'`) |
| Merge-base (`main`…`HEAD`) | `54ca81a` |
| Commits on branch not on `main` | **20** |
| Working tree | clean except untracked `evidence/mlb/game-995731-feed-live.metadata.txt` |

**Recent commits on `sports-resource-hub`:**

```
f0141f4 chore: add manual static deployment workflow
0fd4d73 fix: report missing player logs accurately
37775e8 feat: wire research timeframe to player logs
f871ef5 feat: enable player logs in full candidate builds
1d524dd docs: clarify primary position semantics
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
| Stale active branch (`cursor/fix-dashboard-blank-panels`) | Updated to `sports-resource-hub` | `LEGACY_PARITY_MATRIX.md` header still references old branch |
| L5/L10 “not fully implemented” | Clarified: **yes** for Research player logs; **no** for leaderboard export rows | — |
| Old promotion record (2026-08-01) as “current” | Updated current export to 2026-08-14; prior promotion kept as history | DEC-002 evidence cites old PROJECT_STATE text |
| Phase F “in progress” | Marked **implemented**; sign-off **unverified** | — |
| FastAPI path as active dashboard | Labeled aspirational in §2 | `BUILD_PLAN.md` |
| CI runs legacy runner | Documented in §6 | `.github/workflows/*.yml` |
| README points to wrong export script | Documented in §6 | `web-dashboard/README.md` |
| Empty leaderboard arrays | Still accepted (DEC-005) | — |
| Duplicate `game_pk` export warning | Still present | — |
| Misleading legacy subtitles on empty sections | Partially addressed (`2bdaab1`); UI-copy cleanup may remain | — |

---

## 10. UNRESOLVED DECISIONS

Do **not** decide these without explicit stakeholder approval:

1. **Merge `sports-resource-hub` → `main`** — 20 commits including G0b pipeline not on main.
2. **Cloudflare deployment automation** — whether/how to automate deploys while preserving SHA-pinned export promotion semantics (provider selected: Cloudflare Pages; first manual deploy complete).
3. **Retirement of `mlb_lab_runner.py`** — parallel to G0b path; CI still depends on it.
4. **Restoration of leaderboard formulas** — `top_plays` / `category_boards` empty.
5. **Retirement of legacy routes** — deferred pending parity sign-off (DEC-001).
6. **CI redesign** — align automation with `build_daily_export.py` vs keep legacy runner.
7. **Phase F formal sign-off** — implementation complete; approval not recorded.

Recorded decisions: `docs/DECISIONS.md` (DEC-001 through DEC-007).

---

## 11. CURRENT OBJECTIVE

Stabilize the verified post-deployment project state, reconcile branch and
operational ownership, and choose the next bounded MLB-LAB product/operations task.

---

## 12. EXACT NEXT ACTION

Choose the next bounded task from unresolved decisions (§10) — merge review,
Cloudflare deploy automation design, companion-doc refresh, or product backlog item.

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
4. `docs/DEPLOYMENT.md` (static deploy; export injection before build)
5. `docs/LEGACY_PARITY_MATRIX.md` (legacy retirement gate)

Do not modify export logic or shared context without understanding the architecture.

Use deterministic inspection before inferring JSON semantics:

```bash
python scripts/evidence.py <json-file>
python3 scripts/repo_context.py
```
