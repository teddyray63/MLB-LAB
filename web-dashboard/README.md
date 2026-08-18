# MLB-LAB Web Dashboard

Research-only dashboard. **Single data source:** promoted `data/daily_export.json` from the G0b export pipeline.

## Data flow

```
scripts/build_daily_export.py  →  data/daily_export.json  →  web-dashboard/public/data/  →  fetch /data/daily_export.json
```

- **Source of truth:** repo root `data/daily_export.json` (gitignored; built and promoted locally)
- **Canonical builder:** `scripts/build_daily_export.py` — see `docs/DEPLOYMENT.md` for validation, promotion, and deploy injection
- **Dev/build:** `npm run sync-data` copies into `public/data/` (runs automatically before `dev` and `build`)
- **Fallback:** Vite dev middleware also serves `../data/daily_export.json` if the copy is missing

## Run

```bash
# 1. Build or promote export (repo root)
python3 scripts/build_daily_export.py --help
# See docs/DEPLOYMENT.md for promotion and SHA-pinned deploy flow.

# 2. Dashboard
cd web-dashboard
npm install
npm run dev
```

Open http://localhost:5173 — canonical routes include `/today`, `/research`, and `/leaderboards`.

Click **Reload** after updating the promoted export (or run `npm run sync-data` then reload).

## JSON schema

Primary export sections consumed by the dashboard include `games`, `matchups`, `game_details`, `player_logs`, `top_plays`, and `category_boards`. See `web-dashboard/src/types/slate.ts` and `scripts/build_daily_export.py` for the G0b contract.

Legacy pages under `/legacy/*` remain available per DEC-001.
