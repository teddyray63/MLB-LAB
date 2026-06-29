import json
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Tuple

from jinja2 import Template

import pandas as pd

from backend.engine.card_builder import build_betting_card_portfolios, build_market_cards
from backend.engine.confidence import build_recommendation_context, edge_from_odds, grade_for_market
from backend.engine.exporter import export_json, export_csv, write_exports
from backend.engine.game_analyzer import load_data, validate_slate
from backend.engine.warehouse import ensure_warehouse_tables, record_recommendation
from backend.odds.edge_calculator import build_model_scores, build_odds_exports
from backend.odds.importer import import_odds_csv
from backend.reports.html import open_dashboard, save_dashboard
from backend.utils import normalize_name

ROOT = Path(__file__).resolve().parent.parent.parent
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
        context = build_recommendation_context(
            score=score,
            edge=float(row.get("edge_score", 0.0) or 0.0),
            lineup_certainty=float(row.get("lineup_certainty", 0.7) or 0.7),
            statcast_quality=float(row.get("statcast_quality", 0.7) or 0.7),
            sample_size=float(row.get("sample_size", 0.7) or 0.7),
            opponent_strength=float(row.get("opponent_strength", 0.7) or 0.7),
            weather=float(row.get("weather", 0.7) or 0.7),
            bullpen=float(row.get("bullpen", 0.7) or 0.7),
            park_factor=float(row.get("park_factor", 0.7) or 0.7),
            pitcher_quality=float(row.get("pitcher_quality", 0.7) or 0.7),
            market=market,
            minimum_confidence=config.get("minimum_confidence", 30.0),
        )
        rows.append({
            "section": "game_card",
            "game": game_name,
            "player": row.get("player_name", ""),
            "team": row.get("team", ""),
            "market": market,
            "score": score,
            "grade": context["grade"],
            "confidence": context["confidence"],
            "confidence_pct": context["confidence_pct"],
            "risk": context["risk"],
            "reasons": context["reasons"],
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
    game_lookup = {}
    for game in today_games:
        away = game.get("away_team", "")
        home = game.get("home_team", "")
        game_name = f"{away} @ {home}"
        for team in [away, home]:
            game_lookup[team] = game_name

    portfolio_df = scored.copy()
    if "game_name" not in portfolio_df.columns:
        portfolio_df["game_name"] = ""
    if not portfolio_df.empty:
        portfolio_df["game_name"] = portfolio_df["team"].map(game_lookup).fillna("")
    game_cards: List[Dict[str, Any]] = []
    overall_rows: List[Dict[str, Any]] = []
    value_rows: List[Dict[str, Any]] = []

    for game in today_games:
        away = game.get("away_team", "")
        home = game.get("home_team", "")
        game_name = f"{away} @ {home}"
        game_df = portfolio_df[portfolio_df["team"].isin([away, home])].copy()
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
                "confidence": leg.get("confidence", leg["score"]),
                "confidence_pct": leg.get("confidence_pct", leg.get("confidence", leg["score"])),
                "risk": leg.get("risk", "medium"),
                "reasons": leg.get("reasons", []),
                "edge": 0.0,
                "risk_note": "monitor lineup status",
            })

    portfolio_cards = build_betting_card_portfolios(portfolio_df, CONFIG)
    card_rows = []
    betting_card_rows = []
    lotto_rows = []
    for card_name, card in portfolio_cards.items():
        card_rows.append({
            "card_name": card_name,
            "name": card.get("name", card_name),
            "leg_count": card.get("leg_count", 0),
            "confidence": card.get("confidence", 0.0),
            "confidence_pct": card.get("confidence_pct", 0.0),
            "risk": card.get("risk", "high"),
            "grade": card.get("grade", "PASS"),
            "legs": json.dumps(card.get("legs", [])),
        })
        for leg in card.get("legs", []):
            betting_card_rows.append({
                "card_name": card_name,
                "player": leg.get("player", ""),
                "team": leg.get("team", ""),
                "game": leg.get("game", ""),
                "market": leg.get("market", ""),
                "score": leg.get("score", 0.0),
                "grade": leg.get("grade", "PASS"),
                "confidence": leg.get("confidence", 0.0),
                "confidence_pct": leg.get("confidence_pct", 0.0),
                "risk": leg.get("risk", "high"),
                "reasons": json.dumps(leg.get("reasons", [])),
            })
        if card_name == "best_6_leg_lotto":
            for leg in card.get("legs", []):
                lotto_rows.append({
                    "card_name": card_name,
                    "player": leg.get("player", ""),
                    "team": leg.get("team", ""),
                    "game": leg.get("game", ""),
                    "market": leg.get("market", ""),
                    "score": leg.get("score", 0.0),
                    "grade": leg.get("grade", "PASS"),
                    "confidence": leg.get("confidence", 0.0),
                    "confidence_pct": leg.get("confidence_pct", 0.0),
                    "risk": leg.get("risk", "high"),
                    "reasons": json.dumps(leg.get("reasons", [])),
                })

    ensure_warehouse_tables()
    today_date = date.today().isoformat()
    for entry in overall_rows:
        record_recommendation(
            {
                "player": entry.get("player", ""),
                "team": entry.get("team", ""),
                "market": entry.get("market", ""),
                "sportsbook": entry.get("sportsbook", ""),
                "confidence": entry.get("confidence", 0.0),
                "edge": entry.get("edge", 0.0),
                "line": entry.get("line"),
                "odds": entry.get("odds"),
                "details": entry.get("reasons", []),
                "grade": entry.get("grade", "PASS"),
                "risk": entry.get("risk", "medium"),
            },
            event_date=today_date,
        )

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
    export_csv(pd.DataFrame(card_rows), "cards.csv")
    export_csv(pd.DataFrame(betting_card_rows), "betting_cards.csv")
    export_csv(pd.DataFrame(lotto_rows), "lotto.csv")
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

    export_csv(pd.DataFrame(betting_card_rows), "betting_cards.csv")
    dashboard_path = save_dashboard(pd.DataFrame(card_rows), pd.DataFrame(betting_card_rows), pd.DataFrame(lotto_rows), today_games, EXPORT_DIR / "daily_dashboard.html")
    open_dashboard(dashboard_path)
    odds_path = ROOT / CONFIG.get("odds_path", "exports/odds.csv")
    slate_players = pd.DataFrame([{"player_name": row["player"], "team": row["team"]} for row in overall_rows])
    if odds_path.exists():
        odds_exports = build_odds_exports(odds_path, slate_players, EXPORT_DIR)
    else:
        odds_exports = {
            "live_odds": EXPORT_DIR / "live_odds.csv",
            "value_edges": EXPORT_DIR / "value_edges.csv",
            "betting_edges": EXPORT_DIR / "betting_edges.csv",
        }
        empty_columns = ["player_name", "book", "team", "market", "line", "odds", "implied_probability", "model_probability", "expected_value", "edge_pct", "kelly_fraction", "positive_ev", "negative_ev", "missing_player", "duplicate_player"]
        for export_name, export_path in odds_exports.items():
            pd.DataFrame(columns=empty_columns).to_csv(export_path, index=False)

    export_json({"warnings": warnings, "issues": issues, "games": len(today_games), "cards": game_cards, "odds_exports": {key: str(path.name) for key, path in odds_exports.items()}}, "daily_report.json")
    return {"warnings": warnings, "issues": issues, "rows": export_rows, "cards": game_cards, "value_rows": value_rows, "odds_exports": odds_exports}


def run_workflow() -> Dict[str, Any]:
    return build_daily_report()
