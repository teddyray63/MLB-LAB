import json
import sqlite3
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Tuple

from jinja2 import Template

import pandas as pd

from backend.engine.card_builder import build_market_cards
from backend.engine.confidence import edge_from_odds, grade_for_market
from backend.engine.exporter import export_json, export_csv, write_exports
from backend.engine.game_analyzer import load_data, validate_slate

ROOT = Path(__file__).resolve().parent.parent.parent
DB_PATH = ROOT / "database" / "mlb_lab.db"
CONFIG_PATH = ROOT / "backend" / "betting_config.json"
EXPORT_DIR = ROOT / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def load_config() -> Dict[str, Any]:
    defaults = {
        "minimum_confidence": 30.0,
        "minimum_edge": 7.0,
        "top_players_per_game": 5,
        "safe_card_legs": 2,
        "lotto_card_legs": 4,
        "allow_same_team_stacking": False,
        "export_paths": {
            "command_center": "exports/command_center.csv",
            "singles": "exports/singles.csv",
            "total_bases": "exports/total_bases.csv",
            "runs": "exports/runs.csv",
            "rbis": "exports/rbis.csv",
            "lotto": "exports/lotto.csv",
            "cards": "exports/cards.csv",
            "value_edges": "exports/value_edges.csv",
            "pdf": "exports/daily_report.pdf",
            "html": "exports/daily_report.html",
            "text": "exports/betting_cards.txt",
            "text_csv": "exports/betting_cards.csv",
        },
        "odds_path": "exports/odds.csv",
        "pdf_path": "exports/daily_report.pdf",
        "html_path": "exports/daily_report.html",
        "stale_data_threshold_days": 1,
    }
    if not CONFIG_PATH.exists():
        return defaults
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception:
        return defaults
    defaults.update(data)
    if isinstance(data.get("export_paths"), dict):
        defaults["export_paths"].update(data["export_paths"])
    return defaults


CONFIG = load_config()


def normalize_name(name: Any) -> str:
    if not isinstance(name, str):
        return ""
    name = name.strip()
    if "," in name:
        last, first = [x.strip() for x in name.split(",", 1)]
        return f"{first} {last}".lower()
    return name.lower()


def ensure_alignment(scores: pd.DataFrame, lineups: pd.DataFrame) -> pd.DataFrame:
    if scores.empty or lineups.empty:
        return scores
    work_scores = scores.copy()
    work_lineups = lineups.copy()
    work_scores["name_key"] = work_scores["player_name"].apply(normalize_name)
    work_lineups["name_key"] = work_lineups["player_name"].apply(normalize_name)
    lineup_map = work_lineups[["name_key", "team"]].drop_duplicates("name_key")
    merged = work_scores.drop(columns=["team"], errors="ignore").merge(lineup_map, on="name_key", how="left")
    merged["team"] = merged["team"].fillna("")
    return merged


def load_odds() -> pd.DataFrame:
    odds_path = ROOT / CONFIG.get("odds_path", "exports/odds.csv")
    if not odds_path.exists():
        return pd.DataFrame(columns=["player_name", "team", "market", "line", "odds", "book"])
    return pd.read_csv(odds_path)


def attach_odds(scores: pd.DataFrame, odds: pd.DataFrame) -> pd.DataFrame:
    if scores.empty:
        return scores
    if odds.empty:
        return scores.assign(odds_present=False, edge_score=0.0, value_flag=False, implied_probability=None)

    work_scores = scores.copy()
    work_scores["player_key"] = work_scores["player_name"].apply(normalize_name)
    odds["player_key"] = odds["player_name"].apply(normalize_name)
    merged = work_scores.merge(odds[["player_key", "market", "line", "odds", "book"]], on="player_key", how="left")
    merged["odds_present"] = merged["odds"].notna()
    edge_map = []
    for _, row in merged.iterrows():
        edge = edge_from_odds(row.get("singles_score", 0), row.get("line", None), row.get("odds", None))
        edge_map.append(edge)
    merged["edge_score"] = [entry["edge_score"] for entry in edge_map]
    merged["value_flag"] = [entry["value_flag"] for entry in edge_map]
    merged["implied_probability"] = [entry["implied_probability"] for entry in edge_map]
    return merged


def build_ranked_rows(game_df: pd.DataFrame, game_name: str, config: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    if game_df.empty:
        return rows

    for _, row in game_df.iterrows():
        market = "singles"
        score = float(row.get("singles_score", 0) or 0)
        grade = grade_for_market(score, market, config.get("minimum_confidence", 30.0))
        rows.append({
            "section": "game_card",
            "game": game_name,
            "player": row.get("player_name", ""),
            "team": row.get("team", ""),
            "market": market,
            "score": score,
            "grade": grade,
            "confidence": score,
            "edge": row.get("edge_score", 0.0),
            "risk_note": "monitor lineup status",
        })
    return rows


def build_daily_report() -> Dict[str, Any]:
    games, lineups, scores, initial_warnings = load_data()
    slate = validate_slate(games, lineups, scores)
    warnings = list(initial_warnings) + list(slate.get("warnings", []))
    issues = list(slate.get("issues", []))

    if games.empty or lineups.empty or scores.empty:
        return {"warnings": warnings, "issues": issues, "rows": [], "cards": []}

    aligned_scores = ensure_alignment(scores, lineups)
    odds = load_odds()
    scored = attach_odds(aligned_scores, odds)

    today_games = slate.get("today_games", [])
    game_cards: List[Dict[str, Any]] = []
    overall_rows: List[Dict[str, Any]] = []
    value_rows: List[Dict[str, Any]] = []

    for game in today_games:
        away = game.get("away_team", "")
        home = game.get("home_team", "")
        game_name = f"{away} @ {home}"
        game_df = scored[scored["team"].isin([away, home])].copy()
        if game_df.empty:
            continue
        cards = build_market_cards(game_df, CONFIG)
        game_cards.append({"game": game_name, "cards": cards})
        overall_rows.extend(build_ranked_rows(game_df, game_name, CONFIG))

        for leg in cards.get("safest", [])[: int(CONFIG.get("safe_card_legs", 2))]:
            value_rows.append({
                "game": game_name,
                "player": leg["player"],
                "team": leg["team"],
                "market": leg["market"],
                "score": leg["score"],
                "grade": leg["grade"],
                "confidence": leg["score"],
                "edge": 0.0,
                "risk_note": "monitor lineup status",
            })

    export_rows = []
    for entry in overall_rows:
        export_rows.append(entry)

    export_csv(pd.DataFrame(export_rows), "command_center.csv")
    write_exports(overall_rows, "command_center.csv")
    write_exports([entry for entry in overall_rows if entry["market"] == "singles"], "singles.csv")
    write_exports([entry for entry in overall_rows if entry["market"] == "total_bases"], "total_bases.csv")
    write_exports([entry for entry in overall_rows if entry["market"] == "runs"], "runs.csv")
    write_exports([entry for entry in overall_rows if entry["market"] == "rbis"], "rbis.csv")
    write_exports([entry for entry in overall_rows if entry["market"] == "lotto"], "lotto.csv")
    write_exports([{"card_name": f"{item['game']} safest", "legs": item['cards'].get('safest', []), "market": "safe"} for item in game_cards], "cards.csv")
    write_exports(value_rows, "value_edges.csv")

    summary_lines = ["MLB-LAB BETTING CARDS", f"Games analyzed: {len(today_games)}", ""]
    if game_cards:
        for card in game_cards:
            summary_lines.append(card["game"])
            for leg in card["cards"].get("safest", [])[:2]:
                summary_lines.append(f"- {leg['player']} ({leg['team']}) {leg['market']} {leg['score']:.2f} {leg['grade']}")
            summary_lines.append("")
    else:
        summary_lines.append("No cards generated.")

    text_path = EXPORT_DIR / "betting_cards.txt"
    text_path.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

    html_template = """
    <html><body>
    <h1>MLB-LAB Betting Cards</h1>
    <p>Games analyzed: {{ games }}</p>
    {% for card in cards %}
    <h2>{{ card.game }}</h2>
    <ul>
    {% for leg in card.cards.safest[:2] %}
    <li>{{ leg.player }} ({{ leg.team }}) {{ leg.market }} {{ leg.score }} {{ leg.grade }}</li>
    {% endfor %}
    </ul>
    {% endfor %}
    </body></html>
    """
    html_path = EXPORT_DIR / "daily_report.html"
    html_path.write_text(Template(html_template).render(games=len(today_games), cards=game_cards), encoding="utf-8")

    export_csv(pd.DataFrame([{"summary": "cards generated"}]), "betting_cards.csv")
    export_json({"warnings": warnings, "issues": issues, "games": len(today_games), "cards": game_cards}, "daily_report.json")
    return {"warnings": warnings, "issues": issues, "rows": export_rows, "cards": game_cards, "value_rows": value_rows}


def run_workflow() -> Dict[str, Any]:
    return build_daily_report()
