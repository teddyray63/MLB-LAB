# MLB-LAB V1 Run 001

Status: Automated Schedule + Environment + Pitcher Scoring Active

Date: 2026-06-21

## Objective

Run MLB-LAB V1 using the system already built in this repo.

## Scoring Model

| Layer | Points |
|---|---:|
| Environment | 20 |
| Pitcher Vulnerability | 25 |
| Pitch Arsenal | 20 |
| Batter Matchup | 20 |
| Savant Confirmation | 15 |

---

## Today's Slate

| Rank | Game | Park | Probable Pitchers | Env | Pitcher | Early Total |
|---:|---|---|---|---:|---:|---:|
| 1 | Pittsburgh Pirates @ Colorado Rockies | Coors Field | Jared Jones vs Michael Lorenzen | 20 | 18 | 38 |
| 2 | Los Angeles Angels @ Athletics | Sutter Health Park | Reid Detmers vs Jack Perkins | 16 | 18 | 34 |
| 3 | Milwaukee Brewers @ Atlanta Braves | Truist Park | Robert Gasser vs Bryce Elder | 14 | 18 | 32 |
| 4 | Chicago White Sox @ Detroit Tigers | Comerica Park | Davis Martin vs Keider Montero | 11 | 18 | 29 |
| 5 | San Francisco Giants @ Miami Marlins | loanDepot park | Logan Webb vs Ryan Gusto | 10 | 18 | 28 |
| 6 | Cleveland Guardians @ Houston Astros | Daikin Park | Slade Cecconi vs Kai-Wei Teng | 10 | 18 | 28 |
| 7 | Cincinnati Reds @ New York Yankees | Yankee Stadium | Chase Burns vs Elmer Rodríguez | 15 | 10 | 25 |
| 8 | New York Mets @ Philadelphia Phillies | Citizens Bank Park | David Peterson vs Zack Wheeler | 15 | 10 | 25 |
| 9 | Minnesota Twins @ Arizona Diamondbacks | Chase Field | Mike Paredes vs Jose Cabrera | 13 | 10 | 23 |
| 10 | Washington Nationals @ Tampa Bay Rays | Tropicana Field | Andrew Alvarez vs Nick Martinez | 10 | 10 | 20 |
| 11 | San Diego Padres @ Texas Rangers | Globe Life Field | TBD vs Nathan Eovaldi | 14 | 6 | 20 |
| 12 | Baltimore Orioles @ Los Angeles Dodgers | UNIQLO Field at Dodger Stadium | Brandon Young vs Emmet Sheehan | 10 | 10 | 20 |
| 13 | Boston Red Sox @ Seattle Mariners | T-Mobile Park | Payton Tolle vs Logan Gilbert | 10 | 10 | 20 |
| 14 | St. Louis Cardinals @ Kansas City Royals | Kauffman Stadium | Dustin May vs Stephen Kolek | 8 | 10 | 18 |
| 15 | Toronto Blue Jays @ Chicago Cubs | Wrigley Field | Dylan Cease vs Shota Imanaga | 6 | 6 | 12 |


---

## Priority Games

These are ranked by early total:

Environment Score + Pitcher Vulnerability Score.

## Pitcher Scoring Notes

- TBD pitcher = 5
- Strong pitcher = 6
- Neutral known pitcher = 10
- Weak pitcher watchlist = 18

This is still an early scoring layer, not a final betting card.

## Next Upgrades

1. Add weather
2. Add pitch arsenal scoring
3. Add hitter candidate ranking
4. Add Savant confirmation
5. Generate final daily report

## Current Output

Automated MLB schedule pull is working.  
Environment scoring is working.  
Pitcher vulnerability scoring is working.
