"""Offline tests for G0b.4 pitcher enrichment."""

from __future__ import annotations

import json
from pathlib import Path

from backend.export.build_matchup_layer import build_matchup_layer
from backend.export.enrichment.pitcher_stats import build_pitcher_enrichments
from backend.export.enrichment.statcast_source import events_from_fixture
from backend.export.build_identity_layer import build_identity_layer

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _bundle():
    schedule = json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8"))
    feeds = {822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))}
    events = events_from_fixture(FIXTURES / "statcast_hitter_sample.json")
    identity = build_identity_layer(schedule, slate_date="2026-07-19", feeds_by_pk=feeds)
    return identity, events


def test_complete_starter_summary() -> None:
    layer = build_matchup_layer(
        json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8")),
        slate_date="2026-07-19",
        feeds_by_pk={822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))},
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )
    starter = next(item for item in layer.pitcher_enrichments if item.player_id == 702056)
    assert starter.season is not None
    assert starter.season.counts.pa is not None


def test_probable_vs_actual_starter_flags() -> None:
    identity, _ = _bundle()
    starters = [player for player in identity.players if player.player_id in {680732, 702056}]
    assert any(player.is_probable_starter for player in starters)
    assert any(player.is_actual_starter for player in starters)


def test_missing_starter_warns() -> None:
    identity, events = _bundle()
    from backend.export.build_matchup_layer import _opponent_team_map

    result = build_pitcher_enrichments(
        identity.players,
        events,
        opponent_team_by_player=_opponent_team_map(identity.teams, identity.players),
    )
    assert any(item.player_id in {680732, 702056} for item in result.enrichments)


def test_handedness_splits() -> None:
    layer = build_matchup_layer(
        json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8")),
        slate_date="2026-07-19",
        feeds_by_pk={822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))},
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )
    starter = next(item for item in layer.pitcher_enrichments if item.player_id == 702056)
    assert "vs_lhb" in starter.splits or "vs_rhb" in starter.splits


def test_missing_denominator() -> None:
    identity, _ = _bundle()
    from backend.export.build_matchup_layer import _opponent_team_map

    result = build_pitcher_enrichments(
        identity.players,
        [{"pitcher": 702056, "events": "walk", "description": "ball", "game_date": "2026-07-10"}],
        opponent_team_by_player=_opponent_team_map(identity.teams, identity.players),
    )
    starter = next(item for item in result.enrichments if item.player_id == 702056)
    assert starter.season is not None
    assert starter.season.missing_denominator is True


def test_valid_rates() -> None:
    layer = build_matchup_layer(
        json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8")),
        slate_date="2026-07-19",
        feeds_by_pk={822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))},
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )
    starter = next(item for item in layer.pitcher_enrichments if item.player_id == 702056)
    assert starter.season is not None
    k_pct = starter.season.rates.k_pct
    assert k_pct is None or 0 <= k_pct <= 1


def test_deterministic_output() -> None:
    kwargs = dict(
        schedule_json=json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8")),
        slate_date="2026-07-19",
        feeds_by_pk={822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))},
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )
    first = build_matchup_layer(**kwargs)
    second = build_matchup_layer(**kwargs)
    assert [item.model_dump() for item in first.pitcher_enrichments] == [
        item.model_dump() for item in second.pitcher_enrichments
    ]
