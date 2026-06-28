import math
from typing import Any, Dict


def grade_for_market(score: float, market: str, minimum_confidence: float = 30.0) -> str:
    try:
        score_value = float(score)
    except (TypeError, ValueError):
        return "PASS"

    if market in {"singles", "total_bases", "runs", "rbis", "lotto"}:
        if score_value >= max(minimum_confidence + 25, 55):
            return "A+"
        if score_value >= max(minimum_confidence + 15, 45):
            return "A"
        if score_value >= max(minimum_confidence + 8, 38):
            return "B+"
        if score_value >= max(minimum_confidence, 30):
            return "B"
        if score_value >= max(minimum_confidence - 10, 20):
            return "C"
        return "PASS"

    if score_value >= 60:
        return "A+"
    if score_value >= 50:
        return "A"
    if score_value >= 42:
        return "B+"
    if score_value >= 35:
        return "B"
    if score_value >= 25:
        return "C"
    return "PASS"


def edge_from_odds(model_score: float, line: Any, odds: Any) -> Dict[str, Any]:
    try:
        model = float(model_score)
    except (TypeError, ValueError):
        model = 0.0

    if line in {None, "", "nan"} or odds in {None, "", "nan"}:
        return {"edge_score": 0.0, "value_flag": False, "implied_probability": None}

    try:
        american = float(odds)
    except (TypeError, ValueError):
        return {"edge_score": 0.0, "value_flag": False, "implied_probability": None}

    if american > 0:
        implied = 100 / (american + 100)
    else:
        implied = abs(american) / (abs(american) + 100)

    model_prob = 1 - (model / 100.0)
    if model_prob <= 0:
        model_prob = 0.05
    if model_prob >= 1:
        model_prob = 0.95

    edge = (model_prob - implied) * 100.0
    return {
        "edge_score": round(edge, 2),
        "value_flag": edge >= 5.0,
        "implied_probability": round(implied, 4),
    }
