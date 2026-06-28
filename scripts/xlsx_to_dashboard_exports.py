import pandas as pd
from pathlib import Path

XLSX = Path("reports/mlb-lab-v5-matchup-engine.xlsx")
OUT = Path("exports")
OUT.mkdir(exist_ok=True)

if not XLSX.exists():
    raise SystemExit(f"Missing workbook: {XLSX}")

xls = pd.ExcelFile(XLSX)

# Slate
if "Slate" in xls.sheet_names:
    pd.read_excel(XLSX, sheet_name="Slate").dropna(how="all").to_csv(OUT/"slate.csv", index=False)

# Command Center
cmd_sheet = next((s for s in xls.sheet_names if "Command" in s or "Center" in s), None)
if cmd_sheet:
    df = pd.read_excel(XLSX, sheet_name=cmd_sheet).dropna(how="all")
    df.to_csv(OUT/"command_center.csv", index=False)
else:
    mm = pd.read_excel(XLSX, sheet_name="Master Matchups").dropna(how="all")
    keep = [c for c in ["Hitter","Player","Team","Hitter Team","Game","Opp SP","Pitch","wOBA","xwOBA","xBA","xSLG","Barrel%","HardHit%","Whiff%"] if c in mm.columns]
    df = mm[keep].copy()
    score_cols = [c for c in ["xwOBA","xBA","xSLG","wOBA","Barrel%","HardHit%"] if c in df.columns]
    df["Score"] = df[score_cols].rank(pct=True).mean(axis=1).mul(100).round(1)
    df["Tier"] = pd.cut(df["Score"], bins=[-1,70,85,101], labels=["C","B","A"])
    df["Best Market"] = "Best"
    df = df.sort_values("Score", ascending=False).head(25)
    df.insert(0, "Rank", range(1, len(df)+1))
    df.to_csv(OUT/"command_center.csv", index=False)

# Category exports from Master Matchups
mm = pd.read_excel(XLSX, sheet_name="Master Matchups").dropna(how="all")
cats = {
    "hits.csv": ["xBA","AVG","wOBA"],
    "singles.csv": ["AVG","xBA","Whiff%"],
    "tb.csv": ["xSLG","SLG","ISO"],
    "hrr.csv": ["wOBA","xwOBA","xBA","HardHit%"],
    "hr.csv": ["ISO","xSLG","Barrel%","HardHit%"],
}
for fname, cols in cats.items():
    use = [c for c in cols if c in mm.columns]
    base = mm.copy()
    if use:
        base["Score"] = base[use].rank(pct=True).mean(axis=1).mul(100).round(1)
    else:
        base["Score"] = 0
    base = base.sort_values("Score", ascending=False).head(20)
    base.insert(0, "Rank", range(1, len(base)+1))
    base.to_csv(OUT/fname, index=False)

# Game pages
games = [s for s in xls.sheet_names if s.startswith("G")]
frames = []
for g in games:
    temp = pd.read_excel(XLSX, sheet_name=g).dropna(how="all")
    temp.insert(0, "Sheet", g)
    frames.append(temp)
if frames:
    pd.concat(frames, ignore_index=True).to_csv(OUT/"games.csv", index=False)

print("✅ exports created")
