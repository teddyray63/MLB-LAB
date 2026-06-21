from datetime import date, timedelta
from pathlib import Path
import requests
import pandas as pd
from pybaseball import statcast, playerid_reverse_lookup

TODAY = date.today()
SEASON = TODAY.year
START = (TODAY - timedelta(days=120)).isoformat()
END = TODAY.isoformat()

REPORT = Path("reports/mlb-lab-v5-matchup-engine.md")
CACHE = Path("data/cache/statcast_cache.pkl")

TEAM_CODES = {
    "Arizona Diamondbacks": "ARI", "Athletics": "ATH", "Atlanta Braves": "ATL",
    "Baltimore Orioles": "BAL", "Boston Red Sox": "BOS", "Chicago Cubs": "CHC",
    "Chicago White Sox": "CHW", "Cincinnati Reds": "CIN", "Cleveland Guardians": "CLE",
    "Colorado Rockies": "COL", "Detroit Tigers": "DET", "Houston Astros": "HOU",
    "Kansas City Royals": "KC", "Los Angeles Angels": "LAA", "Los Angeles Dodgers": "LAD",
    "Miami Marlins": "MIA", "Milwaukee Brewers": "MIL", "Minnesota Twins": "MIN",
    "New York Mets": "NYM", "New York Yankees": "NYY", "Philadelphia Phillies": "PHI",
    "Pittsburgh Pirates": "PIT", "San Diego Padres": "SD", "San Francisco Giants": "SF",
    "Seattle Mariners": "SEA", "St. Louis Cardinals": "STL", "Tampa Bay Rays": "TB",
    "Texas Rangers": "TEX", "Toronto Blue Jays": "TOR", "Washington Nationals": "WSH",
}

def mlb_json(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.json()

def safe(x, d="—"):
    return d if x is None or pd.isna(x) else x

def fmt(x, n=3):
    try:
        if pd.isna(x): return "—"
        return f"{float(x):.{n}f}"
    except Exception:
        return "—"

def pct(x):
    try:
        if pd.isna(x): return "—"
        return f"{float(x)*100:.1f}%"
    except Exception:
        return "—"

def table(headers, rows):
    out = "| " + " | ".join(headers) + " |\n"
    out += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    if not rows:
        rows = [["No data"] + ["—"] * (len(headers) - 1)]
    for r in rows:
        out += "| " + " | ".join(str(x) for x in r) + " |\n"
    return out

def get_schedule():
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={TODAY}&hydrate=probablePitcher,venue,team"
    data = mlb_json(url)
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

def load_statcast():
    CACHE.parent.mkdir(parents=True, exist_ok=True)

    try:
        sc = statcast(start_dt=START, end_dt=END)
        if not sc.empty:
            sc.to_pickle(CACHE)
            return prepare_statcast(sc)
    except Exception as e:
        print(f"Savant pull failed: {e}")

    if CACHE.exists():
        print("Using cached Statcast data.")
        return prepare_statcast(pd.read_pickle(CACHE))

    return pd.DataFrame()

def prepare_statcast(sc):
    sc = sc.copy()

    if "inning_topbot" in sc.columns:
        sc["batter_team"] = sc.apply(
            lambda r: r["away_team"] if r["inning_topbot"] == "Top" else r["home_team"],
            axis=1
        )

    if "batter" in sc.columns:
        try:
            ids = sorted(sc["batter"].dropna().astype(int).unique())
            lookup = playerid_reverse_lookup(ids, key_type="mlbam")
            lookup["batter_name"] = lookup["name_first"] + " " + lookup["name_last"]
            sc["batter_name"] = sc["batter"].map(dict(zip(lookup["key_mlbam"], lookup["batter_name"])))
        except Exception as e:
            print(f"Batter lookup failed: {e}")
            sc["batter_name"] = ""

    return sc

def pitcher_rows(sc, name):
    if sc.empty or name == "TBD" or "player_name" not in sc.columns:
        return pd.DataFrame()

    parts = name.split()
    reverse = f"{parts[-1]}, {' '.join(parts[:-1])}"
    return sc[sc["player_name"].astype(str).str.lower() == reverse.lower()]

def event_stats(df):
    events = df.dropna(subset=["events"]) if "events" in df.columns else pd.DataFrame()
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
    woba = df["woba_value"].mean() if "woba_value" in df.columns else None
    xwoba = df["estimated_woba_using_speedangle"].mean() if "estimated_woba_using_speedangle" in df.columns else None

    bbe = df["launch_speed"].dropna() if "launch_speed" in df.columns else pd.Series(dtype=float)
    hard = (bbe >= 95).mean() if len(bbe) else 0

    barrel = 0
    if "launch_speed_angle" in df.columns:
        barrel = (df["launch_speed_angle"] == 6).mean()

    swings = df[df["description"].isin(["swinging_strike", "swinging_strike_blocked", "foul", "hit_into_play"])]
    whiffs = df[df["description"].isin(["swinging_strike", "swinging_strike_blocked"])]
    whiff = len(whiffs) / len(swings) if len(swings) else 0

    return avg, slg, iso, woba, xwoba, barrel, hard, whiff, len(events)

def pitcher_profile(sc, name):
    p = pitcher_rows(sc, name)
    if p.empty:
        return table(["Stat", "Value"], [])

    ip = len(p[p["events"].notna()]) / 3 if "events" in p.columns else 0
    er = (p["events"] == "home_run").sum() if "events" in p.columns else 0
    k = p["events"].isin(["strikeout", "strikeout_double_play"]).sum()
    bb = p["events"].isin(["walk", "intent_walk"]).sum()
    hr = (p["events"] == "home_run").sum()
    hits = p["events"].isin(["single", "double", "triple", "home_run"]).sum()

    rows = [
        ["Sample Pitches", len(p)],
        ["Estimated IP Events", fmt(ip, 1)],
        ["Hits Allowed", hits],
        ["Walks", bb],
        ["Strikeouts", k],
        ["Home Runs", hr],
        ["K Event Rate", pct(k / max(1, len(p.dropna(subset=["events"]))))],
        ["BB Event Rate", pct(bb / max(1, len(p.dropna(subset=["events"]))))],
        ["HR Event Rate", pct(hr / max(1, len(p.dropna(subset=["events"]))))],
    ]
    return table(["Stat", "Value"], rows)

def arsenal(sc, name):
    p = pitcher_rows(sc, name)
    headers = ["Pitch", "Side", "Usage", "Pitches", "AVG", "SLG", "ISO", "wOBA", "xwOBA", "Barrel%", "HardHit%", "Whiff%"]

    if p.empty:
        return table(headers, [])

    rows = []
    total = len(p)

    for (pitch, side), g in p.groupby(["pitch_type", "stand"]):
        avg, slg, iso, woba, xwoba, barrel, hard, whiff, pa = event_stats(g)
        rows.append([
            pitch, f"vs {side}", pct(len(g) / total), len(g),
            fmt(avg), fmt(slg), fmt(iso), fmt(woba), fmt(xwoba),
            pct(barrel), pct(hard), pct(whiff)
        ])

    rows = sorted(rows, key=lambda r: (r[0], r[1]))
    return table(headers, rows)

def major_pitches(sc, name):
    p = pitcher_rows(sc, name)
    if p.empty:
        return []
    mix = p["pitch_type"].value_counts(normalize=True)
    return list(mix[mix >= 0.08].index)

def team_hitter_pool(sc, team):
    if sc.empty or "batter_team" not in sc.columns or "batter_name" not in sc.columns:
        return pd.DataFrame()

    t = sc[sc["batter_team"] == team]
    rows = []

    for name, g in t.groupby("batter_name"):
        if not name or pd.isna(name):
            continue
        avg, slg, iso, woba, xwoba, barrel, hard, whiff, pa = event_stats(g)
        if pa < 20:
            continue
        rows.append({
            "Hitter": name,
            "PA": pa,
            "AVG": avg,
            "SLG": slg,
            "ISO": iso,
            "wOBA": woba,
            "xwOBA": xwoba,
            "Barrel%": barrel,
            "HardHit%": hard,
            "Whiff%": whiff,
        })

    return pd.DataFrame(rows).sort_values(["PA", "wOBA"], ascending=False).head(12)

def hitter_pool_md(df):
    if df.empty:
        return table(["Hitter", "PA", "AVG", "SLG", "ISO", "wOBA", "xwOBA", "Barrel%", "HardHit%", "Whiff%"], [])

    rows = []
    for _, r in df.iterrows():
        rows.append([
            r["Hitter"], int(r["PA"]), fmt(r["AVG"]), fmt(r["SLG"]), fmt(r["ISO"]),
            fmt(r["wOBA"]), fmt(r["xwOBA"]), pct(r["Barrel%"]), pct(r["HardHit%"]), pct(r["Whiff%"])
        ])

    return table(["Hitter", "PA", "AVG", "SLG", "ISO", "wOBA", "xwOBA", "Barrel%", "HardHit%", "Whiff%"], rows)

def hitter_vs_pitch(sc, hitters, pitches):
    headers = ["Pitch", "Hitter", "PA", "AVG", "SLG", "ISO", "wOBA", "xwOBA", "Barrel%", "HardHit%", "Whiff%"]

    if sc.empty or hitters.empty or not pitches:
        return table(headers, [])

    names = set(hitters["Hitter"].str.lower())
    rows = []

    for pitch in pitches:
        g = sc[sc["pitch_type"] == pitch]
        for name in names:
            h = g[g["batter_name"].astype(str).str.lower() == name]
            if h.empty:
                continue

            avg, slg, iso, woba, xwoba, barrel, hard, whiff, pa = event_stats(h)
            if pa < 3:
                continue

            rows.append([
                pitch, name.title(), pa, fmt(avg), fmt(slg), fmt(iso),
                fmt(woba), fmt(xwoba), pct(barrel), pct(hard), pct(whiff)
            ])

    rows = sorted(rows, key=lambda r: float(r[5]) if r[5] != "—" else 0, reverse=True)[:30]
    return table(headers, rows)

def last_5_starts(sc, name):
    p = pitcher_rows(sc, name)
    if p.empty or "game_date" not in p.columns:
        return table(["Date", "Pitches", "H", "BB", "K", "HR"], [])

    rows = []
    for game_date, g in p.groupby("game_date"):
        events = g.dropna(subset=["events"])
        h = events["events"].isin(["single", "double", "triple", "home_run"]).sum()
        bb = events["events"].isin(["walk", "intent_walk"]).sum()
        k = events["events"].isin(["strikeout", "strikeout_double_play"]).sum()
        hr = (events["events"] == "home_run").sum()
        rows.append([game_date, len(g), h, bb, k, hr])

    rows = sorted(rows, key=lambda r: str(r[0]), reverse=True)[:5]
    return table(["Date", "Pitches", "H", "BB", "K", "HR"], rows)

def dissection(sc, g, away_hitters, home_hitters):
    away_mix = major_pitches(sc, g["away_sp"])
    home_mix = major_pitches(sc, g["home_sp"])

    return f"""
## Final Game Dissection

- Away pitcher main pitch mix: {", ".join(away_mix) if away_mix else "No current Statcast sample"}
- Home pitcher main pitch mix: {", ".join(home_mix) if home_mix else "No current Statcast sample"}
- Inspect home hitters against: {", ".join(away_mix) if away_mix else "—"}
- Inspect away hitters against: {", ".join(home_mix) if home_mix else "—"}
- Lineup advantage check: compare team hitter pools above by wOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage check: use pitcher arsenal vs L/R tables above.
- Bullpen context: not active in this runner yet.
- Final MLB-LAB read: use pitch mix + hitter pool + L/R damage profile.
"""

def game_card(i, g, sc):
    away_hitters = team_hitter_pool(sc, g["away_code"])
    home_hitters = team_hitter_pool(sc, g["home_code"])

    away_mix = major_pitches(sc, g["away_sp"])
    home_mix = major_pitches(sc, g["home_sp"])

    return f"""
---

# {i}. {g['game']}

## Game Context

{table(["Field", "Value"], [
    ["Park", g["park"]],
    ["Time", g["time"]],
    ["Away Team", g["away_team"]],
    ["Home Team", g["home_team"]],
    ["Away Probable Pitcher", g["away_sp"]],
    ["Home Probable Pitcher", g["home_sp"]],
])}

## Away Starting Pitcher: {g['away_sp']}

### Pitcher Profile

{pitcher_profile(sc, g["away_sp"])}

### Full Pitch Arsenal vs L/R

{arsenal(sc, g["away_sp"])}

### Last 5 Starts / Appearances

{last_5_starts(sc, g["away_sp"])}

## Home Hitters vs Away SP Pitch Mix

{hitter_vs_pitch(sc, home_hitters, away_mix)}

## Home Starting Pitcher: {g['home_sp']}

### Pitcher Profile

{pitcher_profile(sc, g["home_sp"])}

### Full Pitch Arsenal vs L/R

{arsenal(sc, g["home_sp"])}

### Last 5 Starts / Appearances

{last_5_starts(sc, g["home_sp"])}

## Away Hitters vs Home SP Pitch Mix

{hitter_vs_pitch(sc, away_hitters, home_mix)}

## {g['away_team']} Team Offense Section

{hitter_pool_md(away_hitters)}

## {g['home_team']} Team Offense Section

{hitter_pool_md(home_hitters)}

{dissection(sc, g, away_hitters, home_hitters)}
"""

def main():
    games = get_schedule()
    sc = load_statcast()

    report = f"""# MLB-LAB V5.1 Savant-First Pitch Matchup Engine

Date: {TODAY}

Core build:
- MLB Stats API: schedule, teams, parks, probable pitchers
- Baseball Savant / Statcast: pitch arsenal, L/R splits, hitter pools, hitter vs pitch type
- FanGraphs removed from required runtime because GitHub Actions can block it

No odds. No CSVs. No betting lines. No weak-pitch shortcuts. No placeholder manual tables.

---

# Slate

| # | Game | Park | Away SP | Home SP |
|---:|---|---|---|---|
"""

    for i, g in enumerate(games, 1):
        report += f"| {i} | {g['game']} | {g['park']} | {g['away_sp']} | {g['home_sp']} |\n"

    report += "\n---\n\n# Full Game Breakdown Cards\n"

    for i, g in enumerate(games, 1):
        report += game_card(i, g, sc)

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(report, encoding="utf-8")
    print(f"Updated {REPORT}")

if __name__ == "__main__":
    main()
