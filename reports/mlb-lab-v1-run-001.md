# MLB-LAB V1 Run 001

Status: Full Game Scoring Active

Date: 2026-06-21

## Objective

Run every MLB game through the MLB-LAB V1 scoring system.

## Scoring Model

| Layer | Points |
|---|---:|
| Environment | 20 |
| Pitcher Vulnerability | 25 |
| Pitch Arsenal | 20 |
| Batter Matchup | 20 |
| Savant Confirmation | 15 |

No hard eliminations. Every game receives a score.

---

## Full Slate Scoreboard

| Rank | Game | Park | Probable Pitchers | Env | Pitcher | Arsenal | Matchup | Savant | Total | Tier |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Pittsburgh Pirates @ Colorado Rockies | Coors Field | Jared Jones vs Michael Lorenzen | 20 | 18 | 15 | 16 | 12 | 81 | Priority |
| 2 | Los Angeles Angels @ Athletics | Sutter Health Park | Reid Detmers vs Jack Perkins | 16 | 18 | 15 | 16 | 12 | 77 | Priority |
| 3 | Milwaukee Brewers @ Atlanta Braves | Truist Park | Robert Gasser vs Bryce Elder | 14 | 18 | 12 | 12 | 10 | 66 | Watch |
| 4 | Chicago White Sox @ Detroit Tigers | Comerica Park | Davis Martin vs Keider Montero | 11 | 18 | 13 | 11 | 8 | 61 | Watch |
| 5 | Cleveland Guardians @ Houston Astros | Daikin Park | Slade Cecconi vs Kai-Wei Teng | 10 | 18 | 14 | 11 | 8 | 61 | Watch |
| 6 | San Francisco Giants @ Miami Marlins | loanDepot park | Logan Webb vs Ryan Gusto | 10 | 18 | 13 | 11 | 8 | 60 | Watch |
| 7 | Cincinnati Reds @ New York Yankees | Yankee Stadium | Chase Burns vs Elmer Rodríguez | 15 | 10 | 8 | 12 | 8 | 53 | Low |
| 8 | New York Mets @ Philadelphia Phillies | Citizens Bank Park | David Peterson vs Zack Wheeler | 15 | 10 | 8 | 12 | 8 | 53 | Low |
| 9 | Minnesota Twins @ Arizona Diamondbacks | Chase Field | Mike Paredes vs Jose Cabrera | 13 | 10 | 8 | 12 | 6 | 49 | Low |
| 10 | Washington Nationals @ Tampa Bay Rays | Tropicana Field | Andrew Alvarez vs Nick Martinez | 10 | 10 | 8 | 8 | 6 | 42 | Low |
| 11 | San Diego Padres @ Texas Rangers | Globe Life Field | TBD vs Nathan Eovaldi | 14 | 6 | 8 | 8 | 6 | 42 | Low |
| 12 | Baltimore Orioles @ Los Angeles Dodgers | UNIQLO Field at Dodger Stadium | Brandon Young vs Emmet Sheehan | 10 | 10 | 8 | 8 | 6 | 42 | Low |
| 13 | Boston Red Sox @ Seattle Mariners | T-Mobile Park | Payton Tolle vs Logan Gilbert | 10 | 10 | 8 | 8 | 6 | 42 | Low |
| 14 | St. Louis Cardinals @ Kansas City Royals | Kauffman Stadium | Dustin May vs Stephen Kolek | 8 | 10 | 8 | 8 | 6 | 40 | Low |
| 15 | Toronto Blue Jays @ Chicago Cubs | Wrigley Field | Dylan Cease vs Shota Imanaga | 6 | 6 | 8 | 8 | 6 | 34 | Ignore |


---

## Priority Games

- Pittsburgh Pirates @ Colorado Rockies — 81 total
- Los Angeles Angels @ Athletics — 77 total


## Watch Games

- Milwaukee Brewers @ Atlanta Braves — 66 total
- Chicago White Sox @ Detroit Tigers — 61 total
- Cleveland Guardians @ Houston Astros — 61 total
- San Francisco Giants @ Miami Marlins — 60 total


## Notes

This is a full-slate game scoring engine.

Current automated layers:

- Schedule
- Probable pitchers
- Environment score
- Pitcher vulnerability score
- Pitch arsenal placeholder score
- Matchup placeholder score
- Savant placeholder score

Next upgrade:
Replace placeholder Arsenal / Matchup / Savant scores with real Statcast and batter data.
