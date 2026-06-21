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
    "Comerica Park": 11,
    "UNIQLO Field at Dodger Stadium": 10,
    "Dodger Stadium": 10,
    "T-Mobile Park": 10,
    "Tropicana Field": 10,
    "Daikin Park": 10,
    "loanDepot park": 10,
    "Kauffman Stadium": 8,
    "Wrigley Field": 6,
}

WEAK_PITCHER_NAMES = {
    "Michael Lorenzen",
    "Jack Perkins",
    "Kai-Wei Teng",
    "Slade Cecconi",
    "Ryan Gusto",
    "Keider Montero",
    "Robert Gasser",
}

STRONG_PITCHER_NAMES = {
    "Zack Wheeler",
    "Logan Gilbert",
    "Logan Webb",
    "Shota Imanaga",
    "Dylan Cease",
    "Nathan Eovaldi",
}

def fetch_json(url):
    with urllib.request.urlopen(url, timeout=20) as response:
        return json.loads(response.read().decode())

def pitcher_name(team_data):
    pitcher = team_data.get("probablePitcher")
    return pitcher.get("fullName", "TBD") if pitcher else "TBD"

def score_pitcher(name):
    if name == "TBD":
        return 5
    if name in WEAK_PITCHER_NAMES:
        return 18
    if name in STRONG_PITCHER_NAMES:
        return 6
    return 10

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

            away_pitcher_score = score_pitcher(away_pitcher)
            home_pitcher_score = score_pitcher(home_pitcher)
            pitcher_score = max(away_pitcher_score, home_pitcher_score)

            early_total = env_score + pitcher_score

            games.append({
                "game": f"{away} @ {home}",
                "venue": venue,
                "pitchers": f"{away_pitcher} vs {home_pitcher}",
                "env_score": env_score,
                "pitcher_score": pitcher_score,
                "early_total": early_total,
            })

    games = sorted(games, key=lambda x: x["early_total"], reverse=True)

    report = f"""# MLB-LAB V1 Run 001

Status: Automated Schedule + Environment + Pitcher Scoring Active

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

| Rank | Game | Park | Probable Pitchers | Env | Pitcher | Early Total |
|---:|---|---|---|---:|---:|---:|
"""

    for i, g in enumerate(games, 1):
        report += (
            f"| {i} | {g['game']} | {g['venue']} | {g['pitchers']} | "
            f"{g['env_score']} | {g['pitcher_score']} | {g['early_total']} |\n"
        )

    report += """

---

## Priority Games

These are ranked by early total:

Environment Score + Pitcher Vulnerability Score.

## Pitcher Scoring Notes

- TBD pitcher = 5
- Strong pitcher = 6
- Neutral known pitcher = 10
- Weak pitcher watchlist = 18

This is still an early scoring layer, not a final betting card.

## Next Upgrades

1. Add weather
2. Add pitch arsenal scoring
3. Add hitter candidate ranking
4. Add Savant confirmation
5. Generate final daily report

## Current Output

Automated MLB schedule pull is working.  
Environment scoring is working.  
Pitcher vulnerability scoring is working.
"""

    REPORT_PATH.write_text(report)
    print(f"Updated {REPORT_PATH}")

if __name__ == "__main__":
    main()
