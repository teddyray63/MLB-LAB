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
                "implied_probability": row.get("implied_probability"),
                "clv": row.get("clv"),
                "park_adjusted_ev": row.get("park_adjusted_ev"),
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
                "implied_probability": row.get("implied_probability"),
                "clv": row.get("clv"),
                "park_adjusted_ev": row.get("park_adjusted_ev"),
            })

    games_payload = []
    for game in games or []:
        games_payload.append({
            "away": game.get("away_team", ""),
            "home": game.get("home_team", ""),
            "game_name": f"{game.get('away_team', '')} @ {game.get('home_team', '')}",
        })

    def _reason_pills(reasons: list) -> str:
        if not reasons:
            return '<span class="muted">—</span>'
        return " ".join(f'<span class="pill">{r}</span>' for r in reasons[:5])

    def _edge_cell(row: dict) -> str:
        edge = row.get("edge_score") or row.get("edge") or 0.0
        try:
            edge = float(edge)
        except (TypeError, ValueError):
            edge = 0.0
        if edge >= 8:
            cls, icon = "ev-strong", "▲"
        elif edge >= 3:
            cls, icon = "ev-pos", "+"
        elif edge > 0:
            cls, icon = "ev-fair", "~"
        elif edge < 0:
            cls, icon = "ev-neg", "▼"
        else:
            return '<span class="muted">—</span>'
        return f'<span class="{cls}">{icon}{abs(edge):.1f}</span>'

    def _conf_bar(confidence: float) -> str:
        pct = min(100, max(0, confidence))
        color = _color_for_confidence(confidence)
        return (
            f'<div class="conf-wrap">'
            f'<div class="conf-bar" style="width:{pct:.0f}%;background:{color}"></div>'
            f'<span class="conf-label" style="color:{color}">{confidence:.1f}%</span>'
            f'</div>'
        )

    def _optional_pct_cell(value: Any) -> str:
        """Render an optional probability/pct value, or '—' when missing/null."""
        if value is None:
            return '<span class="muted">—</span>'
        try:
            value = float(value)
        except (TypeError, ValueError):
            return '<span class="muted">—</span>'
        if pd.isna(value):
            return '<span class="muted">—</span>'
        return f'<span>{value * 100:.1f}%</span>' if abs(value) <= 1 else f'<span>{value:.1f}</span>'

    def _optional_signed_cell(value: Any) -> str:
        """Render an optional signed numeric value (CLV, park-adjusted EV), or '—' when missing/null."""
        if value is None:
            return '<span class="muted">—</span>'
        try:
            value = float(value)
        except (TypeError, ValueError):
            return '<span class="muted">—</span>'
        if pd.isna(value):
            return '<span class="muted">—</span>'
        cls = "ev-strong" if value > 0 else ("ev-neg" if value < 0 else "muted")
        sign = "+" if value > 0 else ""
        return f'<span class="{cls}">{sign}{value:.2f}</span>'

    def _kelly_cell(confidence: float, edge: float) -> str:
        # Conservative half-Kelly stake placeholder rendered by JS from bankroll input
        try:
            conf = float(confidence) / 100.0
            e = float(edge)
        except (TypeError, ValueError):
            return '<span class="muted">—</span>'
        if e <= 0 or conf <= 0:
            return '<span class="muted">—</span>'
        # Kelly fraction = edge / odds_decimal; use edge as pct / 100 approximation
        kelly = round(conf * (e / 100.0) * 0.5, 4)  # half-Kelly
        return f'<span class="kelly" data-kelly="{kelly}">{kelly*100:.1f}%</span>'

    cards_rows = ''.join(
        f'<tr><td>{card["name"]}</td><td>{card["leg_count"]}</td>'
        f'<td>{_conf_bar(card["confidence"])}</td>'
        f'<td><span class="risk-{card["risk"]}">{card["risk"]}</span></td>'
        f'<td><strong>{_grade_badge(card["grade"])}</strong></td></tr>'
        for card in cards_payload
    )
    bet_row_idx = [0]

    def _betting_row(row: dict) -> str:
        i = bet_row_idx[0]
        bet_row_idx[0] += 1
        reasons_html = _reason_pills(row["reasons"])
        edge = row.get("edge_score") or row.get("edge") or 0.0
        return (
            f'<tr class="bet-row" onclick="toggleReasons(\'r{i}\')">'
            f'<td><strong>{row["player"]}</strong><div class="summary">{row.get("team","")}</div></td>'
            f'<td>{row["game"]}</td>'
            f'<td><span class="pill pill-mkt">{row["market"]}</span></td>'
            f'<td>{_conf_bar(row["confidence"])}</td>'
            f'<td>{_edge_cell(row)}</td>'
            f'<td>{_kelly_cell(row["confidence"], edge)}</td>'
            f'<td>{_optional_pct_cell(row.get("implied_probability"))}</td>'
            f'<td>{_optional_signed_cell(row.get("clv"))}</td>'
            f'<td>{_optional_signed_cell(row.get("park_adjusted_ev"))}</td>'
            f'<td><span class="risk-{row["risk"]}">{row["risk"]}</span></td>'
            f'<td><strong>{_grade_badge(row["grade"])}</strong></td>'
            f'</tr>'
            f'<tr id="r{i}" class="reasons-row hidden"><td colspan="11">'
            f'<div class="reasons-expand">{reasons_html}</div>'
            f'</td></tr>'
        )

    betting_rows = ''.join(_betting_row(row) for row in betting_payload)

    lotto_row_idx = [0]

    def _lotto_row(row: dict) -> str:
        i = lotto_row_idx[0]
        lotto_row_idx[0] += 1
        reasons_html = _reason_pills(row["reasons"])
        return (
            f'<tr class="bet-row" onclick="toggleReasons(\'lr{i}\')">'
            f'<td><strong>{row["player"]}</strong></td>'
            f'<td>{row["team"]}</td>'
            f'<td><span class="pill pill-mkt">{row["market"]}</span></td>'
            f'<td>{_conf_bar(row["confidence"])}</td>'
            f'<td>{_optional_pct_cell(row.get("implied_probability"))}</td>'
            f'<td>{_optional_signed_cell(row.get("clv"))}</td>'
            f'<td>{_optional_signed_cell(row.get("park_adjusted_ev"))}</td>'
            f'<td><span class="risk-{row["risk"]}">{row["risk"]}</span></td>'
            f'<td><strong>{_grade_badge(row["grade"])}</strong></td>'
            f'</tr>'
            f'<tr id="lr{i}" class="reasons-row hidden"><td colspan="9">'
            f'<div class="reasons-expand">{reasons_html}</div>'
            f'</td></tr>'
        )

    lotto_rows = ''.join(_lotto_row(row) for row in lotto_payload)
    games_rows = ''.join(f'<div class="card"><strong>{game["game_name"]}</strong><div class="summary">{game["away"]} vs {game["home"]}</div></div>' for game in games_payload)

    return f"""
<!DOCTYPE html>
<html lang=\"en\" data-theme=\"dark\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>MLB-LAB Daily Dashboard</title>
  <style>
    :root {{ color-scheme:dark; --bg:#07111f; --card:#101b2d; --text:#f5f7fb; --muted:#94a3b8; --accent:#4fd1c5; --border:rgba(255,255,255,0.08); }}
    html[data-theme='light'] {{ color-scheme:light; --bg:#f8fafc; --card:#ffffff; --text:#0f172a; --muted:#475569; --accent:#2563eb; --border:rgba(15,23,42,0.1); }}
    body {{ margin:0; font-family:Inter,system-ui,Arial,sans-serif; background:var(--bg); color:var(--text); font-size:14px; }}
    .page {{ max-width:1500px; margin:0 auto; padding:20px 16px; }}
    .header {{ display:flex; justify-content:space-between; align-items:center; gap:16px; margin-bottom:16px; flex-wrap:wrap; }}
    .controls {{ display:flex; gap:8px; flex-wrap:wrap; align-items:center; }}
    .card {{ background:var(--card); border:1px solid var(--border); border-radius:14px; padding:16px; box-shadow:0 8px 24px rgba(0,0,0,0.18); }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:14px; margin-bottom:16px; }}
    input,select,button {{ border-radius:8px; border:1px solid var(--border); padding:8px 11px; background:rgba(255,255,255,0.05); color:var(--text); font-size:13px; }}
    input:focus,select:focus {{ outline:none; border-color:var(--accent); }}
    button {{ cursor:pointer; transition:opacity 0.15s; }} button:hover {{ opacity:0.8; }}
    h2, h3 {{ letter-spacing:0.01em; }}
    table {{ width:100%; border-collapse:collapse; margin-top:6px; }}
    th,td {{ padding:9px 7px; border-bottom:1px solid var(--border); text-align:left; vertical-align:middle; }}
    th {{ cursor:pointer; color:var(--muted); font-size:11px; text-transform:uppercase; letter-spacing:0.07em; user-select:none;
      position:sticky; top:0; background:var(--card); z-index:2; box-shadow:0 1px 0 var(--border); }}
    th:hover {{ color:var(--accent); }}
    .table-scroll {{ max-height:560px; overflow-y:auto; }}
    tr.bet-row {{ cursor:pointer; }} tr.bet-row:hover {{ background:rgba(255,255,255,0.03); }}
    .muted {{ color:var(--muted); }}
    .summary {{ font-size:11px; color:var(--muted); }}
    .toolbar {{ display:flex; justify-content:space-between; align-items:center; gap:10px; flex-wrap:wrap; margin-bottom:10px; }}
    .hidden {{ display:none !important; }}
    .pill {{ display:inline-block; background:rgba(79,209,197,0.1); color:var(--accent); border-radius:6px; padding:2px 7px; font-size:11px; margin:1px; white-space:nowrap; }}
    .pill-mkt {{ background:rgba(99,179,237,0.1); color:#63b3ed; }}
    .reasons-expand {{ padding:8px 4px; display:flex; flex-wrap:wrap; gap:4px; }}
    .reasons-row td {{ background:rgba(255,255,255,0.02); }}
    .risk-low {{ color:#2ecc71; font-weight:600; }} .risk-medium {{ color:#f1c40f; font-weight:600; }} .risk-high {{ color:#e74c3c; font-weight:600; }}
    .ev-strong {{ color:#2ecc71; font-weight:700; }} .ev-pos {{ color:#82e0aa; }} .ev-fair {{ color:#f7dc6f; }} .ev-neg {{ color:#e74c3c; }}
    .kelly {{ font-family:monospace; font-size:12px; color:var(--accent); }}
    .conf-wrap {{ display:flex; align-items:center; gap:6px; min-width:100px; }}
    .conf-bar {{ height:6px; border-radius:3px; flex-shrink:0; }}
    .conf-label {{ font-size:12px; font-weight:600; white-space:nowrap; }}
    .bankroll-bar {{ display:flex; align-items:center; gap:8px; padding:8px 12px; background:rgba(255,255,255,0.03); border-radius:10px; border:1px solid var(--border); }}
    .bankroll-bar label {{ font-size:12px; color:var(--muted); white-space:nowrap; }}
    .bankroll-bar input {{ width:90px; }}
    @media(max-width:700px) {{ .header {{ flex-direction:column; align-items:flex-start; }} .grid {{ grid-template-columns:1fr; }} th,td {{ padding:6px 4px; font-size:12px; }} }}
  </style>
</head>
<body>
  <div class=\"page\">
    <div class=\"header\">
      <div>
        <h1 style=\"margin:0;font-size:1.4rem\">MLB-LAB Daily Dashboard</h1>
        <div class=\"muted\" style=\"font-size:12px\">Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
      </div>
      <div class=\"controls\">
        <div class=\"bankroll-bar\">
          <label>Bankroll $</label>
          <input id=\"bankrollInput\" type=\"number\" value=\"1000\" min=\"0\" step=\"100\" oninput=\"updateKellyStakes()\" />
        </div>
        <button onclick=\"toggleTheme()\">🌓 Theme</button>
        <button onclick=\"window.print()\">🖨 Print</button>
        <button onclick=\"exportTable('cards')\">⬇ Cards</button>
        <button onclick=\"exportTable('betting')\">⬇ Plays</button>
      </div>
    </div>

    <div class=\"card\" style=\"margin-bottom:14px;\">
      <div class=\"toolbar\">
        <h2 style=\"margin:0;font-size:1rem\">Today's Games ({len(games_payload)} scheduled)</h2>
        <div class=\"controls\">
          <input id=\"searchInput\" placeholder=\"Search player / market…\" style=\"width:200px\" />
          <select id=\"marketFilter\">
            <option value=\"\">All markets</option>
            <option value=\"singles\">Singles</option>
            <option value=\"total_bases\">Total Bases</option>
            <option value=\"runs\">Runs</option>
            <option value=\"rbis\">RBI</option>
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
        <h3 style=\"margin-top:0;font-size:0.95rem\">Betting Cards</h3>
        <table id=\"cardsTable\">
          <thead><tr>
            <th onclick=\"sortTable('cardsTable',0)\">Card</th>
            <th onclick=\"sortTable('cardsTable',1)\">Legs</th>
            <th onclick=\"sortTable('cardsTable',2)\">Confidence</th>
            <th onclick=\"sortTable('cardsTable',3)\">Risk</th>
            <th onclick=\"sortTable('cardsTable',4)\">Grade</th>
          </tr></thead>
          <tbody>{cards_rows}</tbody>
        </table>
      </div>
      <div class=\"card\" style=\"overflow-x:auto\">
        <h3 style=\"margin-top:0;font-size:0.95rem\">Player Recommendations <span class=\"muted\" style=\"font-weight:normal;font-size:11px\">(click row to expand reasons)</span></h3>
        <div class=\"table-scroll\">
        <table id=\"bettingTable\">
          <thead><tr>
            <th onclick=\"sortTable('bettingTable',0)\">Player</th>
            <th onclick=\"sortTable('bettingTable',1)\">Game</th>
            <th onclick=\"sortTable('bettingTable',2)\">Market</th>
            <th onclick=\"sortTable('bettingTable',3)\">Confidence</th>
            <th onclick=\"sortTable('bettingTable',4)\">Edge</th>
            <th onclick=\"sortTable('bettingTable',5)\">Kelly Stake</th>
            <th onclick=\"sortTable('bettingTable',6)\">Implied %</th>
            <th onclick=\"sortTable('bettingTable',7)\">CLV</th>
            <th onclick=\"sortTable('bettingTable',8)\">Park EV</th>
            <th onclick=\"sortTable('bettingTable',9)\">Risk</th>
            <th onclick=\"sortTable('bettingTable',10)\">Grade</th>
          </tr></thead>
          <tbody>{betting_rows}</tbody>
        </table>
        </div>
      </div>
    </div>

    <div class=\"card\" style=\"overflow-x:auto\">
      <h3 style=\"margin-top:0;font-size:0.95rem\">Lotto / Best 6-Leg <span class=\"muted\" style=\"font-weight:normal;font-size:11px\">(click row to expand reasons)</span></h3>
      <div class=\"table-scroll\">
      <table id=\"lottoTable\">
        <thead><tr>
          <th onclick=\"sortTable('lottoTable',0)\">Player</th>
          <th onclick=\"sortTable('lottoTable',1)\">Team</th>
          <th onclick=\"sortTable('lottoTable',2)\">Market</th>
          <th onclick=\"sortTable('lottoTable',3)\">Confidence</th>
          <th onclick=\"sortTable('lottoTable',4)\">Implied %</th>
          <th onclick=\"sortTable('lottoTable',5)\">CLV</th>
          <th onclick=\"sortTable('lottoTable',6)\">Park EV</th>
          <th onclick=\"sortTable('lottoTable',7)\">Risk</th>
          <th onclick=\"sortTable('lottoTable',8)\">Grade</th>
        </tr></thead>
        <tbody>{lotto_rows}</tbody>
      </table>
      </div>
    </div>
  </div>

  <script>
    function filterRows() {{
      const q = document.getElementById('searchInput').value.toLowerCase();
      const market = document.getElementById('marketFilter').value;
      const risk = document.getElementById('riskFilter').value;
      ['bettingTable','cardsTable','lottoTable'].forEach(id => {{
        const tbl = document.getElementById(id);
        if (!tbl) return;
        Array.from(tbl.querySelectorAll('tbody tr')).forEach(row => {{
          if (row.classList.contains('reasons-row')) return;
          const text = row.textContent.toLowerCase();
          const vis = (!q || text.includes(q)) && (!market || text.includes(market)) && (!risk || text.includes(risk));
          row.classList.toggle('hidden', !vis);
          const next = row.nextElementSibling;
          if (next && next.classList.contains('reasons-row')) next.classList.toggle('hidden', !vis);
        }});
      }});
    }}

    document.getElementById('searchInput').addEventListener('input', filterRows);
    document.getElementById('marketFilter').addEventListener('change', filterRows);
    document.getElementById('riskFilter').addEventListener('change', filterRows);

    function toggleReasons(id) {{
      const el = document.getElementById(id);
      if (el) el.classList.toggle('hidden');
    }}

    function toggleTheme() {{
      const cur = document.documentElement.getAttribute('data-theme');
      document.documentElement.setAttribute('data-theme', cur === 'dark' ? 'light' : 'dark');
    }}

    function updateKellyStakes() {{
      const br = parseFloat(document.getElementById('bankrollInput').value) || 0;
      document.querySelectorAll('.kelly').forEach(el => {{
        const k = parseFloat(el.dataset.kelly) || 0;
        const stake = (k * br).toFixed(2);
        el.textContent = k > 0 && br > 0 ? '$' + stake + ' (' + (k*100).toFixed(1) + '%)' : '—';
      }});
    }}

    function sortTable(tableId, colIdx) {{
      const table = document.getElementById(tableId);
      if (!table) return;
      const rows = Array.from(table.querySelectorAll('tbody tr')).filter(r => !r.classList.contains('reasons-row'));
      const dir = table.dataset.sortDir === 'asc' ? -1 : 1;
      table.dataset.sortDir = dir === 1 ? 'asc' : 'desc';
      rows.sort((a, b) => {{
        const av = (a.children[colIdx] || {{}}).innerText?.trim() || '';
        const bv = (b.children[colIdx] || {{}}).innerText?.trim() || '';
        const an = parseFloat(av.replace(/[^0-9.\-]/g,'')), bn = parseFloat(bv.replace(/[^0-9.\-]/g,''));
        return isNaN(an) || isNaN(bn) ? dir * av.localeCompare(bv) : dir * (an - bn);
      }});
      const tbody = table.querySelector('tbody');
      const ordered = [];
      rows.forEach(r => {{
        ordered.push(r);
        const next = r.nextElementSibling;
        if (next && next.classList.contains('reasons-row')) ordered.push(next);
      }});
      Array.from(tbody.querySelectorAll('tr')).forEach(r => tbody.removeChild(r));
      ordered.forEach(r => tbody.appendChild(r));
    }}

    function exportTable(type) {{
      const id = type === 'cards' ? 'cardsTable' : 'bettingTable';
      const rows = Array.from(document.querySelectorAll('#' + id + ' tbody tr'))
        .filter(r => !r.classList.contains('reasons-row') && !r.classList.contains('hidden'))
        .map(r => r.innerText.replace(/\n/g, ' | '));
      const blob = new Blob([rows.join('\n')], {{type:'text/plain;charset=utf-8'}});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url; a.download = 'mlb_' + type + '_export.txt'; a.click();
      URL.revokeObjectURL(url);
    }}

    updateKellyStakes();
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
