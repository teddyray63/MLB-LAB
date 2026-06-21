from datetime import date, timedelta
from pathlib import Path
from collections import Counter, defaultdict
import csv
import io
import json
import urllib.parse
import urllib.request

TODAY = date.today()
TODAY_STR = TODAY.isoformat()
SEASON = TODAY.year
START_30 = (TODAY - timedelta(days=30)).isoformat()

REPORT_PATH = Path("reports/mlb-lab-v2-daily-report.md")

SCHEDULE_URL = (
    f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={TODAY_STR}"
    "&hydrate=probablePitcher,venue,team"
)

PARK_SCORE = {
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
    with urllib.request.urlopen(url, timeout=25) as r:
        return json.loads(r.read().decode())

def fetch_text(url):
    with urllib.request.urlopen(url, timeout=40) as r:
        return r.read().decode()

def safe(v, default="—"):
    return default if v in [None, "", "null"] else v

def num(v, default=0.0):
    try:
        return float(v)
    except Exception:
        return default

def get_pitcher(team):
    p = team.get("probablePitcher")
    if not p:
        return {"id": None, "name": "TBD", "hand": "—"}
    return {
        "id": p.get("id"),
        "name": p.get("fullName", "TBD"),
        "hand": p.get("pitchHand", {}).get("code", "—"),
    }

def pitcher_season_stats(pid):
    if not pid:
        return {}
    url = (
        f"https://statsapi.mlb.com/api/v1/people/{pid}"
        f"?hydrate=stats(group=[pitching],type=[season],season={SEASON})"
    )
    try:
        data = fetch_json(url)
        splits = data["people"][0].get("stats", [{}])[0].get("splits", [])
        return splits[0].get("stat", {}) if splits else {}
    except Exception:
        return {}

def pitcher_risk(stats):
    era = num(stats.get("era"))
    whip = num(stats.get("whip"))
    hr9 = num(stats.get("homeRunsPer9"))
    bb9 = num(stats.get("walksPer9Inn"))
    k9 = num(stats.get("strikeoutsPer9Inn"))

    score = 8

    if era >= 5.00: score += 6
    elif era >= 4.25: score += 4
    elif era >= 3.75: score += 2

    if whip >= 1.45: score += 5
    elif whip >= 1.30: score += 3
    elif whip >= 1.20: score += 1

    if hr9 >= 1.60: score += 5
    elif hr9 >= 1.20: score += 3
    elif hr9 >= 0.90: score += 1

    if bb9 >= 3.8: score += 3
    elif bb9 >= 3.0: score += 2

    if k9 and k9 < 6.5: score += 3
    elif k9 and k9 < 8.0: score += 1

    return min(score, 25)

def savant_pitch_mix(pid):
    if not pid:
        return {"sample": 0, "top": [], "arsenal_score": 8, "note": "No pitcher ID"}

    params = {
        "all": "true",
        "player_type": "pitcher",
        "game_date_gt": START_30,
        "game_date_lt": TODAY_STR,
        "pitchers_lookup[]": str(pid),
        "hfGT": "R|",
        "type": "details",
    }

    url = "https://baseballsavant.mlb.com/statcast_search/csv?" + urllib.parse.urlencode(params)

    try:
        text = fetch_text(url)
        rows = list(csv.DictReader(io.StringIO(text)))
    except Exception:
        return {"sample": 0, "top": [], "arsenal_score": 8, "note": "Savant pull failed"}

    if not rows:
        return {"sample": 0, "top": [], "arsenal_score": 8, "note": "No recent Savant rows"}

    counts = Counter(r.get("pitch_type", "UNK") or "UNK" for r in rows)
    total = sum(counts.values())

    pitch_data = defaultdict(lambda: {"n": 0, "ev": [], "xwoba": [], "hard": 0})

    for r in rows:
        pt = r.get("pitch_type", "UNK") or "UNK"
        pitch_data[pt]["n"] += 1

        ev = num(r.get("launch_speed"), None)
        if ev is not None and ev > 0:
            pitch_data[pt]["ev"].append(ev)
            if ev >= 95:
                pitch_data[pt]["hard"] += 1

        xwoba = num(r.get("estimated_woba_using_speedangle"), None)
        if xwoba is not None and xwoba > 0:
            pitch_data[pt]["xwoba"].append(xwoba)

    top = []
    arsenal_score = 8

    for pt, c in counts.most_common(5):
        d = pitch_data[pt]
        usage = c / total
        avg_ev = sum(d["ev"]) / len(d["ev"]) if d["ev"] else 0
        avg_xwoba = sum(d["xwoba"]) / len(d["xwoba"]) if d["xwoba"] else 0
        hard_rate = d["hard"] / len(d["ev"]) if d["ev"] else 0

        pitch_score = 6
        if usage >= 0.25: pitch_score += 4
        elif usage >= 0.15: pitch_score += 2

        if avg_xwoba >= .420: pitch_score += 6
        elif avg_xwoba >= .350: pitch_score += 4
        elif avg_xwoba >= .290: pitch_score += 2

        if avg_ev >= 93: pitch_score += 4
        elif avg_ev >= 88: pitch_score += 2

        if hard_rate >= .48: pitch_score += 4
        elif hard_rate >= .40: pitch_score += 2

        arsenal_score = max(arsenal_score, min(pitch_score, 20))

        top.append({
            "pitch": pt,
            "usage": round(usage * 100, 1),
            "avg_ev": round(avg_ev, 1) if avg_ev else "—",
            "xwoba": round(avg_xwoba, 3) if avg_xwoba else "—",
            "hard": round(hard_rate * 100, 1) if hard_rate else "—",
        })

    return {
        "sample": total,
        "top": top,
        "arsenal_score": arsenal_score,
        "note": "Live Baseball Savant last-30 pitch sample",
    }

def boxscore_lineup(game_pk, side):
    try:
        data = fetch_json(f"https://statsapi.mlb.com/api/v1/game/{game_pk}/boxscore")
        players = data["teams"][side]["players"]
    except Exception:
        return []

    lineup = []
    for _, p in players.items():
        order = p.get("battingOrder")
        if order:
            lineup.append((int(order), p["person"]["fullName"], p.get("position", {}).get("abbreviation", "—")))

    lineup.sort()
    return lineup

def matchup_score(env, pitcher_risk_score, arsenal_score, lineup_known):
    score = 8
    if env >= 15: score += 4
    if pitcher_risk_score >= 18: score += 4
    if arsenal_score >= 15: score += 4
    if lineup_known: score += 2
    return min(score, 20)

def savant_confirm(arsenal_a, arsenal_b):
    sample = arsenal_a["sample"] + arsenal_b["sample"]
    if sample >= 700: return 15
    if sample >= 400: return 12
    if sample >= 150: return 9
    return 6

def tier(total):
    if total >= 75: return "Priority"
    if total >= 60: return "Watch"
    if total >= 45: return "Low"
    return "Ignore"

def pitch_table(pitches):
    if not pitches:
        return "| Pitch | Usage | EV | xwOBA | HardHit% |\n|---|---:|---:|---:|---:|\n| — | — | — | — | — |\n"
    s = "| Pitch | Usage% | EV | xwOBA | HardHit% |\n|---|---:|---:|---:|---:|\n"
    for p in pitches:
        s += f"| {p['pitch']} | {p['usage']} | {p['avg_ev']} | {p['xwoba']} | {p['hard']} |\n"
    return s

def lineup_table(lineup):
    if not lineup:
        return "Lineup not confirmed through MLB API at run time.\n"
    s = "| Order | Player | Pos |\n|---:|---|---|\n"
    for order, name, pos in lineup:
        s += f"| {order} | {name} | {pos} |\n"
    return s

def main():
    data = fetch_json(SCHEDULE_URL)
    games = []

    for day in data.get("dates", []):
        for game in day.get("games", []):
            game_pk = game["gamePk"]
            away = game["teams"]["away"]["team"]["name"]
            home = game["teams"]["home"]["team"]["name"]
            venue = game["venue"]["name"]
            game_time = game.get("gameDate", "—")

            away_p = get_pitcher(game["teams"]["away"])
            home_p = get_pitcher(game["teams"]["home"])

            away_stats = pitcher_season_stats(away_p["id"])
            home_stats = pitcher_season_stats(home_p["id"])

            away_risk = pitcher_risk(away_stats)
            home_risk = pitcher_risk(home_stats)
            pitcher_score = max(away_risk, home_risk)

            away_arsenal = savant_pitch_mix(away_p["id"])
            home_arsenal = savant_pitch_mix(home_p["id"])
            arsenal_score = max(away_arsenal["arsenal_score"], home_arsenal["arsenal_score"])

            away_lineup = boxscore_lineup(game_pk, "away")
            home_lineup = boxscore_lineup(game_pk, "home")
            lineup_known = bool(away_lineup or home_lineup)

            env = PARK_SCORE.get(venue, 10)
            matchup = matchup_score(env, pitcher_score, arsenal_score, lineup_known)
            savant = savant_confirm(away_arsenal, home_arsenal)

            total = env + pitcher_score + arsenal_score + matchup + savant
            game_tier = tier(total)

            games.append({
                "game": f"{away} @ {home}",
                "away": away,
                "home": home,
                "venue": venue,
                "time": game_time,
                "away_p": away_p,
                "home_p": home_p,
                "away_stats": away_stats,
                "home_stats": home_stats,
                "away_risk": away_risk,
                "home_risk": home_risk,
                "away_arsenal": away_arsenal,
                "home_arsenal": home_arsenal,
                "away_lineup": away_lineup,
                "home_lineup": home_lineup,
                "env": env,
                "pitcher_score": pitcher_score,
                "arsenal_score": arsenal_score,
                "matchup": matchup,
                "savant": savant,
                "total": total,
                "tier": game_tier,
            })

    games.sort(key=lambda x: x["total"], reverse=True)

    report = f"""# MLB-LAB V2 Daily Dissection Report

Date: {TODAY_STR}

Status: Automated full-slate game dissection.

Purpose: show every game the way a research dashboard would, without building a website.

Framework: six-gate betting signal hierarchy converted into game-by-game intelligence sections.

---

## Slate Index

| Rank | Game | Park | Away SP | Home SP | Env | Pitcher | Arsenal | Matchup | Savant | Total | Tier |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
"""

    for i, g in enumerate(games, 1):
        report += (
            f"| {i} | {g['game']} | {g['venue']} | {g['away_p']['name']} | {g['home_p']['name']} | "
            f"{g['env']} | {g['pitcher_score']} | {g['arsenal_score']} | {g['matchup']} | "
            f"{g['savant']} | {g['total']} | {g['tier']} |\n"
        )

    report += "\n---\n\n# Game Dissection Cards\n"

    for i, g in enumerate(games, 1):
        a, h = g["away_stats"], g["home_stats"]

        report += f"""

---

## {i}. {g['game']} — {g['tier']} ({g['total']})

### Game Context

| Field | Value |
|---|---|
| Park | {g['venue']} |
| Time | {g['time']} |
| Environment Score | {g['env']} |
| Pitcher Score | {g['pitcher_score']} |
| Arsenal Score | {g['arsenal_score']} |
| Matchup Score | {g['matchup']} |
| Savant Confidence | {g['savant']} |

---

### {g['away_p']['name']} Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | {g['away_p']['hand']} |
| ERA | {safe(a.get('era'))} |
| WHIP | {safe(a.get('whip'))} |
| K/9 | {safe(a.get('strikeoutsPer9Inn'))} |
| BB/9 | {safe(a.get('walksPer9Inn'))} |
| HR/9 | {safe(a.get('homeRunsPer9'))} |
| Vulnerability Score | {g['away_risk']} |

#### Pitch Mix / Damage Profile

{pitch_table(g['away_arsenal']['top'])}

Savant note: {g['away_arsenal']['note']}  
Sample: {g['away_arsenal']['sample']} pitches

---

### {g['home_p']['name']} Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | {g['home_p']['hand']} |
| ERA | {safe(h.get('era'))} |
| WHIP | {safe(h.get('whip'))} |
| K/9 | {safe(h.get('strikeoutsPer9Inn'))} |
| BB/9 | {safe(h.get('walksPer9Inn'))} |
| HR/9 | {safe(h.get('homeRunsPer9'))} |
| Vulnerability Score | {g['home_risk']} |

#### Pitch Mix / Damage Profile

{pitch_table(g['home_arsenal']['top'])}

Savant note: {g['home_arsenal']['note']}  
Sample: {g['home_arsenal']['sample']} pitches

---

### Lineup Status

#### {g['away']} Lineup

{lineup_table(g['away_lineup'])}

#### {g['home']} Lineup

{lineup_table(g['home_lineup'])}

---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: {"Home lineup vs away SP" if g['away_risk'] >= g['home_risk'] else "Away lineup vs home SP"}
- Primary pitcher concern: {g['away_p']['name'] if g['away_risk'] >= g['home_risk'] else g['home_p']['name']}
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence
"""

    report += """

---

# End State

This is the complete V2 report:

- every game
- probable pitchers
- pitcher stats
- pitch-mix damage view
- lineup status
- ranked slate index
- game-by-game research cards

No website required.
No manual CSVs required.
"""

    REPORT_PATH.parent.mkdir(exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(f"Updated {REPORT_PATH}")

if __name__ == "__main__":
    main()
