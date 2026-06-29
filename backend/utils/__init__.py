import os
from datetime import date
from typing import Any


def get_run_date() -> str:
    """Return the run date as YYYY-MM-DD.

    Uses MLB_LAB_RUN_DATE env var when set, otherwise today's date.
    """
    override = os.getenv("MLB_LAB_RUN_DATE", "").strip()
    if override:
        return override
    return date.today().strftime("%Y-%m-%d")


def normalize_name(name: Any) -> str:
    if not isinstance(name, str):
        return ""
    name = name.strip()
    if "," in name:
        last, first = [x.strip() for x in name.split(",", 1)]
        return f"{first} {last}".lower()
    return name.lower()


def nz(v: Any) -> Any:
    return 0 if v is None else v
