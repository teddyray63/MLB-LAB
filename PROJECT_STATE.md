# MLB-LAB Project State

Last Updated: 2026-08-02

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
