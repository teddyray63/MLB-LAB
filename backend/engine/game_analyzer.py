from datetime import date
from typing import Any, Dict, List, Tuple

import pandas as pd

from backend.database.database import DB_PATH, get_connection


def normalize_name(name: Any) -> str:
    if not isinstance(name, str):
        return ""
    name = name.strip()
    if "," in name:
        last, first = [x.strip() for x in name.split(",", 1)]
        return f"{first} {last}".lower()
    return name.lower()


def load_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, List[str]]:
    warnings: List[str] = []
    if not DB_PATH.exists():
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), ["Database missing: database/mlb_lab.db"]

    conn = get_connection()
    try:
        games = pd.read_sql("SELECT * FROM games", conn)
        lineups = pd.read_sql("SELECT * FROM lineups", conn)
        scores = pd.read_sql("SELECT * FROM daily_scores", conn)
    finally:
        conn.close()

    if games.empty:
        warnings.append("No games found in games table")
    if lineups.empty:
        warnings.append("No lineups found in lineups table")
    if scores.empty:
        warnings.append("No daily_scores rows found")

    return games, lineups, scores, warnings


def validate_slate(games: pd.DataFrame, lineups: pd.DataFrame, scores: pd.DataFrame) -> Dict[str, Any]:
    today = date.today().strftime("%Y-%m-%d")
    warnings: List[str] = []
    issues: List[str] = []

    if games.empty:
        issues.append("games table empty")
        return {"today_games": [], "warnings": warnings, "issues": issues, "slate_ok": False}

    games_copy = games.copy()
    if "game_date" in games_copy.columns:
        games_copy["game_date"] = games_copy["game_date"].astype(str)
        today_games = games_copy[games_copy["game_date"] == today]
        if today_games.empty:
            warnings.append("No games found for today's date")
            today_games = games_copy.head(8)
    else:
        today_games = games_copy.head(8)

    if lineups.empty:
        issues.append("lineups table empty")
    else:
        today_game_ids = set(today_games["game_pk"].dropna().astype(int).tolist()) if "game_pk" in today_games.columns else set()
        lineup_game_ids = set(lineups["game_pk"].dropna().astype(int).tolist()) if "game_pk" in lineups.columns else set()
        missing_lineups = sorted(today_game_ids - lineup_game_ids)
        if missing_lineups:
            warnings.append(f"Missing lineups for game ids: {missing_lineups}")

        if "player_name" in lineups.columns:
            duplicates = lineups[lineups.duplicated(subset=["game_pk", "player_name", "team"], keep=False)]
            if not duplicates.empty:
                warnings.append(f"Duplicate lineup rows detected: {len(duplicates)}")

    if scores.empty:
        issues.append("daily_scores table empty")

    lineup_player_names = set(normalize_name(x) for x in lineups["player_name"].tolist()) if not lineups.empty and "player_name" in lineups.columns else set()
    score_player_names = set(normalize_name(x) for x in scores["player_name"].tolist()) if not scores.empty and "player_name" in scores.columns else set()
    unmatched = sorted(score_player_names - lineup_player_names)[:10]
    if unmatched:
        warnings.append(f"Players in scores without lineup match: {unmatched}")

    return {
        "today_games": today_games.to_dict("records"),
        "warnings": warnings,
        "issues": issues,
        "slate_ok": not issues,
    }
