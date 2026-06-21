from datetime import date
from pathlib import Path

TODAY = date.today().isoformat()

REPORT_PATH = Path("reports/mlb-lab-v1-run-001.md")

SCORING = {
    "Environment": 20,
    "Pitcher Vulnerability": 25,
    "Pitch Arsenal": 20,
    "Batter Matchup": 20,
    "Savant Confirmation": 15,
}

report = f"""# MLB-LAB V1 Run 001

Status: Automated Shell Active

Date: {TODAY}

## Objective

Run MLB-LAB V1 using the system already built in this repo.

## Scoring Model

| Layer | Points |
|---|---:|
"""

for layer, points in SCORING.items():
    report += f"| {layer} | {points} |\n"

report += """

## Current Automation Status

This script now controls the report generation.

Next upgrades:
1. Pull schedule
2. Pull probable pitchers
3. Add weather
4. Add pitcher scoring
5. Add hitter candidates

## Output

No manual markdown rebuilding needed.
"""

REPORT_PATH.write_text(report)

print(f"Updated {REPORT_PATH}")
