import logging
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import requests

logger = logging.getLogger(__name__)

from backend.database.database import get_connection

conn = get_connection()
cur = conn.cursor()

games = cur.execute("""
SELECT game_pk,away_team,home_team
FROM games
""").fetchall()

logger.info("Checking %d games...", len(games))

loaded = 0

for game_pk, away, home in games:

    url = f"https://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live"

    try:
        r = requests.get(url, timeout=20)
        data = r.json()

        for side in ["away", "home"]:

            team = data["gameData"]["teams"][side]["name"]

            lineup = data["liveData"]["boxscore"]["teams"][side].get("battingOrder", [])

            players = data["liveData"]["boxscore"]["teams"][side]["players"]

            confirmed = 1 if lineup else 0

            for spot, pid in enumerate(lineup, start=1):

                p = players["ID" + str(pid)]

                cur.execute("""
                INSERT OR REPLACE INTO lineups
                VALUES (?,?,?,?,?,?,?,?)
                """,(
                    game_pk,
                    team,
                    spot,
                    int(pid),
                    p["person"]["fullName"],
                    p.get("batSide",{}).get("code",""),
                    p.get("position",{}).get("abbreviation",""),
                    confirmed
                ))

                loaded += 1

    except Exception as e:
        logger.exception("Error loading lineups for game_pk=%s", game_pk)

conn.commit()
conn.close()

logger.info("Loaded %d lineup rows", loaded)
