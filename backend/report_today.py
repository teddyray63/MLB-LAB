import logging
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

from backend.database.database import get_connection

def top(df, col, n=5):
    keep = ["player_name", "team", col, "avg_ev", "max_ev", "barrel_pct", "hard_hit_pct"]
    keep = [c for c in keep if c in df.columns]
    return df.sort_values(col, ascending=False)[keep].head(n)

conn = get_connection()

scores = pd.read_sql("SELECT * FROM daily_scores", conn)
lineups = pd.read_sql("SELECT * FROM lineups", conn)
games = pd.read_sql("SELECT * FROM games", conn)

conn.close()

logger.info("\n================ MLB-LAB DAILY REPORT ================\n")

for _, g in games.iterrows():
    away = g.get("away_team")
    home = g.get("home_team")
    venue = g.get("venue", "")

    game_teams = [away, home]
    game_scores = scores[scores["team"].isin(game_teams)].copy()

    if game_scores.empty:
        continue

    logger.info("\n\n### %s @ %s — %s", away, home, venue)
    logger.info("=" * 70)

    logger.info("\nTOP 5 SINGLES\n%s", top(game_scores, "singles_score").to_string(index=False))
    logger.info("\nTOP 5 TOTAL BASES\n%s", top(game_scores, "total_bases_score").to_string(index=False))

    singles = top(game_scores, "singles_score", 1)
    tb = top(game_scores, "total_bases_score", 1)
    logger.info("\nBEST 2-LEG CARD\n%s", pd.concat([singles, tb]).drop_duplicates("player_name").head(2).to_string(index=False))

    lotto_cols = ["singles_score", "doubles_score", "total_bases_score", "runs_score", "rbi_score", "lotto_score"]
    lotto_cols = [c for c in lotto_cols if c in game_scores.columns]
    logger.info("\nBEST 4-LEG LOTTO\n%s", game_scores.sort_values("lotto_score", ascending=False)[
        ["player_name", "team"] + lotto_cols
    ].head(4).to_string(index=False))

logger.info("\n================ END REPORT ================\n")
