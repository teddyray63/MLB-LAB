import re
import unicodedata
from typing import Iterable

import pandas as pd


def normalize_player_name(value: object) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    if not text:
        return ""
    if "," in text:
        last, first = [segment.strip() for segment in text.split(",", 1)]
        text = f"{first} {last}"
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text).strip()
    return re.sub(r"\s+", " ", text)


def normalize_player_names(values: Iterable[object]) -> list[str]:
    return [normalize_player_name(value) for value in values]


def normalize_team_name(value: object) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()
