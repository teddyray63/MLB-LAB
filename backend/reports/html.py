from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent.parent
EXPORT_DIR = ROOT / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def write_html_report(path: Path, lines: List[str]) -> Path:
    html = "<html><body><pre>" + "\n".join(lines) + "</pre></body></html>"
    path.write_text(html, encoding="utf-8")
    return path
