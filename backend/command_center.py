import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s %(message)s")
logger = logging.getLogger(__name__)

from backend.collectors.schedule import collect_schedule
from backend.engine.betting_engine import run_workflow
from backend.utils import get_run_date


def main():
    run_date = get_run_date()
    logger.info("command_center: run_date=%s", run_date)
    try:
        n = collect_schedule(target_date=run_date)
        logger.info("command_center: schedule collected %d games for %s", n, run_date)
    except Exception as exc:
        logger.warning("command_center: schedule fetch failed (%s) — using existing DB data", exc.__class__.__name__)
    run_workflow()


if __name__ == "__main__":
    main()