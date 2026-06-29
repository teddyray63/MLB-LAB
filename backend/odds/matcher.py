from __future__ import annotations

from difflib import SequenceMatcher
from typing import Any, Iterable

import pandas as pd

from .normalizer import normalize_player_name


def _normalize_targets(player_targets: Any) -> list[dict[str, str]]:
    if isinstance(player_targets, pd.DataFrame):
        records = player_targets.to_dict("records")
    elif isinstance(player_targets, (list, tuple, set)):
        records = list(player_targets)
    else:
        records = [player_targets]

    normalized_targets: list[dict[str, str]] = []
    for entry in records:
        if isinstance(entry, dict):
            display_name = entry.get("player_name") or entry.get("name") or ""
            team = entry.get("team") or entry.get("team_name") or ""
        else:
            display_name = entry
            team = ""
        normalized_targets.append(
            {
                "display_name": str(display_name).strip(),
                "team": str(team).strip(),
                "key": normalize_player_name(display_name),
            }
        )
    return normalized_targets


def match_odds_to_players(odds_df: pd.DataFrame, player_targets: Any, game_team: str | None = None) -> pd.DataFrame:
    odds = odds_df.copy()
    if odds.empty:
        return odds.assign(matched=False, matched_player_name="", match_score=0.0)

    targets = _normalize_targets(player_targets)
    if not targets:
        return odds.assign(matched=False, matched_player_name="", match_score=0.0)

    odds["player_key"] = odds["player_name"].fillna("").apply(normalize_player_name)

    matched_rows: list[dict[str, Any]] = []
    for _, row in odds.iterrows():
        row_key = row.get("player_key", "")
        row_team = str(row.get("team", "")).strip().lower()
        if game_team:
            game_team_key = str(game_team).strip().lower()
            if row_team and game_team_key and row_team != game_team_key:
                matched_rows.append({"matched": False, "matched_player_name": "", "match_score": 0.0})
                continue

        best_match: dict[str, Any] | None = None
        best_score = 0.0
        for target in targets:
            target_key = target["key"]
            if not target_key:
                continue
            target_team = str(target.get("team", "")).strip().lower()
            if target_team and row_team and target_team != row_team:
                continue
            if row_key == target_key:
                score = 1.0
            else:
                row_tokens = set(row_key.split())
                target_tokens = set(target_key.split())
                if row_tokens and target_tokens and row_tokens & target_tokens:
                    score = 0.95
                else:
                    score = SequenceMatcher(None, row_key, target_key).ratio()
            if score > best_score:
                best_score = score
                best_match = target

        matched = bool(best_match and best_score >= 0.6)
        matched_rows.append(
            {
                "matched": matched,
                "matched_player_name": best_match["display_name"] if best_match else "",
                "match_score": round(best_score, 3),
            }
        )

    matched_df = odds.copy()
    matched_df["matched"] = [item["matched"] for item in matched_rows]
    matched_df["matched_player_name"] = [item["matched_player_name"] for item in matched_rows]
    matched_df["match_score"] = [item["match_score"] for item in matched_rows]
    if "matched_player_name" in matched_df.columns:
        matched_df.loc[matched_df["matched"], "player_name"] = matched_df.loc[matched_df["matched"], "matched_player_name"]
    return matched_df