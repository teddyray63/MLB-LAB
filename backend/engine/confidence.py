import math
from typing import Any, Dict, List

GRADE_ORDER = ["A+", "A", "A-", "B+", "B", "B-", "C", "PASS"]


def grade_for_market(score: float, market: str, minimum_confidence: float = 30.0) -> str:
    """Map a numeric score to a letter grade (A+ through PASS) for the given market type."""
    try:
        score_value = float(score)
    except (TypeError, ValueError):
        return "PASS"

    if market in {"singles", "total_bases", "runs", "rbis", "lotto"}:
        if score_value >= max(minimum_confidence + 35, 80):
            return "A+"
        if score_value >= max(minimum_confidence + 25, 70):
            return "A"
        if score_value >= max(minimum_confidence + 15, 60):
            return "A-"
        if score_value >= max(minimum_confidence + 8, 50):
            return "B+"
        if score_value >= max(minimum_confidence, 40):
            return "B"
        if score_value >= max(minimum_confidence - 8, 32):
            return "B-"
        if score_value >= max(minimum_confidence - 20, 25):
            return "C"
        return "PASS"

    if score_value >= 80:
        return "A+"
    if score_value >= 70:
        return "A"
    if score_value >= 60:
        return "A-"
    if score_value >= 50:
        return "B+"
    if score_value >= 40:
        return "B"
    if score_value >= 32:
        return "B-"
    if score_value >= 25:
        return "C"
    return "PASS"


def _clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, float(value)))


def _risk_from_confidence(confidence: float) -> str:
    if confidence >= 80:
        return "low"
    if confidence >= 60:
        return "medium"
    return "high"


def build_recommendation_context(
    score: float,
    edge: float,
    lineup_certainty: float,
    statcast_quality: float,
    sample_size: float,
    opponent_strength: float,
    weather: float,
    bullpen: float,
    park_factor: float,
    pitcher_quality: float,
    market: str,
    minimum_confidence: float = 30.0,
) -> Dict[str, Any]:
    """Combine raw score with contextual factors to produce a graded recommendation dict."""
    try:
        base_score = float(score)
    except (TypeError, ValueError):
        base_score = 0.0

    edge_score = _clamp(edge / 20.0)
    lineup_score = _clamp(lineup_certainty)
    statcast_score = _clamp(statcast_quality)
    sample_score = _clamp(sample_size)
    opponent_score = _clamp(opponent_strength)
    weather_score = _clamp(weather)
    bullpen_score = _clamp(bullpen)
    park_score = _clamp(park_factor)
    pitcher_score = _clamp(pitcher_quality)

    weighted_components = [
        (edge_score, "edge"),
        (lineup_score, "lineup certainty"),
        (statcast_score, "statcast quality"),
        (sample_score, "sample size"),
        (opponent_score, "opponent strength"),
        (weather_score, "weather"),
        (bullpen_score, "bullpen"),
        (park_score, "park factor"),
        (pitcher_score, "pitcher quality"),
    ]

    confidence = round((base_score * 0.55) + (sum(value for value, _ in weighted_components) / len(weighted_components) * 45.0), 2)
    confidence = max(0.0, min(100.0, confidence))
    grade = grade_for_market(confidence, market, minimum_confidence)
    risk = _risk_from_confidence(confidence)

    reasons: List[str] = []
    if edge_score >= 0.6:
        reasons.append("strong edge")
    elif edge_score >= 0.3:
        reasons.append("positive edge")
    else:
        reasons.append("edge not compelling")

    if lineup_score >= 0.8:
        reasons.append("lineup certainty is strong")
    elif lineup_score >= 0.6:
        reasons.append("lineup certainty is moderate")
    else:
        reasons.append("lineup certainty is weak")

    if statcast_score >= 0.8:
        reasons.append("statcast quality is strong")
    elif statcast_score >= 0.6:
        reasons.append("statcast quality is fair")
    else:
        reasons.append("statcast quality is limited")

    if sample_score >= 0.8:
        reasons.append("sample size is healthy")
    elif sample_score >= 0.6:
        reasons.append("sample size is acceptable")
    else:
        reasons.append("sample size is thin")

    if opponent_score >= 0.7:
        reasons.append("opponent strength favors the play")
    elif opponent_score >= 0.4:
        reasons.append("opponent strength is neutral")
    else:
        reasons.append("opponent strength is unfavorable")

    if weather_score >= 0.7:
        reasons.append("weather is favorable")
    elif weather_score >= 0.4:
        reasons.append("weather is neutral")
    else:
        reasons.append("weather is unfavorable")

    if bullpen_score >= 0.7:
        reasons.append("bullpen support is favorable")
    elif bullpen_score >= 0.4:
        reasons.append("bullpen support is neutral")
    else:
        reasons.append("bullpen support is weak")

    if park_score >= 0.7:
        reasons.append("park factor is favorable")
    elif park_score >= 0.4:
        reasons.append("park factor is neutral")
    else:
        reasons.append("park factor is unfavorable")

    if pitcher_score >= 0.7:
        reasons.append("pitcher quality is favorable")
    elif pitcher_score >= 0.4:
        reasons.append("pitcher quality is neutral")
    else:
        reasons.append("pitcher quality is unfavorable")

    return {
        "confidence": round(confidence, 2),
        "confidence_pct": round(confidence, 2),
        "risk": risk,
        "grade": grade,
        "reasons": reasons,
    }


def edge_from_odds(model_score: float, line: Any, odds: Any) -> Dict[str, Any]:
    """Compute edge_score, value_flag, and implied_probability from American odds vs model score."""
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
