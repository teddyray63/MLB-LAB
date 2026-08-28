# MLB-LAB Operator Playbook

Daily production workflow for the G0b static-export dashboard. This document is
authoritative for local operator steps; deployment is a separate governed action
(see `docs/DEPLOYMENT.md`).

## Phases (do not conflate)

| Phase | Purpose | Mutates live export? |
|-------|---------|----------------------|
| **GENERATE** | Build candidate JSON under `data/candidates/` | No |
| **VERIFY** | Validate schema, slate, statuses, SHA | No |
| **PROMOTE/PIN** | Copy eligible candidate → `data/daily_export.json` | **Yes** |
| **BUILD** | Sync export into dashboard `dist/` | Overwrites `data/daily_export.json` if misused |
| **DEPLOY** | Upload `web-dashboard/dist/` to static host | Remote only |

---

## Prerequisites

```bash
cd /path/to/MLB-LAB
python3 -m pip install -r requirements.txt pytest
cd web-dashboard && npm ci && cd ..
```

---

## 1. Obtain / update daily candidate

Build a full G0b candidate (never writes live export):

```bash
python3 scripts/build_daily_export.py \
  --build-full-candidate \
  --date YYYY-MM-DD \
  --output data/candidates/daily_export.YYYY-MM-DD.json
```

Research ops for a slate may use a dated one-shot script under
`data/candidates/` (e.g. `run_research_YYYY-MM-DD.py`) that writes:

- `data/candidates/daily_export.YYYY-MM-DD.json`
- `data/candidates/slate.YYYY-MM-DD.json`
- `data/candidates/research_sidecar.YYYY-MM-DD.json`

---

## 2. Inspect slate

```bash
python3 scripts/evidence.py data/candidates/slate.YYYY-MM-DD.json
python3 scripts/evidence.py data/candidates/daily_export.YYYY-MM-DD.json --match games date
```

Or read `games[]` directly:

```bash
python3 -c "
import json; d=json.load(open('data/candidates/daily_export.YYYY-MM-DD.json'))
print('date:', d['date'], 'games:', len(d['games']))
for g in d['games']:
    print(g.get('game_pk'), g.get('status'), g.get('game_id'))
"
```

---

## 3. Inspect game statuses (DEC-002 eligibility)

DEC-002: promote **only** when every game on the slate is in a recognized
**terminal** status (e.g. `Final`, `Game Over`, `Completed Early`).

```bash
python3 -c "
import json
from collections import Counter
TERMINAL = {'Final','Game Over','Completed Early','Forfeit','Cancelled','Postponed'}
p='data/candidates/daily_export.YYYY-MM-DD.json'
d=json.load(open(p))
c=Counter(g.get('status','?') for g in d['games'])
eligible=all(g.get('status') in TERMINAL for g in d['games'])
print('status counts:', dict(c))
print('DEC-002 eligible:', eligible)
"
```

**Do not promote** if any game is `Scheduled`, `Pre-Game`, `In Progress`, `Warmup`,
or otherwise non-terminal.

---

## 4. Run research ops

Ad-hoc research collection (example pattern):

```bash
python3 data/candidates/run_research_YYYY-MM-DD.py
```

Produces markdown/JSON under `reports/` and sidecar enrichment. Does **not**
promote live export.

---

## 5. Run G0b layered builds (optional diagnostics)

```bash
python3 scripts/build_daily_export.py --build-games --date YYYY-MM-DD
python3 scripts/build_daily_export.py --build-lineups --date YYYY-MM-DD
python3 scripts/build_daily_export.py --build-matchups --date YYYY-MM-DD
```

---

## 6. BVP / vs Today's SP

BVP splits are populated in export `matchups[]` / `game_details.*_splits` when
Statcast sample exists against the opposing starter ID. Verify:

```bash
python3 -c "
import json
d=json.load(open('data/candidates/daily_export.YYYY-MM-DD.json'))
m=d.get('matchups',[])
bvp=sum(1 for r in m if r.get('bvp') is not None)
print('matchups:', len(m), 'bvp non-null:', bvp)
"
```

Sidecar research may contain BVP counts not yet merged into the export candidate.

---

## 7. Validate candidate

```bash
python3 scripts/build_daily_export.py \
  --validate-existing data/candidates/daily_export.YYYY-MM-DD.json
```

Or validate without rebuild:

```bash
python3 scripts/build_daily_export.py \
  --validate-only \
  --output data/candidates/daily_export.YYYY-MM-DD.json
```

---

## 8. Determine DEC-002 eligibility

See step 3. Terminal-slate check is **mandatory** before promotion.

---

## 9. Validate freshness / provenance

```bash
shasum -a 256 data/candidates/daily_export.YYYY-MM-DD.json
python3 -c "
import json; d=json.load(open('data/candidates/daily_export.YYYY-MM-DD.json'))
m=d.get('export_meta',{})
print('generated_at:', m.get('generated_at'))
print('runner_version:', m.get('runner_version'))
print('statcast:', m.get('statcast_start'), '-', m.get('statcast_end'))
"
```

Record candidate SHA256 before any promotion or build pin.

---

## 10. Create / verify backup (required before promotion)

Promotion creates a timestamped backup automatically. Inspect existing backups:

```bash
ls -la data/backups/
shasum -a 256 data/daily_export.json   # current live SHA
```

---

## 11. Promote / pin (eligible candidates only)

Dry-run first:

```bash
CAND=data/candidates/daily_export.YYYY-MM-DD.json
SHA=$(shasum -a 256 "$CAND" | awk '{print $1}')

python3 scripts/build_daily_export.py \
  --promotion-dry-run \
  --candidate "$CAND" \
  --candidate-sha256 "$SHA"
```

Real promotion (creates backup, atomic replace):

```bash
python3 scripts/build_daily_export.py \
  --promote \
  --candidate "$CAND" \
  --candidate-sha256 "$SHA" \
  --yes-promote
```

Verify post-promotion:

```bash
shasum -a 256 data/daily_export.json
python3 scripts/build_daily_export.py --validate-existing data/daily_export.json
```

---

## 12. Prepare build safely

### ⚠️ WARNING — `prepare_export_for_build.sh`

This script **overwrites `data/daily_export.json`** without creating a promote
backup. Use only when:

1. Replacement of live export is **intentional** (deploy pin of an already-approved SHA), **or**
2. Source is already `data/daily_export.json` with matching SHA (no-op copy).

**Do not** point this script at a candidate casually.

```bash
# Safe: pin an approved candidate SHA for build (still overwrites live!)
scripts/prepare_export_for_build.sh \
  <EXPECTED_SHA256> \
  data/candidates/daily_export.YYYY-MM-DD.json
```

Prefer governed `--promote` when changing the live export artifact.

---

## 13. Frontend tests

```bash
cd web-dashboard
npm test
```

---

## 14. Build

```bash
cd web-dashboard
npm run build
```

Prebuild runs `sync-data` → copies `data/daily_export.json` to `public/data/`.

---

## 15. Production / repo-health verification

```bash
python3 -m pytest tests/ -q
python3 scripts/build_daily_export.py --validate-existing tests/fixtures/reference_export_pre_promotion.json
python3 scripts/repo_health.py --fast --no-network
```

Standard scan (includes more checks):

```bash
python3 scripts/repo_health.py --standard --no-network
```

CI parity (`.github/workflows/verify-g0b.yml`):

```bash
python3 -m pytest tests/ -q
cd web-dashboard && npm test && npm run build
```

---

## 16. Inspect final outputs

```bash
shasum -a 256 data/daily_export.json
shasum -a 256 web-dashboard/dist/data/daily_export.json
python3 -c "
import json; d=json.load(open('data/daily_export.json'))
print('date:', d['date'])
print('runner:', d.get('export_meta',{}).get('runner_version'))
"
```

Dist SHA **must** match pinned live SHA.

---

## 17. Rollback / recover

From promotion backup:

```bash
BACKUP=data/backups/daily_export.YYYYMMDDTHHMMSSZ.xxxxxxxxxxxx.json
SHA=$(shasum -a 256 "$BACKUP" | awk '{print $1}')

python3 scripts/build_daily_export.py \
  --rollback-from-backup "$BACKUP" \
  --candidate-sha256 "$SHA" \
  --yes-promote
```

Or restore via `prepare_export_for_build.sh` + rebuild (only with verified backup SHA).

---

## 18. When NOT to promote

- Any game on the slate is non-terminal (DEC-002).
- Candidate SHA does not match `--candidate-sha256`.
- Candidate fails `--validate-existing`.
- Intraday / rolling promotion (out of scope per DEC-002).
- Research sidecar only — export candidate not assembled.
- Operator has not recorded backup/recovery path.

---

## Pitch-type semantics (production honesty)

- **SP pitch mix** = pitcher-ID filtered repertoire for today's starter.
- **Hitter pitch-type rates** = batter + pitch type (not filtered to opposing SP).
- UI copy must not imply pitcher-specific hitter filtering unless export proves it.

## Known post-production items (not blockers)

- Shared `tab=` query key between Research and Leaderboards routes.
- `/today` tab state not URL-persistent (refresh returns Overview).

## Protected evidence

Do not modify or stage `evidence/**/*.raw.json`. Metadata under `evidence/`
may be committed when explicitly authorized.
