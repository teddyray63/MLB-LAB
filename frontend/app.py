import streamlit as st
import pandas as pd
import requests
import sqlite3

def load_daily_scores():
    conn = sqlite3.connect("database/mlb_lab.db")
    df = pd.read_sql("SELECT * FROM daily_scores", conn)
    conn.close()
    return df

daily_scores = load_daily_scores()

API = "http://127.0.0.1:8000"

st.set_page_config(page_title="MLB-LAB", layout="wide")
st.title("MLB-LAB Game Hub")

def get(path):
    return requests.get(f"{API}{path}", timeout=20).json()

games = pd.DataFrame(get("/games"))
lineups = pd.DataFrame(get("/lineups"))
parks = pd.DataFrame(get("/park-factors"))
hitters = pd.DataFrame(get("/statcast/hitters"))
pitchers = pd.DataFrame(get("/statcast/pitchers"))

games = games.merge(parks, on="venue", how="left")

game_labels = games.apply(
    lambda r: f"{r['away_team']} @ {r['home_team']} — {r['venue']}",
    axis=1,
).tolist()

selected = st.selectbox("Choose Game", game_labels)
game = games.iloc[game_labels.index(selected)]

st.header(selected)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Status", game.get("status", ""))
c2.metric("Run Factor", int(game.get("run_factor") or 100))
c3.metric("Hit Factor", int(game.get("hit_factor") or 100))
c4.metric("HR Factor", int(game.get("hr_factor") or 100))

st.subheader("Probable Pitchers")
p1, p2 = st.columns(2)
p1.write(f"**{game['away_team']}**: {game.get('away_probable', '')}")
p2.write(f"**{game['home_team']}**: {game.get('home_probable', '')}")

with st.expander("Lineups", expanded=True):
    gl = lineups[lineups["game_pk"] == game["game_pk"]]

    left, right = st.columns(2)

    with left:
        st.markdown(f"### {game['away_team']}")
        st.dataframe(
            gl[gl["team"] == game["away_team"]][
                ["batting_order", "player_name", "position", "confirmed"]
            ],
            use_container_width=True,
        )

    with right:
        st.markdown(f"### {game['home_team']}")
        st.dataframe(
            gl[gl["team"] == game["home_team"]][
                ["batting_order", "player_name", "position", "confirmed"]
            ],
            use_container_width=True,
        )

st.markdown("---")

with st.expander("Team Run Profile", expanded=True):
    left, right = st.columns(2)

    for col, team in [(left, game["away_team"]), (right, game["home_team"])]:
        with col:
            st.subheader(team)
            st.metric("Runs/Game", "—")
            st.metric("First 5 Runs", "—")
            st.metric("Home/Away Runs", "—")
            st.metric("vs RHP/LHP", "—")
            st.metric("Last 7", "—")
            st.metric("Last 15", "—")
            st.metric("OPS", "—")
            st.metric("ISO", "—")
            st.metric("wRC+", "—")

with st.expander("Pitcher Run Profile", expanded=True):
    left, right = st.columns(2)

    for col, pitcher in [(left, game.get("away_probable", "")), (right, game.get("home_probable", ""))]:
        with col:
            st.subheader(pitcher)
            st.metric("ERA", "—")
            st.metric("xERA", "—")
            st.metric("WHIP", "—")
            st.metric("Runs Allowed/Game", "—")
            st.metric("Runs Allowed First 5", "—")
            st.metric("Home ERA", "—")
            st.metric("Away ERA", "—")
            st.metric("vs Left", "—")
            st.metric("vs Right", "—")
            st.metric("Last 5 Starts", "—")

with st.expander("Best Hitter Matchups", expanded=True):
    st.caption("Top 7 hitters by key Statcast power/contact indicators.")

    top_hitters = hitters.sort_values(
        ["barrel_pct", "avg_ev"],
        ascending=False,
    ).head(7)

    st.dataframe(
        top_hitters[
            ["player_name", "pa", "avg_ev", "max_ev", "barrel_pct", "hard_hit_pct", "xwoba", "xba", "xslg"]
        ],
        use_container_width=True,
    )

with st.expander("Pitcher Arsenal / Weak Spots", expanded=True):
    top_pitchers = pitchers.sort_values(
        ["whiff_pct", "avg_velo"],
        ascending=False,
    ).head(7)

    st.dataframe(
        top_pitchers[
            ["player_name", "pitch_count", "avg_velo", "max_velo", "whiff_pct", "hard_hit_pct", "xwoba"]
        ],
        use_container_width=True,
    )

st.markdown("---")

with st.expander("Betting Hub", expanded=True):
    st.subheader("Stats-Only Betting Hub")
    st.caption("No sportsbooks. No Vegas. No odds. Research-only builder using singles, doubles, total bases, 1.5 hits, runs, and RBIs.")

    def safe_cols(df, wanted):
        return [c for c in wanted if c in df.columns]

    def show_candidates(title, checklist, score_col, rows=10):
        st.subheader(title)
        st.info("Research Checklist\n\n" + "\n".join([f"• {x}" for x in checklist]))

        df = daily_scores.copy()

        display_cols = safe_cols(df, [
            "player_name",
            "team",
            "singles_score",
            "doubles_score",
            "total_bases_score",
            "runs_score",
            "rbi_score",
            "lotto_score",
            "avg_ev",
            "max_ev",
            "barrel_pct",
            "hard_hit_pct",
            "xba",
            "xslg",
            "xwoba",
        ])

        if score_col in df.columns:
            df = df.sort_values(score_col, ascending=False)

        st.dataframe(
            df[display_cols].head(rows),
            use_container_width=True
        )

    tabs = st.tabs([
        "🎾 Singles",
        "⚾ Doubles",
        "💥 Total Bases",
        "🔥 1.5 Hits",
        "🏃 Runs",
        "💰 RBIs",
        "🎲 5 → 250 Lotto",
        "🚀 10 → 10K Challenge",
    ])

    with tabs[0]:
        show_candidates(
            "Best Singles Candidates",
            ["High Contact %", "Low Strikeout %", "xBA", "Recent Form", "Batter vs Pitch Type", "Hard Hit %"],
            "singles_score",
            12
        )

    with tabs[1]:
        show_candidates(
            "Best Doubles Candidates",
            ["Gap Power", "Hard Hit %", "Barrel %", "Park Factor", "Extra Base Hit %", "Exit Velocity"],
            "doubles_score",
            12
        )

    with tabs[2]:
        show_candidates(
            "Best Total Bases Candidates",
            ["Barrel %", "Hard Hit %", "xSLG", "ISO", "Park Factor", "Matchup Advantage"],
            "total_bases_score",
            12
        )

    with tabs[3]:
        show_candidates(
            "Best 1.5 Hits Candidates",
            ["Singles Score", "Contact Skill", "xBA", "Recent Form", "Lineup Spot"],
            "singles_score",
            12
        )

    with tabs[4]:
        show_candidates(
            "Best Runs Candidates",
            ["Top Lineup Position", "On-Base Skill", "Team Run Environment", "Park Run Factor", "Hitters Behind Him"],
            "runs_score",
            12
        )

    with tabs[5]:
        show_candidates(
            "Best RBI Candidates",
            ["Middle Order", "Power", "Team Run Environment", "Runners Ahead", "Pitcher Weakness"],
            "rbi_score",
            12
        )

    with tabs[6]:
        st.subheader("🎲 $5 → $250 Lotto Builder")
        st.info("""
Build 3–5 leg lotto cards from stats only.

Recommended structure:
1. One safe singles candidate
2. One total bases upside candidate
3. One RBI or runs candidate
4. Optional doubles candidate
5. Optional 1.5 hits only if profile is strong

Avoid forcing plays. Only combine hitters with multiple stat edges.
""")
        show_candidates(
            "Top Lotto Candidates",
            ["Multiple Score Edges", "Power", "Contact", "Run/RBI Environment", "Upside"],
            "lotto_score",
            15
        )

    with tabs[7]:
        st.subheader("🚀 $10 → $10K Challenge Research Path")
        st.info("""
Goal: build repeatable stat-only decision discipline.

10-step path:
1. Pick one game only.
2. Confirm both lineups.
3. Check park factor.
4. Check pitcher run profile.
5. Check team run profile.
6. Find top 7 hitter matchup edges.
7. Separate singles, doubles, total bases, 1.5 hits, runs, RBIs.
8. Choose only 1–2 strongest plays.
9. Track result manually.
10. Repeat only if the same research standard is met.

This is a research workflow, not sportsbook or Vegas-based.
""")
        show_candidates(
            "Top Challenge Candidates",
            ["Highest Overall Scores", "Repeatable Edge", "Contact + Power", "Run Environment"],
            "lotto_score",
            15
        )