"""Build ID-safe enrichment matchups and export HitterRow projections."""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.export.daily_export_models import Game, GameDetail, GameHitter, HitterRow, LineupBatter, SplitHitter, SplitLine
from backend.export.enrichment.enrichment_models import EnrichmentMatchup, HeadToHeadSummary, HitterEnrichment, PitchMixSummary, PitcherEnrichment
from backend.export.enrichment.pitch_mix import major_pitch_codes, to_export_pitch_mix
from backend.export.enrichment.statcast_formulas import compute_split_block, filter_rows
from backend.export.enrichment.statcast_source import StatcastEvents
from backend.export.identity_models import ExportLineup, ExportPlayer, ExportTeam


@dataclass
class MatchupBuildResult:
    matchups: list[EnrichmentMatchup] = field(default_factory=list)
    export_rows: list[HitterRow] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def _matchup_effective_bats(hitter_bats: str | None, pitcher_throws: str | None) -> str | None:
    """Derive pregame platoon side for pitcher split selection only (DEC-009).

    Does not mutate inputs. Canonical switch-hitter identity remains ``S`` elsewhere.
    """
    if hitter_bats == "L":
        return "L"
    if hitter_bats == "R":
        return "R"
    if hitter_bats == "S":
        if pitcher_throws == "R":
            return "L"
        if pitcher_throws == "L":
            return "R"
    return None


def _pitcher_split_key(effective_bats: str | None) -> str | None:
    if effective_bats == "L":
        return "vs_lhb"
    if effective_bats == "R":
        return "vs_rhb"
    return None


def build_matchups(
    *,
    games: list[Game],
    game_details: list[GameDetail],
    teams: list[ExportTeam],
    players: list[ExportPlayer],
    lineups: list[ExportLineup],
    hitter_enrichments: list[HitterEnrichment],
    pitcher_enrichments: list[PitcherEnrichment],
    pitch_mix_summaries: list[PitchMixSummary],
    events: StatcastEvents,
) -> MatchupBuildResult:
    games_by_pk = {game.game_pk: game for game in games if game.game_pk is not None}
    players_by_key = {(player.game_pk, player.player_id): player for player in players}
    teams_by_key = {(team.game_pk, team.team_id): team for team in teams}
    lineups_by_key = {(lineup.game_pk, lineup.side): lineup for lineup in lineups}
    hitters_by_key = {(item.game_pk, item.player_id): item for item in hitter_enrichments}
    pitchers_by_key = {(item.game_pk, item.player_id): item for item in pitcher_enrichments}
    mix_by_key = {(item.game_pk, item.pitcher_id): item for item in pitch_mix_summaries}

    matchups: list[EnrichmentMatchup] = []
    export_rows: list[HitterRow] = []
    warnings: list[str] = []

    for detail in game_details:
        if detail.game_pk is None:
            continue
        game = games_by_pk.get(detail.game_pk)
        if game is None:
            warnings.append(f"Missing game record for game_pk {detail.game_pk}")
            continue

        for side, hitter_lineup, pitcher_lineup, opp_sp_id_field in (
            ("away", detail.away_lineup, lineups_by_key.get((detail.game_pk, "home")), game.home_sp_id),
            ("home", detail.home_lineup, lineups_by_key.get((detail.game_pk, "away")), game.away_sp_id),
        ):
            if not hitter_lineup:
                warnings.append(f"Missing lineup for game_pk {detail.game_pk} side {side}")
                continue

            opposing_starter_id = _resolve_opposing_starter(
                pitcher_lineup,
                opp_sp_id_field,
                players_by_key,
                detail.game_pk,
            )
            if opposing_starter_id is None:
                warnings.append(f"Absent starter for game_pk {detail.game_pk} side {side}")
                continue

            opposing_pitcher = players_by_key.get((detail.game_pk, opposing_starter_id))
            if opposing_pitcher is None:
                warnings.append(
                    f"Orphan opposing starter {opposing_starter_id} for game_pk {detail.game_pk}"
                )
                continue

            pitch_mix = mix_by_key.get((detail.game_pk, opposing_starter_id))
            pitch_codes = major_pitch_codes(pitch_mix) if pitch_mix else []
            if not pitch_codes:
                warnings.append(
                    f"Missing pitch mix for opposing starter {opposing_starter_id} game_pk {detail.game_pk}"
                )

            for batter in hitter_lineup:
                hitter_player = _find_player_by_name(detail.game_pk, batter.hitter, players_by_key)
                if hitter_player is None:
                    warnings.append(
                        f"Orphan lineup hitter {batter.hitter!r} in game_pk {detail.game_pk} side {side}"
                    )
                    continue

                hitter_team = teams_by_key.get((detail.game_pk, hitter_player.team_id))
                pitcher_team = teams_by_key.get((detail.game_pk, opposing_pitcher.team_id))
                if hitter_team is None or pitcher_team is None:
                    warnings.append(f"Missing team reference for matchup game_pk {detail.game_pk}")
                    continue
                if hitter_team.team_id == pitcher_team.team_id:
                    warnings.append(
                        f"Hitter {hitter_player.player_id} and pitcher {opposing_starter_id} "
                        f"share team in game_pk {detail.game_pk}"
                    )
                    continue

                hitter_enrichment = hitters_by_key.get((detail.game_pk, hitter_player.player_id))
                pitcher_enrichment = pitchers_by_key.get((detail.game_pk, opposing_starter_id))
                pitcher_hand = opposing_pitcher.throws
                hitter_hand = hitter_player.bats
                effective_bats = _matchup_effective_bats(hitter_hand, pitcher_hand)
                split_key = "vs_lhp" if pitcher_hand == "L" else "vs_rhp" if pitcher_hand == "R" else None
                hitter_split = (
                    hitter_enrichment.splits.get(split_key)
                    if hitter_enrichment and split_key
                    else None
                )
                pitcher_split_key = _pitcher_split_key(effective_bats)
                pitcher_split = (
                    pitcher_enrichment.splits.get(pitcher_split_key)
                    if pitcher_enrichment and pitcher_split_key
                    else None
                )

                h2h = _head_to_head(events, hitter_player.player_id, opposing_starter_id)

                matchup = EnrichmentMatchup(
                    game_pk=detail.game_pk,
                    hitter_id=hitter_player.player_id,
                    pitcher_id=opposing_starter_id,
                    hitter_team_id=hitter_player.team_id,
                    pitcher_team_id=opposing_pitcher.team_id,
                    lineup_slot=batter.order,
                    hitter_bats=hitter_hand,
                    matchup_effective_bats=effective_bats,
                    pitcher_throws=pitcher_hand,
                    is_home_hitter=side == "home",
                    hitter_split_vs_pitcher_hand=hitter_split,
                    pitcher_split_vs_hitter_side=pitcher_split,
                    pitch_mix_pitcher_id=opposing_starter_id,
                    pitch_codes=pitch_codes,
                    head_to_head=h2h,
                    warnings=(["head-to-head unavailable"] if not h2h.available else []),
                )
                matchups.append(matchup)

                if not pitch_codes:
                    continue

                for pitch_code in pitch_codes:
                    export_rows.append(
                        _to_hitter_row(
                            game=game,
                            detail=detail,
                            hitter_player=hitter_player,
                            opposing_pitcher=opposing_pitcher,
                            pitch_code=pitch_code,
                            events=events,
                        )
                    )

    return MatchupBuildResult(matchups=matchups, export_rows=export_rows, warnings=_dedupe(warnings))


def apply_enrichment_to_game_details(
    game_details: list[GameDetail],
    *,
    hitter_enrichments: list[HitterEnrichment],
    pitch_mix_summaries: list[PitchMixSummary],
    players: list[ExportPlayer],
    lineups: list[ExportLineup],
    events: StatcastEvents,
) -> list[GameDetail]:
    players_by_key = {(player.game_pk, player.player_id): player for player in players}
    hitters_by_key = {(item.game_pk, item.player_id): item for item in hitter_enrichments}
    mix_by_key = {(item.game_pk, item.pitcher_id): item for item in pitch_mix_summaries}
    lineups_by_key = {(lineup.game_pk, lineup.side): lineup for lineup in lineups}

    updated: list[GameDetail] = []
    for detail in game_details:
        if detail.game_pk is None:
            updated.append(detail)
            continue

        away_mix = _side_pitch_mix(
            detail.game_pk, "away", players_by_key, mix_by_key, lineups_by_key
        )
        home_mix = _side_pitch_mix(
            detail.game_pk, "home", players_by_key, mix_by_key, lineups_by_key
        )

        away_lineup = _enrich_lineup(detail.away_lineup, detail.game_pk, hitters_by_key)
        home_lineup = _enrich_lineup(detail.home_lineup, detail.game_pk, hitters_by_key)

        away_lineup_model = lineups_by_key.get((detail.game_pk, "away"))
        home_lineup_model = lineups_by_key.get((detail.game_pk, "home"))
        away_splits = _build_split_hitters(
            detail.away_lineup,
            detail.game_pk,
            detail.home_sp,
            hitters_by_key,
            events,
            team_id=away_lineup_model.team_id if away_lineup_model else None,
        )
        home_splits = _build_split_hitters(
            detail.home_lineup,
            detail.game_pk,
            detail.away_sp,
            hitters_by_key,
            events,
            team_id=home_lineup_model.team_id if home_lineup_model else None,
        )

        away_hitters = _build_game_hitter_pool(detail.game_pk, "away", players_by_key, events)
        home_hitters = _build_game_hitter_pool(detail.game_pk, "home", players_by_key, events)

        updated.append(
            detail.model_copy(
                update={
                    "away_pitch_mix": away_mix,
                    "home_pitch_mix": home_mix,
                    "away_lineup": away_lineup,
                    "home_lineup": home_lineup,
                    "away_splits": away_splits or None,
                    "home_splits": home_splits or None,
                    "away_hitters": away_hitters,
                    "home_hitters": home_hitters,
                }
            )
        )
    return updated


def _resolve_opposing_starter(
    opposing_lineup: ExportLineup | None,
    schedule_sp_id: int | None,
    players_by_key: dict[tuple[int, int], ExportPlayer],
    game_pk: int,
) -> int | None:
    if opposing_lineup and opposing_lineup.starting_pitcher_id is not None:
        return opposing_lineup.starting_pitcher_id
    if schedule_sp_id is not None and (game_pk, schedule_sp_id) in players_by_key:
        return schedule_sp_id
    return None


def _find_player_by_name(
    game_pk: int,
    name: str,
    players_by_key: dict[tuple[int, int], ExportPlayer],
) -> ExportPlayer | None:
    for (pk, _), player in players_by_key.items():
        if pk == game_pk and player.full_name == name:
            return player
    return None


def _head_to_head(events: StatcastEvents, hitter_id: int, pitcher_id: int) -> HeadToHeadSummary:
    rows = filter_rows(events, batter_id=hitter_id, pitcher_id=pitcher_id)
    if not rows:
        return HeadToHeadSummary(hitter_id=hitter_id, pitcher_id=pitcher_id, available=False)
    block = compute_split_block(rows, split="overall")
    return HeadToHeadSummary(
        hitter_id=hitter_id,
        pitcher_id=pitcher_id,
        pa=block.counts.pa,
        ab=block.counts.ab,
        h=block.counts.h,
        hr=block.counts.hr,
        bb=block.counts.bb,
        so=block.counts.so,
        avg=block.rates.avg,
        available=True,
    )


def _to_hitter_row(
    *,
    game: Game,
    detail: GameDetail,
    hitter_player: ExportPlayer,
    opposing_pitcher: ExportPlayer,
    pitch_code: str,
    events: StatcastEvents,
) -> HitterRow:
    rows = filter_rows(
        events,
        batter_id=hitter_player.player_id,
        pitch_type=pitch_code,
    )
    block = compute_split_block(rows, split="overall")
    team = _team_name_for_player(detail, hitter_player)

    return HitterRow(
        hitter=hitter_player.full_name,
        team=team,
        game=game.game_id,
        game_pk=game.game_pk,
        opp_sp=opposing_pitcher.full_name,
        pitch=pitch_code,
        pa=block.counts.pa,
        hits=block.counts.h,
        singles=block.counts.singles,
        tb=block.counts.tb,
        avg=block.rates.avg,
        slg=block.rates.slg,
        iso=block.rates.iso,
        woba=block.rates.woba,
        xwoba=block.rates.xwoba,
        barrel_pct=block.rates.barrel_pct,
        hard_hit_pct=block.rates.hard_hit_pct,
        whiff_pct=block.rates.whiff_pct,
        xba=None,
        xslg=None,
        sweet_spot_pct=None,
        bat_speed=None,
        squared_up_pct=None,
        blast_pct=None,
        bat_tracking_low_confidence=None,
        near_hr=None,
    )


def _team_name_for_player(detail: GameDetail, player: ExportPlayer) -> str:
    # Without cross-game team map, infer from lineup side membership
    if detail.away_lineup and any(row.hitter == player.full_name for row in detail.away_lineup):
        return detail.away_team
    if detail.home_lineup and any(row.hitter == player.full_name for row in detail.home_lineup):
        return detail.home_team
    return detail.away_team


def _side_pitch_mix(
    game_pk: int,
    side: str,
    players_by_key: dict[tuple[int, int], ExportPlayer],
    mix_by_key: dict[tuple[int, int], PitchMixSummary],
    lineups_by_key: dict[tuple[int, str], ExportLineup] | None = None,
) -> list:
    lineups_by_key = lineups_by_key or {}
    lineup = lineups_by_key.get((game_pk, side))
    if lineup and lineup.starting_pitcher_id is not None:
        summary = mix_by_key.get((game_pk, lineup.starting_pitcher_id))
        if summary:
            return to_export_pitch_mix(summary)
    for (pk, player_id), player in players_by_key.items():
        if pk == game_pk and player.is_actual_starter:
            summary = mix_by_key.get((game_pk, player_id))
            if summary:
                return to_export_pitch_mix(summary)
    return []


def _enrich_lineup(
    lineup: list[LineupBatter] | None,
    game_pk: int,
    hitters_by_key: dict[tuple[int, int], HitterEnrichment],
) -> list[LineupBatter] | None:
    if not lineup:
        return None
    enriched: list[LineupBatter] = []
    for batter in lineup:
        enrichment = next(
            (
                item
                for (pk, _), item in hitters_by_key.items()
                if pk == game_pk and item.lineup_slot == batter.order
            ),
            None,
        )
        if enrichment is None or enrichment.season is None:
            enriched.append(batter)
            continue
        counts = enrichment.season.counts
        rates = enrichment.season.rates
        enriched.append(
            batter.model_copy(
                update={
                    "ab": counts.ab,
                    "hits": counts.h,
                    "hr": counts.hr,
                    "avg": rates.avg,
                    "slg": rates.slg,
                    "k_pct": rates.k_pct,
                    "barrel_pct": rates.barrel_pct,
                }
            )
        )
    return enriched


def _build_split_hitters(
    lineup: list[LineupBatter] | None,
    game_pk: int,
    opposing_sp_name: str,
    hitters_by_key: dict[tuple[int, int], HitterEnrichment],
    events: StatcastEvents,
    team_id: int | None = None,
) -> list[SplitHitter]:
    if not lineup:
        return []
    rows: list[SplitHitter] = []
    for batter in lineup:
        enrichment = next(
            (
                item
                for (pk, _pid), item in hitters_by_key.items()
                if pk == game_pk
                and item.lineup_slot == batter.order
                and (team_id is None or item.team_id == team_id)
            ),
            None,
        )
        if enrichment is None:
            continue
        overall = _split_line_from_block(enrichment.splits.get("overall"))
        vs_lhp = _split_line_from_block(enrichment.splits.get("vs_lhp"))
        vs_rhp = _split_line_from_block(enrichment.splits.get("vs_rhp"))
        day_split = _split_line_from_block(enrichment.splits.get("day"))
        night_split = _split_line_from_block(enrichment.splits.get("night"))
        bvp = _split_line_from_block(enrichment.splits.get("bvp"))
        rows.append(
            SplitHitter(
                hitter=batter.hitter,
                bvp_pitcher=opposing_sp_name,
                overall=overall or SplitLine(),
                vs_lhp=vs_lhp or SplitLine(),
                vs_rhp=vs_rhp or SplitLine(),
                bvp=bvp,
                day_split=day_split,
                night_split=night_split,
            )
        )
    return rows


def _split_line_from_block(block) -> SplitLine | None:
    if block is None:
        return None
    return SplitLine(
        pa=block.counts.pa,
        ab=block.counts.ab,
        hits=block.counts.h,
        hr=block.counts.hr,
        avg=block.rates.avg,
        slg=block.rates.slg,
        iso=block.rates.iso,
        woba=block.rates.woba,
        k_pct=block.rates.k_pct,
        bb_pct=block.rates.bb_pct,
        hard_hit_pct=block.rates.hard_hit_pct,
        barrel_pct=block.rates.barrel_pct,
        small_sample=block.small_sample,
    )


def _build_game_hitter_pool(
    game_pk: int,
    side: str,
    players_by_key: dict[tuple[int, int], ExportPlayer],
    events: StatcastEvents,
) -> list[GameHitter]:
    pool: list[GameHitter] = []
    for (pk, player_id), player in players_by_key.items():
        if pk != game_pk or player.role != "lineup":
            continue
        rows = filter_rows(events, batter_id=player_id)
        if not rows:
            continue
        block = compute_split_block(rows, split="overall")
        pool.append(
            GameHitter(
                hitter=player.full_name,
                pa=block.counts.pa,
                avg=block.rates.avg,
                slg=block.rates.slg,
                iso=block.rates.iso,
                woba=block.rates.woba,
                xwoba=block.rates.xwoba,
                barrel_pct=block.rates.barrel_pct,
                hard_hit_pct=block.rates.hard_hit_pct,
            )
        )
    pool.sort(key=lambda row: row.pa or 0, reverse=True)
    return pool[:12]


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
