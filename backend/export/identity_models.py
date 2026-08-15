"""Internal identity graph models for G0b.3 export builders."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from backend.export.daily_export_models import _ExportModel

TeamSide = Literal["away", "home"]
PlayerRole = Literal[
    "lineup",
    "bench",
    "bullpen",
    "starting_pitcher",
    "probable_starter",
    "unknown",
]


class ExportTeam(_ExportModel):
    team_id: int
    team_name: str
    game_pk: int
    side: TeamSide
    abbreviation: str | None = None
    league: str | None = None
    division: str | None = None
    venue: str | None = None


class ExportPlayer(_ExportModel):
    player_id: int
    full_name: str
    game_pk: int
    team_id: int
    display_name: str | None = None
    # Optional player-associated position sourced from MLB boxscore/roster
    # position.abbreviation. Used internally as a heuristic; it is not guaranteed
    # to represent the player's game-specific starting defensive position.
    primary_position: str | None = None
    bats: str | None = None
    throws: str | None = None
    roster_status: str | None = None
    role: PlayerRole = "unknown"
    lineup_slot: int | None = None
    is_probable_starter: bool = False
    is_actual_starter: bool = False


class ExportLineup(_ExportModel):
    game_pk: int
    team_id: int
    side: TeamSide
    batting_order_player_ids: list[int] = Field(default_factory=list)
    bench_player_ids: list[int] = Field(default_factory=list)
    starting_pitcher_id: int | None = None
    bullpen_player_ids: list[int] = Field(default_factory=list)
    published: bool = False
    status: str | None = None
