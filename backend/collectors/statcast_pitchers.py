import logging
from datetime import datetime, timezone
import pandas as pd
from pybaseball import statcast_pitcher_exitvelo_barrels

from backend.database.database import get_connection

logger = logging.getLogger(__name__)

def collect_statcast_pitchers():
    year = datetime.now().year
    logger.info("Downloading Statcast pitchers (%d)...", year)

    df = statcast_pitcher_exitvelo_barrels(year)

    conn = get_connection()
    cur = conn.cursor()

    loaded = 0
    now = datetime.now(timezone.utc).isoformat()

    for _, r in df.iterrows():
        pid = r.get("player_id")
        if pd.isna(pid):
            continue

        cur.execute("""
        INSERT OR REPLACE INTO statcast_pitchers
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (
            int(pid),
            str(r.get("last_name, first_name", "")),
            str(r.get("team_name_alt", "")),
            int(r.get("attempts", 0) or 0),
            float(r.get("avg_hit_speed", 0) or 0),
            float(r.get("max_hit_speed", 0) or 0),
            float(r.get("whiff_percent", 0) or 0),
            float(r.get("hard_hit_percent", 0) or 0),
            float(r.get("xwoba", 0) or 0),
            now
        ))

        loaded += 1

    conn.commit()
    conn.close()
    logger.info("Loaded %d pitchers", loaded)

if __name__ == "__main__":
    collect_statcast_pitchers()
    