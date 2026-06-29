import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from datetime import datetime, timezone

from backend.database.database import get_connection

PARKS = [
    ("Rogers Centre", 102, 101, 105),
    ("PNC Park", 97, 99, 92),
    ("Tropicana Field", 96, 98, 91),
    ("loanDepot park", 91, 97, 84),
    ("Comerica Park", 101, 103, 94),
    ("Nationals Park", 99, 100, 101),
    ("Citi Field", 96, 98, 93),
    ("Great American Ball Park", 104, 101, 120),
    ("Target Field", 98, 99, 101),
    ("Rate Field", 101, 100, 106),
    ("Coors Field", 115, 111, 112),
    ("Angel Stadium", 98, 99, 96),
    ("Busch Stadium", 96, 98, 91),
    ("Oracle Park", 94, 97, 82),
    ("Petco Park", 95, 98, 89),
]

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS park_factors (
    venue TEXT PRIMARY KEY,
    run_factor INTEGER,
    hit_factor INTEGER,
    hr_factor INTEGER,
    collected_at TEXT
)
""")

now = datetime.now(timezone.utc).isoformat()

for park in PARKS:
    cur.execute("""
    INSERT OR REPLACE INTO park_factors
    VALUES (?,?,?,?,?)
    """, (*park, now))

conn.commit()
conn.close()

print(f"✅ Loaded {len(PARKS)} park factors")
