"""Statcast event source loading — offline fixtures or in-memory live pull (no cache writes)."""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any

StatcastEvents = list[dict[str, Any]]


def events_from_fixture(path: Path) -> StatcastEvents:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and "events" in payload:
        events = payload["events"]
    elif isinstance(payload, list):
        events = payload
    else:
        raise ValueError(f"Unsupported statcast fixture shape: {path}")
    if not isinstance(events, list):
        raise ValueError(f"Statcast fixture events must be a list: {path}")
    return [row for row in events if isinstance(row, dict)]


def fetch_statcast_events(
    slate_date: str,
    *,
    lookback_days: int = 120,
) -> StatcastEvents:
    """Fetch Statcast pitch events in memory via pybaseball — no cache writes."""
    try:
        from pybaseball import statcast
    except ImportError as exc:
        raise RuntimeError("pybaseball is required for live Statcast fetch") from exc

    end = date.fromisoformat(slate_date)
    start = end - timedelta(days=lookback_days)
    frame = statcast(start_dt=start.isoformat(), end_dt=end.isoformat())
    if frame is None or frame.empty:
        return []
    records = frame.to_dict(orient="records")
    normalized: StatcastEvents = []
    for row in records:
        item: dict[str, Any] = {}
        for key, value in row.items():
            if value is None or (isinstance(value, float) and str(value) == "nan"):
                item[key] = None
            elif hasattr(value, "item"):
                try:
                    item[key] = value.item()
                except (ValueError, AttributeError):
                    item[key] = value
            else:
                item[key] = value
        normalized.append(item)
    return normalized


def merge_event_fixtures(*paths: Path) -> StatcastEvents:
    merged: StatcastEvents = []
    for path in paths:
        merged.extend(events_from_fixture(path))
    return merged
