import json
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
EXPORT_DIR = ROOT / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def _color_for_confidence(confidence: float) -> str:
    if confidence >= 80:
        return "#2ecc71"
    if confidence >= 60:
        return "#f1c40f"
    if confidence >= 40:
        return "#e67e22"
    return "#e74c3c"


def _grade_badge(grade: str) -> str:
    return grade or "PASS"


def build_dashboard_html(cards_df: pd.DataFrame, betting_df: pd.DataFrame, lotto_df: pd.DataFrame, games: List[Dict[str, Any]] | None = None) -> str:
    cards_payload = []
    if not cards_df.empty:
        for _, row in cards_df.iterrows():
            cards_payload.append({
                "card_name": row.get("card_name", ""),
                "name": row.get("name", ""),
                "leg_count": int(row.get("leg_count", 0) or 0),
                "confidence": float(row.get("confidence", 0.0) or 0.0),
                "risk": row.get("risk", "high"),
                "grade": row.get("grade", "PASS"),
                "legs": json.loads(row.get("legs", "[]")) if isinstance(row.get("legs", "[]"), str) else row.get("legs", []),
            })

    betting_payload = []
    if not betting_df.empty:
        for _, row in betting_df.iterrows():
            betting_payload.append({
                "card_name": row.get("card_name", ""),
                "player": row.get("player", ""),
                "team": row.get("team", ""),
                "game": row.get("game", ""),
                "market": row.get("market", ""),
                "score": float(row.get("score", 0.0) or 0.0),
                "grade": row.get("grade", "PASS"),
                "confidence": float(row.get("confidence", 0.0) or 0.0),
                "risk": row.get("risk", "high"),
                "reasons": json.loads(row.get("reasons", "[]")) if isinstance(row.get("reasons", "[]"), str) else row.get("reasons", []),
            })

    lotto_payload = []
    if not lotto_df.empty:
        for _, row in lotto_df.iterrows():
            lotto_payload.append({
                "card_name": row.get("card_name", ""),
                "player": row.get("player", ""),
                "team": row.get("team", ""),
                "game": row.get("game", ""),
                "market": row.get("market", ""),
                "score": float(row.get("score", 0.0) or 0.0),
                "grade": row.get("grade", "PASS"),
                "confidence": float(row.get("confidence", 0.0) or 0.0),
                "risk": row.get("risk", "high"),
                "reasons": json.loads(row.get("reasons", "[]")) if isinstance(row.get("reasons", "[]"), str) else row.get("reasons", []),
            })

    games_payload = []
    for game in games or []:
        games_payload.append({
            "away": game.get("away_team", ""),
            "home": game.get("home_team", ""),
            "game_name": f"{game.get('away_team', '')} @ {game.get('home_team', '')}",
        })

    cards_rows = ''.join(f'<tr><td>{card["name"]}</td><td>{card["leg_count"]}</td><td style="color:{_color_for_confidence(card["confidence"])}">{card["confidence"]:.1f}%</td><td>{card["risk"]}</td><td>{_grade_badge(card["grade"])}</td></tr>' for card in cards_payload)
    betting_rows = ''.join(f'<tr><td>{row["player"]}</td><td>{row["market"]}</td><td style="color:{_color_for_confidence(row["confidence"])}">{row["confidence"]:.1f}%</td><td>{_grade_badge(row["grade"])}</td></tr>' for row in betting_payload)
    lotto_rows = ''.join(f'<tr><td>{row["player"]}</td><td>{row["team"]}</td><td>{row["market"]}</td><td style="color:{_color_for_confidence(row["confidence"])}">{row["confidence"]:.1f}%</td><td>{row["risk"]}</td><td>{_grade_badge(row["grade"])}</td></tr>' for row in lotto_payload)
    games_rows = ''.join(f'<div class="card"><strong>{game["game_name"]}</strong><div class="summary">{game["away"]} vs {game["home"]}</div></div>' for game in games_payload)

    return f"""
<!DOCTYPE html>
<html lang=\"en\" data-theme=\"dark\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>MLB-LAB Daily Dashboard</title>
  <style>
    :root {{ color-scheme: dark; --bg:#07111f; --card:#101b2d; --text:#f5f7fb; --muted:#94a3b8; --accent:#4fd1c5; --border:rgba(255,255,255,0.08); }}
    html[data-theme='light'] {{ color-scheme: light; --bg:#f8fafc; --card:#ffffff; --text:#0f172a; --muted:#475569; --accent:#2563eb; --border:rgba(15,23,42,0.1); }}
    body {{ margin:0; font-family: Inter, system-ui, Arial, sans-serif; background:var(--bg); color:var(--text); }}
    .page {{ max-width: 1400px; margin: 0 auto; padding: 24px; }}
    .header {{ display:flex; justify-content:space-between; align-items:center; gap:16px; margin-bottom:18px; }}
    .controls {{ display:flex; gap:10px; flex-wrap:wrap; }}
    .card {{ background:var(--card); border:1px solid var(--border); border-radius:14px; padding:16px; box-shadow:0 10px 30px rgba(0,0,0,0.16); }}
    .grid {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-bottom:18px; }}
    input, select, button {{ border-radius:10px; border:1px solid var(--border); padding:10px 12px; background:rgba(255,255,255,0.04); color:var(--text); }}
    button {{ cursor:pointer; }}
    table {{ width:100%; border-collapse:collapse; margin-top:8px; }}
    th, td {{ padding:10px 8px; border-bottom:1px solid var(--border); text-align:left; }}
    th {{ cursor:pointer; color:var(--muted); font-size:12px; text-transform:uppercase; letter-spacing:0.08em; }}
    .muted {{ color:var(--muted); }}
    .summary {{ font-size:12px; color:var(--muted); }}
    .toolbar {{ display:flex; justify-content:space-between; align-items:center; gap:10px; flex-wrap:wrap; margin-bottom:10px; }}
    .hidden {{ display:none; }}
  </style>
</head>
<body>
  <div class=\"page\">
    <div class=\"header\">
      <div>
        <h1 style=\"margin:0\">MLB-LAB Daily Dashboard</h1>
        <div class=\"muted\">Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
      </div>
      <div class=\"controls\">
        <button onclick=\"toggleTheme()\">Toggle Theme</button>
        <button onclick=\"window.print()\">Print</button>
        <button onclick=\"exportTable('cards')\">Export Cards</button>
        <button onclick=\"exportTable('betting')\">Export Betting</button>
      </div>
    </div>

    <div class=\"card\" style=\"margin-bottom:16px;\">
      <div class=\"toolbar\">
        <h2 style=\"margin:0\">Today's Games</h2>
        <div class=\"controls\">
          <input id=\"searchInput\" placeholder=\"Search player or market\" />
          <select id=\"marketFilter\">
            <option value=\"\">All markets</option>
            <option value=\"singles\">Singles</option>
            <option value=\"total_bases\">Total Bases</option>
            <option value=\"runs\">Runs</option>
            <option value=\"rbi\">RBI</option>
            <option value=\"lotto\">Lotto</option>
          </select>
          <select id=\"riskFilter\">
            <option value=\"\">All risk</option>
            <option value=\"low\">Low</option>
            <option value=\"medium\">Medium</option>
            <option value=\"high\">High</option>
          </select>
        </div>
      </div>
      <div class=\"grid\">{games_rows}</div>
    </div>

    <div class=\"grid\">
      <div class=\"card\">
        <h3 style=\"margin-top:0\">Cards</h3>
        <table id=\"cardsTable\">
          <thead><tr><th>Card</th><th>Legs</th><th>Confidence</th><th>Risk</th><th>Grade</th></tr></thead>
          <tbody>{cards_rows}</tbody>
        </table>
      </div>
      <div class=\"card\">
        <h3 style=\"margin-top:0\">Player Search</h3>
        <table id=\"bettingTable\">
          <thead><tr><th>Player</th><th>Market</th><th>Confidence</th><th>Grade</th></tr></thead>
          <tbody>{betting_rows}</tbody>
        </table>
      </div>
    </div>

    <div class=\"card\">
      <h3 style=\"margin-top:0\">Lotto / Best 6-Leg</h3>
      <table id=\"lottoTable\">
        <thead><tr><th>Player</th><th>Team</th><th>Market</th><th>Confidence</th><th>Risk</th><th>Grade</th></tr></thead>
        <tbody>{lotto_rows}</tbody>
      </table>
    </div>
  </div>

  <script>
    const searchInput = document.getElementById('searchInput');
    const marketFilter = document.getElementById('marketFilter');
    const riskFilter = document.getElementById('riskFilter');
    const bettingRows = Array.from(document.querySelectorAll('#bettingTable tbody tr'));
    const cardsRows = Array.from(document.querySelectorAll('#cardsTable tbody tr'));
    const lottoRows = Array.from(document.querySelectorAll('#lottoTable tbody tr'));

    function filterRows() {{
      const q = searchInput.value.toLowerCase();
      const market = marketFilter.value;
      const risk = riskFilter.value;
      const apply = (rows) => {{
        rows.forEach((row) => {{
          const text = row.textContent.toLowerCase();
          const visible = text.includes(q) && (!market || text.includes(market)) && (!risk || text.includes(risk));
          row.classList.toggle('hidden', !visible);
        }});
      }};
      apply(bettingRows);
      apply(cardsRows);
      apply(lottoRows);
    }}

    searchInput.addEventListener('input', filterRows);
    marketFilter.addEventListener('change', filterRows);
    riskFilter.addEventListener('change', filterRows);

    function toggleTheme() {{
      const current = document.documentElement.getAttribute('data-theme');
      document.documentElement.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark');
    }}

    function exportTable(type) {{
      let rows = [];
      if (type === 'cards') rows = Array.from(document.querySelectorAll('#cardsTable tbody tr')).map((row) => row.innerText.replace(/\n/g, ' | '));
      if (type === 'betting') rows = Array.from(document.querySelectorAll('#bettingTable tbody tr')).map((row) => row.innerText.replace(/\n/g, ' | '));
      const blob = new Blob([rows.join('\n')], {{ type: 'text/plain;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `mlb_${type}_export.txt`;
      a.click();
      URL.revokeObjectURL(url);
    }}

    document.querySelectorAll('th').forEach((th) => {{
      th.addEventListener('click', () => {{
        const table = th.closest('table');
        const rows = Array.from(table.querySelectorAll('tbody tr'));
        const index = Array.from(th.parentNode.children).indexOf(th);
        const sorted = rows.sort((a, b) => {{
          const av = a.children[index].innerText.trim();
          const bv = b.children[index].innerText.trim();
          return av.localeCompare(bv);
        }});
        const tbody = table.querySelector('tbody');
        tbody.innerHTML = '';
        sorted.forEach((row) => tbody.appendChild(row));
      }});
    }});
  </script>
</body>
</html>
"""


def write_html_report(path: Path, lines: List[str]) -> Path:
    html = "<html><body><pre>" + "\n".join(lines) + "</pre></body></html>"
    path.write_text(html, encoding="utf-8")
    return path


def save_dashboard(cards_df: pd.DataFrame, betting_df: pd.DataFrame, lotto_df: pd.DataFrame, games: List[Dict[str, Any]] | None = None, output_path: str | None = None) -> Path:
    html_path = Path(output_path or EXPORT_DIR / "daily_dashboard.html")
    html_path.write_text(build_dashboard_html(cards_df, betting_df, lotto_df, games), encoding="utf-8")
    return html_path


def open_dashboard(path: Path | None = None) -> Path:
    target = path or (EXPORT_DIR / "daily_dashboard.html")
    if target.exists():
        webbrowser.open(target.resolve().as_uri())
    return target
