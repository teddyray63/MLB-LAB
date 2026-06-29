import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.doctor.doctor import run_doctor
from backend.doctor.repair import suggest_repairs

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def main():
    result = run_doctor()
    logger.info("\n================ MLB-LAB DOCTOR ================\n")
    logger.info("Database: %s", "found" if (ROOT / "database" / "mlb_lab.db").exists() else "missing")

    if result.get("issues"):
        logger.warning("\nIssues:")
        for issue in result["issues"]:
            logger.warning("- %s", issue)
    else:
        logger.info("No issues detected.")

    if result.get("warnings"):
        logger.warning("\nWarnings:")
        for warning in result["warnings"]:
            logger.warning("- %s", warning)

    repairs = suggest_repairs(result)
    if repairs:
        logger.info("\nSuggested repairs:")
        for repair in repairs:
            logger.info("- %s", repair)


if __name__ == "__main__":
    main()
