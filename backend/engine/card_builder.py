from typing import Any, Dict, List, Tuple

import pandas as pd

from backend.engine.confidence import grade_for_market


def build_market_cards(game_df: pd.DataFrame, config: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    cards: Dict[str, List[Dict[str, Any]]] = {"safest": [], "lotto": [], "singles": [], "total_bases": []}
    if game_df.empty:
        return cards

    safe_legs = []
    for _, row in game_df.sort_values("singles_score", ascending=False).iterrows():
        if len(safe_legs) >= int(config.get("safe_card_legs", 2)):
            break
        safe_legs.append({
            "player": row.get("player_name", ""),
            "team": row.get("team", ""),
            "market": "singles",
            "score": float(row.get("singles_score", 0) or 0),
            "grade": grade_for_market(row.get("singles_score", 0), "singles", config.get("minimum_confidence", 30.0)),
        })

    tb_legs = []
    for _, row in game_df.sort_values("total_bases_score", ascending=False).iterrows():
        if len(tb_legs) >= int(config.get("safe_card_legs", 2)):
            break
        tb_legs.append({
            "player": row.get("player_name", ""),
            "team": row.get("team", ""),
            "market": "total_bases",
            "score": float(row.get("total_bases_score", 0) or 0),
            "grade": grade_for_market(row.get("total_bases_score", 0), "total_bases", config.get("minimum_confidence", 30.0)),
        })

    cards["safest"] = safe_legs[: int(config.get("safe_card_legs", 2))] + tb_legs[: int(config.get("safe_card_legs", 2))]
    cards["safest"] = cards["safest"][: int(config.get("safe_card_legs", 2))]

    lotto_legs = []
    for _, row in game_df.sort_values(["total_bases_score", "runs_score", "rbi_score"], ascending=False).iterrows():
        if len(lotto_legs) >= int(config.get("lotto_card_legs", 4)):
            break
        lotto_legs.append({
            "player": row.get("player_name", ""),
            "team": row.get("team", ""),
            "market": "lotto",
            "score": float(row.get("lotto_score", 0) or 0),
            "grade": grade_for_market(row.get("lotto_score", 0), "lotto", config.get("minimum_confidence", 30.0)),
        })
    cards["lotto"] = lotto_legs

    singles = []
    for _, row in game_df.sort_values("singles_score", ascending=False).iterrows():
        if len(singles) >= int(config.get("top_players_per_game", 5)):
            break
        singles.append({
            "player": row.get("player_name", ""),
            "team": row.get("team", ""),
            "market": "singles",
            "score": float(row.get("singles_score", 0) or 0),
            "grade": grade_for_market(row.get("singles_score", 0), "singles", config.get("minimum_confidence", 30.0)),
        })
    cards["singles"] = singles

    totals = []
    for _, row in game_df.sort_values("total_bases_score", ascending=False).iterrows():
        if len(totals) >= int(config.get("top_players_per_game", 5)):
            break
        totals.append({
            "player": row.get("player_name", ""),
            "team": row.get("team", ""),
            "market": "total_bases",
            "score": float(row.get("total_bases_score", 0) or 0),
            "grade": grade_for_market(row.get("total_bases_score", 0), "total_bases", config.get("minimum_confidence", 30.0)),
        })
    cards["total_bases"] = totals

    return cards
