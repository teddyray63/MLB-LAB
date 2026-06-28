import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="MLB-LAB", layout="wide")
OUT = Path("exports")

def load(name):
    p = OUT / name
    return pd.read_csv(p) if p.exists() else pd.DataFrame()

def clean(df):
    if df.empty: return df
    df = df.loc[:, ~df.columns.astype(str).str.contains("^Unnamed")]
    return df.fillna("")

def pick_cols(df, cols):
    df = clean(df)
    return df[[c for c in cols if c in df.columns]]

def add_model_cols(df):
    df = clean(df).copy()
    if df.empty: return df
    metrics = [c for c in ["xwOBA","xBA","xSLG","wOBA","SLG","ISO","Barrel%","HardHit%"] if c in df.columns]
    if "Score" not in df.columns and metrics:
        df["Score"] = df[metrics].apply(pd.to_numeric, errors="coerce").rank(pct=True).mean(axis=1).mul(100).round(1)
    if "Tier" not in df.columns and "Score" in df.columns:
        df["Tier"] = pd.cut(pd.to_numeric(df["Score"], errors="coerce"), [-1,75,88,101], labels=["C","B","A"])
    if "Why" not in df.columns:
        why = []
        for _, r in df.iterrows():
            parts = []
            for c in ["xwOBA","xBA","xSLG","Barrel%","HardHit%"]:
                if c in df.columns and str(r.get(c,"")) != "":
                    parts.append(f"{c} {r.get(c)}")
            why.append(", ".join(parts[:3]) if parts else "Strong model profile")
        df["Why"] = why
    if "Risk" not in df.columns:
        risk = []
        for _, r in df.iterrows():
            flags = []
            try:
                if float(r.get("PA",999)) < 10: flags.append("Low PA")
            except: pass
            try:
                if float(str(r.get("Whiff%","0")).replace("%","")) > 0.30: flags.append("High Whiff")
            except: pass
            risk.append(" + ".join(flags) if flags else "None")
        df["Risk"] = risk
    return df

def style(df):
    def color_score(v):
        try:
            v=float(v)
            if v>=90: return "background-color:#0f9d58;color:white;font-weight:bold"
            if v>=80: return "background-color:#f4b400;color:#111;font-weight:bold"
            return "background-color:#db4437;color:white;font-weight:bold"
        except: return ""
    def color_tier(v):
        v=str(v).upper()
        if v=="A": return "background-color:#0f9d58;color:white;font-weight:bold"
        if v=="B": return "background-color:#f4b400;color:#111;font-weight:bold"
        if v=="C": return "background-color:#db4437;color:white;font-weight:bold"
        return ""
    sty = df.style
    if "Score" in df: sty = sty.map(color_score, subset=["Score"])
    if "Tier" in df: sty = sty.map(color_tier, subset=["Tier"])
    return sty

st.markdown("""
<style>
.block-container {padding-top:2rem; max-width:1450px;}
[data-testid="stMetric"] {background:#171b22; border:1px solid #2b313b; padding:14px; border-radius:14px;}
h1,h2,h3 {letter-spacing:-0.03em;}
</style>
""", unsafe_allow_html=True)

cmd = add_model_cols(load("command_center.csv"))
slate = clean(load("slate.csv"))
games = clean(load("games.csv"))

st.title("⚾ MLB-LAB Command Center")
st.caption("Top plays first. Prop boards second. Evidence only when needed.")

tabs = st.tabs(["🏠 Command Center", "🔥 Prop Boards", "⚾ Game Evidence", "📄 Daily Card"])

with tabs[0]:
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Top Plays", len(cmd))
    c2.metric("A Tier", int((cmd["Tier"].astype(str)=="A").sum()) if "Tier" in cmd else 0)
    c3.metric("Best Score", cmd["Score"].max() if "Score" in cmd else "-")
    c4.metric("Games", cmd["Game"].nunique() if "Game" in cmd else "-")

    st.subheader("🏠 Best Plays")
    view = pick_cols(cmd, ["Rank","Hitter","Player","Team","Hitter Team","Game","Opp SP","Pitch","Best Market","Score","Tier","Why","Risk"])
    st.dataframe(style(view.head(30)), use_container_width=True, hide_index=True)

with tabs[1]:
    boards = {
        "🔥 Hits": "hits.csv",
        "🎯 Singles": "singles.csv",
        "💥 Total Bases": "tb.csv",
        "⚡ HRR": "hrr.csv",
        "💣 Home Runs": "hr.csv",
    }
    pick = st.radio("Market", list(boards), horizontal=True)
    df = add_model_cols(load(boards[pick]))
    view = pick_cols(df, ["Rank","Hitter","Player","Team","Hitter Team","Game","Opp SP","Pitch","Score","Tier","Why","Risk","PA","AVG","SLG","ISO","wOBA","xwOBA","xBA","xSLG","Barrel%","HardHit%","Whiff%"])
    st.dataframe(style(view.head(30)), use_container_width=True, hide_index=True)

with tabs[2]:
    st.subheader("⚾ Game Evidence")
    if games.empty:
        st.warning("No game evidence found.")
    else:
        if "Sheet" in games:
            g = st.selectbox("Game", games["Sheet"].dropna().unique())
            games = games[games["Sheet"] == g]
        st.dataframe(games, use_container_width=True, hide_index=True)

with tabs[3]:
    st.subheader("📄 Printable Daily Card")
    if not slate.empty:
        st.markdown("### Slate")
        st.dataframe(slate.head(20), use_container_width=True, hide_index=True)
    st.markdown("### Top Plays")
    card = pick_cols(cmd, ["Rank","Hitter","Player","Team","Hitter Team","Game","Opp SP","Best Market","Score","Tier","Why","Risk"]).head(25)
    st.dataframe(style(card), use_container_width=True, hide_index=True)

    html = card.to_html(index=False)
    report = f"<html><body><h1>⚾ MLB-LAB Daily Card</h1>{html}</body></html>"
    Path("reports/mlb-lab-daily-card.html").write_text(report)
    st.download_button("Download Daily Card HTML", report, "mlb-lab-daily-card.html", "text/html")
