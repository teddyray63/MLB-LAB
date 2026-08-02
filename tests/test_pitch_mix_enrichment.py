"""Offline tests for G0b.4 pitch-mix enrichment."""

from __future__ import annotations

import json
from pathlib import Path

from backend.export.enrichment.pitch_mix import USAGE_TOLERANCE, build_pitch_mix_summaries, major_pitch_codes
from backend.export.enrichment.statcast_source import events_from_fixture

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _events():
    return events_from_fixture(FIXTURES / "statcast_hitter_sample.json")


def test_multiple_pitch_types() -> None:
    result = build_pitch_mix_summaries(
        pitcher_ids=[(822786, 702056)],
        events=_events(),
    )
    summary = result.summaries[0]
    codes = {entry.pitch_code for entry in summary.entries}
    assert "FF" in codes
    assert "SL" in codes


def test_unknown_pitch_code_visible() -> None:
    result = build_pitch_mix_summaries(
        pitcher_ids=[(822786, 702056)],
        events=_events(),
    )
    summary = result.summaries[0]
    unknown = next((entry for entry in summary.entries if entry.pitch_code == "XX"), None)
    assert unknown is not None
    assert "Unknown" in unknown.pitch_name


def test_usage_reconciliation() -> None:
    result = build_pitch_mix_summaries(
        pitcher_ids=[(822786, 702056)],
        events=_events(),
    )
    summary = result.summaries[0]
    total = sum(entry.usage_pct for entry in summary.entries)
    assert abs(total - 1.0) <= USAGE_TOLERANCE + 0.001


def test_missing_velocity() -> None:
    events = [{"pitcher": 702056, "pitch_type": "FF", "events": "ball", "description": "ball"}]
    result = build_pitch_mix_summaries(pitcher_ids=[(822786, 702056)], events=events)
    entry = result.summaries[0].entries[0]
    assert entry.avg_velocity is None


def test_small_sample_flag() -> None:
    events = [{"pitcher": 702056, "pitch_type": "FF", "events": "ball", "description": "ball"}]
    result = build_pitch_mix_summaries(pitcher_ids=[(822786, 702056)], events=events)
    assert result.summaries[0].small_sample is True


def test_major_pitch_codes_threshold() -> None:
    result = build_pitch_mix_summaries(
        pitcher_ids=[(822786, 702056)],
        events=_events(),
    )
    codes = major_pitch_codes(result.summaries[0])
    assert "FF" in codes


def test_deterministic_output() -> None:
    first = build_pitch_mix_summaries(pitcher_ids=[(822786, 702056)], events=_events())
    second = build_pitch_mix_summaries(pitcher_ids=[(822786, 702056)], events=_events())
    assert [item.model_dump() for item in first.summaries] == [item.model_dump() for item in second.summaries]
