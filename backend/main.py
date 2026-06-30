import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from backend.api.statcast import router as statcast_router

from backend.database.database import get_connection

logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
EXPORTS_DIR = ROOT / "exports"
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

_NO_REPORT_HTML = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>MLB-LAB</title>
<style>body{font-family:system-ui,sans-serif;background:#07111f;color:#f5f7fb;display:flex;align-items:center;justify-content:center;min-height:100vh;margin:0;}
.box{text-align:center;padding:40px;border:1px solid rgba(255,255,255,0.1);border-radius:16px;background:#101b2d;}
h1{margin:0 0 12px;font-size:1.6rem;}p{color:#94a3b8;margin:0 0 20px;}
a{color:#4fd1c5;text-decoration:none;}a:hover{text-decoration:underline;}</style>
</head><body><div class="box">
<h1>MLB-LAB</h1>
<p>No daily report has been generated yet.<br>Run <code>python backend/command_center.py</code> to produce today's cards.</p>
<p><a href="/docs">API docs →</a></p>
</div></body></html>"""

app = FastAPI(title="MLB-LAB API", description="Baseball intelligence & betting card engine.")

app.include_router(statcast_router)
app.mount("/exports", StaticFiles(directory=str(EXPORTS_DIR), html=False), name="exports")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def root():
    """Serve the daily dashboard, or a friendly placeholder when not yet generated."""
    dashboard = EXPORTS_DIR / "daily_dashboard.html"
    if dashboard.exists():
        return FileResponse(str(dashboard), media_type="text/html")
    return HTMLResponse(_NO_REPORT_HTML)


@app.get("/health")
def health():
    """Health probe for load balancers and Render."""
    return {"ok": True}


@app.get("/dashboard", response_class=HTMLResponse, include_in_schema=False)
def dashboard():
    """Explicit route for the HTML betting dashboard."""
    path = EXPORTS_DIR / "daily_dashboard.html"
    if not path.exists():
        return HTMLResponse(_NO_REPORT_HTML, status_code=200)
    return FileResponse(str(path), media_type="text/html")


@app.get("/report")
def report():
    """Return the latest daily_report.json summary, or an empty structure."""
    import json
    path = EXPORTS_DIR / "daily_report.json"
    if not path.exists():
        return {"warnings": [], "issues": ["No report generated yet"], "games": 0, "cards": []}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        logger.exception("Failed to read daily_report.json")
        raise HTTPException(status_code=500, detail="Failed to read report")


@app.get("/cards")
def cards():
    """Return the latest betting cards CSV rows as JSON, or empty list."""
    import csv, io
    path = EXPORTS_DIR / "command_center.csv"
    if not path.exists():
        return []
    try:
        reader = csv.DictReader(io.StringIO(path.read_text(encoding="utf-8")))
        return list(reader)
    except Exception:
        logger.exception("Failed to read command_center.csv")
        raise HTTPException(status_code=500, detail="Failed to read cards")

@app.get("/games")
def games():
    """Return all scheduled games ordered by start time."""
    try:
        conn = get_connection()
        try:
            rows = conn.execute("""
            SELECT game_pk, game_date, away_team, home_team, venue,
                   start_time_utc, status, away_probable, home_probable
            FROM games
            ORDER BY start_time_utc
            """).fetchall()
        finally:
            conn.close()
    except Exception:
        logger.exception("Failed to fetch games")
        raise HTTPException(status_code=500, detail="Failed to fetch games")
    return [dict(r) for r in rows]


@app.get("/lineups")
def lineups():
    """Return all lineup entries across all games."""
    try:
        conn = get_connection()
        try:
            rows = conn.execute("""
            SELECT game_pk, team, batting_order, player_id,
                   player_name, bats, position, confirmed
            FROM lineups
            ORDER BY game_pk, team, batting_order
            """).fetchall()
        finally:
            conn.close()
    except Exception:
        logger.exception("Failed to fetch lineups")
        raise HTTPException(status_code=500, detail="Failed to fetch lineups")
    return [dict(r) for r in rows]


@app.get("/game/{game_pk}/lineups")
def game_lineups(game_pk: int):
    """Return lineup for a specific game. Raises 404 if game_pk is unknown."""
    try:
        conn = get_connection()
        try:
            rows = conn.execute("""
            SELECT team, batting_order, player_name, bats, position, confirmed
            FROM lineups
            WHERE game_pk = ?
            ORDER BY team, batting_order
            """, (game_pk,)).fetchall()
        finally:
            conn.close()
    except Exception:
        logger.exception("Failed to fetch lineups for game_pk=%d", game_pk)
        raise HTTPException(status_code=500, detail="Failed to fetch lineups")
    if not rows:
        raise HTTPException(status_code=404, detail=f"Game {game_pk} not found")
    return [dict(r) for r in rows]
