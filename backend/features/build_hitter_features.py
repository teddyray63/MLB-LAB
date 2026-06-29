import logging
from datetime import datetime, UTC

from backend.database.database import get_connection

logger = logging.getLogger(__name__)

def nz(v):
    return 0 if v is None else v

def build_hitter_features():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    now = datetime.now(UTC).isoformat()

    hitters = cur.execute("""
        SELECT *
        FROM statcast_hitters
    """).fetchall()

    loaded = 0

    for h in hitters:
        research_score = (
            nz(h["avg_ev"]) * 0.30 +
            nz(h["max_ev"]) * 0.20 +
            nz(h["barrel_pct"]) * 1.50 +
            nz(h["hard_hit_pct"]) * 1.00 +
            nz(h["xslg"]) * 20 +
            nz(h["xwoba"]) * 20 +
            nz(h["xba"]) * 20
        )

        cur.execute("""
            INSERT OR REPLACE INTO hitter_features (
                player_id, player_name, team,
                avg_ev, max_ev, barrel_pct, hard_hit_pct,
                xba, xslg, xwoba,
                research_score, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            h["player_id"],
            h["player_name"],
            h["team"],
            nz(h["avg_ev"]),
            nz(h["max_ev"]),
            nz(h["barrel_pct"]),
            nz(h["hard_hit_pct"]),
            nz(h["xba"]),
            nz(h["xslg"]),
            nz(h["xwoba"]),
            round(research_score, 2),
            now
        ))

        loaded += 1

    conn.commit()
    conn.close()
    logger.info("Built hitter_features: %d hitters", loaded)

if __name__ == "__main__":
    build_hitter_features()