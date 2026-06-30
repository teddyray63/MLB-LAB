# MLB-LAB

MLB-LAB is a baseball intelligence research repository that collects Statcast data, builds daily player scores, and generates graded betting card recommendations.

---

## Setup

**Requirements:** Python 3.11+

```bash
pip install -r requirements.txt
```

The SQLite database is created automatically at `database/mlb_lab.db` (override with the `MLB_LAB_DB_PATH` environment variable).

---

## Data Pipeline

Run once to initialize tables and load data:

```bash
python backend/collectors/init_statcast.py   # create Statcast tables
python backend/collectors/init_lineups.py    # create lineups table
python backend/collectors/schedule.py        # fetch today's schedule
python backend/collectors/statcast_hitters.py
python backend/collectors/statcast_pitchers.py
python backend/features/build_hitter_features.py
python backend/features/build_daily_scores.py
```

Or run all data steps at once:

```bash
python backend/build_all.py
```

---

## Daily Workflow

Generate betting cards and exports:

```bash
python backend/command_center.py
```

Exports are written to `exports/`. The HTML dashboard opens automatically.

---

## API Server

```bash
uvicorn backend.main:app --reload
```

| Endpoint | Description |
|---|---|
| `GET /games` | All scheduled games |
| `GET /lineups` | All lineup entries |
| `GET /game/{game_pk}/lineups` | Lineup for a specific game (404 if not found) |
| `GET /statcast/hitters` | Statcast hitter metrics |
| `GET /statcast/pitchers` | Statcast pitcher metrics |
| `GET /park-factors` | Park factor adjustments |

Interactive docs: `http://localhost:8000/docs`

---

## Tests

```bash
python -m pytest tests/ -x -q
```

---

## Render Deployment

MLB-LAB runs as a FastAPI web service on [Render](https://render.com). A `render.yaml` blueprint is included for one-click setup.

### Quick steps

1. Push the repo to GitHub and log in to Render.
2. **New → Blueprint** → point at your GitHub repo → Render reads `render.yaml` automatically.

   Or create a **Web Service** manually with these settings:

   | Setting | Value |
   |---|---|
   | **Runtime** | Python 3 |
   | **Build command** | `pip install -r requirements.txt` |
   | **Start command** | `uvicorn backend.main:app --host 0.0.0.0 --port $PORT` |
   | **Health check path** | `/health` |

3. Set environment variables in the Render dashboard (Settings → Environment):

   | Variable | Purpose | Example |
   |---|---|---|
   | `MLB_LAB_DB_PATH` | SQLite file path on the Render disk | `/opt/render/project/src/database/mlb_lab.db` |
   | `MLB_LAB_RUN_DATE` | Override today's date (optional) | `2026-06-29` — leave blank to use today |

4. After first deploy, the root URL (`/`) shows a "No report generated yet" page until you run the pipeline. Trigger via a GitHub Actions workflow or SSH/one-off job:
   ```bash
   python backend/command_center.py
   ```

### Live endpoints once deployed

| Endpoint | Description |
|---|---|
| `GET /` | Daily dashboard HTML (placeholder if no report yet) |
| `GET /dashboard` | Same as `/` |
| `GET /health` | Health probe (`{"ok": true}`) |
| `GET /report` | Latest `daily_report.json` summary |
| `GET /cards` | Latest `command_center.csv` rows as JSON |
| `GET /exports/{file}` | Raw file download from `exports/` directory |
| `GET /games` | All scheduled games from DB |
| `GET /lineups` | All lineup entries from DB |
| `GET /docs` | Interactive Swagger UI |

### Persistent storage note

Render free-tier web services have an ephemeral filesystem — exports and the database are lost on redeploy. For persistence, attach a **Render Disk** at `/opt/render/project/src` and set `MLB_LAB_DB_PATH` accordingly, or export to an external store (S3, Supabase) from your pipeline.

---

## GitHub Actions

Two workflows are included in `.github/workflows/`:

- **`daily-run.yml`** — runs on a cron schedule (12:00 UTC) and on `workflow_dispatch`. Executes `scripts/mlb_lab_runner.py`, then commits updated reports back to the repo.
- **`run-mlb-lab.yml`** — manual trigger for ad-hoc runs.

Trigger a manual run from the GitHub Actions tab → select the workflow → **Run workflow**.

---

## Repository Structure

| Path | Purpose |
|---|---|
| `backend/collectors/` | Data ingestion scripts (schedule, lineups, Statcast) |
| `backend/features/` | Feature engineering (hitter features, daily scores) |
| `backend/engine/` | Scoring, card building, confidence, warehouse |
| `backend/odds/` | Odds import, normalization, edge calculation |
| `backend/api/` | FastAPI routers |
| `backend/database/` | Centralized DB connection (`get_connection()`) |
| `backend/utils/` | Shared helpers (`normalize_name`, `nz`) |
| `exports/` | Generated CSVs and HTML reports |
| `tests/` | pytest test suite |

---

## Core Principle

Data is not the goal. Intelligence is the goal. Research is the bridge between the two.
