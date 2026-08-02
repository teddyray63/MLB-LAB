# MLB-LAB Project State

Last Updated: 2026-08-01

## Stable Milestone

Phase D complete (Leaderboards workspace)

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

## Current Architecture

- Shared GameContext
- Shared FilterContext
- URL-synchronized research navigation
- Canonical routes: `/today`, `/research`, `/leaderboards`, `/data-status`, `/settings`
- Legacy dashboard preserved at `/legacy/*` until feature parity
- React/Vite dashboard builds successfully

## Active Phase

Phase E – Navigation cleanup (in progress)

Goals:
- Primary nav: Today · Research · Leaderboards · Data Status · Settings
- Canonical routes and safe redirects from old IA aliases
- ResearchChrome isolation on non-research pages
- Preserve legacy pages until Phase F retirement approval

## Known Limitations

- L5/L10 timeframe filtering not fully implemented
- Browser Back behavior not fully verified
- Duplicate game_pk export warning exists
- Legacy pages remain until Phase F
- Phase 1 placeholder pages (`GameResearchPage`, `PlayerResearchPage`) may be removable after Phase E sign-off

## Notes for New Agents

Read these first:

1. PROJECT_STATE.md
2. web-dashboard/ARCHITECTURE.md

Do not modify export logic or shared context without understanding the architecture.
