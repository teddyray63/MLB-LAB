"""Build reproducible starting-pitcher enrichment from Statcast events."""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.export.enrichment.enrichment_models import PitcherEnrichment, SplitBlock
from backend.export.enrichment.statcast_formulas import compute_split_block, filter_rows, recent_game_dates
from backend.export.enrichment.statcast_source import StatcastEvents
from backend.export.identity_models import ExportPlayer

RECENT_WINDOWS: dict[str, int] = {
    "last_20": 20,
    "last_15": 15,
    "last_10": 10,
    "last_7": 7,
    "last_5": 5,
}


@dataclass
class PitcherEnrichmentResult:
    enrichments: list[PitcherEnrichment] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def build_pitcher_enrichments(
    players: list[ExportPlayer],
    events: StatcastEvents,
    *,
    opponent_team_by_player: dict[tuple[int, int], int],
    day_night_by_game: dict[int, str | None] | None = None,
) -> PitcherEnrichmentResult:
    day_night_by_game = day_night_by_game or {}
    enrichments: list[PitcherEnrichment] = []
    warnings: list[str] = []

    starter_roles = {"starting_pitcher", "probable_starter"}
    candidate_starters = [
        player
        for player in players
        if player.role in starter_roles or player.is_actual_starter or player.is_probable_starter
    ]
    seen: set[tuple[int, int]] = set()

    for player in candidate_starters:
        key = (player.game_pk, player.player_id)
        if key in seen:
            continue
        seen.add(key)

        if not (player.is_actual_starter or player.is_probable_starter or player.role == "starting_pitcher"):
            continue

        opponent_team_id = opponent_team_by_player.get((player.game_pk, player.player_id))
        if opponent_team_id is None:
            warnings.append(
                f"Missing opponent team for pitcher {player.player_id} game_pk {player.game_pk}"
            )
            continue

        pitcher_rows = filter_rows(events, pitcher_id=player.player_id)
        if not pitcher_rows:
            warnings.append(f"Missing starter stat block for pitcher {player.player_id}")
            enrichments.append(
                PitcherEnrichment(
                    player_id=player.player_id,
                    game_pk=player.game_pk,
                    team_id=player.team_id,
                    opponent_team_id=opponent_team_id,
                    throws=player.throws,
                    is_probable_starter=player.is_probable_starter,
                    is_actual_starter=player.is_actual_starter,
                    warnings=["missing stat block"],
                )
            )
            continue

        season = compute_split_block(pitcher_rows, split="overall")
        splits: dict[str, SplitBlock] = {"overall": season}

        for split_name, stand in (("vs_lhb", "L"), ("vs_rhb", "R")):
            split_rows = filter_rows(pitcher_rows, stand=stand)
            if split_rows:
                splits[split_name] = compute_split_block(split_rows, split=split_name)  # type: ignore[arg-type]

        for split_name, day_night in (("day", "D"), ("night", "N")):
            split_rows = filter_rows(pitcher_rows, day_night=day_night)
            if split_rows:
                splits[split_name] = compute_split_block(split_rows, split=split_name)  # type: ignore[arg-type]

        recent: dict[str, SplitBlock] = {}
        for window_name, game_count in RECENT_WINDOWS.items():
            dates = recent_game_dates(pitcher_rows, game_count)
            if not dates:
                continue
            window_rows = filter_rows(pitcher_rows, game_dates=dates)
            if window_rows:
                recent[window_name] = compute_split_block(window_rows, split="overall")

        enrichments.append(
            PitcherEnrichment(
                player_id=player.player_id,
                game_pk=player.game_pk,
                team_id=player.team_id,
                opponent_team_id=opponent_team_id,
                throws=player.throws,
                is_probable_starter=player.is_probable_starter,
                is_actual_starter=player.is_actual_starter,
                season=season,
                splits=splits,
                recent=recent,
                warnings=(
                    ["probable starter differs from actual starter"]
                    if player.is_probable_starter
                    and player.is_actual_starter
                    and player.is_probable_starter != player.is_actual_starter
                    else []
                ),
            )
        )

    missing_starters = [
        player
        for player in players
        if player.is_probable_starter or player.is_actual_starter
    ]
    enriched_ids = {(item.game_pk, item.player_id) for item in enrichments}
    for player in missing_starters:
        if (player.game_pk, player.player_id) not in enriched_ids:
            warnings.append(
                f"Missing starter enrichment for pitcher {player.player_id} game_pk {player.game_pk}"
            )

    return PitcherEnrichmentResult(enrichments=enrichments, warnings=_dedupe(warnings))


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
