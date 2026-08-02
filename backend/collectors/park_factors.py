"""Park factor seed data and SQLite persistence helpers."""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB = Path("database/mlb_lab.db")

PARKS: tuple[tuple[str, int, int, int], ...] = (
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
)


def _db_path(db_path: Path | str | None = None) -> Path:
    return Path(db_path) if db_path is not None else DEFAULT_DB


def ensure_park_factors_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS park_factors (
            venue TEXT PRIMARY KEY,
            run_factor INTEGER,
            hit_factor INTEGER,
            hr_factor INTEGER,
            collected_at TEXT
        )
        """
    )


def load_park_factors(db_path: Path | str | None = None) -> int:
    """Seed park factors into the database. Safe to call explicitly from collectors/CLI."""
    path = _db_path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()

    conn = sqlite3.connect(path)
    try:
        ensure_park_factors_table(conn)
        for venue, run_factor, hit_factor, hr_factor in PARKS:
            conn.execute(
                """
                INSERT OR REPLACE INTO park_factors
                VALUES (?, ?, ?, ?, ?)
                """,
                (venue, run_factor, hit_factor, hr_factor, now),
            )
        conn.commit()
    finally:
        conn.close()

    return len(PARKS)


def lookup_park_factors(
    venue: str | None,
    db_path: Path | str | None = None,
) -> dict[str, int | None]:
    """Read park factors for a venue without writing to the database."""
    empty = {"run_factor": None, "hit_factor": None, "hr_factor": None}
    if not venue:
        return empty

    path = _db_path(db_path)
    if not path.exists():
        return empty

    conn = sqlite3.connect(path)
    try:
        row = conn.execute(
            """
            SELECT run_factor, hit_factor, hr_factor
            FROM park_factors
            WHERE venue = ?
            """,
            (venue,),
        ).fetchone()
    finally:
        conn.close()

    if row is None:
        return empty

    return {
        "run_factor": row[0],
        "hit_factor": row[1],
        "hr_factor": row[2],
    }


def list_park_factors(db_path: Path | str | None = None) -> list[dict[str, object]]:
    """Return all park factor rows ordered by venue."""
    path = _db_path(db_path)
    if not path.exists():
        return []

    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            """
            SELECT venue, run_factor, hit_factor, hr_factor, collected_at
            FROM park_factors
            ORDER BY venue
            """
        ).fetchall()
    finally:
        conn.close()

    return [dict(row) for row in rows]


if __name__ == "__main__":
    count = load_park_factors()
    print(f"✅ Loaded {count} park factors")
