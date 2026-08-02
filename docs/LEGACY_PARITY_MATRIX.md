# Legacy Parity Matrix

Last updated: 2026-08-02  
Branch: `cursor/fix-dashboard-blank-panels`  
Evidence: code inspection of legacy page components vs new-IA workspaces; browser verification during Phase F (F2/F3) on new-IA routes only. Legacy routes were **not** modified.

This document supports Phase F retirement decisions. Per `web-dashboard/ARCHITECTURE.md`, legacy routes must not be deleted or redirected until explicit parity sign-off.

---

## Summary

| Legacy route | Parity | New-IA primary equivalent |
|--------------|--------|---------------------------|
| `/legacy/top-plays` | **Partial** | `/leaderboards` (Top Plays category) |
| `/legacy/boards` | **Partial** | `/leaderboards` (category boards) |
| `/legacy/games` | **Partial** | `/today` (tabbed game workspace) |
| `/legacy/player` | **Partial** | `/research` (10-tab player workspace) |
| `/legacy/batted-balls` | **Partial** | `/research?tab=batted-balls` |
| `/legacy/splits` | **Partial** | `/today` → Team Splits tab |
| `/legacy/command-center` | **Partial** | `/today` + `/leaderboards` |

**No legacy route has Full parity.** All retain unique controls, layouts, or deep-link behavior not fully replicated in new IA.

---

## `/legacy/top-plays`

### 1. Legacy purpose
Curated **Top 5 per category** across the full slate — Excel “Top Plays” tab equivalent. Analyst quick-scan of best opportunities slate-wide.

### 2. Controls and filters
- **None** — no game, player, timeframe, situation, or pitch filters.
- Page-local read of `ExportContext` only; no shared `GameContext` / `FilterContext`.

### 3. Data displayed
- Combined table: all 25 plays (`TopPlaysTable` with `showCategory`).
- Per-category cards: 5 categories × Top 5 (`data.top_plays[category]`).
- Columns: Rank, Category, Hitter, Team, Game, Opp SP, Pitch, Score, Tier, Key Stat, Key Val.

**Source:** `TopPlaysPage.tsx`

### 4. Deep-link / query behavior
- Route: `/legacy/top-plays` (also `/top-plays` → redirect preserves query string).
- No query params consumed; stateless.

### 5. New-IA equivalent
- **`/leaderboards`** — category `top-plays`, scopes: Selected Game / Today's Slate / Entire League.
- Shared header filters (timeframe/situation/pitch) apply with documented honesty notes (`LeaderboardFilterNote`).
- Pitch filter can narrow rows; timeframe/situation do not recompute pre-aggregated export rows.

### 6. Parity status
**Partial**

### 7. Exact missing capabilities
| Capability | Legacy | New IA |
|------------|--------|--------|
| All categories in one combined table | Yes | No — one category/view at a time |
| Per-category stacked cards on same page | Yes (5 cards) | No |
| Zero-filter slate-wide view | Yes | Scope + filter chrome always present |
| Category column in unified table | Yes | Only when viewing Top Plays category |

### 8. Blockers to retirement
- Analysts using single-page “full slate Top Plays + by-category cards” layout.
- Bookmark `/top-plays` and `/legacy/top-plays` without learning Leaderboards scope/category UX.
- No automated regression test comparing row sets (scope=slate vs legacy full table).

### 9. Recommended disposition
**Redirect after parity** — once Leaderboards adds optional “All categories” combined view (or documented scope=slate + export note satisfies stakeholders). Until then: **Keep**.

---

## `/legacy/boards`

### 1. Legacy purpose
**Category boards** — Top 20 hitters per metric category with full stat columns; sortable tables for deep stat review.

### 2. Controls and filters
- **Team filter** dropdown (all teams in export).
- No game scope, pitch, timeframe, or situation filters.
- All five category sections visible on one scrollable page.

### 3. Data displayed
- Per category: `CategoryBoardTable` with up to 20 rows (`data.category_boards[category]`).
- Full board stat columns (sortable via `DataTable`).

**Source:** `CategoryBoardsPage.tsx`

### 4. Deep-link / query behavior
- Route: `/legacy/boards` (also `/boards` → redirect).
- No query params.

### 5. New-IA equivalent
- **`/leaderboards`** — one category at a time via `LeaderboardCategoryNav`.
- Scope control (game / slate / league).
- Shared pitch filter; timeframe/situation notes shown when non-default.
- Reuses `CategoryBoardTable` / `TopPlaysTable` with `LeaderboardPlayerLink` → `openResearch()`.

### 6. Parity status
**Partial**

### 7. Exact missing capabilities
| Capability | Legacy | New IA |
|------------|--------|--------|
| Team filter dropdown | Yes | No |
| All five categories on one page | Yes | No — tabbed category nav |
| Game-scoped boards | No explicit scope | Yes (Selected Game scope) |
| League-wide boards with export window label | Implicit full export | Yes (Entire League scope + note) |

### 8. Blockers to retirement
- Team filter workflow for “show me all Mets rows across categories.”
- Single-page category board review pattern.
- Stakeholder sign-off that per-category Leaderboards navigation is acceptable.

### 9. Recommended disposition
**Redirect after parity** — add team filter to Leaderboards or confirm scope=slate + export search satisfies need. Until then: **Keep**.

---

## `/legacy/games`

### 1. Legacy purpose
**Game Hub** — single-page deep dive on one game: context, pitcher splits, expected lineups, pitch mix, bullpen.

### 2. Controls and filters
- **Local game dropdown** (`game_id` string, not `game_pk`).
- No shared research chrome; independent page state.

### 3. Data displayed
- Game context strip (records, park, weather, L5).
- Pitcher splits: situation, platoon, inning splits (both SPs).
- Expected batting orders + bullpen (last 4 days) per side.
- Pitch mix chips with usage %.

**Source:** `GameHubPage.tsx`

### 4. Deep-link / query behavior
- Route: `/legacy/games` (also `/games` → redirect).
- No query params; game selection is local `useState` defaulting to first game.

### 5. New-IA equivalent
- **`/today`** with shared game selection (`ResearchContextHeader` + slate cards).
- Tabs: Overview, Pitchers, Lineups, Team Splits, Matchups.
- Same underlying components (`GameContextStrip`, `PitcherSplitsBlock`, `ExpectedLineupTable`, `BullpenTable`, etc.) split across tabs.

### 6. Parity status
**Partial**

### 7. Exact missing capabilities
| Capability | Legacy | New IA |
|------------|--------|--------|
| Single scrollable game dossier | Yes | Split across 5 tabs |
| Local game picker independent of URL | Yes | Game in URL/context (`?game=` pk) |
| All game hub sections visible at once | Yes | No — tab navigation required |
| Deep link to specific game on page load | No | Yes (`?game=` via research URL) |

### 8. Blockers to retirement
- Users expecting one-page Game Hub layout.
- `/games` bookmark without URL game param (legacy defaulted to first game).
- Bullpen + lineups + pitcher splits not visible simultaneously.

### 9. Recommended disposition
**Redirect after parity** — optional “Game Hub” consolidated tab or print-friendly single-page view on Today. Until then: **Keep**.

---

## `/legacy/player`

### 1. Legacy purpose
**Player Matchup Card** — search any slate hitter; season splits, pitch-mix vs opposing starter, zone heatmap, game log.

### 2. Controls and filters
- **Global hitter search** + dropdown (all names in `data.matchups`, ~full slate pool).
- Season split toggles: Overall, Day, Night (via `PlayerDayNightTable`).
- Per-pitch filter chips on matchup rows.
- Independent of selected game.

### 3. Data displayed
- Recent game log chart (`GameLogChart`).
- Season splits (`PlayerDayNightTable`).
- Pitch-mix matchup table (`CategoryBoardTable` on `data.matchups` rows).
- Zone heatmap (`ZoneHeatmap`).

**Source:** `PlayerMatchupPage.tsx`

### 4. Deep-link / query behavior
- **`?name=`** query param — case-insensitive match against matchup hitter names.
- Route: `/legacy/player?name=…` (also old `/player?name=` → `/research` redirect via Phase E).
- `HitterLink` on legacy routes navigates to `/legacy/player?name=`.

### 5. New-IA equivalent
- **`/research`** — 10 tabs (Overview, Matchup, Recent Games, Splits, Pitch Matchup, Heatmaps, Batted Balls, Swing Metrics, Outcome Profile, Scouting Summary).
- Player picker **scoped to selected game lineup** (header dropdown).
- URL: `?player=`, `?game=`, `?tab=`, filters via `buildResearchNavigation()`.
- `/player`, `/player/:id`, `/matchup/*` → `/research` (`ResearchRedirect` + `buildResearchRedirectPath`).

### 6. Parity status
**Partial** (strongest overlap, but selection model differs)

### 7. Exact missing capabilities
| Capability | Legacy | New IA |
|------------|--------|--------|
| Search any slate hitter (not in selected game) | Yes | No — game lineup pool only |
| `?name=` deep link on legacy route | Yes | Translated to `?player=` on `/research` only |
| Day/Night split **buttons** on Splits panel | Yes (explicit toggles) | Driven by shared situation filter |
| Single-page vertical stack of all panels | Yes | Tabbed workspace |
| Scouting summary / swing metrics / outcome profile | No | Yes (new tabs) |

### 8. Blockers to retirement
- Cross-game hitter lookup (e.g. bench player not in current lineup export).
- Legacy bookmark `/legacy/player?name=` workflows on legacy IA.
- Codex/product sign-off that game-scoped research replaces global search.

### 9. Recommended disposition
**Redirect after parity** — `/legacy/player?name=` → `/research?player=` once league-mode or slate-wide player search exists. Until then: **Keep** (HitterLink still targets legacy on `/legacy/*`).

---

## `/legacy/batted-balls`

### 1. Legacy purpose
**Batted-ball exploration** — EV/LA scatter and batted-ball profile for any hitter in export.

### 2. Controls and filters
- **Global hitter search** from `data.batted_balls` keys (broader than matchup pool).
- No game or pitch filters.

### 3. Data displayed
- Exit velocity vs launch angle scatter (`ExitVeloScatter`).
- Batted-ball profile card (`BattedBallProfileCard`).

**Source:** `BattedBallsPage.tsx`

### 4. Deep-link / query behavior
- **`?name=`** query param — same matching logic as player page.
- Route: `/legacy/batted-balls` (also `/batted-balls` → redirect).

### 5. New-IA equivalent
- **`/research?tab=batted-balls`** — same scatter + profile components.
- Player must be selected via game-scoped header; uses `useResearchPlayerData()`.

### 6. Parity status
**Partial**

### 7. Exact missing capabilities
| Capability | Legacy | New IA |
|------------|--------|--------|
| Hitter pool from `batted_balls` keys | Yes | Game lineup pool only |
| Standalone page (no research chrome) | Yes | Tab inside Research workspace |
| `?name=` deep link on legacy route | Yes | Requires `/research?player=&tab=batted-balls` |

### 8. Blockers to retirement
- Hitters with batted-ball data but not in current game lineup.
- `/batted-balls?name=` bookmarks.

### 9. Recommended disposition
**Redirect after parity** — map `?name=` to research batted-balls tab when player resolution works slate-wide. Until then: **Keep**.

---

## `/legacy/splits`

### 1. Legacy purpose
**Team splits** — platoon, day/night, and batter-vs-pitcher (BVP) tables for both teams in a game.

### 2. Controls and filters
- **Local game dropdown**.
- Split mode buttons: Overall, vs LHP, vs RHP, Day, Night, **vs Today’s SP (bvp)**.
- Per-team pitch-mix filter chips → switches to per-pitch `CategoryBoardTable`.

### 3. Data displayed
- `TeamSplitsTable` or pitch-filtered matchup rows per side.
- Uses `away_splits` / `home_splits` from `game_details`.

**Source:** `TeamSplitsPage.tsx`

### 4. Deep-link / query behavior
- Route: `/legacy/splits` (also `/splits` → redirect).
- No query params.

### 5. New-IA equivalent
- **`/today`** → **Team Splits** tab (`TodayTeamSplitsTab`).
- Split mode from shared **Situation** filter (Overall, Home, Away, Day, Night, vs LHP, vs RHP).
- Pitch type from shared **FilterBar**.
- Same `TeamSplitsTable` / `CategoryBoardTable` components.

### 6. Parity status
**Partial**

### 7. Exact missing capabilities
| Capability | Legacy | New IA |
|------------|--------|--------|
| **BVP / vs Today’s SP** split mode | Yes (`bvp` button) | **Missing** — `situationToSplit()` has no bvp mapping |
| Local game picker | Yes | Shared header game selector |
| Dedicated splits page | Yes | Tab under Today |
| Home/Away situation filters | No | Yes (new IA adds home/away via situation) |

### 8. Blockers to retirement
- **BVP split** is a functional gap in new IA (code supports `split === 'bvp'` in panel but never selected from filters).
- Analysts using “vs Today’s SP” as primary team split view.

### 9. Recommended disposition
**Keep** until BVP parity implemented on Today Team Splits tab (situation option or dedicated control). Then **Redirect after parity** from `/legacy/splits`.

---

## `/legacy/command-center`

### 1. Legacy purpose
Original **Phase 0 landing** — slate overview + top plays by category; entry point before new IA.

### 2. Controls and filters
- None.
- Summary stat tiles (category count, top-play count).

### 3. Data displayed
- Simple slate cards from `data.games` (game_id, SP names).
- Top plays by category (same data as `/legacy/top-plays` per-category sections).

**Source:** `CommandCenter.tsx` at `/legacy/command-center`

### 4. Deep-link / query behavior
- Route: `/legacy/command-center` only (not in root redirect table).
- No query params.

### 5. New-IA equivalent
- **`/today`** — interactive slate (`GameCardGrid`) + game tabs.
- **`/leaderboards`** — top plays and category boards with scope.
- App index `/` → `/today`.

### 6. Parity status
**Partial**

### 7. Exact missing capabilities
| Capability | Legacy | New IA |
|------------|--------|--------|
| Compact slate list (non-selectable cards) | Yes | Interactive game cards + context |
| Inline top-plays-by-category on landing | Yes | Separate Leaderboards workspace |
| Category/top-play count summary tiles | Yes | No equivalent summary tiles |
| Zero chrome / minimal UI | Yes | Full ResearchChrome on Today |

### 8. Blockers to retirement
- Residual “command center” mental model for daily start.
- No single page combining slate summary + top plays.

### 9. Recommended disposition
**Retire after sign-off** — lowest traffic expected; `/today` is canonical entry. Keep until stakeholders confirm Today + Leaderboards replace morning workflow. Do not redirect until Top Plays parity (above) is addressed.

---

## Cross-cutting notes

### Root alias redirects (unchanged in Phase F)
| Old path | Resolves to |
|----------|-------------|
| `/top-plays` | `/legacy/top-plays` |
| `/boards` | `/legacy/boards` |
| `/games` | `/legacy/games` |
| `/batted-balls` | `/legacy/batted-balls` |
| `/splits` | `/legacy/splits` |
| `/player`, `/matchup` | `/research` (Phase E) |

### Retirement prerequisites (all routes)
1. Explicit product/Codex sign-off documented.
2. Browser verification checklist per route (not complete as of this matrix).
3. Deep-link migration plan for `?name=` legacy URLs.
4. No regression in export-driven row counts for equivalent views.

### Phase F scope boundary
Phase F (F1–F3) did **not** redirect, delete, or modify legacy page behavior. This matrix is assessment-only.
