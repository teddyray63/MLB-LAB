import sqlite3
import pandas as pd
from pathlib import Path

DB = Path("database/mlb_lab.db")

REQUIRED_TABLES = [
    "games",
    "lineups",
    "park_factors",
    "statcast_hitters",
    "statcast_pitchers",
    "hitter_features",
    "daily_scores",
]

def check_table(conn, table):
    print(f"\n--- {table} ---")
    try:
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        print(f"rows: {len(df)}")
        print(f"cols: {list(df.columns)}")
        if len(df):
            print(df.head(3).to_string(index=False))
        return df
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def main():
    print("\n================ MLB-LAB DOCTOR ================\n")

    if not DB.exists():
        print(f"❌ Database missing: {DB}")
        return

    print(f"✅ Database found: {DB}")

    conn = sqlite3.connect(DB)

    dfs = {}
    for table in REQUIRED_TABLES:
        dfs[table] = check_table(conn, table)

    print("\n================ KEY DIAGNOSIS ================\n")

    for table, df in dfs.items():
        if df is None:
            print(f"❌ {table}: missing table")
        elif df.empty:
            print(f"⚠️ {table}: empty")
        else:
            print(f"✅ {table}: {len(df)} rows")

    if dfs.get("daily_scores") is not None and not dfs["daily_scores"].empty:
        df = dfs["daily_scores"]
        score_cols = [c for c in df.columns if "score" in c]
        print("\nScore columns:", score_cols)

        print("\nTOP DAILY SCORES:")
        sort_col = "lotto_score" if "lotto_score" in df.columns else score_cols[0]
        print(df.sort_values(sort_col, ascending=False).head(10).to_string(index=False))

    conn.close()

    print("\n================ NEXT ACTION ================")

    if dfs.get("games") is None or dfs["games"].empty:
        print("Run/fix schedule collector.")
    elif dfs.get("lineups") is None or dfs["lineups"].empty:
        print("Run/fix lineups collector.")
    elif dfs.get("statcast_hitters") is None or dfs["statcast_hitters"].empty:
        print("Run/fix Statcast hitters collector.")
    elif dfs.get("hitter_features") is None or dfs["hitter_features"].empty:
        print("Run/fix build_hitter_features.py.")
    elif dfs.get("daily_scores") is None or dfs["daily_scores"].empty:
        print("Run/fix build_daily_scores.py.")
    else:
        print("✅ Data pipeline healthy. Ready to generate report_today.py.")

if __name__ == "__main__":
    main()
    