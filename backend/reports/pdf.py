from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent.parent
EXPORT_DIR = ROOT / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def write_pdf_report(path: Path, lines: List[str]) -> Path:
    content = "\n".join(lines)
    path.write_bytes(f"%PDF-1.4\n%{content}\n".encode("utf-8"))
    return path
