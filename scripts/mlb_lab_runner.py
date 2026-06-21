from datetime import date, timedelta
from pathlib import Path
import requests
import pandas as pd
from pybaseball import statcast, batting_stats, pitching_stats, playerid_reverse_lookup

TODAY = date.today()
SEASON = TODAY.year
START = (TODAY - timedelta(days=75)).isoformat()
END = TODAY.isoformat()
REPORT = Path("reports/mlb-lab-v5-matchup-engine.md")

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

def req(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.json()

def fmt(x, n=3):
    try:
        if pd.isna(x):
            return "—"
        return f"{float(x):.{n}f}"
    except Exception:
        return "—"

def pct(x):
    try:
        if pd.isna(x):
            return "—"
        return f"{float(x):.1%}"
    except Exception:
        return "—"

def table(headers, rows):
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
    data = req(url)
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
                "away_code": TEAM_CODES.get(away["name"], ""),
                "home_code": TEAM_CODES.get(home["name"], ""),
                "park": g["venue"]["name"],
                "time": g.get("gameDate", "—"),
                "away_sp": away_sp.get("fullName", "TBD"),
                "home_sp": home_sp.get("fullName", "TBD"),
            })
    return games

def load_all():
    try:
        sc = statcast(start_dt=START, end_dt=END)
    except Exception as e:
        print(f"Savant statcast failed: {e}")
        sc = pd.DataFrame()

    try:
        bat = batting_stats(SEASON, qual=0)
    except Exception as e:
        print(f"FanGraphs batting failed: {e}")
        bat = pd.DataFrame()

    try:
        pit = pitching_stats(SEASON, qual=0)
    except Exception as e:
        print(f"FanGraphs pitching failed: {e}")
        pit = pd.DataFrame()

    if not sc.empty and "batter" in sc.columns:
        try:
            ids = sorted(sc["batter"].dropna().astype(int).unique().tolist())
            lookup = playerid_reverse_lookup(ids, key_type="mlbam")
            lookup["batter_name"] = lookup["name_first"] + " " + lookup["name_last"]
            mapper = dict(zip(lookup["key_mlbam"], lookup["batter_name"]))
            sc["batter_name"] = sc["batter"].map(mapper)
        except Exception as e:
            print(f"Batter name lookup failed: {e}")
            sc["batter_name"] = ""

    return sc, bat, pit

def fg_player(df, name):
    if df.empty or name == "TBD" or "Name" not in df.columns:
        return pd.DataFrame()

    exact = df[df["Name"].astype(str).str.lower() == name.lower()]
    if not exact.empty:
        return exact

    last = name.split()[-1].lower()
    return df[df["Name"].astype(str).str.lower().str.contains(last, na=False)].head(1)

def fg_pitcher_profile(pit, name):
    keys = ["ERA", "WHIP", "K/9", "BB/9", "HR/9", "IP", "K%", "BB%", "SIERA", "xFIP"]
    m = fg_player(pit, name)

    if m.empty:
        return table(["Stat", "Value"], [[k, "—"] for k in keys])

    r = m.iloc[0]
    rows = []
    for k in keys:
        rows.append([k, fmt(r[k], 2) if k in r else "—"])

    return table(["Stat", "Value"], rows)

def sc_pitcher_rows(sc, name):
    if sc.empty or name == "TBD" or "player_name" not in sc.columns:
        return pd.DataFrame()

    parts = name.split()
    rev = f"{parts[-1]}, {' '.join(parts[:-1])}" if len(parts) > 1 else name

    return sc[
        sc["player_name"].astype(str).str.lower().isin(
            [name.lower(), rev.lower()]
        )
    ]

def arsenal(sc, name):
    p = sc_pitcher_rows(sc, name)
    headers = ["Pitch","Side","Usage","Pitches","AVG","SLG","ISO","wOBA","xwOBA","HardHit%","Whiff%"]

    if p.empty:
        return table(headers, [])

    rows = []
    total = len(p)

    for (pitch, side), g in p.groupby(["pitch_type", "stand"]):
        events = g.dropna(subset=["events"])
        ab_events = events[~events["events"].isin(["walk","hit_by_pitch","sac_bunt","sac_fly"])]
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

        swings = g[g["description"].isin(["swinging_strike","swinging_strike_blocked","foul","hit_into_play"])]
        whiffs = g[g["description"].isin(["swinging_strike","swinging_strike_blocked"])]
        whiff = len(whiffs) / len(swings) if len(swings) else 0

        rows.append([
            pitch,
            f"vs {side}",
            pct(len(g) / total),
            len(g),
            fmt(avg),
            fmt(slg),
            fmt(iso),
            fmt(woba),
            fmt(xwoba),
            pct(hard),
            pct(whiff),
        ])

    return table(headers, rows)

def major_pitches(sc, name):
    p = sc_pitcher_rows(sc, name)
    if p.empty or "pitch_type" not in p.columns:
        return []

    mix = p["pitch_type"].value_counts(normalize=True)
    return list(mix[mix >= 0.08].index)

def team_hitters(bat, code):
    if bat.empty or not code or "Team" not in bat.columns:
        return pd.DataFrame()

    t = bat[bat["Team"].astype(str) == code]

    cols = [
        c for c in [
            "Name", "PA", "AVG", "OBP", "SLG", "ISO",
            "wOBA", "wRC+", "Barrel%", "HardHit%"
        ]
        if c in t.columns
    ]

    if t.empty or not cols:
        return pd.DataFrame()

    return t[cols].sort_values("PA", ascending=False).head(12)

def df_md(df):
    if df.empty:
        return table(["Player", "Data"], [])
    return df.to_markdown(index=False)

def hitter_pitch_matchups(sc, hitter_df, pitches):
    headers = ["Pitch","Hitter","PA","AVG","SLG","ISO","wOBA","Barrel%","HardHit%"]

    if sc.empty or hitter_df.empty or "batter_name" not in sc.columns:
        return table(headers, [])

    hitter_names = set(hitter_df["Name"].astype(str).str.lower())
    rows = []

    for pitch in pitches:
        g = sc[sc["pitch_type"] == pitch]

        for h in hitter_names:
            hg = g[g["batter_name"].astype(str).str.lower() == h]
            if hg.empty:
                continue

            events = hg.dropna(subset=["events"])
            ab_events = events[~events["events"].isin(["walk","hit_by_pitch","sac_bunt","sac_fly"])]
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
                h.title(),
                len(events),
                fmt(avg),
                fmt(slg),
                fmt(iso),
                fmt(woba),
                pct(barrel),
                pct(hard),
            ])

    rows = sorted(
        rows,
        key=lambda r: float(r[5]) if r[5] != "—" else 0,
        reverse=True
    )[:40]

    return table(headers, rows)

def card(i, g, sc, bat, pit):
    away_hitters = team_hitters(bat, g["away_code"])
    home_hitters = team_hitters(bat, g["home_code"])

    away_mix = major_pitches(sc, g["away_sp"])
    home_mix = major_pitches(sc, g["home_sp"])

    return f"""
---

# {i}. {g['game']}

## Game Context

{table(["Field","Value"], [
    ["Park", g["park"]],
    ["Time", g["time"]],
    ["Away SP", g["away_sp"]],
    ["Home SP", g["home_sp"]],
])}

## Away Starting Pitcher: {g['away_sp']}

{fg_pitcher_profile(pit, g["away_sp"])}

### Pitch Arsenal vs L/R

{arsenal(sc, g["away_sp"])}

## Home Hitters vs Away SP Pitch Mix

{hitter_pitch_matchups(sc, home_hitters, away_mix)}

## Home Starting Pitcher: {g['home_sp']}

{fg_pitcher_profile(pit, g["home_sp"])}

### Pitch Arsenal vs L/R

{arsenal(sc, g["home_sp"])}

## Away Hitters vs Home SP Pitch Mix

{hitter_pitch_matchups(sc, away_hitters, home_mix)}

## {g['away_team']} Team Offense Section

{df_md(away_hitters)}

## {g['home_team']} Team Offense Section

{df_md(home_hitters)}

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
    sc, bat, pit = load_all()

    report = f"""# MLB-LAB V5 Pitch Matchup Engine

Date: {TODAY}

Sources:
- MLB Stats API
- Baseball Savant / Statcast
- FanGraphs if available

No odds. No CSVs. No weak-pitch shortcuts.

---

# Slate

| # | Game | Park | Away SP | Home SP |
|---:|---|---|---|---|
"""

    for i, g in enumerate(games, 1):
        report += f"| {i} | {g['game']} | {g['park']} | {g['away_sp']} | {g['home_sp']} |\n"

    report += "\n---\n\n# Full Game Breakdown Cards\n"

    for i, g in enumerate(games, 1):
        report += card(i, g, sc, bat, pit)

    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text(report, encoding="utf-8")
    print(f"Updated {REPORT}")

if __name__ == "__main__":
    main()
