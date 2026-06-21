# MLB-LAB V3 Game Dissection Report

Date: 2026-06-21

Status: Complete.

Mode: full-slate game dissection engine.

No hard eliminations. Every game receives a card.

---

## Slate Index

| Rank | Game | Park | SP Matchup | Env | Pitcher | Offense | Bullpen | Matchup | Total | Tier |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Pittsburgh Pirates @ Colorado Rockies | Coors Field | Jared Jones vs Michael Lorenzen | 20 | 25 | 18 | 15 | 20 | 98 | Priority |
| 2 | Cincinnati Reds @ New York Yankees | Yankee Stadium | Chase Burns vs Elmer Rodríguez | 15 | 21 | 19 | 15 | 20 | 90 | Priority |
| 3 | Los Angeles Angels @ Athletics | Sutter Health Park | Reid Detmers vs Jack Perkins | 16 | 20 | 19 | 15 | 20 | 90 | Priority |
| 4 | San Francisco Giants @ Miami Marlins | loanDepot park | Logan Webb vs Ryan Gusto | 10 | 25 | 16 | 15 | 20 | 86 | Priority |
| 5 | Milwaukee Brewers @ Atlanta Braves | Truist Park | Robert Gasser vs Bryce Elder | 14 | 23 | 19 | 8 | 20 | 84 | Priority |
| 6 | Cleveland Guardians @ Houston Astros | Daikin Park | Slade Cecconi vs Kai-Wei Teng | 10 | 21 | 17 | 15 | 20 | 83 | Priority |
| 7 | Minnesota Twins @ Arizona Diamondbacks | Chase Field | Mike Paredes vs Jose Cabrera | 13 | 18 | 18 | 15 | 16 | 80 | Priority |
| 8 | Baltimore Orioles @ Los Angeles Dodgers | UNIQLO Field at Dodger Stadium | Brandon Young vs Emmet Sheehan | 10 | 18 | 20 | 15 | 16 | 79 | Priority |
| 9 | Washington Nationals @ Tampa Bay Rays | Tropicana Field | Andrew Alvarez vs Nick Martinez | 10 | 16 | 20 | 15 | 16 | 77 | Priority |
| 10 | New York Mets @ Philadelphia Phillies | Citizens Bank Park | David Peterson vs Zack Wheeler | 15 | 22 | 10 | 12 | 16 | 75 | Priority |
| 11 | Toronto Blue Jays @ Chicago Cubs | Wrigley Field | Dylan Cease vs Shota Imanaga | 10 | 17 | 16 | 14 | 16 | 73 | Watch |
| 12 | Chicago White Sox @ Detroit Tigers | Comerica Park | Davis Martin vs Keider Montero | 11 | 12 | 15 | 15 | 12 | 65 | Watch |
| 13 | San Diego Padres @ Texas Rangers | Globe Life Field | TBD vs Nathan Eovaldi | 14 | 15 | 10 | 10 | 12 | 61 | Watch |
| 14 | St. Louis Cardinals @ Kansas City Royals | Kauffman Stadium | Dustin May vs Stephen Kolek | 8 | 11 | 14 | 15 | 12 | 60 | Watch |
| 15 | Boston Red Sox @ Seattle Mariners | T-Mobile Park | Payton Tolle vs Logan Gilbert | 10 | 11 | 12 | 10 | 12 | 55 | Low |

---

# Full Game Cards


---

## 1. Pittsburgh Pirates @ Colorado Rockies — Priority (98)

### Game Context

| Field | Value |
|---|---|
| Park | Coors Field |
| Time | 2026-06-21T19:10:00Z |
| Environment | 20 |
| Pitcher Risk | 25 |
| Offense | 18 |
| Bullpen | 15 |
| Matchup Pressure | 20 |
| Total | 98 |


### Away SP: Jared Jones (—)

| Stat | Value |
|---|---:|
| ERA | 6.23 |
| WHIP | 1.62 |
| K/9 | 9.35 |
| BB/9 | 3.12 |
| HR/9 | 2.08 |
| IP | 17.1 |
| H | 22 |
| R | 12 |
| HR | 4 |
| Risk Score | 25 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-05-29 | Minnesota Twins | 4.1 | 7 | 5 | 2 | 6 | 2 |
| 2026-06-04 | Houston Astros | 5.0 | 4 | 0 | 2 | 4 | 0 |
| 2026-06-10 | Los Angeles Dodgers | 4.0 | 3 | 2 | 1 | 4 | 0 |
| 2026-06-15 | Athletics | 4.0 | 8 | 5 | 1 | 4 | 2 |



### Home SP: Michael Lorenzen (—)

| Stat | Value |
|---|---:|
| ERA | 7.13 |
| WHIP | 1.85 |
| K/9 | 7.64 |
| BB/9 | 3.18 |
| HR/9 | 1.53 |
| IP | 70.2 |
| H | 106 |
| R | 62 |
| HR | 12 |
| Risk Score | 25 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-28 | Miami Marlins | 4.1 | 7 | 3 | 0 | 4 | 1 |
| 2026-04-03 | Philadelphia Phillies | 3.0 | 12 | 9 | 2 | 2 | 2 |
| 2026-04-08 | Houston Astros | 5.2 | 7 | 1 | 2 | 4 | 0 |
| 2026-04-11 | San Diego Padres | 1.0 | 0 | 0 | 0 | 0 | 0 |
| 2026-04-14 | Houston Astros | 2.2 | 7 | 2 | 1 | 3 | 1 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| Pittsburgh Pirates | .254 | .741 | 383 | 92 | 18 |
| Colorado Rockies | .252 | .732 | 350 | 83 | 18 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| Pittsburgh Pirates | 4.20 | 1.31 | 0.97 | 10 |
| Colorado Rockies | 5.49 | 1.52 | 1.39 | 15 |

### Dissection Read

- First attack side: Home bats vs away SP
- Main pitcher concern: Jared Jones
- Park/environment pressure: 20
- Offense pressure: 18
- Bullpen/staff pressure: 15
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 2. Cincinnati Reds @ New York Yankees — Priority (90)

### Game Context

| Field | Value |
|---|---|
| Park | Yankee Stadium |
| Time | 2026-06-21T17:35:00Z |
| Environment | 15 |
| Pitcher Risk | 21 |
| Offense | 19 |
| Bullpen | 15 |
| Matchup Pressure | 20 |
| Total | 90 |


### Away SP: Chase Burns (—)

| Stat | Value |
|---|---:|
| ERA | 2.01 |
| WHIP | 1.02 |
| K/9 | 10.60 |
| BB/9 | 2.90 |
| HR/9 | 1.00 |
| IP | 80.2 |
| H | 56 |
| R | 18 |
| HR | 9 |
| Risk Score | 9 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-30 | Pittsburgh Pirates | 5.0 | 1 | 0 | 3 | 7 | 0 |
| 2026-04-05 | Texas Rangers | 6.0 | 5 | 1 | 1 | 9 | 1 |
| 2026-04-10 | Los Angeles Angels | 5.1 | 7 | 5 | 4 | 2 | 2 |
| 2026-04-16 | San Francisco Giants | 6.0 | 2 | 0 | 1 | 4 | 0 |
| 2026-04-21 | Tampa Bay Rays | 5.2 | 4 | 2 | 2 | 8 | 1 |



### Home SP: Elmer Rodríguez (—)

| Stat | Value |
|---|---:|
| ERA | 4.15 |
| WHIP | 1.85 |
| K/9 | 4.15 |
| BB/9 | 6.23 |
| HR/9 | 0.00 |
| IP | 13.0 |
| H | 15 |
| R | 6 |
| HR | 0 |
| Risk Score | 21 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-04-29 | Texas Rangers | 4.0 | 4 | 2 | 4 | 3 | 0 |
| 2026-05-05 | Texas Rangers | 4.2 | 6 | 3 | 4 | 2 | 0 |
| 2026-05-17 | New York Mets | 4.1 | 5 | 1 | 1 | 1 | 0 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| Cincinnati Reds | .229 | .707 | 321 | 95 | 12 |
| New York Yankees | .246 | .772 | 388 | 113 | 19 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| Cincinnati Reds | 4.63 | 1.47 | 1.37 | 15 |
| New York Yankees | 3.34 | 1.18 | 0.92 | 8 |

### Dissection Read

- First attack side: Away bats vs home SP
- Main pitcher concern: Elmer Rodríguez
- Park/environment pressure: 15
- Offense pressure: 19
- Bullpen/staff pressure: 15
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 3. Los Angeles Angels @ Athletics — Priority (90)

### Game Context

| Field | Value |
|---|---|
| Park | Sutter Health Park |
| Time | 2026-06-21T20:05:00Z |
| Environment | 16 |
| Pitcher Risk | 20 |
| Offense | 19 |
| Bullpen | 15 |
| Matchup Pressure | 20 |
| Total | 90 |


### Away SP: Reid Detmers (—)

| Stat | Value |
|---|---:|
| ERA | 3.68 |
| WHIP | 1.00 |
| K/9 | 10.23 |
| BB/9 | 2.45 |
| HR/9 | 0.72 |
| IP | 88.0 |
| H | 64 |
| R | 39 |
| HR | 7 |
| Risk Score | 8 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-28 | Houston Astros | 4.2 | 6 | 3 | 0 | 9 | 0 |
| 2026-04-03 | Seattle Mariners | 6.2 | 3 | 0 | 4 | 4 | 0 |
| 2026-04-08 | Atlanta Braves | 4.1 | 5 | 5 | 2 | 4 | 1 |
| 2026-04-14 | New York Yankees | 7.0 | 4 | 1 | 0 | 9 | 0 |
| 2026-04-20 | Toronto Blue Jays | 6.0 | 5 | 4 | 2 | 5 | 1 |



### Home SP: Jack Perkins (—)

| Stat | Value |
|---|---:|
| ERA | 6.15 |
| WHIP | 1.39 |
| K/9 | 10.76 |
| BB/9 | 3.07 |
| HR/9 | 1.10 |
| IP | 41.0 |
| H | 43 |
| R | 30 |
| HR | 5 |
| Risk Score | 20 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-04-10 | New York Mets | 2.1 | 3 | 0 | 0 | 3 | 0 |
| 2026-04-13 | Texas Rangers | 1.2 | 5 | 4 | 1 | 4 | 0 |
| 2026-04-16 | Texas Rangers | 1.0 | 0 | 0 | 0 | 0 | 0 |
| 2026-04-18 | Chicago White Sox | 2.1 | 1 | 0 | 2 | 3 | 0 |
| 2026-04-21 | Seattle Mariners | 2.0 | 0 | 0 | 0 | 2 | 0 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| Los Angeles Angels | .239 | .718 | 352 | 92 | 14 |
| Athletics | .250 | .751 | 357 | 104 | 19 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| Los Angeles Angels | 4.63 | 1.43 | 1.09 | 15 |
| Athletics | 4.95 | 1.45 | 1.46 | 15 |

### Dissection Read

- First attack side: Away bats vs home SP
- Main pitcher concern: Jack Perkins
- Park/environment pressure: 16
- Offense pressure: 19
- Bullpen/staff pressure: 15
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 4. San Francisco Giants @ Miami Marlins — Priority (86)

### Game Context

| Field | Value |
|---|---|
| Park | loanDepot park |
| Time | 2026-06-21T17:40:00Z |
| Environment | 10 |
| Pitcher Risk | 25 |
| Offense | 16 |
| Bullpen | 15 |
| Matchup Pressure | 20 |
| Total | 86 |


### Away SP: Logan Webb (—)

| Stat | Value |
|---|---:|
| ERA | 3.46 |
| WHIP | 1.15 |
| K/9 | 7.77 |
| BB/9 | 2.27 |
| HR/9 | 0.48 |
| IP | 75.1 |
| H | 68 |
| R | 32 |
| HR | 4 |
| Risk Score | 9 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-25 | New York Yankees | 5.0 | 9 | 6 | 1 | 7 | 0 |
| 2026-03-31 | San Diego Padres | 6.0 | 3 | 3 | 4 | 5 | 0 |
| 2026-04-05 | New York Mets | 7.0 | 7 | 1 | 1 | 3 | 0 |
| 2026-04-11 | Baltimore Orioles | 6.0 | 5 | 4 | 3 | 6 | 1 |
| 2026-04-17 | Washington Nationals | 6.0 | 7 | 3 | 2 | 6 | 1 |



### Home SP: Ryan Gusto (—)

| Stat | Value |
|---|---:|
| ERA | 7.24 |
| WHIP | 1.76 |
| K/9 | 6.59 |
| BB/9 | 3.29 |
| HR/9 | 1.32 |
| IP | 13.2 |
| H | 19 |
| R | 11 |
| HR | 2 |
| Risk Score | 25 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-04-08 | Cincinnati Reds | 1.0 | 0 | 0 | 0 | 1 | 0 |
| 2026-06-02 | Washington Nationals | 2.0 | 5 | 3 | 0 | 3 | 0 |
| 2026-06-05 | Tampa Bay Rays | 2.0 | 3 | 3 | 1 | 1 | 0 |
| 2026-06-10 | Arizona Diamondbacks | 4.0 | 3 | 0 | 1 | 4 | 0 |
| 2026-06-15 | Philadelphia Phillies | 4.2 | 8 | 5 | 3 | 1 | 2 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| San Francisco Giants | .259 | .731 | 316 | 81 | 16 |
| Miami Marlins | .246 | .711 | 334 | 68 | 12 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| San Francisco Giants | 4.49 | 1.40 | 1.06 | 15 |
| Miami Marlins | 4.11 | 1.26 | 0.99 | 8 |

### Dissection Read

- First attack side: Away bats vs home SP
- Main pitcher concern: Ryan Gusto
- Park/environment pressure: 10
- Offense pressure: 16
- Bullpen/staff pressure: 15
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 5. Milwaukee Brewers @ Atlanta Braves — Priority (84)

### Game Context

| Field | Value |
|---|---|
| Park | Truist Park |
| Time | 2026-06-21T17:35:00Z |
| Environment | 14 |
| Pitcher Risk | 23 |
| Offense | 19 |
| Bullpen | 8 |
| Matchup Pressure | 20 |
| Total | 84 |


### Away SP: Robert Gasser (—)

| Stat | Value |
|---|---:|
| ERA | 4.88 |
| WHIP | 1.38 |
| K/9 | 9.00 |
| BB/9 | 4.13 |
| HR/9 | 2.25 |
| IP | 24.0 |
| H | 22 |
| R | 14 |
| HR | 6 |
| Risk Score | 23 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-05-17 | Minnesota Twins | 4.0 | 3 | 2 | 2 | 3 | 0 |
| 2026-05-23 | Los Angeles Dodgers | 4.1 | 4 | 4 | 4 | 4 | 1 |
| 2026-06-03 | San Francisco Giants | 5.0 | 5 | 1 | 1 | 5 | 1 |
| 2026-06-09 | Athletics | 5.0 | 8 | 6 | 2 | 7 | 4 |
| 2026-06-16 | Cleveland Guardians | 5.2 | 2 | 0 | 2 | 5 | 0 |



### Home SP: Bryce Elder (—)

| Stat | Value |
|---|---:|
| ERA | 3.15 |
| WHIP | 1.14 |
| K/9 | 7.41 |
| BB/9 | 2.74 |
| HR/9 | 0.91 |
| IP | 88.2 |
| H | 74 |
| R | 35 |
| HR | 9 |
| Risk Score | 10 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-30 | Athletics | 6.0 | 5 | 0 | 1 | 5 | 0 |
| 2026-04-04 | Arizona Diamondbacks | 7.0 | 4 | 0 | 1 | 8 | 0 |
| 2026-04-10 | Cleveland Guardians | 4.2 | 4 | 2 | 3 | 3 | 1 |
| 2026-04-15 | Miami Marlins | 5.2 | 4 | 0 | 2 | 7 | 0 |
| 2026-04-20 | Washington Nationals | 6.2 | 3 | 3 | 2 | 6 | 1 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| Milwaukee Brewers | .255 | .732 | 388 | 67 | 16 |
| Atlanta Braves | .253 | .740 | 373 | 100 | 19 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| Milwaukee Brewers | 3.44 | 1.20 | 0.97 | 8 |
| Atlanta Braves | 3.34 | 1.19 | 1.08 | 8 |

### Dissection Read

- First attack side: Home bats vs away SP
- Main pitcher concern: Robert Gasser
- Park/environment pressure: 14
- Offense pressure: 19
- Bullpen/staff pressure: 8
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 6. Cleveland Guardians @ Houston Astros — Priority (83)

### Game Context

| Field | Value |
|---|---|
| Park | Daikin Park |
| Time | 2026-06-21T18:10:00Z |
| Environment | 10 |
| Pitcher Risk | 21 |
| Offense | 17 |
| Bullpen | 15 |
| Matchup Pressure | 20 |
| Total | 83 |


### Away SP: Slade Cecconi (—)

| Stat | Value |
|---|---:|
| ERA | 4.60 |
| WHIP | 1.40 |
| K/9 | 7.47 |
| BB/9 | 2.87 |
| HR/9 | 1.26 |
| IP | 78.1 |
| H | 85 |
| R | 42 |
| HR | 11 |
| Risk Score | 19 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-29 | Seattle Mariners | 4.1 | 6 | 6 | 3 | 5 | 1 |
| 2026-04-05 | Chicago Cubs | 6.0 | 1 | 0 | 1 | 6 | 0 |
| 2026-04-10 | Atlanta Braves | 5.1 | 7 | 4 | 1 | 3 | 2 |
| 2026-04-15 | St. Louis Cardinals | 4.0 | 3 | 1 | 5 | 4 | 0 |
| 2026-04-20 | Houston Astros | 5.0 | 10 | 6 | 2 | 2 | 2 |



### Home SP: Kai-Wei Teng (—)

| Stat | Value |
|---|---:|
| ERA | 4.31 |
| WHIP | 1.34 |
| K/9 | 9.61 |
| BB/9 | 4.31 |
| HR/9 | 1.49 |
| IP | 54.1 |
| H | 47 |
| R | 29 |
| HR | 9 |
| Risk Score | 21 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-28 | Los Angeles Angels | 2.1 | 1 | 0 | 1 | 2 | 0 |
| 2026-04-01 | Boston Red Sox | 1.0 | 1 | 1 | 0 | 1 | 1 |
| 2026-04-04 | Athletics | 2.1 | 2 | 0 | 0 | 3 | 0 |
| 2026-04-07 | Colorado Rockies | 0.2 | 1 | 1 | 0 | 0 | 1 |
| 2026-04-08 | Colorado Rockies | 1.1 | 0 | 0 | 0 | 1 | 0 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| Cleveland Guardians | .229 | .686 | 309 | 74 | 8 |
| Houston Astros | .243 | .731 | 354 | 102 | 17 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| Cleveland Guardians | 3.81 | 1.26 | 1.19 | 10 |
| Houston Astros | 4.89 | 1.41 | 1.32 | 15 |

### Dissection Read

- First attack side: Away bats vs home SP
- Main pitcher concern: Kai-Wei Teng
- Park/environment pressure: 10
- Offense pressure: 17
- Bullpen/staff pressure: 15
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 7. Minnesota Twins @ Arizona Diamondbacks — Priority (80)

### Game Context

| Field | Value |
|---|---|
| Park | Chase Field |
| Time | 2026-06-21T19:15:00Z |
| Environment | 13 |
| Pitcher Risk | 18 |
| Offense | 18 |
| Bullpen | 15 |
| Matchup Pressure | 16 |
| Total | 80 |


### Away SP: Mike Paredes (—)

| Stat | Value |
|---|---:|
| ERA | 4.20 |
| WHIP | 1.00 |
| K/9 | 6.00 |
| BB/9 | 3.60 |
| HR/9 | 1.20 |
| IP | 15.0 |
| H | 9 |
| R | 8 |
| HR | 2 |
| Risk Score | 18 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-05-31 | Pittsburgh Pirates | 3.2 | 2 | 1 | 3 | 3 | 0 |
| 2026-06-04 | Kansas City Royals | 3.2 | 2 | 3 | 1 | 1 | 1 |
| 2026-06-10 | Detroit Tigers | 3.0 | 1 | 1 | 2 | 4 | 0 |
| 2026-06-15 | Texas Rangers | 4.2 | 4 | 2 | 0 | 2 | 1 |



### Home SP: Jose Cabrera (—)

| Stat | Value |
|---|---:|
| ERA | — |
| WHIP | — |
| K/9 | — |
| BB/9 | — |
| HR/9 | — |
| IP | — |
| H | — |
| R | — |
| HR | — |
| Risk Score | 8 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| — | — | — | — | — | — | — | — |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| Minnesota Twins | .246 | .735 | 384 | 97 | 18 |
| Arizona Diamondbacks | .239 | .695 | 329 | 68 | 8 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| Minnesota Twins | 4.83 | 1.39 | 1.15 | 15 |
| Arizona Diamondbacks | 4.32 | 1.30 | 1.25 | 15 |

### Dissection Read

- First attack side: Home bats vs away SP
- Main pitcher concern: Mike Paredes
- Park/environment pressure: 13
- Offense pressure: 18
- Bullpen/staff pressure: 15
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 8. Baltimore Orioles @ Los Angeles Dodgers — Priority (79)

### Game Context

| Field | Value |
|---|---|
| Park | UNIQLO Field at Dodger Stadium |
| Time | 2026-06-21T20:10:00Z |
| Environment | 10 |
| Pitcher Risk | 18 |
| Offense | 20 |
| Bullpen | 15 |
| Matchup Pressure | 16 |
| Total | 79 |


### Away SP: Brandon Young (—)

| Stat | Value |
|---|---:|
| ERA | 3.18 |
| WHIP | 1.25 |
| K/9 | 6.35 |
| BB/9 | 3.32 |
| HR/9 | 0.87 |
| IP | 62.1 |
| H | 55 |
| R | 30 |
| HR | 6 |
| Risk Score | 14 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-04-06 | Chicago White Sox | 5.0 | 2 | 0 | 2 | 2 | 0 |
| 2026-04-24 | Boston Red Sox | 5.2 | 7 | 3 | 1 | 5 | 1 |
| 2026-04-30 | Houston Astros | 4.0 | 9 | 4 | 2 | 2 | 2 |
| 2026-05-06 | Miami Marlins | 6.0 | 4 | 3 | 3 | 5 | 0 |
| 2026-05-11 | New York Yankees | 5.1 | 3 | 2 | 3 | 5 | 1 |



### Home SP: Emmet Sheehan (—)

| Stat | Value |
|---|---:|
| ERA | 4.76 |
| WHIP | 1.20 |
| K/9 | 10.07 |
| BB/9 | 2.38 |
| HR/9 | 1.68 |
| IP | 64.1 |
| H | 60 |
| R | 34 |
| HR | 12 |
| Risk Score | 18 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-27 | Arizona Diamondbacks | 3.1 | 5 | 4 | 2 | 6 | 1 |
| 2026-04-03 | Washington Nationals | 5.2 | 7 | 4 | 3 | 2 | 1 |
| 2026-04-11 | Texas Rangers | 6.0 | 4 | 3 | 1 | 6 | 2 |
| 2026-04-18 | Colorado Rockies | 5.0 | 4 | 2 | 2 | 4 | 0 |
| 2026-04-24 | Chicago Cubs | 6.1 | 4 | 1 | 1 | 10 | 0 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| Baltimore Orioles | .239 | .716 | 357 | 90 | 14 |
| Los Angeles Dodgers | .261 | .783 | 404 | 105 | 20 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| Baltimore Orioles | 4.50 | 1.39 | 1.17 | 15 |
| Los Angeles Dodgers | 3.34 | 1.09 | 1.02 | 8 |

### Dissection Read

- First attack side: Away bats vs home SP
- Main pitcher concern: Emmet Sheehan
- Park/environment pressure: 10
- Offense pressure: 20
- Bullpen/staff pressure: 15
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 9. Washington Nationals @ Tampa Bay Rays — Priority (77)

### Game Context

| Field | Value |
|---|---|
| Park | Tropicana Field |
| Time | 2026-06-21T17:40:00Z |
| Environment | 10 |
| Pitcher Risk | 16 |
| Offense | 20 |
| Bullpen | 15 |
| Matchup Pressure | 16 |
| Total | 77 |


### Away SP: Andrew Alvarez (—)

| Stat | Value |
|---|---:|
| ERA | 3.49 |
| WHIP | 1.45 |
| K/9 | 9.85 |
| BB/9 | 3.81 |
| HR/9 | 0.64 |
| IP | 28.1 |
| H | 29 |
| R | 11 |
| HR | 2 |
| Risk Score | 16 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-04-19 | San Francisco Giants | 4.1 | 4 | 0 | 0 | 5 | 0 |
| 2026-05-15 | Baltimore Orioles | 3.0 | 3 | 2 | 1 | 5 | 0 |
| 2026-05-20 | New York Mets | 4.0 | 2 | 2 | 1 | 5 | 1 |
| 2026-05-24 | Atlanta Braves | 1.1 | 1 | 0 | 1 | 1 | 0 |
| 2026-05-29 | San Diego Padres | 3.0 | 5 | 3 | 2 | 1 | 0 |



### Home SP: Nick Martinez (—)

| Stat | Value |
|---|---:|
| ERA | 2.60 |
| WHIP | 1.16 |
| K/9 | 5.42 |
| BB/9 | 1.52 |
| HR/9 | 0.76 |
| IP | 83.0 |
| H | 82 |
| R | 24 |
| HR | 7 |
| Risk Score | 11 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-30 | Milwaukee Brewers | 6.0 | 6 | 2 | 0 | 3 | 1 |
| 2026-04-05 | Minnesota Twins | 6.0 | 1 | 1 | 1 | 4 | 1 |
| 2026-04-11 | New York Yankees | 4.2 | 5 | 1 | 3 | 4 | 1 |
| 2026-04-17 | Pittsburgh Pirates | 5.1 | 8 | 2 | 3 | 3 | 0 |
| 2026-04-22 | Cincinnati Reds | 8.0 | 5 | 1 | 1 | 6 | 0 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| Washington Nationals | .247 | .743 | 413 | 100 | 20 |
| Tampa Bay Rays | .256 | .716 | 323 | 60 | 12 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| Washington Nationals | 4.64 | 1.39 | 1.42 | 15 |
| Tampa Bay Rays | 3.92 | 1.23 | 1.21 | 10 |

### Dissection Read

- First attack side: Home bats vs away SP
- Main pitcher concern: Andrew Alvarez
- Park/environment pressure: 10
- Offense pressure: 20
- Bullpen/staff pressure: 15
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 10. New York Mets @ Philadelphia Phillies — Priority (75)

### Game Context

| Field | Value |
|---|---|
| Park | Citizens Bank Park |
| Time | 2026-06-21T23:20:00Z |
| Environment | 15 |
| Pitcher Risk | 22 |
| Offense | 10 |
| Bullpen | 12 |
| Matchup Pressure | 16 |
| Total | 75 |


### Away SP: David Peterson (—)

| Stat | Value |
|---|---:|
| ERA | 5.91 |
| WHIP | 1.63 |
| K/9 | 8.16 |
| BB/9 | 3.94 |
| HR/9 | 0.70 |
| IP | 64.0 |
| H | 76 |
| R | 46 |
| HR | 5 |
| Risk Score | 22 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-28 | Pittsburgh Pirates | 5.1 | 6 | 0 | 2 | 3 | 0 |
| 2026-04-02 | San Francisco Giants | 4.1 | 9 | 5 | 2 | 5 | 0 |
| 2026-04-08 | Arizona Diamondbacks | 5.0 | 6 | 5 | 2 | 6 | 0 |
| 2026-04-13 | Los Angeles Dodgers | 5.0 | 5 | 4 | 4 | 7 | 1 |
| 2026-04-19 | Chicago Cubs | 3.2 | 3 | 0 | 0 | 1 | 0 |



### Home SP: Zack Wheeler (—)

| Stat | Value |
|---|---:|
| ERA | 2.01 |
| WHIP | 0.85 |
| K/9 | 8.90 |
| BB/9 | 2.15 |
| HR/9 | 1.01 |
| IP | 62.2 |
| H | 38 |
| R | 14 |
| HR | 7 |
| Risk Score | 9 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-04-25 | Atlanta Braves | 5.0 | 3 | 2 | 3 | 6 | 0 |
| 2026-05-01 | Miami Marlins | 6.0 | 3 | 1 | 2 | 8 | 0 |
| 2026-05-06 | Athletics | 6.1 | 5 | 3 | 1 | 4 | 1 |
| 2026-05-12 | Boston Red Sox | 7.1 | 6 | 1 | 0 | 4 | 0 |
| 2026-05-17 | Pittsburgh Pirates | 7.0 | 4 | 0 | 1 | 8 | 0 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| New York Mets | .233 | .671 | 309 | 81 | 10 |
| Philadelphia Phillies | .232 | .695 | 323 | 97 | 10 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| New York Mets | 4.07 | 1.28 | 1.01 | 8 |
| Philadelphia Phillies | 4.09 | 1.30 | 1.13 | 12 |

### Dissection Read

- First attack side: Home bats vs away SP
- Main pitcher concern: David Peterson
- Park/environment pressure: 15
- Offense pressure: 10
- Bullpen/staff pressure: 12
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 11. Toronto Blue Jays @ Chicago Cubs — Watch (73)

### Game Context

| Field | Value |
|---|---|
| Park | Wrigley Field |
| Time | 2026-06-21T18:20:00Z |
| Environment | 10 |
| Pitcher Risk | 17 |
| Offense | 16 |
| Bullpen | 14 |
| Matchup Pressure | 16 |
| Total | 73 |


### Away SP: Dylan Cease (—)

| Stat | Value |
|---|---:|
| ERA | 2.71 |
| WHIP | 1.19 |
| K/9 | 13.56 |
| BB/9 | 3.82 |
| HR/9 | 0.62 |
| IP | 73.0 |
| H | 56 |
| R | 25 |
| HR | 5 |
| Risk Score | 11 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-28 | Athletics | 5.1 | 3 | 1 | 2 | 12 | 0 |
| 2026-04-03 | Chicago White Sox | 4.1 | 5 | 2 | 3 | 6 | 0 |
| 2026-04-08 | Los Angeles Dodgers | 5.0 | 4 | 1 | 4 | 8 | 0 |
| 2026-04-15 | Milwaukee Brewers | 6.0 | 2 | 0 | 3 | 6 | 0 |
| 2026-04-20 | Los Angeles Angels | 5.0 | 5 | 2 | 2 | 12 | 0 |



### Home SP: Shota Imanaga (—)

| Stat | Value |
|---|---:|
| ERA | 4.26 |
| WHIP | 1.06 |
| K/9 | 8.72 |
| BB/9 | 2.28 |
| HR/9 | 1.77 |
| IP | 86.2 |
| H | 70 |
| R | 42 |
| HR | 17 |
| Risk Score | 17 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-29 | Washington Nationals | 5.0 | 6 | 4 | 2 | 7 | 1 |
| 2026-04-05 | Cleveland Guardians | 5.0 | 3 | 1 | 1 | 4 | 0 |
| 2026-04-10 | Pittsburgh Pirates | 6.0 | 0 | 0 | 1 | 9 | 0 |
| 2026-04-15 | Philadelphia Phillies | 6.0 | 3 | 1 | 1 | 11 | 1 |
| 2026-04-21 | Philadelphia Phillies | 7.0 | 3 | 1 | 1 | 1 | 1 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| Toronto Blue Jays | .249 | .702 | 316 | 77 | 12 |
| Chicago Cubs | .244 | .738 | 366 | 90 | 16 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| Toronto Blue Jays | 4.13 | 1.31 | 1.10 | 12 |
| Chicago Cubs | 4.28 | 1.24 | 1.49 | 14 |

### Dissection Read

- First attack side: Away bats vs home SP
- Main pitcher concern: Shota Imanaga
- Park/environment pressure: 10
- Offense pressure: 16
- Bullpen/staff pressure: 14
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 12. Chicago White Sox @ Detroit Tigers — Watch (65)

### Game Context

| Field | Value |
|---|---|
| Park | Comerica Park |
| Time | 2026-06-21T17:40:00Z |
| Environment | 11 |
| Pitcher Risk | 12 |
| Offense | 15 |
| Bullpen | 15 |
| Matchup Pressure | 12 |
| Total | 65 |


### Away SP: Davis Martin (—)

| Stat | Value |
|---|---:|
| ERA | 3.31 |
| WHIP | 1.19 |
| K/9 | 9.15 |
| BB/9 | 2.20 |
| HR/9 | 0.66 |
| IP | 81.2 |
| H | 77 |
| R | 30 |
| HR | 6 |
| Risk Score | 8 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-30 | Miami Marlins | 5.0 | 5 | 3 | 2 | 6 | 1 |
| 2026-04-05 | Toronto Blue Jays | 6.0 | 4 | 0 | 2 | 6 | 0 |
| 2026-04-10 | Kansas City Royals | 7.0 | 7 | 2 | 0 | 3 | 1 |
| 2026-04-17 | Athletics | 7.0 | 3 | 1 | 2 | 4 | 0 |
| 2026-04-23 | Arizona Diamondbacks | 6.1 | 6 | 1 | 1 | 7 | 0 |



### Home SP: Keider Montero (—)

| Stat | Value |
|---|---:|
| ERA | 3.67 |
| WHIP | 1.02 |
| K/9 | 6.11 |
| BB/9 | 2.08 |
| HR/9 | 0.98 |
| IP | 73.2 |
| H | 58 |
| R | 32 |
| HR | 8 |
| Risk Score | 12 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-04-05 | St. Louis Cardinals | 4.1 | 3 | 2 | 1 | 3 | 0 |
| 2026-04-10 | Miami Marlins | 6.0 | 2 | 0 | 1 | 7 | 0 |
| 2026-04-16 | Kansas City Royals | 6.0 | 7 | 4 | 0 | 5 | 0 |
| 2026-04-21 | Milwaukee Brewers | 5.2 | 5 | 3 | 1 | 3 | 0 |
| 2026-04-26 | Cincinnati Reds | 5.0 | 5 | 3 | 2 | 5 | 2 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| Chicago White Sox | .238 | .733 | 349 | 105 | 15 |
| Detroit Tigers | .233 | .705 | 309 | 85 | 12 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| Chicago White Sox | 4.41 | 1.33 | 1.18 | 15 |
| Detroit Tigers | 3.85 | 1.28 | 1.00 | 8 |

### Dissection Read

- First attack side: Away bats vs home SP
- Main pitcher concern: Keider Montero
- Park/environment pressure: 11
- Offense pressure: 15
- Bullpen/staff pressure: 15
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 13. San Diego Padres @ Texas Rangers — Watch (61)

### Game Context

| Field | Value |
|---|---|
| Park | Globe Life Field |
| Time | 2026-06-21T18:35:00Z |
| Environment | 14 |
| Pitcher Risk | 15 |
| Offense | 10 |
| Bullpen | 10 |
| Matchup Pressure | 12 |
| Total | 61 |


### Away SP: TBD (—)

| Stat | Value |
|---|---:|
| ERA | — |
| WHIP | — |
| K/9 | — |
| BB/9 | — |
| HR/9 | — |
| IP | — |
| H | — |
| R | — |
| HR | — |
| Risk Score | 8 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| — | — | — | — | — | — | — | — |



### Home SP: Nathan Eovaldi (—)

| Stat | Value |
|---|---:|
| ERA | 4.23 |
| WHIP | 1.17 |
| K/9 | 8.55 |
| BB/9 | 2.16 |
| HR/9 | 1.75 |
| IP | 87.1 |
| H | 81 |
| R | 43 |
| HR | 17 |
| Risk Score | 15 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-26 | Philadelphia Phillies | 4.2 | 8 | 5 | 0 | 7 | 2 |
| 2026-04-01 | Baltimore Orioles | 4.0 | 8 | 6 | 3 | 5 | 1 |
| 2026-04-07 | Seattle Mariners | 6.0 | 6 | 2 | 2 | 7 | 1 |
| 2026-04-13 | Athletics | 7.0 | 3 | 0 | 2 | 7 | 0 |
| 2026-04-18 | Seattle Mariners | 5.0 | 8 | 2 | 1 | 3 | 1 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| San Diego Padres | .219 | .656 | 293 | 78 | 8 |
| Texas Rangers | .241 | .704 | 305 | 77 | 10 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| San Diego Padres | 3.90 | 1.30 | 0.99 | 10 |
| Texas Rangers | 3.96 | 1.25 | 1.23 | 10 |

### Dissection Read

- First attack side: Away bats vs home SP
- Main pitcher concern: Nathan Eovaldi
- Park/environment pressure: 14
- Offense pressure: 10
- Bullpen/staff pressure: 10
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 14. St. Louis Cardinals @ Kansas City Royals — Watch (60)

### Game Context

| Field | Value |
|---|---|
| Park | Kauffman Stadium |
| Time | 2026-06-21T18:10:00Z |
| Environment | 8 |
| Pitcher Risk | 11 |
| Offense | 14 |
| Bullpen | 15 |
| Matchup Pressure | 12 |
| Total | 60 |


### Away SP: Dustin May (—)

| Stat | Value |
|---|---:|
| ERA | 3.75 |
| WHIP | 1.14 |
| K/9 | 8.27 |
| BB/9 | 2.31 |
| HR/9 | 0.55 |
| IP | 81.2 |
| H | 72 |
| R | 37 |
| HR | 5 |
| Risk Score | 10 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-29 | Tampa Bay Rays | 4.0 | 10 | 6 | 1 | 3 | 0 |
| 2026-04-04 | Detroit Tigers | 3.1 | 7 | 7 | 2 | 4 | 2 |
| 2026-04-10 | Boston Red Sox | 6.0 | 4 | 1 | 0 | 4 | 0 |
| 2026-04-15 | Cleveland Guardians | 6.0 | 6 | 1 | 1 | 4 | 0 |
| 2026-04-21 | Miami Marlins | 5.1 | 6 | 1 | 1 | 5 | 1 |



### Home SP: Stephen Kolek (—)

| Stat | Value |
|---|---:|
| ERA | 2.68 |
| WHIP | 1.03 |
| K/9 | 6.08 |
| BB/9 | 1.79 |
| HR/9 | 0.89 |
| IP | 50.1 |
| H | 42 |
| R | 18 |
| HR | 5 |
| Risk Score | 11 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-05-05 | Cleveland Guardians | 6.0 | 4 | 3 | 0 | 3 | 1 |
| 2026-05-12 | Chicago White Sox | 4.2 | 5 | 5 | 3 | 6 | 2 |
| 2026-05-17 | St. Louis Cardinals | 6.1 | 4 | 0 | 1 | 3 | 0 |
| 2026-05-23 | Seattle Mariners | 9.0 | 4 | 0 | 1 | 2 | 0 |
| 2026-05-29 | Texas Rangers | 5.0 | 6 | 4 | 1 | 5 | 1 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| St. Louis Cardinals | .247 | .721 | 337 | 83 | 14 |
| Kansas City Royals | .247 | .712 | 321 | 73 | 12 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| St. Louis Cardinals | 4.22 | 1.34 | 1.12 | 12 |
| Kansas City Royals | 4.48 | 1.38 | 1.23 | 15 |

### Dissection Read

- First attack side: Away bats vs home SP
- Main pitcher concern: Stephen Kolek
- Park/environment pressure: 8
- Offense pressure: 14
- Bullpen/staff pressure: 15
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.


---

## 15. Boston Red Sox @ Seattle Mariners — Low (55)

### Game Context

| Field | Value |
|---|---|
| Park | T-Mobile Park |
| Time | 2026-06-21T20:10:00Z |
| Environment | 10 |
| Pitcher Risk | 11 |
| Offense | 12 |
| Bullpen | 10 |
| Matchup Pressure | 12 |
| Total | 55 |


### Away SP: Payton Tolle (—)

| Stat | Value |
|---|---:|
| ERA | 2.93 |
| WHIP | 1.06 |
| K/9 | 9.26 |
| BB/9 | 2.47 |
| HR/9 | 0.77 |
| IP | 58.1 |
| H | 46 |
| R | 23 |
| HR | 5 |
| Risk Score | 8 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-04-23 | New York Yankees | 6.0 | 3 | 1 | 1 | 11 | 1 |
| 2026-04-28 | Toronto Blue Jays | 4.2 | 3 | 3 | 4 | 4 | 0 |
| 2026-05-04 | Detroit Tigers | 7.0 | 1 | 0 | 1 | 8 | 0 |
| 2026-05-10 | Tampa Bay Rays | 5.0 | 6 | 1 | 0 | 4 | 1 |
| 2026-05-16 | Atlanta Braves | 8.0 | 4 | 2 | 1 | 3 | 1 |



### Home SP: Logan Gilbert (—)

| Stat | Value |
|---|---:|
| ERA | 3.43 |
| WHIP | 1.03 |
| K/9 | 9.55 |
| BB/9 | 2.08 |
| HR/9 | 1.35 |
| IP | 86.2 |
| H | 69 |
| R | 33 |
| HR | 13 |
| Risk Score | 11 |

#### Last 5 Starts / Appearances

| Date | Opponent | IP | H | ER | BB | K | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-03-26 | Cleveland Guardians | 5.1 | 5 | 3 | 0 | 7 | 1 |
| 2026-03-31 | New York Yankees | 5.1 | 7 | 5 | 3 | 6 | 0 |
| 2026-04-06 | Texas Rangers | 6.0 | 6 | 2 | 0 | 5 | 0 |
| 2026-04-12 | Houston Astros | 7.0 | 4 | 1 | 1 | 7 | 1 |
| 2026-04-17 | Texas Rangers | 5.1 | 7 | 2 | 1 | 7 | 1 |


### Team Offense

| Team | AVG | OPS | Runs | HR | Attack Score |
|---|---:|---:|---:|---:|---:|
| Boston Red Sox | .244 | .694 | 293 | 63 | 8 |
| Seattle Mariners | .232 | .701 | 323 | 97 | 12 |

### Bullpen / Staff Context

| Team | ERA | WHIP | HR/9 | Bullpen/Staff Stress |
|---|---:|---:|---:|---:|
| Boston Red Sox | 3.86 | 1.26 | 1.12 | 10 |
| Seattle Mariners | 3.66 | 1.18 | 0.99 | 8 |

### Dissection Read

- First attack side: Away bats vs home SP
- Main pitcher concern: Logan Gilbert
- Park/environment pressure: 10
- Offense pressure: 12
- Bullpen/staff pressure: 10
- Research direction: inspect confirmed lineups, pitch mix, hitter handedness, and prop market for this game.



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
