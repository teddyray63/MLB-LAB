# MLB-LAB V1 Run 001

Status: Layer 1 Complete

Date: 2026-06-21

## Objective

Run first complete MLB-LAB workflow on today's MLB slate.

---

## Layer 1 — Data Collection

### Framework

Using MLB-LAB V1 scoring model adapted from the uploaded six-gate prop framework:

- Environment
- Day/Night
- Pitcher Splits
- Pitch Arsenal
- Batter Matchup
- Savant Confirmation

Original framework uses sequential gates; MLB-LAB V1 converts this into a scoring model instead of automatic elimination.

---

## Today's Slate

| Game | Time ET | Park | Probable Pitchers |
|------|---------|------|-------------------|
| Brewers @ Braves | 1:35 PM | Truist Park | Robert Gasser vs TBD |
| Reds @ Yankees | 1:35 PM | Yankee Stadium | Chase Burns vs TBD |
| Giants @ Marlins | 1:40 PM | loanDepot park | TBD vs TBD |
| Nationals @ Rays | 1:40 PM | Tropicana Field | Andrew Alvarez vs Nick Martinez |
| White Sox @ Tigers | 1:40 PM | Comerica Park | Davis Martin vs Justin Verlander |
| Guardians @ Astros | 2:10 PM | Daikin Park | Slade Cecconi vs Kai-Wei Teng |
| Cardinals @ Royals | 2:10 PM | Kauffman Stadium | Dustin May vs Stephen Kolek |
| Blue Jays @ Cubs | 2:20 PM | Wrigley Field | TBD vs TBD |
| Padres @ Rangers | 2:35 PM | Globe Life Field | TBD vs TBD |
| Pirates @ Rockies | 3:10 PM | Coors Field | Jared Jones vs Michael Lorenzen |
| Twins @ D-backs | 3:15 PM | Chase Field | TBD vs Ryne Nelson |
| Angels @ Athletics | 4:05 PM | Sutter Health Park | TBD vs Jack Perkins |
| Red Sox @ Mariners | 4:10 PM | T-Mobile Park | Payton Tolle vs TBD |
| Orioles @ Dodgers | 4:10 PM | Dodger Stadium | TBD vs Emmet Sheehan |
| Mets @ Phillies | 7:20 PM | Citizens Bank Park | TBD vs Zack Wheeler |

---

## Layer 1 Notes

### Highest Environment Priority

1. Pirates @ Rockies
   - Coors Field
   - Immediate environment watch

2. Blue Jays @ Cubs
   - Wrigley wind-sensitive
   - Weather required before scoring

3. Padres @ Rangers
   - Roof status required

4. Twins @ D-backs
   - Roof status required

5. Mets @ Phillies
   - Night game
   - Day/night split filter applies

---

## Missing Inputs Before Layer 2

Need:

- Confirmed lineups
- Weather by stadium
- Roof status
- Pitcher handedness splits
- Pitch arsenal data
- Batter recent form
- Savant confirmation

---

## Current Status

## Current Status

Layer 1 complete.

Next:

Layer 2 — Research

Focus:

- Pitcher vulnerability
- Environment score
- ---

# Layer 2 Research

## Environment Analysis

| Game | Environment Notes | Initial Score |
|--------|--------|--------|
| Pirates @ Rockies | Coors Field boost | 20 |
| Blue Jays @ Cubs | Wind dependent | TBD |
| Padres @ Rangers | Roof dependent | TBD |
| Twins @ D-backs | Roof dependent | TBD |
| Mets @ Phillies | Neutral | 10 |

## Pitcher Vulnerability Analysis

Pending

Need:

- HR/9
- Barrel %
- Hard Hit %
- xERA
- xSLG

for all probable starters.

## Pitch Arsenal Analysis

Pending

Need:

- Pitch mix
- Velocity
- Whiff rates
- Batter pitch-type strengths

## Batter Matchup Analysis

Pending

Need:

- Handedness splits
- ISO
- SLG
- HR rates
- Recent form

## Candidate Watchlist

### 1. Pirates @ Rockies

Reason:
Coors Field environment boost.

Status:
Needs pitcher review.

### 2. Blue Jays @ Cubs

Reason:
Potential wind game.

Status:
Needs weather confirmation.

### 3. Mets @ Phillies

Reason:
Strong offensive talent.

Status:
Needs matchup review.
- Pitch arsenal targets


