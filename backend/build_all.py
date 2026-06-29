import logging
import subprocess
import sys

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

steps = [
    "backend/collectors/warehouse.py",
    "backend/collectors/statcast_hitters.py",
    "backend/features/build_hitter_features.py",
    "backend/features/build_daily_scores.py",
]

for step in steps:
    logger.info("RUNNING: %s", step)
    result = subprocess.run([sys.executable, step])

    if result.returncode != 0:
        logger.error("FAILED at: %s", step)
        sys.exit(result.returncode)

logger.info("ALL DATA BUILT SUCCESSFULLY")
logger.info("Now run: streamlit run frontend/app.py")