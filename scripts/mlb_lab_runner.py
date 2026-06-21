from datetime import date
from pathlib import Path
import json
import urllib.request

TODAY = date.today().isoformat()
REPORT_PATH = Path("reports/mlb-lab-v1-run-001.md")

MLB_SCHEDULE_URL = (
    f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={TODAY}"
    "&hydrate=probablePitcher,venue"
)

ENVIRONMENT_SCORES = {
    "Coors Field": 20,
    "Sutter Health Park": 16,
    "Yankee Stadium": 15,
    "Citizens Bank Park": 15,
    "Truist Park": 14,
    "Globe Life Field": 14,
    "Chase Field": 13,
    "Dodger Stadium": 11,
    "Comerica Park": 11,
    "T-Mobile Park": 10,
    "Tropicana Field": 10,
    "Daikin Park": 10,
    "loanDepot park": 10,
    "Kauffman Stadium": 8,
    "Wrigley Field": 6,
}

def fetch_json(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())

def pitcher_name(team_data):
    pitcher = team_data.get("probablePitcher")
    return pitcher.get("fullName", "TBD") if pitcher else "TBD"

def main():
    data = fetch_json(MLB_SCHEDULE_URL)
    games = []

    for day in data.get("dates", []):
        for game in day.get("games", []):
            away = game["teams"]["away"]["team"]["name"]
            home = game["teams"]["home"]["team"]["name"]
            venue = game["venue"]["name"]

            away_pitcher = pitcher_name(game["teams"]["away"])
            home_pitcher = pitcher_name(game["teams"]["home"])

            env_score = ENVIRONMENT_SCORES.get(venue, 10)

            games.append({
                "game": f"{away} @ {home}",
                "venue": venue,
                "pitchers": f"{away_pitcher} vs {home_pitcher}",
                "env_score": env_score,
            })

    games = sorted(games, key=lambda x: x["env_score"], reverse=True)

    report = f"""# MLB-LAB V1 Run 001

Status: Automated Schedule + Environment Active

Date: {TODAY}

## Objective

Run MLB-LAB V1 using the system already built in this repo.

## Scoring Model

| Layer | Points |
|---|---:|
| Environment | 20 |
| Pitcher Vulnerability | 25 |
| Pitch Arsenal | 20 |
| Batter Matchup | 20 |
| Savant Confirmation | 15 |

---

## Today's Slate

| Rank | Game | Park | Probable Pitchers | Environment Score |
|---:|---|---|---|---:|
"""

    for i, g in enumerate(games, 1):
        report += f"| {i} | {g['game']} | {g['venue']} | {g['pitchers']} | {g['env_score']} |\n"

    report += """

---

## Priority Games

These are ranked by environment score only.

Next upgrades:

1. Add weather
2. Add pitcher vulnerability scoring
3. Add pitch arsenal scoring
4. Add hitter candidate ranking
5. Generate final daily report

## Current Output

Automated MLB schedule pull is working.
Environment scoring is working.
"""

    REPORT_PATH.write_text(report)
    print(f"Updated {REPORT_PATH}")

if __name__ == "__main__":
    
    main()
