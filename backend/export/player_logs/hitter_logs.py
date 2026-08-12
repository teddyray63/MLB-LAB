"""Build hitter game logs from verified Statcast events and optional box scores."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

from backend.export.enrichment.statcast_formulas import compute_count_block, compute_rate_block
from backend.export.enrichment.statcast_source import StatcastEvents
from backend.export.identity_models import ExportPlayer
from backend.export.player_logs.models import HitterGameLog


def _event_value(row: dict[str, Any], key: str) -> Any:
    return row.get(key)


def _normalize_game_date(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value)
    return text[:10] if len(text) >= 10 else text


def _avg_ev(rows: list[dict[str, Any]]) -> float | None:
    speeds = [
        float(_event_value(row, "launch_speed"))
        for row in rows
        if _event_value(row, "launch_speed") is not None
    ]
    if not speeds:
        return None
    return sum(speeds) / len(speeds)


def _barrel_count(rows: list[dict[str, Any]]) -> int:
    return sum(1 for row in rows if _event_value(row, "launch_speed_angle") == 6)


def _infer_home_away(row: dict[str, Any]) -> Literal["home", "away"] | None:
    topbot = _event_value(row, "inning_topbot")
    if topbot == "Bot":
        return "home"
    if topbot == "Top":
        return "away"
    return None


def _group_hitter_events(
    events: StatcastEvents,
    *,
    batter_ids: set[int] | None = None,
) -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = {}
    for row in events:
        batter = _event_value(row, "batter")
        game_date = _normalize_game_date(_event_value(row, "game_date"))
        if batter is None or game_date is None:
            continue
        batter_id = int(batter)
        if batter_ids is not None and batter_id not in batter_ids:
            continue
        key = (batter_id, game_date)
        groups.setdefault(key, []).append(row)
    return groups


def _game_pk_for_group(rows: list[dict[str, Any]]) -> int | None:
    pks = {_event_value(row, "game_pk") for row in rows if _event_value(row, "game_pk") is not None}
    if len(pks) == 1:
        return int(next(iter(pks)))
    if len(pks) > 1:
        return None
    return None


def build_hitter_game_log(
    player_id: int,
    game_date: str,
    event_rows: list[dict[str, Any]],
    *,
    team_id: int | None = None,
    opponent_team_id: int | None = None,
    lineup_slot: int | None = None,
    batting_stats: dict[str, Any] | None = None,
) -> HitterGameLog | None:
    """Build one hitter-game row from Statcast events with optional box-score enrichment."""
    if not event_rows and not batting_stats:
        return None

    counts = compute_count_block(event_rows) if event_rows else None
    rates = compute_rate_block(event_rows) if event_rows else None

    box = batting_stats or {}
    game_pk = _game_pk_for_group(event_rows) if event_rows else None
    if game_pk is None and box.get("game_pk") is not None:
        game_pk = int(box["game_pk"])

    home_away = _infer_home_away(event_rows[0]) if event_rows else box.get("home_away")

    pa = counts.pa if counts and counts.pa is not None else _int_or_none(box.get("pa"))
    if pa is None and not event_rows:
        return None

    h = counts.h if counts and counts.h is not None else _int_or_none(box.get("hits"))
    singles = counts.singles if counts and counts.singles is not None else _int_or_none(box.get("singles"))
    doubles = counts.doubles if counts and counts.doubles is not None else _int_or_none(box.get("doubles"))
    triples = counts.triples if counts and counts.triples is not None else _int_or_none(box.get("triples"))
    hr = counts.hr if counts and counts.hr is not None else _int_or_none(box.get("homeRuns"))
    tb = counts.tb if counts and counts.tb is not None else _int_or_none(box.get("totalBases"))

    return HitterGameLog(
        player_id=player_id,
        game_pk=game_pk,
        game_date=game_date,
        team_id=team_id,
        opponent_team_id=opponent_team_id,
        home_away=home_away,
        lineup_slot=lineup_slot,
        pa=pa,
        ab=counts.ab if counts else _int_or_none(box.get("atBats")),
        r=_int_or_none(box.get("runs")),
        h=h,
        doubles=doubles,
        triples=triples,
        hr=hr,
        rbi=_int_or_none(box.get("rbi")),
        bb=counts.bb if counts else _int_or_none(box.get("baseOnBalls")),
        so=counts.so if counts else _int_or_none(box.get("strikeOuts")),
        hbp=counts.hbp if counts else _int_or_none(box.get("hitByPitch")),
        sf=counts.sf if counts else _int_or_none(box.get("sacFlies")),
        sb=_int_or_none(box.get("stolenBases")),
        cs=_int_or_none(box.get("caughtStealing")),
        singles=singles,
        total_bases=tb,
        avg=rates.avg if rates else _float_or_none(box.get("avg")),
        obp=rates.obp if rates else _float_or_none(box.get("obp")),
        slg=rates.slg if rates else _float_or_none(box.get("slg")),
        ops=rates.ops if rates else _float_or_none(box.get("ops")),
        avg_ev=_avg_ev(event_rows) if event_rows else _float_or_none(box.get("avg_ev")),
        barrels=_barrel_count(event_rows) if event_rows else _int_or_none(box.get("barrels")),
        game_result=box.get("game_result"),
        game_status=box.get("game_status"),
    )


@dataclass
class HitterLogsBuildResult:
    logs: list[HitterGameLog] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def build_hitter_logs(
    events: StatcastEvents,
    players: list[ExportPlayer],
    *,
    target_player_ids: set[int] | None = None,
    max_games_per_player: int = 20,
    lineup_slot_by_player_game: dict[tuple[int, int], int] | None = None,
) -> HitterLogsBuildResult:
    """Build hitter game logs for target players within the Statcast window."""
    warnings: list[str] = []

    hitter_ids = target_player_ids or {
        player.player_id
        for player in players
        if player.role in {"lineup", "bench", "unknown"} and player.primary_position != "P"
    }

    name_by_id: dict[int, str] = {}
    team_by_id_game: dict[tuple[int, int], int] = {}
    for player in players:
        name_by_id[player.player_id] = player.full_name
        team_by_id_game[(player.game_pk, player.player_id)] = player.team_id

    groups = _group_hitter_events(events, batter_ids=hitter_ids)

    by_player: dict[int, list[tuple[str, list[dict[str, Any]]]]] = {}
    for (player_id, game_date), rows in groups.items():
        by_player.setdefault(player_id, []).append((game_date, rows))

    logs: list[HitterGameLog] = []
    for player_id, dated_groups in by_player.items():
        dated_groups.sort(key=lambda item: item[0], reverse=True)
        selected = dated_groups[:max_games_per_player] if max_games_per_player > 0 else dated_groups
        for game_date, rows in selected:
            game_pk = _game_pk_for_group(rows)
            team_id = None
            lineup_slot = None
            if game_pk is not None:
                team_id = team_by_id_game.get((game_pk, player_id))
                if lineup_slot_by_player_game:
                    lineup_slot = lineup_slot_by_player_game.get((game_pk, player_id))
            log = build_hitter_game_log(
                player_id,
                game_date,
                rows,
                team_id=team_id,
                lineup_slot=lineup_slot,
            )
            if log is not None:
                logs.append(log)

    logs.sort(key=lambda row: (row.player_id, row.game_date), reverse=True)

    missing_names = sorted(pid for pid in hitter_ids if pid not in by_player)
    if missing_names:
        sample = missing_names[:3]
        labels = [name_by_id.get(pid, str(pid)) for pid in sample]
        warnings.append(
            f"No Statcast game logs for {len(missing_names)} target hitters; e.g. {labels}"
        )

    return HitterLogsBuildResult(logs=logs, warnings=warnings)


def _int_or_none(value: Any) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _float_or_none(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
