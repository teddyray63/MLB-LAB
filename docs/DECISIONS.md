# Project Decision Log

This file records decisions that have actually been made.

- **FACTS** belong in evidence and source material.
- **TASKS** belong in task contracts and project tracking.
- **DECISIONS** belong here.

A decision may be revisited only when new evidence, requirements, or constraints
justify doing so.

Use this entry template for new decisions:

## DEC-XXX — Short title

**Status:** Accepted | Superseded | Rejected

**Date:** YYYY-MM-DD

**Context:**
What problem required a decision?

**Decision:**
What was actually decided?

**Evidence:**
What verified facts or repository artifacts support the decision?

**Consequences:**
What does this decision imply for future work?

**Revisit only if:**
What specific new evidence, requirement, or constraint would justify
reopening this decision?

**Supersedes:**
DEC-XXX or None

---

## DEC-001 — Preserve legacy dashboard routes until explicit parity sign-off

**Status:** Accepted

**Date:** 2026-08-02

**Context:**
The React dashboard has a new information architecture (`/today`, `/research`,
`/leaderboards`, …) alongside legacy routes under `/legacy/*`. Retiring legacy
routes requires knowing whether new-IA equivalents fully replace them.

**Decision:**
Do not delete, redirect, or materially change `/legacy/*` routes until explicit
parity sign-off. Legacy route retirement remains deferred until that sign-off.

**Evidence:**
- `PROJECT_STATE.md` — Deferred: "Legacy route retirement — **deferred pending explicit parity sign-off**"
- `web-dashboard/ARCHITECTURE.md` — "Legacy routes under `/legacy/*` remain frozen until parity is verified"; "unchanged until explicit parity sign-off"
- `docs/LEGACY_PARITY_MATRIX.md` — "legacy routes must not be deleted or redirected until explicit parity sign-off"; all seven legacy routes assessed **Partial** parity

**Consequences:**
New-IA work proceeds on canonical routes. Legacy pages stay available. Parity
gaps documented in `docs/LEGACY_PARITY_MATRIX.md` must be resolved or explicitly
accepted before retirement.

**Revisit only if:**
Explicit parity sign-off is recorded, or stakeholders authorize retirement with
documented acceptance of remaining gaps.

**Supersedes:**
None

---

## DEC-002 — Promotion Policy v1: terminal slate only

**Status:** Accepted

**Date:** 2026-08-03

**Context:**
The live daily export must be promoted from candidate exports without promoting
incomplete or in-progress slates.

**Decision:**
Promotion Policy (v1):

- Promote only the most recent slate where every scheduled game has reached a
  recognized terminal status.
- Walk backward mechanically from the current date until a fully terminal slate
  is found.
- In-progress, warmup, scheduled, postponed, suspended, or otherwise non-terminal
  slates are ineligible.
- Rolling/intraday promotion remains out of scope.

**Evidence:**
- `PROJECT_STATE.md` — "Promotion Policy (v1)" under First Production Promotion (decision date 2026-08-03)

**Consequences:**
Promotion workflows must enforce terminal-slate eligibility. Intraday or rolling
promotion requires a new policy decision before implementation.

**Revisit only if:**
Product requirements explicitly authorize rolling/intraday promotion, or terminal
status rules need revision based on verified export behavior.

**Supersedes:**
None

---

## DEC-003 — Reference tests use frozen fixtures, not live production export

**Status:** Accepted

**Date:** 2026-08-03

**Context:**
After the first production promotion, five tests were coupled to the mutable live
export, making reference behavior depend on production data that changes over time.

**Decision:**
Tests that assert reference behavior must use frozen fixtures. Production exports
are not immutable reference fixtures and must not be used as such.

**Evidence:**
- `PROJECT_STATE.md` — Post-promotion test finding: "five tests were coupled to the mutable live export"; "tests were migrated to frozen fixtures"; "production exports are no longer used as immutable reference fixtures"

**Consequences:**
New or migrated reference-behavior tests should bind to fixtures under
`tests/fixtures/` (or equivalent frozen artifacts), not `data/daily_export.json`
or other mutable live exports.

**Revisit only if:**
A new testing strategy is explicitly approved that defines a different immutable
reference source with documented update controls.

**Supersedes:**
None

---

## DEC-004 — New-IA pages use shared GameContext and FilterContext only

**Status:** Accepted

**Date:** 2026-08-01

**Context:**
The new dashboard information architecture requires consistent game, player,
pitcher, and filter selection across `/today`, `/research`, and `/leaderboards`.

**Decision:**
All new-IA pages mount inside `ResearchProviders`. No new-IA page may add local
game, player, pitcher, or timeframe selectors. Shared context providers
(`GameContextProvider`, `FilterContextProvider`) govern selection state.

**Evidence:**
- `web-dashboard/ARCHITECTURE.md` — "Architecture Rules (Locked)": Context providers table; "No page may add local game, player, pitcher, or timeframe selectors"

**Consequences:**
New analytical components on new-IA routes should use shared hooks
(`useGameContext()`, `useFilters()`, etc.) rather than page-local selector
state unless there is a documented exception.

**Revisit only if:**
A new workspace is added with an explicitly approved architecture change recorded
here and in `web-dashboard/ARCHITECTURE.md`.

**Supersedes:**
None

---

## DEC-005 — Do not fabricate leaderboard data when export arrays are empty

**Status:** Accepted

**Date:** 2026-08-03

**Context:**
At first production promotion, `top_plays` and `category_boards` export sections
were empty, causing empty leaderboard UI. A choice was required between
fabricating replacement rankings and accepting empty states.

**Decision:**
Accept known empty leaderboard states. Do not introduce fabricated replacement
rankings or scores when export arrays are empty and original formulas are
unavailable.

**Evidence:**
- `PROJECT_STATE.md` — "Known product regressions accepted": "top_plays is empty"; "category_boards is empty"; "original formulas are unavailable"; "no fabricated replacement rankings or scores were introduced"

**Consequences:**
Empty leaderboard states are a known limitation until export formulas or data
sources are restored. Fixes must come from real data or restored computation, not
placeholder rankings.

**Revisit only if:**
Export pipeline reliably populates `top_plays` and `category_boards`, or an
explicit product decision authorizes a documented replacement computation.

**Supersedes:**
None

---

## DEC-006 — Evidence storage: commit metadata, ignore raw captures

**Status:** Accepted

**Date:** 2026-08-14

**Context:**
Investigation workflows capture external API responses under `evidence/`.
The repository needs a durable policy for what enters git versus what remains
local, without conflating provenance records with payload semantics.

**Decision:**

1. Raw external captures under `evidence/` (for example `*.raw.json`) are
   ignored by default.
2. Metadata/manifests describing evidence may be committed.
3. Metadata for an external capture must record enough provenance to identify
   and verify the corresponding raw artifact (request method, request URL,
   capture timestamp, HTTP status, content type, raw artifact filename, byte
   count, SHA256 when available).
4. Raw captures must not be promoted to test fixtures automatically.
5. If a raw capture becomes a durable test fixture, that requires an explicit
   task/decision and the fixture lives under repository fixture conventions.
6. Metadata alone is not proof of fields inside an unavailable raw artifact.

**Evidence:**
- `AGENTS.md` — Evidence artifacts section
- `.gitignore` — `evidence/**/*.raw.json` ignore rule
- `evidence/mlb/game-995731-lineup.metadata.txt` — example metadata manifest

**Consequences:**
Agents commit investigation provenance without bloating history with raw
captures. Raw artifacts remain local for deterministic inspection when present.
Test fixtures require explicit promotion decisions.

**Revisit only if:**
The team adopts a policy to commit all evidence artifacts, or metadata fields
prove insufficient for verification without the raw capture in git.

**Supersedes:**
None

---

## DEC-007 — primary_position is not a starting-defensive-position contract

**Status:** Accepted

**Date:** 2026-08-14

**Context:**
Investigation of lineup identity found that MLB feed `position.abbreviation` was
being considered as a possible game-specific starting defensive position.

**Decision:**
Treat `ExportPlayer.primary_position` only as the existing optional
player-associated position used by internal heuristics.

Do not represent it as guaranteed game-specific starting defensive position.

The current product/export contract does not require starting defensive position,
so no additional MLB source discovery is required for that purpose.

**Evidence:**
- `backend/export/identity_models.py` — `ExportPlayer.primary_position`:
  `str | None = None` (optional)
- `backend/export/mlb_game_feed.py` — `parse_game_feed_side()` and
  `merge_roster_players()` read `position.abbreviation` into `primary_position`
- `backend/export/builders/players.py` — bench role heuristic uses
  `primary_position` for P/non-P classification
- `backend/export/player_logs/hitter_logs.py` — excludes `primary_position == "P"`
  from default hitter set
- `backend/export/player_logs/pitcher_logs.py` and
  `backend/export/build_player_logs.py` — include `primary_position == "P"` in
  pitcher ID set
- `backend/export/daily_export_models.py` — `LineupBatter` has no position field;
  `DailyExport` does not serialize `ExportPlayer`
- `backend/export/identity_validation.py` — does not validate position presence
- `tests/test_players_builder.py` — `test_missing_position_stays_null` accepts
  absent position

**Consequences:**
- Existing runtime behavior remains unchanged.
- Existing lineup membership semantics remain unchanged.
- No new MLB endpoint is required.
- A future feature requiring actual starting defensive positions must establish
  a separate source-semantic contract rather than reusing `primary_position`
  without evidence.

**Revisit only if:**
A future product/schema requirement explicitly requires game-specific starting
defensive position.

**Supersedes:**
None
