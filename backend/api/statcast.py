import logging

from fastapi import APIRouter, HTTPException

from backend.database.database import get_connection

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/statcast/hitters")
def hitters():
    try:
        conn = get_connection()
        try:
            rows = conn.execute("""
                SELECT *
                FROM statcast_hitters
                ORDER BY hard_hit_pct DESC
            """).fetchall()
        finally:
            conn.close()
    except Exception:
        logger.exception("Failed to fetch statcast hitters")
        raise HTTPException(status_code=500, detail="Failed to fetch statcast hitters")
    return [dict(r) for r in rows]


@router.get("/statcast/pitchers")
def pitchers():
    try:
        conn = get_connection()
        try:
            rows = conn.execute("""
                SELECT *
                FROM statcast_pitchers
                ORDER BY whiff_pct DESC
            """).fetchall()
        finally:
            conn.close()
    except Exception:
        logger.exception("Failed to fetch statcast pitchers")
        raise HTTPException(status_code=500, detail="Failed to fetch statcast pitchers")
    return [dict(r) for r in rows]


@router.get("/park-factors")
def park_factors():
    try:
        conn = get_connection()
        try:
            rows = conn.execute("""
                SELECT *
                FROM park_factors
                ORDER BY venue
            """).fetchall()
        finally:
            conn.close()
    except Exception:
        logger.exception("Failed to fetch park factors")
        raise HTTPException(status_code=500, detail="Failed to fetch park factors")
    return [dict(r) for r in rows]