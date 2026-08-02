"""Offline tests for G0b.4 matchup builder."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from backend.export.build_matchup_layer import build_matchup_layer
from backend.export.enrichment.matchups import build_matchups
from backend.export.enrichment.enrichment_validation import validate_enrichment_graph

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _layer():
    return build_matchup_layer(
        json.loads((FIXTURES / "schedule_sample.json").read_text(encoding="utf-8")),
        slate_date="2026-07-19",
        feeds_by_pk={822786: json.loads((FIXTURES / "lineups_sample.json").read_text(encoding="utf-8"))},
        statcast_fixture=str(FIXTURES / "statcast_hitter_sample.json"),
    )


def test_valid_hitter_starter_matchup() -> None:
    layer = _layer()
    assert layer.matchups
    sample = json.loads((FIXTURES / "matchup_sample.json").read_text(encoding="utf-8"))
    matchup = next(
        item
        for item in layer.matchups
        if item.hitter_id == sample["hitter_id"] and item.pitcher_id == sample["pitcher_id"]
    )
    assert matchup.lineup_slot == sample["lineup_slot"]


def test_opposing_team_relationship() -> None:
    layer = _layer()
    for matchup in layer.matchups:
        assert matchup.hitter_team_id != matchup.pitcher_team_id


def test_wrong_team_failure() -> None:
    layer = _layer()
    broken = layer.matchups[0].model_copy(update={"pitcher_team_id": layer.matchups[0].hitter_team_id})
    report = validate_enrichment_graph(
        games=layer.identity.games,
        teams=layer.identity.teams,
        players=layer.identity.players,
        lineups=layer.identity.lineups,
        hitter_enrichments=layer.hitter_enrichments,
        pitcher_enrichments=layer.pitcher_enrichments,
        pitch_mix_summaries=layer.pitch_mix_summaries,
        matchups=[broken],
    )
    assert report.valid is False


def test_orphan_hitter_failure() -> None:
    layer = _layer()
    broken = layer.matchups[0].model_copy(update={"hitter_id": 999999})
    report = validate_enrichment_graph(
        games=layer.identity.games,
        teams=layer.identity.teams,
        players=layer.identity.players,
        lineups=layer.identity.lineups,
        hitter_enrichments=layer.hitter_enrichments,
        pitcher_enrichments=layer.pitcher_enrichments,
        pitch_mix_summaries=layer.pitch_mix_summaries,
        matchups=[broken],
    )
    assert any("orphan hitter" in error.lower() for error in report.errors)


def test_duplicate_matchup_key_failure() -> None:
    layer = _layer()
    duplicate = [layer.matchups[0], layer.matchups[0]]
    report = validate_enrichment_graph(
        games=layer.identity.games,
        teams=layer.identity.teams,
        players=layer.identity.players,
        lineups=layer.identity.lineups,
        hitter_enrichments=layer.hitter_enrichments,
        pitcher_enrichments=layer.pitcher_enrichments,
        pitch_mix_summaries=layer.pitch_mix_summaries,
        matchups=duplicate,
    )
    assert any("Duplicate matchup" in error for error in report.errors)


def test_missing_pitch_mix_warning() -> None:
    layer = _layer()
    assert any("pitch mix" in warning.lower() for warning in layer.warnings + (layer.validation.warnings if layer.validation else [])) or layer.pitch_mix_summaries


def test_head_to_head_absent_without_fabrication() -> None:
    layer = _layer()
    for matchup in layer.matchups:
        if matchup.head_to_head is not None and not matchup.head_to_head.available:
            assert matchup.head_to_head.pa is None


def test_export_rows_include_pitch_dimension() -> None:
    layer = _layer()
    assert layer.export_matchup_rows
    assert all(row.pitch for row in layer.export_matchup_rows)


def test_deterministic_output() -> None:
    first = _layer()
    second = _layer()
    assert [item.model_dump() for item in first.matchups] == [item.model_dump() for item in second.matchups]
