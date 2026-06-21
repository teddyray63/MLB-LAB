from datetime import date
from pathlib import Path
import json, urllib.request

TODAY = date.today().isoformat()
SEASON = date.today().year
REPORT = Path("reports/mlb-lab-v3-game-dissection-report.md")

PARK = {"Coors Field":20,"Sutter Health Park":16,"Yankee Stadium":15,"Citizens Bank Park":15,
"Truist Park":14,"Globe Life Field":14,"Chase Field":13,"Comerica Park":11,"Wrigley Field":10,
"T-Mobile Park":10,"Daikin Park":10,"Tropicana Field":10,"loanDepot park":10,"Kauffman Stadium":8}

def j(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.loads(r.read().decode())

def n(x):
    try: return float(x)
    except: return 0

def s(x): return "—" if x in [None,"","null"] else x

def get_pitcher(team):
    p = team.get("probablePitcher")
    if not p: return {"id":None,"name":"TBD","hand":"—"}
    return {"id":p.get("id"),"name":p.get("fullName","TBD"),"hand":p.get("pitchHand",{}).get("code","—")}

def pitcher_stats(pid):
    if not pid: return {}
    try:
        u=f"https://statsapi.mlb.com/api/v1/people/{pid}?hydrate=stats(group=[pitching],type=[season,gameLog],season={SEASON})"
        d=j(u)["people"][0]["stats"]
        season=d[0]["splits"][0]["stat"] if d and d[0].get("splits") else {}
        logs=d[1]["splits"][:5] if len(d)>1 and d[1].get("splits") else []
        return {"season":season,"logs":logs}
    except: return {"season":{},"logs":[]}

def team_hitting(tid):
    try:
        u=f"https://statsapi.mlb.com/api/v1/teams/{tid}/stats?stats=season&group=hitting&season={SEASON}"
        return j(u)["stats"][0]["splits"][0]["stat"]
    except: return {}

def team_pitching(tid):
    try:
        u=f"https://statsapi.mlb.com/api/v1/teams/{tid}/stats?stats=season&group=pitching&season={SEASON}"
        return j(u)["stats"][0]["splits"][0]["stat"]
    except: return {}

def pitcher_risk(st):
    era,whip,hr9,bb9,k9 = map(n,[st.get("era"),st.get("whip"),st.get("homeRunsPer9"),st.get("walksPer9Inn"),st.get("strikeoutsPer9Inn")])
    score=8
    if era>=5: score+=6
    elif era>=4.25: score+=4
    elif era>=3.75: score+=2
    if whip>=1.45: score+=5
    elif whip>=1.30: score+=3
    elif whip>=1.20: score+=1
    if hr9>=1.6: score+=5
    elif hr9>=1.2: score+=3
    elif hr9>=.9: score+=1
    if bb9>=3.8: score+=3
    elif bb9>=3.0: score+=2
    if k9 and k9<6.5: score+=3
    elif k9 and k9<8: score+=1
    return min(score,25)

def offense_score(st):
    ops,avg,hr,runs = map(n,[st.get("ops"),st.get("avg"),st.get("homeRuns"),st.get("runs")])
    score=8
    if ops>=.780: score+=6
    elif ops>=.730: score+=4
    elif ops>=.700: score+=2
    if avg>=.260: score+=3
    elif avg>=.245: score+=2
    if hr>=100: score+=3
    elif hr>=80: score+=2
    if runs>=400: score+=3
    elif runs>=350: score+=2
    return min(score,20)

def bullpen_score(st):
    era,whip,hr9 = map(n,[st.get("era"),st.get("whip"),st.get("homeRunsPer9")])
    score=8
    if era>=4.75: score+=5
    elif era>=4.25: score+=3
    if whip>=1.40: score+=4
    elif whip>=1.30: score+=2
    if hr9>=1.4: score+=3
    elif hr9>=1.1: score+=2
    return min(score,15)

def tier(x):
    return "Priority" if x>=75 else "Watch" if x>=60 else "Low" if x>=45 else "Ignore"

def ptable(label,p,ps,risk):
    st=ps.get("season",{})
    logs=ps.get("logs",[])
    out=f"""
### {label}: {p['name']} ({p['hand']})

| Stat | Value |
|---|---:|
| ERA | {s(st.get('era'))} |
| WHIP | {s(st.get('whip'))} |
| K/9 | {s(st.get('strikeoutsPer9Inn'))} |
| BB/9 | {s(st.get('walksPer9Inn'))} |
| HR/9 | {s(st.get('homeRunsPer9'))} |
| IP | {s(st.get('inningsPitched'))} |
| H | {s(st.get('hits'))} |
| R | {s(st.get('runs'))} |
| HR | {s(st.get('homeRuns'))} |
| Risk Score | {risk} |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
"""
    if not logs:
        out+="| — | — | — | — | — | — | — | — |\n"
    for g in logs:
        stat=g.get("stat",{})
        opp=g.get("opponent",{}).get("name","—")
        out+=f"| {g.get('date','—')} | {opp} | {s(stat.get('inningsPitched'))} | {s(stat.get('hits'))} | {s(stat.get('earnedRuns'))} | {s(stat.get('baseOnBalls'))} | {s(stat.get('strikeOuts'))} | {s(stat.get('homeRuns'))} |\n"
    return out

def main():
    data=j(f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={TODAY}&hydrate=probablePitcher,venue,team")
    games=[]

    for d in data.get("dates",[]):
        for g in d.get("games",[]):
            away=g["teams"]["away"]["team"]; home=g["teams"]["home"]["team"]
            ap=get_pitcher(g["teams"]["away"]); hp=get_pitcher(g["teams"]["home"])
            aps=pitcher_stats(ap["id"]); hps=pitcher_stats(hp["id"])
            ah=team_hitting(away["id"]); hh=team_hitting(home["id"])
            abp=team_pitching(away["id"]); hbp=team_pitching(home["id"])

            ar=pitcher_risk(aps.get("season",{})); hr=pitcher_risk(hps.get("season",{}))
            env=PARK.get(g["venue"]["name"],10)
            off=max(offense_score(ah),offense_score(hh))
            pen=max(bullpen_score(abp),bullpen_score(hbp))
            matchup=20 if max(ar,hr)>=20 and off>=15 else 16 if max(ar,hr)>=16 else 12
            total=env+max(ar,hr)+off+pen+matchup

            games.append(dict(game=f"{away['name']} @ {home['name']}",away=away,home=home,park=g["venue"]["name"],
            time=g.get("gameDate","—"),ap=ap,hp=hp,aps=aps,hps=hps,ah=ah,hh=hh,abp=abp,hbp=hbp,
            ar=ar,hr=hr,env=env,off=off,pen=pen,matchup=matchup,total=total,tier=tier(total)))

    games.sort(key=lambda x:x["total"], reverse=True)

    r=f"""# MLB-LAB V3 Game Dissection Report

Date: {TODAY}

Status: Complete.

Mode: full-slate game dissection engine.

No hard eliminations. Every game receives a card.

---

## Slate Index

| Rank | Game | Park | SP Matchup | Env | Pitcher | Offense | Bullpen | Matchup | Total | Tier |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
"""
    for i,g in enumerate(games,1):
        r+=f"| {i} | {g['game']} | {g['park']} | {g['ap']['name']} vs {g['hp']['name']} | {g['env']} | {max(g['ar'],g['hr'])} | {g['off']} | {g['pen']} | {g['matchup']} | {g['total']} | {g['tier']} |\n"

    r+="\n---\n\n# Full Game Cards\n"

    for i,g in enumerate(games,1):
        attack="Home bats vs away SP" if g["ar"]>=g["hr"] else "Away bats vs home SP"
        concern=g["ap"]["name"] if g["ar"]>=g["hr"] else g["hp"]["name"]

        r+=f"""

---

## {i}. {g['game']} — {g['tier']} ({g['total']})

### Game Context

| Field | Value |
|---|---|
| Park | {g['park']} |
| Time | {g['time']} |
| Environment | {g['env']} |
| Pitcher Risk | {max(g['ar'],g['hr'])} |
| Offense | {g['off']} |
| Bullpen | {g['pen']} |
| Matchup Pressure | {g['matchup']} |
| Total | {g['total']} |

{ptable("Away SP",g["ap"],g["aps"],g["ar"])}

{ptable("Home SP",g["hp"],g["hps"],g["hr"])}

### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| {g['away']['name']} | {s(g['ah'].get('avg'))} | {s(g['ah'].get('ops'))} | {s(g['ah'].get('runs'))} | {s(g['ah'].get('homeRuns'))} | {offense_score(g['ah'])} |
| {g['home']['name']} | {s(g['hh'].get('avg'))} | {s(g['hh'].get('ops'))} | {s(g['hh'].get('runs'))} | {s(g['hh'].get('homeRuns'))} | {offense_score(g['hh'])} |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| {g['away']['name']} | {s(g['abp'].get('era'))} | {s(g['abp'].get('whip'))} | {s(g['abp'].get('homeRunsPer9'))} | {bullpen_score(g['abp'])} |
| {g['home']['name']} | {s(g['hbp'].get('era'))} | {s(g['hbp'].get('whip'))} | {s(g['hbp'].get('homeRunsPer9'))} | {bullpen_score(g['hbp'])} |

### Dissection Read

- First attack side: {attack}
- Main pitcher concern: {concern}
- Park/environment pressure: {g['env']}
- Offense pressure: {g['off']}
- Bullpen/staff pressure: {g['pen']}
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.
"""

    r+="""


---

# V3 Complete

This runner now creates:

- Full slate index
- Every-game breakdown cards
- Starting pitcher risk
- Recent pitcher form
- Team offense
- Bullpen/staff context
- Attack-side read
- No CSVs
- No website scraping dependency
"""

    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text(r, encoding="utf-8")
    print(f"Updated {REPORT}")

if __name__=="__main__":
    main()
