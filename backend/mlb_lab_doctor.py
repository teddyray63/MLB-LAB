import importlib
import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "database" / "mlb_lab.db"
EXPORT_DIR = ROOT / "exports"

REQUIRED_TABLES = [
    "games",
    "lineups",
    "park_factors",
    "statcast_hitters",
    "statcast_pitchers",
    "hitter_features",
    "daily_scores",
]

REQUIRED_COLUMNS = {
    "games": ["game_pk", "game_date", "away_team", "home_team", "venue"],
    "lineups": ["game_pk", "team", "player_name"],
    "daily_scores": ["player_name", "team", "singles_score", "total_bases_score", "runs_score", "rbi_score", "lotto_score"],
}

REQUIRED_EXPORTS = [
    "exports/daily_report.txt",
    "exports/daily_report.pdf",
    "exports/daily_report.csv",
    "exports/singles.csv",
    "exports/total_bases.csv",
    "exports/command_center.csv",
]


def check_imports():
    missing = []
    for module_name in ["pandas", "sqlite3"]:
        try:
            importlib.import_module(module_name)
        except Exception as exc:
            missing.append(f"{module_name}: {exc}")
    return missing


def check_table(conn, table):
    try:
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        return df
    except Exception as exc:
        return None, str(exc)


def main():
    print("\n================ MLB-LAB DOCTOR ================\n")
    issues = []

    if not DB_PATH.exists():
        issues.append(f"Database missing: {DB_PATH}")
        issues.append("Fix: restore the SQLite database file or rerun the collectors that populate it.")
    else:
        print(f"✅ Database found: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH) if DB_PATH.exists() else None

    if conn is not None:
        available_tables = set()
        try:
            tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
            available_tables = set(tables["name"].tolist())
        except Exception as exc:
            issues.append(f"Could not inspect sqlite schema: {exc}")

        for table in REQUIRED_TABLES:
            if table not in available_tables:
                issues.append(f"Missing table: {table}")
                issues.append(f"Fix: create or restore the {table} table before running the command center.")
                continue

            df = None
            error = None
            try:
                df = pd.read_sql(f"SELECT * FROM {table}", conn)
            except Exception as exc:
                error = str(exc)
            if df is None or error:
                issues.append(f"Could not read table {table}: {error}")
                continue

            if df.empty:
                issues.append(f"Empty table: {table}")
                issues.append(f"Fix: populate {table} with the latest data before generating a report.")
                continue

            required_cols = REQUIRED_COLUMNS.get(table, [])
            missing_cols = [col for col in required_cols if col not in df.columns]
            if missing_cols:
                issues.append(f"Missing columns in {table}: {missing_cols}")
                issues.append(f"Fix: verify the table schema and rebuild the relevant collector output.")

        if "games" in available_tables:
            games = pd.read_sql("SELECT * FROM games", conn)
            if games.empty:
                issues.append("No games found in the games table.")
                issues.append("Fix: restore or refresh the schedule data.")
            else:
                today = pd.Timestamp.today().strftime("%Y-%m-%d")
                if "game_date" in games.columns and not games[games["game_date"].astype(str) == today].empty:
                    print(f"✅ Today's games found for {today}")
                else:
                    issues.append("No games found for today's date in the games table.")
                    issues.append("Fix: refresh the schedule data or use the latest available games from the database.")

        if "lineups" in available_tables:
            lineups = pd.read_sql("SELECT * FROM lineups", conn)
            if lineups.empty:
                issues.append("No lineups found in the lineups table.")
                issues.append("Fix: restore or refresh the lineup data.")
            else:
                duplicate_players = lineups[lineups.duplicated(subset=["player_name", "game_pk"], keep=False)]
                if not duplicate_players.empty:
                    issues.append("Duplicate lineup rows detected for the same player and game.")
                    issues.append("Fix: remove duplicate lineup rows and rerun the lineup collector.")

        if "daily_scores" in available_tables:
            scores = pd.read_sql("SELECT * FROM daily_scores", conn)
            if scores.empty:
                issues.append("No daily score rows found.")
                issues.append("Fix: rebuild the daily score table before generating a report.")
            else:
                score_cols = [c for c in scores.columns if "score" in c]
                if not score_cols:
                    issues.append("The daily_scores table is missing score columns.")
                    issues.append("Fix: rebuild the daily score table from the existing feature tables.")

        conn.close()

    for path in REQUIRED_EXPORTS:
        export_path = ROOT / path
        if not export_path.exists():
            issues.append(f"Missing export: {path}")
            issues.append(f"Fix: rerun python3 backend/command_center.py to create {path}.")

    missing_imports = check_imports()
    if missing_imports:
        issues.append("Python import issues detected:")
        issues.extend([f"- {item}" for item in missing_imports])
        issues.append("Fix: install the missing Python packages in the active environment.")

    print("\n================ DIAGNOSIS ================\n")
    if issues:
        for item in issues:
            print(f"- {item}")
        print("\nSummary: issues detected. Fix the items above before relying on the report outputs.")
    else:
        print("✅ No issues detected. The pipeline should be ready for the command center export flow.")

    print("\n================ NEXT ACTION ================")
    if issues:
        print("Use the fixes above to resolve the failures one by one.")
    else:
        print("Everything looks healthy. Run python3 backend/command_center.py to regenerate the betting report exports.")


if __name__ == "__main__":
    main()
