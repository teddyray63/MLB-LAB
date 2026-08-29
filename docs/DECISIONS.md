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

---

## DEC-008 — Branch and archive lifecycle policy

**Status:** Accepted

**Date:** 2026-08-23

**Context:**
Infrastructure Upgrade 9 cleaned merged, backup, experimental, and review branches
while preserving durable recovery points. Mutable backup branches were replaced with
annotated `archive/*` tags. A divergent Claude experiment branch was archive-tagged
before remote deletion. One review branch (`review/phase-d`) remains intentionally
preserved pending extraction decision. No consolidated repository policy documented
these proven steps.

**Decision:**
Adopt the branch and archive lifecycle policy in `docs/BRANCH_ARCHIVE_POLICY.md` as
the operational standard for:

- merged branch cleanup (ancestry proof, zero unique commits, safe `-d`)
- split-tip handling (audit both tips; no `-D` shortcut)
- backup branch → annotated archive tag migration before deletion
- archive tag immutability and single-tag push discipline
- divergent experiment evaluation (archive-tag when not integration-worthy)
- `review/*` retention rules and naming conventions

Current intentional exception: preserve `review/phase-d` at
`7a016e81d1ae6e4ebc90c1ea702fad2664f69d4d` as a local review/reference branch; do
not cherry-pick or merge wholesale; reimplement against G0b contracts if product work
later requires equivalent behavior.

**Evidence:**
- Upgrade 9 Phase 2d closeout audit (2026-08-23): final topology verified — remote
  `origin/main` only; local `main` + `review/phase-d`; three `archive/*` tags present
- Archive tags verified local and remote:
  `archive/pre-dashboard-merge-2026-07-16`,
  2026-08-02 archive recovery tag (object `72891ca1b19ab1f9a4e2a6fdaf1b7ffec71d7d76`, peeled `54ca81af23a01fcf001e30ba084ae372d8617acc`),
  `archive/claude-odds-engine-experiment-2026-06-30`
- Retired branches absent locally and remotely (including `sports-resource-hub`,
  `backup/*`, `claude/odds-engine-integration-zhe77q`)

**Consequences:**
Branch cleanup and archival tasks must follow `docs/BRANCH_ARCHIVE_POLICY.md`.
`PROJECT_STATE.md` records current topology; policy doc holds operational detail.
Deleting `review/phase-d` or converting it to a tag requires a separate authorized
task after the extraction decision is closed.

**Revisit only if:**
Repository workflow constraints change materially (for example mandatory long-lived
integration branches), or a new recovery mechanism supersedes annotated archive tags.

**Supersedes:**
None

---

## DEC-009 — Switch-hitter matchup-effective batting side for pitcher platoon splits

**Status:** Accepted

**Date:** 2026-08-29

**Context:**
G0b enrichment populates `pitcher_split_vs_hitter_side` by mapping hitter
canonical `bats` to pitcher Statcast split keys (`L→vs_lhb`, `R→vs_rhb`).
Switch hitters have canonical `bats=S`. The mapping yields null, leaving
matchup rows without pitcher platoon context despite working identity plumbing
and available pitcher split blocks.

Hitter-side splits (`hitter_split_vs_pitcher_hand`) already work for switch
hitters because they key off opposing pitcher `throws`, not hitter identity.

**Decision:**
Introduce a **matchup-effective batting side** used solely to select
`pitcher_split_vs_hitter_side` when canonical `bats=S`.

Rule (pregame default):
- Switch hitter vs RHP → effective side **L** → select pitcher split **vs_lhb**
- Switch hitter vs LHP → effective side **R** → select pitcher split **vs_rhb**

Canonical identity semantics are unchanged: `bats`, `hitter_bats`, and
`LineupBatter.hand` remain **S** for switch hitters. The effective side is
contextual, derived at matchup construction time, and must not overwrite or
replace canonical identity fields.

**CANONICAL IDENTITY SEMANTICS:**
- Source: MLB feed `gameData.players[].batSide.code`
- Values: `L`, `R`, `S`
- Switch hitters MUST remain `S` in all identity and export identity fields
- Never infer or convert `S` to `L`/`R` in identity objects

**MATCHUP-EFFECTIVE SIDE SEMANTICS:**
- Derived only when canonical `bats=S` and opposing starter `throws` is known
- Used ONLY for selecting `pitcher_split_vs_hitter_side` split key
- Serialized as `matchup_effective_bats` on `EnrichmentMatchup`
- Not stored as a substitute for canonical `bats`
- DERIVED PREGAME MATCHUP SIDE — NOT OBSERVED PA STAND

**SWITCH-HITTER RULE:**
```
if hitter_bats == "S" and pitcher_throws == "R":
    effective_bats = "L"  → pitcher_split_key = "vs_lhb"
if hitter_bats == "S" and pitcher_throws == "L":
    effective_bats = "R"  → pitcher_split_key = "vs_rhb"
if hitter_bats in ("L", "R"):
    effective_bats = hitter_bats  (unchanged)
else:
    pitcher_split_key = None
```

**KNOWN LIMITATIONS:**
- Assumes conventional platoon default (~99%+ of observed switch-hitter PAs)
- Does not model rare same-handed switch-hitter PAs
- Does not handle switch-pitcher declaration order (MLB Rule 5.07(f))
- Pregame only; does not predict in-game pinch-hit or side changes
- Does not alter hitter split formulas, BVP, pitch-type, L5/L10, or Statcast
  aggregation logic

**UI/EXPORT DISCLOSURE REQUIREMENTS:**
- Display canonical `bats=S` as identity (never show effective L/R as identity)
- When effective side is used, consumers should indicate that pitcher platoon
  split is selected via platoon-default rule
- Do not imply observed tonight-side certainty
- Disclosure semantics: "Switch-hitter side is derived from the opposing
  pitcher's throwing hand for platoon-split context; actual in-game batting
  side may differ."

**TEST REQUIREMENTS:**
1. Switch hitter vs RHP selects `vs_lhb`; canonical `bats` remains `S`
2. Switch hitter vs LHP selects `vs_rhb`; canonical `bats` remains `S`
3. L/R hitters unchanged (regression)
4. Unknown `throws` → pitcher split remains null
5. Identity fields never mutated to L/R for switch hitters

**NON-GOALS:**
- Converting switch hitters to L/R in identity
- Observed-side historical modeling
- Switch-pitcher rule handling
- Changing Statcast split aggregation formulas
- Changing hitter-side split selection logic

**Evidence:**
- `backend/export/enrichment/matchups.py` — prior L/R-only pitcher split mapping
- `backend/export/enrichment/pitcher_stats.py` — `vs_lhb`/`vs_rhb` keyed on Statcast `stand`
- Aug 28 validation — 54/54 hitter splits, 49/54 pitcher splits before DEC-009
- Cached Statcast analysis — platoon-opposite on 4,900/4,908 switch-hitter PAs (99.8%)

**Consequences:**
- Switch-hitter matchup rows gain pitcher platoon context under platoon-default rule
- Identity and hitter-side splits unchanged
- `matchup_effective_bats` exposes derived side for audit/disclosure

**Revisit only if:**
- Product requires observed-side modeling
- Switch-pitcher matchups become common enough to warrant special handling
- MLB feed begins supplying pregame expected batting side

**Supersedes:**
None
