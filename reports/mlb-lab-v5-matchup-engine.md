# MLB-LAB V5.1 Pitch Matchup Engine

Date: 2026-06-24

This runner uses:
- MLB Stats API for slate, teams, parks, probable pitchers
- Baseball Savant / Statcast for pitcher arsenal, L/R splits, hitter pools, hitter-vs-pitch matchups
- MLB Stats API boxscores for bullpen usage/fatigue over the last 4 days

Removed:
- FanGraphs hard dependency
- sportsbook odds
- CSV dependency
- scoring gimmicks
- weak-pitch labels
- manual placeholder tables

---

# Slate

| # | Game | Park | Away SP | Home SP |
|---:|---|---|---|---|
| 1 | Texas Rangers @ Miami Marlins | loanDepot park | Jacob deGrom | Eury Pérez |
| 2 | Chicago Cubs @ New York Mets | Citi Field | Javier Assad | Nolan McLean |
| 3 | Chicago Cubs @ New York Mets | Citi Field | Shota Imanaga | Sean Manaea |
| 4 | Cleveland Guardians @ Chicago White Sox | Rate Field | Tanner Bibee | Erick Fedde |
| 5 | Boston Red Sox @ Colorado Rockies | Coors Field | Ranger Suarez | Kyle Freeland |
| 6 | Baltimore Orioles @ Los Angeles Angels | Angel Stadium | Trey Gibson | José Soriano |
| 7 | Seattle Mariners @ Pittsburgh Pirates | PNC Park | Bryan Woo | Braxton Ashcraft |
| 8 | Kansas City Royals @ Tampa Bay Rays | Tropicana Field | Noah Cameron | Griffin Jax |
| 9 | New York Yankees @ Detroit Tigers | Comerica Park | Ryan Weathers | Tarik Skubal |
| 10 | Philadelphia Phillies @ Washington Nationals | Nationals Park | Aaron Nola | Carson Palmquist |
| 11 | Houston Astros @ Toronto Blue Jays | Rogers Centre | Mike Burrows | Trey Yesavage |
| 12 | Milwaukee Brewers @ Cincinnati Reds | Great American Ball Park | Shane Drohan | Rhett Lowder |
| 13 | Los Angeles Dodgers @ Minnesota Twins | Target Field | Shohei Ohtani | Joe Ryan |
| 14 | Arizona Diamondbacks @ St. Louis Cardinals | Busch Stadium | Mitch Bratt | Matthew Liberatore |
| 15 | Atlanta Braves @ San Diego Padres | Petco Park | Martín Pérez | JP Sears |
| 16 | Athletics @ San Francisco Giants | Oracle Park | Gage Jump | Tyler Mahle |

---

# Full Game Breakdown Cards

---

# 1. Texas Rangers @ Miami Marlins

## Game Context

| Field | Value |
| --- | --- |
| Park | loanDepot park |
| Time | 2026-06-24T16:10:00Z |
| Away Team | Texas Rangers |
| Home Team | Miami Marlins |
| Away Probable Pitcher | Jacob deGrom |
| Home Probable Pitcher | Eury Pérez |


## Away Starting Pitcher: Jacob deGrom

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1346 |
| Batted/Result Events | 335 |
| Hits Allowed | 67 |
| Walks | 18 |
| Strikeouts | 98 |
| Home Runs | 15 |
| K Event Rate | 29.3% |
| BB Event Rate | 5.4% |
| HR Event Rate | 4.5% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | TEX | 9.0 | 6 | 2 | 2 | 9 | 2 |
| 2026-06-13 | BOS | 7.7 | 6 | 0 | 0 | 5 | 0 |
| 2026-06-07 | TEX | 7.7 | 3 | 0 | 2 | 6 | 0 |
| 2026-06-01 | STL | 7.0 | 4 | 0 | 1 | 8 | 0 |
| 2026-05-27 | TEX | 7.7 | 4 | 1 | 1 | 6 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 12.3% | 166 | 0.147 | 0.147 | 0.000 | 0.132 | 0.210 | 0.0% | 26.5% | 45.6% |
| CH | vs R | 1.6% | 21 | 0.375 | 0.500 | 0.125 | 0.494 | 0.290 | 16.7% | 25.0% | 25.0% |
| CU | vs L | 4.8% | 65 | 0.400 | 1.000 | 0.600 | 0.580 | 0.313 | 14.3% | 45.5% | 40.0% |
| CU | vs R | 1.5% | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.066 | 0.0% | 50.0% | 53.8% |
| FF | vs L | 25.3% | 340 | 0.214 | 0.476 | 0.262 | 0.316 | 0.351 | 15.6% | 26.9% | 22.3% |
| FF | vs R | 17.7% | 238 | 0.312 | 0.604 | 0.292 | 0.400 | 0.384 | 14.3% | 24.7% | 19.5% |
| SI | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs R | 1.6% | 22 | 0.600 | 1.400 | 0.800 | 1.010 | 0.409 | 20.0% | 30.0% | 15.4% |
| SL | vs L | 14.9% | 200 | 0.167 | 0.241 | 0.074 | 0.225 | 0.253 | 3.0% | 31.1% | 33.3% |
| SL | vs R | 19.7% | 265 | 0.149 | 0.194 | 0.045 | 0.182 | 0.250 | 2.4% | 15.3% | 44.9% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 110 | 6 | 3 | 9 | 2 |
| 2026-06-13 | 90 | 6 | 0 | 5 | 0 |
| 2026-06-07 | 87 | 3 | 2 | 6 | 0 |
| 2026-06-01 | 91 | 4 | 1 | 8 | 0 |
| 2026-05-27 | 97 | 4 | 1 | 6 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Liam Hicks | 31 | 0.333 | 0.852 | 0.519 | 0.477 | 0.281 | 8.3% | 37.8% | 22.4% |
| SL | Kyle Stowers | 34 | 0.233 | 0.600 | 0.367 | 0.385 | 0.376 | 16.7% | 26.3% | 36.9% |
| SL | Heriberto Hernandez | 34 | 0.414 | 0.724 | 0.310 | 0.518 | 0.438 | 15.0% | 35.5% | 42.6% |
| CH | Owen Caissie | 31 | 0.310 | 0.621 | 0.310 | 0.389 | 0.299 | 20.0% | 17.1% | 42.2% |
| FF | Xavier Edwards | 111 | 0.383 | 0.670 | 0.287 | 0.481 | 0.420 | 8.9% | 19.4% | 6.8% |
| FF | Joe Mack | 30 | 0.321 | 0.571 | 0.250 | 0.402 | 0.338 | 5.0% | 27.5% | 9.8% |
| FF | Owen Caissie | 61 | 0.216 | 0.451 | 0.235 | 0.325 | 0.333 | 20.0% | 22.6% | 22.7% |
| SL | Javier Sanoja | 36 | 0.333 | 0.556 | 0.222 | 0.454 | 0.232 | 3.1% | 15.7% | 18.5% |
| CH | Liam Hicks | 42 | 0.341 | 0.537 | 0.195 | 0.390 | 0.291 | 2.6% | 19.6% | 13.9% |
| FF | Otto Lopez | 77 | 0.377 | 0.565 | 0.188 | 0.428 | 0.428 | 12.5% | 33.6% | 6.0% |
| CH | Heriberto Hernandez | 16 | 0.188 | 0.375 | 0.188 | 0.294 | 0.307 | 11.1% | 18.8% | 39.3% |
| FF | Connor Norby | 76 | 0.219 | 0.391 | 0.172 | 0.340 | 0.288 | 16.7% | 22.3% | 31.5% |
| FF | Liam Hicks | 106 | 0.207 | 0.379 | 0.172 | 0.325 | 0.360 | 6.0% | 22.4% | 5.4% |
| SL | Connor Norby | 32 | 0.267 | 0.433 | 0.167 | 0.325 | 0.239 | 12.5% | 22.9% | 41.8% |
| CH | Joe Mack | 20 | 0.158 | 0.316 | 0.158 | 0.225 | 0.286 | 11.1% | 40.0% | 54.8% |
| SL | Owen Caissie | 29 | 0.154 | 0.308 | 0.154 | 0.260 | 0.263 | 11.8% | 29.4% | 36.2% |
| FF | Heriberto Hernandez | 47 | 0.200 | 0.350 | 0.150 | 0.288 | 0.402 | 9.1% | 42.4% | 24.1% |
| SL | Otto Lopez | 63 | 0.393 | 0.541 | 0.148 | 0.433 | 0.348 | 5.6% | 26.1% | 28.4% |
| FF | Kyle Stowers | 79 | 0.222 | 0.361 | 0.139 | 0.290 | 0.327 | 11.3% | 29.7% | 30.3% |
| CH | Jakob Marsee | 32 | 0.300 | 0.433 | 0.133 | 0.353 | 0.362 | 4.2% | 37.5% | 26.2% |
| CH | Kyle Stowers | 34 | 0.212 | 0.333 | 0.121 | 0.274 | 0.199 | 5.3% | 31.4% | 40.6% |
| FF | Javier Sanoja | 50 | 0.244 | 0.356 | 0.111 | 0.304 | 0.287 | 2.5% | 26.0% | 11.5% |
| SL | Xavier Edwards | 40 | 0.222 | 0.333 | 0.111 | 0.269 | 0.291 | 7.7% | 20.4% | 24.3% |
| FF | Jakob Marsee | 121 | 0.190 | 0.300 | 0.110 | 0.295 | 0.317 | 3.8% | 18.8% | 7.3% |
| CH | Otto Lopez | 41 | 0.256 | 0.359 | 0.103 | 0.255 | 0.161 | 3.3% | 12.0% | 26.9% |
| CH | Agustín Ramírez | 11 | 0.300 | 0.400 | 0.100 | 0.341 | 0.261 | 0.0% | 35.7% | 51.7% |
| SL | Jakob Marsee | 34 | 0.129 | 0.226 | 0.097 | 0.226 | 0.212 | 0.0% | 16.7% | 35.8% |
| FF | Graham Pauley | 37 | 0.152 | 0.242 | 0.091 | 0.250 | 0.210 | 4.2% | 14.3% | 13.1% |
| SL | Graham Pauley | 11 | 0.091 | 0.182 | 0.091 | 0.114 | 0.103 | 0.0% | 21.4% | 28.6% |
| CH | Javier Sanoja | 23 | 0.318 | 0.409 | 0.091 | 0.313 | 0.158 | 0.0% | 10.5% | 15.6% |


## Home Starting Pitcher: Eury Pérez

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1198 |
| Batted/Result Events | 298 |
| Hits Allowed | 55 |
| Walks | 30 |
| Strikeouts | 82 |
| Home Runs | 11 |
| K Event Rate | 27.5% |
| BB Event Rate | 10.1% |
| HR Event Rate | 3.7% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-27 | TOR | 5.0 | 3 | 0 | 1 | 9 | 0 |
| 2026-05-22 | MIA | 6.7 | 2 | 1 | 0 | 5 | 1 |
| 2026-05-17 | TB | 7.7 | 5 | 2 | 4 | 5 | 2 |
| 2026-05-12 | MIN | 8.3 | 3 | 1 | 4 | 8 | 1 |
| 2026-05-06 | MIA | 8.0 | 4 | 1 | 6 | 6 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 7.9% | 95 | 0.118 | 0.118 | 0.000 | 0.147 | 0.168 | 9.1% | 11.8% | 46.3% |
| CH | vs R | 2.8% | 34 | 0.429 | 1.286 | 0.857 | 0.700 | 0.833 | 33.3% | 37.5% | 27.3% |
| CU | vs L | 5.5% | 66 | 0.273 | 0.364 | 0.091 | 0.358 | 0.439 | 9.1% | 43.8% | 29.2% |
| CU | vs R | 1.3% | 16 | 0.000 | 0.000 | 0.000 | 0.233 | 0.516 | 0.0% | 50.0% | 60.0% |
| FF | vs L | 27.8% | 333 | 0.233 | 0.422 | 0.189 | 0.338 | 0.339 | 14.5% | 21.1% | 25.0% |
| FF | vs R | 19.5% | 234 | 0.194 | 0.355 | 0.161 | 0.299 | 0.322 | 8.9% | 24.5% | 15.6% |
| SI | vs L | 2.0% | 24 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 14.3% |
| SI | vs R | 3.7% | 44 | 0.429 | 0.571 | 0.143 | 0.546 | 0.483 | 0.0% | 13.3% | 25.0% |
| SL | vs L | 6.8% | 81 | 0.000 | 0.000 | 0.000 | 0.131 | 0.304 | 0.0% | 25.0% | 30.3% |
| SL | vs R | 8.3% | 99 | 0.250 | 0.688 | 0.438 | 0.403 | 0.479 | 30.8% | 31.8% | 48.9% |
| ST | vs L | 5.6% | 67 | 0.400 | 0.700 | 0.300 | 0.465 | 0.299 | 25.0% | 9.5% | 19.2% |
| ST | vs R | 8.7% | 104 | 0.111 | 0.333 | 0.222 | 0.200 | 0.245 | 12.5% | 14.7% | 34.5% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-05-27 | 73 | 3 | 0 | 9 | 0 |
| 2026-05-22 | 86 | 2 | 0 | 5 | 1 |
| 2026-05-17 | 102 | 5 | 4 | 5 | 2 |
| 2026-05-12 | 87 | 3 | 3 | 8 | 1 |
| 2026-05-06 | 93 | 4 | 5 | 6 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | Kyle Higashioka | 11 | 0.333 | 0.778 | 0.444 | 0.505 | 0.358 | 20.0% | 40.0% | 41.7% |
| ST | Brandon Nimmo | 15 | 0.214 | 0.571 | 0.357 | 0.347 | 0.441 | 33.3% | 29.6% | 27.5% |
| ST | Ezequiel Duran | 37 | 0.343 | 0.686 | 0.343 | 0.409 | 0.353 | 10.7% | 34.9% | 24.2% |
| CH | Corey Seager | 31 | 0.241 | 0.552 | 0.310 | 0.384 | 0.390 | 20.0% | 37.9% | 31.2% |
| ST | Evan Carter | 12 | 0.200 | 0.500 | 0.300 | 0.358 | 0.297 | 25.0% | 26.7% | 29.6% |
| SL | Danny Jansen | 14 | 0.214 | 0.500 | 0.286 | 0.296 | 0.155 | 11.1% | 15.8% | 27.3% |
| ST | Joc Pederson | 14 | 0.273 | 0.545 | 0.273 | 0.421 | 0.311 | 16.7% | 25.0% | 40.9% |
| CH | Danny Jansen | 12 | 0.364 | 0.636 | 0.273 | 0.446 | 0.278 | 0.0% | 15.4% | 36.4% |
| FF | Joc Pederson | 82 | 0.265 | 0.529 | 0.265 | 0.397 | 0.412 | 16.3% | 37.8% | 25.0% |
| SL | Ezequiel Duran | 35 | 0.344 | 0.594 | 0.250 | 0.424 | 0.246 | 0.0% | 18.2% | 38.3% |
| CH | Wyatt Langford | 12 | 0.167 | 0.417 | 0.250 | 0.242 | 0.313 | 11.1% | 36.8% | 31.2% |
| FF | Corey Seager | 55 | 0.156 | 0.378 | 0.222 | 0.295 | 0.296 | 21.4% | 23.1% | 29.7% |
| FF | Josh Jung | 83 | 0.292 | 0.514 | 0.222 | 0.401 | 0.370 | 14.3% | 29.5% | 12.5% |
| CH | Jake Burger | 36 | 0.281 | 0.500 | 0.219 | 0.354 | 0.349 | 9.5% | 25.0% | 38.6% |
| FF | Evan Carter | 83 | 0.186 | 0.400 | 0.214 | 0.312 | 0.355 | 11.7% | 22.0% | 13.8% |
| SL | Joc Pederson | 33 | 0.276 | 0.483 | 0.207 | 0.370 | 0.322 | 18.8% | 36.1% | 39.1% |
| SL | Brandon Nimmo | 46 | 0.220 | 0.415 | 0.195 | 0.300 | 0.381 | 14.3% | 33.9% | 26.1% |
| FF | Brandon Nimmo | 113 | 0.278 | 0.464 | 0.186 | 0.365 | 0.340 | 5.3% | 25.5% | 16.7% |
| CH | Josh Jung | 32 | 0.429 | 0.607 | 0.179 | 0.481 | 0.322 | 4.5% | 36.1% | 21.2% |
| CH | Joc Pederson | 40 | 0.205 | 0.385 | 0.179 | 0.261 | 0.314 | 6.2% | 34.0% | 31.4% |
| SL | Jake Burger | 58 | 0.226 | 0.396 | 0.170 | 0.315 | 0.223 | 7.3% | 28.6% | 43.0% |
| FF | Ezequiel Duran | 66 | 0.169 | 0.339 | 0.169 | 0.265 | 0.270 | 13.2% | 17.5% | 26.8% |
| SL | Evan Carter | 29 | 0.167 | 0.333 | 0.167 | 0.271 | 0.265 | 5.9% | 39.3% | 34.1% |
| FF | Wyatt Langford | 54 | 0.280 | 0.440 | 0.160 | 0.339 | 0.270 | 5.4% | 14.5% | 16.3% |
| SL | Wyatt Langford | 25 | 0.240 | 0.400 | 0.160 | 0.274 | 0.251 | 10.0% | 27.6% | 11.1% |
| FF | Jake Burger | 84 | 0.187 | 0.320 | 0.133 | 0.268 | 0.293 | 5.6% | 38.3% | 26.5% |
| FF | Danny Jansen | 58 | 0.133 | 0.267 | 0.133 | 0.287 | 0.301 | 10.3% | 29.2% | 21.8% |
| CH | Ezequiel Duran | 25 | 0.333 | 0.458 | 0.125 | 0.394 | 0.325 | 0.0% | 16.7% | 13.2% |
| CH | Evan Carter | 42 | 0.081 | 0.189 | 0.108 | 0.182 | 0.158 | 0.0% | 18.9% | 38.7% |
| SL | Corey Seager | 32 | 0.107 | 0.214 | 0.107 | 0.206 | 0.243 | 6.2% | 14.3% | 51.5% |


## Texas Rangers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brandon Nimmo | 351 | 0.268 | 0.433 | 0.166 | 0.340 | 0.378 | 11.9% | 31.1% | 18.3% |
| Josh Jung | 330 | 0.301 | 0.455 | 0.154 | 0.360 | 0.349 | 5.6% | 29.7% | 17.0% |
| Jake Burger | 325 | 0.254 | 0.447 | 0.193 | 0.339 | 0.311 | 9.5% | 32.1% | 32.3% |
| Ezequiel Duran | 272 | 0.266 | 0.435 | 0.169 | 0.338 | 0.306 | 7.1% | 22.4% | 24.4% |
| Joc Pederson | 260 | 0.238 | 0.435 | 0.197 | 0.341 | 0.345 | 10.3% | 31.0% | 28.7% |
| Evan Carter | 241 | 0.168 | 0.307 | 0.139 | 0.276 | 0.294 | 6.8% | 23.0% | 24.9% |
| Corey Seager | 221 | 0.188 | 0.375 | 0.188 | 0.293 | 0.335 | 16.3% | 27.2% | 31.7% |
| Wyatt Langford | 176 | 0.265 | 0.469 | 0.204 | 0.343 | 0.296 | 7.2% | 25.5% | 19.3% |
| Kyle Higashioka | 158 | 0.238 | 0.392 | 0.154 | 0.322 | 0.294 | 10.1% | 27.8% | 28.1% |
| Alejandro Osuna | 152 | 0.269 | 0.308 | 0.038 | 0.335 | 0.321 | 0.9% | 21.3% | 12.5% |
| Danny Jansen | 152 | 0.176 | 0.321 | 0.145 | 0.274 | 0.254 | 6.8% | 25.1% | 24.0% |
| Josh Smith | 137 | 0.214 | 0.239 | 0.026 | 0.268 | 0.284 | 4.4% | 24.9% | 19.0% |


## Miami Marlins Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Otto Lopez | 349 | 0.332 | 0.471 | 0.138 | 0.383 | 0.333 | 6.9% | 29.5% | 18.8% |
| Xavier Edwards | 346 | 0.291 | 0.427 | 0.136 | 0.357 | 0.327 | 5.0% | 19.1% | 14.5% |
| Jakob Marsee | 333 | 0.194 | 0.294 | 0.100 | 0.291 | 0.305 | 3.5% | 22.3% | 17.5% |
| Liam Hicks | 305 | 0.269 | 0.451 | 0.182 | 0.353 | 0.317 | 4.2% | 23.9% | 10.5% |
| Connor Norby | 244 | 0.214 | 0.348 | 0.133 | 0.306 | 0.282 | 9.4% | 21.6% | 29.4% |
| Kyle Stowers | 241 | 0.227 | 0.422 | 0.194 | 0.328 | 0.327 | 10.6% | 30.0% | 33.4% |
| Owen Caissie | 224 | 0.223 | 0.416 | 0.193 | 0.312 | 0.295 | 14.7% | 23.5% | 32.9% |
| Javier Sanoja | 196 | 0.246 | 0.350 | 0.104 | 0.304 | 0.261 | 1.2% | 21.2% | 11.9% |
| Heriberto Hernandez | 179 | 0.245 | 0.428 | 0.182 | 0.344 | 0.356 | 9.5% | 32.8% | 31.5% |
| Agustín Ramírez | 141 | 0.228 | 0.350 | 0.122 | 0.305 | 0.282 | 5.3% | 27.0% | 30.9% |
| Joe Mack | 128 | 0.259 | 0.405 | 0.147 | 0.324 | 0.319 | 9.4% | 25.4% | 20.5% |
| Graham Pauley | 100 | 0.152 | 0.250 | 0.098 | 0.225 | 0.190 | 2.9% | 15.2% | 19.6% |


## Bullpen Fatigue Report

### Texas Rangers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Cole Winn | 2026-06-20 | 0.2 | 14 |
| Jacob Latz | 2026-06-20 | 1.0 | 13 |
| Jacob Latz | 2026-06-22 | 1.1 | 31 |
| Jakob Junis | 2026-06-21 | 1.0 | 15 |
| Jakob Junis | 2026-06-22 | 0.2 | 17 |
| Joe Ross | 2026-06-20 | 1.0 | 21 |
| Joe Ross | 2026-06-23 | 2.2 | 30 |
| Jose Corniell | 2026-06-23 | 3.1 | 69 |
| Kumar Rocker | 2026-06-22 | 5.0 | 76 |
| Peyton Gray | 2026-06-20 | 1.0 | 15 |
| Peyton Gray | 2026-06-21 | 1.0 | 11 |
| Robby Ahlstrom | 2026-06-21 | 1.0 | 12 |
| Robby Ahlstrom | 2026-06-22 | 1.0 | 8 |
| Tyler Alexander | 2026-06-20 | 0.1 | 9 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Joe Ross, Jose Corniell


### Miami Marlins Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Anthony Bender | 2026-06-20 | 0.2 | 13 |
| Anthony Bender | 2026-06-22 | 0.1 | 7 |
| Cade Gibson | 2026-06-20 | 1.0 | 25 |
| Calvin Faucher | 2026-06-21 | 1.1 | 12 |
| Calvin Faucher | 2026-06-22 | 1.0 | 24 |
| Dax Fulton | 2026-06-22 | 1.0 | 16 |
| John King | 2026-06-21 | 1.1 | 10 |
| Lake Bachar | 2026-06-21 | 1.0 | 11 |
| Lake Bachar | 2026-06-23 | 0.2 | 8 |
| Michael Petersen | 2026-06-21 | 1.0 | 16 |
| Michael Petersen | 2026-06-22 | 0.2 | 13 |
| Pete Fairbanks | 2026-06-20 | 1.0 | 15 |
| Pete Fairbanks | 2026-06-23 | 1.0 | 17 |
| Tyler Zuber | 2026-06-20 | 1.1 | 22 |
| Tyler Zuber | 2026-06-23 | 0.2 | 18 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Lake Bachar, Pete Fairbanks, Tyler Zuber



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Brandon Nimmo | 351 | 0.268 | 0.433 | 0.166 | 0.340 | 11.9% | 31.1% |
| 2 | Josh Jung | 330 | 0.301 | 0.455 | 0.154 | 0.360 | 5.6% | 29.7% |
| 3 | Jake Burger | 325 | 0.254 | 0.447 | 0.193 | 0.339 | 9.5% | 32.1% |
| 4 | Ezequiel Duran | 272 | 0.266 | 0.435 | 0.169 | 0.338 | 7.1% | 22.4% |
| 5 | Joc Pederson | 260 | 0.238 | 0.435 | 0.197 | 0.341 | 10.3% | 31.0% |
| 6 | Evan Carter | 241 | 0.168 | 0.307 | 0.139 | 0.276 | 6.8% | 23.0% |
| 7 | Corey Seager | 221 | 0.188 | 0.375 | 0.188 | 0.293 | 16.3% | 27.2% |
| 8 | Wyatt Langford | 176 | 0.265 | 0.469 | 0.204 | 0.343 | 7.2% | 25.5% |
| 9 | Kyle Higashioka | 158 | 0.238 | 0.392 | 0.154 | 0.322 | 10.1% | 27.8% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Otto Lopez | 349 | 0.332 | 0.471 | 0.138 | 0.383 | 6.9% | 29.5% |
| 2 | Xavier Edwards | 346 | 0.291 | 0.427 | 0.136 | 0.357 | 5.0% | 19.1% |
| 3 | Jakob Marsee | 333 | 0.194 | 0.294 | 0.100 | 0.291 | 3.5% | 22.3% |
| 4 | Liam Hicks | 305 | 0.269 | 0.451 | 0.182 | 0.353 | 4.2% | 23.9% |
| 5 | Connor Norby | 244 | 0.214 | 0.348 | 0.133 | 0.306 | 9.4% | 21.6% |
| 6 | Kyle Stowers | 241 | 0.227 | 0.422 | 0.194 | 0.328 | 10.6% | 30.0% |
| 7 | Owen Caissie | 224 | 0.223 | 0.416 | 0.193 | 0.312 | 14.7% | 23.5% |
| 8 | Javier Sanoja | 196 | 0.246 | 0.350 | 0.104 | 0.304 | 1.2% | 21.2% |
| 9 | Heriberto Hernandez | 179 | 0.245 | 0.428 | 0.182 | 0.344 | 9.5% | 32.8% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6489 |
| Hits Allowed | 1383 |
| Walks/HBP | 627 |
| Strikeouts | 1474 |
| Home Runs Allowed | 195 |
| K Event Rate | 22.7% |
| BB/HBP Event Rate | 9.7% |
| HR Event Rate | 3.0% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6472 |
| Hits Allowed | 1351 |
| Walks/HBP | 665 |
| Strikeouts | 1465 |
| Home Runs Allowed | 158 |
| K Event Rate | 22.6% |
| BB/HBP Event Rate | 10.3% |
| HR Event Rate | 2.4% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL, CH
- Home pitcher pitch mix to inspect: FF, SL, ST, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 2. Chicago Cubs @ New York Mets

## Game Context

| Field | Value |
| --- | --- |
| Park | Citi Field |
| Time | 2026-06-24T17:10:00Z |
| Away Team | Chicago Cubs |
| Home Team | New York Mets |
| Away Probable Pitcher | Javier Assad |
| Home Probable Pitcher | Nolan McLean |


## Away Starting Pitcher: Javier Assad

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 717 |
| Batted/Result Events | 186 |
| Hits Allowed | 39 |
| Walks | 10 |
| Strikeouts | 28 |
| Home Runs | 6 |
| K Event Rate | 15.1% |
| BB Event Rate | 5.4% |
| HR Event Rate | 3.2% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-17 | CHC | 7.3 | 5 | 2 | 0 | 1 | 2 |
| 2026-06-12 | SF | 7.0 | 3 | 0 | 1 | 5 | 0 |
| 2026-06-07 | CHC | 7.0 | 1 | 0 | 2 | 5 | 0 |
| 2026-05-15 | CWS | 2.7 | 3 | 1 | 0 | 1 | 1 |
| 2026-05-08 | TEX | 4.0 | 1 | 0 | 1 | 1 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 8.1% | 58 | 0.235 | 0.588 | 0.353 | 0.341 | 0.347 | 16.7% | 33.3% | 33.3% |
| CU | vs L | 7.4% | 53 | 0.000 | 0.000 | 0.000 | 0.200 | 0.267 | 0.0% | 10.0% | 0.0% |
| CU | vs R | 0.3% | 2 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| FC | vs L | 10.9% | 78 | 0.300 | 0.700 | 0.400 | 0.441 | 0.500 | 20.0% | 32.3% | 11.1% |
| FC | vs R | 5.4% | 39 | 0.000 | 0.000 | 0.000 | 0.229 | 0.188 | 16.7% | 15.4% | 18.8% |
| FF | vs L | 15.5% | 111 | 0.259 | 0.481 | 0.222 | 0.337 | 0.408 | 3.8% | 25.0% | 10.7% |
| FF | vs R | 1.5% | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 0.0% |
| SI | vs L | 11.4% | 82 | 0.308 | 0.500 | 0.192 | 0.371 | 0.324 | 10.5% | 41.4% | 7.7% |
| SI | vs R | 26.9% | 193 | 0.250 | 0.304 | 0.054 | 0.273 | 0.299 | 1.9% | 36.2% | 5.4% |
| SL | vs L | 0.6% | 4 | 1.000 | 1.000 | 0.000 | 0.900 | 0.471 | 0.0% | 0.0% | 0.0% |
| SL | vs R | 3.9% | 28 | 0.100 | 0.100 | 0.000 | 0.090 | 0.188 | 0.0% | 22.2% | 25.0% |
| ST | vs L | 0.3% | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.168 | 0.0% | 0.0% | 0.0% |
| ST | vs R | 7.8% | 56 | 0.091 | 0.091 | 0.000 | 0.082 | 0.074 | 0.0% | 22.2% | 45.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-17 | 92 | 5 | 0 | 1 | 2 |
| 2026-06-12 | 85 | 3 | 1 | 5 | 0 |
| 2026-06-07 | 72 | 1 | 1 | 5 | 0 |
| 2026-05-15 | 39 | 3 | 0 | 1 | 1 |
| 2026-05-08 | 41 | 1 | 1 | 1 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | A. J. Ewing | 6 | 0.500 | 1.500 | 1.000 | 0.775 | 0.469 | 0.0% | 16.7% | 0.0% |
| ST | Mj Melendez | 11 | 0.200 | 0.600 | 0.400 | 0.359 | 0.296 | 16.7% | 35.7% | 17.6% |
| FC | Juan Soto | 11 | 0.375 | 0.750 | 0.375 | 0.473 | 0.279 | 0.0% | 20.0% | 27.3% |
| FF | Juan Soto | 73 | 0.303 | 0.667 | 0.364 | 0.434 | 0.480 | 21.8% | 33.3% | 13.4% |
| ST | Juan Soto | 27 | 0.320 | 0.640 | 0.320 | 0.426 | 0.466 | 21.1% | 33.3% | 27.0% |
| CH | Francisco Álvarez | 17 | 0.375 | 0.688 | 0.312 | 0.465 | 0.370 | 15.4% | 35.3% | 29.2% |
| SI | Marcus Semien | 76 | 0.284 | 0.552 | 0.269 | 0.368 | 0.395 | 10.5% | 28.1% | 11.8% |
| CH | Mark Vientos | 39 | 0.278 | 0.528 | 0.250 | 0.350 | 0.321 | 7.4% | 31.1% | 29.2% |
| FF | Mj Melendez | 55 | 0.196 | 0.435 | 0.239 | 0.325 | 0.246 | 7.4% | 24.3% | 32.2% |
| FC | Mark Vientos | 14 | 0.385 | 0.615 | 0.231 | 0.450 | 0.391 | 8.3% | 25.0% | 33.3% |
| FC | Carson Benge | 28 | 0.296 | 0.519 | 0.222 | 0.393 | 0.523 | 14.8% | 33.3% | 2.4% |
| FC | Bo Bichette | 15 | 0.143 | 0.357 | 0.214 | 0.300 | 0.434 | 16.7% | 22.6% | 17.9% |
| SI | Mark Vientos | 40 | 0.205 | 0.410 | 0.205 | 0.270 | 0.320 | 7.9% | 30.2% | 11.8% |
| FC | Marcus Semien | 17 | 0.333 | 0.533 | 0.200 | 0.371 | 0.387 | 13.3% | 17.1% | 22.4% |
| ST | Bo Bichette | 32 | 0.226 | 0.419 | 0.194 | 0.288 | 0.319 | 13.6% | 20.0% | 32.9% |
| FF | Tyrone Taylor | 29 | 0.231 | 0.423 | 0.192 | 0.269 | 0.176 | 0.0% | 10.9% | 13.0% |
| SI | Luis Torrens | 30 | 0.259 | 0.444 | 0.185 | 0.340 | 0.365 | 4.0% | 24.0% | 8.3% |
| SI | A. J. Ewing | 25 | 0.227 | 0.409 | 0.182 | 0.300 | 0.265 | 0.0% | 27.3% | 21.3% |
| CH | Luis Torrens | 12 | 0.273 | 0.455 | 0.182 | 0.300 | 0.233 | 0.0% | 27.3% | 15.8% |
| FF | Carson Benge | 108 | 0.312 | 0.490 | 0.177 | 0.393 | 0.384 | 8.5% | 22.1% | 18.8% |
| FF | A. J. Ewing | 43 | 0.235 | 0.412 | 0.176 | 0.369 | 0.401 | 11.5% | 20.0% | 10.4% |
| FF | Marcus Semien | 88 | 0.211 | 0.382 | 0.171 | 0.297 | 0.361 | 14.5% | 30.1% | 17.1% |
| FF | Bo Bichette | 88 | 0.231 | 0.397 | 0.167 | 0.317 | 0.340 | 5.3% | 26.9% | 11.4% |
| CH | Juan Soto | 25 | 0.320 | 0.480 | 0.160 | 0.346 | 0.407 | 8.3% | 40.0% | 4.9% |
| FF | Francisco Lindor | 46 | 0.179 | 0.333 | 0.154 | 0.311 | 0.395 | 8.8% | 27.4% | 13.3% |
| SI | Juan Soto | 56 | 0.292 | 0.438 | 0.146 | 0.383 | 0.396 | 14.0% | 37.7% | 13.7% |
| ST | Carson Benge | 22 | 0.238 | 0.381 | 0.143 | 0.286 | 0.281 | 10.0% | 25.9% | 33.3% |
| CH | Carson Benge | 30 | 0.207 | 0.345 | 0.138 | 0.280 | 0.315 | 8.3% | 27.0% | 24.1% |
| CH | Francisco Lindor | 23 | 0.174 | 0.304 | 0.130 | 0.241 | 0.273 | 15.8% | 16.2% | 22.8% |
| FF | Mark Vientos | 55 | 0.240 | 0.360 | 0.120 | 0.304 | 0.326 | 10.3% | 24.7% | 25.0% |


## Home Starting Pitcher: Nolan McLean

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1400 |
| Batted/Result Events | 345 |
| Hits Allowed | 59 |
| Walks | 32 |
| Strikeouts | 97 |
| Home Runs | 8 |
| K Event Rate | 28.1% |
| BB Event Rate | 9.3% |
| HR Event Rate | 2.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-17 | CIN | 9.0 | 3 | 0 | 2 | 9 | 0 |
| 2026-06-12 | NYM | 6.0 | 3 | 0 | 4 | 6 | 0 |
| 2026-06-06 | SD | 8.0 | 3 | 0 | 3 | 5 | 0 |
| 2026-05-31 | NYM | 7.7 | 2 | 0 | 6 | 2 | 0 |
| 2026-05-25 | NYM | 6.3 | 5 | 2 | 4 | 6 | 2 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 6.1% | 85 | 0.190 | 0.238 | 0.048 | 0.252 | 0.254 | 0.0% | 10.3% | 24.5% |
| CH | vs R | 1.3% | 18 | 0.000 | 0.000 | 0.000 | 0.140 | 0.184 | 0.0% | 20.0% | 37.5% |
| CS | vs L | 0.2% | 3 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CS | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 0.0% |
| CU | vs L | 7.5% | 105 | 0.034 | 0.034 | 0.000 | 0.053 | 0.079 | 0.0% | 22.2% | 42.2% |
| CU | vs R | 4.0% | 56 | 0.200 | 0.200 | 0.000 | 0.212 | 0.153 | 0.0% | 11.8% | 30.0% |
| FC | vs L | 7.1% | 99 | 0.600 | 0.867 | 0.267 | 0.742 | 0.385 | 0.0% | 14.7% | 21.2% |
| FC | vs R | 3.8% | 53 | 0.250 | 0.583 | 0.333 | 0.373 | 0.470 | 33.3% | 38.9% | 32.1% |
| FF | vs L | 11.4% | 160 | 0.250 | 0.469 | 0.219 | 0.339 | 0.437 | 11.1% | 26.8% | 17.8% |
| FF | vs R | 6.7% | 94 | 0.000 | 0.000 | 0.000 | 0.100 | 0.147 | 0.0% | 11.1% | 26.3% |
| SI | vs L | 15.3% | 214 | 0.169 | 0.254 | 0.085 | 0.241 | 0.279 | 4.7% | 31.0% | 15.9% |
| SI | vs R | 19.1% | 268 | 0.176 | 0.309 | 0.132 | 0.270 | 0.268 | 4.3% | 19.3% | 12.6% |
| SL | vs R | 0.2% | 3 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| ST | vs L | 7.7% | 108 | 0.429 | 0.929 | 0.500 | 0.607 | 0.482 | 16.7% | 27.3% | 9.4% |
| ST | vs R | 9.5% | 133 | 0.167 | 0.167 | 0.000 | 0.250 | 0.252 | 0.0% | 4.2% | 31.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-17 | 101 | 3 | 1 | 9 | 0 |
| 2026-06-12 | 93 | 3 | 4 | 6 | 0 |
| 2026-06-06 | 101 | 3 | 3 | 5 | 0 |
| 2026-05-31 | 94 | 2 | 5 | 2 | 0 |
| 2026-05-25 | 78 | 5 | 2 | 6 | 2 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Matt Shaw | 7 | 0.250 | 1.000 | 0.750 | 0.486 | 0.217 | 0.0% | 20.0% | 14.3% |
| FC | Ian Happ | 21 | 0.421 | 1.053 | 0.632 | 0.586 | 0.510 | 28.6% | 37.1% | 21.8% |
| SI | Michael Conforto | 21 | 0.647 | 1.176 | 0.529 | 0.726 | 0.618 | 20.0% | 61.9% | 12.5% |
| ST | Ian Happ | 23 | 0.318 | 0.818 | 0.500 | 0.478 | 0.373 | 20.0% | 40.9% | 34.2% |
| FC | Moisés Ballesteros | 17 | 0.286 | 0.786 | 0.500 | 0.485 | 0.421 | 9.1% | 36.4% | 17.2% |
| FC | Carson Kelly | 13 | 0.556 | 1.000 | 0.444 | 0.673 | 0.616 | 22.2% | 25.0% | 5.3% |
| FC | Alex Bregman | 19 | 0.438 | 0.812 | 0.375 | 0.518 | 0.411 | 6.2% | 20.0% | 15.8% |
| FF | Matt Shaw | 48 | 0.326 | 0.674 | 0.349 | 0.481 | 0.347 | 13.3% | 23.6% | 18.6% |
| FC | Pete Crow-Armstrong | 14 | 0.250 | 0.583 | 0.333 | 0.396 | 0.379 | 11.1% | 20.0% | 23.9% |
| FC | Michael Busch | 24 | 0.263 | 0.579 | 0.316 | 0.394 | 0.388 | 11.1% | 28.8% | 5.2% |
| FF | Moisés Ballesteros | 53 | 0.156 | 0.444 | 0.289 | 0.301 | 0.295 | 23.1% | 32.1% | 35.2% |
| FF | Miguel Amaya | 45 | 0.333 | 0.619 | 0.286 | 0.459 | 0.318 | 18.2% | 26.6% | 12.7% |
| FF | Ian Happ | 113 | 0.219 | 0.500 | 0.281 | 0.375 | 0.322 | 15.8% | 25.2% | 25.0% |
| ST | Nico Hoerner | 20 | 0.611 | 0.889 | 0.278 | 0.745 | 0.379 | 0.0% | 19.4% | 0.0% |
| ST | Carson Kelly | 19 | 0.263 | 0.526 | 0.263 | 0.332 | 0.245 | 16.7% | 23.1% | 28.9% |
| SI | Miguel Amaya | 23 | 0.375 | 0.625 | 0.250 | 0.511 | 0.485 | 6.7% | 33.3% | 13.2% |
| ST | Pete Crow-Armstrong | 30 | 0.207 | 0.448 | 0.241 | 0.288 | 0.267 | 11.1% | 22.2% | 31.0% |
| ST | Dansby Swanson | 29 | 0.200 | 0.440 | 0.240 | 0.303 | 0.266 | 9.1% | 16.2% | 21.3% |
| FF | Seiya Suzuki | 74 | 0.279 | 0.508 | 0.230 | 0.401 | 0.344 | 13.6% | 28.6% | 18.2% |
| FF | Dansby Swanson | 94 | 0.253 | 0.480 | 0.227 | 0.386 | 0.352 | 5.5% | 29.7% | 23.2% |
| FF | Michael Conforto | 41 | 0.222 | 0.444 | 0.222 | 0.330 | 0.313 | 8.7% | 28.6% | 14.8% |
| FC | Michael Conforto | 9 | 0.333 | 0.556 | 0.222 | 0.378 | 0.439 | 14.3% | 22.2% | 18.2% |
| SI | Seiya Suzuki | 56 | 0.380 | 0.600 | 0.220 | 0.468 | 0.456 | 10.0% | 32.1% | 13.0% |
| FC | Dansby Swanson | 16 | 0.357 | 0.571 | 0.214 | 0.438 | 0.390 | 7.7% | 17.6% | 30.8% |
| SI | Dansby Swanson | 56 | 0.271 | 0.479 | 0.208 | 0.405 | 0.382 | 10.5% | 31.9% | 21.0% |
| ST | Alex Bregman | 35 | 0.172 | 0.379 | 0.207 | 0.317 | 0.322 | 9.1% | 27.8% | 28.3% |
| ST | Moisés Ballesteros | 7 | 0.200 | 0.400 | 0.200 | 0.279 | 0.252 | 33.3% | 30.0% | 14.3% |
| FC | Seiya Suzuki | 16 | 0.333 | 0.533 | 0.200 | 0.394 | 0.315 | 8.3% | 17.6% | 37.0% |
| SI | Michael Busch | 70 | 0.255 | 0.451 | 0.196 | 0.421 | 0.483 | 18.6% | 33.3% | 16.5% |
| FF | Pete Crow-Armstrong | 111 | 0.206 | 0.402 | 0.196 | 0.313 | 0.315 | 10.6% | 32.6% | 19.4% |


## Chicago Cubs Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Alex Bregman | 363 | 0.256 | 0.386 | 0.130 | 0.337 | 0.315 | 5.8% | 27.5% | 16.5% |
| Nico Hoerner | 363 | 0.249 | 0.352 | 0.103 | 0.314 | 0.326 | 1.7% | 18.9% | 10.2% |
| Michael Busch | 360 | 0.240 | 0.392 | 0.152 | 0.350 | 0.351 | 11.4% | 26.2% | 23.9% |
| Ian Happ | 345 | 0.229 | 0.468 | 0.239 | 0.362 | 0.326 | 13.8% | 25.5% | 29.0% |
| Pete Crow-Armstrong | 342 | 0.280 | 0.517 | 0.237 | 0.378 | 0.370 | 11.5% | 32.0% | 25.3% |
| Dansby Swanson | 305 | 0.187 | 0.336 | 0.149 | 0.296 | 0.288 | 6.3% | 24.1% | 28.5% |
| Seiya Suzuki | 265 | 0.270 | 0.443 | 0.174 | 0.369 | 0.342 | 8.6% | 26.0% | 24.1% |
| Carson Kelly | 219 | 0.298 | 0.429 | 0.131 | 0.369 | 0.328 | 7.7% | 24.6% | 20.2% |
| Moisés Ballesteros | 193 | 0.246 | 0.439 | 0.193 | 0.335 | 0.310 | 11.3% | 28.2% | 23.3% |
| Matt Shaw | 157 | 0.262 | 0.454 | 0.191 | 0.359 | 0.299 | 5.4% | 22.5% | 18.9% |
| Miguel Amaya | 143 | 0.240 | 0.430 | 0.190 | 0.369 | 0.313 | 9.7% | 21.4% | 22.6% |
| Michael Conforto | 134 | 0.248 | 0.479 | 0.231 | 0.350 | 0.345 | 12.5% | 32.3% | 26.7% |


## New York Mets Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bo Bichette | 359 | 0.264 | 0.404 | 0.140 | 0.319 | 0.332 | 7.0% | 27.3% | 16.3% |
| Marcus Semien | 330 | 0.220 | 0.358 | 0.139 | 0.289 | 0.319 | 9.1% | 22.0% | 21.4% |
| Carson Benge | 315 | 0.261 | 0.404 | 0.143 | 0.338 | 0.348 | 8.8% | 24.6% | 19.8% |
| Brett Baty | 273 | 0.222 | 0.309 | 0.086 | 0.286 | 0.291 | 8.3% | 21.9% | 26.7% |
| Juan Soto | 268 | 0.291 | 0.552 | 0.261 | 0.399 | 0.420 | 14.6% | 34.0% | 18.0% |
| Mark Vientos | 241 | 0.211 | 0.383 | 0.172 | 0.277 | 0.312 | 10.4% | 27.8% | 29.5% |
| Francisco Álvarez | 181 | 0.258 | 0.411 | 0.153 | 0.333 | 0.343 | 14.9% | 29.8% | 27.5% |
| Luis Torrens | 148 | 0.226 | 0.314 | 0.088 | 0.262 | 0.271 | 3.8% | 23.2% | 21.5% |
| A. J. Ewing | 146 | 0.258 | 0.367 | 0.109 | 0.322 | 0.332 | 4.5% | 19.3% | 22.3% |
| Mj Melendez | 138 | 0.183 | 0.348 | 0.165 | 0.295 | 0.276 | 11.8% | 28.5% | 31.5% |
| Francisco Lindor | 125 | 0.214 | 0.321 | 0.107 | 0.302 | 0.340 | 7.9% | 25.0% | 22.7% |
| Tyrone Taylor | 118 | 0.183 | 0.312 | 0.128 | 0.239 | 0.248 | 5.5% | 22.5% | 21.2% |


## Bullpen Fatigue Report

### Chicago Cubs Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Caleb Thielbar | 2026-06-20 | 0.1 | 13 |
| Caleb Thielbar | 2026-06-22 | 1.0 | 19 |
| Ethan Roberts | 2026-06-20 | 1.1 | 14 |
| Hoby Milner | 2026-06-23 | 1.0 | 12 |
| Jacob Webb | 2026-06-20 | 0.2 | 27 |
| Jayden Murray | 2026-06-23 | 1.0 | 26 |
| Phil Maton | 2026-06-23 | 1.0 | 21 |
| Ryan Rolison | 2026-06-20 | 0.2 | 1 |
| Ryan Rolison | 2026-06-22 | 1.0 | 18 |
| Ryan Rolison | 2026-06-23 | 1.0 | 12 |
| Trent Thornton | 2026-06-20 | 0.2 | 13 |
| Tyler Ferguson | 2026-06-22 | 2.0 | 26 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Hoby Milner, Jayden Murray, Phil Maton, Ryan Rolison


### New York Mets Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| A.J. Minter | 2026-06-21 | 1.0 | 9 |
| A.J. Minter | 2026-06-23 | 1.0 | 14 |
| Austin Warren | 2026-06-21 | 2.0 | 37 |
| Austin Warren | 2026-06-22 | 1.0 | 13 |
| Brooks Raley | 2026-06-21 | 1.0 | 21 |
| Cionel Pérez | 2026-06-20 | 2.0 | 32 |
| Cionel Pérez | 2026-06-23 | 2.1 | 29 |
| Jonathan Pintaro | 2026-06-22 | 2.0 | 45 |
| Tobias Myers | 2026-06-20 | 2.1 | 41 |
| Tobias Myers | 2026-06-23 | 2.0 | 45 |
| Zack Short | 2026-06-20 | 1.0 | 10 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** A.J. Minter, Cionel Pérez, Tobias Myers



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Alex Bregman | 363 | 0.256 | 0.386 | 0.130 | 0.337 | 5.8% | 27.5% |
| 2 | Nico Hoerner | 363 | 0.249 | 0.352 | 0.103 | 0.314 | 1.7% | 18.9% |
| 3 | Michael Busch | 360 | 0.240 | 0.392 | 0.152 | 0.350 | 11.4% | 26.2% |
| 4 | Ian Happ | 345 | 0.229 | 0.468 | 0.239 | 0.362 | 13.8% | 25.5% |
| 5 | Pete Crow-Armstrong | 342 | 0.280 | 0.517 | 0.237 | 0.378 | 11.5% | 32.0% |
| 6 | Dansby Swanson | 305 | 0.187 | 0.336 | 0.149 | 0.296 | 6.3% | 24.1% |
| 7 | Seiya Suzuki | 265 | 0.270 | 0.443 | 0.174 | 0.369 | 8.6% | 26.0% |
| 8 | Carson Kelly | 219 | 0.298 | 0.429 | 0.131 | 0.369 | 7.7% | 24.6% |
| 9 | Moisés Ballesteros | 193 | 0.246 | 0.439 | 0.193 | 0.335 | 11.3% | 28.2% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bo Bichette | 359 | 0.264 | 0.404 | 0.140 | 0.319 | 7.0% | 27.3% |
| 2 | Marcus Semien | 330 | 0.220 | 0.358 | 0.139 | 0.289 | 9.1% | 22.0% |
| 3 | Carson Benge | 315 | 0.261 | 0.404 | 0.143 | 0.338 | 8.8% | 24.6% |
| 4 | Brett Baty | 273 | 0.222 | 0.309 | 0.086 | 0.286 | 8.3% | 21.9% |
| 5 | Juan Soto | 268 | 0.291 | 0.552 | 0.261 | 0.399 | 14.6% | 34.0% |
| 6 | Mark Vientos | 241 | 0.211 | 0.383 | 0.172 | 0.277 | 10.4% | 27.8% |
| 7 | Francisco Álvarez | 181 | 0.258 | 0.411 | 0.153 | 0.333 | 14.9% | 29.8% |
| 8 | Luis Torrens | 148 | 0.226 | 0.314 | 0.088 | 0.262 | 3.8% | 23.2% |
| 9 | A. J. Ewing | 146 | 0.258 | 0.367 | 0.109 | 0.322 | 4.5% | 19.3% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6785 |
| Hits Allowed | 1478 |
| Walks/HBP | 730 |
| Strikeouts | 1451 |
| Home Runs Allowed | 249 |
| K Event Rate | 21.4% |
| BB/HBP Event Rate | 10.8% |
| HR Event Rate | 3.7% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6471 |
| Hits Allowed | 1345 |
| Walks/HBP | 612 |
| Strikeouts | 1491 |
| Home Runs Allowed | 175 |
| K Event Rate | 23.0% |
| BB/HBP Event Rate | 9.5% |
| HR Event Rate | 2.7% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: SI, FF, FC, CH, ST
- Home pitcher pitch mix to inspect: SI, FF, ST, CU, FC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 3. Chicago Cubs @ New York Mets

## Game Context

| Field | Value |
| --- | --- |
| Park | Citi Field |
| Time | 2026-06-24T23:10:00Z |
| Away Team | Chicago Cubs |
| Home Team | New York Mets |
| Away Probable Pitcher | Shota Imanaga |
| Home Probable Pitcher | Sean Manaea |


## Away Starting Pitcher: Shota Imanaga

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1505 |
| Batted/Result Events | 389 |
| Hits Allowed | 78 |
| Walks | 25 |
| Strikeouts | 97 |
| Home Runs | 18 |
| K Event Rate | 24.9% |
| BB Event Rate | 6.4% |
| HR Event Rate | 4.6% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-15 | CHC | 7.3 | 5 | 0 | 1 | 3 | 0 |
| 2026-06-10 | COL | 6.3 | 2 | 0 | 2 | 7 | 0 |
| 2026-06-04 | CHC | 8.0 | 6 | 4 | 1 | 5 | 4 |
| 2026-05-29 | STL | 7.7 | 5 | 3 | 3 | 2 | 3 |
| 2026-05-24 | CHC | 8.7 | 7 | 3 | 2 | 6 | 3 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CU | vs R | 3.1% | 46 | 0.000 | 0.000 | 0.000 | 0.140 | 0.419 | 25.0% | 22.2% | 10.0% |
| FF | vs L | 10.2% | 153 | 0.200 | 0.350 | 0.150 | 0.260 | 0.369 | 11.8% | 38.5% | 7.9% |
| FF | vs R | 32.8% | 494 | 0.270 | 0.470 | 0.200 | 0.363 | 0.344 | 13.9% | 24.4% | 21.3% |
| FS | vs L | 4.3% | 65 | 0.167 | 0.222 | 0.056 | 0.197 | 0.138 | 0.0% | 6.7% | 57.9% |
| FS | vs R | 29.0% | 437 | 0.185 | 0.403 | 0.218 | 0.275 | 0.249 | 9.3% | 21.2% | 39.5% |
| SI | vs L | 2.3% | 35 | 0.214 | 0.429 | 0.214 | 0.347 | 0.363 | 8.3% | 33.3% | 22.7% |
| SI | vs R | 4.7% | 71 | 0.250 | 0.450 | 0.200 | 0.320 | 0.313 | 5.0% | 40.7% | 15.6% |
| SL | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | 0.000 | — | 0.0% | 0.0% | 0.0% |
| SL | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 100.0% |
| ST | vs L | 9.5% | 143 | 0.226 | 0.548 | 0.323 | 0.333 | 0.247 | 15.0% | 16.2% | 43.2% |
| ST | vs R | 3.8% | 57 | 0.273 | 0.364 | 0.091 | 0.342 | 0.375 | 0.0% | 31.2% | 26.1% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 85 | 5 | 1 | 3 | 0 |
| 2026-06-10 | 90 | 2 | 2 | 7 | 0 |
| 2026-06-04 | 84 | 6 | 1 | 5 | 4 |
| 2026-05-29 | 75 | 5 | 1 | 2 | 3 |
| 2026-05-24 | 94 | 7 | 1 | 6 | 3 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FS | Francisco Álvarez | 4 | 0.250 | 1.000 | 0.750 | 0.675 | 0.712 | 50.0% | 50.0% | 40.0% |
| ST | Mj Melendez | 11 | 0.200 | 0.600 | 0.400 | 0.359 | 0.296 | 16.7% | 35.7% | 17.6% |
| FF | Juan Soto | 73 | 0.303 | 0.667 | 0.364 | 0.434 | 0.480 | 21.8% | 33.3% | 13.4% |
| FS | Carson Benge | 12 | 0.250 | 0.583 | 0.333 | 0.346 | 0.343 | 11.1% | 31.2% | 23.8% |
| FS | Francisco Lindor | 6 | 0.167 | 0.500 | 0.333 | 0.267 | 0.161 | 0.0% | 16.7% | 36.4% |
| ST | Juan Soto | 27 | 0.320 | 0.640 | 0.320 | 0.426 | 0.466 | 21.1% | 33.3% | 27.0% |
| FF | Mj Melendez | 55 | 0.196 | 0.435 | 0.239 | 0.325 | 0.246 | 7.4% | 24.3% | 32.2% |
| ST | Bo Bichette | 32 | 0.226 | 0.419 | 0.194 | 0.288 | 0.319 | 13.6% | 20.0% | 32.9% |
| FF | Tyrone Taylor | 29 | 0.231 | 0.423 | 0.192 | 0.269 | 0.176 | 0.0% | 10.9% | 13.0% |
| FF | Carson Benge | 108 | 0.312 | 0.490 | 0.177 | 0.393 | 0.384 | 8.5% | 22.1% | 18.8% |
| FF | A. J. Ewing | 43 | 0.235 | 0.412 | 0.176 | 0.369 | 0.401 | 11.5% | 20.0% | 10.4% |
| FF | Marcus Semien | 88 | 0.211 | 0.382 | 0.171 | 0.297 | 0.361 | 14.5% | 30.1% | 17.1% |
| FF | Bo Bichette | 88 | 0.231 | 0.397 | 0.167 | 0.317 | 0.340 | 5.3% | 26.9% | 11.4% |
| FF | Francisco Lindor | 46 | 0.179 | 0.333 | 0.154 | 0.311 | 0.395 | 8.8% | 27.4% | 13.3% |
| FS | Mj Melendez | 8 | 0.286 | 0.429 | 0.143 | 0.356 | 0.316 | 20.0% | 66.7% | 27.3% |
| ST | Carson Benge | 22 | 0.238 | 0.381 | 0.143 | 0.286 | 0.281 | 10.0% | 25.9% | 33.3% |
| FF | Mark Vientos | 55 | 0.240 | 0.360 | 0.120 | 0.304 | 0.326 | 10.3% | 24.7% | 25.0% |
| FF | Francisco Álvarez | 39 | 0.294 | 0.412 | 0.118 | 0.358 | 0.400 | 20.0% | 26.1% | 26.4% |
| FS | Marcus Semien | 10 | 0.222 | 0.333 | 0.111 | 0.465 | 0.253 | 0.0% | 8.3% | 17.6% |
| FF | Brett Baty | 95 | 0.233 | 0.337 | 0.105 | 0.301 | 0.280 | 10.3% | 22.2% | 20.0% |
| FS | Mark Vientos | 12 | 0.091 | 0.182 | 0.091 | 0.163 | 0.264 | 14.3% | 20.0% | 50.0% |
| FS | Brett Baty | 14 | 0.071 | 0.143 | 0.071 | 0.089 | 0.130 | 0.0% | 0.0% | 43.3% |
| ST | Francisco Álvarez | 17 | 0.214 | 0.286 | 0.071 | 0.262 | 0.291 | 20.0% | 27.8% | 31.0% |
| FF | Luis Torrens | 34 | 0.258 | 0.323 | 0.065 | 0.294 | 0.329 | 4.5% | 24.2% | 17.8% |
| ST | Luis Torrens | 19 | 0.211 | 0.263 | 0.053 | 0.208 | 0.173 | 7.1% | 25.0% | 28.6% |
| ST | Mark Vientos | 24 | 0.083 | 0.125 | 0.042 | 0.090 | 0.183 | 5.9% | 13.8% | 36.7% |
| ST | Brett Baty | 27 | 0.120 | 0.160 | 0.040 | 0.191 | 0.139 | 9.1% | 19.2% | 40.8% |
| FS | Juan Soto | 11 | 0.250 | 0.250 | 0.000 | 0.355 | 0.343 | 0.0% | 50.0% | 38.5% |
| FS | A. J. Ewing | 5 | 0.400 | 0.400 | 0.000 | 0.360 | 0.439 | 0.0% | 14.3% | 30.0% |
| FS | Bo Bichette | 9 | 0.125 | 0.125 | 0.000 | 0.178 | 0.247 | 0.0% | 30.0% | 31.2% |


## Home Starting Pitcher: Sean Manaea

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1007 |
| Batted/Result Events | 250 |
| Hits Allowed | 55 |
| Walks | 18 |
| Strikeouts | 60 |
| Home Runs | 6 |
| K Event Rate | 24.0% |
| BB Event Rate | 7.2% |
| HR Event Rate | 2.4% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-18 | PHI | 7.7 | 6 | 0 | 2 | 5 | 0 |
| 2026-06-13 | NYM | 7.3 | 4 | 1 | 0 | 6 | 1 |
| 2026-06-07 | SD | 5.7 | 4 | 1 | 1 | 3 | 1 |
| 2026-06-01 | SEA | 5.3 | 1 | 1 | 1 | 4 | 1 |
| 2026-05-26 | NYM | 4.7 | 3 | 0 | 2 | 6 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.3% | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.017 | 0.0% | 0.0% | 33.3% |
| CH | vs R | 4.2% | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.453 | 40.0% | 33.3% | 21.1% |
| FC | vs L | 1.6% | 16 | 0.000 | 0.000 | 0.000 | 0.350 | 0.710 | 0.0% | 0.0% | 83.3% |
| FC | vs R | 6.3% | 63 | 0.273 | 0.636 | 0.364 | 0.377 | 0.390 | 11.1% | 14.3% | 22.6% |
| FF | vs L | 8.2% | 83 | 0.294 | 0.529 | 0.235 | 0.378 | 0.376 | 9.1% | 21.4% | 18.4% |
| FF | vs R | 28.1% | 283 | 0.215 | 0.431 | 0.215 | 0.303 | 0.321 | 10.4% | 25.2% | 18.4% |
| SI | vs L | 10.6% | 107 | 0.300 | 0.367 | 0.067 | 0.293 | 0.275 | 0.0% | 26.3% | 6.7% |
| SI | vs R | 8.3% | 84 | 0.391 | 0.478 | 0.087 | 0.457 | 0.375 | 5.0% | 25.0% | 12.8% |
| ST | vs L | 12.3% | 124 | 0.161 | 0.290 | 0.129 | 0.258 | 0.169 | 15.4% | 17.2% | 45.2% |
| ST | vs R | 20.1% | 202 | 0.270 | 0.405 | 0.135 | 0.338 | 0.338 | 6.7% | 19.4% | 27.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-18 | 95 | 6 | 1 | 5 | 0 |
| 2026-06-13 | 84 | 4 | 0 | 6 | 1 |
| 2026-06-07 | 66 | 4 | 1 | 3 | 1 |
| 2026-06-01 | 63 | 1 | 1 | 4 | 1 |
| 2026-05-26 | 68 | 3 | 2 | 6 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SI | Michael Conforto | 21 | 0.647 | 1.176 | 0.529 | 0.726 | 0.618 | 20.0% | 61.9% | 12.5% |
| ST | Ian Happ | 23 | 0.318 | 0.818 | 0.500 | 0.478 | 0.373 | 20.0% | 40.9% | 34.2% |
| FF | Matt Shaw | 48 | 0.326 | 0.674 | 0.349 | 0.481 | 0.347 | 13.3% | 23.6% | 18.6% |
| FF | Moisés Ballesteros | 53 | 0.156 | 0.444 | 0.289 | 0.301 | 0.295 | 23.1% | 32.1% | 35.2% |
| FF | Miguel Amaya | 45 | 0.333 | 0.619 | 0.286 | 0.459 | 0.318 | 18.2% | 26.6% | 12.7% |
| FF | Ian Happ | 113 | 0.219 | 0.500 | 0.281 | 0.375 | 0.322 | 15.8% | 25.2% | 25.0% |
| ST | Nico Hoerner | 20 | 0.611 | 0.889 | 0.278 | 0.745 | 0.379 | 0.0% | 19.4% | 0.0% |
| ST | Carson Kelly | 19 | 0.263 | 0.526 | 0.263 | 0.332 | 0.245 | 16.7% | 23.1% | 28.9% |
| SI | Miguel Amaya | 23 | 0.375 | 0.625 | 0.250 | 0.511 | 0.485 | 6.7% | 33.3% | 13.2% |
| ST | Pete Crow-Armstrong | 30 | 0.207 | 0.448 | 0.241 | 0.288 | 0.267 | 11.1% | 22.2% | 31.0% |
| ST | Dansby Swanson | 29 | 0.200 | 0.440 | 0.240 | 0.303 | 0.266 | 9.1% | 16.2% | 21.3% |
| FF | Seiya Suzuki | 74 | 0.279 | 0.508 | 0.230 | 0.401 | 0.344 | 13.6% | 28.6% | 18.2% |
| FF | Dansby Swanson | 94 | 0.253 | 0.480 | 0.227 | 0.386 | 0.352 | 5.5% | 29.7% | 23.2% |
| FF | Michael Conforto | 41 | 0.222 | 0.444 | 0.222 | 0.330 | 0.313 | 8.7% | 28.6% | 14.8% |
| SI | Seiya Suzuki | 56 | 0.380 | 0.600 | 0.220 | 0.468 | 0.456 | 10.0% | 32.1% | 13.0% |
| SI | Dansby Swanson | 56 | 0.271 | 0.479 | 0.208 | 0.405 | 0.382 | 10.5% | 31.9% | 21.0% |
| ST | Alex Bregman | 35 | 0.172 | 0.379 | 0.207 | 0.317 | 0.322 | 9.1% | 27.8% | 28.3% |
| ST | Moisés Ballesteros | 7 | 0.200 | 0.400 | 0.200 | 0.279 | 0.252 | 33.3% | 30.0% | 14.3% |
| FF | Pete Crow-Armstrong | 111 | 0.206 | 0.402 | 0.196 | 0.313 | 0.315 | 10.6% | 32.6% | 19.4% |
| SI | Michael Busch | 70 | 0.255 | 0.451 | 0.196 | 0.421 | 0.483 | 18.6% | 33.3% | 16.5% |
| SI | Pete Crow-Armstrong | 48 | 0.463 | 0.659 | 0.195 | 0.518 | 0.457 | 8.3% | 37.3% | 13.9% |
| FF | Michael Busch | 120 | 0.217 | 0.377 | 0.160 | 0.328 | 0.337 | 12.9% | 24.7% | 12.1% |
| SI | Moisés Ballesteros | 28 | 0.346 | 0.500 | 0.154 | 0.389 | 0.311 | 13.6% | 27.9% | 11.3% |
| FF | Alex Bregman | 92 | 0.293 | 0.439 | 0.146 | 0.358 | 0.332 | 5.6% | 30.3% | 8.4% |
| SI | Ian Happ | 36 | 0.267 | 0.400 | 0.133 | 0.357 | 0.356 | 8.7% | 31.9% | 7.5% |
| ST | Michael Conforto | 11 | 0.250 | 0.375 | 0.125 | 0.386 | 0.263 | 0.0% | 12.5% | 40.0% |
| ST | Seiya Suzuki | 28 | 0.160 | 0.280 | 0.120 | 0.307 | 0.261 | 9.1% | 20.7% | 36.0% |
| SI | Alex Bregman | 93 | 0.321 | 0.420 | 0.099 | 0.392 | 0.352 | 3.9% | 29.1% | 3.7% |
| SI | Nico Hoerner | 81 | 0.270 | 0.365 | 0.095 | 0.336 | 0.331 | 0.0% | 19.4% | 2.5% |
| FF | Nico Hoerner | 125 | 0.198 | 0.292 | 0.094 | 0.281 | 0.351 | 3.9% | 20.0% | 5.2% |


## Chicago Cubs Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Alex Bregman | 363 | 0.256 | 0.386 | 0.130 | 0.337 | 0.315 | 5.8% | 27.5% | 16.5% |
| Nico Hoerner | 363 | 0.249 | 0.352 | 0.103 | 0.314 | 0.326 | 1.7% | 18.9% | 10.2% |
| Michael Busch | 360 | 0.240 | 0.392 | 0.152 | 0.350 | 0.351 | 11.4% | 26.2% | 23.9% |
| Ian Happ | 345 | 0.229 | 0.468 | 0.239 | 0.362 | 0.326 | 13.8% | 25.5% | 29.0% |
| Pete Crow-Armstrong | 342 | 0.280 | 0.517 | 0.237 | 0.378 | 0.370 | 11.5% | 32.0% | 25.3% |
| Dansby Swanson | 305 | 0.187 | 0.336 | 0.149 | 0.296 | 0.288 | 6.3% | 24.1% | 28.5% |
| Seiya Suzuki | 265 | 0.270 | 0.443 | 0.174 | 0.369 | 0.342 | 8.6% | 26.0% | 24.1% |
| Carson Kelly | 219 | 0.298 | 0.429 | 0.131 | 0.369 | 0.328 | 7.7% | 24.6% | 20.2% |
| Moisés Ballesteros | 193 | 0.246 | 0.439 | 0.193 | 0.335 | 0.310 | 11.3% | 28.2% | 23.3% |
| Matt Shaw | 157 | 0.262 | 0.454 | 0.191 | 0.359 | 0.299 | 5.4% | 22.5% | 18.9% |
| Miguel Amaya | 143 | 0.240 | 0.430 | 0.190 | 0.369 | 0.313 | 9.7% | 21.4% | 22.6% |
| Michael Conforto | 134 | 0.248 | 0.479 | 0.231 | 0.350 | 0.345 | 12.5% | 32.3% | 26.7% |


## New York Mets Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bo Bichette | 359 | 0.264 | 0.404 | 0.140 | 0.319 | 0.332 | 7.0% | 27.3% | 16.3% |
| Marcus Semien | 330 | 0.220 | 0.358 | 0.139 | 0.289 | 0.319 | 9.1% | 22.0% | 21.4% |
| Carson Benge | 315 | 0.261 | 0.404 | 0.143 | 0.338 | 0.348 | 8.8% | 24.6% | 19.8% |
| Brett Baty | 273 | 0.222 | 0.309 | 0.086 | 0.286 | 0.291 | 8.3% | 21.9% | 26.7% |
| Juan Soto | 268 | 0.291 | 0.552 | 0.261 | 0.399 | 0.420 | 14.6% | 34.0% | 18.0% |
| Mark Vientos | 241 | 0.211 | 0.383 | 0.172 | 0.277 | 0.312 | 10.4% | 27.8% | 29.5% |
| Francisco Álvarez | 181 | 0.258 | 0.411 | 0.153 | 0.333 | 0.343 | 14.9% | 29.8% | 27.5% |
| Luis Torrens | 148 | 0.226 | 0.314 | 0.088 | 0.262 | 0.271 | 3.8% | 23.2% | 21.5% |
| A. J. Ewing | 146 | 0.258 | 0.367 | 0.109 | 0.322 | 0.332 | 4.5% | 19.3% | 22.3% |
| Mj Melendez | 138 | 0.183 | 0.348 | 0.165 | 0.295 | 0.276 | 11.8% | 28.5% | 31.5% |
| Francisco Lindor | 125 | 0.214 | 0.321 | 0.107 | 0.302 | 0.340 | 7.9% | 25.0% | 22.7% |
| Tyrone Taylor | 118 | 0.183 | 0.312 | 0.128 | 0.239 | 0.248 | 5.5% | 22.5% | 21.2% |


## Bullpen Fatigue Report

### Chicago Cubs Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Caleb Thielbar | 2026-06-20 | 0.1 | 13 |
| Caleb Thielbar | 2026-06-22 | 1.0 | 19 |
| Ethan Roberts | 2026-06-20 | 1.1 | 14 |
| Hoby Milner | 2026-06-23 | 1.0 | 12 |
| Jacob Webb | 2026-06-20 | 0.2 | 27 |
| Jayden Murray | 2026-06-23 | 1.0 | 26 |
| Phil Maton | 2026-06-23 | 1.0 | 21 |
| Ryan Rolison | 2026-06-20 | 0.2 | 1 |
| Ryan Rolison | 2026-06-22 | 1.0 | 18 |
| Ryan Rolison | 2026-06-23 | 1.0 | 12 |
| Trent Thornton | 2026-06-20 | 0.2 | 13 |
| Tyler Ferguson | 2026-06-22 | 2.0 | 26 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Hoby Milner, Jayden Murray, Phil Maton, Ryan Rolison


### New York Mets Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| A.J. Minter | 2026-06-21 | 1.0 | 9 |
| A.J. Minter | 2026-06-23 | 1.0 | 14 |
| Austin Warren | 2026-06-21 | 2.0 | 37 |
| Austin Warren | 2026-06-22 | 1.0 | 13 |
| Brooks Raley | 2026-06-21 | 1.0 | 21 |
| Cionel Pérez | 2026-06-20 | 2.0 | 32 |
| Cionel Pérez | 2026-06-23 | 2.1 | 29 |
| Jonathan Pintaro | 2026-06-22 | 2.0 | 45 |
| Tobias Myers | 2026-06-20 | 2.1 | 41 |
| Tobias Myers | 2026-06-23 | 2.0 | 45 |
| Zack Short | 2026-06-20 | 1.0 | 10 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** A.J. Minter, Cionel Pérez, Tobias Myers



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Alex Bregman | 363 | 0.256 | 0.386 | 0.130 | 0.337 | 5.8% | 27.5% |
| 2 | Nico Hoerner | 363 | 0.249 | 0.352 | 0.103 | 0.314 | 1.7% | 18.9% |
| 3 | Michael Busch | 360 | 0.240 | 0.392 | 0.152 | 0.350 | 11.4% | 26.2% |
| 4 | Ian Happ | 345 | 0.229 | 0.468 | 0.239 | 0.362 | 13.8% | 25.5% |
| 5 | Pete Crow-Armstrong | 342 | 0.280 | 0.517 | 0.237 | 0.378 | 11.5% | 32.0% |
| 6 | Dansby Swanson | 305 | 0.187 | 0.336 | 0.149 | 0.296 | 6.3% | 24.1% |
| 7 | Seiya Suzuki | 265 | 0.270 | 0.443 | 0.174 | 0.369 | 8.6% | 26.0% |
| 8 | Carson Kelly | 219 | 0.298 | 0.429 | 0.131 | 0.369 | 7.7% | 24.6% |
| 9 | Moisés Ballesteros | 193 | 0.246 | 0.439 | 0.193 | 0.335 | 11.3% | 28.2% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bo Bichette | 359 | 0.264 | 0.404 | 0.140 | 0.319 | 7.0% | 27.3% |
| 2 | Marcus Semien | 330 | 0.220 | 0.358 | 0.139 | 0.289 | 9.1% | 22.0% |
| 3 | Carson Benge | 315 | 0.261 | 0.404 | 0.143 | 0.338 | 8.8% | 24.6% |
| 4 | Brett Baty | 273 | 0.222 | 0.309 | 0.086 | 0.286 | 8.3% | 21.9% |
| 5 | Juan Soto | 268 | 0.291 | 0.552 | 0.261 | 0.399 | 14.6% | 34.0% |
| 6 | Mark Vientos | 241 | 0.211 | 0.383 | 0.172 | 0.277 | 10.4% | 27.8% |
| 7 | Francisco Álvarez | 181 | 0.258 | 0.411 | 0.153 | 0.333 | 14.9% | 29.8% |
| 8 | Luis Torrens | 148 | 0.226 | 0.314 | 0.088 | 0.262 | 3.8% | 23.2% |
| 9 | A. J. Ewing | 146 | 0.258 | 0.367 | 0.109 | 0.322 | 4.5% | 19.3% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6785 |
| Hits Allowed | 1478 |
| Walks/HBP | 730 |
| Strikeouts | 1451 |
| Home Runs Allowed | 249 |
| K Event Rate | 21.4% |
| BB/HBP Event Rate | 10.8% |
| HR Event Rate | 3.7% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6471 |
| Hits Allowed | 1345 |
| Walks/HBP | 612 |
| Strikeouts | 1491 |
| Home Runs Allowed | 175 |
| K Event Rate | 23.0% |
| BB/HBP Event Rate | 9.5% |
| HR Event Rate | 2.7% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, FS, ST
- Home pitcher pitch mix to inspect: FF, ST, SI
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 4. Cleveland Guardians @ Chicago White Sox

## Game Context

| Field | Value |
| --- | --- |
| Park | Rate Field |
| Time | 2026-06-24T18:10:00Z |
| Away Team | Cleveland Guardians |
| Home Team | Chicago White Sox |
| Away Probable Pitcher | Tanner Bibee |
| Home Probable Pitcher | Erick Fedde |


## Away Starting Pitcher: Tanner Bibee

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1570 |
| Batted/Result Events | 418 |
| Hits Allowed | 100 |
| Walks | 28 |
| Strikeouts | 86 |
| Home Runs | 21 |
| K Event Rate | 20.6% |
| BB Event Rate | 6.7% |
| HR Event Rate | 5.0% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | HOU | 7.3 | 4 | 1 | 2 | 7 | 1 |
| 2026-06-12 | CLE | 8.3 | 2 | 2 | 2 | 8 | 2 |
| 2026-06-06 | TEX | 9.0 | 3 | 0 | 2 | 3 | 0 |
| 2026-05-31 | CLE | 8.0 | 6 | 1 | 1 | 5 | 1 |
| 2026-05-25 | CLE | 5.3 | 8 | 5 | 0 | 3 | 5 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 14.0% | 220 | 0.157 | 0.294 | 0.137 | 0.253 | 0.289 | 12.8% | 17.2% | 31.1% |
| CH | vs R | 2.9% | 45 | 0.250 | 0.333 | 0.083 | 0.322 | 0.257 | 0.0% | 15.4% | 30.0% |
| CU | vs L | 5.2% | 82 | 0.167 | 0.458 | 0.292 | 0.294 | 0.383 | 11.8% | 46.4% | 25.6% |
| CU | vs R | 4.9% | 77 | 0.143 | 0.357 | 0.214 | 0.269 | 0.208 | 7.7% | 10.3% | 25.0% |
| FC | vs L | 10.2% | 160 | 0.212 | 0.485 | 0.273 | 0.354 | 0.337 | 10.0% | 27.3% | 39.8% |
| FC | vs R | 15.9% | 250 | 0.305 | 0.610 | 0.305 | 0.390 | 0.380 | 19.1% | 35.6% | 32.5% |
| FF | vs L | 14.0% | 220 | 0.296 | 0.574 | 0.278 | 0.391 | 0.336 | 16.3% | 35.1% | 15.3% |
| FF | vs R | 9.9% | 155 | 0.350 | 0.350 | 0.000 | 0.315 | 0.298 | 2.8% | 35.4% | 9.1% |
| SI | vs L | 6.1% | 95 | 0.385 | 0.654 | 0.269 | 0.478 | 0.462 | 19.0% | 33.3% | 20.8% |
| SI | vs R | 14.8% | 232 | 0.254 | 0.413 | 0.159 | 0.324 | 0.312 | 10.2% | 38.7% | 18.3% |
| ST | vs L | 0.8% | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.171 | 0.0% | 40.0% | 0.0% |
| ST | vs R | 1.4% | 22 | 0.286 | 0.286 | 0.000 | 0.257 | 0.273 | 0.0% | 10.0% | 16.7% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 95 | 4 | 2 | 7 | 1 |
| 2026-06-12 | 91 | 2 | 2 | 8 | 2 |
| 2026-06-06 | 87 | 3 | 2 | 3 | 0 |
| 2026-05-31 | 90 | 6 | 1 | 5 | 1 |
| 2026-05-25 | 61 | 8 | 0 | 3 | 5 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Colson Montgomery | 23 | 0.391 | 1.087 | 0.696 | 0.607 | 0.588 | 33.3% | 40.7% | 31.0% |
| CU | Edgar Quero | 7 | 0.333 | 0.833 | 0.500 | 0.514 | 0.286 | 0.0% | 33.3% | 36.4% |
| FC | Munetaka Murakami | 14 | 0.308 | 0.769 | 0.462 | 0.529 | 0.430 | 10.0% | 33.3% | 29.0% |
| FF | Munetaka Murakami | 90 | 0.257 | 0.714 | 0.457 | 0.476 | 0.462 | 23.9% | 39.3% | 34.9% |
| CH | Colson Montgomery | 35 | 0.281 | 0.688 | 0.406 | 0.427 | 0.419 | 18.2% | 24.4% | 38.4% |
| FF | Drew Romo | 29 | 0.125 | 0.500 | 0.375 | 0.328 | 0.328 | 20.0% | 22.5% | 18.9% |
| CH | Munetaka Murakami | 28 | 0.360 | 0.720 | 0.360 | 0.482 | 0.382 | 25.0% | 44.8% | 43.8% |
| SI | Drew Romo | 18 | 0.333 | 0.667 | 0.333 | 0.467 | 0.508 | 26.7% | 47.4% | 16.7% |
| CH | Everson Pereira | 17 | 0.375 | 0.688 | 0.312 | 0.465 | 0.231 | 10.0% | 33.3% | 43.8% |
| CH | Miguel Vargas | 28 | 0.391 | 0.696 | 0.304 | 0.505 | 0.533 | 17.4% | 26.7% | 3.9% |
| FC | Drew Romo | 10 | 0.200 | 0.500 | 0.300 | 0.290 | 0.232 | 0.0% | 14.3% | 12.5% |
| SI | Munetaka Murakami | 27 | 0.250 | 0.550 | 0.300 | 0.430 | 0.443 | 36.4% | 25.9% | 31.5% |
| FC | Tristan Peters | 19 | 0.294 | 0.588 | 0.294 | 0.403 | 0.289 | 16.7% | 23.3% | 17.9% |
| FF | Miguel Vargas | 108 | 0.224 | 0.494 | 0.271 | 0.399 | 0.406 | 18.0% | 24.3% | 22.3% |
| FF | Andrew Benintendi | 72 | 0.270 | 0.540 | 0.270 | 0.382 | 0.345 | 16.3% | 36.6% | 23.9% |
| SI | Andrew Benintendi | 39 | 0.294 | 0.559 | 0.265 | 0.391 | 0.363 | 13.8% | 27.1% | 16.2% |
| SI | Miguel Vargas | 76 | 0.182 | 0.439 | 0.258 | 0.316 | 0.407 | 16.4% | 33.6% | 6.6% |
| CU | Andrew Benintendi | 4 | 0.250 | 0.500 | 0.250 | 0.312 | 0.342 | 0.0% | 30.0% | 22.2% |
| CU | Munetaka Murakami | 14 | 0.250 | 0.500 | 0.250 | 0.371 | 0.533 | 20.0% | 64.7% | 21.7% |
| FF | Chase Meidroth | 99 | 0.305 | 0.549 | 0.244 | 0.420 | 0.359 | 9.1% | 25.4% | 14.0% |
| SI | Colson Montgomery | 48 | 0.268 | 0.512 | 0.244 | 0.402 | 0.381 | 14.8% | 41.5% | 33.3% |
| FC | Miguel Vargas | 23 | 0.278 | 0.500 | 0.222 | 0.411 | 0.366 | 6.7% | 16.7% | 28.3% |
| FF | Derek Hill | 37 | 0.188 | 0.406 | 0.219 | 0.309 | 0.307 | 16.7% | 26.5% | 39.3% |
| FF | Sam Antonacci | 76 | 0.350 | 0.550 | 0.200 | 0.467 | 0.447 | 13.7% | 23.3% | 14.8% |
| CU | Miguel Vargas | 18 | 0.133 | 0.333 | 0.200 | 0.278 | 0.392 | 7.7% | 28.6% | 17.9% |
| CH | Derek Hill | 18 | 0.375 | 0.562 | 0.188 | 0.411 | 0.444 | 6.7% | 26.3% | 33.3% |
| CU | Colson Montgomery | 13 | 0.364 | 0.545 | 0.182 | 0.438 | 0.351 | 0.0% | 30.0% | 34.3% |
| FC | Sam Antonacci | 22 | 0.294 | 0.471 | 0.176 | 0.430 | 0.337 | 5.9% | 20.8% | 13.8% |
| FF | Tristan Peters | 81 | 0.286 | 0.457 | 0.171 | 0.351 | 0.334 | 5.3% | 19.1% | 17.8% |
| FF | Colson Montgomery | 127 | 0.175 | 0.342 | 0.167 | 0.268 | 0.252 | 9.0% | 27.1% | 32.8% |


## Home Starting Pitcher: Erick Fedde

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1292 |
| Batted/Result Events | 327 |
| Hits Allowed | 78 |
| Walks | 28 |
| Strikeouts | 52 |
| Home Runs | 15 |
| K Event Rate | 15.9% |
| BB Event Rate | 8.6% |
| HR Event Rate | 4.6% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | DET | 6.3 | 4 | 0 | 1 | 4 | 0 |
| 2026-06-14 | CWS | 4.3 | 3 | 0 | 1 | 4 | 0 |
| 2026-06-09 | CWS | 7.7 | 6 | 1 | 1 | 4 | 1 |
| 2026-06-03 | MIN | 6.0 | 2 | 0 | 1 | 2 | 0 |
| 2026-05-29 | CWS | 6.3 | 4 | 1 | 3 | 3 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 12.7% | 164 | 0.259 | 0.407 | 0.148 | 0.313 | 0.256 | 11.8% | 33.3% | 25.9% |
| CH | vs R | 1.0% | 13 | 0.667 | 1.667 | 1.000 | 0.967 | 0.430 | 0.0% | 25.0% | 33.3% |
| FC | vs L | 10.6% | 137 | 0.292 | 0.583 | 0.292 | 0.406 | 0.409 | 14.3% | 17.1% | 17.0% |
| FC | vs R | 7.6% | 98 | 0.367 | 0.900 | 0.533 | 0.536 | 0.408 | 14.8% | 37.5% | 10.9% |
| FF | vs L | 0.9% | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.179 | 0.0% | 0.0% | 0.0% |
| FF | vs R | 1.2% | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.333 | 0.0% | 100.0% | 50.0% |
| SI | vs L | 11.8% | 153 | 0.256 | 0.308 | 0.051 | 0.315 | 0.380 | 2.7% | 27.9% | 4.7% |
| SI | vs R | 15.6% | 201 | 0.326 | 0.558 | 0.233 | 0.415 | 0.368 | 8.8% | 33.3% | 12.7% |
| ST | vs L | 17.0% | 220 | 0.226 | 0.340 | 0.113 | 0.294 | 0.320 | 10.0% | 32.1% | 20.9% |
| ST | vs R | 21.3% | 275 | 0.217 | 0.362 | 0.145 | 0.273 | 0.242 | 5.0% | 13.9% | 21.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 78 | 4 | 1 | 4 | 0 |
| 2026-06-14 | 62 | 3 | 2 | 4 | 0 |
| 2026-06-09 | 88 | 6 | 0 | 4 | 1 |
| 2026-06-03 | 61 | 2 | 1 | 2 | 0 |
| 2026-05-29 | 84 | 4 | 3 | 3 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Angel Martínez | 26 | 0.391 | 0.826 | 0.435 | 0.531 | 0.393 | 11.8% | 35.1% | 10.9% |
| FC | Travis Bazzana | 9 | 0.286 | 0.714 | 0.429 | 0.472 | 0.468 | 0.0% | 27.8% | 20.8% |
| FC | Brayan Rocchio | 22 | 0.300 | 0.650 | 0.350 | 0.434 | 0.350 | 10.5% | 27.3% | 11.9% |
| FC | Austin Hedges | 11 | 0.333 | 0.667 | 0.333 | 0.427 | 0.097 | 0.0% | 11.8% | 27.6% |
| FC | Kyle Manzardo | 23 | 0.211 | 0.526 | 0.316 | 0.343 | 0.323 | 13.3% | 39.5% | 21.7% |
| CH | Rhys Hoskins | 24 | 0.105 | 0.421 | 0.316 | 0.254 | 0.265 | 16.7% | 42.9% | 40.0% |
| FC | David Fry | 12 | 0.200 | 0.500 | 0.300 | 0.358 | 0.342 | 14.3% | 6.7% | 32.0% |
| CH | Bo Naylor | 11 | 0.200 | 0.500 | 0.300 | 0.327 | 0.356 | 14.3% | 11.1% | 26.9% |
| SI | David Fry | 23 | 0.381 | 0.667 | 0.286 | 0.467 | 0.343 | 6.7% | 21.2% | 22.4% |
| FC | José Ramírez | 35 | 0.250 | 0.531 | 0.281 | 0.384 | 0.309 | 7.7% | 32.2% | 14.1% |
| FC | Chase Delauter | 21 | 0.389 | 0.667 | 0.278 | 0.486 | 0.412 | 13.3% | 33.3% | 16.7% |
| ST | Travis Bazzana | 11 | 0.182 | 0.455 | 0.273 | 0.264 | 0.241 | 14.3% | 20.0% | 31.2% |
| FC | Rhys Hoskins | 21 | 0.211 | 0.474 | 0.263 | 0.324 | 0.219 | 0.0% | 29.6% | 30.2% |
| ST | Brayan Rocchio | 14 | 0.167 | 0.417 | 0.250 | 0.371 | 0.286 | 9.1% | 12.5% | 22.7% |
| SI | Travis Bazzana | 47 | 0.316 | 0.553 | 0.237 | 0.433 | 0.400 | 8.6% | 34.4% | 15.4% |
| ST | Chase Delauter | 19 | 0.235 | 0.471 | 0.235 | 0.339 | 0.355 | 0.0% | 42.1% | 9.1% |
| CH | Travis Bazzana | 18 | 0.188 | 0.375 | 0.188 | 0.289 | 0.188 | 0.0% | 13.3% | 51.3% |
| FC | Daniel Schneemann | 20 | 0.294 | 0.471 | 0.176 | 0.385 | 0.305 | 7.1% | 20.8% | 16.1% |
| ST | Kyle Manzardo | 21 | 0.167 | 0.333 | 0.167 | 0.281 | 0.293 | 14.3% | 7.7% | 35.7% |
| CH | José Ramírez | 60 | 0.214 | 0.375 | 0.161 | 0.296 | 0.322 | 4.3% | 29.6% | 21.5% |
| SI | Kyle Manzardo | 44 | 0.289 | 0.447 | 0.158 | 0.390 | 0.481 | 15.4% | 39.1% | 22.2% |
| SI | Bo Naylor | 15 | 0.462 | 0.615 | 0.154 | 0.500 | 0.343 | 0.0% | 31.0% | 3.2% |
| SI | Chase Delauter | 42 | 0.361 | 0.500 | 0.139 | 0.421 | 0.406 | 0.0% | 30.9% | 3.4% |
| SI | Rhys Hoskins | 55 | 0.200 | 0.333 | 0.133 | 0.314 | 0.322 | 13.2% | 33.3% | 20.5% |
| FC | Steven Kwan | 28 | 0.192 | 0.308 | 0.115 | 0.223 | 0.266 | 0.0% | 15.4% | 2.4% |
| CH | Austin Hedges | 9 | 0.222 | 0.333 | 0.111 | 0.439 | 0.366 | 12.5% | 41.7% | 23.5% |
| CH | Angel Martínez | 47 | 0.239 | 0.348 | 0.109 | 0.253 | 0.287 | 7.5% | 28.1% | 21.3% |
| FC | Bo Naylor | 10 | 0.200 | 0.300 | 0.100 | 0.215 | 0.203 | 0.0% | 11.1% | 18.2% |
| SI | Daniel Schneemann | 38 | 0.226 | 0.323 | 0.097 | 0.322 | 0.348 | 0.0% | 30.2% | 22.6% |
| CH | David Fry | 17 | 0.143 | 0.214 | 0.071 | 0.250 | 0.260 | 0.0% | 27.3% | 34.1% |


## Cleveland Guardians Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| José Ramírez | 329 | 0.247 | 0.452 | 0.205 | 0.352 | 0.355 | 7.9% | 30.6% | 15.1% |
| Steven Kwan | 318 | 0.201 | 0.258 | 0.057 | 0.281 | 0.305 | 0.4% | 7.8% | 6.8% |
| Brayan Rocchio | 304 | 0.270 | 0.397 | 0.127 | 0.337 | 0.313 | 3.1% | 21.8% | 20.3% |
| Chase Delauter | 290 | 0.281 | 0.453 | 0.172 | 0.358 | 0.341 | 6.9% | 25.7% | 13.4% |
| Kyle Manzardo | 270 | 0.232 | 0.409 | 0.177 | 0.327 | 0.316 | 12.7% | 24.7% | 29.3% |
| Angel Martínez | 260 | 0.247 | 0.469 | 0.222 | 0.322 | 0.306 | 8.9% | 23.8% | 16.8% |
| Rhys Hoskins | 246 | 0.190 | 0.395 | 0.205 | 0.322 | 0.287 | 11.3% | 28.0% | 27.5% |
| Daniel Schneemann | 236 | 0.214 | 0.353 | 0.140 | 0.288 | 0.289 | 7.0% | 22.6% | 30.1% |
| Travis Bazzana | 220 | 0.284 | 0.500 | 0.216 | 0.383 | 0.323 | 6.1% | 25.3% | 24.2% |
| David Fry | 141 | 0.225 | 0.400 | 0.175 | 0.328 | 0.266 | 6.3% | 21.6% | 28.7% |
| Austin Hedges | 126 | 0.269 | 0.361 | 0.093 | 0.332 | 0.289 | 3.3% | 21.7% | 23.2% |
| Bo Naylor | 108 | 0.152 | 0.242 | 0.091 | 0.207 | 0.295 | 9.7% | 24.3% | 14.9% |


## Chicago White Sox Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Miguel Vargas | 354 | 0.231 | 0.458 | 0.227 | 0.358 | 0.395 | 14.4% | 27.8% | 17.5% |
| Chase Meidroth | 343 | 0.275 | 0.402 | 0.127 | 0.334 | 0.282 | 4.9% | 23.1% | 18.5% |
| Colson Montgomery | 335 | 0.209 | 0.456 | 0.247 | 0.327 | 0.324 | 13.6% | 30.7% | 35.1% |
| Munetaka Murakami | 264 | 0.236 | 0.546 | 0.310 | 0.394 | 0.379 | 20.5% | 37.1% | 38.9% |
| Andrew Benintendi | 258 | 0.235 | 0.432 | 0.197 | 0.318 | 0.322 | 12.0% | 28.4% | 27.8% |
| Sam Antonacci | 249 | 0.289 | 0.417 | 0.128 | 0.377 | 0.376 | 7.6% | 23.1% | 13.4% |
| Tristan Peters | 233 | 0.290 | 0.449 | 0.159 | 0.352 | 0.299 | 4.8% | 19.8% | 19.4% |
| Edgar Quero | 191 | 0.181 | 0.223 | 0.042 | 0.237 | 0.260 | 2.3% | 21.6% | 21.4% |
| Luisangel Acuña | 163 | 0.219 | 0.258 | 0.040 | 0.235 | 0.270 | 4.8% | 26.4% | 21.6% |
| Drew Romo | 111 | 0.143 | 0.347 | 0.204 | 0.258 | 0.266 | 9.9% | 22.8% | 30.2% |
| Derek Hill | 106 | 0.215 | 0.355 | 0.140 | 0.291 | 0.302 | 8.3% | 20.2% | 33.5% |
| Everson Pereira | 92 | 0.244 | 0.451 | 0.207 | 0.331 | 0.303 | 12.3% | 23.9% | 31.7% |


## Bullpen Fatigue Report

### Cleveland Guardians Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Cade Smith | 2026-06-22 | 1.2 | 28 |
| Colin Holderman | 2026-06-21 | 1.0 | 9 |
| Colin Holderman | 2026-06-23 | 0.1 | 6 |
| Hunter Gaddis | 2026-06-21 | 1.0 | 14 |
| Matt Festa | 2026-06-20 | 1.0 | 15 |
| Shawn Armstrong | 2026-06-22 | 1.0 | 14 |
| Tim Herrin | 2026-06-22 | 1.0 | 16 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Colin Holderman


### Chicago White Sox Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brandon Eisert | 2026-06-21 | 0.0 | 14 |
| Bryan Hudson | 2026-06-21 | 1.0 | 10 |
| Bryan Hudson | 2026-06-22 | 1.1 | 23 |
| Chris Murphy | 2026-06-20 | 1.0 | 16 |
| Chris Murphy | 2026-06-22 | 0.2 | 6 |
| Grant Taylor | 2026-06-21 | 1.0 | 20 |
| Grant Taylor | 2026-06-22 | 0.2 | 30 |
| Joe Rock | 2026-06-20 | 2.1 | 47 |
| Jordan Hicks | 2026-06-21 | 0.0 | 2 |
| Sean Newcomb | 2026-06-23 | 2.2 | 45 |
| Seranthony Domínguez | 2026-06-21 | 1.0 | 27 |
| Seranthony Domínguez | 2026-06-22 | 0.1 | 22 |
| Trevor Richards | 2026-06-20 | 1.0 | 16 |
| Tyler Davis | 2026-06-20 | 0.2 | 28 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Sean Newcomb



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | José Ramírez | 329 | 0.247 | 0.452 | 0.205 | 0.352 | 7.9% | 30.6% |
| 2 | Steven Kwan | 318 | 0.201 | 0.258 | 0.057 | 0.281 | 0.4% | 7.8% |
| 3 | Brayan Rocchio | 304 | 0.270 | 0.397 | 0.127 | 0.337 | 3.1% | 21.8% |
| 4 | Chase Delauter | 290 | 0.281 | 0.453 | 0.172 | 0.358 | 6.9% | 25.7% |
| 5 | Kyle Manzardo | 270 | 0.232 | 0.409 | 0.177 | 0.327 | 12.7% | 24.7% |
| 6 | Angel Martínez | 260 | 0.247 | 0.469 | 0.222 | 0.322 | 8.9% | 23.8% |
| 7 | Rhys Hoskins | 246 | 0.190 | 0.395 | 0.205 | 0.322 | 11.3% | 28.0% |
| 8 | Daniel Schneemann | 236 | 0.214 | 0.353 | 0.140 | 0.288 | 7.0% | 22.6% |
| 9 | Travis Bazzana | 220 | 0.284 | 0.500 | 0.216 | 0.383 | 6.1% | 25.3% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Miguel Vargas | 354 | 0.231 | 0.458 | 0.227 | 0.358 | 14.4% | 27.8% |
| 2 | Chase Meidroth | 343 | 0.275 | 0.402 | 0.127 | 0.334 | 4.9% | 23.1% |
| 3 | Colson Montgomery | 335 | 0.209 | 0.456 | 0.247 | 0.327 | 13.6% | 30.7% |
| 4 | Munetaka Murakami | 264 | 0.236 | 0.546 | 0.310 | 0.394 | 20.5% | 37.1% |
| 5 | Andrew Benintendi | 258 | 0.235 | 0.432 | 0.197 | 0.318 | 12.0% | 28.4% |
| 6 | Sam Antonacci | 249 | 0.289 | 0.417 | 0.128 | 0.377 | 7.6% | 23.1% |
| 7 | Tristan Peters | 233 | 0.290 | 0.449 | 0.159 | 0.352 | 4.8% | 19.8% |
| 8 | Edgar Quero | 191 | 0.181 | 0.223 | 0.042 | 0.237 | 2.3% | 21.6% |
| 9 | Luisangel Acuña | 163 | 0.219 | 0.258 | 0.040 | 0.235 | 4.8% | 26.4% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6693 |
| Hits Allowed | 1410 |
| Walks/HBP | 674 |
| Strikeouts | 1553 |
| Home Runs Allowed | 208 |
| K Event Rate | 23.2% |
| BB/HBP Event Rate | 10.1% |
| HR Event Rate | 3.1% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6632 |
| Hits Allowed | 1386 |
| Walks/HBP | 741 |
| Strikeouts | 1510 |
| Home Runs Allowed | 219 |
| K Event Rate | 22.8% |
| BB/HBP Event Rate | 11.2% |
| HR Event Rate | 3.3% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FC, FF, SI, CH, CU
- Home pitcher pitch mix to inspect: ST, SI, FC, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 5. Boston Red Sox @ Colorado Rockies

## Game Context

| Field | Value |
| --- | --- |
| Park | Coors Field |
| Time | 2026-06-24T19:10:00Z |
| Away Team | Boston Red Sox |
| Home Team | Colorado Rockies |
| Away Probable Pitcher | Ranger Suarez |
| Home Probable Pitcher | Kyle Freeland |


## Away Starting Pitcher: Ranger Suarez

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1267 |
| Batted/Result Events | 333 |
| Hits Allowed | 71 |
| Walks | 25 |
| Strikeouts | 79 |
| Home Runs | 6 |
| K Event Rate | 23.7% |
| BB Event Rate | 7.5% |
| HR Event Rate | 1.8% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | SEA | 8.0 | 1 | 0 | 3 | 5 | 0 |
| 2026-06-13 | BOS | 7.7 | 6 | 0 | 2 | 7 | 0 |
| 2026-06-07 | NYY | 8.3 | 6 | 0 | 0 | 6 | 0 |
| 2026-05-31 | CLE | 8.3 | 8 | 0 | 3 | 10 | 0 |
| 2026-05-26 | BOS | 8.3 | 6 | 1 | 4 | 4 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 2.1% | 26 | 0.250 | 0.250 | 0.000 | 0.225 | 0.325 | 0.0% | 28.6% | 27.3% |
| CH | vs R | 13.1% | 166 | 0.233 | 0.442 | 0.209 | 0.311 | 0.290 | 5.7% | 16.7% | 29.3% |
| CU | vs L | 4.7% | 59 | 0.059 | 0.118 | 0.059 | 0.139 | 0.120 | 0.0% | 12.5% | 45.2% |
| CU | vs R | 10.7% | 135 | 0.250 | 0.375 | 0.125 | 0.318 | 0.263 | 11.8% | 25.8% | 40.0% |
| FC | vs L | 0.9% | 11 | 0.500 | 2.000 | 1.500 | 1.000 | 1.676 | 50.0% | 25.0% | 0.0% |
| FC | vs R | 20.4% | 258 | 0.242 | 0.355 | 0.113 | 0.290 | 0.282 | 3.6% | 18.3% | 16.8% |
| FF | vs L | 7.3% | 92 | 0.308 | 0.385 | 0.077 | 0.378 | 0.431 | 11.1% | 20.0% | 24.3% |
| FF | vs R | 13.8% | 175 | 0.129 | 0.226 | 0.097 | 0.185 | 0.236 | 16.7% | 18.5% | 11.9% |
| SI | vs L | 10.6% | 134 | 0.308 | 0.436 | 0.128 | 0.333 | 0.269 | 6.7% | 18.5% | 16.9% |
| SI | vs R | 14.5% | 184 | 0.245 | 0.264 | 0.019 | 0.289 | 0.344 | 0.0% | 30.5% | 10.3% |
| SL | vs L | 1.7% | 22 | 0.286 | 0.429 | 0.143 | 0.307 | 0.298 | 0.0% | 16.7% | 40.0% |
| SL | vs R | 0.2% | 3 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 100.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 94 | 1 | 3 | 5 | 0 |
| 2026-06-13 | 97 | 6 | 2 | 7 | 0 |
| 2026-06-07 | 90 | 6 | 0 | 6 | 0 |
| 2026-05-31 | 93 | 8 | 2 | 10 | 0 |
| 2026-05-26 | 91 | 6 | 3 | 4 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Mickey Moniak | 12 | 0.182 | 0.727 | 0.545 | 0.392 | 0.468 | 66.7% | 41.7% | 45.2% |
| FC | Willi Castro | 16 | 0.600 | 1.000 | 0.400 | 0.684 | 0.553 | 25.0% | 28.0% | 15.6% |
| CU | Troy Johnston | 20 | 0.389 | 0.778 | 0.389 | 0.510 | 0.406 | 7.7% | 36.4% | 27.8% |
| CU | Hunter Goodman | 31 | 0.200 | 0.533 | 0.333 | 0.315 | 0.280 | 17.6% | 44.4% | 36.7% |
| SI | Edouard Julien | 18 | 0.438 | 0.750 | 0.312 | 0.528 | 0.461 | 13.3% | 29.4% | 8.1% |
| FC | Hunter Goodman | 17 | 0.438 | 0.750 | 0.312 | 0.518 | 0.456 | 20.0% | 32.1% | 26.8% |
| FF | Brett Sullivan | 39 | 0.278 | 0.583 | 0.306 | 0.369 | 0.308 | 6.9% | 23.2% | 10.8% |
| FC | Mickey Moniak | 15 | 0.357 | 0.643 | 0.286 | 0.443 | 0.397 | 9.1% | 34.8% | 16.1% |
| FC | Tj Rumfield | 22 | 0.286 | 0.571 | 0.286 | 0.375 | 0.291 | 9.5% | 17.1% | 11.8% |
| CH | Hunter Goodman | 28 | 0.231 | 0.500 | 0.269 | 0.366 | 0.245 | 11.8% | 22.2% | 42.6% |
| FF | Mickey Moniak | 52 | 0.300 | 0.560 | 0.260 | 0.377 | 0.309 | 8.1% | 21.3% | 19.2% |
| SI | Jake Mccarthy | 43 | 0.400 | 0.650 | 0.250 | 0.466 | 0.379 | 8.8% | 29.8% | 14.3% |
| CU | Brenton Doyle | 4 | 0.250 | 0.500 | 0.250 | 0.312 | 0.000 | 100.0% | 66.7% | 25.0% |
| CU | Ezequiel Tovar | 13 | 0.250 | 0.500 | 0.250 | 0.342 | 0.346 | 25.0% | 15.4% | 23.8% |
| CH | Ezequiel Tovar | 25 | 0.200 | 0.440 | 0.240 | 0.304 | 0.225 | 6.7% | 22.2% | 41.0% |
| SI | Hunter Goodman | 46 | 0.385 | 0.615 | 0.231 | 0.471 | 0.416 | 11.8% | 26.2% | 16.0% |
| FF | Hunter Goodman | 96 | 0.188 | 0.412 | 0.224 | 0.305 | 0.308 | 18.5% | 25.5% | 22.4% |
| FC | Ezequiel Tovar | 21 | 0.278 | 0.500 | 0.222 | 0.424 | 0.351 | 6.7% | 32.1% | 28.9% |
| FF | Kyle Karros | 97 | 0.358 | 0.568 | 0.210 | 0.447 | 0.399 | 7.6% | 28.9% | 5.7% |
| FF | Tj Rumfield | 111 | 0.292 | 0.500 | 0.208 | 0.380 | 0.357 | 9.1% | 21.8% | 10.6% |
| CU | Tj Rumfield | 22 | 0.250 | 0.450 | 0.200 | 0.375 | 0.274 | 0.0% | 15.4% | 30.2% |
| CH | Brett Sullivan | 16 | 0.133 | 0.333 | 0.200 | 0.178 | 0.154 | 0.0% | 5.6% | 17.4% |
| CH | Mickey Moniak | 29 | 0.179 | 0.357 | 0.179 | 0.217 | 0.214 | 4.5% | 36.4% | 32.8% |
| FF | Jake Mccarthy | 104 | 0.308 | 0.484 | 0.176 | 0.357 | 0.356 | 3.7% | 14.6% | 11.4% |
| SI | Willi Castro | 28 | 0.261 | 0.435 | 0.174 | 0.402 | 0.368 | 5.3% | 23.3% | 22.4% |
| CH | Tj Rumfield | 44 | 0.220 | 0.390 | 0.171 | 0.310 | 0.251 | 5.7% | 24.6% | 21.7% |
| FC | Edouard Julien | 23 | 0.278 | 0.444 | 0.167 | 0.396 | 0.295 | 10.0% | 11.5% | 18.4% |
| CU | Willi Castro | 26 | 0.375 | 0.542 | 0.167 | 0.421 | 0.342 | 5.0% | 30.3% | 24.4% |
| SI | Brenton Doyle | 21 | 0.211 | 0.368 | 0.158 | 0.376 | 0.301 | 6.2% | 20.0% | 10.8% |
| FF | Tyler Freeman | 57 | 0.400 | 0.540 | 0.140 | 0.437 | 0.331 | 2.2% | 17.9% | 8.0% |


## Home Starting Pitcher: Kyle Freeland

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1184 |
| Batted/Result Events | 322 |
| Hits Allowed | 92 |
| Walks | 17 |
| Strikeouts | 59 |
| Home Runs | 14 |
| K Event Rate | 18.3% |
| BB Event Rate | 5.3% |
| HR Event Rate | 4.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | COL | 8.7 | 4 | 0 | 0 | 8 | 0 |
| 2026-06-13 | ATH | 9.0 | 10 | 1 | 0 | 4 | 1 |
| 2026-06-07 | COL | 7.3 | 7 | 0 | 1 | 2 | 0 |
| 2026-06-01 | LAA | 9.3 | 7 | 1 | 1 | 4 | 1 |
| 2026-05-26 | LAD | 7.3 | 9 | 3 | 1 | 4 | 3 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.5% | 6 | 0.000 | 0.000 | 0.000 | 0.350 | 0.366 | 0.0% | 0.0% | 33.3% |
| CH | vs R | 14.2% | 168 | 0.296 | 0.463 | 0.167 | 0.387 | 0.366 | 6.4% | 36.8% | 17.6% |
| FC | vs L | 3.2% | 38 | 0.273 | 0.273 | 0.000 | 0.245 | 0.354 | 0.0% | 11.8% | 34.6% |
| FC | vs R | 16.2% | 192 | 0.326 | 0.442 | 0.116 | 0.364 | 0.334 | 13.9% | 29.3% | 16.7% |
| FF | vs L | 5.5% | 65 | 0.545 | 0.636 | 0.091 | 0.523 | 0.324 | 0.0% | 20.8% | 7.7% |
| FF | vs R | 21.5% | 254 | 0.355 | 0.790 | 0.435 | 0.516 | 0.419 | 11.5% | 25.2% | 11.3% |
| KC | vs L | 4.0% | 47 | 0.125 | 0.250 | 0.125 | 0.205 | 0.271 | 0.0% | 36.8% | 21.4% |
| KC | vs R | 19.3% | 228 | 0.347 | 0.551 | 0.204 | 0.404 | 0.386 | 11.1% | 35.2% | 29.4% |
| SI | vs L | 3.0% | 35 | 0.400 | 0.800 | 0.400 | 0.505 | 0.490 | 22.2% | 56.2% | 10.5% |
| SI | vs R | 1.4% | 17 | 1.000 | 1.500 | 0.500 | 0.950 | 0.358 | 0.0% | 0.0% | 0.0% |
| ST | vs L | 3.5% | 42 | 0.083 | 0.083 | 0.000 | 0.114 | 0.175 | 0.0% | 6.2% | 29.2% |
| ST | vs R | 7.8% | 92 | 0.185 | 0.444 | 0.259 | 0.305 | 0.345 | 18.8% | 30.8% | 27.9% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 81 | 4 | 0 | 8 | 0 |
| 2026-06-13 | 95 | 10 | 0 | 4 | 1 |
| 2026-06-07 | 89 | 7 | 1 | 2 | 0 |
| 2026-06-01 | 91 | 7 | 1 | 4 | 1 |
| 2026-05-26 | 81 | 9 | 0 | 4 | 3 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Marcelo Mayer | 7 | 0.167 | 0.667 | 0.500 | 0.386 | 0.281 | 33.3% | 44.4% | 38.9% |
| ST | Ceddanne Rafaela | 16 | 0.375 | 0.812 | 0.438 | 0.497 | 0.310 | 18.2% | 16.7% | 29.7% |
| ST | Carlos Narváez | 11 | 0.273 | 0.636 | 0.364 | 0.377 | 0.116 | 20.0% | 21.4% | 37.5% |
| KC | Jarren Duran | 10 | 0.200 | 0.500 | 0.300 | 0.285 | 0.116 | 0.0% | 25.0% | 60.0% |
| FC | Roman Anthony | 7 | 0.286 | 0.571 | 0.286 | 0.357 | 0.362 | 0.0% | 60.0% | 14.3% |
| CH | Ceddanne Rafaela | 34 | 0.312 | 0.594 | 0.281 | 0.428 | 0.245 | 12.5% | 23.1% | 30.6% |
| FF | Jarren Duran | 97 | 0.190 | 0.452 | 0.262 | 0.325 | 0.333 | 15.4% | 19.4% | 32.7% |
| CH | Willson Contreras | 42 | 0.317 | 0.561 | 0.244 | 0.381 | 0.317 | 20.0% | 33.3% | 39.8% |
| CH | Andruw Monasterio | 13 | 0.231 | 0.462 | 0.231 | 0.292 | 0.322 | 10.0% | 24.0% | 28.2% |
| FF | Caleb Durbin | 80 | 0.286 | 0.514 | 0.229 | 0.387 | 0.314 | 5.3% | 25.5% | 7.1% |
| CH | Masataka Yoshida | 26 | 0.318 | 0.545 | 0.227 | 0.419 | 0.415 | 5.6% | 27.6% | 16.7% |
| FF | Wilyer Abreu | 99 | 0.226 | 0.440 | 0.214 | 0.345 | 0.308 | 11.9% | 20.1% | 19.8% |
| FF | Andruw Monasterio | 45 | 0.225 | 0.425 | 0.200 | 0.321 | 0.297 | 7.7% | 14.3% | 18.6% |
| FC | Willson Contreras | 19 | 0.267 | 0.467 | 0.200 | 0.355 | 0.339 | 20.0% | 61.1% | 45.5% |
| FC | Wilyer Abreu | 32 | 0.333 | 0.533 | 0.200 | 0.392 | 0.430 | 15.4% | 28.6% | 5.8% |
| ST | Isiah Kiner-Falefa | 5 | 0.200 | 0.400 | 0.200 | 0.250 | 0.126 | 0.0% | 33.3% | 33.3% |
| CH | Jarren Duran | 42 | 0.179 | 0.359 | 0.179 | 0.244 | 0.275 | 13.3% | 29.5% | 36.5% |
| ST | Wilyer Abreu | 15 | 0.417 | 0.583 | 0.167 | 0.440 | 0.480 | 22.2% | 25.9% | 15.2% |
| FC | Jarren Duran | 29 | 0.217 | 0.348 | 0.130 | 0.314 | 0.355 | 5.0% | 31.4% | 22.0% |
| CH | Caleb Durbin | 26 | 0.130 | 0.261 | 0.130 | 0.198 | 0.273 | 5.6% | 23.1% | 37.5% |
| FC | Caleb Durbin | 19 | 0.235 | 0.353 | 0.118 | 0.347 | 0.284 | 0.0% | 23.3% | 10.8% |
| FF | Trevor Story | 47 | 0.250 | 0.364 | 0.114 | 0.293 | 0.244 | 3.8% | 19.0% | 25.6% |
| FF | Ceddanne Rafaela | 91 | 0.259 | 0.370 | 0.111 | 0.320 | 0.300 | 5.2% | 20.6% | 21.6% |
| FF | Willson Contreras | 96 | 0.231 | 0.333 | 0.103 | 0.323 | 0.333 | 5.5% | 18.6% | 28.0% |
| FF | Isiah Kiner-Falefa | 47 | 0.179 | 0.282 | 0.103 | 0.273 | 0.275 | 0.0% | 10.8% | 8.2% |
| FC | Isiah Kiner-Falefa | 20 | 0.200 | 0.300 | 0.100 | 0.215 | 0.266 | 5.9% | 27.3% | 15.4% |
| ST | Masataka Yoshida | 13 | 0.300 | 0.400 | 0.100 | 0.396 | 0.383 | 0.0% | 33.3% | 16.7% |
| FF | Roman Anthony | 40 | 0.333 | 0.424 | 0.091 | 0.396 | 0.442 | 14.8% | 32.7% | 12.9% |
| FF | Marcelo Mayer | 74 | 0.258 | 0.333 | 0.076 | 0.330 | 0.289 | 9.1% | 19.6% | 14.3% |
| CH | Trevor Story | 16 | 0.188 | 0.250 | 0.062 | 0.191 | 0.193 | 0.0% | 20.0% | 43.9% |


## Boston Red Sox Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jarren Duran | 340 | 0.200 | 0.358 | 0.158 | 0.279 | 0.290 | 11.7% | 26.6% | 32.7% |
| Wilyer Abreu | 339 | 0.273 | 0.447 | 0.174 | 0.340 | 0.344 | 12.0% | 24.4% | 20.2% |
| Willson Contreras | 329 | 0.277 | 0.507 | 0.230 | 0.386 | 0.370 | 12.6% | 28.8% | 29.2% |
| Ceddanne Rafaela | 311 | 0.289 | 0.453 | 0.164 | 0.358 | 0.292 | 5.9% | 22.2% | 23.3% |
| Caleb Durbin | 271 | 0.230 | 0.367 | 0.137 | 0.294 | 0.284 | 2.8% | 21.0% | 15.2% |
| Marcelo Mayer | 242 | 0.217 | 0.304 | 0.088 | 0.281 | 0.257 | 6.4% | 26.8% | 23.9% |
| Trevor Story | 194 | 0.225 | 0.335 | 0.110 | 0.286 | 0.248 | 4.0% | 22.1% | 27.8% |
| Masataka Yoshida | 188 | 0.240 | 0.329 | 0.090 | 0.299 | 0.304 | 1.4% | 26.9% | 14.6% |
| Carlos Narváez | 158 | 0.190 | 0.268 | 0.077 | 0.259 | 0.276 | 6.4% | 19.8% | 28.5% |
| Isiah Kiner-Falefa | 151 | 0.255 | 0.328 | 0.073 | 0.300 | 0.312 | 3.4% | 17.1% | 14.8% |
| Roman Anthony | 145 | 0.240 | 0.322 | 0.083 | 0.318 | 0.352 | 9.6% | 31.2% | 26.6% |
| Andruw Monasterio | 143 | 0.222 | 0.341 | 0.119 | 0.274 | 0.274 | 5.0% | 17.8% | 17.7% |


## Colorado Rockies Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hunter Goodman | 333 | 0.255 | 0.530 | 0.275 | 0.368 | 0.316 | 15.8% | 28.4% | 31.8% |
| Tj Rumfield | 333 | 0.273 | 0.465 | 0.192 | 0.360 | 0.318 | 6.0% | 21.7% | 17.6% |
| Ezequiel Tovar | 299 | 0.213 | 0.350 | 0.137 | 0.277 | 0.283 | 8.8% | 18.8% | 27.5% |
| Troy Johnston | 287 | 0.323 | 0.475 | 0.152 | 0.375 | 0.333 | 2.9% | 24.2% | 21.7% |
| Willi Castro | 285 | 0.280 | 0.417 | 0.138 | 0.345 | 0.308 | 6.7% | 23.3% | 26.8% |
| Kyle Karros | 269 | 0.251 | 0.374 | 0.123 | 0.329 | 0.331 | 6.7% | 26.4% | 23.8% |
| Jake Mccarthy | 253 | 0.307 | 0.472 | 0.165 | 0.356 | 0.308 | 4.2% | 16.4% | 20.3% |
| Edouard Julien | 234 | 0.238 | 0.337 | 0.099 | 0.315 | 0.339 | 8.0% | 27.1% | 22.7% |
| Tyler Freeman | 199 | 0.272 | 0.364 | 0.092 | 0.327 | 0.317 | 1.3% | 20.9% | 10.6% |
| Mickey Moniak | 184 | 0.271 | 0.559 | 0.288 | 0.371 | 0.321 | 12.5% | 26.6% | 26.6% |
| Brenton Doyle | 145 | 0.227 | 0.295 | 0.068 | 0.283 | 0.248 | 7.0% | 18.4% | 25.6% |
| Brett Sullivan | 124 | 0.226 | 0.435 | 0.209 | 0.301 | 0.267 | 4.3% | 20.2% | 16.7% |


## Bullpen Fatigue Report

### Boston Red Sox Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Aroldis Chapman | 2026-06-22 | 0.0 | 8 |
| Danny Coulombe | 2026-06-20 | 1.0 | 5 |
| Danny Coulombe | 2026-06-21 | 1.0 | 18 |
| Garrett Whitlock | 2026-06-20 | 1.0 | 15 |
| Garrett Whitlock | 2026-06-22 | 1.0 | 11 |
| Garrett Whitlock | 2026-06-23 | 1.0 | 14 |
| Justin Slaten | 2026-06-23 | 1.0 | 7 |
| Ryan Watson | 2026-06-21 | 1.0 | 12 |
| Tyron Guerrero | 2026-06-20 | 1.0 | 14 |
| Tyron Guerrero | 2026-06-22 | 1.0 | 8 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Garrett Whitlock, Justin Slaten


### Colorado Rockies Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brennan Bernardino | 2026-06-20 | 1.0 | 21 |
| Brennan Bernardino | 2026-06-22 | 1.0 | 18 |
| Jaden Hill | 2026-06-20 | 0.2 | 13 |
| Jimmy Herget | 2026-06-20 | 1.1 | 20 |
| John Brebbia | 2026-06-21 | 2.0 | 24 |
| Juan Mejia | 2026-06-21 | 1.2 | 32 |
| Juan Mejia | 2026-06-23 | 1.0 | 10 |
| Victor Vodnik | 2026-06-22 | 2.0 | 30 |
| Zach Agnos | 2026-06-23 | 3.0 | 41 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Juan Mejia, Zach Agnos



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Jarren Duran | 340 | 0.200 | 0.358 | 0.158 | 0.279 | 11.7% | 26.6% |
| 2 | Wilyer Abreu | 339 | 0.273 | 0.447 | 0.174 | 0.340 | 12.0% | 24.4% |
| 3 | Willson Contreras | 329 | 0.277 | 0.507 | 0.230 | 0.386 | 12.6% | 28.8% |
| 4 | Ceddanne Rafaela | 311 | 0.289 | 0.453 | 0.164 | 0.358 | 5.9% | 22.2% |
| 5 | Caleb Durbin | 271 | 0.230 | 0.367 | 0.137 | 0.294 | 2.8% | 21.0% |
| 6 | Marcelo Mayer | 242 | 0.217 | 0.304 | 0.088 | 0.281 | 6.4% | 26.8% |
| 7 | Trevor Story | 194 | 0.225 | 0.335 | 0.110 | 0.286 | 4.0% | 22.1% |
| 8 | Masataka Yoshida | 188 | 0.240 | 0.329 | 0.090 | 0.299 | 1.4% | 26.9% |
| 9 | Carlos Narváez | 158 | 0.190 | 0.268 | 0.077 | 0.259 | 6.4% | 19.8% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Hunter Goodman | 333 | 0.255 | 0.530 | 0.275 | 0.368 | 15.8% | 28.4% |
| 2 | Tj Rumfield | 333 | 0.273 | 0.465 | 0.192 | 0.360 | 6.0% | 21.7% |
| 3 | Ezequiel Tovar | 299 | 0.213 | 0.350 | 0.137 | 0.277 | 8.8% | 18.8% |
| 4 | Troy Johnston | 287 | 0.323 | 0.475 | 0.152 | 0.375 | 2.9% | 24.2% |
| 5 | Willi Castro | 285 | 0.280 | 0.417 | 0.138 | 0.345 | 6.7% | 23.3% |
| 6 | Kyle Karros | 269 | 0.251 | 0.374 | 0.123 | 0.329 | 6.7% | 26.4% |
| 7 | Jake Mccarthy | 253 | 0.307 | 0.472 | 0.165 | 0.356 | 4.2% | 16.4% |
| 8 | Edouard Julien | 234 | 0.238 | 0.337 | 0.099 | 0.315 | 8.0% | 27.1% |
| 9 | Tyler Freeman | 199 | 0.272 | 0.364 | 0.092 | 0.327 | 1.3% | 20.9% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6437 |
| Hits Allowed | 1406 |
| Walks/HBP | 597 |
| Strikeouts | 1431 |
| Home Runs Allowed | 163 |
| K Event Rate | 22.2% |
| BB/HBP Event Rate | 9.3% |
| HR Event Rate | 2.5% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6903 |
| Hits Allowed | 1677 |
| Walks/HBP | 650 |
| Strikeouts | 1412 |
| Home Runs Allowed | 220 |
| K Event Rate | 20.5% |
| BB/HBP Event Rate | 9.4% |
| HR Event Rate | 3.2% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: SI, FC, FF, CU, CH
- Home pitcher pitch mix to inspect: FF, KC, FC, CH, ST
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 6. Baltimore Orioles @ Los Angeles Angels

## Game Context

| Field | Value |
| --- | --- |
| Park | Angel Stadium |
| Time | 2026-06-24T20:07:00Z |
| Away Team | Baltimore Orioles |
| Home Team | Los Angeles Angels |
| Away Probable Pitcher | Trey Gibson |
| Home Probable Pitcher | José Soriano |


## Away Starting Pitcher: Trey Gibson

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 475 |
| Batted/Result Events | 122 |
| Hits Allowed | 28 |
| Walks | 17 |
| Strikeouts | 20 |
| Home Runs | 4 |
| K Event Rate | 16.4% |
| BB Event Rate | 13.9% |
| HR Event Rate | 3.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | LAD | 8.7 | 7 | 0 | 4 | 8 | 0 |
| 2026-06-13 | BAL | 7.3 | 3 | 2 | 6 | 7 | 2 |
| 2026-06-08 | BAL | 6.3 | 5 | 0 | 1 | 0 | 0 |
| 2026-05-27 | BAL | 8.0 | 6 | 0 | 4 | 1 | 0 |
| 2026-05-08 | BAL | 3.3 | 3 | 0 | 1 | 2 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 12.2% | 58 | 0.308 | 0.538 | 0.231 | 0.407 | 0.403 | 10.0% | 46.2% | 33.3% |
| CU | vs R | 1.9% | 9 | 1.000 | 4.000 | 3.000 | 2.000 | 1.783 | 100.0% | 33.3% | 0.0% |
| FC | vs L | 11.4% | 54 | 0.545 | 0.636 | 0.091 | 0.523 | 0.495 | 18.2% | 29.4% | 15.0% |
| FC | vs R | 8.6% | 41 | 0.286 | 0.429 | 0.143 | 0.425 | 0.357 | 0.0% | 23.1% | 17.6% |
| FF | vs L | 12.4% | 59 | 0.364 | 0.455 | 0.091 | 0.432 | 0.387 | 11.1% | 27.8% | 10.0% |
| FF | vs R | 3.8% | 18 | 0.333 | 0.333 | 0.000 | 0.400 | 0.218 | 0.0% | 0.0% | 14.3% |
| SI | vs L | 8.0% | 38 | 0.111 | 0.111 | 0.000 | 0.209 | 0.406 | 0.0% | 28.6% | 11.8% |
| SI | vs R | 18.9% | 90 | 0.167 | 0.167 | 0.000 | 0.239 | 0.316 | 13.3% | 16.7% | 16.7% |
| SL | vs L | 11.8% | 56 | 0.125 | 0.312 | 0.188 | 0.239 | 0.269 | 0.0% | 38.9% | 36.1% |
| SL | vs R | 8.8% | 42 | 0.182 | 0.182 | 0.000 | 0.283 | 0.366 | 0.0% | 47.1% | 15.0% |
| ST | vs R | 2.1% | 10 | 0.667 | 2.000 | 1.333 | 1.083 | 0.618 | 33.3% | 40.0% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 97 | 7 | 4 | 8 | 0 |
| 2026-06-13 | 93 | 3 | 5 | 7 | 2 |
| 2026-06-08 | 68 | 5 | 1 | 0 | 0 |
| 2026-05-27 | 100 | 6 | 4 | 1 | 0 |
| 2026-05-08 | 30 | 3 | 1 | 2 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Mike Trout | 30 | 0.348 | 0.913 | 0.565 | 0.562 | 0.476 | 19.0% | 33.3% | 18.4% |
| FC | Wade Meckler | 9 | 0.250 | 0.750 | 0.500 | 0.439 | 0.422 | 14.3% | 22.2% | 35.7% |
| CU | Yoán Moncada | 9 | 0.250 | 0.625 | 0.375 | 0.400 | 0.406 | 16.7% | 25.0% | 26.3% |
| FC | Zach Neto | 23 | 0.368 | 0.737 | 0.368 | 0.507 | 0.511 | 12.5% | 24.3% | 17.6% |
| CU | Jorge Soler | 11 | 0.273 | 0.636 | 0.364 | 0.377 | 0.456 | 25.0% | 41.7% | 35.0% |
| CU | Josh Lowe | 12 | 0.364 | 0.727 | 0.364 | 0.421 | 0.360 | 0.0% | 28.6% | 25.0% |
| CU | Logan O'Hoppe | 13 | 0.545 | 0.909 | 0.364 | 0.631 | 0.472 | 22.2% | 40.0% | 13.6% |
| FF | Jorge Soler | 69 | 0.230 | 0.590 | 0.361 | 0.380 | 0.276 | 18.4% | 31.6% | 28.6% |
| FF | Zach Neto | 106 | 0.272 | 0.598 | 0.326 | 0.400 | 0.351 | 16.7% | 25.5% | 20.9% |
| SL | Josh Lowe | 17 | 0.176 | 0.471 | 0.294 | 0.318 | 0.189 | 10.0% | 22.7% | 41.5% |
| SI | Yoán Moncada | 21 | 0.190 | 0.476 | 0.286 | 0.276 | 0.271 | 23.1% | 39.1% | 12.9% |
| FC | Oswald Peraza | 15 | 0.286 | 0.571 | 0.286 | 0.443 | 0.433 | 16.7% | 36.4% | 29.0% |
| FF | Vaughn Grissom | 41 | 0.182 | 0.455 | 0.273 | 0.313 | 0.364 | 14.3% | 23.2% | 18.2% |
| SI | Zach Neto | 56 | 0.289 | 0.556 | 0.267 | 0.424 | 0.443 | 23.3% | 26.7% | 16.5% |
| FF | Adam Frazier | 39 | 0.233 | 0.500 | 0.267 | 0.371 | 0.282 | 8.3% | 10.3% | 16.2% |
| FF | Mike Trout | 141 | 0.292 | 0.547 | 0.255 | 0.467 | 0.470 | 22.2% | 25.0% | 14.0% |
| FC | Adam Frazier | 4 | 0.500 | 0.750 | 0.250 | 0.537 | 0.202 | 0.0% | 9.1% | 16.7% |
| FF | Josh Lowe | 44 | 0.350 | 0.600 | 0.250 | 0.433 | 0.298 | 17.4% | 19.7% | 24.5% |
| FF | Jo Adell | 96 | 0.270 | 0.506 | 0.236 | 0.341 | 0.370 | 14.7% | 20.2% | 19.7% |
| SL | Nolan Schanuel | 27 | 0.211 | 0.421 | 0.211 | 0.376 | 0.365 | 0.0% | 9.4% | 34.0% |
| FC | Jorge Soler | 18 | 0.267 | 0.467 | 0.200 | 0.378 | 0.483 | 21.4% | 18.8% | 25.0% |
| SL | Zach Neto | 65 | 0.262 | 0.459 | 0.197 | 0.331 | 0.265 | 5.4% | 18.7% | 41.7% |
| SL | Jorge Soler | 52 | 0.213 | 0.404 | 0.191 | 0.320 | 0.280 | 11.5% | 16.7% | 47.4% |
| FF | Logan O'Hoppe | 53 | 0.229 | 0.396 | 0.167 | 0.308 | 0.396 | 15.4% | 30.1% | 16.5% |
| FF | Nolan Schanuel | 87 | 0.270 | 0.432 | 0.162 | 0.353 | 0.357 | 4.9% | 19.4% | 5.8% |
| CU | Jo Adell | 20 | 0.211 | 0.368 | 0.158 | 0.268 | 0.194 | 0.0% | 36.0% | 31.7% |
| FF | Oswald Peraza | 79 | 0.225 | 0.380 | 0.155 | 0.309 | 0.313 | 8.5% | 21.0% | 20.6% |
| CU | Vaughn Grissom | 15 | 0.385 | 0.538 | 0.154 | 0.440 | 0.379 | 7.7% | 31.6% | 17.4% |
| SL | Vaughn Grissom | 24 | 0.261 | 0.391 | 0.130 | 0.298 | 0.290 | 0.0% | 24.1% | 27.3% |
| SL | Jo Adell | 55 | 0.259 | 0.389 | 0.130 | 0.287 | 0.265 | 8.1% | 26.0% | 35.4% |


## Home Starting Pitcher: José Soriano

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1588 |
| Batted/Result Events | 396 |
| Hits Allowed | 72 |
| Walks | 49 |
| Strikeouts | 101 |
| Home Runs | 10 |
| K Event Rate | 25.5% |
| BB Event Rate | 12.4% |
| HR Event Rate | 2.5% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | ATH | 8.0 | 6 | 1 | 4 | 6 | 1 |
| 2026-06-13 | LAA | 6.3 | 3 | 0 | 2 | 5 | 0 |
| 2026-06-07 | LAD | 9.0 | 8 | 2 | 2 | 2 | 2 |
| 2026-06-01 | LAA | 8.3 | 3 | 1 | 9 | 7 | 1 |
| 2026-05-27 | DET | 8.0 | 7 | 1 | 4 | 4 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF | vs L | 13.2% | 209 | 0.333 | 0.689 | 0.356 | 0.487 | 0.447 | 20.0% | 25.0% | 19.8% |
| FF | vs R | 11.5% | 182 | 0.121 | 0.303 | 0.182 | 0.278 | 0.344 | 15.0% | 18.9% | 26.6% |
| FS | vs L | 15.5% | 246 | 0.131 | 0.131 | 0.000 | 0.154 | 0.196 | 0.0% | 18.8% | 40.5% |
| FS | vs R | 3.9% | 62 | 0.133 | 0.133 | 0.000 | 0.120 | 0.190 | 11.1% | 16.7% | 32.0% |
| KC | vs L | 11.0% | 174 | 0.189 | 0.351 | 0.162 | 0.263 | 0.243 | 10.0% | 23.7% | 36.7% |
| KC | vs R | 13.7% | 217 | 0.233 | 0.279 | 0.047 | 0.257 | 0.259 | 8.0% | 16.7% | 43.9% |
| SI | vs L | 12.2% | 193 | 0.381 | 0.452 | 0.071 | 0.433 | 0.478 | 10.0% | 41.0% | 16.1% |
| SI | vs R | 13.2% | 210 | 0.157 | 0.216 | 0.059 | 0.261 | 0.320 | 7.1% | 25.0% | 25.5% |
| SL | vs L | 0.6% | 10 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 100.0% | 25.0% |
| SL | vs R | 5.1% | 81 | 0.133 | 0.133 | 0.000 | 0.217 | 0.293 | 0.0% | 9.5% | 26.7% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 105 | 6 | 4 | 6 | 1 |
| 2026-06-13 | 76 | 3 | 2 | 5 | 0 |
| 2026-06-07 | 88 | 8 | 2 | 2 | 2 |
| 2026-06-01 | 108 | 3 | 7 | 7 | 1 |
| 2026-05-27 | 105 | 7 | 4 | 4 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SI | Colton Cowser | 23 | 0.353 | 0.882 | 0.529 | 0.561 | 0.517 | 27.3% | 21.7% | 21.2% |
| KC | Samuel Basallo | 6 | 0.167 | 0.667 | 0.500 | 0.333 | 0.302 | 50.0% | 33.3% | 46.2% |
| FS | Taylor Ward | 9 | 0.125 | 0.500 | 0.375 | 0.300 | 0.417 | 16.7% | 27.3% | 20.0% |
| FF | Pete Alonso | 98 | 0.281 | 0.629 | 0.348 | 0.402 | 0.439 | 26.2% | 37.1% | 23.7% |
| SI | Coby Mayo | 37 | 0.235 | 0.559 | 0.324 | 0.359 | 0.412 | 12.9% | 37.5% | 13.4% |
| FF | Jeremiah Jackson | 44 | 0.238 | 0.524 | 0.286 | 0.336 | 0.299 | 9.1% | 22.9% | 16.4% |
| FF | Adley Rutschman | 86 | 0.264 | 0.500 | 0.236 | 0.367 | 0.322 | 8.1% | 27.0% | 4.4% |
| SI | Leody Taveras | 32 | 0.423 | 0.654 | 0.231 | 0.520 | 0.469 | 4.3% | 26.3% | 18.4% |
| SI | Tyler O'Neill | 39 | 0.281 | 0.500 | 0.219 | 0.421 | 0.389 | 14.3% | 30.6% | 9.7% |
| FF | Samuel Basallo | 80 | 0.260 | 0.466 | 0.205 | 0.342 | 0.334 | 13.7% | 34.0% | 23.9% |
| FS | Jeremiah Jackson | 5 | 0.200 | 0.400 | 0.200 | 0.430 | 0.299 | 25.0% | 40.0% | 20.0% |
| SI | Gunnar Henderson | 69 | 0.290 | 0.484 | 0.194 | 0.395 | 0.365 | 7.7% | 27.6% | 10.8% |
| SI | Pete Alonso | 89 | 0.284 | 0.473 | 0.189 | 0.372 | 0.408 | 9.5% | 38.9% | 15.2% |
| FS | Samuel Basallo | 16 | 0.312 | 0.500 | 0.188 | 0.350 | 0.327 | 8.3% | 27.8% | 33.3% |
| FF | Taylor Ward | 114 | 0.308 | 0.495 | 0.187 | 0.416 | 0.433 | 10.9% | 23.5% | 18.1% |
| FF | Dylan Beavers | 43 | 0.237 | 0.421 | 0.184 | 0.334 | 0.385 | 13.3% | 19.4% | 12.3% |
| FS | Gunnar Henderson | 25 | 0.217 | 0.391 | 0.174 | 0.302 | 0.377 | 15.8% | 30.0% | 28.0% |
| SI | Jeremiah Jackson | 35 | 0.400 | 0.571 | 0.171 | 0.473 | 0.260 | 6.1% | 24.5% | 3.3% |
| SI | Adley Rutschman | 32 | 0.233 | 0.400 | 0.167 | 0.325 | 0.401 | 15.4% | 26.5% | 10.3% |
| FS | Adley Rutschman | 7 | 0.167 | 0.333 | 0.167 | 0.279 | 0.405 | 20.0% | 30.0% | 21.4% |
| FF | Colton Cowser | 66 | 0.220 | 0.380 | 0.160 | 0.364 | 0.416 | 14.6% | 27.3% | 14.3% |
| FF | Blaze Alexander | 58 | 0.260 | 0.420 | 0.160 | 0.339 | 0.361 | 14.3% | 21.4% | 28.4% |
| SI | Samuel Basallo | 24 | 0.158 | 0.316 | 0.158 | 0.342 | 0.389 | 6.7% | 10.5% | 8.9% |
| SI | Dylan Beavers | 17 | 0.308 | 0.462 | 0.154 | 0.418 | 0.445 | 0.0% | 32.0% | 7.1% |
| FF | Gunnar Henderson | 88 | 0.133 | 0.267 | 0.133 | 0.257 | 0.296 | 9.6% | 20.3% | 16.5% |
| FF | Coby Mayo | 61 | 0.200 | 0.320 | 0.120 | 0.309 | 0.350 | 6.1% | 25.0% | 13.9% |
| KC | Pete Alonso | 10 | 0.100 | 0.200 | 0.100 | 0.125 | 0.183 | 0.0% | 27.3% | 38.9% |
| FF | Tyler O'Neill | 44 | 0.150 | 0.250 | 0.100 | 0.219 | 0.292 | 3.0% | 29.0% | 16.7% |
| FF | Leody Taveras | 92 | 0.197 | 0.289 | 0.092 | 0.287 | 0.290 | 8.6% | 21.4% | 22.2% |
| SI | Blaze Alexander | 49 | 0.341 | 0.409 | 0.068 | 0.358 | 0.401 | 2.4% | 32.9% | 5.8% |


## Baltimore Orioles Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gunnar Henderson | 380 | 0.230 | 0.434 | 0.204 | 0.338 | 0.310 | 8.7% | 26.9% | 21.5% |
| Taylor Ward | 375 | 0.252 | 0.357 | 0.105 | 0.344 | 0.353 | 5.3% | 24.6% | 16.5% |
| Pete Alonso | 373 | 0.246 | 0.458 | 0.212 | 0.341 | 0.373 | 13.0% | 34.1% | 26.0% |
| Leody Taveras | 261 | 0.254 | 0.382 | 0.127 | 0.321 | 0.294 | 5.3% | 19.9% | 24.9% |
| Samuel Basallo | 260 | 0.260 | 0.468 | 0.209 | 0.347 | 0.330 | 12.4% | 26.9% | 26.5% |
| Adley Rutschman | 243 | 0.260 | 0.456 | 0.195 | 0.349 | 0.354 | 8.7% | 27.6% | 12.7% |
| Coby Mayo | 231 | 0.182 | 0.373 | 0.191 | 0.279 | 0.285 | 10.4% | 30.0% | 29.9% |
| Colton Cowser | 215 | 0.216 | 0.378 | 0.162 | 0.311 | 0.319 | 12.0% | 19.4% | 32.2% |
| Jeremiah Jackson | 210 | 0.271 | 0.443 | 0.172 | 0.330 | 0.291 | 7.9% | 28.2% | 23.9% |
| Blaze Alexander | 202 | 0.304 | 0.429 | 0.125 | 0.354 | 0.350 | 6.5% | 24.6% | 25.2% |
| Tyler O'Neill | 158 | 0.184 | 0.270 | 0.085 | 0.256 | 0.276 | 6.1% | 26.3% | 27.9% |
| Dylan Beavers | 123 | 0.234 | 0.355 | 0.121 | 0.309 | 0.308 | 5.0% | 22.1% | 20.1% |


## Los Angeles Angels Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Zach Neto | 374 | 0.226 | 0.452 | 0.226 | 0.341 | 0.318 | 13.5% | 23.0% | 30.9% |
| Jo Adell | 360 | 0.251 | 0.393 | 0.142 | 0.300 | 0.320 | 8.5% | 26.5% | 25.6% |
| Mike Trout | 353 | 0.240 | 0.473 | 0.233 | 0.390 | 0.412 | 20.2% | 26.5% | 20.4% |
| Nolan Schanuel | 276 | 0.260 | 0.388 | 0.128 | 0.331 | 0.318 | 2.5% | 19.2% | 16.3% |
| Jorge Soler | 270 | 0.223 | 0.429 | 0.206 | 0.324 | 0.308 | 12.4% | 26.9% | 34.3% |
| Oswald Peraza | 259 | 0.259 | 0.407 | 0.148 | 0.328 | 0.303 | 8.1% | 22.1% | 25.5% |
| Logan O'Hoppe | 204 | 0.225 | 0.341 | 0.115 | 0.288 | 0.282 | 10.4% | 26.0% | 26.9% |
| Vaughn Grissom | 174 | 0.230 | 0.375 | 0.145 | 0.312 | 0.336 | 6.7% | 26.3% | 17.5% |
| Josh Lowe | 152 | 0.204 | 0.359 | 0.155 | 0.268 | 0.263 | 8.2% | 16.3% | 25.4% |
| Yoán Moncada | 147 | 0.202 | 0.306 | 0.105 | 0.295 | 0.270 | 8.6% | 22.7% | 29.4% |
| Adam Frazier | 115 | 0.198 | 0.312 | 0.115 | 0.285 | 0.237 | 2.9% | 9.8% | 24.5% |
| Wade Meckler | 100 | 0.270 | 0.404 | 0.135 | 0.345 | 0.318 | 5.9% | 17.1% | 23.8% |


## Bullpen Fatigue Report

### Baltimore Orioles Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Albert Suárez | 2026-06-23 | 3.0 | 30 |
| Andrew Kittredge | 2026-06-20 | 0.1 | 10 |
| Grant Wolfram | 2026-06-20 | 0.1 | 3 |
| Grant Wolfram | 2026-06-21 | 2.0 | 14 |
| Keegan Akin | 2026-06-21 | 2.0 | 37 |
| Rico Garcia | 2026-06-20 | 0.2 | 11 |
| Rico Garcia | 2026-06-22 | 1.0 | 9 |
| Yennier Cano | 2026-06-20 | 0.2 | 15 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Albert Suárez


### Los Angeles Angels Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brent Suter | 2026-06-21 | 1.0 | 20 |
| Brent Suter | 2026-06-22 | 2.0 | 35 |
| Chase Silseth | 2026-06-21 | 1.0 | 24 |
| Chase Silseth | 2026-06-23 | 0.2 | 9 |
| José Fermin | 2026-06-22 | 1.1 | 26 |
| Kirby Yates | 2026-06-20 | 1.0 | 15 |
| Kirby Yates | 2026-06-22 | 1.0 | 13 |
| Ryan Zeferjahn | 2026-06-20 | 1.2 | 24 |
| Ryan Zeferjahn | 2026-06-23 | 1.0 | 16 |
| Sam Bachman | 2026-06-21 | 1.0 | 11 |
| Sam Bachman | 2026-06-23 | 1.0 | 8 |
| Samy Natera Jr. | 2026-06-20 | 1.1 | 28 |
| Samy Natera Jr. | 2026-06-23 | 0.1 | 14 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Chase Silseth, Ryan Zeferjahn, Sam Bachman, Samy Natera Jr.



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Gunnar Henderson | 380 | 0.230 | 0.434 | 0.204 | 0.338 | 8.7% | 26.9% |
| 2 | Taylor Ward | 375 | 0.252 | 0.357 | 0.105 | 0.344 | 5.3% | 24.6% |
| 3 | Pete Alonso | 373 | 0.246 | 0.458 | 0.212 | 0.341 | 13.0% | 34.1% |
| 4 | Leody Taveras | 261 | 0.254 | 0.382 | 0.127 | 0.321 | 5.3% | 19.9% |
| 5 | Samuel Basallo | 260 | 0.260 | 0.468 | 0.209 | 0.347 | 12.4% | 26.9% |
| 6 | Adley Rutschman | 243 | 0.260 | 0.456 | 0.195 | 0.349 | 8.7% | 27.6% |
| 7 | Coby Mayo | 231 | 0.182 | 0.373 | 0.191 | 0.279 | 10.4% | 30.0% |
| 8 | Colton Cowser | 215 | 0.216 | 0.378 | 0.162 | 0.311 | 12.0% | 19.4% |
| 9 | Jeremiah Jackson | 210 | 0.271 | 0.443 | 0.172 | 0.330 | 7.9% | 28.2% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Zach Neto | 374 | 0.226 | 0.452 | 0.226 | 0.341 | 13.5% | 23.0% |
| 2 | Jo Adell | 360 | 0.251 | 0.393 | 0.142 | 0.300 | 8.5% | 26.5% |
| 3 | Mike Trout | 353 | 0.240 | 0.473 | 0.233 | 0.390 | 20.2% | 26.5% |
| 4 | Nolan Schanuel | 276 | 0.260 | 0.388 | 0.128 | 0.331 | 2.5% | 19.2% |
| 5 | Jorge Soler | 270 | 0.223 | 0.429 | 0.206 | 0.324 | 12.4% | 26.9% |
| 6 | Oswald Peraza | 259 | 0.259 | 0.407 | 0.148 | 0.328 | 8.1% | 22.1% |
| 7 | Logan O'Hoppe | 204 | 0.225 | 0.341 | 0.115 | 0.288 | 10.4% | 26.0% |
| 8 | Vaughn Grissom | 174 | 0.230 | 0.375 | 0.145 | 0.312 | 6.7% | 26.3% |
| 9 | Josh Lowe | 152 | 0.204 | 0.359 | 0.155 | 0.268 | 8.2% | 16.3% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6757 |
| Hits Allowed | 1463 |
| Walks/HBP | 684 |
| Strikeouts | 1531 |
| Home Runs Allowed | 203 |
| K Event Rate | 22.7% |
| BB/HBP Event Rate | 10.1% |
| HR Event Rate | 3.0% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7015 |
| Hits Allowed | 1451 |
| Walks/HBP | 823 |
| Strikeouts | 1667 |
| Home Runs Allowed | 209 |
| K Event Rate | 23.8% |
| BB/HBP Event Rate | 11.7% |
| HR Event Rate | 3.0% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: SI, SL, FC, FF, CU
- Home pitcher pitch mix to inspect: SI, KC, FF, FS
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 7. Seattle Mariners @ Pittsburgh Pirates

## Game Context

| Field | Value |
| --- | --- |
| Park | PNC Park |
| Time | 2026-06-24T22:40:00Z |
| Away Team | Seattle Mariners |
| Home Team | Pittsburgh Pirates |
| Away Probable Pitcher | Bryan Woo |
| Home Probable Pitcher | Braxton Ashcraft |


## Away Starting Pitcher: Bryan Woo

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1373 |
| Batted/Result Events | 375 |
| Hits Allowed | 76 |
| Walks | 16 |
| Strikeouts | 92 |
| Home Runs | 9 |
| K Event Rate | 24.5% |
| BB Event Rate | 4.3% |
| HR Event Rate | 2.4% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-18 | SEA | 8.3 | 3 | 0 | 1 | 9 | 0 |
| 2026-06-11 | BAL | 7.7 | 7 | 2 | 2 | 4 | 2 |
| 2026-06-05 | DET | 9.0 | 9 | 1 | 0 | 7 | 1 |
| 2026-05-30 | SEA | 7.7 | 2 | 0 | 0 | 9 | 0 |
| 2026-05-24 | KC | 7.7 | 6 | 0 | 1 | 4 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 6.0% | 82 | 0.091 | 0.136 | 0.045 | 0.124 | 0.177 | 6.7% | 18.2% | 17.8% |
| CH | vs R | 0.2% | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.058 | 0.0% | 50.0% | 0.0% |
| FF | vs L | 32.8% | 450 | 0.241 | 0.389 | 0.148 | 0.297 | 0.331 | 7.1% | 24.3% | 18.5% |
| FF | vs R | 15.7% | 215 | 0.185 | 0.259 | 0.074 | 0.202 | 0.189 | 5.4% | 17.7% | 28.8% |
| SI | vs L | 4.4% | 61 | 0.278 | 0.444 | 0.167 | 0.395 | 0.397 | 18.8% | 36.0% | 7.4% |
| SI | vs R | 12.8% | 176 | 0.269 | 0.404 | 0.135 | 0.315 | 0.329 | 4.5% | 29.4% | 8.7% |
| SL | vs L | 12.2% | 168 | 0.200 | 0.333 | 0.133 | 0.250 | 0.251 | 15.8% | 30.8% | 26.5% |
| SL | vs R | 1.6% | 22 | 0.429 | 0.429 | 0.000 | 0.386 | 0.404 | 0.0% | 30.0% | 23.1% |
| ST | vs L | 4.5% | 62 | 0.158 | 0.368 | 0.211 | 0.266 | 0.276 | 18.2% | 30.0% | 30.6% |
| ST | vs R | 9.5% | 131 | 0.167 | 0.262 | 0.095 | 0.185 | 0.230 | 3.6% | 24.4% | 38.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-18 | 89 | 3 | 1 | 9 | 0 |
| 2026-06-11 | 82 | 7 | 1 | 4 | 2 |
| 2026-06-05 | 90 | 9 | 0 | 7 | 1 |
| 2026-05-30 | 86 | 2 | 0 | 9 | 0 |
| 2026-05-24 | 93 | 6 | 2 | 4 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF | Brandon Lowe | 86 | 0.288 | 0.685 | 0.397 | 0.459 | 0.439 | 31.9% | 26.1% | 30.9% |
| ST | Oneil Cruz | 23 | 0.350 | 0.700 | 0.350 | 0.515 | 0.376 | 18.2% | 33.3% | 32.5% |
| SL | Nick Yorke | 7 | 0.333 | 0.667 | 0.333 | 0.457 | 0.286 | 0.0% | 33.3% | 17.6% |
| FF | Bryan Reynolds | 108 | 0.330 | 0.604 | 0.275 | 0.454 | 0.417 | 13.9% | 31.0% | 17.1% |
| SL | Brandon Lowe | 56 | 0.212 | 0.481 | 0.269 | 0.305 | 0.275 | 11.8% | 31.1% | 35.9% |
| SL | Spencer Horwitz | 35 | 0.290 | 0.548 | 0.258 | 0.394 | 0.285 | 4.3% | 19.6% | 15.8% |
| FF | Konnor Griffin | 47 | 0.205 | 0.462 | 0.256 | 0.349 | 0.306 | 11.8% | 14.0% | 25.5% |
| FF | Ryan O'Hearn | 95 | 0.302 | 0.558 | 0.256 | 0.407 | 0.341 | 9.7% | 27.7% | 11.9% |
| ST | Bryan Reynolds | 31 | 0.375 | 0.625 | 0.250 | 0.489 | 0.391 | 21.4% | 45.5% | 40.0% |
| FF | Spencer Horwitz | 114 | 0.269 | 0.495 | 0.226 | 0.389 | 0.375 | 12.3% | 18.6% | 12.9% |
| ST | Henry Davis | 15 | 0.133 | 0.333 | 0.200 | 0.193 | 0.237 | 9.1% | 36.4% | 16.7% |
| SL | Nick Gonzales | 38 | 0.229 | 0.429 | 0.200 | 0.336 | 0.408 | 6.2% | 25.0% | 22.6% |
| SI | Henry Davis | 40 | 0.226 | 0.419 | 0.194 | 0.357 | 0.431 | 10.3% | 38.5% | 9.0% |
| FF | Oneil Cruz | 91 | 0.291 | 0.481 | 0.190 | 0.392 | 0.388 | 15.1% | 37.1% | 27.0% |
| SL | Ryan O'Hearn | 40 | 0.211 | 0.395 | 0.184 | 0.279 | 0.238 | 4.5% | 23.4% | 27.6% |
| ST | Jake Mangum | 19 | 0.471 | 0.647 | 0.176 | 0.471 | 0.320 | 0.0% | 16.0% | 13.3% |
| SL | Oneil Cruz | 38 | 0.235 | 0.412 | 0.176 | 0.345 | 0.351 | 15.0% | 36.8% | 44.0% |
| ST | Brandon Lowe | 28 | 0.080 | 0.240 | 0.160 | 0.223 | 0.238 | 0.0% | 26.7% | 35.7% |
| ST | Konnor Griffin | 20 | 0.211 | 0.368 | 0.158 | 0.270 | 0.241 | 6.2% | 41.7% | 25.0% |
| SI | Nick Yorke | 29 | 0.269 | 0.423 | 0.154 | 0.371 | 0.343 | 4.2% | 36.1% | 6.8% |
| FF | Marcell Ozuna | 83 | 0.243 | 0.392 | 0.149 | 0.319 | 0.430 | 11.9% | 29.2% | 17.2% |
| SI | Ryan O'Hearn | 52 | 0.362 | 0.511 | 0.149 | 0.427 | 0.438 | 9.8% | 40.7% | 8.8% |
| SI | Bryan Reynolds | 42 | 0.429 | 0.571 | 0.143 | 0.525 | 0.480 | 8.0% | 41.3% | 9.1% |
| SL | Konnor Griffin | 37 | 0.194 | 0.333 | 0.139 | 0.219 | 0.273 | 7.7% | 20.8% | 38.0% |
| FF | Jake Mangum | 50 | 0.333 | 0.462 | 0.128 | 0.426 | 0.347 | 3.7% | 13.9% | 18.6% |
| SI | Marcell Ozuna | 57 | 0.235 | 0.353 | 0.118 | 0.301 | 0.319 | 2.6% | 33.9% | 11.5% |
| FF | Henry Davis | 51 | 0.140 | 0.256 | 0.116 | 0.286 | 0.263 | 11.1% | 23.7% | 26.9% |
| SL | Marcell Ozuna | 28 | 0.185 | 0.296 | 0.111 | 0.289 | 0.214 | 9.1% | 21.4% | 47.7% |
| SI | Jared Triolo | 34 | 0.250 | 0.357 | 0.107 | 0.366 | 0.347 | 0.0% | 27.3% | 11.6% |
| SL | Bryan Reynolds | 43 | 0.171 | 0.257 | 0.086 | 0.280 | 0.267 | 5.3% | 28.9% | 32.9% |


## Home Starting Pitcher: Braxton Ashcraft

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1407 |
| Batted/Result Events | 392 |
| Hits Allowed | 83 |
| Walks | 22 |
| Strikeouts | 105 |
| Home Runs | 8 |
| K Event Rate | 26.8% |
| BB Event Rate | 5.6% |
| HR Event Rate | 2.0% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-17 | ATH | 8.3 | 4 | 0 | 3 | 7 | 0 |
| 2026-06-12 | PIT | 7.3 | 5 | 0 | 2 | 4 | 0 |
| 2026-06-06 | ATL | 8.3 | 9 | 1 | 1 | 5 | 1 |
| 2026-05-31 | PIT | 7.3 | 5 | 1 | 0 | 11 | 1 |
| 2026-05-26 | PIT | 9.7 | 7 | 0 | 3 | 5 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 15.8% | 222 | 0.086 | 0.155 | 0.069 | 0.144 | 0.197 | 11.1% | 36.7% | 42.1% |
| CU | vs R | 9.1% | 128 | 0.182 | 0.273 | 0.091 | 0.226 | 0.227 | 0.0% | 19.4% | 35.8% |
| FF | vs L | 19.5% | 275 | 0.344 | 0.672 | 0.328 | 0.458 | 0.353 | 11.5% | 24.8% | 19.3% |
| FF | vs R | 11.2% | 157 | 0.194 | 0.250 | 0.056 | 0.215 | 0.219 | 12.5% | 16.9% | 8.0% |
| FS | vs L | 4.7% | 66 | 0.357 | 0.357 | 0.000 | 0.321 | 0.266 | 0.0% | 20.0% | 6.9% |
| SI | vs L | 5.2% | 73 | 0.368 | 0.421 | 0.053 | 0.383 | 0.352 | 0.0% | 21.7% | 9.7% |
| SI | vs R | 10.8% | 152 | 0.175 | 0.200 | 0.025 | 0.199 | 0.309 | 0.0% | 35.8% | 19.8% |
| SL | vs L | 10.5% | 148 | 0.235 | 0.265 | 0.029 | 0.339 | 0.301 | 0.0% | 42.2% | 32.9% |
| SL | vs R | 13.2% | 186 | 0.271 | 0.373 | 0.102 | 0.324 | 0.232 | 4.8% | 17.4% | 30.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-17 | 93 | 4 | 3 | 7 | 0 |
| 2026-06-12 | 90 | 5 | 2 | 4 | 0 |
| 2026-06-06 | 86 | 9 | 0 | 5 | 1 |
| 2026-05-31 | 80 | 5 | 0 | 11 | 1 |
| 2026-05-26 | 95 | 7 | 1 | 5 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | J. P. Crawford | 10 | 0.333 | 1.000 | 0.667 | 0.560 | 0.387 | 40.0% | 41.7% | 27.8% |
| SI | Cal Raleigh | 13 | 0.500 | 1.000 | 0.500 | 0.592 | 0.617 | 44.4% | 31.6% | 14.8% |
| FF | Brendan Donovan | 41 | 0.323 | 0.774 | 0.452 | 0.498 | 0.326 | 8.0% | 31.1% | 15.0% |
| CU | Dominic Canzone | 18 | 0.312 | 0.750 | 0.438 | 0.469 | 0.401 | 27.3% | 50.0% | 28.0% |
| FF | Luke Raley | 75 | 0.281 | 0.688 | 0.406 | 0.450 | 0.444 | 24.4% | 35.0% | 34.1% |
| FF | Dominic Canzone | 61 | 0.304 | 0.696 | 0.393 | 0.439 | 0.458 | 21.7% | 40.7% | 15.7% |
| SL | Dominic Canzone | 21 | 0.389 | 0.778 | 0.389 | 0.521 | 0.390 | 20.0% | 22.7% | 44.2% |
| CU | Randy Arozarena | 13 | 0.250 | 0.583 | 0.333 | 0.373 | 0.296 | 16.7% | 22.2% | 26.9% |
| CU | Cole Young | 12 | 0.556 | 0.889 | 0.333 | 0.583 | 0.395 | 14.3% | 50.0% | 10.5% |
| CU | Luke Raley | 13 | 0.250 | 0.583 | 0.333 | 0.373 | 0.417 | 42.9% | 33.3% | 34.5% |
| CU | Brendan Donovan | 10 | 0.429 | 0.714 | 0.286 | 0.550 | 0.494 | 20.0% | 33.3% | 25.0% |
| SL | Randy Arozarena | 44 | 0.317 | 0.585 | 0.268 | 0.424 | 0.314 | 6.5% | 24.6% | 29.8% |
| SL | Cole Young | 38 | 0.265 | 0.529 | 0.265 | 0.354 | 0.381 | 12.0% | 28.2% | 24.1% |
| SL | Julio Rodríguez | 51 | 0.271 | 0.521 | 0.250 | 0.357 | 0.377 | 10.0% | 26.7% | 29.8% |
| SL | Cal Raleigh | 27 | 0.125 | 0.375 | 0.250 | 0.233 | 0.289 | 14.3% | 30.3% | 31.5% |
| SI | Luke Raley | 26 | 0.250 | 0.500 | 0.250 | 0.325 | 0.384 | 21.1% | 27.0% | 24.0% |
| FF | Julio Rodríguez | 89 | 0.221 | 0.429 | 0.208 | 0.331 | 0.338 | 13.2% | 25.4% | 26.9% |
| CU | Julio Rodríguez | 17 | 0.200 | 0.400 | 0.200 | 0.306 | 0.325 | 11.1% | 25.0% | 45.5% |
| SL | Mitch Garver | 17 | 0.133 | 0.333 | 0.200 | 0.306 | 0.240 | 0.0% | 16.7% | 72.1% |
| FF | J. P. Crawford | 92 | 0.239 | 0.433 | 0.194 | 0.398 | 0.427 | 9.3% | 16.4% | 13.7% |
| FF | Josh Naylor | 100 | 0.311 | 0.500 | 0.189 | 0.386 | 0.361 | 6.0% | 22.5% | 7.4% |
| SI | Mitch Garver | 28 | 0.227 | 0.409 | 0.182 | 0.395 | 0.384 | 5.9% | 40.0% | 11.1% |
| FF | Cole Young | 121 | 0.234 | 0.393 | 0.159 | 0.314 | 0.320 | 7.7% | 24.3% | 15.4% |
| SI | Julio Rodríguez | 93 | 0.284 | 0.443 | 0.159 | 0.363 | 0.364 | 8.9% | 33.3% | 7.1% |
| FF | Randy Arozarena | 100 | 0.235 | 0.383 | 0.148 | 0.343 | 0.384 | 16.7% | 27.0% | 30.5% |
| FF | Mitch Garver | 50 | 0.238 | 0.381 | 0.143 | 0.322 | 0.323 | 13.8% | 30.6% | 21.3% |
| SL | Luke Raley | 24 | 0.273 | 0.409 | 0.136 | 0.329 | 0.317 | 6.2% | 37.5% | 45.1% |
| FF | Cal Raleigh | 83 | 0.135 | 0.257 | 0.122 | 0.223 | 0.238 | 11.1% | 23.8% | 29.9% |
| SL | J. P. Crawford | 30 | 0.107 | 0.214 | 0.107 | 0.150 | 0.192 | 5.6% | 11.4% | 26.4% |
| SI | Dominic Canzone | 33 | 0.214 | 0.321 | 0.107 | 0.303 | 0.404 | 8.0% | 34.3% | 13.6% |


## Seattle Mariners Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Julio Rodríguez | 359 | 0.247 | 0.430 | 0.183 | 0.329 | 0.345 | 9.5% | 28.8% | 25.2% |
| Cole Young | 345 | 0.251 | 0.383 | 0.132 | 0.310 | 0.329 | 6.0% | 24.9% | 17.9% |
| Josh Naylor | 331 | 0.253 | 0.365 | 0.112 | 0.307 | 0.323 | 5.0% | 26.7% | 16.6% |
| Randy Arozarena | 330 | 0.284 | 0.449 | 0.165 | 0.372 | 0.349 | 8.1% | 24.4% | 24.6% |
| J. P. Crawford | 259 | 0.223 | 0.386 | 0.163 | 0.332 | 0.352 | 8.4% | 21.9% | 15.7% |
| Luke Raley | 237 | 0.252 | 0.528 | 0.276 | 0.369 | 0.358 | 17.6% | 29.8% | 39.0% |
| Cal Raleigh | 225 | 0.172 | 0.328 | 0.157 | 0.264 | 0.292 | 12.4% | 22.6% | 30.2% |
| Dominic Canzone | 214 | 0.288 | 0.576 | 0.288 | 0.393 | 0.384 | 15.7% | 31.1% | 25.2% |
| Leo Rivas | 140 | 0.132 | 0.167 | 0.035 | 0.231 | 0.238 | 2.6% | 9.7% | 23.9% |
| Rob Refsnyder | 132 | 0.132 | 0.219 | 0.088 | 0.206 | 0.257 | 7.5% | 23.4% | 24.3% |
| Brendan Donovan | 127 | 0.311 | 0.505 | 0.194 | 0.399 | 0.345 | 5.8% | 27.8% | 17.9% |
| Mitch Garver | 127 | 0.193 | 0.330 | 0.138 | 0.307 | 0.295 | 7.6% | 29.2% | 35.3% |


## Pittsburgh Pirates Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bryan Reynolds | 357 | 0.287 | 0.473 | 0.186 | 0.389 | 0.374 | 10.3% | 30.3% | 25.4% |
| Brandon Lowe | 337 | 0.246 | 0.498 | 0.253 | 0.360 | 0.349 | 12.7% | 29.4% | 31.8% |
| Nick Gonzales | 313 | 0.292 | 0.371 | 0.079 | 0.323 | 0.327 | 3.0% | 22.2% | 20.7% |
| Spencer Horwitz | 311 | 0.272 | 0.448 | 0.176 | 0.368 | 0.339 | 8.5% | 20.8% | 14.0% |
| Oneil Cruz | 300 | 0.261 | 0.470 | 0.208 | 0.368 | 0.358 | 16.9% | 36.9% | 35.3% |
| Ryan O'Hearn | 280 | 0.260 | 0.421 | 0.161 | 0.331 | 0.319 | 7.2% | 26.3% | 20.6% |
| Marcell Ozuna | 240 | 0.202 | 0.307 | 0.106 | 0.270 | 0.311 | 7.6% | 26.6% | 28.5% |
| Konnor Griffin | 222 | 0.259 | 0.398 | 0.139 | 0.332 | 0.303 | 8.6% | 24.2% | 30.8% |
| Jake Mangum | 196 | 0.289 | 0.344 | 0.056 | 0.328 | 0.286 | 0.7% | 13.6% | 16.2% |
| Jared Triolo | 169 | 0.222 | 0.275 | 0.052 | 0.292 | 0.273 | 0.9% | 24.6% | 22.6% |
| Henry Davis | 166 | 0.152 | 0.303 | 0.152 | 0.269 | 0.296 | 11.8% | 30.7% | 22.1% |
| Nick Yorke | 107 | 0.202 | 0.277 | 0.074 | 0.264 | 0.306 | 5.1% | 28.3% | 14.7% |


## Bullpen Fatigue Report

### Seattle Mariners Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alex Hoppe | 2026-06-20 | 1.0 | 14 |
| Andrés Muñoz | 2026-06-21 | 1.0 | 15 |
| Andrés Muñoz | 2026-06-23 | 1.0 | 16 |
| Eduard Bazardo | 2026-06-21 | 1.0 | 11 |
| Eduard Bazardo | 2026-06-23 | 1.0 | 21 |
| Gabe Speier | 2026-06-21 | 0.2 | 9 |
| José A. Ferrer | 2026-06-20 | 0.2 | 18 |
| José A. Ferrer | 2026-06-23 | 1.0 | 10 |
| Michael Rucker | 2026-06-20 | 1.0 | 15 |
| Nick Davila | 2026-06-20 | 1.0 | 24 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Andrés Muñoz, Eduard Bazardo, José A. Ferrer


### Pittsburgh Pirates Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Carmen Mlodzinski | 2026-06-20 | 2.0 | 32 |
| Dennis Santana | 2026-06-21 | 1.0 | 18 |
| Dennis Santana | 2026-06-23 | 1.0 | 18 |
| Evan Sisk | 2026-06-21 | 2.0 | 35 |
| Gregory Soto | 2026-06-21 | 1.0 | 19 |
| Isaac Mattson | 2026-06-23 | 1.0 | 13 |
| Mason Montgomery | 2026-06-23 | 1.0 | 19 |
| Yohan Ramírez | 2026-06-21 | 2.0 | 28 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Dennis Santana, Isaac Mattson, Mason Montgomery



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Julio Rodríguez | 359 | 0.247 | 0.430 | 0.183 | 0.329 | 9.5% | 28.8% |
| 2 | Cole Young | 345 | 0.251 | 0.383 | 0.132 | 0.310 | 6.0% | 24.9% |
| 3 | Josh Naylor | 331 | 0.253 | 0.365 | 0.112 | 0.307 | 5.0% | 26.7% |
| 4 | Randy Arozarena | 330 | 0.284 | 0.449 | 0.165 | 0.372 | 8.1% | 24.4% |
| 5 | J. P. Crawford | 259 | 0.223 | 0.386 | 0.163 | 0.332 | 8.4% | 21.9% |
| 6 | Luke Raley | 237 | 0.252 | 0.528 | 0.276 | 0.369 | 17.6% | 29.8% |
| 7 | Cal Raleigh | 225 | 0.172 | 0.328 | 0.157 | 0.264 | 12.4% | 22.6% |
| 8 | Dominic Canzone | 214 | 0.288 | 0.576 | 0.288 | 0.393 | 15.7% | 31.1% |
| 9 | Leo Rivas | 140 | 0.132 | 0.167 | 0.035 | 0.231 | 2.6% | 9.7% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bryan Reynolds | 357 | 0.287 | 0.473 | 0.186 | 0.389 | 10.3% | 30.3% |
| 2 | Brandon Lowe | 337 | 0.246 | 0.498 | 0.253 | 0.360 | 12.7% | 29.4% |
| 3 | Nick Gonzales | 313 | 0.292 | 0.371 | 0.079 | 0.323 | 3.0% | 22.2% |
| 4 | Spencer Horwitz | 311 | 0.272 | 0.448 | 0.176 | 0.368 | 8.5% | 20.8% |
| 5 | Oneil Cruz | 300 | 0.261 | 0.470 | 0.208 | 0.368 | 16.9% | 36.9% |
| 6 | Ryan O'Hearn | 280 | 0.260 | 0.421 | 0.161 | 0.331 | 7.2% | 26.3% |
| 7 | Marcell Ozuna | 240 | 0.202 | 0.307 | 0.106 | 0.270 | 7.6% | 26.6% |
| 8 | Konnor Griffin | 222 | 0.259 | 0.398 | 0.139 | 0.332 | 8.6% | 24.2% |
| 9 | Jake Mangum | 196 | 0.289 | 0.344 | 0.056 | 0.328 | 0.7% | 13.6% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6668 |
| Hits Allowed | 1426 |
| Walks/HBP | 628 |
| Strikeouts | 1545 |
| Home Runs Allowed | 205 |
| K Event Rate | 23.2% |
| BB/HBP Event Rate | 9.4% |
| HR Event Rate | 3.1% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6812 |
| Hits Allowed | 1463 |
| Walks/HBP | 728 |
| Strikeouts | 1623 |
| Home Runs Allowed | 190 |
| K Event Rate | 23.8% |
| BB/HBP Event Rate | 10.7% |
| HR Event Rate | 2.8% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SI, ST, SL
- Home pitcher pitch mix to inspect: FF, CU, SL, SI
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 8. Kansas City Royals @ Tampa Bay Rays

## Game Context

| Field | Value |
| --- | --- |
| Park | Tropicana Field |
| Time | 2026-06-24T22:40:00Z |
| Away Team | Kansas City Royals |
| Home Team | Tampa Bay Rays |
| Away Probable Pitcher | Noah Cameron |
| Home Probable Pitcher | Griffin Jax |


## Away Starting Pitcher: Noah Cameron

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1337 |
| Batted/Result Events | 343 |
| Hits Allowed | 81 |
| Walks | 21 |
| Strikeouts | 74 |
| Home Runs | 10 |
| K Event Rate | 21.6% |
| BB Event Rate | 6.1% |
| HR Event Rate | 2.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-18 | KC | 9.0 | 8 | 0 | 3 | 6 | 0 |
| 2026-06-13 | KC | 6.7 | 7 | 2 | 0 | 1 | 2 |
| 2026-06-07 | MIN | 7.7 | 3 | 0 | 0 | 7 | 0 |
| 2026-06-02 | CIN | 7.3 | 1 | 1 | 0 | 8 | 1 |
| 2026-05-27 | KC | 6.7 | 4 | 0 | 1 | 4 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 1.9% | 25 | 0.111 | 0.222 | 0.111 | 0.195 | 0.191 | 0.0% | 12.5% | 33.3% |
| CH | vs R | 20.0% | 267 | 0.200 | 0.333 | 0.133 | 0.292 | 0.281 | 4.4% | 16.7% | 31.5% |
| CU | vs L | 3.1% | 41 | 0.125 | 0.250 | 0.125 | 0.156 | 0.153 | 0.0% | 9.1% | 22.2% |
| CU | vs R | 14.1% | 189 | 0.130 | 0.239 | 0.109 | 0.218 | 0.219 | 14.3% | 21.1% | 31.2% |
| EP | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| FC | vs L | 4.9% | 65 | 0.250 | 0.350 | 0.100 | 0.287 | 0.301 | 5.6% | 25.9% | 24.3% |
| FC | vs R | 14.4% | 193 | 0.375 | 0.542 | 0.167 | 0.432 | 0.375 | 4.7% | 26.7% | 21.7% |
| FF | vs L | 7.8% | 104 | 0.375 | 0.688 | 0.312 | 0.506 | 0.480 | 21.4% | 31.6% | 8.3% |
| FF | vs R | 21.1% | 282 | 0.262 | 0.410 | 0.148 | 0.347 | 0.349 | 7.3% | 32.7% | 14.2% |
| SI | vs L | 1.9% | 26 | 0.400 | 0.400 | 0.000 | 0.417 | 0.331 | 0.0% | 42.9% | 11.1% |
| SI | vs R | 0.8% | 11 | 0.667 | 1.667 | 1.000 | 0.967 | 0.795 | 33.3% | 25.0% | 0.0% |
| SL | vs L | 5.5% | 73 | 0.304 | 0.783 | 0.478 | 0.467 | 0.449 | 31.6% | 38.5% | 22.2% |
| SL | vs R | 4.5% | 60 | 0.294 | 0.412 | 0.118 | 0.311 | 0.345 | 7.7% | 36.0% | 22.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-18 | 108 | 8 | 2 | 6 | 0 |
| 2026-06-13 | 86 | 7 | 0 | 1 | 2 |
| 2026-06-07 | 104 | 3 | 0 | 7 | 0 |
| 2026-06-02 | 87 | 1 | 0 | 8 | 1 |
| 2026-05-27 | 94 | 4 | 1 | 4 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Ryan Vilade | 11 | 0.200 | 0.800 | 0.600 | 0.609 | 0.866 | 20.0% | 41.2% | 35.7% |
| CU | Jonathan Aranda | 16 | 0.357 | 0.786 | 0.429 | 0.463 | 0.485 | 33.3% | 40.9% | 24.2% |
| FC | Ryan Vilade | 14 | 0.417 | 0.750 | 0.333 | 0.525 | 0.459 | 10.0% | 35.0% | 12.5% |
| FC | Ben Williamson | 17 | 0.333 | 0.667 | 0.333 | 0.515 | 0.412 | 8.3% | 25.0% | 14.7% |
| FF | Junior Caminero | 75 | 0.349 | 0.651 | 0.302 | 0.468 | 0.454 | 16.7% | 42.9% | 20.0% |
| CU | Ryan Vilade | 10 | 0.400 | 0.700 | 0.300 | 0.470 | 0.414 | 12.5% | 38.5% | 13.3% |
| CH | Yandy Díaz | 34 | 0.258 | 0.548 | 0.290 | 0.349 | 0.329 | 3.8% | 34.9% | 14.8% |
| SL | Yandy Díaz | 55 | 0.413 | 0.696 | 0.283 | 0.498 | 0.505 | 17.8% | 33.8% | 12.0% |
| SL | Jonny Deluca | 18 | 0.278 | 0.556 | 0.278 | 0.350 | 0.287 | 6.7% | 20.0% | 35.3% |
| CH | Cedric Mullins | 23 | 0.227 | 0.500 | 0.273 | 0.322 | 0.346 | 15.0% | 20.0% | 9.8% |
| SL | Richie Palacios | 23 | 0.273 | 0.545 | 0.273 | 0.357 | 0.368 | 6.2% | 17.9% | 21.1% |
| SL | Jonathan Aranda | 42 | 0.243 | 0.514 | 0.270 | 0.363 | 0.303 | 11.5% | 30.2% | 18.5% |
| FC | Chandler Simpson | 19 | 0.333 | 0.600 | 0.267 | 0.421 | 0.305 | 0.0% | 8.0% | 6.9% |
| FC | Jonny Deluca | 12 | 0.417 | 0.667 | 0.250 | 0.467 | 0.369 | 8.3% | 12.0% | 9.7% |
| FC | Junior Caminero | 24 | 0.389 | 0.611 | 0.222 | 0.469 | 0.429 | 23.5% | 25.0% | 4.5% |
| FC | Richie Palacios | 15 | 0.333 | 0.533 | 0.200 | 0.373 | 0.334 | 8.3% | 23.8% | 12.0% |
| CH | Jonathan Aranda | 33 | 0.258 | 0.452 | 0.194 | 0.326 | 0.298 | 4.3% | 15.0% | 18.0% |
| SL | Chandler Simpson | 29 | 0.333 | 0.519 | 0.185 | 0.390 | 0.245 | 0.0% | 24.1% | 19.5% |
| FF | Yandy Díaz | 87 | 0.225 | 0.388 | 0.163 | 0.297 | 0.290 | 6.8% | 23.4% | 15.8% |
| FF | Jonathan Aranda | 131 | 0.245 | 0.406 | 0.160 | 0.344 | 0.372 | 11.5% | 22.2% | 20.0% |
| CU | Junior Caminero | 21 | 0.105 | 0.263 | 0.158 | 0.205 | 0.254 | 11.1% | 29.4% | 35.5% |
| FF | Hunter Feduccia | 41 | 0.147 | 0.294 | 0.147 | 0.273 | 0.312 | 19.0% | 18.6% | 16.9% |
| FF | Nick Fortes | 61 | 0.268 | 0.411 | 0.143 | 0.325 | 0.267 | 4.3% | 31.9% | 8.9% |
| SL | Cedric Mullins | 28 | 0.143 | 0.286 | 0.143 | 0.286 | 0.260 | 0.0% | 11.9% | 22.8% |
| FF | Taylor Walls | 86 | 0.232 | 0.362 | 0.130 | 0.323 | 0.277 | 5.4% | 17.0% | 17.1% |
| CH | Ryan Vilade | 17 | 0.438 | 0.562 | 0.125 | 0.453 | 0.363 | 0.0% | 15.4% | 12.9% |
| FF | Ryan Vilade | 47 | 0.244 | 0.366 | 0.122 | 0.309 | 0.232 | 3.6% | 9.1% | 20.9% |
| FF | Cedric Mullins | 102 | 0.182 | 0.295 | 0.114 | 0.270 | 0.267 | 4.5% | 21.4% | 22.0% |
| SL | Junior Caminero | 57 | 0.182 | 0.291 | 0.109 | 0.220 | 0.283 | 11.1% | 38.2% | 21.1% |
| FF | Ben Williamson | 72 | 0.258 | 0.355 | 0.097 | 0.327 | 0.321 | 2.0% | 23.1% | 6.9% |


## Home Starting Pitcher: Griffin Jax

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 760 |
| Batted/Result Events | 204 |
| Hits Allowed | 46 |
| Walks | 18 |
| Strikeouts | 46 |
| Home Runs | 9 |
| K Event Rate | 22.5% |
| BB Event Rate | 8.8% |
| HR Event Rate | 4.4% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | TB | 6.0 | 4 | 2 | 0 | 5 | 2 |
| 2026-06-13 | LAA | 6.7 | 5 | 0 | 0 | 5 | 0 |
| 2026-06-07 | MIA | 5.7 | 3 | 0 | 2 | 4 | 0 |
| 2026-06-01 | TB | 6.7 | 7 | 3 | 1 | 5 | 3 |
| 2026-05-26 | BAL | 3.7 | 4 | 0 | 0 | 3 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 17.6% | 134 | 0.238 | 0.262 | 0.024 | 0.297 | 0.266 | 0.0% | 19.6% | 36.6% |
| CH | vs R | 3.6% | 27 | 0.250 | 0.250 | 0.000 | 0.225 | 0.320 | 20.0% | 40.0% | 37.5% |
| CU | vs L | 7.5% | 57 | 0.167 | 0.167 | 0.000 | 0.150 | 0.383 | 16.7% | 27.3% | 45.5% |
| CU | vs R | 0.9% | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 100.0% |
| FC | vs L | 6.2% | 47 | 0.333 | 0.833 | 0.500 | 0.500 | 0.702 | 25.0% | 31.6% | 13.0% |
| FC | vs R | 0.4% | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.118 | 0.0% | 0.0% | 0.0% |
| FF | vs L | 12.0% | 91 | 0.412 | 0.824 | 0.412 | 0.539 | 0.428 | 14.3% | 17.2% | 25.6% |
| FF | vs R | 5.7% | 43 | 0.300 | 0.900 | 0.600 | 0.525 | 0.531 | 37.5% | 31.2% | 15.8% |
| SI | vs L | 7.0% | 53 | 0.267 | 0.467 | 0.200 | 0.359 | 0.366 | 16.7% | 21.1% | 8.3% |
| SI | vs R | 13.4% | 102 | 0.308 | 0.308 | 0.000 | 0.363 | 0.348 | 0.0% | 34.1% | 14.8% |
| ST | vs L | 8.6% | 65 | 0.273 | 0.545 | 0.273 | 0.386 | 0.432 | 11.1% | 23.8% | 20.0% |
| ST | vs R | 16.2% | 123 | 0.120 | 0.280 | 0.160 | 0.191 | 0.215 | 13.3% | 22.7% | 44.7% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 69 | 4 | 0 | 5 | 2 |
| 2026-06-13 | 63 | 5 | 0 | 5 | 0 |
| 2026-06-07 | 62 | 3 | 2 | 4 | 0 |
| 2026-06-01 | 72 | 7 | 1 | 5 | 3 |
| 2026-05-26 | 38 | 4 | 0 | 3 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Michael Massey | 6 | 0.167 | 0.667 | 0.500 | 0.333 | 0.227 | 25.0% | 16.7% | 20.0% |
| SI | Starling Marte | 11 | 0.500 | 0.900 | 0.400 | 0.605 | 0.614 | 22.2% | 33.3% | 9.5% |
| FF | Jac Caglianone | 72 | 0.328 | 0.703 | 0.375 | 0.462 | 0.461 | 28.2% | 30.7% | 23.9% |
| CU | Nick Loftin | 9 | 0.250 | 0.625 | 0.375 | 0.400 | 0.373 | 25.0% | 30.0% | 37.5% |
| SI | Salvador Pérez | 43 | 0.378 | 0.730 | 0.351 | 0.469 | 0.450 | 15.8% | 28.9% | 10.9% |
| CH | Bobby Witt | 30 | 0.321 | 0.607 | 0.286 | 0.413 | 0.446 | 16.7% | 28.6% | 16.7% |
| CU | Maikel García | 15 | 0.429 | 0.714 | 0.286 | 0.560 | 0.417 | 8.3% | 47.1% | 10.0% |
| ST | Isaac Collins | 12 | 0.273 | 0.545 | 0.273 | 0.375 | 0.324 | 14.3% | 28.6% | 23.8% |
| CH | Jac Caglianone | 34 | 0.367 | 0.633 | 0.267 | 0.459 | 0.393 | 13.6% | 35.1% | 27.8% |
| CH | Salvador Pérez | 32 | 0.226 | 0.484 | 0.258 | 0.309 | 0.204 | 12.0% | 26.5% | 20.3% |
| CU | Bobby Witt | 24 | 0.375 | 0.625 | 0.250 | 0.467 | 0.426 | 9.1% | 40.7% | 9.7% |
| SI | Carter Jensen | 37 | 0.412 | 0.647 | 0.235 | 0.474 | 0.341 | 3.6% | 34.9% | 13.0% |
| CH | Vinnie Pasquantino | 28 | 0.308 | 0.538 | 0.231 | 0.416 | 0.327 | 5.9% | 28.9% | 28.8% |
| CU | Salvador Pérez | 27 | 0.192 | 0.423 | 0.231 | 0.272 | 0.244 | 9.5% | 22.2% | 21.3% |
| FF | Kyle Isbel | 62 | 0.358 | 0.566 | 0.208 | 0.417 | 0.274 | 4.7% | 15.3% | 7.8% |
| SI | Lane Thomas | 48 | 0.205 | 0.410 | 0.205 | 0.346 | 0.363 | 8.6% | 28.6% | 4.7% |
| FF | Nick Loftin | 61 | 0.265 | 0.469 | 0.204 | 0.357 | 0.326 | 9.1% | 18.7% | 6.0% |
| FF | Michael Massey | 85 | 0.241 | 0.443 | 0.203 | 0.315 | 0.270 | 8.8% | 21.4% | 15.2% |
| CH | Maikel García | 17 | 0.312 | 0.500 | 0.188 | 0.368 | 0.182 | 0.0% | 9.1% | 7.7% |
| FF | Lane Thomas | 79 | 0.197 | 0.377 | 0.180 | 0.347 | 0.335 | 8.9% | 23.0% | 12.4% |
| FF | Carter Jensen | 82 | 0.179 | 0.358 | 0.179 | 0.296 | 0.287 | 6.8% | 17.4% | 26.7% |
| CU | Carter Jensen | 19 | 0.294 | 0.471 | 0.176 | 0.366 | 0.314 | 9.1% | 22.7% | 25.8% |
| ST | Jac Caglianone | 34 | 0.129 | 0.290 | 0.161 | 0.247 | 0.291 | 15.8% | 30.6% | 30.2% |
| SI | Isaac Collins | 36 | 0.290 | 0.452 | 0.161 | 0.358 | 0.301 | 3.7% | 28.6% | 4.0% |
| FF | Bobby Witt | 89 | 0.243 | 0.400 | 0.157 | 0.367 | 0.402 | 12.2% | 26.7% | 16.6% |
| ST | Maikel García | 29 | 0.154 | 0.308 | 0.154 | 0.222 | 0.256 | 5.9% | 12.0% | 30.8% |
| FF | Salvador Pérez | 79 | 0.233 | 0.370 | 0.137 | 0.275 | 0.353 | 18.5% | 27.7% | 21.8% |
| CH | Michael Massey | 22 | 0.409 | 0.545 | 0.136 | 0.418 | 0.325 | 5.3% | 22.2% | 20.8% |
| FF | Vinnie Pasquantino | 120 | 0.260 | 0.394 | 0.135 | 0.327 | 0.325 | 10.8% | 26.1% | 7.4% |
| CU | Jac Caglianone | 23 | 0.217 | 0.348 | 0.130 | 0.243 | 0.303 | 13.3% | 32.1% | 32.7% |


## Kansas City Royals Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bobby Witt | 347 | 0.288 | 0.456 | 0.168 | 0.367 | 0.392 | 12.2% | 32.7% | 20.9% |
| Salvador Pérez | 322 | 0.213 | 0.367 | 0.153 | 0.275 | 0.290 | 10.8% | 25.4% | 23.4% |
| Maikel García | 304 | 0.257 | 0.370 | 0.112 | 0.309 | 0.316 | 4.8% | 28.3% | 13.6% |
| Vinnie Pasquantino | 302 | 0.219 | 0.340 | 0.121 | 0.300 | 0.316 | 7.4% | 27.5% | 14.0% |
| Carter Jensen | 296 | 0.234 | 0.410 | 0.176 | 0.317 | 0.289 | 8.0% | 25.4% | 27.1% |
| Jac Caglianone | 290 | 0.272 | 0.487 | 0.215 | 0.363 | 0.387 | 16.6% | 33.6% | 28.4% |
| Isaac Collins | 273 | 0.218 | 0.306 | 0.087 | 0.299 | 0.310 | 5.9% | 26.4% | 21.4% |
| Lane Thomas | 221 | 0.219 | 0.355 | 0.137 | 0.326 | 0.323 | 5.7% | 21.0% | 16.7% |
| Kyle Isbel | 196 | 0.263 | 0.383 | 0.120 | 0.317 | 0.275 | 2.9% | 24.5% | 14.6% |
| Michael Massey | 192 | 0.261 | 0.450 | 0.189 | 0.316 | 0.291 | 7.8% | 25.9% | 19.5% |
| Nick Loftin | 167 | 0.268 | 0.437 | 0.169 | 0.356 | 0.335 | 6.6% | 23.1% | 15.7% |
| Starling Marte | 113 | 0.265 | 0.343 | 0.078 | 0.304 | 0.308 | 12.2% | 22.4% | 26.3% |


## Tampa Bay Rays Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Junior Caminero | 351 | 0.275 | 0.475 | 0.200 | 0.365 | 0.362 | 12.4% | 36.3% | 21.1% |
| Jonathan Aranda | 347 | 0.274 | 0.445 | 0.171 | 0.359 | 0.368 | 10.8% | 24.7% | 19.5% |
| Yandy Díaz | 345 | 0.330 | 0.507 | 0.177 | 0.403 | 0.367 | 8.3% | 30.3% | 12.0% |
| Chandler Simpson | 312 | 0.268 | 0.323 | 0.055 | 0.298 | 0.253 | 0.0% | 8.9% | 8.2% |
| Cedric Mullins | 279 | 0.199 | 0.311 | 0.112 | 0.289 | 0.261 | 3.8% | 19.7% | 20.5% |
| Taylor Walls | 213 | 0.220 | 0.288 | 0.068 | 0.297 | 0.250 | 3.1% | 12.2% | 21.1% |
| Ben Williamson | 205 | 0.243 | 0.335 | 0.092 | 0.296 | 0.299 | 1.4% | 24.8% | 15.7% |
| Nick Fortes | 202 | 0.241 | 0.326 | 0.086 | 0.277 | 0.272 | 3.1% | 29.5% | 13.7% |
| Richie Palacios | 193 | 0.223 | 0.301 | 0.078 | 0.295 | 0.299 | 3.9% | 16.7% | 19.5% |
| Jonny Deluca | 156 | 0.270 | 0.432 | 0.162 | 0.330 | 0.282 | 4.3% | 20.6% | 22.8% |
| Ryan Vilade | 153 | 0.274 | 0.467 | 0.193 | 0.367 | 0.315 | 4.6% | 21.1% | 17.5% |
| Hunter Feduccia | 118 | 0.216 | 0.275 | 0.059 | 0.267 | 0.296 | 6.5% | 18.2% | 24.5% |


## Bullpen Fatigue Report

### Kansas City Royals Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alex Lange | 2026-06-22 | 1.0 | 15 |
| Beck Way | 2026-06-21 | 2.0 | 18 |
| Beck Way | 2026-06-23 | 1.0 | 16 |
| Connor Seabold | 2026-06-21 | 1.1 | 29 |
| Connor Seabold | 2026-06-23 | 1.0 | 37 |
| John Schreiber | 2026-06-22 | 1.0 | 18 |
| Lucas Erceg | 2026-06-21 | 1.1 | 18 |
| Matt Strahm | 2026-06-21 | 1.0 | 16 |
| Matt Strahm | 2026-06-23 | 1.0 | 16 |
| Steven Cruz | 2026-06-21 | 1.2 | 37 |
| Steven Cruz | 2026-06-23 | 1.0 | 10 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Beck Way, Connor Seabold, Matt Strahm, Steven Cruz


### Tampa Bay Rays Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Ben Williamson | 2026-06-23 | 1.0 | 11 |
| Bryan Baker | 2026-06-21 | 1.0 | 19 |
| Cam Booser | 2026-06-20 | 1.0 | 24 |
| Cam Booser | 2026-06-22 | 1.0 | 9 |
| Cole Sulser | 2026-06-20 | 2.0 | 25 |
| Cole Sulser | 2026-06-22 | 1.0 | 13 |
| Craig Kimbrel | 2026-06-20 | 1.0 | 11 |
| Craig Kimbrel | 2026-06-22 | 1.0 | 14 |
| Garrett Cleavinger | 2026-06-21 | 1.0 | 14 |
| Kevin Kelly | 2026-06-21 | 1.0 | 14 |
| Steven Matz | 2026-06-23 | 2.0 | 43 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Ben Williamson, Steven Matz



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bobby Witt | 347 | 0.288 | 0.456 | 0.168 | 0.367 | 12.2% | 32.7% |
| 2 | Salvador Pérez | 322 | 0.213 | 0.367 | 0.153 | 0.275 | 10.8% | 25.4% |
| 3 | Maikel García | 304 | 0.257 | 0.370 | 0.112 | 0.309 | 4.8% | 28.3% |
| 4 | Vinnie Pasquantino | 302 | 0.219 | 0.340 | 0.121 | 0.300 | 7.4% | 27.5% |
| 5 | Carter Jensen | 296 | 0.234 | 0.410 | 0.176 | 0.317 | 8.0% | 25.4% |
| 6 | Jac Caglianone | 290 | 0.272 | 0.487 | 0.215 | 0.363 | 16.6% | 33.6% |
| 7 | Isaac Collins | 273 | 0.218 | 0.306 | 0.087 | 0.299 | 5.9% | 26.4% |
| 8 | Lane Thomas | 221 | 0.219 | 0.355 | 0.137 | 0.326 | 5.7% | 21.0% |
| 9 | Kyle Isbel | 196 | 0.263 | 0.383 | 0.120 | 0.317 | 2.9% | 24.5% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Junior Caminero | 351 | 0.275 | 0.475 | 0.200 | 0.365 | 12.4% | 36.3% |
| 2 | Jonathan Aranda | 347 | 0.274 | 0.445 | 0.171 | 0.359 | 10.8% | 24.7% |
| 3 | Yandy Díaz | 345 | 0.330 | 0.507 | 0.177 | 0.403 | 8.3% | 30.3% |
| 4 | Chandler Simpson | 312 | 0.268 | 0.323 | 0.055 | 0.298 | 0.0% | 8.9% |
| 5 | Cedric Mullins | 279 | 0.199 | 0.311 | 0.112 | 0.289 | 3.8% | 19.7% |
| 6 | Taylor Walls | 213 | 0.220 | 0.288 | 0.068 | 0.297 | 3.1% | 12.2% |
| 7 | Ben Williamson | 205 | 0.243 | 0.335 | 0.092 | 0.296 | 1.4% | 24.8% |
| 8 | Nick Fortes | 202 | 0.241 | 0.326 | 0.086 | 0.277 | 3.1% | 29.5% |
| 9 | Richie Palacios | 193 | 0.223 | 0.301 | 0.078 | 0.295 | 3.9% | 16.7% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6777 |
| Hits Allowed | 1497 |
| Walks/HBP | 697 |
| Strikeouts | 1424 |
| Home Runs Allowed | 201 |
| K Event Rate | 21.0% |
| BB/HBP Event Rate | 10.3% |
| HR Event Rate | 3.0% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6411 |
| Hits Allowed | 1408 |
| Walks/HBP | 585 |
| Strikeouts | 1296 |
| Home Runs Allowed | 178 |
| K Event Rate | 20.2% |
| BB/HBP Event Rate | 9.1% |
| HR Event Rate | 2.8% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, CH, FC, CU, SL
- Home pitcher pitch mix to inspect: ST, CH, SI, FF, CU
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 9. New York Yankees @ Detroit Tigers

## Game Context

| Field | Value |
| --- | --- |
| Park | Comerica Park |
| Time | 2026-06-24T22:40:00Z |
| Away Team | New York Yankees |
| Home Team | Detroit Tigers |
| Away Probable Pitcher | Ryan Weathers |
| Home Probable Pitcher | Tarik Skubal |


## Away Starting Pitcher: Ryan Weathers

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1441 |
| Batted/Result Events | 365 |
| Hits Allowed | 81 |
| Walks | 24 |
| Strikeouts | 98 |
| Home Runs | 19 |
| K Event Rate | 26.8% |
| BB Event Rate | 6.6% |
| HR Event Rate | 5.2% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-18 | NYY | 7.3 | 3 | 1 | 1 | 8 | 1 |
| 2026-06-12 | TOR | 6.7 | 5 | 2 | 2 | 2 | 2 |
| 2026-06-05 | NYY | 8.7 | 7 | 2 | 1 | 4 | 2 |
| 2026-05-30 | ATH | 9.7 | 6 | 3 | 3 | 10 | 3 |
| 2026-05-24 | NYY | 8.7 | 4 | 0 | 3 | 4 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 1.4% | 20 | 0.167 | 0.167 | 0.000 | 0.150 | 0.222 | 0.0% | 20.0% | 44.4% |
| CH | vs R | 21.1% | 304 | 0.214 | 0.357 | 0.143 | 0.250 | 0.246 | 8.3% | 25.8% | 34.4% |
| FF | vs L | 3.2% | 46 | 0.357 | 1.000 | 0.643 | 0.557 | 0.357 | 44.4% | 53.8% | 34.8% |
| FF | vs R | 24.9% | 359 | 0.274 | 0.603 | 0.329 | 0.403 | 0.427 | 18.2% | 22.7% | 14.8% |
| SI | vs L | 6.9% | 100 | 0.379 | 0.483 | 0.103 | 0.418 | 0.438 | 8.7% | 31.0% | 10.0% |
| SI | vs R | 12.6% | 182 | 0.227 | 0.318 | 0.091 | 0.302 | 0.377 | 7.3% | 28.6% | 6.6% |
| SL | vs L | 2.6% | 38 | 0.182 | 0.182 | 0.000 | 0.208 | 0.172 | 0.0% | 0.0% | 31.2% |
| SL | vs R | 6.7% | 97 | 0.182 | 0.394 | 0.212 | 0.267 | 0.243 | 25.0% | 35.1% | 30.9% |
| ST | vs L | 5.7% | 82 | 0.250 | 0.312 | 0.062 | 0.274 | 0.252 | 0.0% | 21.4% | 48.3% |
| ST | vs R | 14.7% | 212 | 0.138 | 0.345 | 0.207 | 0.232 | 0.205 | 15.4% | 10.3% | 41.4% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-18 | 88 | 3 | 1 | 8 | 1 |
| 2026-06-12 | 82 | 5 | 1 | 2 | 2 |
| 2026-06-05 | 93 | 7 | 1 | 4 | 2 |
| 2026-05-30 | 107 | 6 | 3 | 10 | 3 |
| 2026-05-24 | 95 | 4 | 3 | 4 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Dillon Dingler | 28 | 0.462 | 1.154 | 0.692 | 0.670 | 0.451 | 13.6% | 34.2% | 22.4% |
| ST | Dillon Dingler | 26 | 0.292 | 0.792 | 0.500 | 0.465 | 0.436 | 15.8% | 31.2% | 19.1% |
| ST | Kerry Carpenter | 7 | 0.333 | 0.833 | 0.500 | 0.514 | 0.379 | 25.0% | 44.4% | 35.3% |
| CH | Kerry Carpenter | 32 | 0.385 | 0.846 | 0.462 | 0.577 | 0.366 | 10.5% | 36.8% | 25.9% |
| ST | Colt Keith | 8 | 0.286 | 0.714 | 0.429 | 0.450 | 0.468 | 20.0% | 28.6% | 33.3% |
| ST | Zach Mckinstry | 9 | 0.250 | 0.625 | 0.375 | 0.400 | 0.464 | 20.0% | 36.4% | 14.3% |
| SI | Jahmai Jones | 22 | 0.176 | 0.529 | 0.353 | 0.382 | 0.519 | 14.3% | 20.8% | 13.8% |
| CH | Wenceel Pérez | 35 | 0.206 | 0.529 | 0.324 | 0.314 | 0.199 | 7.1% | 22.9% | 23.1% |
| SI | Spencer Torkelson | 64 | 0.298 | 0.596 | 0.298 | 0.401 | 0.443 | 19.1% | 33.7% | 12.6% |
| SI | Wenceel Pérez | 35 | 0.290 | 0.581 | 0.290 | 0.404 | 0.395 | 17.2% | 23.3% | 9.6% |
| FF | Spencer Torkelson | 92 | 0.230 | 0.500 | 0.270 | 0.382 | 0.358 | 18.8% | 28.3% | 22.5% |
| FF | Dillon Dingler | 88 | 0.308 | 0.577 | 0.269 | 0.403 | 0.457 | 19.4% | 28.9% | 14.0% |
| FF | Kerry Carpenter | 60 | 0.192 | 0.462 | 0.269 | 0.317 | 0.323 | 8.6% | 27.8% | 23.7% |
| ST | Riley Greene | 22 | 0.312 | 0.562 | 0.250 | 0.502 | 0.442 | 10.0% | 16.0% | 28.2% |
| SI | Gleyber Torres | 44 | 0.333 | 0.583 | 0.250 | 0.447 | 0.329 | 6.5% | 18.6% | 5.7% |
| SL | Kevin Mcgonigle | 37 | 0.188 | 0.438 | 0.250 | 0.319 | 0.362 | 17.4% | 25.6% | 17.5% |
| FF | Hao-Yu Lee | 39 | 0.216 | 0.459 | 0.243 | 0.304 | 0.279 | 20.0% | 34.1% | 29.4% |
| CH | Colt Keith | 38 | 0.270 | 0.514 | 0.243 | 0.341 | 0.283 | 7.1% | 27.3% | 30.8% |
| SL | Spencer Torkelson | 41 | 0.216 | 0.459 | 0.243 | 0.323 | 0.291 | 12.0% | 27.3% | 33.7% |
| CH | Dillon Dingler | 36 | 0.235 | 0.471 | 0.235 | 0.350 | 0.299 | 8.3% | 35.6% | 34.7% |
| SL | Matt Vierling | 38 | 0.211 | 0.421 | 0.211 | 0.289 | 0.328 | 9.1% | 26.7% | 16.7% |
| ST | Matt Vierling | 24 | 0.292 | 0.500 | 0.208 | 0.335 | 0.271 | 0.0% | 15.0% | 8.5% |
| SL | Colt Keith | 26 | 0.200 | 0.400 | 0.200 | 0.304 | 0.209 | 20.0% | 35.0% | 38.9% |
| FF | Riley Greene | 122 | 0.252 | 0.437 | 0.184 | 0.352 | 0.356 | 15.3% | 23.0% | 21.8% |
| SI | Kevin Mcgonigle | 78 | 0.388 | 0.567 | 0.179 | 0.454 | 0.394 | 6.5% | 30.9% | 6.5% |
| ST | Hao-Yu Lee | 17 | 0.471 | 0.647 | 0.176 | 0.485 | 0.258 | 0.0% | 4.8% | 25.0% |
| CH | Riley Greene | 55 | 0.212 | 0.385 | 0.173 | 0.265 | 0.251 | 9.1% | 25.4% | 35.8% |
| FF | Gleyber Torres | 66 | 0.226 | 0.396 | 0.170 | 0.354 | 0.374 | 15.8% | 25.0% | 24.0% |
| CH | Spencer Torkelson | 33 | 0.200 | 0.367 | 0.167 | 0.282 | 0.277 | 35.7% | 36.8% | 41.3% |
| SI | Matt Vierling | 42 | 0.162 | 0.324 | 0.162 | 0.263 | 0.351 | 6.2% | 33.3% | 10.8% |


## Home Starting Pitcher: Tarik Skubal

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 874 |
| Batted/Result Events | 232 |
| Hits Allowed | 53 |
| Walks | 8 |
| Strikeouts | 62 |
| Home Runs | 5 |
| K Event Rate | 26.7% |
| BB Event Rate | 3.4% |
| HR Event Rate | 2.2% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | DET | 8.7 | 7 | 2 | 1 | 8 | 2 |
| 2026-06-13 | CLE | 7.0 | 5 | 1 | 2 | 4 | 1 |
| 2026-04-29 | ATL | 8.0 | 5 | 1 | 0 | 7 | 1 |
| 2026-04-23 | DET | 8.0 | 7 | 0 | 0 | 5 | 0 |
| 2026-04-18 | BOS | 7.7 | 4 | 0 | 2 | 10 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 4.2% | 37 | 0.300 | 0.700 | 0.400 | 0.410 | 0.120 | 0.0% | 38.5% | 43.5% |
| CH | vs R | 20.9% | 183 | 0.170 | 0.340 | 0.170 | 0.240 | 0.249 | 9.1% | 22.9% | 45.2% |
| CU | vs L | 0.5% | 4 | 0.000 | 0.000 | 0.000 | 0.000 | — | 0.0% | 0.0% | 100.0% |
| CU | vs R | 2.6% | 23 | 0.167 | 0.167 | 0.000 | 0.150 | 0.178 | 20.0% | 40.0% | 37.5% |
| FF | vs L | 3.3% | 29 | 0.167 | 0.667 | 0.500 | 0.333 | 0.392 | 50.0% | 21.4% | 27.3% |
| FF | vs R | 32.7% | 286 | 0.250 | 0.359 | 0.109 | 0.297 | 0.330 | 7.4% | 18.8% | 14.5% |
| SI | vs L | 11.4% | 100 | 0.400 | 0.400 | 0.000 | 0.385 | 0.403 | 0.0% | 36.1% | 11.1% |
| SI | vs R | 8.6% | 75 | 0.235 | 0.412 | 0.176 | 0.383 | 0.342 | 0.0% | 25.0% | 15.2% |
| SL | vs L | 1.7% | 15 | 0.429 | 0.571 | 0.143 | 0.564 | 0.366 | 0.0% | 42.9% | 0.0% |
| SL | vs R | 13.8% | 121 | 0.200 | 0.240 | 0.040 | 0.230 | 0.209 | 0.0% | 40.6% | 33.9% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 94 | 7 | 1 | 8 | 2 |
| 2026-06-13 | 80 | 5 | 1 | 4 | 1 |
| 2026-04-29 | 91 | 5 | 0 | 7 | 1 |
| 2026-04-23 | 94 | 7 | 0 | 5 | 0 |
| 2026-04-18 | 89 | 4 | 2 | 10 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF | Ben Rice | 78 | 0.369 | 1.031 | 0.662 | 0.608 | 0.565 | 32.0% | 39.8% | 15.6% |
| SL | Giancarlo Stanton | 14 | 0.385 | 1.000 | 0.615 | 0.579 | 0.531 | 42.9% | 30.8% | 43.3% |
| FF | Paul Goldschmidt | 63 | 0.389 | 0.944 | 0.556 | 0.561 | 0.445 | 23.9% | 28.7% | 17.0% |
| SI | Giancarlo Stanton | 12 | 0.417 | 0.917 | 0.500 | 0.558 | 0.482 | 27.3% | 37.5% | 20.0% |
| SL | Cody Bellinger | 39 | 0.375 | 0.875 | 0.500 | 0.558 | 0.460 | 16.7% | 27.5% | 19.2% |
| CH | Jazz Chisholm | 32 | 0.267 | 0.633 | 0.367 | 0.422 | 0.366 | 13.6% | 34.2% | 32.8% |
| SL | Jazz Chisholm | 46 | 0.244 | 0.585 | 0.341 | 0.383 | 0.320 | 14.3% | 36.2% | 37.5% |
| FF | Aaron Judge | 54 | 0.233 | 0.558 | 0.326 | 0.404 | 0.467 | 26.9% | 24.7% | 22.9% |
| SL | Trent Grisham | 23 | 0.158 | 0.474 | 0.316 | 0.374 | 0.283 | 18.2% | 30.0% | 34.4% |
| CH | Ben Rice | 34 | 0.312 | 0.625 | 0.312 | 0.440 | 0.422 | 20.0% | 33.3% | 29.5% |
| SI | Aaron Judge | 47 | 0.389 | 0.694 | 0.306 | 0.547 | 0.542 | 17.9% | 30.8% | 10.8% |
| SL | José Caballero | 39 | 0.297 | 0.595 | 0.297 | 0.391 | 0.352 | 3.2% | 20.8% | 32.1% |
| CH | Amed Rosario | 27 | 0.222 | 0.519 | 0.296 | 0.307 | 0.272 | 8.7% | 21.2% | 25.9% |
| SL | Ben Rice | 51 | 0.333 | 0.595 | 0.262 | 0.449 | 0.384 | 12.9% | 39.7% | 33.0% |
| SI | Jazz Chisholm | 42 | 0.378 | 0.622 | 0.243 | 0.461 | 0.398 | 6.5% | 28.3% | 17.8% |
| CH | Trent Grisham | 32 | 0.276 | 0.517 | 0.241 | 0.369 | 0.352 | 8.0% | 25.7% | 24.0% |
| FF | Anthony Volpe | 34 | 0.320 | 0.560 | 0.240 | 0.460 | 0.427 | 16.7% | 25.6% | 21.1% |
| SI | Ryan Mcmahon | 33 | 0.179 | 0.393 | 0.214 | 0.336 | 0.377 | 13.6% | 35.1% | 23.5% |
| SL | Amed Rosario | 14 | 0.286 | 0.500 | 0.214 | 0.336 | 0.354 | 12.5% | 22.7% | 33.3% |
| FF | Austin Wells | 61 | 0.200 | 0.400 | 0.200 | 0.322 | 0.320 | 7.5% | 25.8% | 17.9% |
| CH | Aaron Judge | 42 | 0.143 | 0.343 | 0.200 | 0.306 | 0.323 | 17.4% | 26.2% | 37.8% |
| CH | Ryan Mcmahon | 22 | 0.273 | 0.455 | 0.182 | 0.311 | 0.187 | 21.4% | 24.1% | 34.7% |
| FF | Ryan Mcmahon | 66 | 0.295 | 0.475 | 0.180 | 0.351 | 0.374 | 14.0% | 19.3% | 18.1% |
| SI | Ben Rice | 50 | 0.283 | 0.457 | 0.174 | 0.348 | 0.339 | 8.3% | 34.3% | 12.5% |
| FF | Trent Grisham | 107 | 0.239 | 0.409 | 0.170 | 0.351 | 0.417 | 16.2% | 35.8% | 10.8% |
| CH | Anthony Volpe | 6 | 0.333 | 0.500 | 0.167 | 0.508 | 0.201 | 0.0% | 8.3% | 27.8% |
| SI | Austin Wells | 35 | 0.226 | 0.387 | 0.161 | 0.297 | 0.334 | 8.3% | 36.8% | 14.0% |
| CH | Paul Goldschmidt | 28 | 0.320 | 0.480 | 0.160 | 0.384 | 0.416 | 14.3% | 29.6% | 25.6% |
| SI | José Caballero | 53 | 0.283 | 0.435 | 0.152 | 0.361 | 0.364 | 7.3% | 18.8% | 11.5% |
| SI | Cody Bellinger | 68 | 0.291 | 0.436 | 0.145 | 0.377 | 0.407 | 4.0% | 30.7% | 9.2% |


## New York Yankees Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cody Bellinger | 348 | 0.262 | 0.446 | 0.184 | 0.357 | 0.372 | 7.6% | 24.7% | 17.5% |
| Ben Rice | 337 | 0.274 | 0.579 | 0.305 | 0.407 | 0.385 | 14.7% | 31.7% | 23.2% |
| Jazz Chisholm | 323 | 0.228 | 0.407 | 0.179 | 0.321 | 0.301 | 8.8% | 28.5% | 29.8% |
| Trent Grisham | 281 | 0.232 | 0.397 | 0.165 | 0.337 | 0.360 | 11.4% | 32.6% | 15.1% |
| Aaron Judge | 270 | 0.250 | 0.536 | 0.286 | 0.399 | 0.415 | 21.9% | 31.3% | 30.8% |
| José Caballero | 256 | 0.250 | 0.384 | 0.134 | 0.315 | 0.288 | 3.9% | 16.6% | 23.6% |
| Paul Goldschmidt | 221 | 0.285 | 0.520 | 0.235 | 0.373 | 0.342 | 11.5% | 26.1% | 23.3% |
| Ryan Mcmahon | 220 | 0.217 | 0.365 | 0.148 | 0.282 | 0.304 | 12.6% | 26.7% | 28.2% |
| Austin Wells | 187 | 0.161 | 0.255 | 0.093 | 0.242 | 0.295 | 7.2% | 29.2% | 27.6% |
| Amed Rosario | 145 | 0.263 | 0.474 | 0.211 | 0.337 | 0.329 | 10.3% | 27.1% | 22.7% |
| Anthony Volpe | 113 | 0.278 | 0.381 | 0.103 | 0.354 | 0.325 | 4.2% | 21.0% | 22.6% |
| Giancarlo Stanton | 111 | 0.260 | 0.433 | 0.173 | 0.323 | 0.326 | 23.9% | 30.8% | 34.1% |


## Detroit Tigers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kevin Mcgonigle | 357 | 0.276 | 0.421 | 0.145 | 0.362 | 0.364 | 8.6% | 23.4% | 12.9% |
| Riley Greene | 354 | 0.294 | 0.454 | 0.160 | 0.372 | 0.360 | 13.3% | 29.4% | 27.4% |
| Spencer Torkelson | 325 | 0.208 | 0.415 | 0.208 | 0.315 | 0.313 | 14.6% | 27.3% | 28.1% |
| Dillon Dingler | 320 | 0.280 | 0.567 | 0.287 | 0.396 | 0.398 | 12.8% | 29.7% | 19.5% |
| Colt Keith | 246 | 0.260 | 0.370 | 0.110 | 0.311 | 0.320 | 8.9% | 28.7% | 21.8% |
| Matt Vierling | 235 | 0.197 | 0.347 | 0.150 | 0.271 | 0.298 | 6.2% | 20.8% | 14.9% |
| Kerry Carpenter | 201 | 0.211 | 0.429 | 0.217 | 0.319 | 0.303 | 9.6% | 28.7% | 28.6% |
| Gleyber Torres | 200 | 0.289 | 0.410 | 0.120 | 0.367 | 0.343 | 8.4% | 18.5% | 20.5% |
| Zach Mckinstry | 198 | 0.178 | 0.259 | 0.080 | 0.274 | 0.260 | 2.1% | 12.2% | 13.0% |
| Wenceel Pérez | 190 | 0.183 | 0.371 | 0.189 | 0.270 | 0.272 | 8.5% | 23.6% | 16.1% |
| Hao-Yu Lee | 114 | 0.239 | 0.358 | 0.119 | 0.280 | 0.271 | 8.9% | 19.6% | 28.2% |
| Jahmai Jones | 112 | 0.167 | 0.265 | 0.098 | 0.247 | 0.297 | 7.6% | 27.2% | 31.0% |


## Bullpen Fatigue Report

### New York Yankees Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brent Headrick | 2026-06-21 | 1.0 | 11 |
| Brent Headrick | 2026-06-23 | 1.2 | 22 |
| Camilo Doval | 2026-06-21 | 1.0 | 29 |
| David Bednar | 2026-06-23 | 1.1 | 17 |
| Fernando Cruz | 2026-06-21 | 0.2 | 12 |
| Fernando Cruz | 2026-06-23 | 0.2 | 17 |
| Jake Bird | 2026-06-20 | 1.0 | 15 |
| Max Schuemann | 2026-06-20 | 1.0 | 14 |
| Paul Blackburn | 2026-06-21 | 1.1 | 7 |
| Paul Blackburn | 2026-06-22 | 1.2 | 18 |
| Ryan Yarbrough | 2026-06-20 | 1.0 | 29 |
| Ryan Yarbrough | 2026-06-22 | 2.0 | 31 |
| Tim Hill | 2026-06-20 | 0.1 | 5 |
| Tim Hill | 2026-06-21 | 1.0 | 11 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Brent Headrick, David Bednar, Fernando Cruz


### Detroit Tigers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Drew Anderson | 2026-06-22 | 1.1 | 19 |
| Drew Sommers | 2026-06-21 | 1.0 | 17 |
| Drew Sommers | 2026-06-22 | 0.1 | 6 |
| Enmanuel De Jesus | 2026-06-23 | 1.0 | 14 |
| Kenley Jansen | 2026-06-20 | 1.0 | 10 |
| Kyle Finnegan | 2026-06-21 | 1.0 | 13 |
| Kyle Finnegan | 2026-06-23 | 1.1 | 18 |
| Tyler Holton | 2026-06-20 | 2.0 | 21 |
| Tyler Holton | 2026-06-23 | 1.0 | 17 |
| Will Vest | 2026-06-21 | 1.0 | 16 |
| Will Vest | 2026-06-22 | 1.1 | 12 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Enmanuel De Jesus, Kyle Finnegan, Tyler Holton



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cody Bellinger | 348 | 0.262 | 0.446 | 0.184 | 0.357 | 7.6% | 24.7% |
| 2 | Ben Rice | 337 | 0.274 | 0.579 | 0.305 | 0.407 | 14.7% | 31.7% |
| 3 | Jazz Chisholm | 323 | 0.228 | 0.407 | 0.179 | 0.321 | 8.8% | 28.5% |
| 4 | Trent Grisham | 281 | 0.232 | 0.397 | 0.165 | 0.337 | 11.4% | 32.6% |
| 5 | Aaron Judge | 270 | 0.250 | 0.536 | 0.286 | 0.399 | 21.9% | 31.3% |
| 6 | José Caballero | 256 | 0.250 | 0.384 | 0.134 | 0.315 | 3.9% | 16.6% |
| 7 | Paul Goldschmidt | 221 | 0.285 | 0.520 | 0.235 | 0.373 | 11.5% | 26.1% |
| 8 | Ryan Mcmahon | 220 | 0.217 | 0.365 | 0.148 | 0.282 | 12.6% | 26.7% |
| 9 | Austin Wells | 187 | 0.161 | 0.255 | 0.093 | 0.242 | 7.2% | 29.2% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Kevin Mcgonigle | 357 | 0.276 | 0.421 | 0.145 | 0.362 | 8.6% | 23.4% |
| 2 | Riley Greene | 354 | 0.294 | 0.454 | 0.160 | 0.372 | 13.3% | 29.4% |
| 3 | Spencer Torkelson | 325 | 0.208 | 0.415 | 0.208 | 0.315 | 14.6% | 27.3% |
| 4 | Dillon Dingler | 320 | 0.280 | 0.567 | 0.287 | 0.396 | 12.8% | 29.7% |
| 5 | Colt Keith | 246 | 0.260 | 0.370 | 0.110 | 0.311 | 8.9% | 28.7% |
| 6 | Matt Vierling | 235 | 0.197 | 0.347 | 0.150 | 0.271 | 6.2% | 20.8% |
| 7 | Kerry Carpenter | 201 | 0.211 | 0.429 | 0.217 | 0.319 | 9.6% | 28.7% |
| 8 | Gleyber Torres | 200 | 0.289 | 0.410 | 0.120 | 0.367 | 8.4% | 18.5% |
| 9 | Zach Mckinstry | 198 | 0.178 | 0.259 | 0.080 | 0.274 | 2.1% | 12.2% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6586 |
| Hits Allowed | 1390 |
| Walks/HBP | 662 |
| Strikeouts | 1540 |
| Home Runs Allowed | 210 |
| K Event Rate | 23.4% |
| BB/HBP Event Rate | 10.1% |
| HR Event Rate | 3.2% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6498 |
| Hits Allowed | 1392 |
| Walks/HBP | 636 |
| Strikeouts | 1449 |
| Home Runs Allowed | 184 |
| K Event Rate | 22.3% |
| BB/HBP Event Rate | 9.8% |
| HR Event Rate | 2.8% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, CH, ST, SI, SL
- Home pitcher pitch mix to inspect: FF, CH, SI, SL
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 10. Philadelphia Phillies @ Washington Nationals

## Game Context

| Field | Value |
| --- | --- |
| Park | Nationals Park |
| Time | 2026-06-24T22:45:00Z |
| Away Team | Philadelphia Phillies |
| Home Team | Washington Nationals |
| Away Probable Pitcher | Aaron Nola |
| Home Probable Pitcher | Carson Palmquist |


## Away Starting Pitcher: Aaron Nola

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1426 |
| Batted/Result Events | 354 |
| Hits Allowed | 93 |
| Walks | 28 |
| Strikeouts | 81 |
| Home Runs | 16 |
| K Event Rate | 22.9% |
| BB Event Rate | 7.9% |
| HR Event Rate | 4.5% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-18 | PHI | 8.0 | 7 | 2 | 1 | 6 | 2 |
| 2026-06-13 | MIL | 7.3 | 6 | 2 | 2 | 3 | 2 |
| 2026-06-07 | PHI | 7.7 | 6 | 0 | 4 | 4 | 0 |
| 2026-06-02 | PHI | 6.3 | 4 | 1 | 0 | 8 | 1 |
| 2026-05-26 | SD | 7.0 | 3 | 1 | 0 | 5 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 10.4% | 148 | 0.103 | 0.103 | 0.000 | 0.150 | 0.266 | 3.7% | 22.9% | 16.4% |
| CH | vs R | 2.0% | 29 | 0.400 | 1.000 | 0.600 | 0.600 | 0.187 | 20.0% | 30.0% | 9.1% |
| FC | vs L | 4.1% | 59 | 0.357 | 0.643 | 0.286 | 0.443 | 0.267 | 0.0% | 35.0% | 25.0% |
| FC | vs R | 4.7% | 67 | 0.444 | 0.611 | 0.167 | 0.471 | 0.384 | 0.0% | 28.6% | 19.4% |
| FF | vs L | 16.4% | 234 | 0.478 | 0.891 | 0.413 | 0.596 | 0.498 | 18.4% | 29.6% | 12.4% |
| FF | vs R | 7.6% | 109 | 0.318 | 0.682 | 0.364 | 0.407 | 0.357 | 21.4% | 25.9% | 18.9% |
| KC | vs L | 19.0% | 271 | 0.235 | 0.412 | 0.176 | 0.324 | 0.254 | 5.7% | 20.5% | 34.0% |
| KC | vs R | 14.3% | 204 | 0.197 | 0.303 | 0.106 | 0.229 | 0.213 | 6.8% | 15.4% | 36.9% |
| SI | vs L | 8.6% | 122 | 0.300 | 0.467 | 0.167 | 0.405 | 0.381 | 4.3% | 37.8% | 9.1% |
| SI | vs R | 12.1% | 172 | 0.324 | 0.595 | 0.270 | 0.399 | 0.353 | 13.8% | 26.5% | 11.5% |
| SL | vs R | 0.7% | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.145 | 0.0% | 42.9% | 22.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-18 | 97 | 7 | 1 | 6 | 2 |
| 2026-06-13 | 85 | 6 | 2 | 3 | 2 |
| 2026-06-07 | 99 | 6 | 4 | 4 | 0 |
| 2026-06-02 | 95 | 4 | 0 | 8 | 1 |
| 2026-05-26 | 80 | 3 | 0 | 5 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KC | Daylen Lile | 4 | 0.250 | 1.000 | 0.750 | 0.500 | 0.462 | 100.0% | 100.0% | 0.0% |
| FC | Keibert Ruiz | 9 | 0.429 | 1.143 | 0.714 | 0.578 | 0.440 | 33.3% | 27.3% | 4.3% |
| FC | Cj Abrams | 27 | 0.458 | 1.167 | 0.708 | 0.681 | 0.402 | 13.0% | 30.6% | 21.3% |
| FC | Curtis Mead | 21 | 0.235 | 0.647 | 0.412 | 0.426 | 0.447 | 13.3% | 29.4% | 18.6% |
| FC | James Wood | 27 | 0.280 | 0.640 | 0.360 | 0.381 | 0.488 | 26.1% | 37.2% | 27.0% |
| KC | Jacob Young | 3 | 0.667 | 1.000 | 0.333 | 0.717 | 0.519 | 0.0% | 25.0% | 33.3% |
| FC | José Tena | 9 | 0.222 | 0.556 | 0.333 | 0.417 | 0.412 | 0.0% | 33.3% | 28.0% |
| FF | James Wood | 106 | 0.333 | 0.633 | 0.300 | 0.453 | 0.487 | 23.8% | 36.2% | 17.4% |
| SI | Curtis Mead | 43 | 0.189 | 0.459 | 0.270 | 0.329 | 0.413 | 16.1% | 30.2% | 11.4% |
| FF | Brady House | 53 | 0.224 | 0.490 | 0.265 | 0.345 | 0.343 | 23.1% | 28.8% | 35.8% |
| CH | Keibert Ruiz | 34 | 0.294 | 0.559 | 0.265 | 0.360 | 0.224 | 3.7% | 34.1% | 26.3% |
| FF | Keibert Ruiz | 56 | 0.255 | 0.510 | 0.255 | 0.355 | 0.299 | 6.1% | 27.9% | 5.3% |
| FF | Cj Abrams | 85 | 0.362 | 0.609 | 0.246 | 0.471 | 0.430 | 12.5% | 20.7% | 21.7% |
| FF | Jacob Young | 76 | 0.239 | 0.478 | 0.239 | 0.361 | 0.351 | 7.5% | 24.8% | 12.4% |
| CH | Luis García | 52 | 0.250 | 0.481 | 0.231 | 0.309 | 0.279 | 9.5% | 22.1% | 22.0% |
| SI | James Wood | 62 | 0.327 | 0.551 | 0.224 | 0.443 | 0.500 | 20.5% | 42.9% | 15.7% |
| FF | José Tena | 47 | 0.220 | 0.439 | 0.220 | 0.350 | 0.366 | 9.4% | 22.5% | 20.4% |
| SI | Daylen Lile | 48 | 0.341 | 0.561 | 0.220 | 0.436 | 0.460 | 5.0% | 26.6% | 10.8% |
| SI | Luis García | 40 | 0.270 | 0.486 | 0.216 | 0.350 | 0.337 | 9.1% | 35.6% | 3.2% |
| FC | Jacob Young | 14 | 0.286 | 0.500 | 0.214 | 0.336 | 0.429 | 20.0% | 22.7% | 20.0% |
| CH | Cj Abrams | 45 | 0.186 | 0.395 | 0.209 | 0.264 | 0.298 | 9.4% | 26.7% | 29.5% |
| FF | Daylen Lile | 97 | 0.265 | 0.470 | 0.205 | 0.353 | 0.338 | 10.3% | 19.5% | 21.6% |
| FF | Luis García | 66 | 0.246 | 0.443 | 0.197 | 0.350 | 0.376 | 11.3% | 25.7% | 10.7% |
| SI | Drew Millas | 22 | 0.188 | 0.375 | 0.188 | 0.341 | 0.353 | 8.3% | 9.1% | 4.0% |
| FC | Luis García | 16 | 0.312 | 0.500 | 0.188 | 0.350 | 0.306 | 6.7% | 33.3% | 9.8% |
| CH | Jacob Young | 25 | 0.136 | 0.318 | 0.182 | 0.230 | 0.292 | 5.0% | 17.9% | 27.7% |
| CH | Curtis Mead | 25 | 0.227 | 0.409 | 0.182 | 0.322 | 0.365 | 5.3% | 34.1% | 11.8% |
| SI | Cj Abrams | 44 | 0.293 | 0.463 | 0.171 | 0.350 | 0.396 | 11.8% | 37.0% | 13.5% |
| SI | José Tena | 22 | 0.278 | 0.444 | 0.167 | 0.382 | 0.349 | 14.3% | 25.0% | 11.9% |
| FF | Curtis Mead | 68 | 0.200 | 0.350 | 0.150 | 0.302 | 0.339 | 9.3% | 19.3% | 12.1% |


## Home Starting Pitcher: Carson Palmquist

### Pitcher Profile

| Stat | Value |
| --- | --- |
| No data | — |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — | — | — |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No data | — | — | — | — | — | — | — | — | — | — | — |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| No data | — | — | — | — | — |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No data | — | — | — | — | — | — | — | — | — | — |


## Philadelphia Phillies Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Trea Turner | 359 | 0.219 | 0.320 | 0.102 | 0.274 | 0.282 | 4.7% | 27.3% | 25.5% |
| Kyle Schwarber | 348 | 0.249 | 0.593 | 0.343 | 0.405 | 0.385 | 21.5% | 34.8% | 31.2% |
| Bryce Harper | 337 | 0.268 | 0.514 | 0.246 | 0.384 | 0.407 | 12.4% | 28.7% | 28.0% |
| Alec Bohm | 322 | 0.227 | 0.356 | 0.129 | 0.300 | 0.292 | 4.0% | 26.5% | 14.3% |
| Brandon Marsh | 306 | 0.310 | 0.491 | 0.181 | 0.365 | 0.328 | 9.0% | 25.2% | 22.7% |
| Bryson Stott | 296 | 0.250 | 0.415 | 0.165 | 0.315 | 0.316 | 7.0% | 26.4% | 15.3% |
| Adolis García | 278 | 0.207 | 0.358 | 0.150 | 0.290 | 0.294 | 9.9% | 28.4% | 30.8% |
| Justin Crawford | 253 | 0.244 | 0.342 | 0.098 | 0.295 | 0.267 | 1.1% | 18.9% | 16.4% |
| J. T. Realmuto | 216 | 0.209 | 0.330 | 0.120 | 0.295 | 0.319 | 4.7% | 26.2% | 22.5% |
| Edmundo Sosa | 151 | 0.239 | 0.401 | 0.162 | 0.319 | 0.341 | 9.1% | 25.8% | 23.6% |
| Rafael Marchán | 92 | 0.103 | 0.172 | 0.069 | 0.179 | 0.195 | 2.9% | 16.2% | 16.7% |
| Otto Kemp | 48 | 0.156 | 0.311 | 0.156 | 0.228 | 0.205 | 6.9% | 12.3% | 30.9% |


## Washington Nationals Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| James Wood | 399 | 0.260 | 0.511 | 0.251 | 0.384 | 0.428 | 23.3% | 36.2% | 30.4% |
| Daylen Lile | 361 | 0.247 | 0.399 | 0.152 | 0.315 | 0.319 | 7.0% | 23.3% | 20.8% |
| Cj Abrams | 348 | 0.288 | 0.526 | 0.239 | 0.391 | 0.350 | 9.7% | 28.0% | 25.6% |
| Nasim Nuñez | 280 | 0.238 | 0.280 | 0.042 | 0.295 | 0.275 | 0.0% | 11.7% | 20.7% |
| Luis García | 276 | 0.252 | 0.455 | 0.203 | 0.322 | 0.329 | 9.7% | 28.7% | 17.1% |
| Jacob Young | 272 | 0.218 | 0.361 | 0.143 | 0.295 | 0.303 | 6.0% | 24.5% | 19.0% |
| Curtis Mead | 232 | 0.219 | 0.448 | 0.229 | 0.340 | 0.357 | 11.0% | 26.3% | 15.4% |
| Brady House | 193 | 0.242 | 0.404 | 0.163 | 0.315 | 0.320 | 9.5% | 28.9% | 30.2% |
| Keibert Ruiz | 189 | 0.270 | 0.455 | 0.185 | 0.325 | 0.273 | 5.1% | 28.8% | 11.6% |
| José Tena | 167 | 0.213 | 0.335 | 0.123 | 0.280 | 0.300 | 8.7% | 28.9% | 30.9% |
| Jorbit Vivas | 164 | 0.254 | 0.345 | 0.092 | 0.325 | 0.309 | 4.1% | 18.3% | 15.9% |
| Drew Millas | 136 | 0.174 | 0.256 | 0.083 | 0.264 | 0.272 | 3.4% | 12.3% | 20.4% |


## Bullpen Fatigue Report

### Philadelphia Phillies Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alan Rangel | 2026-06-22 | 5.0 | 72 |
| Chase Shugart | 2026-06-22 | 1.0 | 24 |
| Chase Shugart | 2026-06-23 | 1.0 | 12 |
| Jhoan Duran | 2026-06-20 | 1.0 | 17 |
| Jhoan Duran | 2026-06-21 | 1.0 | 15 |
| Jonathan Bowlan | 2026-06-21 | 0.1 | 4 |
| Jonathan Bowlan | 2026-06-23 | 0.1 | 5 |
| José Alvarado | 2026-06-21 | 1.0 | 21 |
| Max Lazar | 2026-06-20 | 2.0 | 26 |
| Orion Kerkering | 2026-06-21 | 1.0 | 11 |
| Orion Kerkering | 2026-06-23 | 1.0 | 22 |
| Seth Johnson | 2026-06-22 | 1.0 | 17 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Chase Shugart, Jonathan Bowlan, Orion Kerkering


### Washington Nationals Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brad Lord | 2026-06-20 | 3.0 | 36 |
| Brad Lord | 2026-06-23 | 0.2 | 30 |
| Clayton Beeter | 2026-06-20 | 1.0 | 21 |
| Clayton Beeter | 2026-06-22 | 1.0 | 6 |
| Clayton Beeter | 2026-06-23 | 0.1 | 9 |
| Gus Varland | 2026-06-21 | 2.0 | 32 |
| Mitchell Parker | 2026-06-20 | 2.1 | 32 |
| Mitchell Parker | 2026-06-23 | 1.1 | 15 |
| Orlando Ribalta | 2026-06-21 | 1.0 | 27 |
| Orlando Ribalta | 2026-06-23 | 1.0 | 17 |
| Paxton Schultz | 2026-06-21 | 1.0 | 16 |
| Paxton Schultz | 2026-06-23 | 0.1 | 21 |
| Richard Lovelady | 2026-06-22 | 0.2 | 9 |
| Richard Lovelady | 2026-06-23 | 0.1 | 15 |
| Zack Littell | 2026-06-23 | 4.0 | 59 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Brad Lord, Clayton Beeter, Mitchell Parker, Orlando Ribalta, Paxton Schultz, Richard Lovelady, Zack Littell



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Trea Turner | 359 | 0.219 | 0.320 | 0.102 | 0.274 | 4.7% | 27.3% |
| 2 | Kyle Schwarber | 348 | 0.249 | 0.593 | 0.343 | 0.405 | 21.5% | 34.8% |
| 3 | Bryce Harper | 337 | 0.268 | 0.514 | 0.246 | 0.384 | 12.4% | 28.7% |
| 4 | Alec Bohm | 322 | 0.227 | 0.356 | 0.129 | 0.300 | 4.0% | 26.5% |
| 5 | Brandon Marsh | 306 | 0.310 | 0.491 | 0.181 | 0.365 | 9.0% | 25.2% |
| 6 | Bryson Stott | 296 | 0.250 | 0.415 | 0.165 | 0.315 | 7.0% | 26.4% |
| 7 | Adolis García | 278 | 0.207 | 0.358 | 0.150 | 0.290 | 9.9% | 28.4% |
| 8 | Justin Crawford | 253 | 0.244 | 0.342 | 0.098 | 0.295 | 1.1% | 18.9% |
| 9 | J. T. Realmuto | 216 | 0.209 | 0.330 | 0.120 | 0.295 | 4.7% | 26.2% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | James Wood | 399 | 0.260 | 0.511 | 0.251 | 0.384 | 23.3% | 36.2% |
| 2 | Daylen Lile | 361 | 0.247 | 0.399 | 0.152 | 0.315 | 7.0% | 23.3% |
| 3 | Cj Abrams | 348 | 0.288 | 0.526 | 0.239 | 0.391 | 9.7% | 28.0% |
| 4 | Nasim Nuñez | 280 | 0.238 | 0.280 | 0.042 | 0.295 | 0.0% | 11.7% |
| 5 | Luis García | 276 | 0.252 | 0.455 | 0.203 | 0.322 | 9.7% | 28.7% |
| 6 | Jacob Young | 272 | 0.218 | 0.361 | 0.143 | 0.295 | 6.0% | 24.5% |
| 7 | Curtis Mead | 232 | 0.219 | 0.448 | 0.229 | 0.340 | 11.0% | 26.3% |
| 8 | Brady House | 193 | 0.242 | 0.404 | 0.163 | 0.315 | 9.5% | 28.9% |
| 9 | Keibert Ruiz | 189 | 0.270 | 0.455 | 0.185 | 0.325 | 5.1% | 28.8% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6606 |
| Hits Allowed | 1454 |
| Walks/HBP | 563 |
| Strikeouts | 1582 |
| Home Runs Allowed | 210 |
| K Event Rate | 23.9% |
| BB/HBP Event Rate | 8.5% |
| HR Event Rate | 3.2% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6809 |
| Hits Allowed | 1501 |
| Walks/HBP | 664 |
| Strikeouts | 1417 |
| Home Runs Allowed | 233 |
| K Event Rate | 20.8% |
| BB/HBP Event Rate | 9.8% |
| HR Event Rate | 3.4% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: KC, FF, SI, CH, FC
- Home pitcher pitch mix to inspect: No current Statcast sample
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 11. Houston Astros @ Toronto Blue Jays

## Game Context

| Field | Value |
| --- | --- |
| Park | Rogers Centre |
| Time | 2026-06-24T23:07:00Z |
| Away Team | Houston Astros |
| Home Team | Toronto Blue Jays |
| Away Probable Pitcher | Mike Burrows |
| Home Probable Pitcher | Trey Yesavage |


## Away Starting Pitcher: Mike Burrows

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1380 |
| Batted/Result Events | 376 |
| Hits Allowed | 102 |
| Walks | 30 |
| Strikeouts | 68 |
| Home Runs | 18 |
| K Event Rate | 18.1% |
| BB Event Rate | 8.0% |
| HR Event Rate | 4.8% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | HOU | 1.3 | 1 | 0 | 0 | 1 | 0 |
| 2026-06-13 | KC | 8.0 | 7 | 1 | 2 | 5 | 1 |
| 2026-06-07 | HOU | 8.7 | 8 | 2 | 2 | 3 | 2 |
| 2026-06-02 | HOU | 8.3 | 8 | 2 | 5 | 3 | 2 |
| 2026-05-27 | TEX | 9.0 | 5 | 1 | 1 | 6 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 20.3% | 280 | 0.304 | 0.377 | 0.072 | 0.358 | 0.307 | 3.3% | 19.6% | 28.9% |
| CH | vs R | 6.5% | 90 | 0.143 | 0.190 | 0.048 | 0.215 | 0.214 | 0.0% | 30.4% | 43.4% |
| CU | vs L | 8.7% | 120 | 0.333 | 0.714 | 0.381 | 0.448 | 0.395 | 25.0% | 34.6% | 18.4% |
| CU | vs R | 5.3% | 73 | 0.118 | 0.176 | 0.059 | 0.158 | 0.237 | 22.2% | 23.5% | 34.3% |
| FF | vs L | 19.9% | 274 | 0.323 | 0.758 | 0.435 | 0.475 | 0.430 | 17.0% | 32.7% | 9.5% |
| FF | vs R | 8.7% | 120 | 0.217 | 0.609 | 0.391 | 0.368 | 0.381 | 12.5% | 20.0% | 13.6% |
| SI | vs L | 2.9% | 40 | 0.455 | 0.545 | 0.091 | 0.462 | 0.461 | 0.0% | 35.3% | 10.0% |
| SI | vs R | 10.9% | 151 | 0.327 | 0.481 | 0.154 | 0.375 | 0.314 | 4.3% | 23.4% | 8.8% |
| SL | vs L | 8.0% | 111 | 0.258 | 0.516 | 0.258 | 0.359 | 0.391 | 13.6% | 35.7% | 24.6% |
| SL | vs R | 8.6% | 119 | 0.389 | 0.528 | 0.139 | 0.400 | 0.208 | 0.0% | 17.8% | 30.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 7 | 1 | 0 | 1 | 0 |
| 2026-06-13 | 93 | 7 | 2 | 5 | 1 |
| 2026-06-07 | 97 | 8 | 2 | 3 | 2 |
| 2026-06-02 | 90 | 8 | 5 | 3 | 2 |
| 2026-05-27 | 91 | 5 | 1 | 6 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Brandon Valenzuela | 13 | 0.308 | 1.231 | 0.923 | 0.615 | 0.464 | 57.1% | 36.8% | 38.2% |
| CH | Davis Schneider | 14 | 0.308 | 0.846 | 0.538 | 0.489 | 0.437 | 25.0% | 41.7% | 22.2% |
| CU | Andrés Giménez | 17 | 0.357 | 0.857 | 0.500 | 0.456 | 0.305 | 14.3% | 8.3% | 25.7% |
| CU | Nathan Lukes | 12 | 0.417 | 0.833 | 0.417 | 0.525 | 0.369 | 0.0% | 27.8% | 14.3% |
| SI | Davis Schneider | 15 | 0.364 | 0.727 | 0.364 | 0.490 | 0.465 | 33.3% | 35.3% | 9.1% |
| CU | Jesús Sánchez | 21 | 0.250 | 0.600 | 0.350 | 0.369 | 0.445 | 33.3% | 47.6% | 28.1% |
| CH | Myles Straw | 10 | 0.100 | 0.400 | 0.300 | 0.200 | 0.173 | 14.3% | 16.7% | 18.8% |
| FF | Kazuma Okamoto | 108 | 0.326 | 0.621 | 0.295 | 0.437 | 0.416 | 20.9% | 38.3% | 25.7% |
| CH | Yohendrick Pinango | 22 | 0.238 | 0.524 | 0.286 | 0.334 | 0.300 | 11.8% | 16.7% | 23.5% |
| SL | Kazuma Okamoto | 47 | 0.282 | 0.564 | 0.282 | 0.415 | 0.390 | 20.0% | 28.2% | 47.0% |
| FF | George Springer | 76 | 0.274 | 0.548 | 0.274 | 0.411 | 0.359 | 11.8% | 22.5% | 19.0% |
| FF | Daulton Varsho | 91 | 0.210 | 0.481 | 0.272 | 0.332 | 0.324 | 21.2% | 25.4% | 18.8% |
| SL | Nathan Lukes | 14 | 0.333 | 0.583 | 0.250 | 0.436 | 0.346 | 0.0% | 18.2% | 19.4% |
| SI | Yohendrick Pinango | 18 | 0.235 | 0.471 | 0.235 | 0.319 | 0.348 | 14.3% | 47.8% | 7.4% |
| CH | Ernie Clement | 32 | 0.258 | 0.484 | 0.226 | 0.305 | 0.254 | 3.8% | 19.1% | 21.5% |
| FF | Ernie Clement | 78 | 0.311 | 0.527 | 0.216 | 0.386 | 0.266 | 0.0% | 14.4% | 9.0% |
| SI | Kazuma Okamoto | 65 | 0.211 | 0.421 | 0.211 | 0.308 | 0.336 | 11.1% | 33.3% | 26.0% |
| FF | Andrés Giménez | 82 | 0.253 | 0.453 | 0.200 | 0.328 | 0.243 | 3.4% | 11.0% | 20.2% |
| SL | Jesús Sánchez | 26 | 0.240 | 0.440 | 0.200 | 0.304 | 0.376 | 20.0% | 33.3% | 24.5% |
| CH | George Springer | 26 | 0.227 | 0.409 | 0.182 | 0.363 | 0.334 | 15.4% | 28.6% | 29.8% |
| SL | Daulton Varsho | 43 | 0.225 | 0.400 | 0.175 | 0.337 | 0.262 | 3.1% | 17.2% | 21.2% |
| CH | Daulton Varsho | 20 | 0.278 | 0.444 | 0.167 | 0.350 | 0.440 | 5.9% | 17.1% | 10.0% |
| CU | Brandon Valenzuela | 16 | 0.308 | 0.462 | 0.154 | 0.400 | 0.320 | 0.0% | 11.8% | 30.8% |
| CH | Vladimir Guerrero | 35 | 0.364 | 0.515 | 0.152 | 0.400 | 0.373 | 3.4% | 31.7% | 26.3% |
| CH | Brandon Valenzuela | 22 | 0.300 | 0.450 | 0.150 | 0.359 | 0.377 | 13.3% | 18.8% | 33.3% |
| FF | Jesús Sánchez | 75 | 0.309 | 0.456 | 0.147 | 0.337 | 0.325 | 8.0% | 22.8% | 21.0% |
| FF | Vladimir Guerrero | 58 | 0.340 | 0.480 | 0.140 | 0.391 | 0.391 | 9.3% | 27.2% | 16.4% |
| CH | Andrés Giménez | 29 | 0.241 | 0.379 | 0.138 | 0.267 | 0.253 | 8.3% | 20.5% | 22.2% |
| CH | Nathan Lukes | 15 | 0.400 | 0.533 | 0.133 | 0.407 | 0.312 | 7.7% | 20.0% | 21.2% |
| CH | Kazuma Okamoto | 26 | 0.174 | 0.304 | 0.130 | 0.235 | 0.228 | 14.3% | 17.2% | 37.5% |


## Home Starting Pitcher: Trey Yesavage

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 883 |
| Batted/Result Events | 224 |
| Hits Allowed | 39 |
| Walks | 25 |
| Strikeouts | 53 |
| Home Runs | 5 |
| K Event Rate | 23.7% |
| BB Event Rate | 11.2% |
| HR Event Rate | 2.2% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-18 | BOS | 8.7 | 4 | 2 | 0 | 6 | 2 |
| 2026-06-12 | TOR | 8.3 | 4 | 1 | 6 | 3 | 1 |
| 2026-06-05 | TOR | 8.0 | 5 | 2 | 2 | 5 | 2 |
| 2026-05-30 | BAL | 7.0 | 2 | 0 | 7 | 4 | 0 |
| 2026-05-25 | TOR | 9.0 | 5 | 0 | 2 | 6 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF | vs L | 25.0% | 221 | 0.292 | 0.479 | 0.188 | 0.388 | 0.317 | 2.6% | 27.8% | 15.5% |
| FF | vs R | 21.4% | 189 | 0.128 | 0.298 | 0.170 | 0.240 | 0.224 | 2.7% | 17.7% | 15.8% |
| FS | vs L | 23.1% | 204 | 0.143 | 0.245 | 0.102 | 0.215 | 0.288 | 8.3% | 18.8% | 44.4% |
| FS | vs R | 7.9% | 70 | 0.125 | 0.125 | 0.000 | 0.160 | 0.165 | 0.0% | 30.0% | 30.0% |
| SL | vs L | 6.0% | 53 | 0.154 | 0.231 | 0.077 | 0.204 | 0.262 | 0.0% | 25.0% | 28.6% |
| SL | vs R | 16.5% | 146 | 0.310 | 0.586 | 0.276 | 0.402 | 0.276 | 10.5% | 24.4% | 40.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-18 | 95 | 4 | 0 | 6 | 2 |
| 2026-06-12 | 81 | 4 | 6 | 3 | 1 |
| 2026-06-05 | 91 | 5 | 2 | 5 | 2 |
| 2026-05-30 | 92 | 2 | 7 | 4 | 0 |
| 2026-05-25 | 98 | 5 | 2 | 6 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FS | Christian Walker | 5 | 0.200 | 0.800 | 0.600 | 0.400 | 0.430 | 25.0% | 40.0% | 25.0% |
| FS | Jeremy Peña | 7 | 0.500 | 1.000 | 0.500 | 0.643 | 0.549 | 25.0% | 33.3% | 40.0% |
| SL | Christian Walker | 61 | 0.271 | 0.695 | 0.424 | 0.408 | 0.275 | 14.0% | 32.2% | 39.4% |
| FS | Cam Smith | 12 | 0.333 | 0.750 | 0.417 | 0.450 | 0.287 | 12.5% | 45.5% | 35.0% |
| FF | Yordan Álvarez | 92 | 0.312 | 0.688 | 0.377 | 0.463 | 0.487 | 19.3% | 29.2% | 15.6% |
| SL | Jeremy Peña | 32 | 0.222 | 0.519 | 0.296 | 0.369 | 0.319 | 0.0% | 19.0% | 35.7% |
| SL | Yordan Álvarez | 41 | 0.289 | 0.579 | 0.289 | 0.395 | 0.403 | 20.0% | 20.4% | 22.1% |
| FF | Yainer Diaz | 32 | 0.250 | 0.536 | 0.286 | 0.375 | 0.352 | 13.6% | 20.9% | 23.0% |
| SL | Cam Smith | 37 | 0.219 | 0.500 | 0.281 | 0.358 | 0.360 | 23.8% | 26.7% | 37.5% |
| FF | Christian Walker | 94 | 0.192 | 0.436 | 0.244 | 0.348 | 0.311 | 9.1% | 21.2% | 22.1% |
| FF | Cam Smith | 91 | 0.263 | 0.474 | 0.211 | 0.369 | 0.388 | 17.2% | 31.6% | 20.5% |
| FF | José Altuve | 77 | 0.310 | 0.521 | 0.211 | 0.382 | 0.335 | 12.2% | 38.8% | 24.2% |
| SL | José Altuve | 41 | 0.184 | 0.368 | 0.184 | 0.255 | 0.269 | 6.9% | 8.7% | 27.3% |
| FF | Isaac Paredes | 95 | 0.214 | 0.393 | 0.179 | 0.318 | 0.339 | 8.5% | 24.8% | 10.5% |
| FF | Joey Loperfido | 38 | 0.387 | 0.548 | 0.161 | 0.459 | 0.413 | 8.0% | 34.8% | 19.7% |
| FF | Christian Vázquez | 73 | 0.219 | 0.375 | 0.156 | 0.295 | 0.265 | 3.7% | 12.7% | 15.2% |
| FF | Jeremy Peña | 38 | 0.364 | 0.515 | 0.152 | 0.424 | 0.455 | 7.1% | 20.0% | 9.8% |
| FF | Jake Meyers | 47 | 0.273 | 0.409 | 0.136 | 0.339 | 0.283 | 10.8% | 20.5% | 10.2% |
| FF | Carlos Correa | 36 | 0.267 | 0.400 | 0.133 | 0.357 | 0.315 | 9.1% | 20.8% | 13.0% |
| FF | Brice Matthews | 72 | 0.274 | 0.403 | 0.129 | 0.343 | 0.329 | 12.8% | 25.3% | 36.6% |
| SL | Carlos Correa | 22 | 0.222 | 0.333 | 0.111 | 0.291 | 0.283 | 14.3% | 23.8% | 30.3% |
| SL | Yainer Diaz | 20 | 0.200 | 0.300 | 0.100 | 0.215 | 0.256 | 6.2% | 13.8% | 25.6% |
| SL | Joey Loperfido | 17 | 0.067 | 0.133 | 0.067 | 0.197 | 0.181 | 0.0% | 9.5% | 41.5% |
| SL | Christian Vázquez | 18 | 0.125 | 0.188 | 0.062 | 0.169 | 0.152 | 0.0% | 20.8% | 29.4% |
| SL | Isaac Paredes | 41 | 0.132 | 0.184 | 0.053 | 0.161 | 0.176 | 0.0% | 23.5% | 27.3% |
| SL | Brice Matthews | 28 | 0.115 | 0.154 | 0.038 | 0.173 | 0.166 | 0.0% | 25.0% | 36.5% |
| FS | Brice Matthews | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.039 | 0.0% | 0.0% | 45.5% |
| FS | Isaac Paredes | 8 | 0.125 | 0.125 | 0.000 | 0.113 | 0.241 | 0.0% | 20.0% | 26.7% |
| FS | Yainer Diaz | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.108 | 0.0% | 0.0% | 33.3% |
| FS | Yordan Álvarez | 15 | 0.308 | 0.308 | 0.000 | 0.333 | 0.332 | 10.0% | 18.8% | 25.0% |


## Houston Astros Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yordan Álvarez | 362 | 0.318 | 0.619 | 0.301 | 0.437 | 0.485 | 18.4% | 31.0% | 16.8% |
| Christian Walker | 346 | 0.230 | 0.463 | 0.233 | 0.342 | 0.308 | 10.6% | 28.1% | 26.5% |
| Isaac Paredes | 318 | 0.245 | 0.410 | 0.165 | 0.344 | 0.324 | 6.4% | 23.1% | 16.9% |
| Cam Smith | 312 | 0.220 | 0.361 | 0.141 | 0.301 | 0.334 | 13.1% | 28.3% | 28.7% |
| José Altuve | 263 | 0.236 | 0.388 | 0.152 | 0.311 | 0.303 | 6.9% | 24.2% | 23.5% |
| Brice Matthews | 211 | 0.208 | 0.359 | 0.151 | 0.296 | 0.269 | 9.6% | 24.2% | 35.7% |
| Jeremy Peña | 179 | 0.284 | 0.451 | 0.167 | 0.363 | 0.350 | 4.4% | 24.5% | 25.1% |
| Christian Vázquez | 179 | 0.217 | 0.329 | 0.112 | 0.273 | 0.237 | 2.3% | 14.6% | 16.6% |
| Carlos Correa | 149 | 0.281 | 0.414 | 0.133 | 0.356 | 0.364 | 9.8% | 22.4% | 21.2% |
| Jake Meyers | 142 | 0.206 | 0.321 | 0.115 | 0.271 | 0.251 | 7.8% | 16.2% | 20.3% |
| Yainer Diaz | 135 | 0.244 | 0.370 | 0.126 | 0.294 | 0.289 | 5.6% | 19.7% | 20.3% |
| Joey Loperfido | 112 | 0.240 | 0.344 | 0.104 | 0.314 | 0.304 | 5.7% | 21.5% | 28.4% |


## Toronto Blue Jays Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kazuma Okamoto | 329 | 0.243 | 0.462 | 0.219 | 0.347 | 0.334 | 14.9% | 29.9% | 32.4% |
| Vladimir Guerrero | 329 | 0.288 | 0.386 | 0.098 | 0.339 | 0.348 | 7.5% | 30.0% | 17.2% |
| Ernie Clement | 316 | 0.286 | 0.428 | 0.141 | 0.324 | 0.268 | 2.6% | 17.1% | 14.9% |
| Andrés Giménez | 280 | 0.241 | 0.393 | 0.152 | 0.296 | 0.265 | 4.3% | 13.8% | 22.6% |
| George Springer | 273 | 0.247 | 0.439 | 0.192 | 0.354 | 0.315 | 9.6% | 22.5% | 21.1% |
| Daulton Varsho | 271 | 0.259 | 0.440 | 0.181 | 0.352 | 0.317 | 8.4% | 24.0% | 17.4% |
| Jesús Sánchez | 248 | 0.286 | 0.458 | 0.172 | 0.343 | 0.339 | 10.8% | 27.1% | 23.4% |
| Nathan Lukes | 169 | 0.312 | 0.403 | 0.091 | 0.351 | 0.295 | 0.8% | 15.5% | 16.4% |
| Brandon Valenzuela | 166 | 0.253 | 0.438 | 0.185 | 0.337 | 0.340 | 8.4% | 22.8% | 24.0% |
| Myles Straw | 150 | 0.241 | 0.323 | 0.083 | 0.286 | 0.306 | 3.5% | 17.1% | 12.0% |
| Yohendrick Pinango | 138 | 0.289 | 0.445 | 0.156 | 0.351 | 0.319 | 8.2% | 27.0% | 21.1% |
| Davis Schneider | 124 | 0.165 | 0.301 | 0.136 | 0.273 | 0.285 | 10.9% | 28.4% | 26.7% |


## Bullpen Fatigue Report

### Houston Astros Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| AJ Blubaugh | 2026-06-20 | 1.0 | 16 |
| AJ Blubaugh | 2026-06-22 | 2.0 | 38 |
| Bryan Abreu | 2026-06-20 | 1.0 | 11 |
| Bryan King | 2026-06-21 | 1.0 | 11 |
| Bryan King | 2026-06-22 | 0.2 | 11 |
| Enyel De Los Santos | 2026-06-22 | 1.1 | 19 |
| Enyel De Los Santos | 2026-06-23 | 1.1 | 26 |
| Josh Hader | 2026-06-21 | 1.0 | 9 |
| Josh Hader | 2026-06-23 | 1.0 | 16 |
| Logan VanWey | 2026-06-22 | 1.0 | 16 |
| Logan VanWey | 2026-06-23 | 2.0 | 23 |
| Nate Pearson | 2026-06-20 | 1.0 | 24 |
| Nate Pearson | 2026-06-23 | 1.0 | 21 |
| Steven Okert | 2026-06-21 | 1.0 | 21 |
| Steven Okert | 2026-06-23 | 1.0 | 17 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Enyel De Los Santos, Josh Hader, Logan VanWey, Nate Pearson, Steven Okert


### Toronto Blue Jays Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Braydon Fisher | 2026-06-22 | 1.1 | 6 |
| Braydon Fisher | 2026-06-23 | 2.0 | 26 |
| Jeff Hoffman | 2026-06-20 | 1.0 | 22 |
| Jeff Hoffman | 2026-06-23 | 0.2 | 13 |
| Lazaro Estrada | 2026-06-20 | 2.1 | 32 |
| Louis Varland | 2026-06-20 | 2.0 | 28 |
| Louis Varland | 2026-06-22 | 1.0 | 12 |
| Mason Fluharty | 2026-06-20 | 0.0 | 11 |
| Mason Fluharty | 2026-06-23 | 1.0 | 15 |
| Spencer Miles | 2026-06-23 | 1.1 | 28 |
| Tommy Nance | 2026-06-23 | 1.1 | 17 |
| Tyler Rogers | 2026-06-22 | 1.0 | 19 |
| Tyler Rogers | 2026-06-23 | 1.0 | 18 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Braydon Fisher, Jeff Hoffman, Mason Fluharty, Spencer Miles, Tommy Nance, Tyler Rogers



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Yordan Álvarez | 362 | 0.318 | 0.619 | 0.301 | 0.437 | 18.4% | 31.0% |
| 2 | Christian Walker | 346 | 0.230 | 0.463 | 0.233 | 0.342 | 10.6% | 28.1% |
| 3 | Isaac Paredes | 318 | 0.245 | 0.410 | 0.165 | 0.344 | 6.4% | 23.1% |
| 4 | Cam Smith | 312 | 0.220 | 0.361 | 0.141 | 0.301 | 13.1% | 28.3% |
| 5 | José Altuve | 263 | 0.236 | 0.388 | 0.152 | 0.311 | 6.9% | 24.2% |
| 6 | Brice Matthews | 211 | 0.208 | 0.359 | 0.151 | 0.296 | 9.6% | 24.2% |
| 7 | Jeremy Peña | 179 | 0.284 | 0.451 | 0.167 | 0.363 | 4.4% | 24.5% |
| 8 | Christian Vázquez | 179 | 0.217 | 0.329 | 0.112 | 0.273 | 2.3% | 14.6% |
| 9 | Carlos Correa | 149 | 0.281 | 0.414 | 0.133 | 0.356 | 9.8% | 22.4% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Kazuma Okamoto | 329 | 0.243 | 0.462 | 0.219 | 0.347 | 14.9% | 29.9% |
| 2 | Vladimir Guerrero | 329 | 0.288 | 0.386 | 0.098 | 0.339 | 7.5% | 30.0% |
| 3 | Ernie Clement | 316 | 0.286 | 0.428 | 0.141 | 0.324 | 2.6% | 17.1% |
| 4 | Andrés Giménez | 280 | 0.241 | 0.393 | 0.152 | 0.296 | 4.3% | 13.8% |
| 5 | George Springer | 273 | 0.247 | 0.439 | 0.192 | 0.354 | 9.6% | 22.5% |
| 6 | Daulton Varsho | 271 | 0.259 | 0.440 | 0.181 | 0.352 | 8.4% | 24.0% |
| 7 | Jesús Sánchez | 248 | 0.286 | 0.458 | 0.172 | 0.343 | 10.8% | 27.1% |
| 8 | Nathan Lukes | 169 | 0.312 | 0.403 | 0.091 | 0.351 | 0.8% | 15.5% |
| 9 | Brandon Valenzuela | 166 | 0.253 | 0.438 | 0.185 | 0.337 | 8.4% | 22.8% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6712 |
| Hits Allowed | 1412 |
| Walks/HBP | 753 |
| Strikeouts | 1497 |
| Home Runs Allowed | 219 |
| K Event Rate | 22.3% |
| BB/HBP Event Rate | 11.2% |
| HR Event Rate | 3.3% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6438 |
| Hits Allowed | 1425 |
| Walks/HBP | 578 |
| Strikeouts | 1371 |
| Home Runs Allowed | 183 |
| K Event Rate | 21.3% |
| BB/HBP Event Rate | 9.0% |
| HR Event Rate | 2.8% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, CH, SL, CU, SI
- Home pitcher pitch mix to inspect: FF, FS, SL
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 12. Milwaukee Brewers @ Cincinnati Reds

## Game Context

| Field | Value |
| --- | --- |
| Park | Great American Ball Park |
| Time | 2026-06-24T23:10:00Z |
| Away Team | Milwaukee Brewers |
| Home Team | Cincinnati Reds |
| Away Probable Pitcher | Shane Drohan |
| Home Probable Pitcher | Rhett Lowder |


## Away Starting Pitcher: Shane Drohan

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 830 |
| Batted/Result Events | 216 |
| Hits Allowed | 48 |
| Walks | 16 |
| Strikeouts | 52 |
| Home Runs | 5 |
| K Event Rate | 24.1% |
| BB Event Rate | 7.4% |
| HR Event Rate | 2.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-18 | MIL | 7.0 | 3 | 1 | 4 | 3 | 1 |
| 2026-06-13 | MIL | 7.7 | 8 | 1 | 0 | 7 | 1 |
| 2026-06-07 | COL | 8.0 | 5 | 0 | 1 | 4 | 0 |
| 2026-06-01 | MIL | 5.7 | 4 | 1 | 2 | 5 | 1 |
| 2026-05-27 | MIL | 2.3 | 1 | 0 | 0 | 1 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.346 | 0.0% | 0.0% | 0.0% |
| CH | vs R | 5.1% | 42 | 0.000 | 0.000 | 0.000 | 0.100 | 0.286 | 0.0% | 10.0% | 45.0% |
| CU | vs L | 0.4% | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.397 | 0.0% | 50.0% | 0.0% |
| CU | vs R | 12.9% | 107 | 0.222 | 0.222 | 0.000 | 0.250 | 0.243 | 0.0% | 14.8% | 36.2% |
| FC | vs L | 4.5% | 37 | 0.167 | 0.333 | 0.167 | 0.279 | 0.349 | 16.7% | 7.7% | 27.8% |
| FC | vs R | 8.9% | 74 | 0.435 | 0.739 | 0.304 | 0.526 | 0.353 | 8.7% | 27.0% | 10.9% |
| FF | vs L | 10.4% | 86 | 0.263 | 0.316 | 0.053 | 0.357 | 0.355 | 14.3% | 25.0% | 21.2% |
| FF | vs R | 18.8% | 156 | 0.103 | 0.241 | 0.138 | 0.225 | 0.181 | 6.2% | 16.4% | 23.5% |
| SI | vs L | 8.8% | 73 | 0.353 | 0.588 | 0.235 | 0.417 | 0.313 | 6.2% | 30.4% | 16.1% |
| SI | vs R | 10.7% | 89 | 0.321 | 0.607 | 0.286 | 0.403 | 0.346 | 16.0% | 37.1% | 7.5% |
| SL | vs L | 12.5% | 104 | 0.294 | 0.382 | 0.088 | 0.299 | 0.223 | 4.3% | 18.8% | 40.7% |
| SL | vs R | 7.0% | 58 | 0.000 | 0.000 | 0.000 | 0.100 | 0.230 | 0.0% | 22.2% | 20.7% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-18 | 91 | 3 | 3 | 3 | 1 |
| 2026-06-13 | 78 | 8 | 0 | 7 | 1 |
| 2026-06-07 | 83 | 5 | 1 | 4 | 0 |
| 2026-06-01 | 68 | 4 | 2 | 5 | 1 |
| 2026-05-27 | 27 | 1 | 0 | 1 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Jj Bleday | 14 | 0.455 | 1.364 | 0.909 | 0.732 | 0.614 | 30.0% | 78.6% | 37.5% |
| FC | Eugenio Suárez | 14 | 0.429 | 1.286 | 0.857 | 0.700 | 0.375 | 30.0% | 46.2% | 23.8% |
| FC | Nathaniel Lowe | 14 | 0.462 | 1.154 | 0.692 | 0.732 | 0.481 | 44.4% | 33.3% | 16.0% |
| SL | Nathaniel Lowe | 13 | 0.308 | 0.769 | 0.462 | 0.446 | 0.121 | 12.5% | 23.1% | 25.0% |
| SI | Tyler Stephenson | 41 | 0.412 | 0.824 | 0.412 | 0.573 | 0.561 | 25.9% | 37.2% | 16.4% |
| FF | Jj Bleday | 52 | 0.214 | 0.571 | 0.357 | 0.368 | 0.489 | 22.2% | 23.8% | 9.4% |
| SL | Jj Bleday | 25 | 0.304 | 0.652 | 0.348 | 0.424 | 0.312 | 5.6% | 31.0% | 30.2% |
| FF | Elly De La Cruz | 99 | 0.256 | 0.600 | 0.344 | 0.395 | 0.427 | 29.5% | 37.6% | 16.4% |
| SL | Elly De La Cruz | 21 | 0.190 | 0.524 | 0.333 | 0.336 | 0.361 | 15.4% | 42.9% | 25.7% |
| FC | Elly De La Cruz | 16 | 0.462 | 0.769 | 0.308 | 0.556 | 0.448 | 8.3% | 28.0% | 12.9% |
| FC | Matt Mclain | 12 | 0.200 | 0.500 | 0.300 | 0.358 | 0.298 | 14.3% | 18.8% | 33.3% |
| FF | Sal Stewart | 98 | 0.300 | 0.575 | 0.275 | 0.448 | 0.371 | 18.4% | 29.7% | 32.6% |
| CU | Tj Friedl | 13 | 0.182 | 0.455 | 0.273 | 0.277 | 0.293 | 10.0% | 28.6% | 27.3% |
| CU | Eugenio Suárez | 12 | 0.273 | 0.545 | 0.273 | 0.375 | 0.440 | 20.0% | 16.7% | 38.1% |
| FC | Jj Bleday | 17 | 0.200 | 0.467 | 0.267 | 0.379 | 0.379 | 10.0% | 29.6% | 14.7% |
| FF | Spencer Steer | 77 | 0.194 | 0.448 | 0.254 | 0.323 | 0.352 | 24.4% | 27.3% | 27.5% |
| SI | Ke'Bryan Hayes | 35 | 0.219 | 0.469 | 0.250 | 0.323 | 0.401 | 15.4% | 41.5% | 10.9% |
| SI | Dane Myers | 29 | 0.522 | 0.739 | 0.217 | 0.641 | 0.562 | 11.1% | 27.3% | 2.6% |
| CU | Matt Mclain | 16 | 0.071 | 0.286 | 0.214 | 0.212 | 0.302 | 9.1% | 46.7% | 26.1% |
| SL | Sal Stewart | 47 | 0.150 | 0.350 | 0.200 | 0.281 | 0.253 | 10.7% | 19.2% | 27.8% |
| SI | Sal Stewart | 82 | 0.236 | 0.431 | 0.194 | 0.334 | 0.433 | 15.9% | 28.6% | 13.8% |
| SL | Matt Mclain | 51 | 0.170 | 0.362 | 0.191 | 0.277 | 0.314 | 12.1% | 24.5% | 28.2% |
| FC | Spencer Steer | 24 | 0.429 | 0.619 | 0.190 | 0.485 | 0.446 | 6.2% | 30.8% | 21.6% |
| SI | Elly De La Cruz | 35 | 0.250 | 0.438 | 0.188 | 0.309 | 0.307 | 15.0% | 33.3% | 18.2% |
| SI | Spencer Steer | 86 | 0.229 | 0.414 | 0.186 | 0.344 | 0.378 | 10.5% | 27.6% | 14.7% |
| SI | Matt Mclain | 59 | 0.275 | 0.451 | 0.176 | 0.367 | 0.378 | 9.5% | 22.5% | 11.7% |
| SL | Spencer Steer | 34 | 0.219 | 0.375 | 0.156 | 0.279 | 0.363 | 8.7% | 25.7% | 28.4% |
| FC | Sal Stewart | 26 | 0.346 | 0.500 | 0.154 | 0.367 | 0.403 | 9.1% | 31.2% | 25.5% |
| FF | Tyler Stephenson | 72 | 0.238 | 0.381 | 0.143 | 0.310 | 0.389 | 14.0% | 28.0% | 24.3% |
| SI | Tj Friedl | 33 | 0.321 | 0.464 | 0.143 | 0.394 | 0.398 | 4.5% | 38.7% | 4.9% |


## Home Starting Pitcher: Rhett Lowder

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 963 |
| Batted/Result Events | 247 |
| Hits Allowed | 52 |
| Walks | 28 |
| Strikeouts | 45 |
| Home Runs | 5 |
| K Event Rate | 18.2% |
| BB Event Rate | 11.3% |
| HR Event Rate | 2.0% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | NYY | 8.3 | 6 | 2 | 3 | 5 | 2 |
| 2026-06-13 | CIN | 8.3 | 5 | 1 | 3 | 6 | 1 |
| 2026-06-07 | STL | 5.3 | 1 | 0 | 6 | 4 | 0 |
| 2026-05-07 | CHC | 4.3 | 1 | 1 | 4 | 1 | 1 |
| 2026-05-02 | PIT | 4.3 | 5 | 0 | 4 | 1 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 16.4% | 158 | 0.167 | 0.306 | 0.139 | 0.250 | 0.324 | 7.4% | 23.1% | 21.7% |
| CH | vs R | 4.9% | 47 | 0.375 | 0.375 | 0.000 | 0.338 | 0.200 | 0.0% | 25.0% | 28.6% |
| FF | vs L | 17.9% | 172 | 0.220 | 0.390 | 0.171 | 0.345 | 0.389 | 12.9% | 30.6% | 11.5% |
| FF | vs R | 6.2% | 60 | 0.231 | 0.231 | 0.000 | 0.208 | 0.219 | 0.0% | 11.1% | 15.6% |
| SI | vs L | 15.1% | 145 | 0.167 | 0.200 | 0.033 | 0.275 | 0.457 | 20.0% | 35.3% | 3.5% |
| SI | vs R | 14.6% | 141 | 0.282 | 0.359 | 0.077 | 0.377 | 0.358 | 0.0% | 28.6% | 4.5% |
| SL | vs L | 12.0% | 116 | 0.444 | 1.000 | 0.556 | 0.613 | 0.418 | 21.4% | 32.1% | 33.3% |
| SL | vs R | 12.8% | 123 | 0.219 | 0.281 | 0.062 | 0.233 | 0.231 | 0.0% | 24.1% | 38.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 95 | 6 | 3 | 5 | 2 |
| 2026-06-13 | 96 | 5 | 2 | 6 | 1 |
| 2026-06-07 | 70 | 1 | 5 | 4 | 0 |
| 2026-05-07 | 59 | 1 | 4 | 1 | 1 |
| 2026-05-02 | 52 | 5 | 4 | 1 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | Christian Yelich | 19 | 0.400 | 0.933 | 0.533 | 0.584 | 0.347 | 20.0% | 28.6% | 25.8% |
| FF | Andrew Vaughn | 36 | 0.483 | 0.931 | 0.448 | 0.617 | 0.474 | 11.5% | 31.1% | 9.8% |
| CH | Jake Bauers | 28 | 0.360 | 0.720 | 0.360 | 0.480 | 0.357 | 22.2% | 48.0% | 46.2% |
| FF | Jake Bauers | 79 | 0.380 | 0.732 | 0.352 | 0.492 | 0.390 | 19.2% | 31.7% | 14.4% |
| FF | Gary Sánchez | 49 | 0.297 | 0.595 | 0.297 | 0.455 | 0.438 | 13.8% | 21.2% | 19.4% |
| CH | Jackson Chourio | 21 | 0.400 | 0.650 | 0.250 | 0.462 | 0.238 | 5.9% | 28.6% | 14.3% |
| FF | William Contreras | 86 | 0.243 | 0.486 | 0.243 | 0.383 | 0.380 | 9.2% | 37.3% | 12.1% |
| FF | Jackson Chourio | 58 | 0.259 | 0.463 | 0.204 | 0.349 | 0.327 | 19.4% | 25.9% | 23.9% |
| SI | Brice Turang | 64 | 0.273 | 0.473 | 0.200 | 0.391 | 0.351 | 4.8% | 22.4% | 10.6% |
| CH | Gary Sánchez | 17 | 0.267 | 0.467 | 0.200 | 0.318 | 0.268 | 7.7% | 43.8% | 41.7% |
| FF | David Hamilton | 79 | 0.258 | 0.455 | 0.197 | 0.365 | 0.315 | 5.3% | 18.4% | 9.2% |
| SI | Jackson Chourio | 47 | 0.357 | 0.548 | 0.190 | 0.443 | 0.414 | 9.4% | 42.9% | 10.7% |
| FF | Brice Turang | 100 | 0.215 | 0.405 | 0.190 | 0.356 | 0.349 | 12.5% | 16.5% | 19.1% |
| SL | Jake Bauers | 45 | 0.158 | 0.342 | 0.184 | 0.286 | 0.303 | 9.5% | 29.2% | 28.2% |
| SL | Andrew Vaughn | 19 | 0.353 | 0.529 | 0.176 | 0.413 | 0.330 | 6.7% | 33.3% | 21.4% |
| CH | Brice Turang | 35 | 0.207 | 0.379 | 0.172 | 0.331 | 0.329 | 0.0% | 18.6% | 20.6% |
| SI | Jake Bauers | 58 | 0.229 | 0.396 | 0.167 | 0.341 | 0.366 | 10.0% | 30.0% | 12.4% |
| SL | Brice Turang | 49 | 0.256 | 0.419 | 0.163 | 0.340 | 0.351 | 10.0% | 39.0% | 22.8% |
| SL | Garrett Mitchell | 42 | 0.135 | 0.297 | 0.162 | 0.226 | 0.299 | 15.0% | 21.2% | 52.7% |
| CH | Andrew Vaughn | 17 | 0.429 | 0.571 | 0.143 | 0.482 | 0.508 | 0.0% | 58.8% | 20.8% |
| FF | Garrett Mitchell | 94 | 0.203 | 0.329 | 0.127 | 0.307 | 0.332 | 16.7% | 24.5% | 28.3% |
| SI | Gary Sánchez | 30 | 0.250 | 0.375 | 0.125 | 0.357 | 0.383 | 4.8% | 29.4% | 2.8% |
| SI | Sal Frelick | 57 | 0.294 | 0.412 | 0.118 | 0.380 | 0.312 | 2.0% | 20.3% | 1.4% |
| FF | Luis Rengifo | 62 | 0.283 | 0.396 | 0.113 | 0.354 | 0.346 | 4.3% | 19.8% | 6.9% |
| CH | Garrett Mitchell | 21 | 0.278 | 0.389 | 0.111 | 0.348 | 0.304 | 8.3% | 23.5% | 53.5% |
| CH | William Contreras | 21 | 0.389 | 0.500 | 0.111 | 0.433 | 0.341 | 0.0% | 28.6% | 32.6% |
| SL | David Hamilton | 32 | 0.286 | 0.393 | 0.107 | 0.298 | 0.176 | 9.5% | 27.6% | 41.1% |
| FF | Christian Yelich | 52 | 0.250 | 0.354 | 0.104 | 0.295 | 0.294 | 6.1% | 17.8% | 22.3% |
| SI | William Contreras | 91 | 0.362 | 0.463 | 0.100 | 0.387 | 0.364 | 10.0% | 37.5% | 6.2% |
| SL | Christian Yelich | 34 | 0.129 | 0.226 | 0.097 | 0.221 | 0.222 | 6.2% | 25.0% | 50.0% |


## Milwaukee Brewers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brice Turang | 343 | 0.259 | 0.452 | 0.193 | 0.364 | 0.354 | 9.4% | 22.9% | 19.5% |
| William Contreras | 331 | 0.302 | 0.443 | 0.141 | 0.364 | 0.346 | 8.5% | 33.3% | 17.6% |
| Jake Bauers | 290 | 0.277 | 0.550 | 0.273 | 0.398 | 0.353 | 14.8% | 34.3% | 23.6% |
| Sal Frelick | 277 | 0.230 | 0.315 | 0.085 | 0.306 | 0.281 | 1.9% | 19.6% | 9.6% |
| Garrett Mitchell | 267 | 0.228 | 0.375 | 0.147 | 0.316 | 0.327 | 13.0% | 27.3% | 36.0% |
| Luis Rengifo | 229 | 0.211 | 0.289 | 0.078 | 0.274 | 0.296 | 5.5% | 23.1% | 15.8% |
| David Hamilton | 228 | 0.253 | 0.354 | 0.101 | 0.310 | 0.269 | 5.1% | 18.2% | 19.4% |
| Christian Yelich | 222 | 0.246 | 0.392 | 0.146 | 0.316 | 0.297 | 6.6% | 19.1% | 29.3% |
| Jackson Chourio | 213 | 0.294 | 0.528 | 0.234 | 0.380 | 0.336 | 13.3% | 28.8% | 22.3% |
| Joey Ortiz | 208 | 0.208 | 0.253 | 0.045 | 0.265 | 0.285 | 2.8% | 21.8% | 18.1% |
| Gary Sánchez | 161 | 0.227 | 0.455 | 0.227 | 0.357 | 0.363 | 9.8% | 28.0% | 23.5% |
| Andrew Vaughn | 151 | 0.338 | 0.508 | 0.169 | 0.417 | 0.369 | 5.4% | 32.9% | 17.1% |


## Cincinnati Reds Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sal Stewart | 363 | 0.248 | 0.452 | 0.204 | 0.351 | 0.358 | 14.4% | 25.1% | 24.3% |
| Spencer Steer | 316 | 0.238 | 0.434 | 0.196 | 0.335 | 0.350 | 13.9% | 27.4% | 22.4% |
| Matt Mclain | 306 | 0.217 | 0.382 | 0.165 | 0.315 | 0.324 | 10.7% | 22.9% | 23.3% |
| Elly De La Cruz | 283 | 0.273 | 0.508 | 0.234 | 0.373 | 0.359 | 16.2% | 35.3% | 27.7% |
| Tyler Stephenson | 235 | 0.213 | 0.353 | 0.140 | 0.298 | 0.325 | 11.5% | 26.0% | 26.0% |
| Jj Bleday | 223 | 0.251 | 0.560 | 0.309 | 0.398 | 0.371 | 11.6% | 31.7% | 24.3% |
| Nathaniel Lowe | 212 | 0.257 | 0.487 | 0.230 | 0.371 | 0.363 | 12.2% | 21.7% | 16.5% |
| Eugenio Suárez | 212 | 0.202 | 0.347 | 0.145 | 0.290 | 0.258 | 7.6% | 18.9% | 33.6% |
| Tj Friedl | 193 | 0.201 | 0.284 | 0.083 | 0.261 | 0.250 | 3.3% | 22.3% | 24.3% |
| Blake Dunn | 151 | 0.266 | 0.367 | 0.101 | 0.321 | 0.280 | 2.9% | 20.5% | 21.2% |
| Ke'Bryan Hayes | 146 | 0.157 | 0.231 | 0.075 | 0.224 | 0.312 | 8.5% | 31.3% | 18.1% |
| Dane Myers | 140 | 0.269 | 0.387 | 0.118 | 0.355 | 0.372 | 7.4% | 22.5% | 16.1% |


## Bullpen Fatigue Report

### Milwaukee Brewers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Aaron Ashby | 2026-06-20 | 0.1 | 14 |
| Aaron Ashby | 2026-06-22 | 1.0 | 17 |
| Aaron Ashby | 2026-06-23 | 1.0 | 14 |
| Abner Uribe | 2026-06-20 | 0.2 | 8 |
| Abner Uribe | 2026-06-22 | 1.0 | 10 |
| Abner Uribe | 2026-06-23 | 1.0 | 16 |
| Chad Patrick | 2026-06-21 | 3.0 | 40 |
| Joel Kuhnel | 2026-06-22 | 1.0 | 10 |
| Trevor Megill | 2026-06-20 | 1.0 | 8 |
| Trevor Megill | 2026-06-22 | 1.0 | 12 |
| Trevor Megill | 2026-06-23 | 1.0 | 12 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Aaron Ashby, Abner Uribe, Trevor Megill


### Cincinnati Reds Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brock Burke | 2026-06-20 | 1.0 | 13 |
| Brock Burke | 2026-06-22 | 0.1 | 6 |
| Caleb Ferguson | 2026-06-21 | 1.0 | 13 |
| Caleb Ferguson | 2026-06-23 | 0.2 | 8 |
| Chase Petty | 2026-06-20 | 1.0 | 23 |
| Chase Petty | 2026-06-23 | 2.0 | 34 |
| Julian Garcia | 2026-06-23 | 1.2 | 35 |
| Pierce Johnson | 2026-06-23 | 0.2 | 7 |
| Sam Moll | 2026-06-21 | 1.0 | 21 |
| Sam Moll | 2026-06-22 | 1.0 | 12 |
| Tejay Antone | 2026-06-20 | 2.0 | 23 |
| Tejay Antone | 2026-06-22 | 0.2 | 11 |
| Tony Santillan | 2026-06-21 | 2.0 | 16 |
| Tony Santillan | 2026-06-22 | 1.0 | 13 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Caleb Ferguson, Chase Petty, Julian Garcia, Pierce Johnson



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Brice Turang | 343 | 0.259 | 0.452 | 0.193 | 0.364 | 9.4% | 22.9% |
| 2 | William Contreras | 331 | 0.302 | 0.443 | 0.141 | 0.364 | 8.5% | 33.3% |
| 3 | Jake Bauers | 290 | 0.277 | 0.550 | 0.273 | 0.398 | 14.8% | 34.3% |
| 4 | Sal Frelick | 277 | 0.230 | 0.315 | 0.085 | 0.306 | 1.9% | 19.6% |
| 5 | Garrett Mitchell | 267 | 0.228 | 0.375 | 0.147 | 0.316 | 13.0% | 27.3% |
| 6 | Luis Rengifo | 229 | 0.211 | 0.289 | 0.078 | 0.274 | 5.5% | 23.1% |
| 7 | David Hamilton | 228 | 0.253 | 0.354 | 0.101 | 0.310 | 5.1% | 18.2% |
| 8 | Christian Yelich | 222 | 0.246 | 0.392 | 0.146 | 0.316 | 6.6% | 19.1% |
| 9 | Jackson Chourio | 213 | 0.294 | 0.528 | 0.234 | 0.380 | 13.3% | 28.8% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Sal Stewart | 363 | 0.248 | 0.452 | 0.204 | 0.351 | 14.4% | 25.1% |
| 2 | Spencer Steer | 316 | 0.238 | 0.434 | 0.196 | 0.335 | 13.9% | 27.4% |
| 3 | Matt Mclain | 306 | 0.217 | 0.382 | 0.165 | 0.315 | 10.7% | 22.9% |
| 4 | Elly De La Cruz | 283 | 0.273 | 0.508 | 0.234 | 0.373 | 16.2% | 35.3% |
| 5 | Tyler Stephenson | 235 | 0.213 | 0.353 | 0.140 | 0.298 | 11.5% | 26.0% |
| 6 | Jj Bleday | 223 | 0.251 | 0.560 | 0.309 | 0.398 | 11.6% | 31.7% |
| 7 | Nathaniel Lowe | 212 | 0.257 | 0.487 | 0.230 | 0.371 | 12.2% | 21.7% |
| 8 | Eugenio Suárez | 212 | 0.202 | 0.347 | 0.145 | 0.290 | 7.6% | 18.9% |
| 9 | Tj Friedl | 193 | 0.201 | 0.284 | 0.083 | 0.261 | 3.3% | 22.3% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6619 |
| Hits Allowed | 1389 |
| Walks/HBP | 681 |
| Strikeouts | 1578 |
| Home Runs Allowed | 171 |
| K Event Rate | 23.8% |
| BB/HBP Event Rate | 10.3% |
| HR Event Rate | 2.6% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6829 |
| Hits Allowed | 1433 |
| Walks/HBP | 763 |
| Strikeouts | 1541 |
| Home Runs Allowed | 231 |
| K Event Rate | 22.6% |
| BB/HBP Event Rate | 11.2% |
| HR Event Rate | 3.4% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL, SI, FC, CU
- Home pitcher pitch mix to inspect: SI, SL, FF, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 13. Los Angeles Dodgers @ Minnesota Twins

## Game Context

| Field | Value |
| --- | --- |
| Park | Target Field |
| Time | 2026-06-24T23:40:00Z |
| Away Team | Los Angeles Dodgers |
| Home Team | Minnesota Twins |
| Away Probable Pitcher | Shohei Ohtani |
| Home Probable Pitcher | Joe Ryan |


## Away Starting Pitcher: Shohei Ohtani

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1283 |
| Batted/Result Events | 323 |
| Hits Allowed | 48 |
| Walks | 26 |
| Strikeouts | 93 |
| Home Runs | 3 |
| K Event Rate | 28.8% |
| BB Event Rate | 8.0% |
| HR Event Rate | 0.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-17 | LAD | 9.0 | 7 | 0 | 2 | 5 | 0 |
| 2026-06-10 | PIT | 9.7 | 6 | 1 | 4 | 6 | 1 |
| 2026-06-03 | AZ | 6.7 | 2 | 0 | 1 | 6 | 0 |
| 2026-05-27 | LAD | 7.7 | 0 | 0 | 5 | 7 | 0 |
| 2026-05-20 | SD | 6.3 | 3 | 0 | 2 | 4 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 7.6% | 97 | 0.133 | 0.133 | 0.000 | 0.188 | 0.190 | 0.0% | 7.1% | 36.0% |
| CU | vs R | 3.7% | 48 | 0.000 | 0.000 | 0.000 | 0.127 | 0.295 | 0.0% | 50.0% | 60.0% |
| FC | vs L | 0.4% | 5 | 0.500 | 0.500 | 0.000 | 0.450 | 0.456 | 0.0% | 33.3% | 0.0% |
| FC | vs R | 0.2% | 2 | 0.000 | 0.000 | 0.000 | 0.700 | 0.700 | 0.0% | 0.0% | 0.0% |
| FF | vs L | 26.9% | 345 | 0.204 | 0.312 | 0.108 | 0.283 | 0.273 | 4.0% | 23.0% | 18.4% |
| FF | vs R | 17.8% | 229 | 0.130 | 0.217 | 0.087 | 0.183 | 0.228 | 4.2% | 20.3% | 34.6% |
| FS | vs L | 8.0% | 102 | 0.154 | 0.231 | 0.077 | 0.167 | 0.214 | 0.0% | 33.3% | 31.9% |
| FS | vs R | 1.4% | 18 | 0.600 | 0.800 | 0.200 | 0.610 | 0.324 | 0.0% | 75.0% | 37.5% |
| SI | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | 0.000 | — | 0.0% | 0.0% | 0.0% |
| SI | vs R | 4.8% | 61 | 0.214 | 0.214 | 0.000 | 0.345 | 0.355 | 0.0% | 35.3% | 25.0% |
| SL | vs L | 0.9% | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.550 | 50.0% | 28.6% | 12.5% |
| SL | vs R | 0.2% | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.469 | 0.0% | 0.0% | 0.0% |
| ST | vs L | 9.4% | 120 | 0.118 | 0.176 | 0.059 | 0.212 | 0.293 | 0.0% | 16.7% | 44.2% |
| ST | vs R | 18.8% | 241 | 0.140 | 0.193 | 0.053 | 0.181 | 0.220 | 5.1% | 13.2% | 32.4% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-17 | 91 | 7 | 1 | 5 | 0 |
| 2026-06-10 | 102 | 6 | 3 | 6 | 1 |
| 2026-06-03 | 89 | 2 | 1 | 6 | 0 |
| 2026-05-27 | 99 | 0 | 4 | 7 | 0 |
| 2026-05-20 | 88 | 3 | 2 | 4 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Víctor Caratini | 6 | 0.200 | 0.800 | 0.600 | 0.450 | 0.225 | 50.0% | 25.0% | 33.3% |
| FF | Byron Buxton | 92 | 0.321 | 0.753 | 0.432 | 0.477 | 0.428 | 34.5% | 35.1% | 24.7% |
| FS | Kody Clemens | 13 | 0.182 | 0.545 | 0.364 | 0.427 | 0.322 | 25.0% | 23.1% | 16.7% |
| CU | Byron Buxton | 17 | 0.353 | 0.706 | 0.353 | 0.444 | 0.290 | 14.3% | 54.5% | 21.4% |
| ST | Austin Martin | 16 | 0.467 | 0.800 | 0.333 | 0.550 | 0.369 | 0.0% | 25.0% | 29.2% |
| CU | Royce Lewis | 9 | 0.333 | 0.667 | 0.333 | 0.422 | 0.345 | 14.3% | 23.1% | 12.5% |
| ST | Ryan Jeffers | 21 | 0.200 | 0.500 | 0.300 | 0.352 | 0.287 | 13.3% | 22.2% | 24.0% |
| CU | Tristan Gray | 11 | 0.300 | 0.600 | 0.300 | 0.345 | 0.280 | 12.5% | 23.5% | 41.9% |
| FF | Brooks Lee | 88 | 0.273 | 0.558 | 0.286 | 0.395 | 0.299 | 8.8% | 15.9% | 15.3% |
| ST | Kody Clemens | 14 | 0.250 | 0.500 | 0.250 | 0.336 | 0.261 | 12.5% | 15.8% | 23.1% |
| CU | Kody Clemens | 23 | 0.238 | 0.476 | 0.238 | 0.335 | 0.258 | 8.3% | 35.7% | 33.3% |
| ST | Matt Wallner | 13 | 0.077 | 0.308 | 0.231 | 0.154 | 0.157 | 100.0% | 16.7% | 66.7% |
| CU | Austin Martin | 12 | 0.222 | 0.444 | 0.222 | 0.383 | 0.212 | 0.0% | 0.0% | 25.0% |
| CU | Trevor Larnach | 24 | 0.333 | 0.524 | 0.190 | 0.448 | 0.331 | 6.7% | 18.2% | 37.1% |
| FF | Kody Clemens | 85 | 0.216 | 0.405 | 0.189 | 0.322 | 0.293 | 8.8% | 22.1% | 21.8% |
| FF | Ryan Jeffers | 45 | 0.211 | 0.395 | 0.184 | 0.309 | 0.359 | 25.0% | 25.7% | 8.6% |
| FF | Luke Keaschall | 80 | 0.282 | 0.465 | 0.183 | 0.356 | 0.317 | 4.9% | 24.0% | 11.1% |
| FF | Josh Bell | 102 | 0.307 | 0.489 | 0.182 | 0.400 | 0.363 | 5.5% | 20.7% | 18.7% |
| FF | Trevor Larnach | 89 | 0.325 | 0.500 | 0.175 | 0.390 | 0.396 | 8.3% | 30.4% | 11.5% |
| ST | Josh Bell | 13 | 0.167 | 0.333 | 0.167 | 0.246 | 0.169 | 0.0% | 12.5% | 32.0% |
| FF | Royce Lewis | 57 | 0.160 | 0.320 | 0.160 | 0.251 | 0.277 | 25.0% | 22.7% | 26.6% |
| ST | Byron Buxton | 26 | 0.160 | 0.320 | 0.160 | 0.221 | 0.167 | 16.7% | 11.5% | 43.4% |
| CU | Brooks Lee | 27 | 0.115 | 0.269 | 0.154 | 0.180 | 0.144 | 5.6% | 19.4% | 26.8% |
| CU | Matt Wallner | 8 | 0.143 | 0.286 | 0.143 | 0.244 | 0.311 | 0.0% | 45.5% | 40.9% |
| FF | Matt Wallner | 50 | 0.209 | 0.349 | 0.140 | 0.304 | 0.231 | 11.5% | 22.6% | 34.2% |
| ST | Royce Lewis | 15 | 0.333 | 0.467 | 0.133 | 0.347 | 0.288 | 0.0% | 26.1% | 30.6% |
| FF | Víctor Caratini | 86 | 0.197 | 0.329 | 0.132 | 0.294 | 0.319 | 6.6% | 19.4% | 16.2% |
| FS | Brooks Lee | 8 | 0.250 | 0.375 | 0.125 | 0.269 | 0.100 | 0.0% | 20.0% | 9.1% |
| CU | Josh Bell | 30 | 0.222 | 0.333 | 0.111 | 0.287 | 0.277 | 11.8% | 21.4% | 45.3% |
| FS | Trevor Larnach | 13 | 0.200 | 0.300 | 0.100 | 0.327 | 0.311 | 0.0% | 27.3% | 42.1% |


## Home Starting Pitcher: Joe Ryan

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1559 |
| Batted/Result Events | 390 |
| Hits Allowed | 77 |
| Walks | 20 |
| Strikeouts | 107 |
| Home Runs | 9 |
| K Event Rate | 27.4% |
| BB Event Rate | 5.1% |
| HR Event Rate | 2.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-18 | TEX | 6.7 | 3 | 0 | 2 | 7 | 0 |
| 2026-06-12 | MIN | 8.0 | 6 | 1 | 0 | 8 | 1 |
| 2026-06-06 | MIN | 8.7 | 6 | 1 | 2 | 5 | 1 |
| 2026-06-01 | MIN | 9.0 | 8 | 2 | 0 | 9 | 2 |
| 2026-05-26 | CWS | 10.0 | 5 | 1 | 2 | 9 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF | vs L | 24.7% | 385 | 0.210 | 0.410 | 0.200 | 0.297 | 0.295 | 13.2% | 25.5% | 19.1% |
| FF | vs R | 19.2% | 300 | 0.280 | 0.360 | 0.080 | 0.338 | 0.329 | 13.9% | 21.2% | 23.6% |
| FS | vs L | 10.1% | 157 | 0.091 | 0.182 | 0.091 | 0.174 | 0.235 | 4.3% | 34.7% | 25.0% |
| FS | vs R | 0.9% | 14 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 20.0% |
| KC | vs L | 7.2% | 113 | 0.231 | 0.385 | 0.154 | 0.322 | 0.294 | 13.3% | 21.4% | 20.0% |
| KC | vs R | 4.4% | 69 | 0.143 | 0.214 | 0.071 | 0.179 | 0.121 | 0.0% | 17.4% | 36.6% |
| SI | vs L | 4.1% | 64 | 0.176 | 0.176 | 0.000 | 0.240 | 0.301 | 0.0% | 16.0% | 10.7% |
| SI | vs R | 7.9% | 123 | 0.294 | 0.324 | 0.029 | 0.267 | 0.301 | 12.9% | 40.4% | 6.7% |
| SL | vs L | 1.8% | 28 | 0.250 | 0.500 | 0.250 | 0.390 | 0.713 | 50.0% | 33.3% | 20.0% |
| SL | vs R | 5.8% | 91 | 0.286 | 0.357 | 0.071 | 0.282 | 0.283 | 8.3% | 13.3% | 22.0% |
| ST | vs L | 5.5% | 86 | 0.278 | 0.444 | 0.167 | 0.311 | 0.331 | 16.7% | 28.6% | 23.1% |
| ST | vs R | 8.1% | 127 | 0.147 | 0.265 | 0.118 | 0.223 | 0.174 | 5.0% | 10.8% | 38.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-18 | 97 | 3 | 2 | 7 | 0 |
| 2026-06-12 | 102 | 6 | 0 | 8 | 1 |
| 2026-06-06 | 103 | 6 | 2 | 5 | 1 |
| 2026-06-01 | 98 | 8 | 0 | 9 | 2 |
| 2026-05-26 | 98 | 5 | 0 | 9 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KC | Andy Pages | 4 | 0.333 | 1.333 | 1.000 | 0.675 | 0.448 | 100.0% | 100.0% | 57.1% |
| SI | Shohei Ohtani | 48 | 0.513 | 0.949 | 0.436 | 0.621 | 0.576 | 19.4% | 43.1% | 16.7% |
| ST | Dalton Rushing | 7 | 0.143 | 0.571 | 0.429 | 0.286 | 0.233 | 25.0% | 14.3% | 57.1% |
| ST | Kyle Tucker | 19 | 0.267 | 0.667 | 0.400 | 0.450 | 0.327 | 16.7% | 29.4% | 34.6% |
| FS | Shohei Ohtani | 12 | 0.400 | 0.800 | 0.400 | 0.538 | 0.366 | 11.1% | 23.1% | 18.2% |
| FS | Freddie Freeman | 10 | 0.500 | 0.900 | 0.400 | 0.595 | 0.395 | 20.0% | 33.3% | 11.1% |
| FF | Max Muncy | 129 | 0.346 | 0.701 | 0.355 | 0.484 | 0.462 | 22.5% | 33.7% | 18.7% |
| FS | Mookie Betts | 4 | 0.333 | 0.667 | 0.333 | 0.487 | 0.327 | 50.0% | 25.0% | 33.3% |
| FF | Freddie Freeman | 108 | 0.333 | 0.645 | 0.312 | 0.447 | 0.403 | 12.7% | 21.5% | 19.1% |
| FS | Alex Freeland | 12 | 0.300 | 0.600 | 0.300 | 0.450 | 0.292 | 0.0% | 55.6% | 35.7% |
| FF | Mookie Betts | 58 | 0.216 | 0.510 | 0.294 | 0.365 | 0.344 | 15.2% | 25.3% | 3.6% |
| ST | Andy Pages | 27 | 0.385 | 0.654 | 0.269 | 0.452 | 0.411 | 9.5% | 21.7% | 22.6% |
| SI | Dalton Rushing | 10 | 0.375 | 0.625 | 0.250 | 0.480 | 0.343 | 0.0% | 19.0% | 0.0% |
| FF | Dalton Rushing | 60 | 0.286 | 0.531 | 0.245 | 0.426 | 0.353 | 12.9% | 27.7% | 28.7% |
| SI | Max Muncy | 63 | 0.302 | 0.547 | 0.245 | 0.413 | 0.386 | 13.6% | 27.8% | 11.5% |
| FF | Shohei Ohtani | 93 | 0.231 | 0.462 | 0.231 | 0.367 | 0.430 | 24.1% | 23.9% | 19.1% |
| SI | Will Smith | 48 | 0.300 | 0.500 | 0.200 | 0.358 | 0.474 | 22.2% | 33.3% | 4.1% |
| FF | Teoscar Hernández | 54 | 0.283 | 0.478 | 0.196 | 0.368 | 0.367 | 14.3% | 23.8% | 17.1% |
| ST | Shohei Ohtani | 29 | 0.192 | 0.385 | 0.192 | 0.290 | 0.310 | 11.1% | 38.5% | 28.9% |
| SI | Hyeseong Kim | 23 | 0.381 | 0.571 | 0.190 | 0.407 | 0.355 | 5.6% | 20.0% | 16.4% |
| FF | Will Smith | 66 | 0.226 | 0.415 | 0.189 | 0.357 | 0.458 | 20.0% | 27.8% | 14.5% |
| FF | Kyle Tucker | 106 | 0.242 | 0.429 | 0.187 | 0.361 | 0.362 | 11.3% | 22.8% | 17.9% |
| SI | Freddie Freeman | 66 | 0.236 | 0.418 | 0.182 | 0.348 | 0.366 | 8.2% | 22.3% | 17.2% |
| KC | Kyle Tucker | 7 | 0.333 | 0.500 | 0.167 | 0.407 | 0.517 | 0.0% | 33.3% | 11.1% |
| FF | Miguel Rojas | 47 | 0.302 | 0.465 | 0.163 | 0.347 | 0.364 | 10.5% | 37.1% | 11.0% |
| SI | Andy Pages | 77 | 0.294 | 0.456 | 0.162 | 0.358 | 0.391 | 6.7% | 36.0% | 9.1% |
| FF | Alex Freeland | 60 | 0.300 | 0.460 | 0.160 | 0.382 | 0.374 | 7.1% | 28.2% | 17.4% |
| FF | Andy Pages | 101 | 0.220 | 0.363 | 0.143 | 0.280 | 0.322 | 9.0% | 23.1% | 21.7% |
| ST | Teoscar Hernández | 21 | 0.190 | 0.333 | 0.143 | 0.224 | 0.177 | 10.0% | 16.7% | 43.8% |
| SI | Kyle Tucker | 43 | 0.200 | 0.343 | 0.143 | 0.301 | 0.360 | 3.1% | 29.4% | 10.3% |


## Los Angeles Dodgers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Andy Pages | 359 | 0.266 | 0.465 | 0.199 | 0.344 | 0.342 | 8.0% | 26.6% | 20.6% |
| Freddie Freeman | 358 | 0.278 | 0.485 | 0.207 | 0.370 | 0.382 | 11.5% | 25.6% | 19.2% |
| Shohei Ohtani | 346 | 0.291 | 0.546 | 0.255 | 0.411 | 0.423 | 17.7% | 30.6% | 24.8% |
| Kyle Tucker | 337 | 0.234 | 0.379 | 0.145 | 0.327 | 0.323 | 5.8% | 24.3% | 21.8% |
| Max Muncy | 296 | 0.267 | 0.514 | 0.247 | 0.383 | 0.382 | 16.3% | 29.0% | 24.4% |
| Teoscar Hernández | 224 | 0.286 | 0.482 | 0.196 | 0.367 | 0.339 | 12.9% | 25.6% | 27.5% |
| Mookie Betts | 217 | 0.223 | 0.394 | 0.171 | 0.316 | 0.330 | 8.4% | 24.6% | 12.5% |
| Will Smith | 212 | 0.245 | 0.375 | 0.130 | 0.319 | 0.386 | 13.6% | 22.3% | 15.1% |
| Alex Freeland | 205 | 0.227 | 0.330 | 0.102 | 0.300 | 0.298 | 7.3% | 26.3% | 26.4% |
| Dalton Rushing | 172 | 0.250 | 0.486 | 0.236 | 0.370 | 0.341 | 9.8% | 27.7% | 30.7% |
| Hyeseong Kim | 148 | 0.265 | 0.326 | 0.061 | 0.308 | 0.304 | 3.1% | 14.3% | 23.3% |
| Miguel Rojas | 147 | 0.292 | 0.415 | 0.123 | 0.353 | 0.328 | 6.7% | 29.0% | 16.3% |


## Minnesota Twins Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brooks Lee | 327 | 0.249 | 0.439 | 0.189 | 0.341 | 0.277 | 4.7% | 21.2% | 18.1% |
| Josh Bell | 327 | 0.236 | 0.377 | 0.141 | 0.307 | 0.324 | 9.3% | 22.4% | 22.4% |
| Luke Keaschall | 321 | 0.258 | 0.353 | 0.095 | 0.321 | 0.296 | 3.8% | 21.9% | 14.1% |
| Byron Buxton | 319 | 0.275 | 0.608 | 0.333 | 0.397 | 0.357 | 20.4% | 31.4% | 29.1% |
| Kody Clemens | 279 | 0.243 | 0.471 | 0.227 | 0.343 | 0.335 | 12.7% | 29.1% | 22.3% |
| Austin Martin | 259 | 0.257 | 0.335 | 0.078 | 0.336 | 0.310 | 2.3% | 18.3% | 18.3% |
| Trevor Larnach | 246 | 0.277 | 0.427 | 0.150 | 0.367 | 0.333 | 7.7% | 24.9% | 26.1% |
| Víctor Caratini | 234 | 0.234 | 0.386 | 0.152 | 0.321 | 0.346 | 8.9% | 24.4% | 20.3% |
| Royce Lewis | 211 | 0.198 | 0.348 | 0.150 | 0.288 | 0.307 | 13.3% | 25.3% | 29.3% |
| Ryan Jeffers | 166 | 0.298 | 0.532 | 0.234 | 0.417 | 0.389 | 15.4% | 27.0% | 15.8% |
| Tristan Gray | 166 | 0.229 | 0.333 | 0.105 | 0.264 | 0.284 | 6.7% | 25.7% | 30.2% |
| Matt Wallner | 151 | 0.194 | 0.343 | 0.149 | 0.288 | 0.281 | 11.5% | 24.1% | 39.3% |


## Bullpen Fatigue Report

### Los Angeles Dodgers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alex Vesia | 2026-06-20 | 1.0 | 20 |
| Brock Stewart | 2026-06-23 | 1.0 | 18 |
| Chayce McDermott | 2026-06-21 | 1.1 | 23 |
| Edgardo Henriquez | 2026-06-20 | 1.0 | 14 |
| Edgardo Henriquez | 2026-06-21 | 1.0 | 11 |
| Edgardo Henriquez | 2026-06-23 | 1.0 | 9 |
| Eric Lauer | 2026-06-22 | 6.0 | 84 |
| Jack Dreyer | 2026-06-21 | 0.2 | 23 |
| Jonathan Hernández | 2026-06-20 | 1.0 | 14 |
| Jonathan Hernández | 2026-06-21 | 1.2 | 37 |
| Kyle Hurt | 2026-06-22 | 1.0 | 11 |
| Miguel Rojas | 2026-06-21 | 1.0 | 7 |
| Tanner Scott | 2026-06-22 | 1.0 | 11 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Brock Stewart, Edgardo Henriquez


### Minnesota Twins Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Andrew Morris | 2026-06-21 | 1.0 | 17 |
| Andrew Morris | 2026-06-22 | 1.0 | 15 |
| Anthony Banda | 2026-06-20 | 1.0 | 12 |
| Anthony Banda | 2026-06-21 | 1.0 | 10 |
| Austin Voth | 2026-06-23 | 4.0 | 96 |
| Cody Laweryson | 2026-06-21 | 1.0 | 14 |
| Eric Orze | 2026-06-20 | 1.1 | 24 |
| Eric Orze | 2026-06-22 | 0.2 | 11 |
| Justin Lawrence | 2026-06-20 | 0.2 | 40 |
| Taylor Rogers | 2026-06-22 | 1.1 | 17 |
| Taylor Rogers | 2026-06-23 | 1.0 | 38 |
| Travis Adams | 2026-06-23 | 2.0 | 30 |
| Yoendrys Gómez | 2026-06-20 | 1.0 | 7 |
| Yoendrys Gómez | 2026-06-21 | 1.0 | 20 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Austin Voth, Taylor Rogers, Travis Adams



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Andy Pages | 359 | 0.266 | 0.465 | 0.199 | 0.344 | 8.0% | 26.6% |
| 2 | Freddie Freeman | 358 | 0.278 | 0.485 | 0.207 | 0.370 | 11.5% | 25.6% |
| 3 | Shohei Ohtani | 346 | 0.291 | 0.546 | 0.255 | 0.411 | 17.7% | 30.6% |
| 4 | Kyle Tucker | 337 | 0.234 | 0.379 | 0.145 | 0.327 | 5.8% | 24.3% |
| 5 | Max Muncy | 296 | 0.267 | 0.514 | 0.247 | 0.383 | 16.3% | 29.0% |
| 6 | Teoscar Hernández | 224 | 0.286 | 0.482 | 0.196 | 0.367 | 12.9% | 25.6% |
| 7 | Mookie Betts | 217 | 0.223 | 0.394 | 0.171 | 0.316 | 8.4% | 24.6% |
| 8 | Will Smith | 212 | 0.245 | 0.375 | 0.130 | 0.319 | 13.6% | 22.3% |
| 9 | Alex Freeland | 205 | 0.227 | 0.330 | 0.102 | 0.300 | 7.3% | 26.3% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Brooks Lee | 327 | 0.249 | 0.439 | 0.189 | 0.341 | 4.7% | 21.2% |
| 2 | Josh Bell | 327 | 0.236 | 0.377 | 0.141 | 0.307 | 9.3% | 22.4% |
| 3 | Luke Keaschall | 321 | 0.258 | 0.353 | 0.095 | 0.321 | 3.8% | 21.9% |
| 4 | Byron Buxton | 319 | 0.275 | 0.608 | 0.333 | 0.397 | 20.4% | 31.4% |
| 5 | Kody Clemens | 279 | 0.243 | 0.471 | 0.227 | 0.343 | 12.7% | 29.1% |
| 6 | Austin Martin | 259 | 0.257 | 0.335 | 0.078 | 0.336 | 2.3% | 18.3% |
| 7 | Trevor Larnach | 246 | 0.277 | 0.427 | 0.150 | 0.367 | 7.7% | 24.9% |
| 8 | Víctor Caratini | 234 | 0.234 | 0.386 | 0.152 | 0.321 | 8.9% | 24.4% |
| 9 | Royce Lewis | 211 | 0.198 | 0.348 | 0.150 | 0.288 | 13.3% | 25.3% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6776 |
| Hits Allowed | 1418 |
| Walks/HBP | 717 |
| Strikeouts | 1550 |
| Home Runs Allowed | 218 |
| K Event Rate | 22.9% |
| BB/HBP Event Rate | 10.6% |
| HR Event Rate | 3.2% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6899 |
| Hits Allowed | 1534 |
| Walks/HBP | 708 |
| Strikeouts | 1444 |
| Home Runs Allowed | 211 |
| K Event Rate | 20.9% |
| BB/HBP Event Rate | 10.3% |
| HR Event Rate | 3.1% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, ST, CU, FS
- Home pitcher pitch mix to inspect: FF, ST, SI, KC, FS
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 14. Arizona Diamondbacks @ St. Louis Cardinals

## Game Context

| Field | Value |
| --- | --- |
| Park | Busch Stadium |
| Time | 2026-06-24T23:45:00Z |
| Away Team | Arizona Diamondbacks |
| Home Team | St. Louis Cardinals |
| Away Probable Pitcher | Mitch Bratt |
| Home Probable Pitcher | Matthew Liberatore |


## Away Starting Pitcher: Mitch Bratt

### Pitcher Profile

| Stat | Value |
| --- | --- |
| No data | — |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — | — | — |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No data | — | — | — | — | — | — | — | — | — | — | — |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| No data | — | — | — | — | — |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No data | — | — | — | — | — | — | — | — | — | — |


## Home Starting Pitcher: Matthew Liberatore

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1282 |
| Batted/Result Events | 339 |
| Hits Allowed | 87 |
| Walks | 28 |
| Strikeouts | 72 |
| Home Runs | 15 |
| K Event Rate | 21.2% |
| BB Event Rate | 8.3% |
| HR Event Rate | 4.4% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-18 | KC | 4.3 | 7 | 1 | 0 | 2 | 1 |
| 2026-06-13 | MIN | 6.0 | 5 | 3 | 1 | 4 | 3 |
| 2026-06-06 | STL | 7.0 | 4 | 1 | 3 | 4 | 1 |
| 2026-05-31 | STL | 6.7 | 3 | 0 | 1 | 4 | 0 |
| 2026-05-25 | MIL | 8.0 | 7 | 1 | 2 | 10 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs R | 15.4% | 197 | 0.300 | 0.380 | 0.080 | 0.336 | 0.406 | 6.2% | 23.9% | 23.5% |
| CU | vs L | 1.9% | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.202 | 0.0% | 20.0% | 0.0% |
| CU | vs R | 14.4% | 185 | 0.200 | 0.500 | 0.300 | 0.316 | 0.258 | 21.4% | 32.3% | 36.8% |
| FC | vs L | 0.5% | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.026 | 0.0% | 0.0% | 25.0% |
| FC | vs R | 3.1% | 40 | 0.750 | 0.875 | 0.125 | 0.719 | 0.365 | 0.0% | 30.8% | 19.0% |
| FF | vs L | 7.0% | 90 | 0.294 | 0.529 | 0.235 | 0.460 | 0.554 | 14.3% | 28.1% | 7.7% |
| FF | vs R | 26.1% | 335 | 0.266 | 0.468 | 0.203 | 0.356 | 0.425 | 11.4% | 27.2% | 11.5% |
| FS | vs R | 0.7% | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.482 | 0.0% | 0.0% | 0.0% |
| SI | vs L | 4.8% | 62 | 0.353 | 0.529 | 0.176 | 0.432 | 0.278 | 0.0% | 39.3% | 2.9% |
| SI | vs R | 4.4% | 57 | 0.444 | 0.556 | 0.111 | 0.476 | 0.481 | 6.2% | 42.3% | 9.7% |
| SL | vs L | 11.3% | 145 | 0.300 | 0.675 | 0.375 | 0.420 | 0.324 | 20.0% | 34.1% | 39.2% |
| SL | vs R | 10.2% | 131 | 0.190 | 0.333 | 0.143 | 0.260 | 0.255 | 9.1% | 24.0% | 31.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-18 | 48 | 7 | 0 | 2 | 1 |
| 2026-06-13 | 70 | 5 | 1 | 4 | 3 |
| 2026-06-06 | 84 | 4 | 3 | 4 | 1 |
| 2026-05-31 | 85 | 3 | 1 | 4 | 0 |
| 2026-05-25 | 101 | 7 | 2 | 10 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | Alek Thomas | 11 | 0.364 | 0.909 | 0.545 | 0.523 | 0.281 | 12.5% | 22.2% | 25.9% |
| SI | Jorge Barrosa | 16 | 0.417 | 0.833 | 0.417 | 0.569 | 0.375 | 33.3% | 31.2% | 20.0% |
| CU | Ketel Marte | 23 | 0.300 | 0.700 | 0.400 | 0.452 | 0.501 | 11.1% | 37.9% | 22.0% |
| CH | Jorge Barrosa | 14 | 0.364 | 0.727 | 0.364 | 0.439 | 0.420 | 8.3% | 15.0% | 16.0% |
| SL | Corbin Carroll | 53 | 0.319 | 0.681 | 0.362 | 0.465 | 0.391 | 17.1% | 39.3% | 24.1% |
| SL | Ryan Waldschmidt | 19 | 0.471 | 0.824 | 0.353 | 0.563 | 0.296 | 8.3% | 41.2% | 35.5% |
| CH | Corbin Carroll | 40 | 0.189 | 0.541 | 0.351 | 0.328 | 0.344 | 9.4% | 31.9% | 24.3% |
| SI | Alek Thomas | 10 | 0.333 | 0.667 | 0.333 | 0.450 | 0.333 | 12.5% | 21.4% | 19.0% |
| SI | Ildemaro Vargas | 36 | 0.382 | 0.706 | 0.324 | 0.461 | 0.413 | 11.8% | 43.2% | 4.3% |
| SI | Ketel Marte | 46 | 0.429 | 0.738 | 0.310 | 0.515 | 0.504 | 18.9% | 40.7% | 3.0% |
| FF | Gabriel Moreno | 68 | 0.269 | 0.558 | 0.288 | 0.410 | 0.398 | 12.5% | 26.1% | 15.0% |
| FF | Corbin Carroll | 108 | 0.224 | 0.506 | 0.282 | 0.390 | 0.371 | 17.9% | 25.2% | 30.1% |
| SL | Alek Thomas | 17 | 0.200 | 0.467 | 0.267 | 0.297 | 0.374 | 18.2% | 23.5% | 38.2% |
| FF | Nolan Arenado | 83 | 0.270 | 0.527 | 0.257 | 0.367 | 0.383 | 10.8% | 25.0% | 12.5% |
| FF | Geraldo Perdomo | 116 | 0.300 | 0.533 | 0.233 | 0.423 | 0.377 | 3.7% | 22.6% | 9.3% |
| FF | Ketel Marte | 111 | 0.232 | 0.465 | 0.232 | 0.347 | 0.400 | 15.7% | 31.1% | 7.8% |
| CU | Corbin Carroll | 20 | 0.368 | 0.579 | 0.211 | 0.420 | 0.400 | 14.3% | 28.6% | 22.6% |
| CH | Lourdes Gurriel | 19 | 0.158 | 0.368 | 0.211 | 0.218 | 0.161 | 0.0% | 17.6% | 43.8% |
| SI | Gabriel Moreno | 39 | 0.382 | 0.588 | 0.206 | 0.477 | 0.394 | 6.2% | 26.7% | 1.4% |
| SI | Adrian Del Castillo | 30 | 0.240 | 0.440 | 0.200 | 0.387 | 0.393 | 13.6% | 23.1% | 12.5% |
| SI | Corbin Carroll | 44 | 0.450 | 0.650 | 0.200 | 0.495 | 0.372 | 9.1% | 35.7% | 23.2% |
| FF | Alek Thomas | 33 | 0.226 | 0.419 | 0.194 | 0.326 | 0.311 | 8.7% | 25.0% | 22.4% |
| CH | Gabriel Moreno | 23 | 0.227 | 0.409 | 0.182 | 0.289 | 0.333 | 16.7% | 31.4% | 14.6% |
| SI | Nolan Arenado | 53 | 0.356 | 0.533 | 0.178 | 0.423 | 0.336 | 9.5% | 33.8% | 11.7% |
| CH | Ildemaro Vargas | 44 | 0.268 | 0.439 | 0.171 | 0.355 | 0.325 | 2.6% | 34.0% | 16.2% |
| FF | Jorge Barrosa | 60 | 0.127 | 0.291 | 0.164 | 0.207 | 0.163 | 2.4% | 16.0% | 20.4% |
| FF | Adrian Del Castillo | 45 | 0.209 | 0.372 | 0.163 | 0.288 | 0.274 | 10.0% | 22.4% | 26.0% |
| SL | Ketel Marte | 38 | 0.243 | 0.405 | 0.162 | 0.289 | 0.385 | 9.7% | 42.3% | 21.7% |
| SL | Gabriel Moreno | 33 | 0.281 | 0.438 | 0.156 | 0.355 | 0.288 | 3.8% | 20.4% | 23.1% |
| FF | Ryan Waldschmidt | 29 | 0.231 | 0.385 | 0.154 | 0.362 | 0.358 | 17.6% | 17.9% | 20.8% |


## Arizona Diamondbacks Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ketel Marte | 340 | 0.262 | 0.450 | 0.188 | 0.339 | 0.369 | 10.7% | 34.5% | 18.6% |
| Corbin Carroll | 339 | 0.271 | 0.532 | 0.261 | 0.388 | 0.366 | 13.2% | 32.0% | 27.2% |
| Geraldo Perdomo | 333 | 0.236 | 0.343 | 0.107 | 0.326 | 0.332 | 2.5% | 22.1% | 10.7% |
| Nolan Arenado | 297 | 0.243 | 0.403 | 0.160 | 0.324 | 0.303 | 6.2% | 23.7% | 20.5% |
| Ildemaro Vargas | 277 | 0.263 | 0.417 | 0.154 | 0.331 | 0.311 | 3.9% | 26.7% | 12.2% |
| Gabriel Moreno | 216 | 0.280 | 0.478 | 0.199 | 0.378 | 0.366 | 10.7% | 27.1% | 16.1% |
| Jose Fernandez | 178 | 0.253 | 0.349 | 0.096 | 0.301 | 0.276 | 3.9% | 24.7% | 23.3% |
| Adrian Del Castillo | 150 | 0.190 | 0.307 | 0.117 | 0.263 | 0.264 | 6.5% | 21.0% | 25.0% |
| Jorge Barrosa | 140 | 0.211 | 0.431 | 0.220 | 0.313 | 0.211 | 8.0% | 17.6% | 24.9% |
| Ryan Waldschmidt | 131 | 0.273 | 0.380 | 0.107 | 0.327 | 0.289 | 7.6% | 22.1% | 29.0% |
| Lourdes Gurriel | 127 | 0.216 | 0.284 | 0.069 | 0.249 | 0.278 | 5.3% | 20.8% | 22.0% |
| Alek Thomas | 117 | 0.193 | 0.394 | 0.202 | 0.280 | 0.292 | 9.9% | 27.6% | 23.7% |


## St. Louis Cardinals Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Iván Herrera | 359 | 0.260 | 0.426 | 0.166 | 0.378 | 0.372 | 7.8% | 30.8% | 18.2% |
| Alec Burleson | 351 | 0.293 | 0.490 | 0.197 | 0.368 | 0.390 | 10.6% | 31.4% | 18.5% |
| Jj Wetherholt | 347 | 0.259 | 0.407 | 0.148 | 0.341 | 0.355 | 8.3% | 28.2% | 19.2% |
| Jordan Walker | 342 | 0.287 | 0.519 | 0.232 | 0.380 | 0.365 | 14.0% | 32.6% | 28.8% |
| Masyn Winn | 310 | 0.241 | 0.330 | 0.089 | 0.304 | 0.307 | 3.3% | 20.4% | 19.7% |
| Nolan Gorman | 242 | 0.194 | 0.313 | 0.118 | 0.269 | 0.278 | 8.8% | 28.0% | 37.5% |
| Nathan Church | 214 | 0.264 | 0.406 | 0.142 | 0.323 | 0.299 | 8.4% | 18.4% | 21.8% |
| Victor Scott | 200 | 0.196 | 0.262 | 0.065 | 0.264 | 0.273 | 0.8% | 15.6% | 24.2% |
| Pedro Pagés | 154 | 0.214 | 0.343 | 0.129 | 0.259 | 0.284 | 5.6% | 23.2% | 25.6% |
| José Fermín | 137 | 0.244 | 0.331 | 0.087 | 0.285 | 0.272 | 0.9% | 22.3% | 11.2% |
| Thomas Saggese | 92 | 0.198 | 0.314 | 0.116 | 0.251 | 0.274 | 10.5% | 22.6% | 28.6% |
| Ramón Urías | 77 | 0.156 | 0.344 | 0.188 | 0.294 | 0.306 | 9.8% | 23.7% | 22.3% |


## Bullpen Fatigue Report

### Arizona Diamondbacks Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brandyn Garcia | 2026-06-21 | 1.0 | 8 |
| Brandyn Garcia | 2026-06-23 | 0.1 | 4 |
| Ildemaro Vargas | 2026-06-20 | 1.2 | 20 |
| Jonathan Loáisiga | 2026-06-22 | 0.1 | 4 |
| Juan Morillo | 2026-06-21 | 1.0 | 22 |
| Juan Morillo | 2026-06-23 | 0.1 | 10 |
| Kevin Ginkel | 2026-06-21 | 1.0 | 25 |
| Kevin Ginkel | 2026-06-23 | 1.0 | 8 |
| Paul Sewald | 2026-06-23 | 0.2 | 23 |
| Philip Abner | 2026-06-20 | 2.2 | 44 |
| Ryan Thompson | 2026-06-21 | 1.0 | 16 |
| Taylor Clarke | 2026-06-22 | 1.2 | 27 |
| Yilber Díaz | 2026-06-20 | 0.2 | 44 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Brandyn Garcia, Juan Morillo, Kevin Ginkel, Paul Sewald


### St. Louis Cardinals Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| George Soriano | 2026-06-21 | 1.0 | 14 |
| George Soriano | 2026-06-22 | 0.1 | 5 |
| Gordon Graceffo | 2026-06-21 | 1.0 | 10 |
| Gordon Graceffo | 2026-06-23 | 0.2 | 22 |
| JoJo Romero | 2026-06-21 | 1.0 | 14 |
| JoJo Romero | 2026-06-22 | 1.0 | 9 |
| Matt Svanson | 2026-06-21 | 0.2 | 17 |
| Matt Svanson | 2026-06-23 | 0.1 | 36 |
| Max Rajcic | 2026-06-21 | 1.1 | 23 |
| Max Rajcic | 2026-06-23 | 1.2 | 24 |
| Riley O'Brien | 2026-06-21 | 1.0 | 12 |
| Riley O'Brien | 2026-06-22 | 1.0 | 17 |
| Ryne Stanek | 2026-06-21 | 1.0 | 11 |
| Ryne Stanek | 2026-06-22 | 0.2 | 11 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Gordon Graceffo, Matt Svanson, Max Rajcic



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Ketel Marte | 340 | 0.262 | 0.450 | 0.188 | 0.339 | 10.7% | 34.5% |
| 2 | Corbin Carroll | 339 | 0.271 | 0.532 | 0.261 | 0.388 | 13.2% | 32.0% |
| 3 | Geraldo Perdomo | 333 | 0.236 | 0.343 | 0.107 | 0.326 | 2.5% | 22.1% |
| 4 | Nolan Arenado | 297 | 0.243 | 0.403 | 0.160 | 0.324 | 6.2% | 23.7% |
| 5 | Ildemaro Vargas | 277 | 0.263 | 0.417 | 0.154 | 0.331 | 3.9% | 26.7% |
| 6 | Gabriel Moreno | 216 | 0.280 | 0.478 | 0.199 | 0.378 | 10.7% | 27.1% |
| 7 | Jose Fernandez | 178 | 0.253 | 0.349 | 0.096 | 0.301 | 3.9% | 24.7% |
| 8 | Adrian Del Castillo | 150 | 0.190 | 0.307 | 0.117 | 0.263 | 6.5% | 21.0% |
| 9 | Jorge Barrosa | 140 | 0.211 | 0.431 | 0.220 | 0.313 | 8.0% | 17.6% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Iván Herrera | 359 | 0.260 | 0.426 | 0.166 | 0.378 | 7.8% | 30.8% |
| 2 | Alec Burleson | 351 | 0.293 | 0.490 | 0.197 | 0.368 | 10.6% | 31.4% |
| 3 | Jj Wetherholt | 347 | 0.259 | 0.407 | 0.148 | 0.341 | 8.3% | 28.2% |
| 4 | Jordan Walker | 342 | 0.287 | 0.519 | 0.232 | 0.380 | 14.0% | 32.6% |
| 5 | Masyn Winn | 310 | 0.241 | 0.330 | 0.089 | 0.304 | 3.3% | 20.4% |
| 6 | Nolan Gorman | 242 | 0.194 | 0.313 | 0.118 | 0.269 | 8.8% | 28.0% |
| 7 | Nathan Church | 214 | 0.264 | 0.406 | 0.142 | 0.323 | 8.4% | 18.4% |
| 8 | Victor Scott | 200 | 0.196 | 0.262 | 0.065 | 0.264 | 0.8% | 15.6% |
| 9 | Pedro Pagés | 154 | 0.214 | 0.343 | 0.129 | 0.259 | 5.6% | 23.2% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6612 |
| Hits Allowed | 1455 |
| Walks/HBP | 612 |
| Strikeouts | 1282 |
| Home Runs Allowed | 190 |
| K Event Rate | 19.4% |
| BB/HBP Event Rate | 9.3% |
| HR Event Rate | 2.9% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6405 |
| Hits Allowed | 1406 |
| Walks/HBP | 640 |
| Strikeouts | 1292 |
| Home Runs Allowed | 186 |
| K Event Rate | 20.2% |
| BB/HBP Event Rate | 10.0% |
| HR Event Rate | 2.9% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: No current Statcast sample
- Home pitcher pitch mix to inspect: FF, SL, CU, CH, SI
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 15. Atlanta Braves @ San Diego Padres

## Game Context

| Field | Value |
| --- | --- |
| Park | Petco Park |
| Time | 2026-06-25T00:40:00Z |
| Away Team | Atlanta Braves |
| Home Team | San Diego Padres |
| Away Probable Pitcher | Martín Pérez |
| Home Probable Pitcher | JP Sears |


## Away Starting Pitcher: Martín Pérez

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1104 |
| Batted/Result Events | 289 |
| Hits Allowed | 56 |
| Walks | 24 |
| Strikeouts | 57 |
| Home Runs | 6 |
| K Event Rate | 19.7% |
| BB Event Rate | 8.3% |
| HR Event Rate | 2.1% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | ATL | 8.3 | 6 | 0 | 1 | 5 | 0 |
| 2026-06-13 | NYM | 6.7 | 4 | 0 | 1 | 4 | 0 |
| 2026-06-05 | ATL | 6.7 | 3 | 0 | 2 | 5 | 0 |
| 2026-05-30 | CIN | 6.7 | 4 | 1 | 3 | 2 | 1 |
| 2026-05-24 | ATL | 7.3 | 5 | 0 | 2 | 2 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 8.6% | 95 | 0.125 | 0.167 | 0.042 | 0.171 | 0.179 | 10.0% | 25.0% | 34.9% |
| CH | vs R | 23.7% | 262 | 0.141 | 0.268 | 0.127 | 0.217 | 0.295 | 6.6% | 14.4% | 27.4% |
| CU | vs L | 2.3% | 25 | 0.200 | 0.800 | 0.600 | 0.400 | 0.238 | 0.0% | 44.4% | 18.2% |
| CU | vs R | 6.5% | 72 | 0.286 | 0.429 | 0.143 | 0.307 | 0.320 | 0.0% | 13.3% | 33.3% |
| FC | vs L | 3.3% | 36 | 0.143 | 0.286 | 0.143 | 0.179 | 0.128 | 0.0% | 0.0% | 25.0% |
| FC | vs R | 18.3% | 202 | 0.264 | 0.528 | 0.264 | 0.361 | 0.324 | 7.5% | 34.3% | 16.5% |
| FF | vs L | 0.5% | 6 | 0.000 | 0.000 | 0.000 | 0.000 | — | 0.0% | 0.0% | 0.0% |
| FF | vs R | 6.0% | 66 | 0.308 | 0.385 | 0.077 | 0.332 | 0.237 | 0.0% | 38.9% | 13.6% |
| SI | vs L | 16.8% | 186 | 0.300 | 0.450 | 0.150 | 0.366 | 0.422 | 7.9% | 26.6% | 7.7% |
| SI | vs R | 13.8% | 152 | 0.243 | 0.270 | 0.027 | 0.324 | 0.333 | 6.9% | 38.1% | 8.5% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 84 | 6 | 2 | 5 | 0 |
| 2026-06-13 | 71 | 4 | 1 | 4 | 0 |
| 2026-06-05 | 85 | 3 | 2 | 5 | 0 |
| 2026-05-30 | 81 | 4 | 3 | 2 | 1 |
| 2026-05-24 | 86 | 5 | 2 | 2 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Freddy Fermin | 6 | 0.250 | 1.000 | 0.750 | 0.450 | 0.182 | 0.0% | 37.5% | 33.3% |
| FC | Rodolfo Durán | 5 | 0.200 | 0.800 | 0.600 | 0.400 | 0.194 | 33.3% | 20.0% | 28.6% |
| FC | Manny Machado | 16 | 0.429 | 1.000 | 0.571 | 0.563 | 0.498 | 20.0% | 41.4% | 15.8% |
| FC | Gavin Sheets | 22 | 0.300 | 0.800 | 0.500 | 0.475 | 0.423 | 22.2% | 34.2% | 11.8% |
| CU | Miguel Andújar | 9 | 0.444 | 0.889 | 0.444 | 0.561 | 0.439 | 14.3% | 41.7% | 20.0% |
| FC | Nick Castellanos | 8 | 0.286 | 0.714 | 0.429 | 0.450 | 0.450 | 40.0% | 33.3% | 40.9% |
| CH | Ramón Laureano | 25 | 0.261 | 0.652 | 0.391 | 0.404 | 0.298 | 18.8% | 14.8% | 37.3% |
| SI | Rodolfo Durán | 17 | 0.118 | 0.353 | 0.235 | 0.244 | 0.245 | 6.7% | 36.4% | 10.7% |
| CH | Ty France | 27 | 0.462 | 0.692 | 0.231 | 0.531 | 0.308 | 10.5% | 48.1% | 27.9% |
| FC | Ty France | 15 | 0.077 | 0.308 | 0.231 | 0.227 | 0.479 | 30.0% | 33.3% | 31.2% |
| FC | Ramón Laureano | 14 | 0.071 | 0.286 | 0.214 | 0.143 | 0.181 | 14.3% | 16.7% | 39.5% |
| CH | Gavin Sheets | 40 | 0.211 | 0.421 | 0.211 | 0.310 | 0.236 | 7.7% | 19.1% | 22.1% |
| SI | Ty France | 45 | 0.190 | 0.381 | 0.190 | 0.291 | 0.332 | 5.4% | 22.7% | 17.0% |
| FC | Xander Bogaerts | 21 | 0.250 | 0.438 | 0.188 | 0.390 | 0.452 | 8.3% | 23.5% | 22.7% |
| SI | Jackson Merrill | 51 | 0.400 | 0.578 | 0.178 | 0.474 | 0.444 | 8.3% | 27.1% | 9.5% |
| CH | Jackson Merrill | 43 | 0.225 | 0.400 | 0.175 | 0.305 | 0.311 | 9.4% | 27.6% | 27.3% |
| SI | Nick Castellanos | 27 | 0.250 | 0.417 | 0.167 | 0.306 | 0.375 | 4.8% | 23.7% | 21.0% |
| CU | Ty France | 12 | 0.250 | 0.417 | 0.167 | 0.283 | 0.152 | 0.0% | 35.7% | 22.7% |
| SI | Manny Machado | 69 | 0.177 | 0.339 | 0.161 | 0.263 | 0.352 | 8.9% | 28.3% | 14.5% |
| SI | Gavin Sheets | 42 | 0.231 | 0.385 | 0.154 | 0.294 | 0.359 | 6.5% | 37.5% | 11.6% |
| SI | Freddy Fermin | 41 | 0.189 | 0.324 | 0.135 | 0.266 | 0.293 | 3.0% | 25.4% | 10.3% |
| SI | Miguel Andújar | 55 | 0.358 | 0.491 | 0.132 | 0.385 | 0.355 | 3.8% | 28.9% | 4.2% |
| CH | Manny Machado | 40 | 0.143 | 0.257 | 0.114 | 0.264 | 0.221 | 3.8% | 17.4% | 25.0% |
| SI | Ramón Laureano | 55 | 0.289 | 0.400 | 0.111 | 0.347 | 0.343 | 7.5% | 29.2% | 16.7% |
| SI | Fernando Tatís | 94 | 0.317 | 0.427 | 0.110 | 0.379 | 0.397 | 9.2% | 40.4% | 14.6% |
| SI | Xander Bogaerts | 92 | 0.247 | 0.353 | 0.106 | 0.353 | 0.316 | 4.0% | 28.8% | 12.0% |
| CU | Jackson Merrill | 22 | 0.263 | 0.368 | 0.105 | 0.332 | 0.365 | 0.0% | 25.0% | 21.1% |
| CU | Jake Cronenworth | 11 | 0.100 | 0.200 | 0.100 | 0.177 | 0.300 | 33.3% | 50.0% | 50.0% |
| CU | Manny Machado | 15 | 0.077 | 0.154 | 0.077 | 0.177 | 0.243 | 0.0% | 11.8% | 24.0% |
| CH | Fernando Tatís | 31 | 0.276 | 0.345 | 0.069 | 0.277 | 0.257 | 11.1% | 34.4% | 39.0% |


## Home Starting Pitcher: JP Sears

### Pitcher Profile

| Stat | Value |
| --- | --- |
| No data | — |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — | — | — |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No data | — | — | — | — | — | — | — | — | — | — | — |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| No data | — | — | — | — | — |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No data | — | — | — | — | — | — | — | — | — | — |


## Atlanta Braves Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Matt Olson | 360 | 0.273 | 0.540 | 0.267 | 0.376 | 0.362 | 14.5% | 31.2% | 20.4% |
| Ozzie Albies | 353 | 0.273 | 0.435 | 0.162 | 0.338 | 0.308 | 4.0% | 21.6% | 18.1% |
| Austin Riley | 335 | 0.221 | 0.375 | 0.154 | 0.303 | 0.300 | 11.6% | 29.9% | 29.5% |
| Mauricio Dubón | 316 | 0.268 | 0.414 | 0.146 | 0.337 | 0.320 | 5.3% | 18.6% | 14.4% |
| Michael Harris | 294 | 0.297 | 0.495 | 0.197 | 0.361 | 0.386 | 15.5% | 35.4% | 23.6% |
| Drake Baldwin | 267 | 0.281 | 0.515 | 0.234 | 0.384 | 0.384 | 18.2% | 28.7% | 23.5% |
| Ronald Acuña | 244 | 0.254 | 0.428 | 0.174 | 0.359 | 0.378 | 12.8% | 25.3% | 26.3% |
| Mike Yastrzemski | 228 | 0.236 | 0.389 | 0.153 | 0.323 | 0.287 | 4.1% | 25.4% | 21.9% |
| Dominic Smith | 204 | 0.272 | 0.408 | 0.136 | 0.332 | 0.332 | 7.4% | 22.3% | 17.8% |
| Jorge Mateo | 128 | 0.280 | 0.441 | 0.161 | 0.350 | 0.334 | 9.4% | 25.1% | 27.1% |
| Eli White | 117 | 0.255 | 0.453 | 0.198 | 0.356 | 0.292 | 8.4% | 22.1% | 23.9% |
| Ha-Seong Kim | 69 | 0.081 | 0.081 | 0.000 | 0.136 | 0.204 | 2.4% | 14.6% | 18.0% |


## San Diego Padres Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fernando Tatís | 344 | 0.284 | 0.370 | 0.086 | 0.333 | 0.354 | 10.5% | 35.9% | 26.3% |
| Jackson Merrill | 335 | 0.209 | 0.350 | 0.141 | 0.278 | 0.315 | 9.7% | 24.9% | 24.7% |
| Manny Machado | 329 | 0.179 | 0.369 | 0.190 | 0.286 | 0.309 | 9.0% | 24.8% | 23.8% |
| Xander Bogaerts | 310 | 0.229 | 0.347 | 0.118 | 0.324 | 0.318 | 7.0% | 25.7% | 20.6% |
| Gavin Sheets | 274 | 0.233 | 0.469 | 0.237 | 0.341 | 0.324 | 9.3% | 31.1% | 18.1% |
| Ramón Laureano | 224 | 0.209 | 0.383 | 0.173 | 0.301 | 0.312 | 13.4% | 23.3% | 30.5% |
| Miguel Andújar | 219 | 0.236 | 0.385 | 0.149 | 0.286 | 0.282 | 4.1% | 21.5% | 18.1% |
| Ty France | 192 | 0.240 | 0.464 | 0.223 | 0.331 | 0.305 | 11.5% | 25.5% | 25.6% |
| Freddy Fermin | 157 | 0.162 | 0.265 | 0.103 | 0.253 | 0.266 | 2.8% | 16.4% | 22.8% |
| Nick Castellanos | 137 | 0.178 | 0.333 | 0.155 | 0.246 | 0.285 | 7.5% | 20.4% | 30.8% |
| Jake Cronenworth | 132 | 0.162 | 0.216 | 0.054 | 0.257 | 0.304 | 4.7% | 21.2% | 21.2% |
| Rodolfo Durán | 74 | 0.154 | 0.431 | 0.277 | 0.307 | 0.295 | 13.3% | 23.2% | 25.0% |


## Bullpen Fatigue Report

### Atlanta Braves Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Carlos Carrasco | 2026-06-23 | 1.2 | 30 |
| Didier Fuentes | 2026-06-20 | 1.1 | 28 |
| Didier Fuentes | 2026-06-22 | 0.1 | 4 |
| Dylan Dodd | 2026-06-22 | 1.1 | 39 |
| Dylan Lee | 2026-06-20 | 1.0 | 11 |
| Dylan Lee | 2026-06-23 | 1.1 | 17 |
| James Karinchak | 2026-06-20 | 1.0 | 10 |
| James Karinchak | 2026-06-22 | 1.2 | 22 |
| Raisel Iglesias | 2026-06-23 | 1.0 | 19 |
| Reynaldo López | 2026-06-21 | 3.0 | 58 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Carlos Carrasco, Dylan Lee, Raisel Iglesias


### San Diego Padres Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Adrian Morejon | 2026-06-20 | 2.0 | 35 |
| Adrian Morejon | 2026-06-22 | 1.0 | 12 |
| Adrian Morejon | 2026-06-23 | 1.0 | 10 |
| David Morgan | 2026-06-23 | 1.0 | 15 |
| Griffin Canning | 2026-06-23 | 0.2 | 40 |
| Jason Adam | 2026-06-20 | 1.0 | 28 |
| Kyle Hart | 2026-06-20 | 0.2 | 10 |
| Kyle Hart | 2026-06-21 | 1.0 | 11 |
| Kyle Hart | 2026-06-23 | 2.0 | 45 |
| Lucas Giolito | 2026-06-21 | 4.0 | 66 |
| Mason Miller | 2026-06-20 | 1.0 | 21 |
| Mason Miller | 2026-06-22 | 1.0 | 20 |
| Mason Miller | 2026-06-23 | 2.0 | 22 |
| Ron Marinaccio | 2026-06-21 | 1.0 | 15 |
| Yuki Matsui | 2026-06-21 | 1.0 | 17 |
| Yuki Matsui | 2026-06-23 | 2.1 | 35 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Adrian Morejon, David Morgan, Griffin Canning, Kyle Hart, Mason Miller, Yuki Matsui



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Olson | 360 | 0.273 | 0.540 | 0.267 | 0.376 | 14.5% | 31.2% |
| 2 | Ozzie Albies | 353 | 0.273 | 0.435 | 0.162 | 0.338 | 4.0% | 21.6% |
| 3 | Austin Riley | 335 | 0.221 | 0.375 | 0.154 | 0.303 | 11.6% | 29.9% |
| 4 | Mauricio Dubón | 316 | 0.268 | 0.414 | 0.146 | 0.337 | 5.3% | 18.6% |
| 5 | Michael Harris | 294 | 0.297 | 0.495 | 0.197 | 0.361 | 15.5% | 35.4% |
| 6 | Drake Baldwin | 267 | 0.281 | 0.515 | 0.234 | 0.384 | 18.2% | 28.7% |
| 7 | Ronald Acuña | 244 | 0.254 | 0.428 | 0.174 | 0.359 | 12.8% | 25.3% |
| 8 | Mike Yastrzemski | 228 | 0.236 | 0.389 | 0.153 | 0.323 | 4.1% | 25.4% |
| 9 | Dominic Smith | 204 | 0.272 | 0.408 | 0.136 | 0.332 | 7.4% | 22.3% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Fernando Tatís | 344 | 0.284 | 0.370 | 0.086 | 0.333 | 10.5% | 35.9% |
| 2 | Jackson Merrill | 335 | 0.209 | 0.350 | 0.141 | 0.278 | 9.7% | 24.9% |
| 3 | Manny Machado | 329 | 0.179 | 0.369 | 0.190 | 0.286 | 9.0% | 24.8% |
| 4 | Xander Bogaerts | 310 | 0.229 | 0.347 | 0.118 | 0.324 | 7.0% | 25.7% |
| 5 | Gavin Sheets | 274 | 0.233 | 0.469 | 0.237 | 0.341 | 9.3% | 31.1% |
| 6 | Ramón Laureano | 224 | 0.209 | 0.383 | 0.173 | 0.301 | 13.4% | 23.3% |
| 7 | Miguel Andújar | 219 | 0.236 | 0.385 | 0.149 | 0.286 | 4.1% | 21.5% |
| 8 | Ty France | 192 | 0.240 | 0.464 | 0.223 | 0.331 | 11.5% | 25.5% |
| 9 | Freddy Fermin | 157 | 0.162 | 0.265 | 0.103 | 0.253 | 2.8% | 16.4% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6489 |
| Hits Allowed | 1385 |
| Walks/HBP | 593 |
| Strikeouts | 1438 |
| Home Runs Allowed | 198 |
| K Event Rate | 22.2% |
| BB/HBP Event Rate | 9.1% |
| HR Event Rate | 3.1% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6469 |
| Hits Allowed | 1337 |
| Walks/HBP | 641 |
| Strikeouts | 1472 |
| Home Runs Allowed | 185 |
| K Event Rate | 22.8% |
| BB/HBP Event Rate | 9.9% |
| HR Event Rate | 2.9% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: CH, SI, FC, CU
- Home pitcher pitch mix to inspect: No current Statcast sample
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 16. Athletics @ San Francisco Giants

## Game Context

| Field | Value |
| --- | --- |
| Park | Oracle Park |
| Time | 2026-06-25T01:45:00Z |
| Away Team | Athletics |
| Home Team | San Francisco Giants |
| Away Probable Pitcher | Gage Jump |
| Home Probable Pitcher | Tyler Mahle |


## Away Starting Pitcher: Gage Jump

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 451 |
| Batted/Result Events | 120 |
| Hits Allowed | 21 |
| Walks | 9 |
| Strikeouts | 26 |
| Home Runs | 0 |
| K Event Rate | 21.7% |
| BB Event Rate | 7.5% |
| HR Event Rate | 0.0% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-18 | ATH | 8.3 | 1 | 0 | 3 | 7 | 0 |
| 2026-06-12 | ATH | 7.0 | 5 | 0 | 1 | 6 | 0 |
| 2026-06-07 | HOU | 8.0 | 3 | 0 | 3 | 3 | 0 |
| 2026-06-02 | CHC | 8.3 | 3 | 0 | 2 | 5 | 0 |
| 2026-05-26 | ATH | 8.3 | 9 | 0 | 2 | 5 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs R | 8.9% | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.165 | 0.0% | 0.0% | 41.7% |
| CU | vs L | 1.1% | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.199 | 0.0% | 33.3% | 20.0% |
| CU | vs R | 11.1% | 50 | 0.077 | 0.077 | 0.000 | 0.179 | 0.187 | 0.0% | 18.2% | 31.8% |
| FF | vs L | 8.0% | 36 | 0.400 | 0.400 | 0.000 | 0.457 | 0.316 | 0.0% | 0.0% | 12.5% |
| FF | vs R | 40.6% | 183 | 0.209 | 0.233 | 0.023 | 0.229 | 0.270 | 2.9% | 14.8% | 20.2% |
| SL | vs L | 5.5% | 25 | 0.333 | 0.333 | 0.000 | 0.312 | 0.503 | 14.3% | 40.0% | 21.4% |
| SL | vs R | 19.1% | 86 | 0.136 | 0.182 | 0.045 | 0.225 | 0.307 | 0.0% | 21.4% | 22.5% |
| ST | vs L | 3.8% | 17 | 0.286 | 0.286 | 0.000 | 0.225 | 0.133 | 0.0% | 0.0% | 27.3% |
| ST | vs R | 2.0% | 9 | 0.500 | 0.750 | 0.250 | 0.537 | 0.368 | 0.0% | 66.7% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-18 | 107 | 1 | 3 | 7 | 0 |
| 2026-06-12 | 75 | 5 | 1 | 6 | 0 |
| 2026-06-07 | 96 | 3 | 3 | 3 | 0 |
| 2026-06-02 | 85 | 3 | 1 | 5 | 0 |
| 2026-05-26 | 88 | 9 | 1 | 5 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | Casey Schmitt | 20 | 0.450 | 1.100 | 0.650 | 0.643 | 0.549 | 25.0% | 33.3% | 26.2% |
| CU | Matt Chapman | 14 | 0.357 | 1.000 | 0.643 | 0.554 | 0.455 | 16.7% | 26.1% | 14.8% |
| SL | Heliot Ramos | 20 | 0.450 | 0.900 | 0.450 | 0.568 | 0.417 | 12.5% | 28.6% | 31.1% |
| FF | Bryce Eldridge | 50 | 0.300 | 0.725 | 0.425 | 0.480 | 0.510 | 28.1% | 32.0% | 12.0% |
| FF | Willy Adames | 94 | 0.225 | 0.573 | 0.348 | 0.348 | 0.333 | 12.1% | 26.7% | 21.1% |
| SL | Harrison Bader | 20 | 0.250 | 0.550 | 0.300 | 0.333 | 0.346 | 16.7% | 37.5% | 48.5% |
| SL | Bryce Eldridge | 18 | 0.412 | 0.706 | 0.294 | 0.489 | 0.208 | 0.0% | 31.8% | 25.0% |
| FF | Drew Gilbert | 65 | 0.302 | 0.528 | 0.226 | 0.415 | 0.346 | 2.3% | 22.7% | 16.5% |
| FF | Rafael Devers | 132 | 0.192 | 0.400 | 0.208 | 0.289 | 0.280 | 14.3% | 27.9% | 36.7% |
| FF | Jung Hoo Lee | 100 | 0.402 | 0.609 | 0.207 | 0.450 | 0.348 | 4.7% | 22.2% | 7.2% |
| FF | Harrison Bader | 34 | 0.133 | 0.333 | 0.200 | 0.253 | 0.254 | 4.5% | 21.6% | 20.0% |
| SL | Rafael Devers | 35 | 0.242 | 0.424 | 0.182 | 0.287 | 0.300 | 7.7% | 29.3% | 34.3% |
| FF | Heliot Ramos | 41 | 0.256 | 0.436 | 0.179 | 0.337 | 0.320 | 13.0% | 14.5% | 25.0% |
| SL | Matt Chapman | 47 | 0.190 | 0.357 | 0.167 | 0.281 | 0.288 | 12.5% | 30.0% | 30.4% |
| CU | Casey Schmitt | 13 | 0.167 | 0.333 | 0.167 | 0.246 | 0.281 | 0.0% | 5.3% | 36.7% |
| CU | Luis Arráez | 19 | 0.474 | 0.632 | 0.158 | 0.482 | 0.305 | 0.0% | 8.3% | 0.0% |
| CH | Matt Chapman | 30 | 0.269 | 0.423 | 0.154 | 0.350 | 0.348 | 11.8% | 34.4% | 22.9% |
| CH | Luis Arráez | 36 | 0.152 | 0.303 | 0.152 | 0.194 | 0.239 | 2.9% | 14.5% | 4.9% |
| CU | Jung Hoo Lee | 21 | 0.286 | 0.429 | 0.143 | 0.307 | 0.278 | 0.0% | 26.7% | 10.0% |
| SL | Patrick Bailey | 22 | 0.318 | 0.455 | 0.136 | 0.336 | 0.245 | 7.1% | 23.3% | 32.7% |
| CH | Drew Gilbert | 23 | 0.227 | 0.364 | 0.136 | 0.311 | 0.273 | 0.0% | 19.2% | 25.6% |
| FF | Luis Arráez | 129 | 0.355 | 0.488 | 0.132 | 0.374 | 0.315 | 0.0% | 14.9% | 8.7% |
| SL | Willy Adames | 49 | 0.130 | 0.261 | 0.130 | 0.215 | 0.170 | 13.0% | 21.7% | 41.9% |
| FF | Daniel Susac | 26 | 0.200 | 0.320 | 0.120 | 0.221 | 0.214 | 5.3% | 16.3% | 13.3% |
| SL | Daniel Susac | 21 | 0.389 | 0.500 | 0.111 | 0.400 | 0.345 | 6.2% | 16.7% | 28.3% |
| FF | Casey Schmitt | 88 | 0.265 | 0.373 | 0.108 | 0.302 | 0.340 | 11.4% | 25.8% | 16.0% |
| CH | Rafael Devers | 37 | 0.216 | 0.324 | 0.108 | 0.232 | 0.349 | 12.5% | 36.5% | 16.4% |
| CH | Bryce Eldridge | 21 | 0.250 | 0.350 | 0.100 | 0.281 | 0.374 | 14.3% | 19.0% | 36.1% |
| CH | Harrison Bader | 10 | 0.300 | 0.400 | 0.100 | 0.305 | 0.290 | 20.0% | 23.1% | 34.8% |
| CH | Daniel Susac | 10 | 0.300 | 0.400 | 0.100 | 0.305 | 0.214 | 0.0% | 16.7% | 36.7% |


## Home Starting Pitcher: Tyler Mahle

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1021 |
| Batted/Result Events | 264 |
| Hits Allowed | 64 |
| Walks | 24 |
| Strikeouts | 63 |
| Home Runs | 11 |
| K Event Rate | 23.9% |
| BB Event Rate | 9.1% |
| HR Event Rate | 4.2% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-26 | SF | 6.7 | 3 | 1 | 3 | 3 | 1 |
| 2026-05-20 | AZ | 7.7 | 8 | 1 | 0 | 6 | 1 |
| 2026-05-15 | ATH | 8.3 | 10 | 1 | 1 | 6 | 1 |
| 2026-05-10 | SF | 8.0 | 5 | 2 | 2 | 8 | 2 |
| 2026-05-03 | TB | 7.3 | 4 | 0 | 1 | 5 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | vs L | 8.5% | 87 | 0.278 | 0.500 | 0.222 | 0.343 | 0.280 | 6.7% | 33.3% | 13.3% |
| FC | vs R | 6.8% | 69 | 0.368 | 0.526 | 0.158 | 0.405 | 0.383 | 5.6% | 18.8% | 5.4% |
| FF | vs L | 26.3% | 269 | 0.204 | 0.408 | 0.204 | 0.298 | 0.297 | 13.3% | 17.9% | 16.8% |
| FF | vs R | 21.3% | 217 | 0.310 | 0.548 | 0.238 | 0.407 | 0.350 | 12.1% | 25.4% | 13.8% |
| FS | vs L | 16.4% | 167 | 0.222 | 0.389 | 0.167 | 0.271 | 0.211 | 2.4% | 15.9% | 21.4% |
| FS | vs R | 8.4% | 86 | 0.333 | 0.524 | 0.190 | 0.398 | 0.420 | 15.4% | 28.6% | 34.8% |
| SI | vs R | 1.7% | 17 | 1.000 | 1.000 | 0.000 | 0.900 | 0.259 | 0.0% | 25.0% | 14.3% |
| SL | vs L | 0.8% | 8 | 0.500 | 1.000 | 0.500 | 0.625 | 0.507 | 0.0% | 20.0% | 0.0% |
| SL | vs R | 9.8% | 100 | 0.286 | 0.429 | 0.143 | 0.414 | 0.401 | 9.5% | 33.3% | 26.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-05-26 | 82 | 3 | 3 | 3 | 1 |
| 2026-05-20 | 79 | 8 | 0 | 6 | 1 |
| 2026-05-15 | 90 | 10 | 1 | 6 | 1 |
| 2026-05-10 | 97 | 5 | 2 | 8 | 2 |
| 2026-05-03 | 92 | 4 | 1 | 5 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FS | Shea Langeliers | 8 | 0.375 | 1.125 | 0.750 | 0.613 | 0.244 | 16.7% | 33.3% | 33.3% |
| FC | Carlos Cortes | 11 | 0.333 | 1.000 | 0.667 | 0.509 | 0.627 | 20.0% | 27.8% | 20.0% |
| FC | Zack Gelof | 12 | 0.500 | 1.100 | 0.600 | 0.633 | 0.560 | 18.2% | 22.2% | 26.7% |
| FC | Max Muncy | 30 | 0.296 | 0.778 | 0.481 | 0.468 | 0.445 | 17.4% | 29.2% | 17.5% |
| FS | Zack Gelof | 8 | 0.429 | 0.857 | 0.429 | 0.562 | 0.360 | 25.0% | 42.9% | 43.8% |
| SL | Lawrence Butler | 17 | 0.286 | 0.714 | 0.429 | 0.465 | 0.514 | 25.0% | 33.3% | 23.3% |
| FF | Shea Langeliers | 77 | 0.250 | 0.676 | 0.426 | 0.421 | 0.417 | 22.9% | 23.8% | 21.2% |
| FF | Nick Kurtz | 107 | 0.268 | 0.659 | 0.390 | 0.457 | 0.477 | 29.2% | 34.1% | 31.0% |
| FF | Brent Rooker | 58 | 0.184 | 0.571 | 0.388 | 0.356 | 0.355 | 29.6% | 26.3% | 29.3% |
| FC | Brent Rooker | 8 | 0.500 | 0.875 | 0.375 | 0.588 | 0.398 | 28.6% | 33.3% | 23.8% |
| SL | Nick Kurtz | 51 | 0.256 | 0.628 | 0.372 | 0.418 | 0.357 | 24.0% | 37.0% | 40.5% |
| FF | Max Muncy | 129 | 0.346 | 0.701 | 0.355 | 0.484 | 0.462 | 22.5% | 33.7% | 18.7% |
| FC | Jacob Wilson | 12 | 0.250 | 0.583 | 0.333 | 0.346 | 0.261 | 10.0% | 26.7% | 30.8% |
| FF | Zack Gelof | 68 | 0.226 | 0.516 | 0.290 | 0.356 | 0.279 | 10.3% | 27.2% | 27.6% |
| SL | Tyler Soderstrom | 46 | 0.179 | 0.462 | 0.282 | 0.349 | 0.347 | 23.1% | 25.0% | 40.2% |
| FC | Tyler Soderstrom | 27 | 0.280 | 0.560 | 0.280 | 0.380 | 0.382 | 5.0% | 44.8% | 11.1% |
| SL | Max Muncy | 69 | 0.241 | 0.500 | 0.259 | 0.363 | 0.346 | 20.0% | 35.7% | 40.0% |
| FS | Nick Kurtz | 22 | 0.250 | 0.500 | 0.250 | 0.350 | 0.296 | 22.2% | 43.8% | 52.6% |
| FS | Jacob Wilson | 4 | 0.250 | 0.500 | 0.250 | 0.312 | 0.113 | 0.0% | 33.3% | 25.0% |
| FF | Henry Bolte | 25 | 0.348 | 0.565 | 0.217 | 0.416 | 0.324 | 21.4% | 26.7% | 32.7% |
| FC | Lawrence Butler | 24 | 0.211 | 0.421 | 0.211 | 0.356 | 0.402 | 13.3% | 24.1% | 23.8% |
| FF | Tyler Soderstrom | 96 | 0.237 | 0.434 | 0.197 | 0.371 | 0.379 | 12.1% | 24.6% | 16.1% |
| FS | Carlos Cortes | 16 | 0.188 | 0.375 | 0.188 | 0.237 | 0.392 | 14.3% | 29.2% | 13.8% |
| FC | Nick Kurtz | 23 | 0.250 | 0.438 | 0.188 | 0.417 | 0.517 | 25.0% | 18.8% | 33.3% |
| SL | Zack Gelof | 33 | 0.182 | 0.364 | 0.182 | 0.230 | 0.254 | 3.4% | 30.0% | 14.6% |
| FC | Shea Langeliers | 25 | 0.304 | 0.478 | 0.174 | 0.366 | 0.393 | 15.0% | 24.3% | 28.8% |
| FS | Tyler Soderstrom | 14 | 0.167 | 0.333 | 0.167 | 0.279 | 0.258 | 0.0% | 20.0% | 25.7% |
| SL | Brent Rooker | 31 | 0.290 | 0.452 | 0.161 | 0.377 | 0.210 | 9.5% | 14.7% | 51.4% |
| SL | Carlos Cortes | 22 | 0.316 | 0.474 | 0.158 | 0.391 | 0.394 | 7.7% | 37.0% | 33.3% |
| FF | Lawrence Butler | 69 | 0.177 | 0.323 | 0.145 | 0.275 | 0.323 | 7.5% | 25.7% | 26.5% |


## Athletics Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nick Kurtz | 375 | 0.284 | 0.538 | 0.254 | 0.415 | 0.391 | 18.4% | 33.0% | 32.1% |
| Shea Langeliers | 338 | 0.269 | 0.521 | 0.252 | 0.369 | 0.369 | 14.5% | 28.1% | 24.0% |
| Tyler Soderstrom | 334 | 0.243 | 0.476 | 0.233 | 0.365 | 0.337 | 10.6% | 28.8% | 20.3% |
| Jeff Mcneil | 265 | 0.224 | 0.304 | 0.080 | 0.278 | 0.302 | 1.0% | 18.3% | 15.2% |
| Zack Gelof | 238 | 0.276 | 0.484 | 0.207 | 0.368 | 0.299 | 6.8% | 27.6% | 25.1% |
| Lawrence Butler | 226 | 0.197 | 0.315 | 0.118 | 0.280 | 0.307 | 7.3% | 26.4% | 26.7% |
| Jacob Wilson | 224 | 0.274 | 0.377 | 0.104 | 0.312 | 0.278 | 1.6% | 20.6% | 13.0% |
| Carlos Cortes | 217 | 0.260 | 0.411 | 0.151 | 0.333 | 0.356 | 8.0% | 24.0% | 19.0% |
| Brent Rooker | 215 | 0.214 | 0.411 | 0.198 | 0.316 | 0.315 | 16.5% | 26.9% | 35.2% |
| Max Muncy | 156 | 0.230 | 0.439 | 0.209 | 0.326 | 0.297 | 13.0% | 33.9% | 30.4% |
| Darell Hernaiz | 145 | 0.248 | 0.302 | 0.054 | 0.292 | 0.263 | 1.0% | 13.7% | 19.9% |
| Henry Bolte | 141 | 0.298 | 0.397 | 0.099 | 0.350 | 0.305 | 6.2% | 30.9% | 32.9% |


## San Francisco Giants Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rafael Devers | 340 | 0.242 | 0.432 | 0.190 | 0.317 | 0.302 | 10.4% | 28.0% | 27.9% |
| Luis Arráez | 338 | 0.321 | 0.443 | 0.121 | 0.351 | 0.303 | 0.3% | 13.2% | 7.2% |
| Matt Chapman | 337 | 0.251 | 0.407 | 0.156 | 0.337 | 0.291 | 7.7% | 23.9% | 20.3% |
| Willy Adames | 335 | 0.226 | 0.424 | 0.197 | 0.308 | 0.291 | 9.4% | 24.9% | 26.6% |
| Casey Schmitt | 311 | 0.298 | 0.521 | 0.223 | 0.364 | 0.364 | 12.4% | 28.5% | 20.5% |
| Jung Hoo Lee | 297 | 0.337 | 0.486 | 0.149 | 0.377 | 0.334 | 3.2% | 20.7% | 10.7% |
| Drew Gilbert | 197 | 0.243 | 0.376 | 0.133 | 0.320 | 0.285 | 2.2% | 21.7% | 20.1% |
| Heliot Ramos | 188 | 0.261 | 0.420 | 0.159 | 0.319 | 0.326 | 12.8% | 24.5% | 24.4% |
| Bryce Eldridge | 156 | 0.286 | 0.489 | 0.203 | 0.379 | 0.376 | 12.2% | 28.2% | 21.2% |
| Daniel Susac | 126 | 0.274 | 0.363 | 0.088 | 0.297 | 0.290 | 5.6% | 17.4% | 23.1% |
| Harrison Bader | 114 | 0.167 | 0.352 | 0.185 | 0.244 | 0.272 | 8.2% | 25.0% | 30.6% |
| Patrick Bailey | 102 | 0.160 | 0.191 | 0.032 | 0.198 | 0.283 | 4.3% | 25.6% | 24.6% |


## Bullpen Fatigue Report

### Athletics Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Elvis Alvarado | 2026-06-21 | 1.2 | 21 |
| Geoff Hartlieb | 2026-06-20 | 3.0 | 43 |
| Hogan Harris | 2026-06-21 | 0.1 | 18 |
| José Suarez | 2026-06-23 | 1.2 | 25 |
| Luis Medina | 2026-06-21 | 1.0 | 15 |
| Mason Barnett | 2026-06-23 | 1.0 | 25 |
| Matt Krook | 2026-06-21 | 1.0 | 18 |
| Matt Krook | 2026-06-23 | 1.1 | 25 |
| Scott Barlow | 2026-06-20 | 0.2 | 24 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** José Suarez, Mason Barnett, Matt Krook


### San Francisco Giants Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Caleb Kilian | 2026-06-23 | 1.0 | 18 |
| JT Brubaker | 2026-06-20 | 2.1 | 35 |
| Matt Gage | 2026-06-20 | 0.2 | 28 |
| Tristan Beck | 2026-06-20 | 2.0 | 18 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Caleb Kilian



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nick Kurtz | 375 | 0.284 | 0.538 | 0.254 | 0.415 | 18.4% | 33.0% |
| 2 | Shea Langeliers | 338 | 0.269 | 0.521 | 0.252 | 0.369 | 14.5% | 28.1% |
| 3 | Tyler Soderstrom | 334 | 0.243 | 0.476 | 0.233 | 0.365 | 10.6% | 28.8% |
| 4 | Jeff Mcneil | 265 | 0.224 | 0.304 | 0.080 | 0.278 | 1.0% | 18.3% |
| 5 | Zack Gelof | 238 | 0.276 | 0.484 | 0.207 | 0.368 | 6.8% | 27.6% |
| 6 | Lawrence Butler | 226 | 0.197 | 0.315 | 0.118 | 0.280 | 7.3% | 26.4% |
| 7 | Jacob Wilson | 224 | 0.274 | 0.377 | 0.104 | 0.312 | 1.6% | 20.6% |
| 8 | Carlos Cortes | 217 | 0.260 | 0.411 | 0.151 | 0.333 | 8.0% | 24.0% |
| 9 | Brent Rooker | 215 | 0.214 | 0.411 | 0.198 | 0.316 | 16.5% | 26.9% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Rafael Devers | 340 | 0.242 | 0.432 | 0.190 | 0.317 | 10.4% | 28.0% |
| 2 | Luis Arráez | 338 | 0.321 | 0.443 | 0.121 | 0.351 | 0.3% | 13.2% |
| 3 | Matt Chapman | 337 | 0.251 | 0.407 | 0.156 | 0.337 | 7.7% | 23.9% |
| 4 | Willy Adames | 335 | 0.226 | 0.424 | 0.197 | 0.308 | 9.4% | 24.9% |
| 5 | Casey Schmitt | 311 | 0.298 | 0.521 | 0.223 | 0.364 | 12.4% | 28.5% |
| 6 | Jung Hoo Lee | 297 | 0.337 | 0.486 | 0.149 | 0.377 | 3.2% | 20.7% |
| 7 | Drew Gilbert | 197 | 0.243 | 0.376 | 0.133 | 0.320 | 2.2% | 21.7% |
| 8 | Heliot Ramos | 188 | 0.261 | 0.420 | 0.159 | 0.319 | 12.8% | 24.5% |
| 9 | Bryce Eldridge | 156 | 0.286 | 0.489 | 0.203 | 0.379 | 12.2% | 28.2% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6803 |
| Hits Allowed | 1532 |
| Walks/HBP | 716 |
| Strikeouts | 1478 |
| Home Runs Allowed | 246 |
| K Event Rate | 21.7% |
| BB/HBP Event Rate | 10.5% |
| HR Event Rate | 3.6% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6440 |
| Hits Allowed | 1461 |
| Walks/HBP | 578 |
| Strikeouts | 1324 |
| Home Runs Allowed | 180 |
| K Event Rate | 20.6% |
| BB/HBP Event Rate | 9.0% |
| HR Event Rate | 2.8% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL, CU, CH
- Home pitcher pitch mix to inspect: FF, FS, FC, SL
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.

