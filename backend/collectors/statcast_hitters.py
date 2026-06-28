import sqlite3
from datetime import datetime
import pandas as pd
from pybaseball import statcast_batter_exitvelo_barrels

DB = "database/mlb_lab.db"

def collect_statcast_hitters():
    year = datetime.now().year

    print(f"Downloading Statcast hitters ({year})...")

    df = statcast_batter_exitvelo_barrels(year)

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    loaded = 0
    now = datetime.utcnow().isoformat()

    for _, r in df.iterrows():

        pid = r.get("player_id")

        if pd.isna(pid):
            continue

        cur.execute("""
        cur.execute("""
        INSERT OR REPLACE INTO statcast_hitters
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            int(pid),
            str(r.get("last_name, first_name", "")),
            str(r.get("team_name_alt", "")),
            int(r.get("attempts", 0) or 0),
            float(r.get("avg_hit_speed", 0) or 0),
            float(r.get("max_hit_speed", 0) or 0),
            float(r.get("brl_percent", 0) or 0),
            float(r.get("hard_hit_percent", 0) or 0),
            float(r.get("xwoba", 0) or 0),
            float(r.get("xba", 0) or 0),
            float(r.get("xslg", 0) or 0),
            now
         ))