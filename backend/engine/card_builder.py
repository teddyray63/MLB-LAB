from typing import Any, Dict, List

import pandas as pd

from backend.engine.confidence import build_recommendation_context


def _context_for_row(row: pd.Series, market: str, config: Dict[str, Any]) -> Dict[str, Any]:
    score = float(row.get(f"{market}_score", 0) or 0) if market in {"singles", "total_bases", "runs", "rbi", "lotto"} else float(row.get("score", 0) or 0)
    return build_recommendation_context(
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


def _leg_from_row(row: pd.Series, market: str, config: Dict[str, Any]) -> Dict[str, Any]:
    context = _context_for_row(row, market, config)
    return {
        "player": row.get("player_name", ""),
        "team": row.get("team", ""),
        "game": row.get("game_name", ""),
        "market": market,
        "score": float(row.get(f"{market}_score", 0) or 0) if market in {"singles", "total_bases", "runs", "rbi", "lotto"} else float(row.get("score", 0) or 0),
        "grade": context["grade"],
        "confidence": context["confidence"],
        "confidence_pct": context["confidence_pct"],
        "risk": context["risk"],
        "reasons": context["reasons"],
    }


def _build_ranked_legs(game_df: pd.DataFrame, market: str, config: Dict[str, Any], limit: int) -> List[Dict[str, Any]]:
    if game_df.empty:
        return []
    ranked = game_df.sort_values([f"{market}_score" if market in {"singles", "total_bases", "runs", "rbi", "lotto"} else "score"], ascending=False)
    legs = []
    for _, row in ranked.iterrows():
        if len(legs) >= limit:
            break
        legs.append(_leg_from_row(row, market, config))
    return legs


def _select_diversified_legs(candidates: List[Dict[str, Any]], count: int, max_same_team: int = 2) -> List[Dict[str, Any]]:
    selected: List[Dict[str, Any]] = []
    used_players = set()
    team_counts: Dict[str, int] = {}
    game_counts: Dict[str, int] = {}
    for leg in sorted(candidates, key=lambda item: item.get("confidence", 0), reverse=True):
        player = leg.get("player", "")
        team = leg.get("team", "")
        game = leg.get("game", "")
        if not player or player in used_players:
            continue
        if team_counts.get(team, 0) >= max_same_team:
            continue
        if game and game_counts.get(game, 0) >= 1:
            continue
        selected.append(leg)
        used_players.add(player)
        team_counts[team] = team_counts.get(team, 0) + 1
        if game:
            game_counts[game] = game_counts.get(game, 0) + 1
        if len(selected) >= count:
            break
    return selected


def build_market_cards(game_df: pd.DataFrame, config: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    cards: Dict[str, List[Dict[str, Any]]] = {"safest": [], "lotto": [], "singles": [], "total_bases": []}
    if game_df.empty:
        return cards

    safe_candidates = [
        _leg_from_row(row, "singles", config) for _, row in game_df.sort_values("singles_score", ascending=False).iterrows()
    ] + [
        _leg_from_row(row, "total_bases", config) for _, row in game_df.sort_values("total_bases_score", ascending=False).iterrows()
    ]
    cards["safest"] = _select_diversified_legs(safe_candidates, int(config.get("safe_card_legs", 2)), max_same_team=1)

    lotto_candidates = [
        _leg_from_row(row, "lotto", config) for _, row in game_df.sort_values(["lotto_score", "total_bases_score", "runs_score", "rbi_score"], ascending=False).iterrows()
    ]
    cards["lotto"] = _select_diversified_legs(lotto_candidates, int(config.get("lotto_card_legs", 4)), max_same_team=2)

    cards["singles"] = _build_ranked_legs(game_df, "singles", config, int(config.get("top_players_per_game", 5)))
    cards["total_bases"] = _build_ranked_legs(game_df, "total_bases", config, int(config.get("top_players_per_game", 5)))
    return cards


def build_betting_card_portfolios(game_df: pd.DataFrame, config: Dict[str, Any]) -> Dict[str, Any]:
    if game_df.empty:
        return {
            "top_10_singles": {"name": "Top 10 Singles", "legs": [], "leg_count": 0, "confidence": 0.0, "confidence_pct": 0.0, "risk": "high", "grade": "PASS"},
            "top_10_total_bases": {"name": "Top 10 Total Bases", "legs": [], "leg_count": 0, "confidence": 0.0, "confidence_pct": 0.0, "risk": "high", "grade": "PASS"},
            "top_10_runs": {"name": "Top 10 Runs", "legs": [], "leg_count": 0, "confidence": 0.0, "confidence_pct": 0.0, "risk": "high", "grade": "PASS"},
            "top_10_rbi": {"name": "Top 10 RBI", "legs": [], "leg_count": 0, "confidence": 0.0, "confidence_pct": 0.0, "risk": "high", "grade": "PASS"},
            "safest_2_leg": {"name": "Safest 2-Leg", "legs": [], "leg_count": 0, "confidence": 0.0, "confidence_pct": 0.0, "risk": "high", "grade": "PASS"},
            "safest_3_leg": {"name": "Safest 3-Leg", "legs": [], "leg_count": 0, "confidence": 0.0, "confidence_pct": 0.0, "risk": "high", "grade": "PASS"},
            "best_4_leg": {"name": "Best 4-Leg", "legs": [], "leg_count": 0, "confidence": 0.0, "confidence_pct": 0.0, "risk": "high", "grade": "PASS"},
            "best_6_leg_lotto": {"name": "Best 6-Leg Lotto", "legs": [], "leg_count": 0, "confidence": 0.0, "confidence_pct": 0.0, "risk": "high", "grade": "PASS"},
        }

    portfolios = {
        "top_10_singles": {"name": "Top 10 Singles", "legs": []},
        "top_10_total_bases": {"name": "Top 10 Total Bases", "legs": []},
        "top_10_runs": {"name": "Top 10 Runs", "legs": []},
        "top_10_rbi": {"name": "Top 10 RBI", "legs": []},
        "safest_2_leg": {"name": "Safest 2-Leg", "legs": []},
        "safest_3_leg": {"name": "Safest 3-Leg", "legs": []},
        "best_4_leg": {"name": "Best 4-Leg", "legs": []},
        "best_6_leg_lotto": {"name": "Best 6-Leg Lotto", "legs": []},
    }

    portfolios["top_10_singles"]["legs"] = _select_diversified_legs(
        [_leg_from_row(row, "singles", config) for _, row in game_df.sort_values("singles_score", ascending=False).iterrows()],
        10,
        max_same_team=2,
    )
    portfolios["top_10_total_bases"]["legs"] = _select_diversified_legs(
        [_leg_from_row(row, "total_bases", config) for _, row in game_df.sort_values("total_bases_score", ascending=False).iterrows()],
        10,
        max_same_team=2,
    )
    portfolios["top_10_runs"]["legs"] = _select_diversified_legs(
        [_leg_from_row(row, "runs", config) for _, row in game_df.sort_values("runs_score", ascending=False).iterrows()],
        10,
        max_same_team=2,
    )
    portfolios["top_10_rbi"]["legs"] = _select_diversified_legs(
        [_leg_from_row(row, "rbi", config) for _, row in game_df.sort_values("rbi_score", ascending=False).iterrows()],
        10,
        max_same_team=2,
    )
    portfolios["safest_2_leg"]["legs"] = _select_diversified_legs(
        [_leg_from_row(row, "singles", config) for _, row in game_df.sort_values("singles_score", ascending=False).iterrows()] +
        [_leg_from_row(row, "total_bases", config) for _, row in game_df.sort_values("total_bases_score", ascending=False).iterrows()],
        2,
        max_same_team=1,
    )
    portfolios["safest_3_leg"]["legs"] = _select_diversified_legs(
        [_leg_from_row(row, "singles", config) for _, row in game_df.sort_values("singles_score", ascending=False).iterrows()] +
        [_leg_from_row(row, "total_bases", config) for _, row in game_df.sort_values("total_bases_score", ascending=False).iterrows()],
        3,
        max_same_team=1,
    )
    portfolios["best_4_leg"]["legs"] = _select_diversified_legs(
        [_leg_from_row(row, "singles", config) for _, row in game_df.sort_values("singles_score", ascending=False).iterrows()] +
        [_leg_from_row(row, "total_bases", config) for _, row in game_df.sort_values("total_bases_score", ascending=False).iterrows()] +
        [_leg_from_row(row, "runs", config) for _, row in game_df.sort_values("runs_score", ascending=False).iterrows()] +
        [_leg_from_row(row, "rbi", config) for _, row in game_df.sort_values("rbi_score", ascending=False).iterrows()],
        4,
        max_same_team=2,
    )
    portfolios["best_6_leg_lotto"]["legs"] = _select_diversified_legs(
        [_leg_from_row(row, "lotto", config) for _, row in game_df.sort_values(["lotto_score", "total_bases_score", "runs_score", "rbi_score"], ascending=False).iterrows()],
        6,
        max_same_team=2,
    )

    for name, card in portfolios.items():
        legs = card["legs"]
        if not legs:
            card.update({"leg_count": 0, "confidence": 0.0, "confidence_pct": 0.0, "risk": "high", "grade": "PASS"})
            continue
        average_confidence = sum(leg.get("confidence", 0.0) for leg in legs) / len(legs)
        card.update({
            "leg_count": len(legs),
            "confidence": round(average_confidence, 2),
            "confidence_pct": round(average_confidence, 2),
            "risk": "low" if average_confidence >= 70 else "medium" if average_confidence >= 45 else "high",
            "grade": "A+" if average_confidence >= 85 else "A" if average_confidence >= 75 else "A-" if average_confidence >= 65 else "B+" if average_confidence >= 55 else "B" if average_confidence >= 45 else "B-" if average_confidence >= 35 else "C" if average_confidence >= 25 else "PASS",
        })

    return portfolios
