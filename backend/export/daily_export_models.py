"""Pydantic models for data/daily_export.json — mirrors web-dashboard/src/types/slate.ts."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator

PlayCategory = Literal["hits", "singles", "total_bases", "hrr", "home_runs"]
Tier = Literal["T1", "T2", "T3"]
LineupSource = Literal["override", "projected", "empty"]

# ---------------------------------------------------------------------------
# Schema constants
# ---------------------------------------------------------------------------

DAILY_EXPORT_SCHEMA_VERSION = 1
EXPORT_RUNNER_VERSION = "3.0.0-g0b"

PLAY_CATEGORIES: tuple[PlayCategory, ...] = (
    "hits",
    "singles",
    "total_bases",
    "hrr",
    "home_runs",
)

# ---------------------------------------------------------------------------
# Field classification registry (required / optional / nullable / deprecated /
# currently unreproducible). Keys are dotted paths relative to DailyExport.
# ---------------------------------------------------------------------------

FIELD_CLASSIFICATION: dict[str, str] = {
    "date": "required",
    "schema_version": "optional",
    "export_meta": "optional",
    "export_meta.generated_at": "required when export_meta present",
    "export_meta.statcast_start": "required when export_meta present",
    "export_meta.statcast_end": "required when export_meta present",
    "export_meta.runner_version": "required when export_meta present",
    "export_meta.warnings": "required when export_meta present",
    "games": "required",
    "games[].game_id": "required",
    "games[].game_pk": "optional nullable",
    "games[].away_sp_id": "required nullable",
    "games[].home_sp_id": "required nullable",
    "game_details": "required",
    "matchups": "required",
    "top_plays": "required",
    "category_boards": "required",
    "player_logs": "optional",
    "batted_balls": "optional",
    "batted_ball_profiles": "optional",
    "player_day_night_splits": "optional",
    "player_zone_heatmaps": "optional",
    "matchups[].bat_speed": "optional nullable unreproducible",
    "matchups[].squared_up_pct": "optional nullable unreproducible",
    "matchups[].blast_pct": "optional nullable unreproducible",
    "matchups[].bat_tracking_low_confidence": "optional unreproducible",
    "matchups[].near_hr": "optional nullable unreproducible",
    "matchups[].xba": "optional nullable unreproducible",
    "matchups[].xslg": "optional nullable unreproducible",
    "matchups[].sweet_spot_pct": "optional nullable unreproducible",
    "top_plays[].score": "required unreproducible",
    "top_plays[].tier": "required unreproducible",
    "game_details[].away_splits": "optional unreproducible",
    "game_details[].home_splits": "optional unreproducible",
    "game_details[].context": "optional unreproducible",
    "game_details[].away_sp_situation": "optional unreproducible",
    "game_details[].home_sp_inning_splits": "optional unreproducible",
    "player_zone_heatmaps": "optional unreproducible",
    "player_day_night_splits": "optional unreproducible",
}


class _ExportModel(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)


# ---------------------------------------------------------------------------
# Shared nested types
# ---------------------------------------------------------------------------


class ExportMeta(_ExportModel):
    generated_at: str
    statcast_start: str
    statcast_end: str
    runner_version: str
    warnings: list[str] = Field(default_factory=list)


class ParkFactors(_ExportModel):
    run_factor: float | None = None
    hit_factor: float | None = None
    hr_factor: float | None = None


class Game(_ExportModel):
    game_id: str
    away_team: str
    home_team: str
    away_sp: str
    home_sp: str
    away_sp_id: int | None
    home_sp_id: int | None
    game_pk: int | None = None
    start_time_utc: str | None = None
    status: str | None = None
    venue: str | None = None


class TopPlay(_ExportModel):
    rank: int
    hitter: str
    team: str
    game: str
    opp_sp: str
    pitch: str
    score: float
    tier: Tier
    key_stat: str
    key_val: float | int | str | None = None
    game_pk: int | None = None


class HitterRow(_ExportModel):
    hitter: str
    team: str
    game: str
    opp_sp: str
    pitch: str
    pa: int | None = None
    hits: int | None = None
    singles: int | None = None
    tb: int | None = None
    avg: float | None = None
    slg: float | None = None
    iso: float | None = None
    woba: float | None = None
    xwoba: float | None = None
    xba: float | None = None
    xslg: float | None = None
    sweet_spot_pct: float | None = None
    barrel_pct: float | None = None
    hard_hit_pct: float | None = None
    whiff_pct: float | None = None
    bat_speed: float | None = None
    squared_up_pct: float | None = None
    blast_pct: float | None = None
    bat_tracking_low_confidence: bool | None = None
    near_hr: int | None = None
    game_pk: int | None = None


class GameHitter(_ExportModel):
    hitter: str
    pa: int | None = None
    avg: float | None = None
    slg: float | None = None
    iso: float | None = None
    woba: float | None = None
    xwoba: float | None = None
    xba: float | None = None
    xslg: float | None = None
    sweet_spot_pct: float | None = None
    barrel_pct: float | None = None
    hard_hit_pct: float | None = None
    bat_speed: float | None = None
    squared_up_pct: float | None = None
    blast_pct: float | None = None
    bat_tracking_low_confidence: bool | None = None


class BullpenAppearance(_ExportModel):
    reliever: str
    date: str
    ip: str | float | int | None = None
    pitches: int | None = None
    flagged: bool


class PitchMixEntry(_ExportModel):
    pitch: str
    usage_pct: float | None = None


PitchMixItem = Annotated[PitchMixEntry | str, Field(discriminator=None)]


class TeamRecord(_ExportModel):
    wins: int | None = None
    losses: int | None = None
    pct: str | None = None


class GameWeather(_ExportModel):
    condition: str | None = None
    temp: str | None = None
    wind: str | None = None


class RecentGame(_ExportModel):
    date: str
    opponent: str
    result: str
    score: str
    is_home: bool


class GameContext(_ExportModel):
    away_record: TeamRecord | None = None
    home_record: TeamRecord | None = None
    weather: GameWeather | None = None
    away_last5: list[RecentGame] = Field(default_factory=list)
    home_last5: list[RecentGame] = Field(default_factory=list)
    park: str | None = None
    park_factors: ParkFactors | None = None


class PitcherSituationLine(_ExportModel):
    split: str
    ip: float | None = None
    ra9: float | None = None
    whip: float | None = None
    oba: float | None = None
    iso: float | None = None
    k_pct: float | None = None
    k9: float | None = None
    hr9: float | None = None
    barrel_pct: float | None = None


class PitcherPlatoonLine(_ExportModel):
    split: str
    bf: int | None = None
    hr: int | None = None
    singles: int | None = None
    doubles: int | None = None
    triples: int | None = None
    bb: int | None = None
    oba: float | None = None
    slg: float | None = None
    iso: float | None = None
    barrel_pct: float | None = None
    hard_hit_pct: float | None = None
    k_pct: float | None = None


class LineupBatter(_ExportModel):
    order: int
    hitter: str
    hand: str | None = None
    status: str | None = None
    ab: int | None = None
    hits: int | None = None
    hr: int | None = None
    avg: float | None = None
    slg: float | None = None
    k_pct: float | None = None
    barrel_pct: float | None = None
    bat_speed: float | None = None
    squared_up_pct: float | None = None
    blast_pct: float | None = None
    bat_tracking_low_confidence: bool | None = None


class SplitLine(_ExportModel):
    pa: int | None = None
    ab: int | None = None
    hits: int | None = None
    hr: int | None = None
    avg: float | None = None
    slg: float | None = None
    iso: float | None = None
    woba: float | None = None
    babip: float | None = None
    k_pct: float | None = None
    bb_pct: float | None = None
    hard_hit_pct: float | None = None
    barrel_pct: float | None = None
    small_sample: bool | None = None
    bat_speed: float | None = None
    squared_up_pct: float | None = None
    blast_pct: float | None = None
    bat_tracking_low_confidence: bool | None = None


class HitterFullSplitLine(SplitLine):
    xwoba: float | None = None
    xba: float | None = None
    xslg: float | None = None
    sweet_spot_pct: float | None = None
    whiff_pct: float | None = None


class HitterDayNightProfile(_ExportModel):
    overall: HitterFullSplitLine
    day_split: HitterFullSplitLine
    night_split: HitterFullSplitLine


class PitcherDayNightSplit(_ExportModel):
    ip: float | None = None
    ra9: float | None = None
    whip: float | None = None
    oba: float | None = None
    iso: float | None = None
    k_pct: float | None = None
    k9: float | None = None
    hr9: float | None = None
    barrel_pct: float | None = None
    bf: int | None = None
    small_sample: bool | None = None


class PitcherDayNightProfile(_ExportModel):
    day_split: PitcherDayNightSplit
    night_split: PitcherDayNightSplit


class SplitHitter(_ExportModel):
    hitter: str
    bvp_pitcher: str
    overall: SplitLine
    vs_lhp: SplitLine
    vs_rhp: SplitLine
    bvp: SplitLine | None = None
    day_split: SplitLine | None = None
    night_split: SplitLine | None = None


class SpInningStart(_ExportModel):
    date: str
    game_pk: int
    f1: float | None = None
    f3: float | None = None
    f5: float | None = None
    f7: float | None = None


class GameDetail(_ExportModel):
    game_id: str
    away_team: str
    home_team: str
    away_sp: str
    home_sp: str
    away_hitters: list[GameHitter]
    home_hitters: list[GameHitter]
    away_pitch_mix: list[PitchMixEntry | str]
    home_pitch_mix: list[PitchMixEntry | str]
    away_bullpen: list[BullpenAppearance]
    home_bullpen: list[BullpenAppearance]
    game_pk: int | None = None
    start_time_utc: str | None = None
    status: str | None = None
    venue: str | None = None
    away_splits: list[SplitHitter] | None = None
    home_splits: list[SplitHitter] | None = None
    away_lineup: list[LineupBatter] | None = None
    home_lineup: list[LineupBatter] | None = None
    away_lineup_source: LineupSource | None = None
    home_lineup_source: LineupSource | None = None
    away_sp_situation: list[PitcherSituationLine] | None = None
    home_sp_situation: list[PitcherSituationLine] | None = None
    away_sp_platoon: list[PitcherPlatoonLine] | None = None
    home_sp_platoon: list[PitcherPlatoonLine] | None = None
    context: GameContext | None = None
    away_sp_day_night: PitcherDayNightProfile | None = None
    home_sp_day_night: PitcherDayNightProfile | None = None
    away_sp_inning_splits: list[SpInningStart] | None = None
    home_sp_inning_splits: list[SpInningStart] | None = None


class ZoneHeatmapCell(_ExportModel):
    zone: int
    contact_rate: float | None = None
    hard_hit_pct: float | None = None
    swings: int
    pitches: int


class ZoneHeatmapProfile(_ExportModel):
    metric: Literal["contact_rate"]
    zones: list[ZoneHeatmapCell]


class BattedBallProfile(_ExportModel):
    bbe: int
    pull_pct: float | None = None
    straight_pct: float | None = None
    oppo_pct: float | None = None
    gb_pct: float | None = None
    ld_pct: float | None = None
    fb_pct: float | None = None
    avg_dist: float | None = None
    dist_300_plus: int
    dist_350_plus: int


class BattedBall(_ExportModel):
    date: str
    ev: float | None = None
    la: float | None = None
    dist: float | None = None
    result: str
    barrel: bool
    pitch: str | None = None


class GameLogEntry(_ExportModel):
    date: str
    pa: int | None = None
    hits: int | None = None
    singles: int | None = None
    tb: int | None = None
    hr: int | None = None
    avg_ev: float | None = None
    barrels: int | None = None


class CategoryBoards(_ExportModel):
    hits: list[HitterRow]
    singles: list[HitterRow]
    total_bases: list[HitterRow]
    hrr: list[HitterRow]
    home_runs: list[HitterRow]


class TopPlaysBoard(_ExportModel):
    hits: list[TopPlay]
    singles: list[TopPlay]
    total_bases: list[TopPlay]
    hrr: list[TopPlay]
    home_runs: list[TopPlay]


class FilterSupportEntry(_ExportModel):
    supported: bool
    source: Literal["export", "client-slice", "unsupported"]
    reason: str | None = None


class FilterSupportMetadata(_ExportModel):
    """Derived from export contents — mirrors filterSupport.ts policy, not stored in JSON."""

    timeframe: dict[str, FilterSupportEntry]
    situation: dict[str, FilterSupportEntry]
    pitch_type: FilterSupportEntry


class DailyExport(_ExportModel):
    date: str
    games: list[Game]
    top_plays: TopPlaysBoard
    category_boards: CategoryBoards
    matchups: list[HitterRow]
    game_details: list[GameDetail]
    export_meta: ExportMeta | None = None
    schema_version: int | str | None = None
    player_logs: dict[str, list[GameLogEntry]] | None = None
    batted_balls: dict[str, list[BattedBall]] | None = None
    batted_ball_profiles: dict[str, BattedBallProfile] | None = None
    player_day_night_splits: dict[str, HitterDayNightProfile] | None = None
    player_zone_heatmaps: dict[str, ZoneHeatmapProfile] | None = None

    @field_validator("date")
    @classmethod
    def validate_date_format(cls, value: str) -> str:
        datetime.strptime(value, "%Y-%m-%d")
        return value


class DailyExportEnvelope(RootModel[DailyExport]):
    """Root wrapper for validating a full export document."""

    root: DailyExport


def parse_daily_export(data: dict[str, Any]) -> DailyExport:
    """Parse and structurally validate export JSON."""
    return DailyExport.model_validate(data)


def export_top_level_keys() -> frozenset[str]:
    """Top-level keys expected on DailyExport — parity with slate.ts."""
    return frozenset(DailyExport.model_fields.keys())
