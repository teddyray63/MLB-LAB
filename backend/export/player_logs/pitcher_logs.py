"""Build pitcher appearance logs from game feeds and Statcast events."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

from backend.export.enrichment.statcast_formulas import BB_EVENTS, HIT_EVENTS, SO_EVENTS
from backend.export.enrichment.statcast_source import StatcastEvents
from backend.export.identity_models import ExportPlayer
from backend.export.player_logs.models import AppearanceType, PitcherGameLog


def parse_innings_pitched(value: str | float | int | None) -> float | None:
    """Parse MLB fractional innings (0.1 = 1 out, 0.2 = 2 outs, 1.0 = 1 inning)."""
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        whole = int(value)
        outs = round((float(value) - whole) * 10)
        if outs not in (0, 1, 2):
            return None
        return whole + outs / 3.0
    text = str(value).strip()
    if not text:
        return None
    if "." not in text:
        try:
            return float(text)
        except ValueError:
            return None
    whole_text, frac_text = text.split(".", 1)
    try:
        whole = int(whole_text)
        outs = int(frac_text[:1])
    except ValueError:
        return None
    if outs not in (0, 1, 2):
        return None
    return whole + outs / 3.0


def format_innings_pitched(decimal: float | None) -> str | None:
    if decimal is None:
        return None
    whole = int(decimal)
    outs = round((decimal - whole) * 3)
    if outs == 3:
        whole += 1
        outs = 0
    return f"{whole}.{outs}"


def _event_value(row: dict[str, Any], key: str) -> Any:
    return row.get(key)


def _normalize_game_date(value: Any) -> str | None:
    if value is None:
        return None
    return str(value)[:10]


def _parse_decision(note: str | None) -> str | None:
    if not note:
        return None
    token = note.split(",")[0].strip()
    if token in {"W", "L", "S", "H", "BS", "ND"}:
        return token
    return None


def _pitching_stats_from_box(player_obj: dict[str, Any]) -> dict[str, Any]:
    return (player_obj.get("stats") or {}).get("pitching") or {}


def extract_pitcher_appearances_from_feed(
    feed: dict[str, Any],
    *,
    game_date: str | None = None,
) -> list[dict[str, Any]]:
    """Extract normalized pitcher appearance dicts from one game feed."""
    game_data = feed.get("gameData") or {}
    live_data = feed.get("liveData") or {}
    game_pk = feed.get("gamePk") or game_data.get("game", {}).get("pk")
    official_date = game_date or (game_data.get("datetime") or {}).get("officialDate")
    if official_date is None:
        official_date = (game_data.get("game") or {}).get("officialDate")

    linescore = (live_data.get("linescore") or {})
    status = ((game_data.get("status") or {}).get("detailedState")) or linescore.get("currentInning")

    appearances: list[dict[str, Any]] = []
    teams_meta = game_data.get("teams") or {}
    box_teams = ((live_data.get("boxscore") or {}).get("teams") or {})

    for side in ("away", "home"):
        box_team = box_teams.get(side) or {}
        meta_team = teams_meta.get(side) or {}
        team_id = meta_team.get("id") or box_team.get("team", {}).get("id")
        opponent_side = "home" if side == "away" else "away"
        opponent_team_id = (teams_meta.get(opponent_side) or {}).get("id")

        pitcher_ids = box_team.get("pitchers") or []
        players = box_team.get("players") or {}

        for index, pitcher_id in enumerate(pitcher_ids):
            key = f"ID{pitcher_id}"
            player_obj = players.get(key) or {}
            stats = _pitching_stats_from_box(player_obj)
            if not stats:
                continue

            appearance_type: AppearanceType = "start" if index == 0 else "relief"
            ip_text = stats.get("inningsPitched")
            ip_decimal = parse_innings_pitched(ip_text)

            appearances.append(
                {
                    "player_id": int(pitcher_id),
                    "game_pk": int(game_pk) if game_pk is not None else None,
                    "game_date": str(official_date)[:10] if official_date else None,
                    "team_id": int(team_id) if team_id is not None else None,
                    "opponent_team_id": int(opponent_team_id) if opponent_team_id is not None else None,
                    "home_away": side,
                    "appearance_type": appearance_type,
                    "is_start": appearance_type == "start",
                    "is_relief": appearance_type == "relief",
                    "innings_pitched": str(ip_text) if ip_text is not None else None,
                    "innings_pitched_decimal": ip_decimal,
                    "batters_faced": _int_or_none(stats.get("battersFaced")),
                    "hits": _int_or_none(stats.get("hits")),
                    "runs": _int_or_none(stats.get("runs")),
                    "earned_runs": _int_or_none(stats.get("earnedRuns")),
                    "walks": _int_or_none(stats.get("baseOnBalls")),
                    "strikeouts": _int_or_none(stats.get("strikeOuts")),
                    "home_runs": _int_or_none(stats.get("homeRuns")),
                    "pitches": _int_or_none(stats.get("numberOfPitches")),
                    "strikes": _int_or_none(stats.get("strikes")),
                    "decision": _parse_decision(stats.get("note")),
                    "game_status": status,
                }
            )
    return appearances


def _statcast_pitcher_counts(rows: list[dict[str, Any]]) -> dict[str, int | None]:
    event_rows = [row for row in rows if _event_value(row, "events") not in (None, "")]
    if not event_rows:
        return {
            "batters_faced": None,
            "hits": None,
            "walks": None,
            "strikeouts": None,
            "home_runs": None,
            "pitches": len(rows) if rows else None,
        }

    events = [_event_value(row, "events") for row in event_rows]
    return {
        "batters_faced": len(event_rows),
        "hits": sum(1 for event in events if event in HIT_EVENTS),
        "walks": sum(1 for event in events if event in BB_EVENTS),
        "strikeouts": sum(1 for event in events if event in SO_EVENTS),
        "home_runs": sum(1 for event in events if event == "home_run"),
        "pitches": len(rows),
    }


def build_pitcher_game_log(
    player_id: int,
    game_date: str,
    *,
    appearance_type: AppearanceType,
    box: dict[str, Any] | None = None,
    event_rows: list[dict[str, Any]] | None = None,
) -> PitcherGameLog | None:
    box = box or {}
    sc_counts = _statcast_pitcher_counts(event_rows or [])

    ip_decimal = box.get("innings_pitched_decimal")
    if ip_decimal is None and box.get("innings_pitched") is not None:
        ip_decimal = parse_innings_pitched(box.get("innings_pitched"))

    pitches = box.get("pitches")
    if pitches is None:
        pitches = sc_counts.get("pitches")

    bf = box.get("batters_faced")
    if bf is None:
        bf = sc_counts.get("batters_faced")

    if not box and not event_rows:
        return None
    if bf is None and pitches is None and ip_decimal is None:
        return None

    is_start = appearance_type == "start"
    return PitcherGameLog(
        player_id=player_id,
        game_pk=box.get("game_pk"),
        game_date=game_date,
        team_id=box.get("team_id"),
        opponent_team_id=box.get("opponent_team_id"),
        home_away=box.get("home_away"),
        appearance_type=appearance_type,
        is_start=is_start,
        is_relief=not is_start,
        innings_pitched=box.get("innings_pitched"),
        innings_pitched_decimal=ip_decimal,
        batters_faced=bf,
        hits=box.get("hits") if box.get("hits") is not None else sc_counts.get("hits"),
        runs=box.get("runs"),
        earned_runs=box.get("earned_runs"),
        walks=box.get("walks") if box.get("walks") is not None else sc_counts.get("walks"),
        strikeouts=box.get("strikeouts")
        if box.get("strikeouts") is not None
        else sc_counts.get("strikeouts"),
        home_runs=box.get("home_runs")
        if box.get("home_runs") is not None
        else sc_counts.get("home_runs"),
        pitches=pitches,
        strikes=box.get("strikes"),
        decision=box.get("decision"),
        game_result=box.get("game_result"),
        game_status=box.get("game_status"),
    )


@dataclass
class PitcherLogsBuildResult:
    logs: list[PitcherGameLog] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def _group_pitcher_events(
    events: StatcastEvents,
    *,
    pitcher_ids: set[int] | None = None,
) -> dict[tuple[int, str, AppearanceType], list[dict[str, Any]]]:
    """Group Statcast rows by pitcher + date; appearance type unknown without box score."""
    groups: dict[tuple[int, str], list[dict[str, Any]]] = {}
    for row in events:
        pitcher = _event_value(row, "pitcher")
        game_date = _normalize_game_date(_event_value(row, "game_date"))
        if pitcher is None or game_date is None:
            continue
        pitcher_id = int(pitcher)
        if pitcher_ids is not None and pitcher_id not in pitcher_ids:
            continue
        groups.setdefault((pitcher_id, game_date), []).append(row)

    result: dict[tuple[int, str, AppearanceType], list[dict[str, Any]]] = {}
    for (pitcher_id, game_date), rows in groups.items():
        result[(pitcher_id, game_date, "start")] = rows
    return result


def build_pitcher_logs(
    events: StatcastEvents,
    players: list[ExportPlayer],
    *,
    feeds_by_pk: dict[int, dict] | None = None,
    feed_dates_by_pk: dict[int, str] | None = None,
    target_player_ids: set[int] | None = None,
    max_appearances_per_player: int = 20,
) -> PitcherLogsBuildResult:
    warnings: list[str] = []
    feeds_by_pk = feeds_by_pk or {}
    feed_dates_by_pk = feed_dates_by_pk or {}

    pitcher_ids = target_player_ids or {
        player.player_id
        for player in players
        if player.role in {"starting_pitcher", "probable_starter", "bullpen"}
        or player.primary_position == "P"
        or player.is_actual_starter
        or player.is_probable_starter
    }

    logs_by_key: dict[tuple[int, int | None, str, AppearanceType], PitcherGameLog] = {}

    for game_pk, feed in feeds_by_pk.items():
        game_date = feed_dates_by_pk.get(game_pk)
        for appearance in extract_pitcher_appearances_from_feed(feed, game_date=game_date):
            player_id = appearance.get("player_id")
            if player_id is None or int(player_id) not in pitcher_ids:
                continue
            pid = int(player_id)
            date = appearance.get("game_date")
            if not date:
                warnings.append(f"Pitcher appearance missing game_date for player_id {pid}")
                continue
            appearance_type = appearance["appearance_type"]
            key = (pid, appearance.get("game_pk"), date, appearance_type)
            log = build_pitcher_game_log(
                pid,
                date,
                appearance_type=appearance_type,
                box=appearance,
            )
            if log is not None:
                logs_by_key[key] = log

    sc_groups = _group_pitcher_events(events, pitcher_ids=pitcher_ids)
    for (player_id, game_date, appearance_type), rows in sc_groups.items():
        game_pks = {_event_value(row, "game_pk") for row in rows if _event_value(row, "game_pk") is not None}
        game_pk = int(next(iter(game_pks))) if len(game_pks) == 1 else None
        key = (player_id, game_pk, game_date, appearance_type)
        if key in logs_by_key:
            continue
        log = build_pitcher_game_log(
            player_id,
            game_date,
            appearance_type=appearance_type,
            event_rows=rows,
        )
        if log is not None:
            if log.innings_pitched is None:
                warnings.append(
                    f"Pitcher log player_id {player_id} {game_date}: innings_pitched unavailable (Statcast-only)"
                )
            logs_by_key[key] = log

    logs = list(logs_by_key.values())
    by_player: dict[int, list[PitcherGameLog]] = {}
    for log in logs:
        by_player.setdefault(log.player_id, []).append(log)

    trimmed: list[PitcherGameLog] = []
    for player_id, player_logs in by_player.items():
        player_logs.sort(key=lambda row: row.game_date, reverse=True)
        trimmed.extend(
            player_logs[:max_appearances_per_player]
            if max_appearances_per_player > 0
            else player_logs
        )

    trimmed.sort(key=lambda row: (row.player_id, row.game_date, row.appearance_type or ""), reverse=True)
    return PitcherLogsBuildResult(logs=trimmed, warnings=warnings)


def _int_or_none(value: Any) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None
