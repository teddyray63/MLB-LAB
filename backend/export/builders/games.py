"""Build export games[] from normalized MLB schedule data."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from backend.export.daily_export_models import Game
from backend.export.mlb_schedule import ScheduleGameRow, parse_schedule_rows


@dataclass
class GamesBuildResult:
    games: list[Game]
    warnings: list[str] = field(default_factory=list)
    coverage: dict[str, int | str | None] = field(default_factory=dict)


def _schedule_row_to_game(row: ScheduleGameRow) -> Game:
    return Game(
        game_id=row.game_id,
        away_team=row.away_team,
        home_team=row.home_team,
        away_sp=row.away_sp,
        home_sp=row.home_sp,
        away_sp_id=row.away_sp_id,
        home_sp_id=row.home_sp_id,
        game_pk=row.game_pk,
        start_time_utc=row.start_time_utc,
        status=row.status,
        venue=row.venue,
    )


def build_games_from_schedule_rows(rows: list[ScheduleGameRow]) -> GamesBuildResult:
    """Build Game models from normalized schedule rows without deduplicating game_pk."""
    warnings: list[str] = []
    games: list[Game] = []

    for row in rows:
        warnings.extend(row.warnings)
        games.append(_schedule_row_to_game(row))

    pk_counts: dict[int, int] = {}
    for game in games:
        if game.game_pk is None:
            continue
        pk_counts[game.game_pk] = pk_counts.get(game.game_pk, 0) + 1
    for pk, count in sorted(pk_counts.items()):
        if count > 1:
            warnings.append(
                f"Duplicate game_pk ({count}x): {pk} — use game_pk for selection"
            )

    coverage = _coverage_summary(rows, games)
    return GamesBuildResult(games=games, warnings=_dedupe_preserve_order(warnings), coverage=coverage)


def build_games_from_schedule_json(
    schedule_json: dict[str, Any],
    *,
    slate_date: str,
) -> GamesBuildResult:
    rows, parse_warnings = parse_schedule_rows(schedule_json, slate_date=slate_date)
    result = build_games_from_schedule_rows(rows)
    result.warnings = _dedupe_preserve_order(parse_warnings + result.warnings)
    result.coverage["slate_date"] = slate_date
    return result


def _coverage_summary(rows: list[ScheduleGameRow], games: list[Game]) -> dict[str, int | str | None]:
    with_pk = sum(1 for game in games if game.game_pk is not None)
    with_sp = sum(
        1
        for game in games
        if game.away_sp != "TBD" and game.home_sp != "TBD"
    )
    with_venue = sum(1 for game in games if game.venue)
    with_score = sum(
        1 for row in rows if row.away_score is not None or row.home_score is not None
    )
    with_inning_state = sum(1 for row in rows if row.inning_state)
    duplicate_pks = sum(
        1
        for pk, count in _pk_counts(games).items()
        if count > 1
    )
    return {
        "games_total": len(games),
        "games_with_game_pk": with_pk,
        "games_with_probable_sps": with_sp,
        "games_with_venue": with_venue,
        "schedule_rows_with_score": with_score,
        "schedule_rows_with_inning_state": with_inning_state,
        "duplicate_game_pk_groups": duplicate_pks,
    }


def _pk_counts(games: list[Game]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for game in games:
        if game.game_pk is None:
            continue
        counts[game.game_pk] = counts.get(game.game_pk, 0) + 1
    return counts


def _dedupe_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
