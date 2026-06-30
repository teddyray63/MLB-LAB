from backend.engine.confidence import build_recommendation_context


def test_build_recommendation_context_returns_grade_metadata():
    context = build_recommendation_context(
        score=72.0,
        edge=12.0,
        lineup_certainty=0.92,
        statcast_quality=0.85,
        sample_size=0.78,
        opponent_strength=0.6,
        weather=0.8,
        bullpen=0.7,
        park_factor=0.8,
        pitcher_quality=0.75,
        market="singles",
    )

    assert context["grade"] == "A"
    assert context["risk"] in {"low", "medium", "high"}
    assert 0 <= context["confidence"] <= 100
    assert 0 <= context["confidence_pct"] <= 100
    assert context["reasons"]
    assert any("edge" in reason.lower() for reason in context["reasons"])
    assert context["implied_probability"] is None
    assert context["clv"] is None
    assert isinstance(context["park_adjusted_ev"], float)


def test_build_recommendation_context_with_implied_probability_and_clv():
    context = build_recommendation_context(
        score=72.0,
        edge=12.0,
        lineup_certainty=0.92,
        statcast_quality=0.85,
        sample_size=0.78,
        opponent_strength=0.6,
        weather=0.8,
        bullpen=0.7,
        park_factor=0.8,
        pitcher_quality=0.75,
        market="singles",
        implied_probability=0.55,
        handedness_advantage=0.8,
        closing_line_value=2.3,
    )

    assert context["implied_probability"] == 0.55
    assert context["clv"] == 2.3
    assert isinstance(context["park_adjusted_ev"], float)


def test_build_recommendation_context_graceful_fallback_when_optional_missing():
    context = build_recommendation_context(
        score=50.0,
        edge=5.0,
        lineup_certainty=0.6,
        statcast_quality=0.6,
        sample_size=0.6,
        opponent_strength=0.5,
        weather=0.5,
        bullpen=0.5,
        park_factor=0.5,
        pitcher_quality=0.5,
        market="singles",
    )

    assert context["implied_probability"] is None
    assert context["clv"] is None
    assert context["grade"] in {"A+", "A", "A-", "B+", "B", "B-", "C", "PASS"}
