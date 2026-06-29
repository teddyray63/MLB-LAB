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
