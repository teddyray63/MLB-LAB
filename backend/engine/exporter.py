import json
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
EXPORT_DIR = ROOT / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def export_csv(df: pd.DataFrame, filename: str) -> Path:
    path = EXPORT_DIR / filename
    df.to_csv(path, index=False)
    return path


def export_json(payload: Dict[str, Any], filename: str) -> Path:
    path = EXPORT_DIR / filename
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def write_exports(rows: List[Dict[str, Any]], export_name: str) -> Path:
    if not rows:
        df = pd.DataFrame(columns=["section", "game", "player", "team", "market", "score", "grade", "confidence", "edge", "risk_note"])
    else:
        df = pd.DataFrame(rows)
    return export_csv(df, export_name)
