# MLB-LAB Architecture

## Layer 1: Data

Sources:

- MLB-StatsAPI
- pybaseball
- baseballr

Purpose:

Collect:

- Schedule
- Lineups
- Pitchers
- Statcast
- Historical data

---

## Layer 2: Research

Purpose:

Transform data into information.

Questions:

- Who is vulnerable?
- Which pitches are weak?
- Which hitters match those weaknesses?
- What environments increase outcomes?

Output:

Research candidates.

---

## Layer 3: Intelligence

Purpose:

Score opportunities.

Framework:

Environment Score
Pitcher Score
Matchup Score
Recent Form Score
Statcast Score

Output:

Ranked opportunities.

---

## Layer 4: Decision Support

Purpose:

Generate reports.

Outputs:

- Daily slate report
- Top hitter report
- Top HR report
- Pitcher attack list
- Watchlist

---

Goal:

Convert baseball data into actionable intelligence.
