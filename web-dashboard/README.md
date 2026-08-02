# MLB-LAB Web Dashboard

Research-only dashboard. **Single data source:** `data/daily_export.json` from the Python runner.

## Data flow

```
scripts/mlb_lab_runner.py  →  data/daily_export.json  →  web-dashboard/public/data/  →  fetch /data/daily_export.json
```

- **Source of truth:** repo root `data/daily_export.json`
- **Dev/build:** `npm run sync-data` copies into `public/data/` (runs automatically before `dev` and `build`)
- **Fallback:** Vite dev middleware also serves `../data/daily_export.json` if the copy is missing

## Run

```bash
# 1. Generate export (repo root)
python3 scripts/mlb_lab_runner.py

# 2. Dashboard
cd web-dashboard
npm install
npm run dev
```

Open http://localhost:5173 — Command Center renders `top_plays` for all five categories from the real JSON.

Click **Reload** after re-running the Python export (or run `npm run sync-data` then reload).

## JSON schema (Command Center)

Uses `top_plays.{hits,singles,total_bases,hrr,home_runs}` — 5 rows each:

`rank`, `hitter`, `team`, `game`, `opp_sp`, `pitch`, `score`, `tier`, `key_stat`, `key_val`

Tiers: **T1** green · **T2** yellow · **T3** orange

## Next views (same file)

- Category Boards → `category_boards` (20 rows per category)
- Game Hub → per-game detail (not in JSON yet)
- Player Matchup Card → filter `matchups` by hitter
