"""Deterministic tests for batter-vs-today's-starter (BVP) population."""

from __future__ import annotations

import json
from pathlib import Path

from backend.export.build_identity_layer import build_identity_layer
from backend.export.build_matchup_layer import (
    _opponent_starter_map,
    _opponent_team_map,
    build_matchup_layer,
)
from backend.export.enrichment.hitter_stats import build_hitter_enrichments
from backend.export.enrichment.statcast_formulas import compute_split_block, filter_rows
from backend.export.enrichment.statcast_source import events_from_fixture

FIXTURES = Path(__file__).resolve().parent / "fixtures"

# Fixture Statcast / identity IDs (JSON numbers → Python int).
HITTER_AWAY = 7000001  # CWS; faces home SP
HITTER_AWAY_2 = 7000002
HITTER_HOME = 7000003  # TOR; faces away SP
HOME_SP = 702056
AWAY_SP = 680732
OTHER_PITCHER = 680000


def _events():
    return events_from_fixture(FIXTURES / "statcast_hitter_sample.json")


def _identity():
    schedule = json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8"))
    feeds = {822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))}
    return build_identity_layer(schedule, slate_date="2026-07-19", feeds_by_pk=feeds)


def _enrich(events, *, starter_map=None):
    identity = _identity()
    return build_hitter_enrichments(
        identity.players,
        events,
        opponent_starter_by_team=starter_map
        if starter_map is not None
        else _opponent_starter_map(identity.games, identity.lineups),
        opponent_team_by_player=_opponent_team_map(identity.teams, identity.players),
    )


def _hitter(result, player_id: int):
    return next(item for item in result.enrichments if item.player_id == player_id)


def _expected_bvp(events, batter_id: int, pitcher_id: int):
    rows = filter_rows(events, batter_id=batter_id, pitcher_id=pitcher_id)
    assert rows
    return compute_split_block(rows, split="overall")


def test_matching_pitcher_id_populates_bvp() -> None:
    events = _events()
    hitter = _hitter(_enrich(events), HITTER_AWAY)
    assert hitter.opponent_starter_id == HOME_SP
    block = hitter.splits.get("bvp")
    assert block is not None
    expected = _expected_bvp(events, HITTER_AWAY, HOME_SP)
    assert block.counts.pa == expected.counts.pa
    assert expected.counts.pa and expected.counts.pa > 0


def test_non_matching_pitcher_rows_excluded() -> None:
    events = _events()
    hitter = _hitter(_enrich(events), HITTER_AWAY)
    bvp = hitter.splits["bvp"]
    other = filter_rows(events, batter_id=HITTER_AWAY, pitcher_id=OTHER_PITCHER)
    own_sp = filter_rows(events, batter_id=HITTER_AWAY, pitcher_id=AWAY_SP)
    all_rows = filter_rows(events, batter_id=HITTER_AWAY)
    assert other
    assert own_sp
    assert bvp.counts.pa != compute_split_block(all_rows, split="overall").counts.pa
    assert bvp.counts.pa == _expected_bvp(events, HITTER_AWAY, HOME_SP).counts.pa


def test_missing_opponent_starter_id_leaves_bvp_absent() -> None:
    events = _events()
    hitter = _hitter(_enrich(events, starter_map={}), HITTER_AWAY)
    assert hitter.opponent_starter_id is None
    assert "bvp" not in hitter.splits


def test_starter_id_with_zero_matching_events_leaves_bvp_absent() -> None:
    events = _events()
    identity = _identity()
    starter_map = {
        (player.game_pk, player.team_id): 999999
        for player in identity.players
        if player.role == "lineup"
    }
    hitter = _hitter(_enrich(events, starter_map=starter_map), HITTER_AWAY)
    assert hitter.opponent_starter_id == 999999
    assert "bvp" not in hitter.splits
    assert "overall" in hitter.splits


def test_mixed_pitchers_aggregate_only_selected_starter() -> None:
    events = [
        {"batter": HITTER_AWAY, "pitcher": HOME_SP, "events": "single", "p_throws": "R", "game_date": "2026-07-10"},
        {"batter": HITTER_AWAY, "pitcher": HOME_SP, "events": "strikeout", "p_throws": "R", "game_date": "2026-07-10"},
        {"batter": HITTER_AWAY, "pitcher": OTHER_PITCHER, "events": "home_run", "p_throws": "L", "game_date": "2026-07-10"},
        {"batter": HITTER_AWAY, "pitcher": AWAY_SP, "events": "double", "p_throws": "R", "game_date": "2026-07-10"},
    ]
    hitter = _hitter(_enrich(events), HITTER_AWAY)
    bvp = hitter.splits["bvp"]
    assert bvp.counts.pa == 2
    assert bvp.counts.h == 1
    assert bvp.counts.hr is None or bvp.counts.hr == 0
    overall = hitter.splits["overall"]
    assert overall.counts.pa == 4
    assert overall.counts.hr == 1


def test_existing_non_bvp_splits_remain_unchanged() -> None:
    events = _events()
    hitter = _hitter(_enrich(events), HITTER_AWAY)
    player_rows = filter_rows(events, batter_id=HITTER_AWAY)
    expected_overall = compute_split_block(player_rows, split="overall")
    expected_lhp = compute_split_block(filter_rows(player_rows, p_throws="L"), split="vs_lhp")
    expected_rhp = compute_split_block(filter_rows(player_rows, p_throws="R"), split="vs_rhp")
    assert hitter.splits["overall"].counts.pa == expected_overall.counts.pa
    assert hitter.splits["vs_lhp"].counts.pa == expected_lhp.counts.pa
    assert hitter.splits["vs_rhp"].counts.pa == expected_rhp.counts.pa
    assert hitter.splits["bvp"].counts.pa != expected_overall.counts.pa


def test_no_fabricated_bvp_values() -> None:
    events = _events()
    hitter = _hitter(_enrich(events), HITTER_HOME)
    assert hitter.opponent_starter_id == AWAY_SP
    expected = _expected_bvp(events, HITTER_HOME, AWAY_SP)
    bvp = hitter.splits["bvp"]
    assert bvp.counts.pa == expected.counts.pa
    assert bvp.counts.h == expected.counts.h
    assert bvp.rates.avg == expected.rates.avg
    vs_home_sp = filter_rows(events, batter_id=HITTER_HOME, pitcher_id=HOME_SP)
    assert vs_home_sp == []


def test_export_split_hitter_bvp_uses_existing_contract() -> None:
    layer = build_matchup_layer(
        json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8")),
        slate_date="2026-07-19",
        feeds_by_pk={822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))},
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )
    away = next(
        row
        for detail in layer.game_details
        if detail.away_splits
        for row in detail.away_splits
        if row.hitter
    )
    populated = [
        row
        for detail in layer.game_details
        for row in (detail.away_splits or []) + (detail.home_splits or [])
        if row.bvp is not None
    ]
    assert populated
    for row in populated:
        assert row.bvp.pa is not None and row.bvp.pa > 0
        assert row.overall.pa is not None
        assert row.bvp.pa <= row.overall.pa
    assert away.vs_lhp is not None
    assert away.vs_rhp is not None
