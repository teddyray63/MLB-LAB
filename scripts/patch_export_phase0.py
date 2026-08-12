#!/usr/bin/env python3
"""
Patch an existing daily_export.json with Phase 0 fields without a full Statcast re-pull.

Adds: game_pk, start_time_utc, status, venue, export_meta, park_factors,
lineup_source flags, and game_pk on matchups/top_plays/category_boards.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.mlb_lab_runner import (  # noqa: E402
    JSON_EXPORT,
    build_export_meta,
    lookup_park_factors,
    mlb_json,
)


def fetch_schedule_for_date(iso_date: str) -> list[dict]:
    url = (
        "https://statsapi.mlb.com/api/v1/schedule"
        f"?sportId=1&date={iso_date}&hydrate=probablePitcher,venue,team,weather"
    )
    data = mlb_json(url)
    rows = []
    for d in data.get("dates", []):
        for g in d.get("games", []):
            away = g["teams"]["away"]["team"]
            home = g["teams"]["home"]["team"]
            away_sp = g["teams"]["away"].get("probablePitcher", {})
            home_sp = g["teams"]["home"].get("probablePitcher", {})
            status_obj = g.get("status") or {}
            rows.append(
                {
                    "game_id": f"{away['name']} @ {home['name']}",
                    "game_pk": g.get("gamePk"),
                    "away_team": away["name"],
                    "home_team": home["name"],
                    "away_sp": away_sp.get("fullName", "TBD"),
                    "home_sp": home_sp.get("fullName", "TBD"),
                    "start_time_utc": g.get("gameDate"),
                    "status": status_obj.get("detailedState")
                    or status_obj.get("abstractGameState"),
                    "venue": g["venue"]["name"],
                }
            )
    return rows


def match_schedule_row(game: dict, schedule: list[dict]) -> dict | None:
    gid = game.get("game_id") or game.get("game")
    if not gid:
        return None
    away_sp = game.get("away_sp", "TBD")
    home_sp = game.get("home_sp", "TBD")
    for row in schedule:
        if row["game_id"] != gid:
            continue
        if row["away_sp"] == away_sp and row["home_sp"] == home_sp:
            return row
    for row in schedule:
        if row["game_id"] == gid:
            return row
    return None


def infer_lineup_source(lineup: list | None) -> str:
    if not lineup:
        return "empty"
    status = (lineup[0] or {}).get("status") or ""
    if "PA order" in status:
        return "projected"
    if status:
        return "override"
    return "projected"


def patch_export(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    export_date = payload.get("date")
    if not export_date:
        raise ValueError("Export missing date")

    schedule = fetch_schedule_for_date(export_date)
    warnings: list[str] = list(payload.get("export_meta", {}).get("warnings") or [])

    # games[]
    for game in payload.get("games", []):
        row = match_schedule_row(game, schedule)
        if not row:
            warnings.append(f"No schedule match for game: {game.get('game_id')}")
            continue
        game["game_pk"] = row["game_pk"]
        game["start_time_utc"] = row["start_time_utc"]
        game["status"] = row["status"]
        game["venue"] = row["venue"]

    # game_details[]
    for detail in payload.get("game_details", []):
        row = match_schedule_row(detail, schedule)
        if row:
            detail["game_pk"] = row["game_pk"]
            detail["start_time_utc"] = row["start_time_utc"]
            detail["status"] = row["status"]
            detail["venue"] = row["venue"]
        venue = detail.get("venue") or (detail.get("context") or {}).get("park")
        ctx = detail.setdefault("context", {})
        ctx["park"] = venue
        ctx["park_factors"] = lookup_park_factors(venue)
        if ctx["park_factors"].get("run_factor") is None and venue:
            warnings.append(f"No park factors for venue: {venue}")
        detail["away_lineup_source"] = infer_lineup_source(detail.get("away_lineup"))
        detail["home_lineup_source"] = infer_lineup_source(detail.get("home_lineup"))

    # Build (game_id, team, opp_sp) -> game_pk for matchup rows
    pk_by_matchup = {}
    for detail in payload.get("game_details", []):
        pk = detail.get("game_pk")
        gid = detail.get("game_id")
        if not gid or pk is None:
            continue
        pk_by_matchup[(gid, detail.get("home_team"), detail.get("away_sp"))] = pk
        pk_by_matchup[(gid, detail.get("away_team"), detail.get("home_sp"))] = pk

    def attach_pk(row: dict) -> None:
        gid = row.get("game")
        pk = pk_by_matchup.get((gid, row.get("team"), row.get("opp_sp")))
        if pk is not None:
            row["game_pk"] = pk

    for row in payload.get("matchups", []):
        attach_pk(row)

    for cat_rows in (payload.get("category_boards") or {}).values():
        for row in cat_rows:
            attach_pk(row)

    for cat_rows in (payload.get("top_plays") or {}).values():
        for row in cat_rows:
            attach_pk(row)

    # Duplicate game_id warning
    counts: dict[str, int] = {}
    for g in payload.get("games", []):
        gid = g.get("game_id", "")
        counts[gid] = counts.get(gid, 0) + 1
    for gid, n in counts.items():
        if n > 1:
            warnings.append(
                f"Duplicate legacy game_id ({n}x): {gid} — use game_pk for selection"
            )

    payload["export_meta"] = build_export_meta(warnings)
    return payload


def main() -> None:
    out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else JSON_EXPORT
    if not out_path.exists():
        raise SystemExit(f"Export not found: {out_path}")

    print(f"Patching {out_path} with Phase 0 fields…")
    patched = patch_export(out_path)
    out_path.write_text(json.dumps(patched, indent=2), encoding="utf-8")
    meta = patched.get("export_meta", {})
    games = patched.get("games", [])
    pks = [g.get("game_pk") for g in games if g.get("game_pk") is not None]
    print(f"  export_meta.generated_at: {meta.get('generated_at')}")
    print(f"  games with game_pk: {len(pks)}/{len(games)}")
    print(f"  unique game_pk: {len(set(pks))}")
    print(f"  warnings: {len(meta.get('warnings') or [])}")
    print("Done.")


if __name__ == "__main__":
    main()
