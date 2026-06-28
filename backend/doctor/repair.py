from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent.parent


def suggest_repairs(doctor_result: Dict[str, Any]) -> List[str]:
    suggestions: List[str] = []
    for issue in doctor_result.get("issues", []):
        if issue.startswith("Missing table"):
            suggestions.append(f"Create or restore the missing table. {issue}")
        elif issue.startswith("Missing export"):
            suggestions.append(f"Re-run python3 backend/command_center.py to generate {issue.split(': ', 1)[1]}")
        elif issue.startswith("No games found"):
            suggestions.append("Refresh the schedule data before generating today's slate")
        elif issue.startswith("No lineups"):
            suggestions.append("Refresh lineup data for today's games")
        elif issue.startswith("No daily_scores"):
            suggestions.append("Rebuild the daily_scores table from existing feature data")
        elif issue.startswith("Import issue"):
            suggestions.append("Install the missing Python dependency in the active environment")
        else:
            suggestions.append(f"Investigate and fix: {issue}")
    return suggestions
