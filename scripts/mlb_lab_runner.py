from datetime import date, timedelta
from pathlib import Path
import requests
import pandas as pd
from pybaseball import statcast, playerid_reverse_lookup

TODAY = date.today()
START = (TODAY - timedelta(days=120)).isoformat()
END = TODAY.isoformat()

REPORT = Path("reports/mlb-lab-v5-matchup-engine.md")
CACHE = Path("data/cache/statcast_cache.pkl")

TEAM_CODES = {
    "Arizona Diamondbacks": "AZ", "Athletics": "ATH", "Atlanta Braves": "ATL",
    "Baltimore Orioles": "BAL", "Boston Red Sox": "BOS", "Chicago Cubs": "CHC",
    "Chicago White Sox": "CWS", "Cincinnati Reds": "CIN", "Cleveland Guardians": "CLE",
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

def fmt(x, n=3):
    try:
        if x is None or pd.isna(x):
            return "—"
        return f"{float(x):.{n}f}"
    except Exception:
        return "—"

def pct(x):
    try:
        if x is None or pd.isna(x):
            return "—"
        return f"{float(x) * 100:.1f}%"
    except Exception:
        return "—"

def md_table(headers, rows):
    out = "| " + " | ".join(headers) + " |\n"
    out += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    if not rows:
        rows = [["No data"] + ["—"] * (len(headers) - 1)]
    for row in rows:
        out += "| " + " | ".join(str(x) for x in row) + " |\n"
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
        print(f"Pulling Statcast {START} to {END}")
        sc = statcast(start_dt=START, end_dt=END)
        if not sc.empty:
            sc.to_pickle(CACHE)
            return prep_statcast(sc)
    except Exception as e:
        print(f"Statcast pull failed: {e}")

    if CACHE.exists():
        print("Using cached Statcast.")
        return prep_statcast(pd.read_pickle(CACHE))

    return pd.DataFrame()

def prep_statcast(sc):
    sc = sc.copy()

    if "inning_topbot" in sc.columns:
        sc["batter_team"] = sc.apply(
            lambda r: r.get("away_team") if r.get("inning_topbot") == "Top" else r.get("home_team"),
            axis=1
        )

    if "batter" in sc.columns:
        try:
            ids = sorted(sc["batter"].dropna().astype(int).unique().tolist())
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
    if len(parts) < 2:
        return pd.DataFrame()

    reverse = f"{parts[-1]}, {' '.join(parts[:-1])}"
    return sc[sc["player_name"].astype(str).str.lower() == reverse.lower()]

def event_stats(df):
    if df.empty:
        return 0, 0, 0, None, None, 0, 0, 0, 0

    events = df.dropna(subset=["events"]) if "events" in df.columns else pd.DataFrame()
    ab_events = events[~events["events"].isin(["walk", "intent_walk", "hit_by_pitch", "sac_bunt", "sac_fly"])]
    ab = len(ab_events)

    singles = (events["events"] == "single").sum()
    doubles = (events["events"] == "double").sum()
    triples = (events["events"] == "triple").sum()
    hrs = (events["events"] == "home_run").sum()

    hits = singles + doubles + triples + hrs
    tb = singles + 2 * doubles + 3 * triples + 4 * hrs

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
        return md_table(["Stat", "Value"], [])

    events = p.dropna(subset=["events"])
    h = events["events"].isin(["single", "double", "triple", "home_run"]).sum()
    bb = events["events"].isin(["walk", "intent_walk"]).sum()
    k = events["events"].isin(["strikeout", "strikeout_double_play"]).sum()
    hr = (events["events"] == "home_run").sum()

    total_events = max(1, len(events))

    rows = [
        ["Sample Pitches", len(p)],
        ["Batted/Result Events", len(events)],
        ["Hits Allowed", h],
        ["Walks", bb],
        ["Strikeouts", k],
        ["Home Runs", hr],
        ["K Event Rate", pct(k / total_events)],
        ["BB Event Rate", pct(bb / total_events)],
        ["HR Event Rate", pct(hr / total_events)],
    ]

    return md_table(["Stat", "Value"], rows)

def arsenal(sc, name):
    p = pitcher_rows(sc, name)
    headers = ["Pitch", "Side", "Usage", "Pitches", "AVG", "SLG", "ISO", "wOBA", "xwOBA", "Barrel%", "HardHit%", "Whiff%"]

    if p.empty or "pitch_type" not in p.columns or "stand" not in p.columns:
        return md_table(headers, [])

    rows = []
    total = max(1, len(p))

    for (pitch, side), g in p.groupby(["pitch_type", "stand"]):
        avg, slg, iso, woba, xwoba, barrel, hard, whiff, pa = event_stats(g)
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
            pct(barrel),
            pct(hard),
            pct(whiff),
        ])

    return md_table(headers, sorted(rows, key=lambda x: (x[0], x[1])))

def major_pitches(sc, name):
    p = pitcher_rows(sc, name)
    if p.empty or "pitch_type" not in p.columns:
        return []

    mix = p["pitch_type"].value_counts(normalize=True)
    return list(mix[mix >= 0.08].index)

def last_5_starts(sc, name):
    p = pitcher_rows(sc, name)
    headers = ["Date", "Pitches", "Hits", "BB", "K", "HR"]

    if p.empty or "game_date" not in p.columns:
        return md_table(headers, [])

    rows = []

    for game_date, g in p.groupby("game_date"):
        events = g.dropna(subset=["events"])
        hits = events["events"].isin(["single", "double", "triple", "home_run"]).sum()
        bb = events["events"].isin(["walk", "intent_walk"]).sum()
        k = events["events"].isin(["strikeout", "strikeout_double_play"]).sum()
        hr = (events["events"] == "home_run").sum()
        rows.append([game_date, len(g), hits, bb, k, hr])

    rows = sorted(rows, key=lambda x: str(x[0]), reverse=True)[:5]
    return md_table(headers, rows)

def team_hitter_pool(sc, team_code):
    if sc.empty or not team_code or "batter_team" not in sc.columns or "batter_name" not in sc.columns:
        return pd.DataFrame()

    t = sc[sc["batter_team"] == team_code]
    rows = []

    for name, g in t.groupby("batter_name"):
        if not name or pd.isna(name):
            continue

        avg, slg, iso, woba, xwoba, barrel, hard, whiff, pa = event_stats(g)

        if pa < 10:
            continue

        rows.append({
            "Hitter": name,
            "PA": pa,
            "AVG": avg,
            "SLG": slg,
            "ISO": iso,
            "wOBA": woba if woba is not None else 0,
            "xwOBA": xwoba if xwoba is not None else 0,
            "Barrel%": barrel,
            "HardHit%": hard,
            "Whiff%": whiff,
        })

    df = pd.DataFrame(rows)

    if df.empty or "PA" not in df.columns:
        return pd.DataFrame()

    return df.sort_values(["PA", "wOBA"], ascending=[False, False]).head(12)

def hitter_pool_md(df):
    headers = ["Hitter", "PA", "AVG", "SLG", "ISO", "wOBA", "xwOBA", "Barrel%", "HardHit%", "Whiff%"]

    if df.empty:
        return md_table(headers, [])

    rows = []
    for _, r in df.iterrows():
        rows.append([
            r["Hitter"],
            int(r["PA"]),
            fmt(r["AVG"]),
            fmt(r["SLG"]),
            fmt(r["ISO"]),
            fmt(r["wOBA"]),
            fmt(r["xwOBA"]),
            pct(r["Barrel%"]),
            pct(r["HardHit%"]),
            pct(r["Whiff%"]),
        ])

    return md_table(headers, rows)

def hitter_vs_pitch(sc, hitters, pitches):
    headers = ["Pitch", "Hitter", "PA", "AVG", "SLG", "ISO", "wOBA", "xwOBA", "Barrel%", "HardHit%", "Whiff%"]

    if sc.empty or hitters.empty or not pitches or "batter_name" not in sc.columns or "pitch_type" not in sc.columns:
        return md_table(headers, [])

    names = set(hitters["Hitter"].astype(str).str.lower())
    rows = []

    for pitch in pitches:
        pitch_df = sc[sc["pitch_type"] == pitch]

        for name in names:
            h = pitch_df[pitch_df["batter_name"].astype(str).str.lower() == name]

            if h.empty:
                continue

            avg, slg, iso, woba, xwoba, barrel, hard, whiff, pa = event_stats(h)

            if pa < 3:
                continue

            rows.append([
                pitch,
                name.title(),
                pa,
                fmt(avg),
                fmt(slg),
                fmt(iso),
                fmt(woba),
                fmt(xwoba),
                pct(barrel),
                pct(hard),
                pct(whiff),
            ])

    if not rows:
        return md_table(headers, [])

    rows = sorted(rows, key=lambda r: float(r[5]) if r[5] != "—" else 0, reverse=True)[:30]
    return md_table(headers, rows)

def game_dissection(sc, g, away_hitters, home_hitters):
    away_mix = major_pitches(sc, g["away_sp"])
    home_mix = major_pitches(sc, g["home_sp"])

    return f"""
## Final Game Dissection

- Away pitcher pitch mix to inspect: {", ".join(away_mix) if away_mix else "No current Statcast sample"}
- Home pitcher pitch mix to inspect: {", ".join(home_mix) if home_mix else "No current Statcast sample"}
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen context: not included yet.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, and current form.
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

{md_table(["Field", "Value"], [
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

## {g['away_team']} Team Hitter Pool

{hitter_pool_md(away_hitters)}

## {g['home_team']} Team Hitter Pool

{hitter_pool_md(home_hitters)}

{game_dissection(sc, g, away_hitters, home_hitters)}
"""

def main():
    games = get_schedule()
    sc = load_statcast()

    report = f"""# MLB-LAB V5.1 Pitch Matchup Engine

Date: {TODAY}

This runner uses:
- MLB Stats API for slate, teams, parks, probable pitchers
- Baseball Savant / Statcast for pitcher arsenal, L/R splits, hitter pools, hitter-vs-pitch matchups

Removed:
- FanGraphs hard dependency
- sportsbook odds
- CSV dependency
- scoring gimmicks
- weak-pitch labels
- manual placeholder tables

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
