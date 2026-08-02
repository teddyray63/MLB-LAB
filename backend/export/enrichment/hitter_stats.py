"""Build reproducible hitter enrichment from Statcast events."""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.export.enrichment.enrichment_models import HitterEnrichment, SplitBlock
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
class HitterEnrichmentResult:
    enrichments: list[HitterEnrichment] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def build_hitter_enrichments(
    players: list[ExportPlayer],
    events: StatcastEvents,
    *,
    opponent_starter_by_team: dict[tuple[int, int], int | None],
    opponent_team_by_player: dict[tuple[int, int], int],
    day_night_by_game: dict[int, str | None] | None = None,
) -> HitterEnrichmentResult:
    day_night_by_game = day_night_by_game or {}
    enrichments: list[HitterEnrichment] = []
    warnings: list[str] = []

    lineup_hitters = [player for player in players if player.role == "lineup"]
    for player in lineup_hitters:
        key = (player.game_pk, player.team_id)
        opponent_team_id = opponent_team_by_player.get((player.game_pk, player.player_id))
        if opponent_team_id is None:
            warnings.append(
                f"Missing opponent team for hitter {player.player_id} game_pk {player.game_pk}"
            )
            continue

        opponent_starter_id = opponent_starter_by_team.get((player.game_pk, opponent_team_id))
        player_rows = filter_rows(events, batter_id=player.player_id)
        if not player_rows:
            warnings.append(f"No Statcast events for hitter {player.player_id}")
            enrichments.append(
                HitterEnrichment(
                    player_id=player.player_id,
                    game_pk=player.game_pk,
                    team_id=player.team_id,
                    opponent_team_id=opponent_team_id,
                    opponent_starter_id=opponent_starter_id,
                    lineup_slot=player.lineup_slot,
                    bats=player.bats,
                    is_home=None,
                    day_night=day_night_by_game.get(player.game_pk),
                    warnings=["missing stat block"],
                )
            )
            continue

        season = compute_split_block(player_rows, split="overall")
        splits: dict[str, SplitBlock] = {"overall": season}

        for split_name, p_throws in (("vs_lhp", "L"), ("vs_rhp", "R")):
            split_rows = filter_rows(player_rows, p_throws=p_throws)
            if split_rows:
                splits[split_name] = compute_split_block(split_rows, split=split_name)  # type: ignore[arg-type]
            else:
                warnings.append(f"Missing {split_name} split for hitter {player.player_id}")

        for split_name, day_night in (("day", "D"), ("night", "N")):
            split_rows = filter_rows(player_rows, day_night=day_night)
            if split_rows:
                splits[split_name] = compute_split_block(split_rows, split=split_name)  # type: ignore[arg-type]

        recent: dict[str, SplitBlock] = {}
        for window_name, game_count in RECENT_WINDOWS.items():
            dates = recent_game_dates(player_rows, game_count)
            if not dates:
                continue
            window_rows = filter_rows(player_rows, game_dates=dates)
            if window_rows:
                recent[window_name] = compute_split_block(window_rows, split="overall")

        enrichments.append(
            HitterEnrichment(
                player_id=player.player_id,
                game_pk=player.game_pk,
                team_id=player.team_id,
                opponent_team_id=opponent_team_id,
                opponent_starter_id=opponent_starter_id,
                lineup_slot=player.lineup_slot,
                bats=player.bats,
                day_night=day_night_by_game.get(player.game_pk),
                season=season,
                splits=splits,
                recent=recent,
            )
        )

    return HitterEnrichmentResult(enrichments=enrichments, warnings=_dedupe(warnings))


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
