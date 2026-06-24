import sqlite3

conn = sqlite3.connect("database/mlb_lab.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS statcast_hitters (
    player_id INTEGER PRIMARY KEY,
    player_name TEXT,
    team TEXT,
    pa INTEGER,
    avg_ev REAL,
    max_ev REAL,
    barrel_pct REAL,
    hard_hit_pct REAL,
    xwoba REAL,
    xba REAL,
    xslg REAL,
    collected_at TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS statcast_pitchers (
    player_id INTEGER PRIMARY KEY,
    player_name TEXT,
    team TEXT,
    pitch_count INTEGER,
    avg_velo REAL,
    max_velo REAL,
    whiff_pct REAL,
    hard_hit_pct REAL,
    xwoba REAL,
    collected_at TEXT
)
""")

conn.commit()
conn.close()

print("✅ Statcast tables ready")
