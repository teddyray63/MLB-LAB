# MLB-LAB Project State

Last Updated: 2026-08-03

## Stable Milestone

Phase E complete (Navigation cleanup)

## Active Branch

cursor/fix-dashboard-blank-panels

## Stable GitHub Artifacts

- Draft PR: MLB-LAB React Dashboard Foundation (Phases 0–C)
- Tag: mlb-dashboard-phase-c

## Completed

- Phase 0 – Export foundation
- Phase A – Shared GameContext / FilterContext
- Phase B – Today workspace
- Phase B.5 – Centralized research navigation
- Phase C – Research workspace
- Phase D – Leaderboards workspace (Codex accessibility audit passed)
- Phase E – Navigation cleanup

## Current Architecture

- Shared GameContext
- Shared FilterContext
- URL-synchronized research navigation
- Canonical routes: `/today`, `/research`, `/leaderboards`, `/data-status`, `/settings`
- Legacy dashboard preserved at `/legacy/*` until feature parity sign-off
- React/Vite dashboard builds successfully

## Active Phase

Phase F – Visual polish and cleanup (**in progress — awaiting Codex review**)

### Implemented (pending review sign-off)

| Milestone | Status | Summary |
|-----------|--------|---------|
| F1 | Implemented | Removed orphaned `GameResearchPage` / `PlayerResearchPage`; PROJECT_STATE sync |
| F2 | Implemented | Sticky `ResearchChrome` beneath AppLayout header; measured CSS vars (`--app-header-height`, `--research-chrome-height`) |
| F3 | Implemented | Shared page header/card/table/empty-state consistency across new-IA workspaces |

### Deferred

- Legacy route retirement — **deferred pending explicit parity sign-off**
- Parity assessment documented in `docs/LEGACY_PARITY_MATRIX.md` (all seven `/legacy/*` routes: **Partial** — none at Full parity)

## Known Limitations

- L5/L10 timeframe filtering not fully implemented
- Browser Back behavior not fully verified
- Duplicate game_pk export warning exists
- Legacy pages remain at `/legacy/*` until parity sign-off and retirement approval
- BVP (“vs Today’s SP”) team split available on legacy `/legacy/splits` but not exposed in new-IA Today Team Splits tab

## Notes for New Agents

Read these first:

1. PROJECT_STATE.md
2. web-dashboard/ARCHITECTURE.md
3. docs/LEGACY_PARITY_MATRIX.md (legacy retirement gate)

Do not modify export logic or shared context without understanding the architecture.

## First Production Promotion

Decision date:
2026-08-03

Branch:
cursor/phase-g

Promotion commit baseline:
c2d1867

Promoted slate date:
2026-08-01

Promoted live SHA256:
a87d894fc905f88dd9f4141370fd6342bc94037dddedd6192863e707445e36d6

Prior live SHA256:
6ccd284c812ddd2c40b2a208db86277ee0ed1410c73b16248068ff767592a404

Backup file:
data/backups/daily_export.20260803T100738Z.6ccd284c812d.json

Backup SHA256:
6ccd284c812ddd2c40b2a208db86277ee0ed1410c73b16248068ff767592a404

Promotion result:
SUCCESS

Rollback required:
No

Promotion Policy (v1)
- promote only the most recent slate where every scheduled game has reached a recognized terminal status
- walk backward mechanically from the current date until a fully terminal slate is found
- in-progress, warmup, scheduled, postponed, suspended, or otherwise non-terminal slates are ineligible
- rolling/intraday promotion remains out of scope

Known product regressions accepted:
- Known regression: Leaderboards Top Plays and Category Boards render empty states on /leaderboards, /legacy/top-plays, /legacy/boards, and /legacy/command-center.
- top_plays is empty
- category_boards is empty
- original formulas are unavailable
- no fabricated replacement rankings or scores were introduced

Known follow-up:
- legacy Top Plays and Boards subtitles remain misleading when arrays are empty
- examples include "5 per category" or "Top 20 per category" while zero rows render
- track this as a UI-copy cleanup item

Post-promotion test finding:
- five tests were coupled to the mutable live export
- tests were migrated to frozen fixtures
- production exports are no longer used as immutable reference fixtures
