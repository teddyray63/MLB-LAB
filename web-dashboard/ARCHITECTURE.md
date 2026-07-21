# MLB-LAB Dashboard — Architecture Rules (Locked)

These rules govern the new information architecture (`/today`, `/research`, `/leaderboards`, …). Legacy routes under `/legacy/*` remain frozen until parity is verified.

---

## Context providers

| Provider | Responsibility |
|----------|----------------|
| `GameContextProvider` | Date, game, player, pitcher, league mode |
| `FilterContextProvider` | Timeframe, situation, pitch type |

All new-IA pages mount inside `ResearchProviders`. No page may add local game, player, pitcher, or timeframe selectors.

---

## Resolution

- **`resolveResearchSelection()`** in `lib/researchResolver.ts` — single resolver; no page-level duplication.
- **`RESEARCH_SCHEMA_VERSION = 2`** in context and URL (`?v=2`).

---

## Research navigation

- **`buildResearchNavigation()`** / **`buildResearchHref()`** in `lib/researchNavigation.ts` — single source of truth for `/research` URLs.
- **`openResearch()`** on `GameContext` delegates to this helper; callers must not hand-build research query strings.
- Today, Leaderboards, game cards, search, and `HitterLink` all use `openResearch()` or the pure helpers.

---

## Context-aware components (required)

> **Any new analytical component must be context-aware by default.**

It should automatically respect:

- selected game
- selected player
- selected pitcher
- selected filters

…without requiring additional props or page-specific state unless there is a compelling reason.

Prefer hooks: `useGameContext()`, `useFilters()`, `useFilteredMatchupRows()`, and future slice helpers over prop drilling or local selector state.

---

## Chrome

- **`ResearchChrome`** renders only on new-IA paths (not `/legacy/*`, `/history`, `/settings`).
- Header + `FilterBar` + URL bootstrap — pages do not duplicate this chrome.

---

## Legacy isolation

- `/legacy/*` routes are unchanged until explicit parity sign-off.
- `HitterLink` uses legacy `/player?name=` on `/legacy/*`; new IA uses `openResearch()`.
