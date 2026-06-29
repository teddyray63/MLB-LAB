from datetime import datetime, UTC

from backend.database.database import get_connection

def nz(v):
    return 0 if v is None else v

def build_daily_scores():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    now = datetime.now(UTC).isoformat()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS daily_scores (
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
        singles_score REAL,
        doubles_score REAL,
        total_bases_score REAL,
        runs_score REAL,
        rbi_score REAL,
        lotto_score REAL,
        updated_at TEXT
    )
    """)

    hitters = cur.execute("SELECT * FROM hitter_features").fetchall()

    for h in hitters:
        xba = nz(h["xba"])
        xslg = nz(h["xslg"])
        xwoba = nz(h["xwoba"])
        avg_ev = nz(h["avg_ev"])
        max_ev = nz(h["max_ev"])
        barrel = nz(h["barrel_pct"])
        hard = nz(h["hard_hit_pct"])

        singles = (xba * 60) + (xwoba * 25) + (avg_ev * .10) + (hard * .25)
        doubles = (xslg * 50) + (barrel * 2.0) + (hard * .60) + (avg_ev * .20)
        total_bases = (xslg * 65) + (barrel * 2.5) + (max_ev * .12) + (hard * .50)
        runs = (xwoba * 50) + (xba * 20) + (avg_ev * .10)
        rbi = (xslg * 45) + (barrel * 2.0) + (max_ev * .10)
        lotto = (doubles + total_bases + rbi) / 3

        cur.execute("""
        INSERT OR REPLACE INTO daily_scores (
            player_id, player_name, team,
            avg_ev, max_ev, barrel_pct, hard_hit_pct,
            xba, xslg, xwoba,
            singles_score, doubles_score, total_bases_score,
            runs_score, rbi_score, lotto_score, updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            h["player_id"], h["player_name"], h["team"],
            avg_ev, max_ev, barrel, hard,
            xba, xslg, xwoba,
            round(singles, 2), round(doubles, 2), round(total_bases, 2),
            round(runs, 2), round(rbi, 2), round(lotto, 2), now
        ))

    conn.commit()
    conn.close()
    print(f"✅ Built daily_scores: {len(hitters)} hitters")

if __name__ == "__main__":
    build_daily_scores()