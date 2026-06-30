import math
from typing import Any, Dict, List, Optional

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
    recent_form: float = 0.7,
    implied_probability: Optional[float] = None,
    handedness_advantage: float = 0.7,
) -> Dict[str, Any]:
    """Combine raw score with contextual factors to produce a graded recommendation dict.

    Additional signals beyond the base nine:
      recent_form         — recency-weighted performance (0-1); pass actual value when available
      implied_probability — sportsbook implied prob (0-1); used to compare vs model estimate
      handedness_advantage — L/R matchup advantage (0-1); pass actual split when available

    TODO: wire weather from real forecast API (weather_score currently passed as default 0.7)
    TODO: wire umpire strike zone tendency when umpire data source is available
    TODO: wire pitch-mix matchup (hitter vs pitcher arsenal) when pitch data is integrated
    TODO: wire closing-line-value (CLV) signal once line-movement tracking is in place
    """
    try:
        base_score = float(score)
    except (TypeError, ValueError):
        base_score = 0.0

    # When implied_probability is known, compute real edge from model vs market
    if implied_probability is not None and 0 < implied_probability < 1:
        model_prob = base_score / 100.0
        real_edge_pct = (model_prob - implied_probability) * 100.0
        edge_score = _clamp((real_edge_pct + 20.0) / 40.0)  # map [-20, +20] → [0, 1]
    else:
        edge_score = _clamp(edge / 20.0)

    lineup_score = _clamp(lineup_certainty)
    statcast_score = _clamp(statcast_quality)
    sample_score = _clamp(sample_size)
    opponent_score = _clamp(opponent_strength)
    weather_score = _clamp(weather)
    bullpen_score = _clamp(bullpen)
    # Park factor carries higher weight for extra-base / total-bases markets
    park_raw = _clamp(park_factor)
    park_weight = 1.4 if market in {"total_bases", "runs", "rbis"} else 1.0
    park_score = _clamp(park_raw * park_weight)
    pitcher_score = _clamp(pitcher_quality)
    form_score = _clamp(recent_form)
    hand_score = _clamp(handedness_advantage)

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
        (form_score, "recent form"),
        (hand_score, "handedness matchup"),
    ]

    confidence = round(
        (base_score * 0.55) + (sum(v for v, _ in weighted_components) / len(weighted_components) * 45.0), 2
    )
    confidence = max(0.0, min(100.0, confidence))
    grade = grade_for_market(confidence, market, minimum_confidence)
    risk = _risk_from_confidence(confidence)

    reasons: List[str] = []

    if implied_probability is not None and 0 < implied_probability < 1:
        model_prob = base_score / 100.0
        real_edge_pct = (model_prob - implied_probability) * 100.0
        imp_pct = round(implied_probability * 100, 1)
        if real_edge_pct >= 8:
            reasons.append(f"strong edge vs market ({imp_pct}% implied)")
        elif real_edge_pct >= 3:
            reasons.append(f"positive edge vs {imp_pct}% market line")
        elif real_edge_pct >= -3:
            reasons.append(f"fair value near {imp_pct}% implied")
        else:
            reasons.append(f"model trails {imp_pct}% implied — no edge")
    elif edge_score >= 0.6:
        reasons.append("strong model edge")
    elif edge_score >= 0.3:
        reasons.append("positive model edge")
    else:
        reasons.append("edge not compelling")

    if form_score >= 0.8:
        reasons.append("player in strong recent form")
    elif form_score >= 0.55:
        reasons.append("recent form is acceptable")
    else:
        reasons.append("recent form is soft")

    if hand_score >= 0.75:
        reasons.append("favorable handedness matchup")
    elif hand_score >= 0.5:
        reasons.append("neutral handedness matchup")
    else:
        reasons.append("unfavorable L/R matchup")

    if lineup_score >= 0.8:
        reasons.append("confirmed lineup spot")
    elif lineup_score >= 0.6:
        reasons.append("likely in lineup")
    else:
        reasons.append("lineup status uncertain")

    if statcast_score >= 0.8:
        reasons.append("elite statcast profile")
    elif statcast_score >= 0.6:
        reasons.append("solid statcast metrics")
    else:
        reasons.append("limited statcast support")

    if sample_score >= 0.8:
        reasons.append("large sample size")
    elif sample_score >= 0.6:
        reasons.append("adequate sample")
    else:
        reasons.append("small sample — higher variance")

    if opponent_score >= 0.7:
        reasons.append("weak opponent pitching")
    elif opponent_score >= 0.4:
        reasons.append("neutral opponent matchup")
    else:
        reasons.append("tough opponent pitching")

    if park_score >= 0.7:
        reasons.append("hitter-friendly park")
    elif park_score >= 0.4:
        reasons.append("neutral park")
    else:
        reasons.append("pitcher-friendly park")

    if pitcher_score >= 0.7:
        reasons.append("opposing pitcher is hittable")
    elif pitcher_score >= 0.4:
        reasons.append("opposing pitcher is average")
    else:
        reasons.append("tough starting pitcher")

    if bullpen_score >= 0.7:
        reasons.append("bullpen situation is favorable")
    elif bullpen_score < 0.4:
        reasons.append("bullpen situation is concerning")

    if weather_score < 0.4:
        reasons.append("weather may suppress offense")

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
