import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.engine.betting_engine import run_workflow


def main():
    run_workflow()


if __name__ == "__main__":
    main()