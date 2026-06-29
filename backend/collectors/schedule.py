import logging
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from datetime import date
import requests

from backend.database.database import get_connection
from backend.utils import get_run_date

logger = logging.getLogger(__name__)

def ensure_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS games (
        game_pk INTEGER PRIMARY KEY,
        game_date TEXT,
        away_team TEXT,
        home_team TEXT,
        venue TEXT,
        start_time_utc TEXT,
        status TEXT,
        away_probable TEXT,
        home_probable TEXT
    )
    """)
    conn.commit()
    conn.close()

def collect_schedule(target_date=None):
    ensure_table()
    target_date = target_date or get_run_date()
    logger.info("collect_schedule: run_date=%s", target_date)

    url = (
        "https://statsapi.mlb.com/api/v1/schedule"
        f"?sportId=1&date={target_date}&hydrate=probablePitcher,venue"
    )

    r = requests.get(url, timeout=20)
    r.raise_for_status()
    data = r.json()

    conn = get_connection()
    cur = conn.cursor()
    count = 0

    for d in data.get("dates", []):
        for g in d.get("games", []):
            cur.execute("""
            INSERT OR REPLACE INTO games
            VALUES (?,?,?,?,?,?,?,?,?)
            """, (
                g.get("gamePk"),
                target_date,
                g["teams"]["away"]["team"]["name"],
                g["teams"]["home"]["team"]["name"],
                g.get("venue", {}).get("name", ""),
                g.get("gameDate", ""),
                g.get("status", {}).get("detailedState", ""),
                g["teams"]["away"].get("probablePitcher", {}).get("fullName", ""),
                g["teams"]["home"].get("probablePitcher", {}).get("fullName", "")
            ))
            count += 1

    conn.commit()
    conn.close()
    logger.info("collect_schedule: stored %d games for %s", count, target_date)
    return count

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    n = collect_schedule()
    logger.info("Done: %d games", n)
