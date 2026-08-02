"""Side-effect-free MLB Stats API schedule fetch and normalization for export builders."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

import requests

SCHEDULE_API_URL = "https://statsapi.mlb.com/api/v1/schedule"
SCHEDULE_HYDRATE = "probablePitcher,venue,team"
DEFAULT_TIMEOUT_SECONDS = 30

HttpGet = Callable[[str, float], Any]


@dataclass(frozen=True)
class ScheduleGameRow:
    """Normalized schedule row before export Game model mapping."""

    slate_date: str
    game_pk: int | None
    game_id: str
    away_team: str
    home_team: str
    away_team_id: int | None
    home_team_id: int | None
    away_sp: str
    home_sp: str
    away_sp_id: int | None
    home_sp_id: int | None
    start_time_utc: str | None
    status: str | None
    venue: str | None
    away_score: int | None = None
    home_score: int | None = None
    inning_state: str | None = None
    warnings: tuple[str, ...] = field(default_factory=tuple)


def build_game_id(away_team: str, home_team: str) -> str:
    return f"{away_team} @ {home_team}"


def fetch_schedule_json(
    iso_date: str,
    *,
    http_get: HttpGet | None = None,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    """Fetch raw schedule JSON for a slate date. Network occurs only when called."""
    getter = http_get or requests.get
    url = (
        f"{SCHEDULE_API_URL}?sportId=1&date={iso_date}"
        f"&hydrate={SCHEDULE_HYDRATE}"
    )
    response = getter(url, timeout)
    if hasattr(response, "raise_for_status"):
        response.raise_for_status()
        payload = response.json()
    else:
        payload = response
    if not isinstance(payload, dict):
        raise ValueError("Schedule response must be a JSON object")
    return payload


def _probable_pitcher(team_side: dict[str, Any]) -> tuple[str, int | None]:
    pitcher = team_side.get("probablePitcher") or {}
    name = pitcher.get("fullName") or "TBD"
    pitcher_id = pitcher.get("id")
    return name, pitcher_id if pitcher_id is not None else None


def _team_score(team_side: dict[str, Any]) -> int | None:
    score = team_side.get("score")
    if score is None:
        return None
    try:
        return int(score)
    except (TypeError, ValueError):
        return None


def _parse_game_row(raw_game: dict[str, Any], slate_date: str) -> ScheduleGameRow:
    warnings: list[str] = []
    away_side = raw_game.get("teams", {}).get("away", {})
    home_side = raw_game.get("teams", {}).get("home", {})
    away_team_obj = away_side.get("team") or {}
    home_team_obj = home_side.get("team") or {}

    away_team = away_team_obj.get("name")
    home_team = home_team_obj.get("name")
    if not away_team or not home_team:
        warnings.append("Schedule game missing away or home team name")

    away_team = away_team or "Unknown Away"
    home_team = home_team or "Unknown Home"

    away_sp, away_sp_id = _probable_pitcher(away_side)
    home_sp, home_sp_id = _probable_pitcher(home_side)
    if away_sp == "TBD":
        warnings.append(f"No probable away pitcher for {away_team} @ {home_team}")
    if home_sp == "TBD":
        warnings.append(f"No probable home pitcher for {away_team} @ {home_team}")

    venue_obj = raw_game.get("venue") or {}
    venue = venue_obj.get("name")
    if not venue:
        warnings.append(f"Unknown or missing venue for {away_team} @ {home_team}")

    status_obj = raw_game.get("status") or {}
    status = status_obj.get("detailedState") or status_obj.get("abstractGameState")

    game_pk = raw_game.get("gamePk")
    if game_pk is None:
        warnings.append(f"Schedule game missing gamePk for {away_team} @ {home_team}")

    start_time_utc = raw_game.get("gameDate")
    if start_time_utc and not _looks_like_iso_timestamp(start_time_utc):
        warnings.append(
            f"Malformed start time for game_pk {game_pk}: {start_time_utc!r}"
        )

    linescore = raw_game.get("linescore") or {}
    inning_state = linescore.get("inningState") or linescore.get("currentInningOrdinal")

    return ScheduleGameRow(
        slate_date=slate_date,
        game_pk=int(game_pk) if game_pk is not None else None,
        game_id=build_game_id(away_team, home_team),
        away_team=away_team,
        home_team=home_team,
        away_team_id=away_team_obj.get("id"),
        home_team_id=home_team_obj.get("id"),
        away_sp=away_sp,
        home_sp=home_sp,
        away_sp_id=away_sp_id,
        home_sp_id=home_sp_id,
        start_time_utc=start_time_utc,
        status=status,
        venue=venue,
        away_score=_team_score(away_side),
        home_score=_team_score(home_side),
        inning_state=inning_state,
        warnings=tuple(warnings),
    )


def _looks_like_iso_timestamp(value: str) -> bool:
    return "T" in value and value.endswith("Z")


def parse_schedule_rows(
    schedule_json: dict[str, Any],
    *,
    slate_date: str | None = None,
) -> tuple[list[ScheduleGameRow], list[str]]:
    """Parse MLB schedule JSON into normalized rows. Pure function — no I/O."""
    warnings: list[str] = []
    rows: list[ScheduleGameRow] = []

    dates = schedule_json.get("dates") or []
    if not dates:
        warnings.append(f"No schedule dates returned for slate {slate_date or 'unknown'}")

    for date_block in dates:
        block_date = date_block.get("date") or slate_date or ""
        for raw_game in date_block.get("games") or []:
            row = _parse_game_row(raw_game, block_date or slate_date or "")
            warnings.extend(row.warnings)
            rows.append(row)

    pk_counts: dict[int, int] = {}
    for row in rows:
        if row.game_pk is None:
            continue
        pk_counts[row.game_pk] = pk_counts.get(row.game_pk, 0) + 1

    for pk, count in sorted(pk_counts.items()):
        if count > 1:
            warnings.append(
                f"Duplicate game_pk ({count}x): {pk} — use game_pk for selection"
            )

    return rows, warnings
