"""Orchestrate G0b.4 matchup and enrichment layer."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

from backend.export.build_identity_layer import IdentityLayerResult, build_identity_layer
from backend.export.daily_export_models import GameDetail, HitterRow
from backend.export.enrichment.enrichment_models import EnrichmentMatchup, HitterEnrichment, PitchMixSummary, PitcherEnrichment
from backend.export.enrichment.enrichment_validation import EnrichmentValidationReport, validate_enrichment_graph
from backend.export.enrichment.hitter_stats import HitterEnrichmentResult, build_hitter_enrichments
from backend.export.enrichment.matchups import MatchupBuildResult, apply_enrichment_to_game_details, build_matchups
from backend.export.enrichment.pitch_mix import PitchMixBuildResult, build_pitch_mix_summaries
from backend.export.enrichment.pitcher_stats import PitcherEnrichmentResult, build_pitcher_enrichments
from backend.export.enrichment.statcast_source import StatcastEvents, events_from_fixture, fetch_statcast_events
from backend.export.identity_models import ExportLineup, ExportPlayer, ExportTeam


@dataclass
class MatchupLayerResult:
    identity: IdentityLayerResult
    hitter_enrichments: list[HitterEnrichment] = field(default_factory=list)
    pitcher_enrichments: list[PitcherEnrichment] = field(default_factory=list)
    pitch_mix_summaries: list[PitchMixSummary] = field(default_factory=list)
    matchups: list[EnrichmentMatchup] = field(default_factory=list)
    export_matchup_rows: list[HitterRow] = field(default_factory=list)
    game_details: list[GameDetail] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    validation: EnrichmentValidationReport | None = None


def build_matchup_layer(
    schedule_json: dict[str, Any],
    *,
    slate_date: str,
    feeds_by_pk: dict[int, dict] | None = None,
    statcast_events: StatcastEvents | None = None,
    statcast_fixture: str | None = None,
    lookback_days: int = 120,
) -> MatchupLayerResult:
    identity = build_identity_layer(
        schedule_json,
        slate_date=slate_date,
        feeds_by_pk=feeds_by_pk,
    )

    events = statcast_events
    if events is None and statcast_fixture:
        from pathlib import Path

        events = events_from_fixture(Path(statcast_fixture))
    if events is None:
        events = fetch_statcast_events(slate_date, lookback_days=lookback_days)

    window_end = slate_date
    window_start = (date.fromisoformat(slate_date) - timedelta(days=lookback_days)).isoformat()

    opponent_team_by_player = _opponent_team_map(identity.teams, identity.players)
    opponent_starter_by_team = _opponent_starter_map(identity.games, identity.lineups)

    hitter_result: HitterEnrichmentResult = build_hitter_enrichments(
        identity.players,
        events,
        opponent_starter_by_team=opponent_starter_by_team,
        opponent_team_by_player=opponent_team_by_player,
    )
    pitcher_result: PitcherEnrichmentResult = build_pitcher_enrichments(
        identity.players,
        events,
        opponent_team_by_player=opponent_team_by_player,
    )

    starter_ids = _starter_pitcher_ids(identity.players, identity.lineups)
    pitch_mix_result: PitchMixBuildResult = build_pitch_mix_summaries(
        pitcher_ids=starter_ids,
        events=events,
        window_start=window_start,
        window_end=window_end,
    )

    enriched_details = apply_enrichment_to_game_details(
        identity.game_details,
        hitter_enrichments=hitter_result.enrichments,
        pitch_mix_summaries=pitch_mix_result.summaries,
        players=identity.players,
        lineups=identity.lineups,
        events=events,
    )

    matchup_result: MatchupBuildResult = build_matchups(
        games=identity.games,
        game_details=enriched_details,
        teams=identity.teams,
        players=identity.players,
        lineups=identity.lineups,
        hitter_enrichments=hitter_result.enrichments,
        pitcher_enrichments=pitcher_result.enrichments,
        pitch_mix_summaries=pitch_mix_result.summaries,
        events=events,
    )

    warnings = _dedupe(
        identity.warnings
        + hitter_result.warnings
        + pitcher_result.warnings
        + pitch_mix_result.warnings
        + matchup_result.warnings
    )

    validation = validate_enrichment_graph(
        games=identity.games,
        teams=identity.teams,
        players=identity.players,
        lineups=identity.lineups,
        hitter_enrichments=hitter_result.enrichments,
        pitcher_enrichments=pitcher_result.enrichments,
        pitch_mix_summaries=pitch_mix_result.summaries,
        matchups=matchup_result.matchups,
        builder_warnings=warnings,
    )

    return MatchupLayerResult(
        identity=identity,
        hitter_enrichments=hitter_result.enrichments,
        pitcher_enrichments=pitcher_result.enrichments,
        pitch_mix_summaries=pitch_mix_result.summaries,
        matchups=matchup_result.matchups,
        export_matchup_rows=matchup_result.export_rows,
        game_details=enriched_details,
        warnings=warnings,
        validation=validation,
    )


def _opponent_team_map(
    teams: list[ExportTeam],
    players: list[ExportPlayer],
) -> dict[tuple[int, int], int]:
    team_side_by_game: dict[tuple[int, int], str] = {
        (team.game_pk, team.team_id): team.side for team in teams
    }
    game_sides = {}
    for team in teams:
        game_sides.setdefault(team.game_pk, {})[team.side] = team.team_id

    mapping: dict[tuple[int, int], int] = {}
    for player in players:
        side = team_side_by_game.get((player.game_pk, player.team_id))
        if side is None:
            continue
        other_side = "home" if side == "away" else "away"
        opponent_team_id = game_sides.get(player.game_pk, {}).get(other_side)
        if opponent_team_id is not None:
            mapping[(player.game_pk, player.player_id)] = opponent_team_id
    return mapping


def _opponent_starter_map(
    games,
    lineups: list[ExportLineup],
) -> dict[tuple[int, int], int | None]:
    lineup_starters: dict[tuple[int, int], int | None] = {}
    for lineup in lineups:
        if lineup.starting_pitcher_id is not None:
            lineup_starters[(lineup.game_pk, lineup.team_id)] = lineup.starting_pitcher_id

    mapping: dict[tuple[int, int], int | None] = {}
    for game in games:
        if game.game_pk is None:
            continue
        home_team_lineup = next(
            (lineup for lineup in lineups if lineup.game_pk == game.game_pk and lineup.side == "home"),
            None,
        )
        away_team_lineup = next(
            (lineup for lineup in lineups if lineup.game_pk == game.game_pk and lineup.side == "away"),
            None,
        )
        if home_team_lineup:
            mapping[(game.game_pk, home_team_lineup.team_id)] = (
                away_team_lineup.starting_pitcher_id if away_team_lineup else game.away_sp_id
            )
        if away_team_lineup:
            mapping[(game.game_pk, away_team_lineup.team_id)] = (
                home_team_lineup.starting_pitcher_id if home_team_lineup else game.home_sp_id
            )
    return mapping


def _starter_pitcher_ids(
    players: list[ExportPlayer],
    lineups: list[ExportLineup],
) -> list[tuple[int, int]]:
    ids: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()
    for lineup in lineups:
        if lineup.starting_pitcher_id is not None:
            key = (lineup.game_pk, lineup.starting_pitcher_id)
            if key not in seen:
                seen.add(key)
                ids.append(key)
    for player in players:
        if player.is_actual_starter or player.is_probable_starter:
            key = (player.game_pk, player.player_id)
            if key not in seen:
                seen.add(key)
                ids.append(key)
    return ids


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
