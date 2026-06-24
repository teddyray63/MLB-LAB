from fastapi import APIRouter
import sqlite3

router = APIRouter()

DB = "database/mlb_lab.db"


@router.get("/statcast/hitters")
def hitters():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT *
        FROM statcast_hitters
        ORDER BY hard_hit_pct DESC
    """).fetchall()

    conn.close()
    return [dict(r) for r in rows]


@router.get("/statcast/pitchers")
def pitchers():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT *
        FROM statcast_pitchers
        ORDER BY whiff_pct DESC
    """).fetchall()

    conn.close()
    return [dict(r) for r in rows]