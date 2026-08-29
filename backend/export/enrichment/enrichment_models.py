"""Internal enrichment graph models for G0b.4."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from backend.export.daily_export_models import _ExportModel

SplitCategory = Literal[
    "overall",
    "home",
    "away",
    "day",
    "night",
    "vs_lhp",
    "vs_rhp",
    "vs_lhb",
    "vs_rhb",
]

RecentWindow = Literal["last_20", "last_15", "last_10", "last_7", "last_5"]


class CountBlock(_ExportModel):
    pa: int | None = None
    ab: int | None = None
    h: int | None = None
    doubles: int | None = None
    triples: int | None = None
    hr: int | None = None
    bb: int | None = None
    so: int | None = None
    hbp: int | None = None
    sf: int | None = None
    singles: int | None = None
    tb: int | None = None


class RateBlock(_ExportModel):
    avg: float | None = None
    obp: float | None = None
    slg: float | None = None
    ops: float | None = None
    iso: float | None = None
    k_pct: float | None = None
    bb_pct: float | None = None
    woba: float | None = None
    xwoba: float | None = None
    barrel_pct: float | None = None
    hard_hit_pct: float | None = None
    whiff_pct: float | None = None


class SplitBlock(_ExportModel):
    split: SplitCategory
    counts: CountBlock = Field(default_factory=CountBlock)
    rates: RateBlock = Field(default_factory=RateBlock)
    small_sample: bool = False
    missing_denominator: bool = False
    warnings: list[str] = Field(default_factory=list)


class HitterEnrichment(_ExportModel):
    player_id: int
    game_pk: int
    team_id: int
    opponent_team_id: int
    opponent_starter_id: int | None = None
    lineup_slot: int | None = None
    bats: str | None = None
    is_home: bool | None = None
    day_night: str | None = None
    season: SplitBlock | None = None
    splits: dict[str, SplitBlock] = Field(default_factory=dict)
    recent: dict[str, SplitBlock] = Field(default_factory=dict)
    warnings: list[str] = Field(default_factory=list)


class PitcherEnrichment(_ExportModel):
    player_id: int
    game_pk: int
    team_id: int
    opponent_team_id: int
    throws: str | None = None
    is_probable_starter: bool = False
    is_actual_starter: bool = False
    season: SplitBlock | None = None
    splits: dict[str, SplitBlock] = Field(default_factory=dict)
    recent: dict[str, SplitBlock] = Field(default_factory=dict)
    warnings: list[str] = Field(default_factory=list)


class PitchMixEntry(_ExportModel):
    pitcher_id: int
    pitch_code: str
    pitch_name: str
    pitch_count: int
    usage_pct: float
    avg_velocity: float | None = None
    max_velocity: float | None = None
    batter_side: str | None = None


class PitchMixSummary(_ExportModel):
    pitcher_id: int
    game_pk: int
    window_start: str | None = None
    window_end: str | None = None
    entries: list[PitchMixEntry] = Field(default_factory=list)
    small_sample: bool = False
    warnings: list[str] = Field(default_factory=list)


class HeadToHeadSummary(_ExportModel):
    hitter_id: int
    pitcher_id: int
    pa: int | None = None
    ab: int | None = None
    h: int | None = None
    hr: int | None = None
    bb: int | None = None
    so: int | None = None
    avg: float | None = None
    available: bool = False


class EnrichmentMatchup(_ExportModel):
    game_pk: int
    hitter_id: int
    pitcher_id: int
    hitter_team_id: int
    pitcher_team_id: int
    lineup_slot: int | None = None
    hitter_bats: str | None = None
    # DERIVED PREGAME MATCHUP SIDE — NOT OBSERVED PA STAND.
    # Used only to select pitcher platoon splits when canonical hitter_bats is S.
    # Switch-hitter side is derived from the opposing pitcher's throwing hand for
    # platoon-split context; actual in-game batting side may differ (DEC-009).
    matchup_effective_bats: str | None = None
    pitcher_throws: str | None = None
    is_home_hitter: bool | None = None
    day_night: str | None = None
    hitter_split_vs_pitcher_hand: SplitBlock | None = None
    pitcher_split_vs_hitter_side: SplitBlock | None = None
    pitch_mix_pitcher_id: int | None = None
    pitch_codes: list[str] = Field(default_factory=list)
    head_to_head: HeadToHeadSummary | None = None
    non_starting: bool = False
    warnings: list[str] = Field(default_factory=list)
