from datetime import date
from pathlib import Path
import json
import urllib.request

TODAY = date.today().isoformat()
SEASON = date.today().year
REPORT = Path("reports/mlb-lab-v2-daily-report.md")

PARK_SCORE = {
    "Coors Field": 20,
    "Sutter Health Park": 16,
    "Yankee Stadium": 15,
    "Citizens Bank Park": 15,
    "Truist Park": 14,
    "Globe Life Field": 14,
    "Chase Field": 13,
    "Comerica Park": 11,
    "T-Mobile Park": 10,
    "Tropicana Field": 10,
    "Daikin Park": 10,
    "loanDepot park": 10,
    "Kauffman Stadium": 8,
    "Wrigley Field": 6,
}

def get_json(url):
    with urllib.request.urlopen(url, timeout=25) as r:
        return json.loads(r.read().decode())

def safe(v):
    return "—" if v in [None, "", "null"] else v

def fnum(v):
    try:
        return float(v)
    except:
        return 0.0

def pitcher(team):
    p = team.get("probablePitcher")
    if not p:
        return {"id": None, "name": "TBD", "hand": "—"}
    return {
        "id": p.get("id"),
        "name": p.get("fullName", "TBD"),
        "hand": p.get("pitchHand", {}).get("code", "—"),
    }

def pitcher_stats(pid):
    if not pid:
        return {}
    url = f"https://statsapi.mlb.com/api/v1/people/{pid}?hydrate=stats(group=[pitching],type=[season],season={SEASON})"
    try:
        data = get_json(url)
        splits = data["people"][0]["stats"][0].get("splits", [])
        return splits[0].get("stat", {}) if splits else {}
    except:
        return {}

def pitcher_risk(s):
    era = fnum(s.get("era"))
    whip = fnum(s.get("whip"))
    hr9 = fnum(s.get("homeRunsPer9"))
    bb9 = fnum(s.get("walksPer9Inn"))
    k9 = fnum(s.get("strikeoutsPer9Inn"))

    score = 8
    if era >= 5: score += 6
    elif era >= 4.25: score += 4
    elif era >= 3.75: score += 2

    if whip >= 1.45: score += 5
    elif whip >= 1.30: score += 3
    elif whip >= 1.20: score += 1

    if hr9 >= 1.6: score += 5
    elif hr9 >= 1.2: score += 3
    elif hr9 >= 0.9: score += 1

    if bb9 >= 3.8: score += 3
    elif bb9 >= 3.0: score += 2

    if k9 and k9 < 6.5: score += 3
    elif k9 and k9 < 8: score += 1

    return min(score, 25)

def team_stats(team_id):
    url = f"https://statsapi.mlb.com/api/v1/teams/{team_id}/stats?stats=season&group=hitting&season={SEASON}"
    try:
        data = get_json(url)
        return data["stats"][0]["splits"][0]["stat"]
    except:
        return {}

def offense_score(s):
    ops = fnum(s.get("ops"))
    hr = fnum(s.get("homeRuns"))
    avg = fnum(s.get("avg"))

    score = 8
    if ops >= .780: score += 6
    elif ops >= .730: score += 4
    elif ops >= .700: score += 2

    if avg >= .260: score += 3
    elif avg >= .245: score += 2

    if hr >= 100: score += 3
    elif hr >= 80: score += 2

    return min(score, 20)

def tier(total):
    if total >= 75: return "Priority"
    if total >= 60: return "Watch"
    if total >= 45: return "Low"
    return "Ignore"

def stat_table(title, p, s, risk):
    return f"""
### {title}: {p['name']} ({p['hand']})

| Stat | Value |
|---|---:|
| ERA | {safe(s.get("era"))} |
| WHIP | {safe(s.get("whip"))} |
| K/9 | {safe(s.get("strikeoutsPer9Inn"))} |
| BB/9 | {safe(s.get("walksPer9Inn"))} |
| HR/9 | {safe(s.get("homeRunsPer9"))} |
| Innings | {safe(s.get("inningsPitched"))} |
| Hits Allowed | {safe(s.get("hits"))} |
| Runs Allowed | {safe(s.get("runs"))} |
| HR Allowed | {safe(s.get("homeRuns"))} |
| Pitcher Risk | {risk} |
"""

def main():
    schedule = get_json(
        f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={TODAY}&hydrate=probablePitcher,venue,team"
    )

    games = []

    for day in schedule.get("dates", []):
        for g in day.get("games", []):
            away_team = g["teams"]["away"]["team"]
            home_team = g["teams"]["home"]["team"]

            away_p = pitcher(g["teams"]["away"])
            home_p = pitcher(g["teams"]["home"])

            away_ps = pitcher_stats(away_p["id"])
            home_ps = pitcher_stats(home_p["id"])

            away_ts = team_stats(away_team["id"])
            home_ts = team_stats(home_team["id"])

            env = PARK_SCORE.get(g["venue"]["name"], 10)
            away_risk = pitcher_risk(away_ps)
            home_risk = pitcher_risk(home_ps)
            pitcher_score = max(away_risk, home_risk)

            away_off = offense_score(away_ts)
            home_off = offense_score(home_ts)
            offense = max(away_off, home_off)

            matchup = 10
            if pitcher_score >= 20 and offense >= 15:
                matchup = 20
            elif pitcher_score >= 16 and offense >= 12:
                matchup = 16
            elif pitcher_score >= 13:
                matchup = 12

            total = env + pitcher_score + offense + matchup

            games.append({
                "game": f"{away_team['name']} @ {home_team['name']}",
                "away": away_team["name"],
                "home": home_team["name"],
                "park": g["venue"]["name"],
                "time": g.get("gameDate", "—"),
                "away_p": away_p,
                "home_p": home_p,
                "away_ps": away_ps,
                "home_ps": home_ps,
                "away_ts": away_ts,
                "home_ts": home_ts,
                "away_risk": away_risk,
                "home_risk": home_risk,
                "env": env,
                "pitcher": pitcher_score,
                "offense": offense,
                "matchup": matchup,
                "total": total,
                "tier": tier(total),
            })

    games.sort(key=lambda x: x["total"], reverse=True)

    report = f"""# MLB-LAB V2 Daily Report

Date: {TODAY}

Status: Complete automated MLB API report.

Purpose: dissect every game without manual CSVs, website scraping, or hard eliminations.

---

## Full Slate Index

| Rank | Game | Park | Pitchers | Env | Pitcher | Offense | Matchup | Total | Tier |
|---:|---|---|---|---:|---:|---:|---:|---:|---|
"""

    for i, g in enumerate(games, 1):
        report += f"| {i} | {g['game']} | {g['park']} | {g['away_p']['name']} vs {g['home_p']['name']} | {g['env']} | {g['pitcher']} | {g['offense']} | {g['matchup']} | {g['total']} | {g['tier']} |\n"

    report += "\n---\n\n# Game Cards\n"

    for i, g in enumerate(games, 1):
        report += f"""

---

## {i}. {g['game']} — {g['tier']} ({g['total']})

### Game Context

| Field | Value |
|---|---|
| Park | {g['park']} |
| Time | {g['time']} |
| Environment Score | {g['env']} |
| Pitcher Score | {g['pitcher']} |
| Offense Score | {g['offense']} |
| Matchup Score | {g['matchup']} |
| Total Score | {g['total']} |
| Tier | {g['tier']} |

{stat_table("Away SP", g["away_p"], g["away_ps"], g["away_risk"])}

{stat_table("Home SP", g["home_p"], g["home_ps"], g["home_risk"])}

### Team Offense Snapshot

| Team | AVG | OPS | HR | Runs | Offense Read |
|---|---:|---:|---:|---:|---:|
| {g['away']} | {safe(g['away_ts'].get('avg'))} | {safe(g['away_ts'].get('ops'))} | {safe(g['away_ts'].get('homeRuns'))} | {safe(g['away_ts'].get('runs'))} | {offense_score(g['away_ts'])} |
| {g['home']} | {safe(g['home_ts'].get('avg'))} | {safe(g['home_ts'].get('ops'))} | {safe(g['home_ts'].get('homeRuns'))} | {safe(g['home_ts'].get('runs'))} | {offense_score(g['home_ts'])} |

### MLB-LAB Read

- Best attack side: {"Home bats vs away SP" if g["away_risk"] >= g["home_risk"] else "Away bats vs home SP"}
- Primary pitcher concern: {g["away_p"]["name"] if g["away_risk"] >= g["home_risk"] else g["home_p"]["name"]}
- Why this game ranks here: park + pitcher risk + offense context + matchup pressure.
- Next manual check: pitch mix, confirmed lineup, weather/roof, prop market.
"""

    report += """

---

# Build Status

Complete V2 automation:

- Pulls today's full MLB slate
- Pulls probable pitchers
- Pulls pitcher season stats
- Pulls team offense stats
- Scores every game
- Builds every game card
- Produces one daily report

Next version can add true pitch-mix data once a stable source is selected.
"""

    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text(report, encoding="utf-8")
    print(f"Updated {REPORT}")

if __name__ == "__main__":
    main()
