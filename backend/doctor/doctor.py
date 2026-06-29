import importlib
from pathlib import Path
from typing import Any, Dict, List, Tuple

import pandas as pd

from backend.database.database import DB_PATH, get_connection

ROOT = Path(__file__).resolve().parent.parent.parent
EXPORT_DIR = ROOT / "exports"

REQUIRED_TABLES = ["games", "lineups", "park_factors", "statcast_hitters", "statcast_pitchers", "hitter_features", "daily_scores"]
REQUIRED_COLUMNS = {
    "games": ["game_pk", "game_date", "away_team", "home_team", "venue"],
    "lineups": ["game_pk", "team", "player_name"],
    "daily_scores": ["player_name", "team", "singles_score", "total_bases_score", "runs_score", "rbi_score", "lotto_score"],
}
REQUIRED_EXPORTS = [
    "exports/command_center.csv",
    "exports/singles.csv",
    "exports/total_bases.csv",
    "exports/runs.csv",
    "exports/rbis.csv",
    "exports/lotto.csv",
    "exports/cards.csv",
    "exports/value_edges.csv",
    "exports/daily_report.pdf",
    "exports/daily_report.html",
    "exports/betting_cards.txt",
    "exports/betting_cards.csv",
]


def check_imports() -> List[str]:
    missing = []
    for module_name in ["pandas", "sqlite3"]:
        try:
            importlib.import_module(module_name)
        except Exception as exc:  # pragma: no cover
            missing.append(f"{module_name}: {exc}")
    return missing


def run_doctor() -> Dict[str, Any]:
    issues: List[str] = []
    warnings: List[str] = []
    counts: Dict[str, int] = {}

    if not DB_PATH.exists():
        issues.append(f"Database missing: {DB_PATH}")
    else:
        conn = get_connection()
        try:
            tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
            available = set(tables["name"].tolist())
            for table in REQUIRED_TABLES:
                if table not in available:
                    issues.append(f"Missing table: {table}")
                    continue
                df = pd.read_sql(f"SELECT * FROM {table}", conn)
                counts[table] = len(df)
                if df.empty:
                    issues.append(f"Empty table: {table}")
                missing_cols = [col for col in REQUIRED_COLUMNS.get(table, []) if col not in df.columns]
                if missing_cols:
                    issues.append(f"Missing columns in {table}: {missing_cols}")
            if "games" in available:
                games = pd.read_sql("SELECT * FROM games", conn)
                if games.empty:
                    issues.append("No games found in games table")
                else:
                    today = pd.Timestamp.today().strftime("%Y-%m-%d")
                    if "game_date" in games.columns and games[games["game_date"].astype(str) == today].empty:
                        warnings.append("No games found for today's date")
            if "lineups" in available:
                lineups = pd.read_sql("SELECT * FROM lineups", conn)
                if lineups.empty:
                    issues.append("No lineups found in lineups table")
                else:
                    dupes = lineups[lineups.duplicated(subset=["game_pk", "player_name", "team"], keep=False)]
                    if not dupes.empty:
                        warnings.append("Duplicate lineup rows detected")
            if "daily_scores" in available:
                scores = pd.read_sql("SELECT * FROM daily_scores", conn)
                if scores.empty:
                    issues.append("No daily_scores rows found")
            conn.close()
        except Exception as exc:  # pragma: no cover
            issues.append(f"Database inspection failed: {exc}")

    for export_path in REQUIRED_EXPORTS:
        full_path = ROOT / export_path
        if not full_path.exists():
            issues.append(f"Missing export: {export_path}")

    missing_imports = check_imports()
    if missing_imports:
        issues.extend([f"Import issue: {item}" for item in missing_imports])

    odds_path = ROOT / "exports" / "odds.csv"
    if not odds_path.exists():
        warnings.append("Odds file not found; report will be model-only")

    return {"issues": issues, "warnings": warnings, "counts": counts, "exports": REQUIRED_EXPORTS}
