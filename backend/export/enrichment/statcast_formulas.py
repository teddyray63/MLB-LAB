"""Reproducible Statcast event formulas — mirrors scripts/mlb_lab_runner.event_stats."""

from __future__ import annotations

from typing import Any

from backend.export.enrichment.enrichment_models import CountBlock, RateBlock, SplitBlock

AB_EXCLUDE_EVENTS = frozenset({"walk", "intent_walk", "hit_by_pitch", "sac_bunt", "sac_fly"})
HIT_EVENTS = frozenset({"single", "double", "triple", "home_run"})
BB_EVENTS = frozenset({"walk", "intent_walk"})
SO_EVENTS = frozenset({"strikeout", "strikeout_double_play"})
SWING_DESCRIPTIONS = frozenset(
    {"swinging_strike", "swinging_strike_blocked", "foul", "foul_tip", "hit_into_play"}
)
WHIFF_DESCRIPTIONS = frozenset({"swinging_strike", "swinging_strike_blocked"})

PITCH_NAME_MAP: dict[str, str] = {
    "FF": "Four-Seam Fastball",
    "SI": "Sinker",
    "FC": "Cutter",
    "SL": "Slider",
    "ST": "Sweeper",
    "CU": "Curveball",
    "KC": "Knuckle Curve",
    "CH": "Changeup",
    "FS": "Splitter",
    "SV": "Slurve",
    "KN": "Knuckleball",
    "EP": "Eephus",
    "FO": "Forkball",
    "SC": "Screwball",
    "PO": "Pitchout",
    "AB": "Auto Ball",
    "UN": "Unknown",
}


def pitch_display_name(code: str) -> str:
    upper = code.upper()
    return PITCH_NAME_MAP.get(upper, f"Unknown Pitch ({upper})")


def _event_value(row: dict[str, Any], key: str) -> Any:
    return row.get(key)


def _is_event(row: dict[str, Any]) -> bool:
    event = _event_value(row, "events")
    return event is not None and event != ""


def compute_count_block(rows: list[dict[str, Any]]) -> CountBlock:
    if not rows:
        return CountBlock()

    event_rows = [row for row in rows if _is_event(row)]
    pa = len(event_rows)
    if pa == 0:
        return CountBlock(pa=0)

    ab_rows = [row for row in event_rows if _event_value(row, "events") not in AB_EXCLUDE_EVENTS]
    ab = len(ab_rows)

    singles = sum(1 for row in event_rows if _event_value(row, "events") == "single")
    doubles = sum(1 for row in event_rows if _event_value(row, "events") == "double")
    triples = sum(1 for row in event_rows if _event_value(row, "events") == "triple")
    hrs = sum(1 for row in event_rows if _event_value(row, "events") == "home_run")
    hits = singles + doubles + triples + hrs
    tb = singles + 2 * doubles + 3 * triples + 4 * hrs
    bb = sum(1 for row in event_rows if _event_value(row, "events") in BB_EVENTS)
    so = sum(1 for row in event_rows if _event_value(row, "events") in SO_EVENTS)
    hbp = sum(1 for row in event_rows if _event_value(row, "events") == "hit_by_pitch")
    sf = sum(1 for row in event_rows if _event_value(row, "events") == "sac_fly")

    return CountBlock(
        pa=pa,
        ab=ab,
        h=hits,
        singles=singles,
        doubles=doubles,
        triples=triples,
        hr=hrs,
        bb=bb,
        so=so,
        hbp=hbp,
        sf=sf,
        tb=tb,
    )


def compute_rate_block(rows: list[dict[str, Any]], counts: CountBlock | None = None) -> RateBlock:
    counts = counts or compute_count_block(rows)
    if counts.pa is None or counts.pa == 0:
        return RateBlock()

    ab = counts.ab or 0
    pa = counts.pa
    hits = counts.h or 0
    tb = counts.tb or 0
    bb = counts.bb or 0
    so = counts.so or 0
    hbp = counts.hbp or 0
    sf = counts.sf or 0

    # Undefined-rate semantics intentionally differ from mlb_lab_runner.event_stats:
    # when AB == 0, export None rather than 0 to avoid fabricating a valid-looking rate.
    avg = hits / ab if ab else None
    slg = tb / ab if ab else None
    iso = (slg - avg) if avg is not None and slg is not None else None

    obp_den = ab + bb + hbp + sf
    obp = (hits + bb + hbp) / obp_den if obp_den else None
    ops = (obp + slg) if obp is not None and slg is not None else None

    k_pct = so / pa if pa else None
    bb_pct = bb / pa if pa else None

    woba_values = [_event_value(row, "woba_value") for row in rows if _event_value(row, "woba_value") is not None]
    xwoba_values = [
        _event_value(row, "estimated_woba_using_speedangle")
        for row in rows
        if _event_value(row, "estimated_woba_using_speedangle") is not None
    ]
    woba = sum(woba_values) / len(woba_values) if woba_values else None
    xwoba = sum(xwoba_values) / len(xwoba_values) if xwoba_values else None

    launch_speeds = [
        float(_event_value(row, "launch_speed"))
        for row in rows
        if _event_value(row, "launch_speed") is not None
    ]
    hard_hit_pct = (
        sum(1 for speed in launch_speeds if speed >= 95) / len(launch_speeds) if launch_speeds else None
    )

    barrel_values = [
        _event_value(row, "launch_speed_angle")
        for row in rows
        if _event_value(row, "launch_speed_angle") is not None
    ]
    barrel_pct = (
        sum(1 for value in barrel_values if value == 6) / len(barrel_values) if barrel_values else None
    )

    swings = [row for row in rows if _event_value(row, "description") in SWING_DESCRIPTIONS]
    whiffs = [row for row in rows if _event_value(row, "description") in WHIFF_DESCRIPTIONS]
    whiff_pct = len(whiffs) / len(swings) if swings else None

    return RateBlock(
        avg=avg,
        obp=obp,
        slg=slg,
        ops=ops,
        iso=iso,
        k_pct=k_pct,
        bb_pct=bb_pct,
        woba=woba,
        xwoba=xwoba,
        barrel_pct=barrel_pct,
        hard_hit_pct=hard_hit_pct,
        whiff_pct=whiff_pct,
    )


def compute_split_block(
    rows: list[dict[str, Any]],
    *,
    split: str,
    small_sample_threshold: int = 20,
) -> SplitBlock:
    counts = compute_count_block(rows)
    rates = compute_rate_block(rows, counts)
    pa = counts.pa or 0
    missing_denominator = pa > 0 and (counts.ab or 0) == 0
    warnings: list[str] = []
    if missing_denominator:
        warnings.append(f"{split}: rate denominators incomplete (PA>0, AB=0)")
    return SplitBlock(
        split=split,  # type: ignore[arg-type]
        counts=counts,
        rates=rates,
        small_sample=0 < pa < small_sample_threshold,
        missing_denominator=missing_denominator,
        warnings=warnings,
    )


def filter_rows(
    rows: list[dict[str, Any]],
    *,
    batter_id: int | None = None,
    pitcher_id: int | None = None,
    pitch_type: str | None = None,
    p_throws: str | None = None,
    stand: str | None = None,
    home_team: str | None = None,
    away_team: str | None = None,
    is_home_batter: bool | None = None,
    day_night: str | None = None,
    game_dates: set[str] | None = None,
    max_games: int | None = None,
) -> list[dict[str, Any]]:
    filtered = rows
    if batter_id is not None:
        filtered = [row for row in filtered if _event_value(row, "batter") == batter_id]
    if pitcher_id is not None:
        filtered = [row for row in filtered if _event_value(row, "pitcher") == pitcher_id]
    if pitch_type is not None:
        filtered = [row for row in filtered if _event_value(row, "pitch_type") == pitch_type]
    if p_throws is not None:
        filtered = [row for row in filtered if _event_value(row, "p_throws") == p_throws]
    if stand is not None:
        filtered = [row for row in filtered if _event_value(row, "stand") == stand]
    if day_night is not None:
        filtered = [row for row in filtered if _event_value(row, "day_night") == day_night]
    if game_dates is not None:
        filtered = [row for row in filtered if _event_value(row, "game_date") in game_dates]
    if is_home_batter is not None and home_team is not None and away_team is not None:
        if is_home_batter:
            filtered = [
                row
                for row in filtered
                if _event_value(row, "inning_topbot") == "Bot"
                or _event_value(row, "home_team") == home_team
            ]
        else:
            filtered = [
                row
                for row in filtered
                if _event_value(row, "inning_topbot") == "Top"
                or _event_value(row, "away_team") == away_team
            ]
    if max_games is not None and max_games > 0:
        dates = sorted(
            {str(_event_value(row, "game_date")) for row in filtered if _event_value(row, "game_date")},
            reverse=True,
        )[:max_games]
        date_set = set(dates)
        filtered = [row for row in filtered if _event_value(row, "game_date") in date_set]
    return filtered


def recent_game_dates(rows: list[dict[str, Any]], max_games: int) -> set[str]:
    dates = sorted(
        {str(_event_value(row, "game_date")) for row in rows if _event_value(row, "game_date")},
        reverse=True,
    )
    return set(dates[:max_games])
