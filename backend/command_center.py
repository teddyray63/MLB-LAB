import json
import sqlite3
from datetime import date, datetime
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "database" / "mlb_lab.db"
CONFIG_PATH = ROOT / "backend" / "betting_config.json"
EXPORT_DIR = ROOT / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

REQUIRED_TABLES = ["games", "lineups", "daily_scores"]


def load_config():
    defaults = {
        "minimum_confidence": 30.0,
        "minimum_edge": 7.0,
        "top_players_per_game": 5,
        "lotto_legs": 4,
        "safe_legs": 2,
        "csv_exports": {
            "daily_report": "exports/daily_report.csv",
            "singles": "exports/singles.csv",
            "total_bases": "exports/total_bases.csv",
            "command_center": "exports/command_center.csv",
        },
        "pdf_output": "exports/daily_report.pdf",
        "text_output": "exports/daily_report.txt",
    }
    if not CONFIG_PATH.exists():
        return defaults
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        defaults.update(data)
        if "csv_exports" in data and isinstance(data["csv_exports"], dict):
            defaults["csv_exports"].update(data["csv_exports"])
        return defaults
    except Exception:
        return defaults


CONFIG = load_config()


def read_table(conn, table):
    try:
        return pd.read_sql(f"SELECT * FROM {table}", conn)
    except Exception:
        return pd.DataFrame()


def norm(name):
    if not isinstance(name, str):
        return ""
    name = name.strip()
    if "," in name:
        last, first = [x.strip() for x in name.split(",", 1)]
        return f"{first} {last}".lower()
    return name.lower()


def grade(score):
    try:
        s = float(score)
    except Exception:
        return "C"
    if s >= 60:
        return "A+ 🔥"
    if s >= 50:
        return "A ⭐"
    if s >= 42:
        return "B+"
    if s >= 35:
        return "B"
    return "C"


def safe_float(value):
    try:
        return float(value)
    except Exception:
        return 0.0


def build_game_window(games_df):
    if games_df.empty:
        return games_df
    if "game_date" in games_df.columns:
        today = date.today().strftime("%Y-%m-%d")
        today_games = games_df[games_df["game_date"].astype(str) == today]
        if not today_games.empty:
            return today_games
        recent = games_df.copy()
        recent["game_date"] = recent["game_date"].astype(str)
        recent = recent.sort_values("game_date", ascending=False)
        return recent.head(8)
    return games_df.head(8)


def ensure_player_alignment(scores_df, lineups_df):
    if scores_df.empty or lineups_df.empty:
        return scores_df
    work_scores = scores_df.copy()
    work_lineups = lineups_df.copy()
    work_scores["name_key"] = work_scores["player_name"].apply(norm)
    work_lineups["name_key"] = work_lineups["player_name"].apply(norm)
    lineup_map = work_lineups[["name_key", "team"]].drop_duplicates("name_key")
    work_scores = work_scores.drop(columns=["team"], errors="ignore").merge(lineup_map, on="name_key", how="left")
    work_scores["team"] = work_scores["team"].fillna("")
    return work_scores


def unique_card(df, markets, limit=4):
    used, legs = set(), []
    for label, col in markets:
        if col not in df.columns:
            continue
        for _, row in df.sort_values(col, ascending=False).iterrows():
            player = row.get("player_name", "")
            if not player or player in used:
                continue
            used.add(player)
            legs.append(
                {
                    "market": label,
                    "player": player,
                    "team": row.get("team", ""),
                    "score": safe_float(row.get(col, 0)),
                    "grade": grade(row.get(col, 0)),
                }
            )
            if len(legs) >= limit:
                break
    return legs


def top_players(df, col, n=5):
    cols = ["player_name", "team", col, "avg_ev", "max_ev", "barrel_pct", "hard_hit_pct", "xba", "xslg", "xwoba"]
    cols = [c for c in cols if c in df.columns]
    if not cols:
        return pd.DataFrame()
    return df.sort_values(col, ascending=False)[cols].head(n)


def build_reasons(legs, market_type):
    if not legs:
        return []
    reasons = []
    for leg in legs:
        if market_type == "safe":
            reasons.append(f"{leg['player']} ({leg['team']}) offers a strong {leg['market']} profile with {leg['score']:.2f} support.")
        else:
            reasons.append(f"{leg['player']} ({leg['team']}) brings upside via {leg['market']} at {leg['score']:.2f}.")
    return reasons


def build_risk_notes(legs, lineup_ok):
    if not legs:
        return []
    notes = []
    for leg in legs:
        note_parts = []
        if not lineup_ok:
            note_parts.append("lineup availability not confirmed")
        if safe_float(leg["score"]) < CONFIG["minimum_confidence"]:
            note_parts.append("score below minimum confidence")
        if safe_float(leg["score"]) < CONFIG["minimum_edge"]:
            note_parts.append("edge below threshold")
        notes.append("; ".join(note_parts) if note_parts else "monitor for late lineup shifts")
    return notes


def render_text_report(lines):
    text = "\n".join(lines)
    return text.rstrip() + "\n"


def write_text_output(path, content):
    path.write_text(content, encoding="utf-8")


def write_pdf_output(path, content):
    lines = content.splitlines()
    if not lines:
        lines = ["No report available."]

    objects = []
    content_stream = []
    y = 760
    for line in lines:
        escaped = line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        content_stream.append(f"BT /F1 10 Tf 50 {y} Td ({escaped}) Tj ET")
        y -= 12

    content_body = "\n".join(content_stream)
    content_bytes = content_body.encode("latin-1", "replace")
    content_len = len(content_bytes)

    objects.append(b"%PDF-1.4\n")
    objects.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    objects.append(b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n")
    objects.append(b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n")
    objects.append(f"4 0 obj\n<< /Length {content_len} >>\nstream\n".encode("latin-1") + content_bytes + b"\nendstream\nendobj\n")
    objects.append(b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n")

    pdf_bytes = b"".join(objects)
    offsets = []
    cursor = 0
    for obj in objects:
        offsets.append(cursor)
        cursor += len(obj)

    xref_offset = cursor
    pdf_bytes += f"xref\n0 {len(objects) + 1}\n".encode("latin-1")
    pdf_bytes += b"0000000000 65535 f \n"
    for offset in offsets:
        pdf_bytes += f"{offset:010d} 00000 n \n".encode("latin-1")
    pdf_bytes += f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("latin-1")
    path.write_bytes(pdf_bytes)


def write_exports(rows, path):
    if not rows:
        pd.DataFrame(columns=["section", "game", "player", "team", "market", "score", "grade", "confidence_grade", "reasons", "risk_notes"]).to_csv(path, index=False)
        return
    pd.DataFrame(rows).to_csv(path, index=False)


def main():
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines = []
    report_rows = []
    singles_rows = []
    total_bases_rows = []
    command_rows = []

    report_lines.append("==============================")
    report_lines.append("MLB-LAB COMMAND CENTER")
    report_lines.append(f"Generated: {start_time}")
    report_lines.append("==============================")

    if not DB_PATH.exists():
        report_lines.append("Database missing: database/mlb_lab.db")
        report_lines.append("Fix: restore or regenerate the SQLite file before running the pipeline.")
    else:
        conn = sqlite3.connect(DB_PATH)
        games = read_table(conn, "games")
        scores = read_table(conn, "daily_scores")
        lineups = read_table(conn, "lineups")
        conn.close()

        report_lines.append(f"games: {len(games)} | scores: {len(scores)} | lineups: {len(lineups)}")

        if games.empty or scores.empty or lineups.empty:
            report_lines.append("Core tables are missing or empty.")
            report_lines.append("Fix: run the available collectors or restore the database tables before generating reports.")
        else:
            games = games.drop_duplicates(subset=[c for c in ["away_team", "home_team", "venue"] if c in games.columns])
            games = build_game_window(games)
            scores = ensure_player_alignment(scores, lineups)

            if scores.empty:
                report_lines.append("Scores could not be aligned to lineup names.")
                report_lines.append("Fix: verify the lineup player names match the daily score player names.")
            else:
                for _, game in games.iterrows():
                    away = game.get("away_team", "")
                    home = game.get("home_team", "")
                    venue = game.get("venue", "")
                    game_pk = game.get("game_pk", "")
                    game_header = f"{away} @ {home} — {venue}"
                    report_lines.append("")
                    report_lines.append("=" * 90)
                    report_lines.append(game_header)
                    report_lines.append("=" * 90)

                    game_df = scores[scores["team"].isin([away, home])].copy()
                    if game_pk not in [None, ""]:
                        lineup_rows = lineups[lineups["game_pk"] == game_pk]
                        if not lineup_rows.empty:
                            lineup_keys = set(norm(x) for x in lineup_rows["player_name"] if isinstance(x, str))
                            game_df = game_df[game_df["name_key"].isin(lineup_keys) | game_df["team"].isin([away, home])].copy()

                    if game_df.empty:
                        report_lines.append("No aligned players found for this game.")
                        continue

                    top_singles = top_players(game_df, "singles_score", n=int(CONFIG.get("top_players_per_game", 5)))
                    top_tb = top_players(game_df, "total_bases_score", n=int(CONFIG.get("top_players_per_game", 5)))

                    report_lines.append("")
                    report_lines.append("TOP 5 SINGLES")
                    if not top_singles.empty:
                        report_lines.extend(top_singles.to_string(index=False).splitlines())
                    else:
                        report_lines.append("No singles data.")

                    report_lines.append("")
                    report_lines.append("TOP 5 TOTAL BASES")
                    if not top_tb.empty:
                        report_lines.extend(top_tb.to_string(index=False).splitlines())
                    else:
                        report_lines.append("No total bases data.")

                    safe_legs = unique_card(game_df, [("1+ Hit / Single Profile", "singles_score"), ("Total Bases", "total_bases_score")], limit=int(CONFIG.get("safe_legs", 2)))
                    lotto_legs = unique_card(game_df, [("1+ Hit", "singles_score"), ("Total Bases", "total_bases_score"), ("Run", "runs_score"), ("RBI", "rbi_score")], limit=int(CONFIG.get("lotto_legs", 4)))
                    safe_score = sum(leg["score"] for leg in safe_legs) / max(len(safe_legs), 1)
                    lotto_score = sum(leg["score"] for leg in lotto_legs) / max(len(lotto_legs), 1)
                    confidence_grade = grade(safe_score + lotto_score)

                    report_lines.append("")
                    report_lines.append("SAFEST 2-LEG CARD")
                    for leg in safe_legs:
                        report_lines.append(f"- {leg['player']} ({leg['team']}) — {leg['market']} — {leg['score']:.2f} — {leg['grade']}")

                    report_lines.append("")
                    report_lines.append("HIGHEST UPSIDE 4-LEG LOTTO")
                    for leg in lotto_legs:
                        report_lines.append(f"- {leg['player']} ({leg['team']}) — {leg['market']} — {leg['score']:.2f} — {leg['grade']}")

                    report_lines.append("")
                    report_lines.append(f"CONFIDENCE GRADE: {confidence_grade}")
                    report_lines.append("REASONS:")
                    report_lines.extend([f"- {reason}" for reason in build_reasons(safe_legs, "safe")])
                    report_lines.append("RISK NOTES:")
                    report_lines.extend([f"- {note}" for note in build_risk_notes(safe_legs, not lineups.empty)])

                    for leg in safe_legs:
                        command_rows.append({
                            "section": "safe_card",
                            "game": game_header,
                            "player": leg["player"],
                            "team": leg["team"],
                            "market": leg["market"],
                            "score": leg["score"],
                            "grade": leg["grade"],
                            "confidence_grade": confidence_grade,
                            "reasons": "High singles/total bases profile",
                            "risk_notes": "monitor lineup status",
                        })
                    for leg in lotto_legs:
                        command_rows.append({
                            "section": "lotto_card",
                            "game": game_header,
                            "player": leg["player"],
                            "team": leg["team"],
                            "market": leg["market"],
                            "score": leg["score"],
                            "grade": leg["grade"],
                            "confidence_grade": confidence_grade,
                            "reasons": "Cross-market upside",
                            "risk_notes": "monitor lineup status",
                        })

                    for _, row in top_singles.head(int(CONFIG.get("top_players_per_game", 5))).iterrows():
                        singles_rows.append({
                            "section": "top_singles",
                            "game": game_header,
                            "player": row.get("player_name", ""),
                            "team": row.get("team", ""),
                            "market": "singles",
                            "score": safe_float(row.get("singles_score", 0)),
                            "grade": grade(row.get("singles_score", 0)),
                            "confidence_grade": confidence_grade,
                            "reasons": "Top singles profile",
                            "risk_notes": "lineup availability should be confirmed",
                        })
                    for _, row in top_tb.head(int(CONFIG.get("top_players_per_game", 5))).iterrows():
                        total_bases_rows.append({
                            "section": "top_total_bases",
                            "game": game_header,
                            "player": row.get("player_name", ""),
                            "team": row.get("team", ""),
                            "market": "total_bases",
                            "score": safe_float(row.get("total_bases_score", 0)),
                            "grade": grade(row.get("total_bases_score", 0)),
                            "confidence_grade": confidence_grade,
                            "reasons": "Top total bases profile",
                            "risk_notes": "lineup availability should be confirmed",
                        })

                report_lines.append("")
                report_lines.append("=" * 90)
                report_lines.append("OVERALL ACTION BOARD")
                report_lines.append("=" * 90)

                overall_scores = scores[scores["team"].astype(str) != ""].copy()
                overall_scores["prizepicks_score"] = (
                    overall_scores["singles_score"].fillna(0) +
                    overall_scores["total_bases_score"].fillna(0) +
                    overall_scores["runs_score"].fillna(0) +
                    overall_scores["rbi_score"].fillna(0)
                ) / 4.0

                report_lines.append("")
                report_lines.append("TOP 10 SINGLES OVERALL")
                for _, row in overall_scores.sort_values("singles_score", ascending=False).head(10).iterrows():
                    report_lines.append(f"- {row.get('player_name', '')} ({row.get('team', '')}) — singles {safe_float(row.get('singles_score', 0)):.2f}")
                    report_rows.append({"section": "top_singles_overall", "game": "Overall", "player": row.get("player_name", ""), "team": row.get("team", ""), "market": "singles", "score": safe_float(row.get("singles_score", 0)), "grade": grade(row.get("singles_score", 0)), "confidence_grade": grade(safe_float(row.get("singles_score", 0))), "reasons": "Overall singles leader", "risk_notes": "monitor lineup status"})

                report_lines.append("")
                report_lines.append("TOP 10 TOTAL BASES OVERALL")
                for _, row in overall_scores.sort_values("total_bases_score", ascending=False).head(10).iterrows():
                    report_lines.append(f"- {row.get('player_name', '')} ({row.get('team', '')}) — total bases {safe_float(row.get('total_bases_score', 0)):.2f}")
                    report_rows.append({"section": "top_total_bases_overall", "game": "Overall", "player": row.get("player_name", ""), "team": row.get("team", ""), "market": "total_bases", "score": safe_float(row.get("total_bases_score", 0)), "grade": grade(row.get("total_bases_score", 0)), "confidence_grade": grade(safe_float(row.get("total_bases_score", 0))), "reasons": "Overall total bases leader", "risk_notes": "monitor lineup status"})

                report_lines.append("")
                report_lines.append("TOP 10 HR")
                for _, row in overall_scores.sort_values("total_bases_score", ascending=False).head(10).iterrows():
                    report_lines.append(f"- {row.get('player_name', '')} ({row.get('team', '')}) — hr proxy {safe_float(row.get('total_bases_score', 0)):.2f}")
                    report_rows.append({"section": "top_hr", "game": "Overall", "player": row.get("player_name", ""), "team": row.get("team", ""), "market": "hr_proxy", "score": safe_float(row.get("total_bases_score", 0)), "grade": grade(row.get("total_bases_score", 0)), "confidence_grade": grade(safe_float(row.get("total_bases_score", 0))), "reasons": "High slugging profile", "risk_notes": "monitor lineup status"})

                report_lines.append("")
                report_lines.append("TOP 10 RBI")
                for _, row in overall_scores.sort_values("rbi_score", ascending=False).head(10).iterrows():
                    report_lines.append(f"- {row.get('player_name', '')} ({row.get('team', '')}) — rbi {safe_float(row.get('rbi_score', 0)):.2f}")
                    report_rows.append({"section": "top_rbi", "game": "Overall", "player": row.get("player_name", ""), "team": row.get("team", ""), "market": "rbi", "score": safe_float(row.get("rbi_score", 0)), "grade": grade(row.get("rbi_score", 0)), "confidence_grade": grade(safe_float(row.get("rbi_score", 0))), "reasons": "Strong RBI profile", "risk_notes": "monitor lineup status"})

                report_lines.append("")
                report_lines.append("TOP 10 RUNS")
                for _, row in overall_scores.sort_values("runs_score", ascending=False).head(10).iterrows():
                    report_lines.append(f"- {row.get('player_name', '')} ({row.get('team', '')}) — runs {safe_float(row.get('runs_score', 0)):.2f}")
                    report_rows.append({"section": "top_runs", "game": "Overall", "player": row.get("player_name", ""), "team": row.get("team", ""), "market": "runs", "score": safe_float(row.get("runs_score", 0)), "grade": grade(row.get("runs_score", 0)), "confidence_grade": grade(safe_float(row.get("runs_score", 0))), "reasons": "Strong run-scoring profile", "risk_notes": "monitor lineup status"})

                report_lines.append("")
                report_lines.append("TOP 10 PRIZEPICKS PLAYS")
                for _, row in overall_scores.sort_values("prizepicks_score", ascending=False).head(10).iterrows():
                    report_lines.append(f"- {row.get('player_name', '')} ({row.get('team', '')}) — prizepicks {safe_float(row.get('prizepicks_score', 0)):.2f}")
                    report_rows.append({"section": "prizepicks", "game": "Overall", "player": row.get("player_name", ""), "team": row.get("team", ""), "market": "prizepicks", "score": safe_float(row.get("prizepicks_score", 0)), "grade": grade(row.get("prizepicks_score", 0)), "confidence_grade": grade(safe_float(row.get("prizepicks_score", 0))), "reasons": "Balanced multi-market profile", "risk_notes": "monitor lineup status"})

                report_lines.append("")
                report_lines.append("SAFEST PLAYS")
                safe_overall = overall_scores[overall_scores["singles_score"].fillna(0) >= CONFIG["minimum_confidence"]].copy()
                for _, row in safe_overall.sort_values(["singles_score", "total_bases_score"], ascending=False).head(10).iterrows():
                    report_lines.append(f"- {row.get('player_name', '')} ({row.get('team', '')}) — safe {safe_float(row.get('singles_score', 0)):.2f}")
                    report_rows.append({"section": "safest_plays", "game": "Overall", "player": row.get("player_name", ""), "team": row.get("team", ""), "market": "safe", "score": safe_float(row.get("singles_score", 0)), "grade": grade(row.get("singles_score", 0)), "confidence_grade": grade(safe_float(row.get("singles_score", 0))), "reasons": "Strong safe profile", "risk_notes": "monitor lineup status"})

                report_lines.append("")
                report_lines.append("HIGHEST EV PLAYS")
                for _, row in overall_scores.sort_values("lotto_score", ascending=False).head(10).iterrows():
                    report_lines.append(f"- {row.get('player_name', '')} ({row.get('team', '')}) — ev {safe_float(row.get('lotto_score', 0)):.2f}")
                    report_rows.append({"section": "highest_ev", "game": "Overall", "player": row.get("player_name", ""), "team": row.get("team", ""), "market": "ev", "score": safe_float(row.get("lotto_score", 0)), "grade": grade(row.get("lotto_score", 0)), "confidence_grade": grade(safe_float(row.get("lotto_score", 0))), "reasons": "High upside profile", "risk_notes": "monitor lineup status"})

                report_lines.append("")
                report_lines.append("BEST UNDERDOGS")
                for _, row in overall_scores.sort_values("total_bases_score", ascending=False).head(10).iterrows():
                    report_lines.append(f"- {row.get('player_name', '')} ({row.get('team', '')}) — underdog proxy {safe_float(row.get('total_bases_score', 0)):.2f}")
                    report_rows.append({"section": "best_underdogs", "game": "Overall", "player": row.get("player_name", ""), "team": row.get("team", ""), "market": "underdog_proxy", "score": safe_float(row.get("total_bases_score", 0)), "grade": grade(row.get("total_bases_score", 0)), "confidence_grade": grade(safe_float(row.get("total_bases_score", 0))), "reasons": "High-value slate profile", "risk_notes": "monitor lineup status"})

    report_text = render_text_report(report_lines)
    text_output = EXPORT_DIR / CONFIG.get("text_output", "exports/daily_report.txt").split("/", 1)[-1]
    if isinstance(CONFIG.get("text_output"), str) and str(CONFIG["text_output"]).startswith("exports/"):
        text_output = EXPORT_DIR / str(CONFIG["text_output"]).split("/", 1)[-1]
    else:
        text_output = EXPORT_DIR / "daily_report.txt"
    write_text_output(text_output, report_text)

    pdf_output = EXPORT_DIR / "daily_report.pdf"
    if isinstance(CONFIG.get("pdf_output"), str) and str(CONFIG["pdf_output"]).startswith("exports/"):
        pdf_output = EXPORT_DIR / str(CONFIG["pdf_output"]).split("/", 1)[-1]
    else:
        pdf_output = EXPORT_DIR / "daily_report.pdf"
    write_pdf_output(pdf_output, report_text)

    daily_csv = EXPORT_DIR / "daily_report.csv"
    if isinstance(CONFIG.get("csv_exports", {}).get("daily_report"), str):
        daily_csv = EXPORT_DIR / str(CONFIG["csv_exports"]["daily_report"]).split("/", 1)[-1]
    write_exports(report_rows, daily_csv)

    singles_csv = EXPORT_DIR / "singles.csv"
    if isinstance(CONFIG.get("csv_exports", {}).get("singles"), str):
        singles_csv = EXPORT_DIR / str(CONFIG["csv_exports"]["singles"]).split("/", 1)[-1]
    write_exports(singles_rows, singles_csv)

    total_bases_csv = EXPORT_DIR / "total_bases.csv"
    if isinstance(CONFIG.get("csv_exports", {}).get("total_bases"), str):
        total_bases_csv = EXPORT_DIR / str(CONFIG["csv_exports"]["total_bases"]).split("/", 1)[-1]
    write_exports(total_bases_rows, total_bases_csv)

    command_csv = EXPORT_DIR / "command_center.csv"
    if isinstance(CONFIG.get("csv_exports", {}).get("command_center"), str):
        command_csv = EXPORT_DIR / str(CONFIG["csv_exports"]["command_center"]).split("/", 1)[-1]
    write_exports(command_rows, command_csv)

    print(report_text)
    print(f"Wrote {text_output}")
    print(f"Wrote {pdf_output}")
    print(f"Wrote {daily_csv}")
    print(f"Wrote {singles_csv}")
    print(f"Wrote {total_bases_csv}")
    print(f"Wrote {command_csv}")


if __name__ == "__main__":
    main()