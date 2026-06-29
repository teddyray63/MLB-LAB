from fastapi import APIRouter

from backend.database.database import get_connection

router = APIRouter()


@router.get("/statcast/hitters")
def hitters():
    conn = get_connection()
    try:
        rows = conn.execute("""
            SELECT *
            FROM statcast_hitters
            ORDER BY hard_hit_pct DESC
        """).fetchall()
    finally:
        conn.close()
    return [dict(r) for r in rows]


@router.get("/statcast/pitchers")
def pitchers():
    conn = get_connection()
    try:
        rows = conn.execute("""
            SELECT *
            FROM statcast_pitchers
            ORDER BY whiff_pct DESC
        """).fetchall()
    finally:
        conn.close()
    return [dict(r) for r in rows]


@router.get("/park-factors")
def park_factors():
    conn = get_connection()
    try:
        rows = conn.execute("""
            SELECT *
            FROM park_factors
            ORDER BY venue
        """).fetchall()
    finally:
        conn.close()
    return [dict(r) for r in rows]