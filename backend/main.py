import logging

from fastapi import FastAPI, HTTPException
from backend.api.statcast import router as statcast_router

from backend.database.database import get_connection

logger = logging.getLogger(__name__)

app = FastAPI(title="MLB-LAB API")

app.include_router(statcast_router)

@app.get("/")
def root():
    return {"status": "MLB-LAB backend running"}

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/games")
def games():
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
