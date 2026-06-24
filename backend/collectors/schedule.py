import sqlite3
from pathlib import Path
from datetime import date
import requests

DB = Path("database/mlb_lab.db")

def ensure_table():
    conn = sqlite3.connect(DB)
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
    target_date = target_date or date.today().strftime("%Y-%m-%d")

    url = (
        "https://statsapi.mlb.com/api/v1/schedule"
        f"?sportId=1&date={target_date}&hydrate=probablePitcher,venue"
    )

    r = requests.get(url, timeout=20)
    r.raise_for_status()
    data = r.json()

    conn = sqlite3.connect(DB)
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
    return count

if __name__ == "__main__":
    n = collect_schedule()
    print(f"✅ Stored {n} games")
