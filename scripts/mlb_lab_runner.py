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

ARSENAL_WATCH = {
    "Michael Lorenzen": 15,
    "Jack Perkins": 15,
    "Kai-Wei Teng": 14,
    "Slade Cecconi": 14,
    "Ryan Gusto": 13,
    "Keider Montero": 13,
    "Robert Gasser": 12,
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

def score_arsenal(away_pitcher, home_pitcher):
    return max(
        ARSENAL_WATCH.get(away_pitcher, 8),
        ARSENAL_WATCH.get(home_pitcher, 8),
    )

def score_matchup(env_score, pitcher_score):
    if env_score >= 15 and pitcher_score >= 18:
        return 16
    if env_score >= 13 and pitcher_score >= 10:
        return 12
    if pitcher_score >= 18:
        return 11
    return 8

def score_savant_placeholder(total_before_savant):
    if total_before_savant >= 65:
        return 12
    if total_before_savant >= 55:
        return 10
    if total_before_savant >= 45:
        return 8
    return 6

def tier(total):
    if total >= 70:
        return "Priority"
    if total >= 55:
        return "Watch"
    if total >= 40:
        return "Low"
    return "Ignore"

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

            env = ENVIRONMENT_SCORES.get(venue, 10)
            pitcher = max(score_pitcher(away_pitcher), score_pitcher(home_pitcher))
            arsenal = score_arsenal(away_pitcher, home_pitcher)
            matchup = score_matchup(env, pitcher)

            before_savant = env + pitcher + arsenal + matchup
            savant = score_savant_placeholder(before_savant)

            total = before_savant + savant

            games.append({
                "game": f"{away} @ {home}",
                "venue": venue,
                "pitchers": f"{away_pitcher} vs {home_pitcher}",
                "env": env,
                "pitcher": pitcher,
                "arsenal": arsenal,
                "matchup": matchup,
                "savant": savant,
                "total": total,
                "tier": tier(total),
            })

    games = sorted(games, key=lambda x: x["total"], reverse=True)

    report = f"""# MLB-LAB V1 Run 001

Status: Full Game Scoring Active

Date: {TODAY}

## Objective

Run every MLB game through the MLB-LAB V1 scoring system.

## Scoring Model

| Layer | Points |
|---|---:|
| Environment | 20 |
| Pitcher Vulnerability | 25 |
| Pitch Arsenal | 20 |
| Batter Matchup | 20 |
| Savant Confirmation | 15 |

No hard eliminations. Every game receives a score.

---

## Full Slate Scoreboard

| Rank | Game | Park | Probable Pitchers | Env | Pitcher | Arsenal | Matchup | Savant | Total | Tier |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
"""

    for i, g in enumerate(games, 1):
        report += (
            f"| {i} | {g['game']} | {g['venue']} | {g['pitchers']} | "
            f"{g['env']} | {g['pitcher']} | {g['arsenal']} | "
            f"{g['matchup']} | {g['savant']} | {g['total']} | {g['tier']} |\n"
        )

    priority = [g for g in games if g["tier"] == "Priority"]
    watch = [g for g in games if g["tier"] == "Watch"]

    report += """

---

## Priority Games

"""

    if priority:
        for g in priority:
            report += f"- {g['game']} — {g['total']} total\n"
    else:
        report += "- None\n"

    report += """

## Watch Games

"""

    if watch:
        for g in watch:
            report += f"- {g['game']} — {g['total']} total\n"
    else:
        report += "- None\n"

    report += """

## Notes

This is a full-slate game scoring engine.

Current automated layers:

- Schedule
- Probable pitchers
- Environment score
- Pitcher vulnerability score
- Pitch arsenal placeholder score
- Matchup placeholder score
- Savant placeholder score

Next upgrade:
Replace placeholder Arsenal / Matchup / Savant scores with real Statcast and batter data.
"""

    REPORT_PATH.write_text(report)
    print(f"Updated {REPORT_PATH}")

if __name__ == "__main__":
    main()
