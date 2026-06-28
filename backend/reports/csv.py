from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
EXPORT_DIR = ROOT / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def write_text_export(rows: List[Dict[str, Any]], filename: str) -> Path:
    path = EXPORT_DIR / filename
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(str(row) + "\n")
    return path
