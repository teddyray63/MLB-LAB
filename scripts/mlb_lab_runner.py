from datetime import date, timedelta
from pathlib import Path
import requests
import pandas as pd
from pybaseball import statcast, batting_stats, pitching_stats

TODAY = date.today()
SEASON = TODAY.year
REPORT = Path("reports/mlb-lab-v5-matchup-engine.md")

STATCAST_DAYS = 60
START = (TODAY - timedelta(days=STATCAST_DAYS)).isoformat()
END = TODAY.isoformat()

TEAM_CODES = {
    "Arizona Diamondbacks": "ARI", "Athletics": "ATH", "Atlanta Braves": "ATL",
    "Baltimore Orioles": "BAL", "Boston Red Sox": "BOS", "Chicago Cubs": "CHC",
    "Chicago White Sox": "CHW", "Cincinnati Reds": "CIN", "Cleveland Guardians": "CLE",
    "Colorado Rockies": "COL", "Detroit Tigers": "DET", "Houston Astros": "HOU",
    "Kansas City Royals": "KCR", "Los Angeles Angels": "LAA", "Los Angeles Dodgers": "LAD",
    "Miami Marlins": "MIA", "Milwaukee Brewers": "MIL", "Minnesota Twins": "MIN",
    "New York Mets": "NYM", "New York Yankees": "NYY", "Philadelphia Phillies": "PHI",
    "Pittsburgh Pirates": "PIT", "San Diego Padres": "SDP", "San Francisco Giants": "SFG",
    "Seattle Mariners": "SEA", "St. Louis Cardinals": "STL", "Tampa Bay Rays": "TBR",
    "Texas Rangers": "TEX", "Toronto Blue Jays": "TOR", "Washington Nationals": "WSN",
}

def get_json(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.json()

def safe(x):
    if pd.isna(x) if not isinstance(x, str) else False:
        return "—"
    return "—" if x in [None, ""] else x

def fmt(x, decimals=3):
    try:
        if pd.isna(x):
            return "—"
        return f"{float(x):.{decimals}f}"
    except Exception:
        return "—"

def pct(x):
    try:
        if pd.isna(x):
            return "—"
        return f"{float(x):.1%}"
    except Exception:
        return "—"

def md_table(headers, rows):
    out = "| " + " | ".join(headers) + " |\n"
    out += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    if not rows:
        out += "| " + " | ".join(["—"] * len(headers)) + " |\n"
    else:
        for r in rows:
            out += "| " + " | ".join(str(x) for x in r) + " |\n"
    return out

def get_schedule():
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={TODAY}&hydrate=probablePitcher,venue,team"
    data = get_json(url)
    games = []

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
                "time": g.get("gameDate", "—"),
                "away_sp": away_sp.get("fullName", "TBD"),
                "home_sp": home_sp.get("fullName", "TBD"),
                "away_sp_id": away_sp.get("id"),
                "home_sp_id": home_sp.get("id"),
            })

    return games

def load_data():
    try:
        sc = statcast(start_dt=START, end_dt=END)
    except Exception:
        sc = pd.DataFrame()

    try:
        bat = batting_stats(SEASON, qual=0)
    except Exception:
        bat = pd.DataFrame()

    try:
        pit = pitching_stats(SEASON, qual=0)
    except Exception:
        pit = pd.DataFrame()

    return sc, bat, pit

def find_player_sc(sc, name):
    if sc.empty or name in ["TBD", None]:
        return pd.DataFrame()

    parts = name.split()
    reverse = f"{parts[-1]}, {' '.join(parts[:-1])}" if len(parts) > 1 else name

    if "player_name" not in sc.columns:
        return pd.DataFrame()

    return sc[
        sc["player_name"].astype(str).str.lower().isin(
            [name.lower(), reverse.lower()]
        )
    ]

def find_fangraphs_player(df, name):
    if df.empty or name in ["TBD", None] or "Name" not in df.columns:
        return pd.DataFrame()

    exact = df[df["Name"].astype(str).str.lower() == name.lower()]
    if not exact.empty:
        return exact

    parts = name.split()
    if parts:
        last = parts[-1].lower()
        fuzzy = df[df["Name"].astype(str).str.lower().str.contains(last, na=False)]
        return fuzzy.head(1)

    return pd.DataFrame()

def pitcher_profile_table(pit, name):
    m = find_fangraphs_player(pit, name)
    if m.empty:
        return md_table(
            ["Stat", "Value"],
            [["ERA", "—"], ["WHIP", "—"], ["K/9", "—"], ["BB/9", "—"], ["HR/9", "—"], ["IP", "—"], ["K%", "—"], ["BB%", "—"], ["SIERA", "—"], ["xFIP", "—"]]
        )

    r = m.iloc[0]
    rows = []
    for k in ["ERA", "WHIP", "K/9", "BB/9", "HR/9", "IP", "K%", "BB%", "SIERA", "xFIP"]:
        val = r[k] if k in r else "—"
        rows.append([k, fmt(val, 2) if isinstance(val, (int, float)) else safe(val)])
    return md_table(["Stat", "Value"], rows)

def pitcher_arsenal_table(sc, name):
    p = find_player_sc(sc, name)
    if p.empty:
        return md_table(
            ["Pitch", "Batter Side", "Usage", "Pitches", "AVG", "SLG", "ISO", "wOBA", "xwOBA", "HardHit%", "Whiff%"],
            []
        )

    rows = []
    total = len(p)

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
        woba = g["woba_value"].mean() if "woba_value" in g else None
        xwoba = g["estimated_woba_using_speedangle"].mean() if "estimated_woba_using_speedangle" in g else None

        bbe = g["launch_speed"].dropna() if "launch_speed" in g else pd.Series(dtype=float)
        hard = (bbe >= 95).mean() if len(bbe) else 0

        swings = g[g["description"].isin(["swinging_strike", "swinging_strike_blocked", "foul", "hit_into_play"])]
        whiffs = g[g["description"].isin(["swinging_strike", "swinging_strike_blocked"])]
        whiff = len(whiffs) / len(swings) if len(swings) else 0

        usage = len(g) / total if total else 0

        rows.append([
            pitch,
            f"vs {stand}",
            pct(usage),
            len(g),
            fmt(avg),
            fmt(slg),
            fmt(iso),
            fmt(woba),
            fmt(xwoba),
            pct(hard),
            pct(whiff),
        ])

    return md_table(
        ["Pitch", "Batter Side", "Usage", "Pitches", "AVG", "SLG", "ISO", "wOBA", "xwOBA", "HardHit%", "Whiff%"],
        rows
    )

def major_pitches(sc, name):
    p = find_player_sc(sc, name)
    if p.empty:
        return []

    mix = p["pitch_type"].value_counts(normalize=True)
    return list(mix[mix >= 0.08].index)

def hitter_vs_pitch_table(sc, hitters_df, pitch_types):
    if sc.empty or hitters_df.empty or not pitch_types:
        return md_table(["Pitch", "Hitter", "PA", "AVG", "SLG", "ISO", "wOBA", "Barrel%", "HardHit%"], [])

    rows = []
    hitter_names = set(hitters_df["Name"].astype(str).str.lower())

    if "batter_name" not in sc.columns:
        sc = sc.copy()
        sc["batter_name"] = ""

    for pitch in pitch_types:
        g = sc[sc["pitch_type"] == pitch]
        if g.empty:
            continue

        for hitter in hitter_names:
            hg = g[g["batter_name"].astype(str).str.lower() == hitter]
            if hg.empty:
                continue

            events = hg.dropna(subset=["events"])
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
            woba = hg["woba_value"].mean() if "woba_value" in hg else None

            bbe = hg["launch_speed"].dropna() if "launch_speed" in hg else pd.Series(dtype=float)
            hard = (bbe >= 95).mean() if len(bbe) else 0

            barrel = 0
            if "launch_speed_angle" in hg:
                barrel = (hg["launch_speed_angle"] == 6).mean()

            rows.append([
                pitch,
                hitter.title(),
                len(events),
                fmt(avg),
                fmt(slg),
                fmt(iso),
                fmt(woba),
                pct(barrel),
                pct(hard),
            ])

    rows = sorted(rows, key=lambda r: (r[0], float(r[5]) if r[5] != "—" else 0), reverse=True)[:30]
    return md_table(["Pitch", "Hitter", "PA", "AVG", "SLG", "ISO", "wOBA", "Barrel%", "HardHit%"], rows)

def team_hitter_pool(bat, team):
    if bat.empty or "Team" not in bat.columns:
        return pd.DataFrame()

    code = TEAM_CODES.get(team)
    if not code:
        return pd.DataFrame()

    t = bat[bat["Team"].astype(str) == code]
    if t.empty:
        return pd.DataFrame()

    cols = [c for c in ["Name", "PA", "AVG", "OBP", "SLG", "ISO", "wOBA", "wRC+", "Barrel%", "HardHit%"] if c in t.columns]
    return t[cols].sort_values("PA", ascending=False).head(12)

def markdown_df(df):
    if df.empty:
        return md_table(["Player", "Data"], [])
    return df.to_markdown(index=False)

def game_card(i, g, sc, bat, pit):
    away_hitters = team_hitter_pool(bat, g["away_team"])
    home_hitters = team_hitter_pool(bat, g["home_team"])

    away_sp_pitches = major_pitches(sc, g["away_sp"])
    home_sp_pitches = major_pitches(sc, g["home_sp"])

    return f"""
---

## {i}. {g['game']}

## Game Context

{md_table(["Field", "Value"], [
    ["Park", g["park"]],
    ["Time", g["time"]],
    ["Away Team", g["away_team"]],
    ["Home Team", g["home_team"]],
    ["Away SP", g["away_sp"]],
    ["Home SP", g["home_sp"]],
])}

## Away Starting Pitcher: {g["away_sp"]}

{pitcher_profile_table(pit, g["away_sp"])}

### Pitch Arsenal vs L/R

{pitcher_arsenal_table(sc, g["away_sp"])}

## Home Hitters vs Away SP Pitch Mix

{hitter_vs_pitch_table(sc, home_hitters, away_sp_pitches)}

## Home Starting Pitcher: {g["home_sp"]}

{pitcher_profile_table(pit, g["home_sp"])}

### Pitch Arsenal vs L/R

{pitcher_arsenal_table(sc, g["home_sp"])}

## Away Hitters vs Home SP Pitch Mix

{hitter_vs_pitch_table(sc, away_hitters, home_sp_pitches)}

## {g["away_team"]} Team Offense Section

{markdown_df(away_hitters)}

## {g["home_team"]} Team Offense Section

{markdown_df(home_hitters)}

## Final Game Dissection

- Strongest pitch attack points:
- Weakest pitch attack points:
- Best hitter vs pitch matches:
- Lineup advantages:
- Handedness advantages:
- Bullpen context:
- Final MLB-LAB read:
"""

def main():
    games = get_schedule()
    sc, bat, pit = load_data()

    report = f"""# MLB-LAB V5 Pitch Matchup Engine

Date: {TODAY}

Sources:
- MLB Stats API
- Baseball Savant / Statcast
- FanGraphs

Removed:
- Odds
- CSVs
- Weak-pitch shortcuts
- Scoring gimmicks
- Manual placeholder tables

---

# Slate

| # | Game | Park | Away SP | Home SP |
|---:|---|---|---|---|
"""

    for i, g in enumerate(games, 1):
        report += f"| {i} | {g['game']} | {g['park']} | {g['away_sp']} | {g['home_sp']} |\n"

    report += "\n---\n\n# Full Game Breakdown Cards\n"

    for i, g in enumerate(games, 1):
        report += game_card(i, g, sc, bat, pit)

    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text(report, encoding="utf-8")
    print(f"Updated {REPORT}")

if __name__ == "__main__":
    main()
