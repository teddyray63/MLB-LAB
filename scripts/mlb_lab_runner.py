from datetime import date, timedelta
from pathlib import Path
import requests
import pandas as pd
from pybaseball import statcast, batting_stats, pitching_stats

TODAY = date.today()
SEASON = TODAY.year
REPORT = Path("reports/mlb-lab-v4-v5-daily-report.md")

START = (TODAY - timedelta(days=45)).isoformat()
END = TODAY.isoformat()

def get_json(url):
    return requests.get(url, timeout=30).json()

def clean(x):
    return "—" if x is None or x == "" else x

def get_schedule():
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={TODAY}&hydrate=probablePitcher,venue,team"
    games = []
    data = get_json(url)

    for d in data.get("dates", []):
        for g in d.get("games", []):
            away = g["teams"]["away"]["team"]
            home = g["teams"]["home"]["team"]
            away_sp = g["teams"]["away"].get("probablePitcher", {})
            home_sp = g["teams"]["home"].get("probablePitcher", {})

            games.append({
                "game": f"{away['name']} @ {home['name']}",
                "away_team": away["name"],
                "home_team": home["name"],
                "away_id": away["id"],
                "home_id": home["id"],
                "park": g["venue"]["name"],
                "time": g.get("gameDate"),
                "away_sp": away_sp.get("fullName", "TBD"),
                "home_sp": home_sp.get("fullName", "TBD"),
                "away_sp_id": away_sp.get("id"),
                "home_sp_id": home_sp.get("id"),
            })

    return games

def load_statcast():
    try:
        return statcast(start_dt=START, end_dt=END)
    except Exception:
        return pd.DataFrame()

def load_fangraphs():
    try:
        bat = batting_stats(SEASON, qual=0)
    except Exception:
        bat = pd.DataFrame()

    try:
        pit = pitching_stats(SEASON, qual=0)
    except Exception:
        pit = pd.DataFrame()

    return bat, pit

def player_name_match(df, name):
    if df.empty or not name or name == "TBD":
        return pd.DataFrame()

    first_last = name.lower()
    parts = name.split()
    if len(parts) >= 2:
        savant_name = f"{parts[-1]}, {' '.join(parts[:-1])}".lower()
    else:
        savant_name = first_last

    if "player_name" in df.columns:
        return df[df["player_name"].str.lower().isin([first_last, savant_name])]

    return pd.DataFrame()

def pitcher_pitch_table(sc, pitcher_name):
    p = player_name_match(sc, pitcher_name)
    if p.empty:
        return "| Pitch | Batter Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | HardHit% | Whiff% |\n|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n| — | — | — | — | — | — | — | — | — | — | — |\n"

    rows = []
    total_pitches = len(p)

    for (pitch, stand), g in p.groupby(["pitch_type", "stand"]):
        events = g.dropna(subset=["events"])
        ab_events = events[~events["events"].isin(["walk", "hit_by_pitch", "sac_bunt", "sac_fly"])]
        ab = len(ab_events)

        singles = (events["events"] == "single").sum()
        doubles = (events["events"] == "double").sum()
        triples = (events["events"] == "triple").sum()
        hrs = (events["events"] == "home_run").sum()
        hits = singles + doubles + triples + hrs
        tb = singles + 2*doubles + 3*triples + 4*hrs

        avg = hits / ab if ab else 0
        slg = tb / ab if ab else 0
        iso = slg - avg if ab else 0
        woba = g["woba_value"].mean() if "woba_value" in g else 0
        xwoba = g["estimated_woba_using_speedangle"].mean() if "estimated_woba_using_speedangle" in g else 0

        hard = 0
        if "launch_speed" in g:
            bbe = g["launch_speed"].dropna()
            hard = (bbe >= 95).mean() if len(bbe) else 0

        whiff = 0
        if "description" in g:
            swings = g[g["description"].isin(["swinging_strike", "swinging_strike_blocked", "foul", "hit_into_play"])]
            whiffs = g[g["description"].isin(["swinging_strike", "swinging_strike_blocked"])]
            whiff = len(whiffs) / len(swings) if len(swings) else 0

        usage = len(g) / total_pitches if total_pitches else 0

        rows.append([
            pitch, stand, usage, len(g), avg, slg, iso, woba, xwoba, hard, whiff
        ])

    out = "| Pitch | Batter Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | HardHit% | Whiff% |\n"
    out += "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n"

    for r in sorted(rows, key=lambda x: (x[1], -x[2])):
        out += f"| {r[0]} | vs {r[1]} | {r[2]:.1%} | {r[3]} | {r[4]:.3f} | {r[5]:.3f} | {r[6]:.3f} | {r[7]:.3f} | {r[8]:.3f} | {r[9]:.1%} | {r[10]:.1%} |\n"

    return out

def fangraphs_pitcher_row(pit, name):
    if pit.empty or name == "TBD":
        return {}

    m = pit[pit["Name"].str.lower() == name.lower()]
    if m.empty:
        return {}

    r = m.iloc[0]
    keys = ["ERA", "WHIP", "K/9", "BB/9", "HR/9", "IP", "K%", "BB%", "SIERA", "xFIP"]
    return {k: clean(r[k]) if k in r else "—" for k in keys}

def fangraphs_team_bats(bat, team):
    if bat.empty or "Team" not in bat.columns:
        return pd.DataFrame()

    team_code = team.split()[-1]
    t = bat[bat["Team"].astype(str).str.contains(team_code, case=False, na=False)]

    cols = [c for c in ["Name", "Team", "PA", "AVG", "OBP", "SLG", "ISO", "wOBA", "wRC+", "HR", "Barrel%", "HardHit%"] if c in t.columns]
    return t[cols].sort_values("PA", ascending=False).head(9) if cols else pd.DataFrame()

def markdown_df(df):
    if df.empty:
        return "| Player | Data |\n|---|---|\n| — | — |\n"
    return df.to_markdown(index=False)

def pitcher_profile(title, name, pit, sc):
    fg = fangraphs_pitcher_row(pit, name)

    out = f"\n### {title}: {name}\n\n"
    out += "| Stat | Value |\n|---|---:|\n"
    for k in ["ERA", "WHIP", "K/9", "BB/9", "HR/9", "IP", "K%", "BB%", "SIERA", "xFIP"]:
        out += f"| {k} | {fg.get(k, '—')} |\n"

    out += "\n#### Pitch Arsenal vs L/R\n\n"
    out += pitcher_pitch_table(sc, name)
    return out

def main():
    games = get_schedule()
    sc = load_statcast()
    bat, pit = load_fangraphs()

    report = f"""# MLB-LAB V4/V5 Daily Report

Date: {TODAY}

Build: Baseball Savant + FanGraphs + MLB API

No odds.  
No CSVs.  
No shortcut weak-pitch labels.  
Every game gets full pitch tables vs L/R.

---

# Slate

| # | Game | Park | Away SP | Home SP |
|---:|---|---|---|---|
"""

    for i, g in enumerate(games, 1):
        report += f"| {i} | {g['game']} | {g['park']} | {g['away_sp']} | {g['home_sp']} |\n"

    report += "\n---\n\n# Full Game Cards\n"

    for i, g in enumerate(games, 1):
        away_bats = fangraphs_team_bats(bat, g["away_team"])
        home_bats = fangraphs_team_bats(bat, g["home_team"])

        report += f"""

---

## {i}. {g['game']}

### Game Context

| Field | Value |
|---|---|
| Park | {g['park']} |
| Time | {g['time']} |
| Away SP | {g['away_sp']} |
| Home SP | {g['home_sp']} |

{pitcher_profile("Away Starting Pitcher", g["away_sp"], pit, sc)}

{pitcher_profile("Home Starting Pitcher", g["home_sp"], pit, sc)}

---

## {g['away_team']} Projected Hitter Pool

{markdown_df(away_bats)}

---

## {g['home_team']} Projected Hitter Pool

{markdown_df(home_bats)}

---

## Manual Read Space

### What To Look For

- Which pitcher pitch types are getting hit by LHB?
- Which pitcher pitch types are getting hit by RHB?
- Which lineup has more hitters matching those pitch types?
- Which hitters have strong ISO / wOBA / Barrel% / HardHit%?
- Which side has the better full-game attack profile?

### MLB-LAB Notes

- Attack Side:
- Pitcher Concern:
- Best Hitter Fits:
- Game Environment:
- Final Read:
"""

    report += """

---

# End Report

This is the V4/V5 all-in-one research board.
"""

    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text(report, encoding="utf-8")
    print(f"Updated {REPORT}")

if __name__ == "__main__":
    main()
