from datetime import date
from pathlib import Path
import json
import urllib.request

TODAY = date.today().isoformat()
YEAR = date.today().year
REPORT_PATH = Path("reports/mlb-lab-v1-run-001.md")

SCHEDULE_URL = (
    f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={TODAY}"
    "&hydrate=probablePitcher,venue,team"
)

PARK_SCORES = {
    "Coors Field": 20,
    "Sutter Health Park": 16,
    "Yankee Stadium": 15,
    "Citizens Bank Park": 15,
    "Truist Park": 14,
    "Globe Life Field": 14,
    "Chase Field": 13,
    "Comerica Park": 11,
    "Dodger Stadium": 10,
    "UNIQLO Field at Dodger Stadium": 10,
    "T-Mobile Park": 10,
    "Tropicana Field": 10,
    "Daikin Park": 10,
    "loanDepot park": 10,
    "Kauffman Stadium": 8,
    "Wrigley Field": 6,
}

def fetch_json(url):
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.loads(r.read().decode())

def safe(v, default="—"):
    return v if v not in [None, "", "null"] else default

def get_pitcher(team):
    p = team.get("probablePitcher")
    if not p:
        return {"name": "TBD", "id": None, "hand": "—"}
    return {
        "name": p.get("fullName", "TBD"),
        "id": p.get("id"),
        "hand": p.get("pitchHand", {}).get("code", "—"),
    }

def pitcher_stats(player_id):
    if not player_id:
        return {}

    url = (
        f"https://statsapi.mlb.com/api/v1/people/{player_id}"
        f"?hydrate=stats(group=[pitching],type=[season],season={YEAR})"
    )

    try:
        data = fetch_json(url)
        people = data.get("people", [])
        if not people:
            return {}

        splits = people[0].get("stats", [{}])[0].get("splits", [])
        if not splits:
            return {}

        return splits[0].get("stat", {})
    except Exception:
        return {}

def pitcher_vulnerability_score(stats):
    era = float(stats.get("era", 0) or 0)
    whip = float(stats.get("whip", 0) or 0)
    hr9 = float(stats.get("homeRunsPer9", 0) or 0)

    score = 10

    if era >= 5:
        score += 6
    elif era >= 4:
        score += 3

    if whip >= 1.4:
        score += 4
    elif whip >= 1.25:
        score += 2

    if hr9 >= 1.4:
        score += 5
    elif hr9 >= 1:
        score += 3

    return min(score, 25)

def game_tier(total):
    if total >= 70:
        return "Priority"
    if total >= 55:
        return "Watch"
    if total >= 40:
        return "Low"
    return "Ignore"

def main():
    data = fetch_json(SCHEDULE_URL)
    games = []

    for day in data.get("dates", []):
        for game in day.get("games", []):
            away_team = game["teams"]["away"]["team"]["name"]
            home_team = game["teams"]["home"]["team"]["name"]
            away_abbrev = game["teams"]["away"]["team"].get("abbreviation", "")
            home_abbrev = game["teams"]["home"]["team"].get("abbreviation", "")
            venue = game["venue"]["name"]
            game_time = game.get("gameDate", "")

            away_p = get_pitcher(game["teams"]["away"])
            home_p = get_pitcher(game["teams"]["home"])

            away_stats = pitcher_stats(away_p["id"])
            home_stats = pitcher_stats(home_p["id"])

            env_score = PARK_SCORES.get(venue, 10)
            away_vuln = pitcher_vulnerability_score(away_stats)
            home_vuln = pitcher_vulnerability_score(home_stats)
            pitcher_score = max(away_vuln, home_vuln)

            total = env_score + pitcher_score
            tier = game_tier(total)

            games.append({
                "away": away_team,
                "home": home_team,
                "away_abbrev": away_abbrev,
                "home_abbrev": home_abbrev,
                "game": f"{away_team} @ {home_team}",
                "venue": venue,
                "time": game_time,
                "away_pitcher": away_p,
                "home_pitcher": home_p,
                "away_stats": away_stats,
                "home_stats": home_stats,
                "env_score": env_score,
                "away_vuln": away_vuln,
                "home_vuln": home_vuln,
                "pitcher_score": pitcher_score,
                "total": total,
                "tier": tier,
            })

    games.sort(key=lambda g: g["total"], reverse=True)

    report = f"""# MLB-LAB Daily Game Dissection Report

Date: {TODAY}

Status: Full game-card report active.

Purpose: dissect every MLB game, not just find picks.

---

## Slate Index

| Rank | Game | Park | Away SP | Home SP | Env | Pitcher Risk | Total | Tier |
|---:|---|---|---|---|---:|---:|---:|---|
"""

    for i, g in enumerate(games, 1):
        report += (
            f"| {i} | {g['game']} | {g['venue']} | "
            f"{g['away_pitcher']['name']} | {g['home_pitcher']['name']} | "
            f"{g['env_score']} | {g['pitcher_score']} | {g['total']} | {g['tier']} |\n"
        )

    report += "\n---\n\n# Game Breakdown Cards\n"

    for i, g in enumerate(games, 1):
        a = g["away_stats"]
        h = g["home_stats"]

        report += f"""

---

## {i}. {g['game']}

### Game Context

| Field | Value |
|---|---|
| Park | {g['venue']} |
| Time | {g['time']} |
| Environment Score | {g['env_score']} |
| Pitcher Risk Score | {g['pitcher_score']} |
| Current Tier | {g['tier']} |

---

### Away Starting Pitcher: {g['away_pitcher']['name']} ({g['away_pitcher']['hand']})

| Stat | Value |
|---|---:|
| ERA | {safe(a.get('era'))} |
| WHIP | {safe(a.get('whip'))} |
| K/9 | {safe(a.get('strikeoutsPer9Inn'))} |
| BB/9 | {safe(a.get('walksPer9Inn'))} |
| HR/9 | {safe(a.get('homeRunsPer9'))} |
| Innings | {safe(a.get('inningsPitched'))} |
| Hits Allowed | {safe(a.get('hits'))} |
| Runs Allowed | {safe(a.get('runs'))} |
| Home Runs Allowed | {safe(a.get('homeRuns'))} |
| Vulnerability Score | {g['away_vuln']} |

#### Attack Questions

- Is this pitcher giving up hard contact?
- Is HR/9 elevated?
- Is WHIP creating traffic?
- Does opponent lineup have handedness advantage?
- What pitch type does this pitcher rely on most?
- Which hitters match that pitch type?

---

### Home Starting Pitcher: {g['home_pitcher']['name']} ({g['home_pitcher']['hand']})

| Stat | Value |
|---|---:|
| ERA | {safe(h.get('era'))} |
| WHIP | {safe(h.get('whip'))} |
| K/9 | {safe(h.get('strikeoutsPer9Inn'))} |
| BB/9 | {safe(h.get('walksPer9Inn'))} |
| HR/9 | {safe(h.get('homeRunsPer9'))} |
| Innings | {safe(h.get('inningsPitched'))} |
| Hits Allowed | {safe(h.get('hits'))} |
| Runs Allowed | {safe(h.get('runs'))} |
| Home Runs Allowed | {safe(h.get('homeRuns'))} |
| Vulnerability Score | {g['home_vuln']} |

#### Attack Questions

- Is this pitcher giving up hard contact?
- Is HR/9 elevated?
- Is WHIP creating traffic?
- Does opponent lineup have handedness advantage?
- What pitch type does this pitcher rely on most?
- Which hitters match that pitch type?

---

### Team vs Pitcher Research Block

#### {g['away']} hitters vs {g['home_pitcher']['name']}

Manual research fields:

| Hitter | Hand | Order | ISO | wOBA | Barrel% | HardHit% | Pitch Matchup | Notes |
|---|---|---:|---:|---:|---:|---:|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

#### {g['home']} hitters vs {g['away_pitcher']['name']}

Manual research fields:

| Hitter | Hand | Order | ISO | wOBA | Barrel% | HardHit% | Pitch Matchup | Notes |
|---|---|---:|---:|---:|---:|---:|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

---

### Pitch Arsenal Notes

Use your external tools here:

| Pitcher | Main Pitch | Secondary Pitch | Weak Pitch | Batter Type That Benefits |
|---|---|---|---|---|
| {g['away_pitcher']['name']} | TBD | TBD | TBD | TBD |
| {g['home_pitcher']['name']} | TBD | TBD | TBD | TBD |

---

### Market / Prop Context

| Market | Value |
|---|---|
| Game Total | TBD |
| Run Line | TBD |
| Team Totals | TBD |
| HR Props To Review | TBD |
| Strikeout Props To Review | TBD |

---

### MLB-LAB Notes

- Environment read:
- Pitcher vulnerability read:
- Lineup confirmation needed:
- Best research angle:
- Caution flags:
- Final lean:
"""

    report += """

---

# Final Notes

This report is intentionally built as a research lab.

It does not eliminate games.

It does not force picks.

It gives every game a structured dissection card so you can plug in:
- pitch mix
- hitter splits
- lineup order
- Barrel %
- HardHit %
- ISO
- wOBA
- prop market context
- final notes

The Slate Index is only the table of contents.
The game cards are the real lab.
"""

    REPORT_PATH.write_text(report)
    print(f"Updated {REPORT_PATH}")

if __name__ == "__main__":
    main()
