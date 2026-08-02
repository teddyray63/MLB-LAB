"""Offline tests for G0b.4 hitter enrichment."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from backend.export.build_matchup_layer import build_matchup_layer
from backend.export.enrichment.hitter_stats import build_hitter_enrichments
from backend.export.enrichment.statcast_formulas import compute_rate_block, compute_split_block, filter_rows
from backend.export.enrichment.statcast_source import events_from_fixture
from backend.export.build_identity_layer import build_identity_layer

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _events():
    return events_from_fixture(FIXTURES / "statcast_hitter_sample.json")


def _identity():
    schedule = json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8"))
    feeds = {822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))}
    return build_identity_layer(schedule, slate_date="2026-07-19", feeds_by_pk=feeds)


def test_complete_season_summary() -> None:
    events = _events()
    block = compute_split_block(filter_rows(events, batter_id=7000001), split="overall")
    assert block.counts.pa is not None and block.counts.pa > 0
    assert block.rates.avg is not None
    assert block.rates.obp is not None
    assert block.rates.slg is not None


def test_missing_denominator_warning() -> None:
    rows = [{"events": "walk", "description": "ball"}]
    block = compute_split_block(rows, split="overall")
    assert block.missing_denominator is True


def test_valid_rate_calculations() -> None:
    events = _events()
    rates = compute_rate_block(filter_rows(events, batter_id=7000001))
    assert rates.k_pct is not None
    assert 0 <= rates.k_pct <= 1


def test_missing_handedness_split_warns() -> None:
    identity = _identity()
    from backend.export.build_matchup_layer import _opponent_team_map, _opponent_starter_map

    result = build_hitter_enrichments(
        identity.players,
        [{"batter": 7000001, "events": "single", "p_throws": "R", "game_date": "2026-07-10"}],
        opponent_starter_by_team=_opponent_starter_map(identity.games, identity.lineups),
        opponent_team_by_player=_opponent_team_map(identity.teams, identity.players),
    )
    assert any("Missing vs_lhp" in warning for warning in result.warnings)


def test_recent_window_present() -> None:
    layer = build_matchup_layer(
        json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8")),
        slate_date="2026-07-19",
        feeds_by_pk={822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))},
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )
    hitter = next(item for item in layer.hitter_enrichments if item.player_id == 7000001)
    assert "last_5" in hitter.recent or "last_7" in hitter.recent


def test_recent_window_absent_for_unknown_player() -> None:
    identity = _identity()
    from backend.export.build_matchup_layer import _opponent_team_map, _opponent_starter_map

    result = build_hitter_enrichments(
        [player for player in identity.players if player.player_id == 7000003],
        [],
        opponent_starter_by_team=_opponent_starter_map(identity.games, identity.lineups),
        opponent_team_by_player=_opponent_team_map(identity.teams, identity.players),
    )
    assert result.enrichments[0].season is None


def test_null_preservation_unsupported_fields_not_in_enrichment() -> None:
    layer = build_matchup_layer(
        json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8")),
        slate_date="2026-07-19",
        feeds_by_pk={822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))},
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )
    for row in layer.export_matchup_rows:
        assert row.xba is None
        assert row.xslg is None
        assert row.bat_speed is None


def test_deterministic_output() -> None:
    kwargs = dict(
        schedule_json=json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8")),
        slate_date="2026-07-19",
        feeds_by_pk={822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))},
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )
    first = build_matchup_layer(**kwargs)
    second = build_matchup_layer(**kwargs)
    assert [item.model_dump() for item in first.hitter_enrichments] == [
        item.model_dump() for item in second.hitter_enrichments
    ]
