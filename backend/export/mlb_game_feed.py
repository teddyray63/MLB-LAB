"""Side-effect-free MLB game feed fetch and normalization."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import requests

GAME_FEED_API = "https://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live"
ROSTER_API = "https://statsapi.mlb.com/api/v1/teams/{team_id}/roster"
DEFAULT_TIMEOUT_SECONDS = 30

HttpGet = Callable[[str, float], Any]


def fetch_game_feed_json(
    game_pk: int,
    *,
    http_get: HttpGet | None = None,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    getter = http_get or (lambda url, timeout: requests.get(url, timeout=timeout))
    url = GAME_FEED_API.format(game_pk=game_pk)
    response = getter(url, timeout)
    if hasattr(response, "raise_for_status"):
        response.raise_for_status()
        payload = response.json()
    else:
        payload = response
    if not isinstance(payload, dict):
        raise ValueError("Game feed response must be a JSON object")
    return payload


def fetch_team_roster_json(
    team_id: int,
    *,
    http_get: HttpGet | None = None,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    getter = http_get or (lambda url, timeout: requests.get(url, timeout=timeout))
    url = ROSTER_API.format(team_id=team_id)
    response = getter(url, timeout)
    if hasattr(response, "raise_for_status"):
        response.raise_for_status()
        payload = response.json()
    else:
        payload = response
    if not isinstance(payload, dict):
        raise ValueError("Roster response must be a JSON object")
    return payload


def _handedness_by_player_id(game_data: dict[str, Any]) -> dict[int, dict[str, Any]]:
    """Index canonical MLB handedness codes by player ID.

    The feed exposes `batSide`/`pitchHand` only on `gameData.players` person
    objects; boxscore player objects do not carry them.
    """
    index: dict[int, dict[str, Any]] = {}
    for person in (game_data.get("players") or {}).values():
        if not isinstance(person, dict):
            continue
        player_id = person.get("id")
        if player_id is None:
            continue
        index[int(player_id)] = {
            "bats": (person.get("batSide") or {}).get("code"),
            "throws": (person.get("pitchHand") or {}).get("code"),
        }
    return index


def parse_game_feed_side(
    feed: dict[str, Any],
    side: str,
) -> dict[str, Any]:
    """Extract normalized team/player/lineup data for one side of a game feed."""
    game_data = feed.get("gameData") or {}
    live_data = feed.get("liveData") or {}
    teams_meta = (game_data.get("teams") or {}).get(side) or {}
    box_team = ((live_data.get("boxscore") or {}).get("teams") or {}).get(side) or {}
    players_raw = box_team.get("players") or {}
    batting_order = box_team.get("battingOrder") or []

    handedness = _handedness_by_player_id(game_data)

    players: list[dict[str, Any]] = []
    for key, player_obj in players_raw.items():
        if not isinstance(player_obj, dict):
            continue
        person = player_obj.get("person") or {}
        player_id = person.get("id")
        if player_id is None:
            continue
        hands = handedness.get(int(player_id)) or {}
        players.append(
            {
                "player_id": int(player_id),
                "full_name": person.get("fullName") or "",
                "display_name": person.get("nickName") or person.get("fullName"),
                "primary_position": (player_obj.get("position") or {}).get("abbreviation"),
                "bats": hands.get("bats"),
                "throws": hands.get("throws"),
                "roster_status": (player_obj.get("status") or {}).get("description"),
                "game_status_code": (player_obj.get("gameStatus") or {}).get("code"),
            }
        )

    probable = (game_data.get("probablePitchers") or {}).get(side) or {}
    probable_id = probable.get("id")

    pitchers = box_team.get("pitchers") or []
    starter_id = pitchers[0] if pitchers else None

    return {
        "team_id": teams_meta.get("id"),
        "team_name": teams_meta.get("name"),
        "abbreviation": teams_meta.get("teamCode") or teams_meta.get("fileCode"),
        "league": ((teams_meta.get("league") or {}).get("name")),
        "division": ((teams_meta.get("division") or {}).get("name")),
        "batting_order": [int(pid) for pid in batting_order],
        "players": players,
        "probable_pitcher_id": int(probable_id) if probable_id is not None else None,
        "starting_pitcher_id": int(starter_id) if starter_id is not None else None,
        "bullpen_pitcher_ids": [int(pid) for pid in pitchers[1:]] if len(pitchers) > 1 else [],
        "published": bool(batting_order),
    }


def merge_roster_players(
    feed_players: list[dict[str, Any]],
    roster_json: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    """Merge roster endpoint rows into feed players without name-only identity."""
    if not roster_json:
        return feed_players

    roster_by_id: dict[int, dict[str, Any]] = {}
    for entry in roster_json.get("roster") or []:
        person = (entry or {}).get("person") or {}
        player_id = person.get("id")
        if player_id is None:
            continue
        roster_by_id[int(player_id)] = {
            "player_id": int(player_id),
            "full_name": person.get("fullName") or "",
            "display_name": person.get("nickName") or person.get("fullName"),
            "primary_position": (entry.get("position") or {}).get("abbreviation"),
            "bats": (person.get("batSide") or {}).get("code"),
            "throws": (person.get("pitchHand") or {}).get("code"),
            "roster_status": (entry.get("status") or {}).get("description"),
        }

    merged: dict[int, dict[str, Any]] = {row["player_id"]: dict(row) for row in feed_players}
    for player_id, roster_row in roster_by_id.items():
        if player_id in merged:
            for key, value in roster_row.items():
                if merged[player_id].get(key) in (None, "") and value not in (None, ""):
                    merged[player_id][key] = value
        else:
            merged[player_id] = roster_row
    return list(merged.values())
