import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from backend.database.database import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS lineups (
    game_pk INTEGER,
    team TEXT,
    batting_order INTEGER,
    player_id INTEGER,
    player_name TEXT,
    bats TEXT,
    position TEXT,
    confirmed INTEGER DEFAULT 0,
    PRIMARY KEY(game_pk, team, batting_order)
)
""")

conn.commit()
conn.close()

print("✅ Lineups table ready")
