from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable

import pandas as pd

from .importer import EXPORT_DIR, export_odds_csv, import_odds_csv
from .matcher import match_odds_to_players
from .normalizer import normalize_player_name

DEFAULT_SCORE_COLUMNS = ["singles_score", "total_bases_score", "runs_score", "rbi_score", "lotto_score"]


def _coerce_model_scores(model_scores: Any) -> pd.DataFrame:
    if isinstance(model_scores, pd.DataFrame):
        return model_scores.copy()
    if isinstance(model_scores, (list, tuple)):
        return pd.DataFrame(model_scores)
    return pd.DataFrame()


def build_model_scores(scores_df: pd.DataFrame, score_column: str | None = None) -> pd.DataFrame:
    scores = scores_df.copy()
    if scores.empty:
        return pd.DataFrame(columns=["player_name", "team", "model_score", "model_probability"])

    player_name_col = "player_name" if "player_name" in scores.columns else "player"
    team_col = "team" if "team" in scores.columns else None

    if score_column and score_column in scores.columns:
        model_scores = pd.to_numeric(scores[score_column], errors="coerce")
    else:
        available = [col for col in DEFAULT_SCORE_COLUMNS if col in scores.columns]
        if available:
            model_scores = scores[available].mean(axis=1, skipna=True)
        else:
            model_scores = pd.Series(0.0, index=scores.index)

    result = pd.DataFrame({
        "player_name": scores[player_name_col].fillna("") if player_name_col in scores.columns else ["" for _ in scores.index],
        "team": scores[team_col].fillna("") if team_col and team_col in scores.columns else ["" for _ in scores.index],
    })
    result["model_score"] = pd.to_numeric(model_scores, errors="coerce").fillna(0.0)
    result["model_probability"] = result["model_score"].clip(0.05, 0.95)
    result["model_probability"] = result["model_probability"].fillna(0.5)
    return result.reset_index(drop=True)


def _american_to_decimal(odds: float) -> float:
    if pd.isna(odds):
        return 1.0
    value = float(odds)
    if value > 0:
        return 1 + (value / 100.0)
    if value < 0:
        return 1 + (100.0 / abs(value))
    return 1.0


def _american_to_probability(odds: float) -> float:
    if pd.isna(odds):
        return 0.5
    value = float(odds)
    if value > 0:
        return 100.0 / (value + 100.0)
    if value < 0:
        return abs(value) / (abs(value) + 100.0)
    return 0.5


def calculate_edges(odds_df: pd.DataFrame, model_scores: Any) -> pd.DataFrame:
    odds = odds_df.copy()
    if odds.empty:
        return pd.DataFrame(columns=["player_name", "book", "team", "market", "line", "odds", "implied_probability", "model_probability", "expected_value", "edge_pct", "kelly_fraction", "positive_ev", "negative_ev", "missing_player", "duplicate_player"])

    model_df = _coerce_model_scores(model_scores)
    if model_df.empty:
        model_df = pd.DataFrame(columns=["player_name", "team", "model_probability", "model_score"])

    if "player_name" not in model_df.columns:
        model_df = model_df.copy()
        model_df["player_name"] = ""
    if "team" not in model_df.columns:
        model_df["team"] = ""
    if "model_probability" not in model_df.columns:
        model_df["model_probability"] = 0.5
    if "model_score" not in model_df.columns:
        model_df["model_score"] = 0.0

    model_df["player_key"] = model_df["player_name"].fillna("").apply(normalize_player_name)
    odds["player_key"] = odds["player_name"].fillna("").apply(normalize_player_name)

    merged = odds.merge(model_df[["player_key", "player_name", "team", "model_probability", "model_score"]], on="player_key", how="left", suffixes=("", "_model"))
    merged = merged.rename(columns={"player_name_model": "model_player_name"})

    merged["implied_probability"] = merged["odds"].apply(_american_to_probability)
    merged["model_probability"] = pd.to_numeric(merged["model_probability"], errors="coerce")
    if merged["model_probability"].isna().all():
        merged["model_probability"] = 0.5
    else:
        merged["model_probability"] = merged["model_probability"].fillna(0.5)
    merged["model_probability"] = merged["model_probability"].clip(0.05, 0.95)

    decimal_odds = merged["odds"].apply(_american_to_decimal)
    merged["expected_value"] = (merged["model_probability"] * decimal_odds) - 1.0
    merged["edge_pct"] = (merged["model_probability"] - merged["implied_probability"]) * 100.0
    merged["kelly_fraction"] = 0.0
    valid = (decimal_odds - 1.0) > 0
    if valid.any():
        b = decimal_odds[valid] - 1.0
        p = merged.loc[valid, "model_probability"]
        q = 1.0 - p
        merged.loc[valid, "kelly_fraction"] = ((b * p) - q) / b
    merged["kelly_fraction"] = merged["kelly_fraction"].clip(0.0, 0.5)

    merged["positive_ev"] = merged["expected_value"] > 0.0
    merged["negative_ev"] = merged["expected_value"] < 0.0
    merged["missing_player"] = merged["model_probability"].isna() | (merged["model_probability"] == 0.5) & merged["player_name"].isna()
    merged["duplicate_player"] = merged.duplicated(subset=["player_name", "book", "market"], keep=False)
    merged["missing_player"] = merged["missing_player"] | merged["player_name"].isna() | (merged["model_probability"] == 0.5)

    output_cols = [
        "player_name",
        "book",
        "team",
        "market",
        "line",
        "odds",
        "implied_probability",
        "model_probability",
        "expected_value",
        "edge_pct",
        "kelly_fraction",
        "positive_ev",
        "negative_ev",
        "missing_player",
        "duplicate_player",
    ]
    return merged[output_cols].reset_index(drop=True)


def build_odds_exports(odds_path: str | Path, slate_players: pd.DataFrame, output_dir: str | Path | None = None) -> dict[str, Path]:
    source_path = Path(odds_path)
    output_folder = Path(output_dir or EXPORT_DIR)
    output_folder.mkdir(parents=True, exist_ok=True)

    imported = import_odds_csv(source_path)
    matched = match_odds_to_players(imported, slate_players)
    model_scores = build_model_scores(slate_players)
    edges = calculate_edges(matched, model_scores)

    live_odds_path = export_odds_csv(matched, output_folder / "live_odds.csv")
    value_edges_path = export_odds_csv(edges, output_folder / "value_edges.csv")
    betting_edges_path = export_odds_csv(edges[edges["positive_ev"]].copy(), output_folder / "betting_edges.csv")
    return {
        "live_odds": live_odds_path,
        "value_edges": value_edges_path,
        "betting_edges": betting_edges_path,
    }
