from pathlib import Path
from typing import Any, Dict, Optional

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
EXPORT_DIR = ROOT / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

SUPPORTED_BOOKS = {
    "draftkings": "DraftKings",
    "dk": "DraftKings",
    "fanduel": "FanDuel",
    "fd": "FanDuel",
    "betmgm": "BetMGM",
    "mgm": "BetMGM",
    "caesars": "Caesars",
    "caesar": "Caesars",
    "caesars sportsbook": "Caesars",
}

BOOK_ALIASES = {value.lower(): value for value in SUPPORTED_BOOKS.values()}
BOOK_ALIASES.update(SUPPORTED_BOOKS)

COLUMN_ALIASES = {
    "book": ["book", "sportsbook", "bookmaker", "site", "book_name", "operator"],
    "player_name": ["player_name", "player", "name", "player_name_raw", "player_name_display"],
    "team": ["team", "team_name", "club", "team_abbr"],
    "market": ["market", "bet_type", "prop", "prop_type", "market_type"],
    "line": ["line", "lines", "threshold", "total", "line_value", "market_line"],
    "odds": ["odds", "american_odds", "price", "american", "odds_value"],
}


def _normalize_header(name: Any) -> str:
    if not isinstance(name, str):
        return ""
    return "".join(ch.lower() for ch in name if ch.isalnum())


def _resolve_column(columns: list[str], canonical: str) -> Optional[str]:
    aliases = COLUMN_ALIASES.get(canonical, [])
    normalized_lookup = {_normalize_header(col): col for col in columns}
    for alias in aliases:
        if _normalize_header(alias) in normalized_lookup:
            return normalized_lookup[_normalize_header(alias)]
    return None


def _normalize_book_name(value: Any) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return "Unknown"
    text = str(value).strip()
    if not text:
        return "Unknown"
    lowered = text.lower()
    if lowered in BOOK_ALIASES:
        return BOOK_ALIASES[lowered]
    return text


def import_odds_csv(path: str | Path) -> pd.DataFrame:
    source_path = Path(path)
    if not source_path.exists():
        return pd.DataFrame(columns=["book", "player_name", "team", "market", "line", "odds", "source_file"])

    raw_df = pd.read_csv(source_path)
    if raw_df.empty:
        return pd.DataFrame(columns=["book", "player_name", "team", "market", "line", "odds", "source_file"])

    resolved = {}
    columns = list(raw_df.columns)
    for canonical in COLUMN_ALIASES:
        resolved[canonical] = _resolve_column(columns, canonical)

    result = pd.DataFrame(
        {
            "book": raw_df[resolved["book"]].fillna("Unknown") if resolved["book"] else ["Unknown"] * len(raw_df),
            "player_name": raw_df[resolved["player_name"]].fillna("") if resolved["player_name"] else [""] * len(raw_df),
            "team": raw_df[resolved["team"]].fillna("") if resolved["team"] else [""] * len(raw_df),
            "market": raw_df[resolved["market"]].fillna("") if resolved["market"] else [""] * len(raw_df),
            "line": raw_df[resolved["line"]].fillna("") if resolved["line"] else [""] * len(raw_df),
            "odds": raw_df[resolved["odds"]].fillna("") if resolved["odds"] else [""] * len(raw_df),
        }
    )
    result["book"] = result["book"].apply(_normalize_book_name)
    result["player_name"] = result["player_name"].astype(str).str.strip()
    result["team"] = result["team"].astype(str).str.strip()
    result["market"] = result["market"].astype(str).str.strip()
    result["line"] = pd.to_numeric(result["line"], errors="coerce")
    result["odds"] = pd.to_numeric(result["odds"], errors="coerce")
    result["source_file"] = str(source_path)
    result = result.dropna(subset=["player_name"]).reset_index(drop=True)
    return result


def export_odds_csv(df: pd.DataFrame, path: str | Path) -> Path:
    target_path = Path(path)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(target_path, index=False)
    return target_path
