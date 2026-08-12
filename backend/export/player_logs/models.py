"""Internal player game-log models for G0b.7 builders."""

from __future__ import annotations

from typing import Literal

from backend.export.daily_export_models import GameLogEntry, _ExportModel

AppearanceType = Literal["start", "relief"]


class HitterGameLog(_ExportModel):
    player_id: int
    game_pk: int | None = None
    game_date: str
    team_id: int | None = None
    opponent_team_id: int | None = None
    home_away: Literal["home", "away"] | None = None
    lineup_slot: int | None = None
    pa: int | None = None
    ab: int | None = None
    r: int | None = None
    h: int | None = None
    doubles: int | None = None
    triples: int | None = None
    hr: int | None = None
    rbi: int | None = None
    bb: int | None = None
    so: int | None = None
    hbp: int | None = None
    sf: int | None = None
    sb: int | None = None
    cs: int | None = None
    singles: int | None = None
    total_bases: int | None = None
    avg: float | None = None
    obp: float | None = None
    slg: float | None = None
    ops: float | None = None
    avg_ev: float | None = None
    barrels: int | None = None
    game_result: str | None = None
    game_status: str | None = None


class PitcherGameLog(_ExportModel):
    player_id: int
    game_pk: int | None = None
    game_date: str
    team_id: int | None = None
    opponent_team_id: int | None = None
    home_away: Literal["home", "away"] | None = None
    appearance_type: AppearanceType | None = None
    is_start: bool | None = None
    is_relief: bool | None = None
    innings_pitched: str | None = None
    innings_pitched_decimal: float | None = None
    batters_faced: int | None = None
    hits: int | None = None
    runs: int | None = None
    earned_runs: int | None = None
    walks: int | None = None
    strikeouts: int | None = None
    home_runs: int | None = None
    pitches: int | None = None
    strikes: int | None = None
    decision: str | None = None
    game_result: str | None = None
    game_status: str | None = None


def hitter_log_to_export_entry(log: HitterGameLog) -> GameLogEntry:
    """Map internal hitter log to export GameLogEntry contract."""
    return GameLogEntry(
        date=log.game_date,
        pa=log.pa,
        hits=log.h,
        singles=log.singles,
        tb=log.total_bases,
        hr=log.hr,
        avg_ev=round(log.avg_ev, 1) if log.avg_ev is not None else None,
        barrels=log.barrels,
    )
