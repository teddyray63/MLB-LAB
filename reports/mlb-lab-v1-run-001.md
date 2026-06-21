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
---

# Layer 2 Research — Live Data Pass

## Data Sources Used

- MLB schedule / probable pitchers
- Weather by stadium city
- Uploaded Signal Hierarchy Framework

## Environment Scoring

| Game | Park | Weather / Context | Env Score | Notes |
|---|---|---|---:|---|
| Brewers @ Braves | Truist Park | Atlanta high 86°F, humid, possible afternoon thunderstorm | 14 | Warm, but weather risk |
| Reds @ Yankees | Yankee Stadium | New York high 83°F, sun/clouds | 15 | Warm enough for power/contact |
| Giants @ Marlins | loanDepot park | Miami high 92°F, roof/indoor context likely | 10 | Weather less useful without roof status |
| Nationals @ Rays | Tropicana Field | Dome | 10 | Neutral controlled environment |
| White Sox @ Tigers | Comerica Park | Detroit high 76°F | 11 | Mild/neutral |
| Guardians @ Astros | Daikin Park | Houston storms, roof likely relevant | 10 | Roof/weather uncertainty |
| Cardinals @ Royals | Kauffman Stadium | Kansas City rain/thunderstorm risk | 8 | Weather risk suppresses confidence |
| Blue Jays @ Cubs | Wrigley Field | Chicago rain/thunderstorm risk | 6 | Major weather risk; wind still needed |
| Padres @ Rangers | Globe Life Field | Arlington high 93°F, humid/windy | 14 | Strong heat, roof status needed |
| Pirates @ Rockies | Coors Field | Denver high 91°F | 20 | Best raw environment |
| Twins @ D-backs | Chase Field | Phoenix high 107°F, roof status needed | 13 | Extreme heat, roof likely relevant |
| Angels @ Athletics | Sutter Health Park | Sacramento high 90°F | 16 | Strong heat boost |
| Red Sox @ Mariners | T-Mobile Park | Seattle high 76°F | 10 | Neutral/slightly mild |
| Orioles @ Dodgers | Dodger Stadium | Los Angeles high 75°F | 11 | Neutral |
| Mets @ Phillies | Citizens Bank Park | Philadelphia high 86°F, night game | 15 | Warm night environment |

## Environment Priority List

### Green / Attack First

1. Pirates @ Rockies — 20
2. Angels @ Athletics — 16
3. Reds @ Yankees — 15
4. Mets @ Phillies — 15
5. Brewers @ Braves — 14
6. Padres @ Rangers — 14

### Yellow / Need More Data

1. Twins @ D-backs — roof status
2. Orioles @ Dodgers — pitcher matchup needed
3. Red Sox @ Mariners — neutral
4. Nationals @ Rays — dome/neutral
5. Guardians @ Astros — roof/weather uncertainty

### Red / Deprioritize For Now

1. Blue Jays @ Cubs — rain/thunderstorm risk
2. Cardinals @ Royals — rain/thunderstorm risk

---

## Pitcher Vulnerability First Pass

| Game | Pitchers | Initial Vulnerability Read |
|---|---|---|
| Brewers @ Braves | Robert Gasser vs TBD | Need Braves pitcher. Gasser has elevated ERA, possible Braves bats watch. |
| Reds @ Yankees | Chase Burns vs TBD | Burns profile appears strong; wait for Yankees pitcher. |
| Nationals @ Rays | Andrew Alvarez vs Nick Martinez | Martinez strong ERA; Alvarez moderate. Low-priority until splits. |
| White Sox @ Tigers | Davis Martin vs Justin Verlander | Verlander 12.27 ERA small-sample red flag; Tigers/White Sox needs review. |
| Guardians @ Astros | Slade Cecconi vs Kai-Wei Teng | Both ERAs above 4.30; possible hitter candidate game. |
| Cardinals @ Royals | Dustin May vs Stephen Kolek | Both moderate/solid; weather lowers priority. |
| Pirates @ Rockies | Jared Jones vs Michael Lorenzen | Both ERAs above 6.00; Coors + weak pitching = top research game. |
| Twins @ D-backs | TBD vs Ryne Nelson | Nelson 4.97 ERA; Twins bats may deserve review. |
| Angels @ Athletics | TBD vs Jack Perkins | Perkins 6.15 ERA plus hot Sacramento environment = attack watch. |
| Red Sox @ Mariners | Payton Tolle vs TBD | Tolle solid ERA; needs opposing pitcher. |
| Orioles @ Dodgers | TBD vs Emmet Sheehan | Sheehan 4.76 ERA; Orioles bats watch if lineup confirms. |
| Mets @ Phillies | TBD vs Zack Wheeler | Wheeler elite ERA; Phillies side depends on Mets pitcher TBD. |

---

## Current Candidate Games

| Rank | Game | Reason | Status |
|---:|---|---|---|
| 1 | Pirates @ Rockies | Coors + two vulnerable pitchers | Priority research |
| 2 | Angels @ Athletics | Hot environment + Jack Perkins 6.15 ERA | Priority research |
| 3 | Guardians @ Astros | Both pitchers vulnerable by ERA | Watch |
| 4 | Mets @ Phillies | Warm night + Phillies offense if Mets pitcher weak | Watch |
| 5 | Reds @ Yankees | Warm Yankee Stadium, pitcher TBD needed | Watch |
| 6 | Brewers @ Braves | Warm park, Gasser vulnerability possible | Watch |

---

## Layer 2 Status

Environment pass complete.

Pitcher vulnerability first pass complete.

Next step:

Layer 3 Intelligence Scoring.

Need to score only the best candidate games first:

1. Pirates @ Rockies
2. Angels @ Athletics
3. Guardians @ Astros
4. Mets @ Phillies

# Layer 2 Research

