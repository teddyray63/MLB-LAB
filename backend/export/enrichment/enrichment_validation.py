"""Relationship validation for G0b.4 enrichment graph."""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.export.daily_export_models import Game
from backend.export.enrichment.enrichment_models import EnrichmentMatchup, HitterEnrichment, PitchMixSummary, PitcherEnrichment
from backend.export.enrichment.pitch_mix import USAGE_TOLERANCE
from backend.export.identity_models import ExportLineup, ExportPlayer, ExportTeam


@dataclass
class EnrichmentValidationReport:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    counts: dict[str, int | float | str] = field(default_factory=dict)
    coverage: dict[str, float | int | str] = field(default_factory=dict)


def validate_enrichment_graph(
    *,
    games: list[Game],
    teams: list[ExportTeam],
    players: list[ExportPlayer],
    lineups: list[ExportLineup],
    hitter_enrichments: list[HitterEnrichment],
    pitcher_enrichments: list[PitcherEnrichment],
    pitch_mix_summaries: list[PitchMixSummary],
    matchups: list[EnrichmentMatchup],
    builder_warnings: list[str] | None = None,
) -> EnrichmentValidationReport:
    errors: list[str] = []
    warnings: list[str] = list(builder_warnings or [])

    game_pks = {game.game_pk for game in games if game.game_pk is not None}
    team_keys = {(team.game_pk, team.team_id) for team in teams}
    player_keys = {(player.game_pk, player.player_id) for player in players}
    lineup_slots: dict[tuple[int, str, int], int] = {}
    for lineup in lineups:
        for slot, player_id in enumerate(lineup.batting_order_player_ids, start=1):
            lineup_slots[(lineup.game_pk, lineup.side, player_id)] = slot

    seen_matchup_keys: set[tuple[int, int, int]] = set()
    orphan_references = 0
    duplicate_matchups = 0
    missing_stat_blocks = 0
    missing_starters = 0
    missing_pitch_mix = 0

    for item in hitter_enrichments:
        if item.game_pk not in game_pks:
            errors.append(f"Hitter enrichment orphan game_pk {item.game_pk}")
            orphan_references += 1
        if (item.game_pk, item.player_id) not in player_keys:
            errors.append(f"Hitter enrichment orphan player_id {item.player_id}")
            orphan_references += 1
        if item.season is None:
            missing_stat_blocks += 1
            warnings.append(f"Missing hitter stat block for player_id {item.player_id}")

    for item in pitcher_enrichments:
        if item.game_pk not in game_pks:
            errors.append(f"Pitcher enrichment orphan game_pk {item.game_pk}")
            orphan_references += 1
        if (item.game_pk, item.player_id) not in player_keys:
            errors.append(f"Pitcher enrichment orphan player_id {item.player_id}")
            orphan_references += 1
        if item.season is None:
            missing_stat_blocks += 1
            warnings.append(f"Missing pitcher stat block for player_id {item.player_id}")

    for summary in pitch_mix_summaries:
        if (summary.game_pk, summary.pitcher_id) not in player_keys:
            errors.append(f"Pitch mix orphan pitcher_id {summary.pitcher_id}")
            orphan_references += 1
        if not summary.entries:
            missing_pitch_mix += 1
        usage_total = sum(entry.usage_pct for entry in summary.entries)
        if summary.entries and abs(usage_total - 1.0) > USAGE_TOLERANCE:
            warnings.append(
                f"Pitch mix usage for pitcher {summary.pitcher_id} totals {usage_total:.3f}"
            )
        for entry in summary.entries:
            if entry.pitch_count < 0:
                errors.append(f"Negative pitch count for pitcher {summary.pitcher_id}")
            if entry.usage_pct < 0 or entry.usage_pct > 1.01:
                errors.append(f"Invalid usage_pct for pitcher {summary.pitcher_id} pitch {entry.pitch_code}")

    for matchup in matchups:
        key = (matchup.game_pk, matchup.hitter_id, matchup.pitcher_id)
        if key in seen_matchup_keys:
            errors.append(f"Duplicate matchup key {key}")
            duplicate_matchups += 1
        seen_matchup_keys.add(key)

        if matchup.game_pk not in game_pks:
            errors.append(f"Matchup orphan game_pk {matchup.game_pk}")
            orphan_references += 1
        if (matchup.game_pk, matchup.hitter_id) not in player_keys:
            errors.append(f"Matchup orphan hitter_id {matchup.hitter_id}")
            orphan_references += 1
        if (matchup.game_pk, matchup.pitcher_id) not in player_keys:
            errors.append(f"Matchup orphan pitcher_id {matchup.pitcher_id}")
            orphan_references += 1
        if (matchup.game_pk, matchup.hitter_team_id) not in team_keys:
            errors.append(f"Matchup orphan hitter team_id {matchup.hitter_team_id}")
            orphan_references += 1
        if (matchup.game_pk, matchup.pitcher_team_id) not in team_keys:
            errors.append(f"Matchup orphan pitcher team_id {matchup.pitcher_team_id}")
            orphan_references += 1
        if matchup.hitter_team_id == matchup.pitcher_team_id:
            errors.append(
                f"Matchup hitter/pitcher same team in game_pk {matchup.game_pk} "
                f"hitter={matchup.hitter_id} pitcher={matchup.pitcher_id}"
            )

        side = "home" if matchup.is_home_hitter else "away"
        expected_slot = lineup_slots.get((matchup.game_pk, side, matchup.hitter_id))
        if expected_slot is not None and matchup.lineup_slot != expected_slot:
            errors.append(
                f"Lineup slot mismatch for hitter {matchup.hitter_id} game_pk {matchup.game_pk}: "
                f"expected {expected_slot}, got {matchup.lineup_slot}"
            )
        if matchup.lineup_slot is None:
            warnings.append(f"Missing lineup slot for hitter {matchup.hitter_id} game_pk {matchup.game_pk}")

        if not matchup.pitch_codes:
            missing_pitch_mix += 1
            warnings.append(
                f"Missing pitch mix reference for matchup hitter {matchup.hitter_id} "
                f"game_pk {matchup.game_pk}"
            )

        if matchup.head_to_head is not None and not matchup.head_to_head.available:
            warnings.append(
                f"Head-to-head unavailable for hitter {matchup.hitter_id} "
                f"vs pitcher {matchup.pitcher_id}"
            )

        for block in (matchup.hitter_split_vs_pitcher_hand, matchup.pitcher_split_vs_hitter_side):
            if block is None:
                continue
            pa = block.counts.pa or 0
            if pa < 0:
                errors.append("Negative sample size in split block")
            for rate_name, value in block.rates.model_dump().items():
                if value is None:
                    continue
                if rate_name.endswith("_pct") and (value < 0 or value > 1.01):
                    errors.append(f"Rate out of range {rate_name}={value}")

    lineup_hitters = sum(1 for player in players if player.role == "lineup")
    hitters_enriched = sum(1 for item in hitter_enrichments if item.season is not None)
    starters_enriched = sum(1 for item in pitcher_enrichments if item.season is not None)
    pitch_types_found = sum(len(summary.entries) for summary in pitch_mix_summaries)

    counts = {
        "games": len(games),
        "lineups": len(lineups),
        "players": len(players),
        "matchups": len(matchups),
        "hitters_enriched": hitters_enriched,
        "starters_enriched": starters_enriched,
        "pitch_types_found": pitch_types_found,
        "missing_stat_blocks": missing_stat_blocks,
        "missing_starters": missing_starters,
        "missing_pitch_mix": missing_pitch_mix,
        "orphan_references": orphan_references,
        "duplicate_matchups": duplicate_matchups,
    }

    coverage = {
        "hitter_enrichment_pct": round((hitters_enriched / lineup_hitters * 100) if lineup_hitters else 0, 1),
        "starter_enrichment_pct": round(
            (starters_enriched / max(1, len(pitcher_enrichments)) * 100),
            1,
        ),
        "matchup_coverage_pct": round(
            (len(matchups) / max(1, lineup_hitters) * 100) if lineup_hitters else 0,
            1,
        ),
    }
    counts.update(coverage)

    return EnrichmentValidationReport(
        valid=not errors,
        errors=_dedupe(errors),
        warnings=_dedupe(warnings),
        counts=counts,
        coverage=coverage,
    )


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
