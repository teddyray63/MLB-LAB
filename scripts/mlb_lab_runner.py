from datetime import date
from pathlib import Path
import json
import urllib.request

TODAY = date.today().isoformat()
REPORT_PATH = Path("reports/mlb-lab-v1-run-001.md")

URL = (
    f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={TODAY}"
    "&hydrate=probablePitcher,venue"
)

ENV = {
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

WEAK_PITCHERS = {
    "Michael Lorenzen",
    "Jack Perkins",
    "Kai-Wei Teng",
    "Slade Cecconi",
    "Ryan Gusto",
    "Keider Montero",
    "Robert Gasser",
}

STRONG_PITCHERS = {
    "Zack Wheeler",
    "Logan Gilbert",
    "Logan Webb",
    "Shota Imanaga",
    "Dylan Cease",
    "Nathan Eovaldi",
}

STRONG_OFFENSES = {
    "Los Angeles Dodgers",
    "New York Yankees",
    "Philadelphia Phillies",
    "Atlanta Braves",
    "Baltimore Orioles",
    "Arizona Diamondbacks",
}

WEAK_OFFENSES = {
    "Chicago White Sox",
    "Miami Marlins",
    "Washington Nationals",
    "Colorado Rockies",
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
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.loads(r.read().decode())

def pitcher_name(team):
    p = team.get("probablePitcher")
    return p.get("fullName", "TBD") if p else "TBD"

def pitcher_score(name):
    if name == "TBD":
        return 5
    if name in WEAK_PITCHERS:
        return 18
    if name in STRONG_PITCHERS:
        return 6
    return 10

def arsenal_score(away_p, home_p):
    return max(
        ARSENAL_WATCH.get(away_p, 8),
        ARSENAL_WATCH.get(home_p, 8),
    )

def offense_score(away, home):
    score = 10
    if away in STRONG_OFFENSES or home in STRONG_OFFENSES:
        score += 6
    if away in WEAK_OFFENSES and home in WEAK_OFFENSES:
        score -= 4
    return max(6, min(score, 20))

def matchup_score(env, pitcher, offense):
    score = 8
    if env >= 15:
        score += 4
    if pitcher >= 18:
        score += 4
    if offense >= 16:
        score += 4
    return min(score, 20)

def savant_score(env, pitcher, arsenal, matchup):
    pre = env + pitcher + arsenal + matchup
    if pre >= 65:
        return 15
    if pre >= 55:
        return 12
    if pre >= 45:
        return 9
    return 6

def tier(total):
    if total >= 75:
        return "Priority"
    if total >= 60:
        return "Watch"
    if total >= 45:
        return "Low"
    return "Ignore"

def action(tier_name):
    if tier_name == "Priority":
        return "Research props / lineup angles first"
    if tier_name == "Watch":
        return "Review after lineups confirm"
    if tier_name == "Low":
        return "Only check if market or lineup changes"
    return "Skip"

def main():
    data = fetch_json(URL)
    games = []

    for day in data.get("dates", []):
        for game in day.get("games", []):
            away = game["teams"]["away"]["team"]["name"]
            home = game["teams"]["home"]["team"]["name"]
            venue = game["venue"]["name"]

            away_p = pitcher_name(game["teams"]["away"])
            home_p = pitcher_name(game["teams"]["home"])

            env = ENV.get(venue, 10)
            pitcher = max(pitcher_score(away_p), pitcher_score(home_p))
            arsenal = arsenal_score(away_p, home_p)
            offense = offense_score(away, home)
            matchup = matchup_score(env, pitcher, offense)
            savant = savant_score(env, pitcher, arsenal, matchup)

            total = env + pitcher + arsenal + matchup + savant
            game_tier = tier(total)

            games.append({
                "game": f"{away} @ {home}",
                "park": venue,
                "pitchers": f"{away_p} vs {home_p}",
                "env": env,
                "pitcher": pitcher,
                "arsenal": arsenal,
                "offense": offense,
                "matchup": matchup,
                "savant": savant,
                "total": total,
                "tier": game_tier,
                "action": action(game_tier),
            })

    games.sort(key=lambda x: x["total"], reverse=True)

    report = f"""# MLB-LAB V1 Run 001

Status: Complete Full-Slate Automated Scoring

Date: {TODAY}

## Objective

Run every MLB game through the MLB-LAB V1 scoring system.

No hard eliminations. Every game receives a score.

## Full Slate Scoreboard

| Rank | Game | Park | Pitchers | Env | Pitcher | Arsenal | Offense | Matchup | Savant | Total | Tier | Action |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
"""

    for i, g in enumerate(games, 1):
        report += (
            f"| {i} | {g['game']} | {g['park']} | {g['pitchers']} | "
            f"{g['env']} | {g['pitcher']} | {g['arsenal']} | {g['offense']} | "
            f"{g['matchup']} | {g['savant']} | {g['total']} | {g['tier']} | {g['action']} |\n"
        )

    report += "\n## Priority Games\n\n"
    priority = [g for g in games if g["tier"] == "Priority"]
    report += "\n".join([f"- {g['game']} — {g['total']}" for g in priority]) or "- None"

    report += "\n\n## Watch Games\n\n"
    watch = [g for g in games if g["tier"] == "Watch"]
    report += "\n".join([f"- {g['game']} — {g['total']}" for g in watch]) or "- None"

    report += """

## What This Runner Now Does

- Pulls today's MLB schedule
- Pulls probable pitchers
- Scores every game
- Applies environment score
- Applies pitcher vulnerability score
- Applies pitch arsenal estimate
- Applies offense estimate
- Applies matchup estimate
- Applies Savant confirmation estimate
- Produces Priority / Watch / Low / Ignore tiers

## Important Note

This is a complete V1 engine.

It is not a final betting model.

Use Priority and Watch games as research targets.
"""

    REPORT_PATH.write_text(report)
    print(f"Updated {REPORT_PATH}")

if __name__ == "__main__":
    main()
