import logging

from backend.database.database import get_connection

logger = logging.getLogger(__name__)

def ensure_warehouse_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS player_master (
        player_id INTEGER PRIMARY KEY,
        player_name TEXT,
        team TEXT,
        bats TEXT,
        throws TEXT,
        updated_at TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS hitter_features (
        player_id INTEGER PRIMARY KEY,
        player_name TEXT,
        team TEXT,
        avg_ev REAL,
        max_ev REAL,
        barrel_pct REAL,
        hard_hit_pct REAL,
        xba REAL,
        xslg REAL,
        xwoba REAL,
        iso REAL,
        woba REAL,
        k_pct REAL,
        bb_pct REAL,
        research_score REAL,
        updated_at TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS matchup_features (
        game_pk INTEGER,
        player_id INTEGER,
        player_name TEXT,
        team TEXT,
        opponent TEXT,
        pitcher_name TEXT,
        venue TEXT,
        park_factor REAL,
        pitch_matchup_score REAL,
        recent_form_score REAL,
        contact_score REAL,
        power_score REAL,
        singles_score REAL,
        doubles_score REAL,
        total_bases_score REAL,
        runs_score REAL,
        rbi_score REAL,
        lotto_score REAL,
        updated_at TEXT
    )
    """)

    conn.commit()
    conn.close()
    logger.info("Warehouse tables ready")

if __name__ == "__main__":
    ensure_warehouse_tables()
    