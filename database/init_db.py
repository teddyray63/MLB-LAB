import sqlite3
from pathlib import Path

DB = Path("database/mlb_lab.db")
DB.parent.mkdir(exist_ok=True)

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

print("✅ Database ready:", DB)
