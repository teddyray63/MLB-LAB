# MLB-LAB V5.1 Pitch Matchup Engine

Date: 2026-06-28

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
| 1 | Washington Nationals @ Baltimore Orioles | Oriole Park at Camden Yards | Zack Littell | Kyle Bradish |
| 2 | Cincinnati Reds @ Pittsburgh Pirates | PNC Park | Brady Singer | Mitch Keller |
| 3 | Texas Rangers @ Toronto Blue Jays | Rogers Centre | Kumar Rocker | Shane Bieber |
| 4 | Houston Astros @ Detroit Tigers | Comerica Park | Hunter Brown | Jack Flaherty |
| 5 | Seattle Mariners @ Cleveland Guardians | Progressive Field | Emerson Hancock | Gavin Williams |
| 6 | Arizona Diamondbacks @ Tampa Bay Rays | Tropicana Field | Merrill Kelly | Drew Rasmussen |
| 7 | Philadelphia Phillies @ New York Mets | Citi Field | Jesús Luzardo | Cionel Pérez |
| 8 | Colorado Rockies @ Minnesota Twins | Target Field | Ryan Feltner | Connor Prielipp |
| 9 | Kansas City Royals @ Chicago White Sox | Rate Field | Luinder Avila | Anthony Kay |
| 10 | Chicago Cubs @ Milwaukee Brewers | American Family Field | Ryan Rolison | Brandon Woodruff |
| 11 | Miami Marlins @ St. Louis Cardinals | Busch Stadium | Tyler Phillips | Kyle Leahy |
| 12 | Athletics @ Los Angeles Angels | Angel Stadium | Aaron Civale | Sam Aldegheri |
| 13 | Atlanta Braves @ San Francisco Giants | Oracle Park | Chris Sale | Robbie Ray |
| 14 | Los Angeles Dodgers @ San Diego Padres | Petco Park | Emmet Sheehan | Michael King |
| 15 | New York Yankees @ Boston Red Sox | Fenway Park | Carlos Rodón | Sonny Gray |

---

# Full Game Breakdown Cards

---

# 1. Washington Nationals @ Baltimore Orioles

## Game Context

| Field | Value |
| --- | --- |
| Park | Oriole Park at Camden Yards |
| Time | 2026-06-28T17:35:00Z |
| Away Team | Washington Nationals |
| Home Team | Baltimore Orioles |
| Away Probable Pitcher | Zack Littell |
| Home Probable Pitcher | Kyle Bradish |


## Away Starting Pitcher: Zack Littell

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1262 |
| Batted/Result Events | 346 |
| Hits Allowed | 83 |
| Walks | 28 |
| Strikeouts | 49 |
| Home Runs | 21 |
| K Event Rate | 14.2% |
| BB Event Rate | 8.1% |
| HR Event Rate | 6.1% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | WSH | 5.3 | 5 | 1 | 0 | 5 | 1 |
| 2026-06-17 | WSH | 8.0 | 7 | 4 | 2 | 2 | 4 |
| 2026-06-12 | WSH | 3.3 | 4 | 1 | 1 | 0 | 1 |
| 2026-06-06 | AZ | 6.3 | 2 | 0 | 2 | 4 | 0 |
| 2026-05-31 | WSH | 8.3 | 5 | 0 | 2 | 5 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF | vs L | 19.0% | 240 | 0.333 | 0.667 | 0.333 | 0.458 | 0.443 | 12.0% | 28.0% | 7.5% |
| FF | vs R | 9.1% | 115 | 0.280 | 0.680 | 0.400 | 0.471 | 0.371 | 16.7% | 22.4% | 14.3% |
| FS | vs L | 13.5% | 171 | 0.260 | 0.500 | 0.240 | 0.364 | 0.374 | 11.6% | 30.3% | 17.9% |
| FS | vs R | 6.3% | 79 | 0.138 | 0.276 | 0.138 | 0.222 | 0.217 | 5.6% | 30.8% | 24.4% |
| PO | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs L | 4.9% | 62 | 0.400 | 1.150 | 0.750 | 0.677 | 0.632 | 25.0% | 39.4% | 5.4% |
| SI | vs R | 8.6% | 109 | 0.333 | 0.481 | 0.148 | 0.341 | 0.381 | 11.1% | 26.3% | 4.8% |
| SL | vs L | 15.6% | 197 | 0.250 | 0.500 | 0.250 | 0.359 | 0.414 | 8.1% | 30.6% | 13.5% |
| SL | vs R | 13.2% | 167 | 0.189 | 0.243 | 0.054 | 0.268 | 0.364 | 9.4% | 32.1% | 21.5% |
| ST | vs L | 2.8% | 35 | 0.333 | 0.333 | 0.000 | 0.300 | 0.304 | 0.0% | 25.0% | 38.5% |
| ST | vs R | 6.8% | 86 | 0.227 | 0.227 | 0.000 | 0.226 | 0.276 | 0.0% | 14.3% | 19.4% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 59 | 5 | 0 | 5 | 1 |
| 2026-06-17 | 99 | 7 | 2 | 2 | 4 |
| 2026-06-12 | 56 | 4 | 1 | 0 | 1 |
| 2026-06-06 | 64 | 2 | 1 | 4 | 0 |
| 2026-05-31 | 84 | 5 | 2 | 5 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SI | Colton Cowser | 24 | 0.389 | 0.889 | 0.500 | 0.575 | 0.516 | 25.0% | 25.0% | 20.6% |
| SL | Colton Cowser | 34 | 0.273 | 0.667 | 0.394 | 0.399 | 0.358 | 25.0% | 33.3% | 57.4% |
| FS | Taylor Ward | 9 | 0.125 | 0.500 | 0.375 | 0.300 | 0.417 | 16.7% | 27.3% | 20.0% |
| FS | Samuel Basallo | 17 | 0.353 | 0.706 | 0.353 | 0.447 | 0.418 | 15.4% | 31.6% | 31.0% |
| FF | Pete Alonso | 100 | 0.278 | 0.622 | 0.344 | 0.401 | 0.443 | 25.8% | 37.1% | 23.4% |
| SI | Coby Mayo | 39 | 0.250 | 0.583 | 0.333 | 0.373 | 0.410 | 12.1% | 38.5% | 12.7% |
| FF | Jeremiah Jackson | 44 | 0.238 | 0.524 | 0.286 | 0.336 | 0.299 | 9.1% | 22.6% | 16.2% |
| SL | Coby Mayo | 47 | 0.213 | 0.489 | 0.277 | 0.312 | 0.250 | 17.4% | 51.1% | 49.5% |
| ST | Gunnar Henderson | 31 | 0.179 | 0.429 | 0.250 | 0.295 | 0.252 | 14.3% | 25.8% | 33.3% |
| SL | Adley Rutschman | 22 | 0.190 | 0.429 | 0.238 | 0.277 | 0.283 | 5.6% | 23.3% | 15.4% |
| FF | Adley Rutschman | 86 | 0.264 | 0.500 | 0.236 | 0.367 | 0.322 | 8.1% | 27.0% | 4.4% |
| FF | Samuel Basallo | 85 | 0.269 | 0.500 | 0.231 | 0.356 | 0.345 | 15.1% | 33.3% | 25.2% |
| SI | Leody Taveras | 34 | 0.407 | 0.630 | 0.222 | 0.510 | 0.463 | 4.2% | 25.6% | 18.0% |
| SI | Tyler O'Neill | 40 | 0.281 | 0.500 | 0.219 | 0.427 | 0.397 | 14.3% | 30.0% | 9.4% |
| SL | Jeremiah Jackson | 52 | 0.224 | 0.429 | 0.204 | 0.274 | 0.305 | 10.3% | 32.1% | 35.5% |
| FS | Pete Alonso | 6 | 0.200 | 0.400 | 0.200 | 0.325 | 0.346 | 0.0% | 50.0% | 50.0% |
| FF | Taylor Ward | 116 | 0.312 | 0.505 | 0.194 | 0.428 | 0.426 | 10.6% | 23.1% | 18.3% |
| SI | Gunnar Henderson | 72 | 0.292 | 0.477 | 0.185 | 0.391 | 0.366 | 7.3% | 26.9% | 11.7% |
| FF | Dylan Beavers | 43 | 0.237 | 0.421 | 0.184 | 0.334 | 0.385 | 13.3% | 19.4% | 12.3% |
| SI | Pete Alonso | 92 | 0.303 | 0.487 | 0.184 | 0.387 | 0.421 | 9.2% | 37.4% | 14.6% |
| ST | Blaze Alexander | 18 | 0.353 | 0.529 | 0.176 | 0.400 | 0.409 | 7.7% | 15.8% | 32.1% |
| FS | Gunnar Henderson | 25 | 0.217 | 0.391 | 0.174 | 0.302 | 0.377 | 15.8% | 29.0% | 27.5% |
| SL | Gunnar Henderson | 63 | 0.190 | 0.362 | 0.172 | 0.298 | 0.228 | 7.5% | 30.1% | 29.8% |
| FS | Jeremiah Jackson | 6 | 0.167 | 0.333 | 0.167 | 0.358 | 0.250 | 25.0% | 40.0% | 27.3% |
| FS | Adley Rutschman | 7 | 0.167 | 0.333 | 0.167 | 0.279 | 0.405 | 20.0% | 30.0% | 21.4% |
| SI | Jeremiah Jackson | 36 | 0.389 | 0.556 | 0.167 | 0.460 | 0.257 | 5.9% | 23.6% | 3.2% |
| SI | Adley Rutschman | 32 | 0.233 | 0.400 | 0.167 | 0.325 | 0.401 | 15.4% | 26.5% | 10.3% |
| FF | Colton Cowser | 68 | 0.212 | 0.365 | 0.154 | 0.353 | 0.402 | 14.3% | 28.1% | 14.9% |
| FF | Blaze Alexander | 60 | 0.250 | 0.404 | 0.154 | 0.327 | 0.349 | 13.9% | 20.0% | 27.3% |
| SI | Dylan Beavers | 17 | 0.308 | 0.462 | 0.154 | 0.418 | 0.445 | 0.0% | 32.0% | 7.1% |


## Home Starting Pitcher: Kyle Bradish

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1564 |
| Batted/Result Events | 404 |
| Hits Allowed | 91 |
| Walks | 45 |
| Strikeouts | 97 |
| Home Runs | 11 |
| K Event Rate | 24.0% |
| BB Event Rate | 11.1% |
| HR Event Rate | 2.7% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | LAA | 10.0 | 6 | 0 | 1 | 9 | 0 |
| 2026-06-17 | SEA | 9.3 | 5 | 0 | 2 | 12 | 0 |
| 2026-06-11 | BAL | 7.0 | 7 | 3 | 3 | 5 | 3 |
| 2026-06-06 | TOR | 7.0 | 9 | 1 | 3 | 3 | 1 |
| 2026-05-31 | BAL | 9.0 | 4 | 0 | 3 | 4 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 17.2% | 269 | 0.208 | 0.417 | 0.208 | 0.271 | 0.234 | 9.7% | 27.4% | 40.9% |
| CU | vs R | 4.7% | 73 | 0.200 | 0.250 | 0.050 | 0.263 | 0.277 | 18.2% | 47.1% | 40.0% |
| FF | vs L | 15.8% | 247 | 0.305 | 0.390 | 0.085 | 0.355 | 0.373 | 5.7% | 23.0% | 13.6% |
| FF | vs R | 2.7% | 42 | 0.444 | 0.556 | 0.111 | 0.519 | 0.513 | 11.1% | 53.8% | 5.9% |
| SI | vs L | 16.6% | 260 | 0.250 | 0.333 | 0.083 | 0.310 | 0.310 | 7.8% | 28.0% | 10.3% |
| SI | vs R | 16.0% | 250 | 0.254 | 0.339 | 0.085 | 0.294 | 0.252 | 9.5% | 20.3% | 8.9% |
| SL | vs L | 11.1% | 173 | 0.200 | 0.511 | 0.311 | 0.366 | 0.299 | 6.9% | 28.8% | 27.7% |
| SL | vs R | 15.9% | 249 | 0.289 | 0.533 | 0.244 | 0.384 | 0.358 | 12.1% | 18.8% | 39.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 101 | 6 | 1 | 9 | 0 |
| 2026-06-17 | 100 | 5 | 2 | 12 | 0 |
| 2026-06-11 | 85 | 7 | 3 | 5 | 3 |
| 2026-06-06 | 81 | 9 | 3 | 3 | 1 |
| 2026-05-31 | 94 | 4 | 3 | 4 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Curtis Mead | 14 | 0.455 | 0.909 | 0.455 | 0.600 | 0.394 | 12.5% | 40.0% | 15.0% |
| SL | James Wood | 59 | 0.264 | 0.604 | 0.340 | 0.396 | 0.390 | 25.0% | 34.1% | 46.5% |
| SI | Curtis Mead | 47 | 0.195 | 0.512 | 0.317 | 0.344 | 0.423 | 17.6% | 30.4% | 11.6% |
| SL | Dylan Crews | 19 | 0.158 | 0.474 | 0.316 | 0.258 | 0.350 | 27.3% | 28.6% | 45.5% |
| FF | James Wood | 108 | 0.330 | 0.626 | 0.297 | 0.451 | 0.484 | 23.8% | 35.9% | 17.3% |
| SI | Luis García | 42 | 0.289 | 0.579 | 0.289 | 0.398 | 0.383 | 11.8% | 36.1% | 3.0% |
| SL | Cj Abrams | 57 | 0.250 | 0.519 | 0.269 | 0.387 | 0.307 | 8.8% | 36.2% | 34.5% |
| FF | Brady House | 53 | 0.224 | 0.490 | 0.265 | 0.345 | 0.343 | 23.1% | 28.8% | 35.8% |
| SI | José Tena | 23 | 0.316 | 0.579 | 0.263 | 0.435 | 0.338 | 13.3% | 23.5% | 11.1% |
| SL | Curtis Mead | 39 | 0.171 | 0.429 | 0.257 | 0.295 | 0.342 | 13.8% | 25.0% | 20.7% |
| CU | Jacob Young | 13 | 0.250 | 0.500 | 0.250 | 0.346 | 0.274 | 12.5% | 30.8% | 30.0% |
| FF | Keibert Ruiz | 59 | 0.259 | 0.500 | 0.241 | 0.353 | 0.306 | 5.8% | 27.0% | 5.2% |
| FF | Luis García | 68 | 0.270 | 0.508 | 0.238 | 0.382 | 0.403 | 12.7% | 26.7% | 10.4% |
| FF | Jacob Young | 77 | 0.235 | 0.471 | 0.235 | 0.368 | 0.347 | 7.4% | 24.5% | 12.3% |
| FF | Cj Abrams | 91 | 0.342 | 0.575 | 0.233 | 0.455 | 0.418 | 12.1% | 20.3% | 22.6% |
| FF | Dylan Crews | 37 | 0.200 | 0.429 | 0.229 | 0.286 | 0.313 | 10.7% | 26.2% | 22.9% |
| CU | Luis García | 22 | 0.227 | 0.455 | 0.227 | 0.286 | 0.276 | 7.7% | 39.1% | 27.5% |
| FF | José Tena | 52 | 0.217 | 0.435 | 0.217 | 0.340 | 0.346 | 8.6% | 23.1% | 22.6% |
| SI | Daylen Lile | 49 | 0.357 | 0.571 | 0.214 | 0.446 | 0.462 | 4.9% | 25.0% | 10.3% |
| SI | James Wood | 67 | 0.296 | 0.500 | 0.204 | 0.410 | 0.471 | 19.0% | 40.8% | 14.7% |
| FF | Daylen Lile | 99 | 0.259 | 0.459 | 0.200 | 0.346 | 0.340 | 10.0% | 18.9% | 21.7% |
| SI | Cj Abrams | 45 | 0.310 | 0.500 | 0.190 | 0.370 | 0.390 | 11.4% | 32.8% | 13.4% |
| SL | Brady House | 32 | 0.375 | 0.531 | 0.156 | 0.394 | 0.197 | 4.8% | 29.0% | 38.9% |
| FF | Curtis Mead | 70 | 0.194 | 0.339 | 0.145 | 0.294 | 0.340 | 8.9% | 18.8% | 11.8% |
| SL | Daylen Lile | 59 | 0.207 | 0.345 | 0.138 | 0.259 | 0.220 | 4.8% | 23.0% | 23.3% |
| CU | James Wood | 32 | 0.069 | 0.207 | 0.138 | 0.167 | 0.272 | 16.7% | 36.4% | 50.0% |
| CU | Cj Abrams | 37 | 0.290 | 0.419 | 0.129 | 0.372 | 0.258 | 5.0% | 28.6% | 36.8% |
| SL | Luis García | 48 | 0.255 | 0.383 | 0.128 | 0.303 | 0.329 | 5.4% | 17.7% | 28.9% |
| SI | Jorbit Vivas | 31 | 0.360 | 0.480 | 0.120 | 0.421 | 0.294 | 0.0% | 19.5% | 10.4% |
| FF | Jorbit Vivas | 53 | 0.283 | 0.391 | 0.109 | 0.360 | 0.323 | 7.5% | 13.8% | 7.4% |


## Washington Nationals Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| James Wood | 418 | 0.249 | 0.490 | 0.241 | 0.371 | 0.413 | 22.5% | 35.6% | 31.2% |
| Daylen Lile | 377 | 0.250 | 0.401 | 0.151 | 0.315 | 0.314 | 6.7% | 22.3% | 20.7% |
| Cj Abrams | 362 | 0.281 | 0.514 | 0.233 | 0.385 | 0.343 | 9.5% | 27.1% | 26.2% |
| Nasim Nuñez | 294 | 0.234 | 0.274 | 0.040 | 0.289 | 0.269 | 0.0% | 11.5% | 21.0% |
| Luis García | 287 | 0.262 | 0.484 | 0.222 | 0.339 | 0.345 | 10.2% | 29.2% | 17.1% |
| Jacob Young | 278 | 0.221 | 0.364 | 0.143 | 0.300 | 0.302 | 6.3% | 24.6% | 18.8% |
| Curtis Mead | 245 | 0.220 | 0.463 | 0.243 | 0.342 | 0.362 | 11.4% | 26.3% | 15.6% |
| Keibert Ruiz | 196 | 0.265 | 0.443 | 0.178 | 0.318 | 0.271 | 4.9% | 27.8% | 12.3% |
| Brady House | 193 | 0.242 | 0.404 | 0.163 | 0.315 | 0.320 | 9.5% | 28.9% | 30.2% |
| Jorbit Vivas | 176 | 0.260 | 0.364 | 0.104 | 0.339 | 0.304 | 4.5% | 18.2% | 16.0% |
| José Tena | 176 | 0.213 | 0.348 | 0.134 | 0.282 | 0.292 | 8.3% | 28.6% | 30.8% |
| Dylan Crews | 146 | 0.210 | 0.355 | 0.145 | 0.273 | 0.320 | 8.7% | 28.1% | 28.2% |


## Baltimore Orioles Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gunnar Henderson | 395 | 0.224 | 0.420 | 0.196 | 0.329 | 0.306 | 8.3% | 26.3% | 21.7% |
| Taylor Ward | 390 | 0.257 | 0.361 | 0.103 | 0.347 | 0.347 | 5.0% | 24.2% | 16.9% |
| Pete Alonso | 387 | 0.251 | 0.463 | 0.212 | 0.347 | 0.380 | 13.1% | 33.5% | 25.8% |
| Leody Taveras | 274 | 0.243 | 0.364 | 0.121 | 0.311 | 0.286 | 5.1% | 19.3% | 25.0% |
| Samuel Basallo | 271 | 0.260 | 0.484 | 0.224 | 0.351 | 0.339 | 13.0% | 27.5% | 26.4% |
| Adley Rutschman | 243 | 0.260 | 0.456 | 0.195 | 0.349 | 0.354 | 8.7% | 27.6% | 12.7% |
| Coby Mayo | 241 | 0.188 | 0.381 | 0.193 | 0.284 | 0.285 | 10.1% | 30.5% | 29.9% |
| Colton Cowser | 220 | 0.216 | 0.374 | 0.158 | 0.308 | 0.317 | 11.7% | 19.9% | 32.6% |
| Jeremiah Jackson | 218 | 0.265 | 0.431 | 0.166 | 0.322 | 0.289 | 7.6% | 27.4% | 23.7% |
| Blaze Alexander | 214 | 0.299 | 0.418 | 0.119 | 0.349 | 0.352 | 6.8% | 24.5% | 24.8% |
| Tyler O'Neill | 165 | 0.185 | 0.274 | 0.089 | 0.262 | 0.279 | 5.9% | 25.8% | 27.6% |
| Dylan Beavers | 123 | 0.234 | 0.355 | 0.121 | 0.309 | 0.308 | 5.0% | 22.1% | 20.1% |


## Bullpen Fatigue Report

### Washington Nationals Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brad Lord | 2026-06-26 | 2.2 | 59 |
| Clayton Beeter | 2026-06-25 | 0.2 | 18 |
| Clayton Beeter | 2026-06-27 | 1.0 | 20 |
| Gus Varland | 2026-06-25 | 2.0 | 28 |
| Justin Lawrence | 2026-06-27 | 1.0 | 15 |
| Miles Mikolas | 2026-06-24 | 3.1 | 60 |
| Mitchell Parker | 2026-06-25 | 0.1 | 18 |
| Orlando Ribalta | 2026-06-24 | 0.2 | 23 |
| Orlando Ribalta | 2026-06-27 | 0.1 | 12 |
| PJ Poulin | 2026-06-24 | 1.1 | 15 |
| PJ Poulin | 2026-06-27 | 0.2 | 11 |
| Richard Lovelady | 2026-06-24 | 0.1 | 6 |
| Zak Kent | 2026-06-26 | 1.0 | 24 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Clayton Beeter, Justin Lawrence, Orlando Ribalta, PJ Poulin


### Baltimore Orioles Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Andrew Kittredge | 2026-06-24 | 0.1 | 11 |
| Andrew Kittredge | 2026-06-27 | 1.0 | 14 |
| Grant Wolfram | 2026-06-24 | 0.2 | 9 |
| Grant Wolfram | 2026-06-26 | 1.0 | 10 |
| Keegan Akin | 2026-06-24 | 0.2 | 12 |
| Keegan Akin | 2026-06-27 | 2.0 | 35 |
| Rico Garcia | 2026-06-24 | 1.0 | 19 |
| Rico Garcia | 2026-06-27 | 1.0 | 18 |
| Ryan Helsley | 2026-06-24 | 1.0 | 16 |
| Ryan Helsley | 2026-06-26 | 1.0 | 12 |
| Ryan Helsley | 2026-06-27 | 1.0 | 21 |
| Tyler Wells | 2026-06-24 | 1.1 | 28 |
| Tyler Wells | 2026-06-26 | 0.2 | 6 |
| Yennier Cano | 2026-06-24 | 0.2 | 25 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Andrew Kittredge, Keegan Akin, Rico Garcia, Ryan Helsley



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | James Wood | 418 | 0.249 | 0.490 | 0.241 | 0.371 | 22.5% | 35.6% |
| 2 | Daylen Lile | 377 | 0.250 | 0.401 | 0.151 | 0.315 | 6.7% | 22.3% |
| 3 | Cj Abrams | 362 | 0.281 | 0.514 | 0.233 | 0.385 | 9.5% | 27.1% |
| 4 | Nasim Nuñez | 294 | 0.234 | 0.274 | 0.040 | 0.289 | 0.0% | 11.5% |
| 5 | Luis García | 287 | 0.262 | 0.484 | 0.222 | 0.339 | 10.2% | 29.2% |
| 6 | Jacob Young | 278 | 0.221 | 0.364 | 0.143 | 0.300 | 6.3% | 24.6% |
| 7 | Curtis Mead | 245 | 0.220 | 0.463 | 0.243 | 0.342 | 11.4% | 26.3% |
| 8 | Keibert Ruiz | 196 | 0.265 | 0.443 | 0.178 | 0.318 | 4.9% | 27.8% |
| 9 | Brady House | 193 | 0.242 | 0.404 | 0.163 | 0.315 | 9.5% | 28.9% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Gunnar Henderson | 395 | 0.224 | 0.420 | 0.196 | 0.329 | 8.3% | 26.3% |
| 2 | Taylor Ward | 390 | 0.257 | 0.361 | 0.103 | 0.347 | 5.0% | 24.2% |
| 3 | Pete Alonso | 387 | 0.251 | 0.463 | 0.212 | 0.347 | 13.1% | 33.5% |
| 4 | Leody Taveras | 274 | 0.243 | 0.364 | 0.121 | 0.311 | 5.1% | 19.3% |
| 5 | Samuel Basallo | 271 | 0.260 | 0.484 | 0.224 | 0.351 | 13.0% | 27.5% |
| 6 | Adley Rutschman | 243 | 0.260 | 0.456 | 0.195 | 0.349 | 8.7% | 27.6% |
| 7 | Coby Mayo | 241 | 0.188 | 0.381 | 0.193 | 0.284 | 10.1% | 30.5% |
| 8 | Colton Cowser | 220 | 0.216 | 0.374 | 0.158 | 0.308 | 11.7% | 19.9% |
| 9 | Jeremiah Jackson | 218 | 0.265 | 0.431 | 0.166 | 0.322 | 7.6% | 27.4% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7124 |
| Hits Allowed | 1569 |
| Walks/HBP | 692 |
| Strikeouts | 1503 |
| Home Runs Allowed | 242 |
| K Event Rate | 21.1% |
| BB/HBP Event Rate | 9.7% |
| HR Event Rate | 3.4% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7002 |
| Hits Allowed | 1513 |
| Walks/HBP | 708 |
| Strikeouts | 1606 |
| Home Runs Allowed | 207 |
| K Event Rate | 22.9% |
| BB/HBP Event Rate | 10.1% |
| HR Event Rate | 3.0% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: SL, FF, FS, SI, ST
- Home pitcher pitch mix to inspect: SI, SL, CU, FF
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 2. Cincinnati Reds @ Pittsburgh Pirates

## Game Context

| Field | Value |
| --- | --- |
| Park | PNC Park |
| Time | 2026-06-28T17:35:00Z |
| Away Team | Cincinnati Reds |
| Home Team | Pittsburgh Pirates |
| Away Probable Pitcher | Brady Singer |
| Home Probable Pitcher | Mitch Keller |


## Away Starting Pitcher: Brady Singer

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1424 |
| Batted/Result Events | 361 |
| Hits Allowed | 93 |
| Walks | 27 |
| Strikeouts | 65 |
| Home Runs | 18 |
| K Event Rate | 18.0% |
| BB Event Rate | 7.5% |
| HR Event Rate | 5.0% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | CIN | 8.3 | 2 | 0 | 2 | 7 | 0 |
| 2026-06-16 | CIN | 7.3 | 3 | 0 | 5 | 5 | 0 |
| 2026-06-10 | SD | 8.0 | 6 | 0 | 1 | 5 | 0 |
| 2026-06-05 | STL | 6.7 | 4 | 1 | 3 | 6 | 1 |
| 2026-05-30 | CIN | 7.3 | 4 | 2 | 4 | 2 | 2 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | vs L | 5.0% | 71 | 0.308 | 0.538 | 0.231 | 0.407 | 0.425 | 7.7% | 14.3% | 21.1% |
| FC | vs R | 1.3% | 19 | 1.000 | 1.000 | 0.000 | 0.800 | 0.785 | 0.0% | 0.0% | 33.3% |
| FF | vs L | 2.9% | 41 | 0.571 | 1.000 | 0.429 | 0.671 | 0.551 | 16.7% | 23.1% | 11.8% |
| FF | vs R | 0.6% | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.755 | 0.0% | 25.0% | 0.0% |
| SI | vs L | 30.3% | 432 | 0.318 | 0.500 | 0.182 | 0.394 | 0.343 | 7.1% | 26.0% | 9.9% |
| SI | vs R | 17.1% | 243 | 0.246 | 0.493 | 0.246 | 0.356 | 0.380 | 8.9% | 35.9% | 15.2% |
| SL | vs L | 23.6% | 336 | 0.271 | 0.525 | 0.254 | 0.360 | 0.318 | 13.6% | 26.4% | 27.2% |
| SL | vs R | 8.6% | 122 | 0.185 | 0.259 | 0.074 | 0.228 | 0.297 | 10.0% | 33.3% | 37.0% |
| ST | vs L | 4.8% | 68 | 0.316 | 0.684 | 0.368 | 0.418 | 0.313 | 25.0% | 36.8% | 42.1% |
| ST | vs R | 5.8% | 83 | 0.238 | 0.571 | 0.333 | 0.379 | 0.411 | 13.3% | 27.3% | 30.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 106 | 2 | 2 | 7 | 0 |
| 2026-06-16 | 91 | 3 | 3 | 5 | 0 |
| 2026-06-10 | 95 | 6 | 1 | 5 | 0 |
| 2026-06-05 | 89 | 4 | 3 | 6 | 1 |
| 2026-05-30 | 94 | 4 | 4 | 2 | 2 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Oneil Cruz | 23 | 0.350 | 0.700 | 0.350 | 0.515 | 0.376 | 18.2% | 33.3% | 32.5% |
| SL | Nick Yorke | 7 | 0.333 | 0.667 | 0.333 | 0.457 | 0.286 | 0.0% | 33.3% | 17.6% |
| SL | Brandon Lowe | 60 | 0.232 | 0.536 | 0.304 | 0.333 | 0.297 | 13.9% | 31.2% | 38.1% |
| SL | Spencer Horwitz | 36 | 0.281 | 0.531 | 0.250 | 0.383 | 0.281 | 4.2% | 21.3% | 15.5% |
| ST | Bryan Reynolds | 32 | 0.360 | 0.600 | 0.240 | 0.473 | 0.379 | 21.4% | 45.5% | 41.5% |
| ST | Henry Davis | 15 | 0.133 | 0.333 | 0.200 | 0.193 | 0.237 | 9.1% | 36.4% | 19.4% |
| SI | Henry Davis | 41 | 0.219 | 0.406 | 0.188 | 0.349 | 0.422 | 10.0% | 37.7% | 8.8% |
| SL | Ryan O'Hearn | 45 | 0.233 | 0.419 | 0.186 | 0.296 | 0.249 | 3.7% | 26.8% | 24.7% |
| SL | Nick Gonzales | 41 | 0.237 | 0.421 | 0.184 | 0.333 | 0.394 | 6.1% | 24.1% | 24.7% |
| SL | Oneil Cruz | 38 | 0.235 | 0.412 | 0.176 | 0.345 | 0.351 | 15.0% | 36.8% | 44.0% |
| ST | Jake Mangum | 20 | 0.500 | 0.667 | 0.167 | 0.492 | 0.310 | 0.0% | 14.8% | 12.5% |
| ST | Konnor Griffin | 20 | 0.211 | 0.368 | 0.158 | 0.270 | 0.241 | 6.2% | 41.7% | 27.0% |
| SI | Nick Yorke | 29 | 0.269 | 0.423 | 0.154 | 0.371 | 0.343 | 4.2% | 36.1% | 6.8% |
| ST | Brandon Lowe | 29 | 0.077 | 0.231 | 0.154 | 0.216 | 0.231 | 0.0% | 25.0% | 35.0% |
| SI | Ryan O'Hearn | 53 | 0.354 | 0.500 | 0.146 | 0.419 | 0.442 | 9.5% | 38.7% | 8.5% |
| SL | Konnor Griffin | 37 | 0.194 | 0.333 | 0.139 | 0.219 | 0.273 | 7.7% | 20.8% | 38.0% |
| SI | Bryan Reynolds | 43 | 0.414 | 0.552 | 0.138 | 0.513 | 0.469 | 7.7% | 37.3% | 8.3% |
| SI | Marcell Ozuna | 57 | 0.235 | 0.353 | 0.118 | 0.301 | 0.319 | 2.6% | 33.9% | 11.5% |
| SL | Henry Davis | 20 | 0.158 | 0.263 | 0.105 | 0.240 | 0.255 | 8.3% | 27.3% | 28.6% |
| SL | Marcell Ozuna | 31 | 0.167 | 0.267 | 0.100 | 0.261 | 0.191 | 9.1% | 21.4% | 50.0% |
| SI | Jared Triolo | 37 | 0.226 | 0.323 | 0.097 | 0.361 | 0.325 | 0.0% | 32.4% | 12.5% |
| SL | Bryan Reynolds | 47 | 0.184 | 0.263 | 0.079 | 0.290 | 0.276 | 5.0% | 26.5% | 34.4% |
| SI | Brandon Lowe | 45 | 0.205 | 0.282 | 0.077 | 0.261 | 0.358 | 11.4% | 34.5% | 15.4% |
| SI | Konnor Griffin | 52 | 0.372 | 0.442 | 0.070 | 0.454 | 0.383 | 5.1% | 20.3% | 17.9% |
| ST | Nick Gonzales | 37 | 0.371 | 0.429 | 0.057 | 0.373 | 0.372 | 0.0% | 25.0% | 17.5% |
| SI | Oneil Cruz | 43 | 0.289 | 0.342 | 0.053 | 0.328 | 0.349 | 9.1% | 53.7% | 20.6% |
| SI | Jake Mangum | 24 | 0.125 | 0.167 | 0.042 | 0.202 | 0.225 | 0.0% | 16.2% | 12.8% |
| SI | Nick Gonzales | 85 | 0.333 | 0.372 | 0.038 | 0.356 | 0.292 | 0.0% | 23.5% | 16.8% |
| SI | Spencer Horwitz | 46 | 0.314 | 0.343 | 0.029 | 0.410 | 0.379 | 3.1% | 29.1% | 7.7% |
| SL | Jake Mangum | 29 | 0.207 | 0.207 | 0.000 | 0.248 | 0.248 | 0.0% | 20.9% | 18.2% |


## Home Starting Pitcher: Mitch Keller

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1584 |
| Batted/Result Events | 413 |
| Hits Allowed | 92 |
| Walks | 36 |
| Strikeouts | 80 |
| Home Runs | 11 |
| K Event Rate | 19.4% |
| BB Event Rate | 8.7% |
| HR Event Rate | 2.7% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | PIT | 8.7 | 7 | 2 | 1 | 4 | 2 |
| 2026-06-16 | ATH | 8.0 | 4 | 1 | 4 | 7 | 1 |
| 2026-06-11 | PIT | 8.0 | 7 | 1 | 6 | 3 | 1 |
| 2026-06-05 | ATL | 8.3 | 7 | 1 | 4 | 4 | 1 |
| 2026-05-30 | PIT | 7.7 | 10 | 0 | 1 | 5 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 8.1% | 129 | 0.286 | 0.536 | 0.250 | 0.359 | 0.386 | 18.2% | 26.5% | 18.5% |
| CH | vs R | 0.4% | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 33.3% |
| CU | vs L | 7.8% | 123 | 0.174 | 0.217 | 0.043 | 0.266 | 0.273 | 0.0% | 25.0% | 38.5% |
| CU | vs R | 0.8% | 13 | 0.333 | 1.333 | 1.000 | 0.667 | 0.381 | 50.0% | 33.3% | 20.0% |
| FC | vs L | 5.6% | 88 | 0.316 | 0.474 | 0.158 | 0.387 | 0.250 | 0.0% | 14.3% | 20.8% |
| FC | vs R | 0.9% | 15 | 0.250 | 0.250 | 0.000 | 0.320 | 0.265 | 0.0% | 0.0% | 20.0% |
| FF | vs L | 21.6% | 342 | 0.253 | 0.354 | 0.101 | 0.309 | 0.355 | 5.8% | 21.8% | 11.4% |
| FF | vs R | 11.0% | 174 | 0.188 | 0.250 | 0.062 | 0.247 | 0.385 | 4.5% | 27.3% | 24.1% |
| SI | vs L | 7.5% | 119 | 0.400 | 0.480 | 0.080 | 0.456 | 0.491 | 4.3% | 34.2% | 8.7% |
| SI | vs R | 11.0% | 174 | 0.294 | 0.294 | 0.000 | 0.353 | 0.374 | 0.0% | 27.6% | 18.2% |
| SL | vs L | 4.5% | 71 | 0.238 | 0.476 | 0.238 | 0.286 | 0.331 | 12.5% | 29.0% | 23.8% |
| SL | vs R | 3.9% | 61 | 0.235 | 0.235 | 0.000 | 0.263 | 0.328 | 0.0% | 16.0% | 12.9% |
| ST | vs L | 6.4% | 101 | 0.300 | 0.833 | 0.533 | 0.479 | 0.437 | 17.4% | 31.6% | 21.6% |
| ST | vs R | 10.5% | 166 | 0.151 | 0.283 | 0.132 | 0.224 | 0.183 | 5.1% | 21.3% | 25.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 92 | 7 | 1 | 4 | 2 |
| 2026-06-16 | 96 | 4 | 4 | 7 | 1 |
| 2026-06-11 | 98 | 7 | 4 | 3 | 1 |
| 2026-06-05 | 99 | 7 | 3 | 4 | 1 |
| 2026-05-30 | 77 | 10 | 1 | 5 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Jj Bleday | 14 | 0.455 | 1.364 | 0.909 | 0.732 | 0.614 | 30.0% | 78.6% | 37.5% |
| ST | Jj Bleday | 13 | 0.273 | 0.818 | 0.545 | 0.481 | 0.202 | 0.0% | 20.0% | 40.7% |
| SL | Nathaniel Lowe | 14 | 0.286 | 0.714 | 0.429 | 0.414 | 0.111 | 12.5% | 23.1% | 30.8% |
| SI | Tyler Stephenson | 43 | 0.429 | 0.829 | 0.400 | 0.584 | 0.568 | 25.0% | 37.8% | 15.9% |
| CH | Nathaniel Lowe | 31 | 0.276 | 0.621 | 0.345 | 0.394 | 0.359 | 13.0% | 30.0% | 18.2% |
| FF | Jj Bleday | 55 | 0.200 | 0.533 | 0.333 | 0.348 | 0.461 | 21.1% | 22.9% | 9.9% |
| CU | Eugenio Suárez | 15 | 0.333 | 0.667 | 0.333 | 0.477 | 0.469 | 16.7% | 15.4% | 36.4% |
| SL | Jj Bleday | 27 | 0.292 | 0.625 | 0.333 | 0.419 | 0.315 | 5.6% | 30.0% | 32.6% |
| SL | Elly De La Cruz | 21 | 0.190 | 0.524 | 0.333 | 0.336 | 0.361 | 15.4% | 40.9% | 26.3% |
| FF | Elly De La Cruz | 105 | 0.253 | 0.579 | 0.326 | 0.388 | 0.424 | 27.7% | 37.0% | 15.9% |
| FF | Sal Stewart | 101 | 0.313 | 0.614 | 0.301 | 0.464 | 0.378 | 19.6% | 29.5% | 32.8% |
| FF | Spencer Steer | 82 | 0.208 | 0.486 | 0.278 | 0.339 | 0.356 | 24.4% | 28.0% | 26.4% |
| CU | Tj Friedl | 13 | 0.182 | 0.455 | 0.273 | 0.277 | 0.293 | 10.0% | 28.6% | 27.3% |
| CH | Spencer Steer | 35 | 0.182 | 0.455 | 0.273 | 0.320 | 0.222 | 15.0% | 27.0% | 29.0% |
| SI | Ke'Bryan Hayes | 35 | 0.219 | 0.469 | 0.250 | 0.323 | 0.401 | 15.4% | 41.5% | 10.9% |
| ST | Matt Mclain | 40 | 0.243 | 0.459 | 0.216 | 0.328 | 0.286 | 17.4% | 25.0% | 22.2% |
| CU | Matt Mclain | 16 | 0.071 | 0.286 | 0.214 | 0.212 | 0.302 | 9.1% | 46.7% | 26.1% |
| ST | Nathaniel Lowe | 6 | 0.200 | 0.400 | 0.200 | 0.325 | 0.261 | 0.0% | 27.3% | 13.3% |
| CH | Sal Stewart | 30 | 0.320 | 0.520 | 0.200 | 0.447 | 0.387 | 6.2% | 29.0% | 31.1% |
| SI | Dane Myers | 32 | 0.462 | 0.654 | 0.192 | 0.581 | 0.515 | 10.0% | 27.8% | 2.4% |
| SI | Sal Stewart | 83 | 0.233 | 0.425 | 0.192 | 0.330 | 0.433 | 15.6% | 29.0% | 13.6% |
| SL | Sal Stewart | 49 | 0.190 | 0.381 | 0.190 | 0.306 | 0.259 | 10.0% | 20.0% | 26.0% |
| SL | Matt Mclain | 52 | 0.167 | 0.354 | 0.188 | 0.272 | 0.308 | 11.8% | 24.0% | 27.8% |
| CH | Jj Bleday | 50 | 0.200 | 0.378 | 0.178 | 0.304 | 0.340 | 8.8% | 29.6% | 33.7% |
| SI | Matt Mclain | 59 | 0.275 | 0.451 | 0.176 | 0.367 | 0.378 | 9.5% | 22.2% | 11.4% |
| SI | Elly De La Cruz | 37 | 0.235 | 0.412 | 0.176 | 0.292 | 0.302 | 14.3% | 34.3% | 17.0% |
| SI | Spencer Steer | 91 | 0.240 | 0.413 | 0.173 | 0.353 | 0.372 | 10.0% | 27.7% | 14.0% |
| SL | Spencer Steer | 35 | 0.212 | 0.364 | 0.152 | 0.271 | 0.351 | 8.7% | 25.7% | 32.0% |
| ST | Spencer Steer | 36 | 0.235 | 0.382 | 0.147 | 0.287 | 0.294 | 16.0% | 23.4% | 16.9% |
| ST | Sal Stewart | 45 | 0.171 | 0.317 | 0.146 | 0.223 | 0.257 | 12.9% | 16.1% | 21.1% |


## Cincinnati Reds Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sal Stewart | 377 | 0.254 | 0.462 | 0.208 | 0.358 | 0.356 | 14.6% | 25.3% | 24.4% |
| Spencer Steer | 328 | 0.242 | 0.440 | 0.198 | 0.340 | 0.348 | 13.9% | 27.6% | 22.5% |
| Matt Mclain | 312 | 0.213 | 0.375 | 0.162 | 0.312 | 0.326 | 10.5% | 23.2% | 23.0% |
| Elly De La Cruz | 298 | 0.266 | 0.491 | 0.225 | 0.364 | 0.361 | 15.3% | 35.3% | 27.0% |
| Tyler Stephenson | 242 | 0.217 | 0.354 | 0.137 | 0.303 | 0.331 | 11.8% | 26.7% | 26.1% |
| Jj Bleday | 235 | 0.245 | 0.540 | 0.295 | 0.390 | 0.370 | 11.1% | 30.8% | 24.2% |
| Eugenio Suárez | 226 | 0.211 | 0.373 | 0.162 | 0.305 | 0.261 | 7.1% | 19.3% | 32.9% |
| Nathaniel Lowe | 218 | 0.255 | 0.484 | 0.229 | 0.370 | 0.360 | 12.0% | 21.3% | 16.9% |
| Tj Friedl | 193 | 0.201 | 0.284 | 0.083 | 0.261 | 0.250 | 3.3% | 22.3% | 24.3% |
| Blake Dunn | 158 | 0.276 | 0.379 | 0.103 | 0.326 | 0.280 | 2.8% | 20.6% | 20.7% |
| Dane Myers | 152 | 0.256 | 0.364 | 0.109 | 0.342 | 0.357 | 7.0% | 21.6% | 16.9% |
| Ke'Bryan Hayes | 146 | 0.157 | 0.231 | 0.075 | 0.224 | 0.312 | 8.5% | 31.3% | 18.1% |


## Pittsburgh Pirates Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bryan Reynolds | 376 | 0.288 | 0.468 | 0.179 | 0.388 | 0.372 | 9.8% | 29.7% | 26.0% |
| Brandon Lowe | 356 | 0.245 | 0.503 | 0.258 | 0.357 | 0.349 | 13.2% | 29.2% | 32.1% |
| Nick Gonzales | 329 | 0.292 | 0.367 | 0.075 | 0.323 | 0.321 | 2.9% | 21.9% | 21.2% |
| Spencer Horwitz | 313 | 0.271 | 0.447 | 0.176 | 0.368 | 0.339 | 8.5% | 21.0% | 14.0% |
| Oneil Cruz | 300 | 0.261 | 0.470 | 0.208 | 0.368 | 0.358 | 16.9% | 36.9% | 35.3% |
| Ryan O'Hearn | 298 | 0.266 | 0.428 | 0.162 | 0.335 | 0.321 | 6.8% | 25.9% | 19.7% |
| Marcell Ozuna | 248 | 0.204 | 0.320 | 0.116 | 0.276 | 0.315 | 8.1% | 27.2% | 29.1% |
| Konnor Griffin | 227 | 0.263 | 0.415 | 0.151 | 0.341 | 0.310 | 9.0% | 24.6% | 30.5% |
| Jake Mangum | 213 | 0.289 | 0.340 | 0.051 | 0.323 | 0.278 | 1.3% | 14.0% | 17.2% |
| Jared Triolo | 182 | 0.229 | 0.283 | 0.054 | 0.298 | 0.276 | 0.8% | 25.2% | 22.9% |
| Henry Davis | 171 | 0.160 | 0.333 | 0.173 | 0.286 | 0.302 | 12.2% | 31.9% | 21.7% |
| Nick Yorke | 107 | 0.202 | 0.277 | 0.074 | 0.264 | 0.306 | 5.1% | 28.3% | 14.7% |


## Bullpen Fatigue Report

### Cincinnati Reds Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brock Burke | 2026-06-24 | 1.0 | 15 |
| Brock Burke | 2026-06-26 | 1.0 | 20 |
| Caleb Ferguson | 2026-06-26 | 1.0 | 18 |
| Caleb Ferguson | 2026-06-27 | 1.0 | 14 |
| Chase Petty | 2026-06-27 | 1.0 | 12 |
| Pierce Johnson | 2026-06-26 | 0.2 | 13 |
| Sam Moll | 2026-06-24 | 1.0 | 22 |
| Sam Moll | 2026-06-27 | 0.2 | 20 |
| Tejay Antone | 2026-06-24 | 1.1 | 17 |
| Tejay Antone | 2026-06-26 | 1.0 | 17 |
| Tejay Antone | 2026-06-27 | 0.1 | 6 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Caleb Ferguson, Chase Petty, Sam Moll, Tejay Antone


### Pittsburgh Pirates Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brandan Bidois | 2026-06-26 | 1.0 | 10 |
| Carmen Mlodzinski | 2026-06-24 | 3.0 | 39 |
| Dennis Santana | 2026-06-26 | 1.1 | 14 |
| Evan Sisk | 2026-06-25 | 1.0 | 23 |
| Evan Sisk | 2026-06-27 | 0.1 | 11 |
| Gregory Soto | 2026-06-25 | 1.0 | 17 |
| Gregory Soto | 2026-06-27 | 1.0 | 33 |
| Isaac Mattson | 2026-06-26 | 1.0 | 12 |
| Isaac Mattson | 2026-06-27 | 1.0 | 13 |
| Mason Montgomery | 2026-06-25 | 1.1 | 15 |
| Mason Montgomery | 2026-06-26 | 0.2 | 23 |
| Yohan Ramírez | 2026-06-25 | 0.1 | 13 |
| Yohan Ramírez | 2026-06-27 | 2.0 | 26 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Evan Sisk, Gregory Soto, Isaac Mattson, Yohan Ramírez



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Sal Stewart | 377 | 0.254 | 0.462 | 0.208 | 0.358 | 14.6% | 25.3% |
| 2 | Spencer Steer | 328 | 0.242 | 0.440 | 0.198 | 0.340 | 13.9% | 27.6% |
| 3 | Matt Mclain | 312 | 0.213 | 0.375 | 0.162 | 0.312 | 10.5% | 23.2% |
| 4 | Elly De La Cruz | 298 | 0.266 | 0.491 | 0.225 | 0.364 | 15.3% | 35.3% |
| 5 | Tyler Stephenson | 242 | 0.217 | 0.354 | 0.137 | 0.303 | 11.8% | 26.7% |
| 6 | Jj Bleday | 235 | 0.245 | 0.540 | 0.295 | 0.390 | 11.1% | 30.8% |
| 7 | Eugenio Suárez | 226 | 0.211 | 0.373 | 0.162 | 0.305 | 7.1% | 19.3% |
| 8 | Nathaniel Lowe | 218 | 0.255 | 0.484 | 0.229 | 0.370 | 12.0% | 21.3% |
| 9 | Tj Friedl | 193 | 0.201 | 0.284 | 0.083 | 0.261 | 3.3% | 22.3% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bryan Reynolds | 376 | 0.288 | 0.468 | 0.179 | 0.388 | 9.8% | 29.7% |
| 2 | Brandon Lowe | 356 | 0.245 | 0.503 | 0.258 | 0.357 | 13.2% | 29.2% |
| 3 | Nick Gonzales | 329 | 0.292 | 0.367 | 0.075 | 0.323 | 2.9% | 21.9% |
| 4 | Spencer Horwitz | 313 | 0.271 | 0.447 | 0.176 | 0.368 | 8.5% | 21.0% |
| 5 | Oneil Cruz | 300 | 0.261 | 0.470 | 0.208 | 0.368 | 16.9% | 36.9% |
| 6 | Ryan O'Hearn | 298 | 0.266 | 0.428 | 0.162 | 0.335 | 6.8% | 25.9% |
| 7 | Marcell Ozuna | 248 | 0.204 | 0.320 | 0.116 | 0.276 | 8.1% | 27.2% |
| 8 | Konnor Griffin | 227 | 0.263 | 0.415 | 0.151 | 0.341 | 9.0% | 24.6% |
| 9 | Jake Mangum | 213 | 0.289 | 0.340 | 0.051 | 0.323 | 1.3% | 14.0% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7078 |
| Hits Allowed | 1493 |
| Walks/HBP | 792 |
| Strikeouts | 1599 |
| Home Runs Allowed | 242 |
| K Event Rate | 22.6% |
| BB/HBP Event Rate | 11.2% |
| HR Event Rate | 3.4% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7119 |
| Hits Allowed | 1537 |
| Walks/HBP | 752 |
| Strikeouts | 1707 |
| Home Runs Allowed | 200 |
| K Event Rate | 24.0% |
| BB/HBP Event Rate | 10.6% |
| HR Event Rate | 2.8% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: SI, SL, ST
- Home pitcher pitch mix to inspect: FF, SI, ST, CU, CH, SL
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 3. Texas Rangers @ Toronto Blue Jays

## Game Context

| Field | Value |
| --- | --- |
| Park | Rogers Centre |
| Time | 2026-06-28T17:37:00Z |
| Away Team | Texas Rangers |
| Home Team | Toronto Blue Jays |
| Away Probable Pitcher | Kumar Rocker |
| Home Probable Pitcher | Shane Bieber |


## Away Starting Pitcher: Kumar Rocker

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1328 |
| Batted/Result Events | 337 |
| Hits Allowed | 75 |
| Walks | 32 |
| Strikeouts | 71 |
| Home Runs | 8 |
| K Event Rate | 21.1% |
| BB Event Rate | 9.5% |
| HR Event Rate | 2.4% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | MIA | 6.3 | 5 | 0 | 0 | 9 | 0 |
| 2026-06-16 | TEX | 6.7 | 7 | 2 | 2 | 4 | 2 |
| 2026-06-11 | KC | 6.7 | 5 | 0 | 2 | 3 | 0 |
| 2026-06-05 | TEX | 7.3 | 6 | 1 | 1 | 5 | 1 |
| 2026-05-30 | TEX | 8.0 | 3 | 0 | 3 | 2 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 6.1% | 81 | 0.235 | 0.412 | 0.176 | 0.261 | 0.491 | 17.6% | 41.4% | 23.7% |
| CH | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| FC | vs L | 8.0% | 106 | 0.412 | 0.706 | 0.294 | 0.500 | 0.472 | 6.2% | 35.9% | 12.0% |
| FC | vs R | 4.6% | 61 | 0.250 | 0.250 | 0.000 | 0.291 | 0.437 | 14.3% | 14.3% | 39.1% |
| FF | vs L | 8.1% | 107 | 0.227 | 0.455 | 0.227 | 0.321 | 0.292 | 5.9% | 20.0% | 10.9% |
| FF | vs R | 2.7% | 36 | 0.000 | 0.000 | 0.000 | 0.117 | 0.220 | 0.0% | 0.0% | 25.0% |
| PO | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs L | 14.1% | 187 | 0.467 | 0.778 | 0.311 | 0.572 | 0.538 | 14.3% | 46.4% | 7.4% |
| SI | vs R | 17.4% | 231 | 0.262 | 0.344 | 0.082 | 0.355 | 0.332 | 1.8% | 31.7% | 9.2% |
| SL | vs L | 22.4% | 298 | 0.143 | 0.186 | 0.043 | 0.157 | 0.170 | 2.6% | 24.7% | 37.5% |
| SL | vs R | 16.3% | 216 | 0.182 | 0.273 | 0.091 | 0.222 | 0.257 | 8.8% | 15.5% | 42.1% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 76 | 5 | 0 | 9 | 0 |
| 2026-06-16 | 70 | 7 | 2 | 4 | 2 |
| 2026-06-11 | 84 | 5 | 2 | 3 | 0 |
| 2026-06-05 | 94 | 6 | 1 | 5 | 1 |
| 2026-05-30 | 85 | 3 | 3 | 2 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Brandon Valenzuela | 13 | 0.308 | 1.231 | 0.923 | 0.615 | 0.464 | 57.1% | 36.8% | 38.2% |
| FC | Yohendrick Pinango | 10 | 0.444 | 1.000 | 0.556 | 0.610 | 0.519 | 14.3% | 40.0% | 25.0% |
| FC | Jesús Sánchez | 21 | 0.500 | 1.050 | 0.550 | 0.652 | 0.468 | 22.2% | 39.4% | 29.4% |
| FC | George Springer | 21 | 0.429 | 0.905 | 0.476 | 0.560 | 0.488 | 21.1% | 32.1% | 10.8% |
| SI | Davis Schneider | 15 | 0.364 | 0.727 | 0.364 | 0.490 | 0.465 | 33.3% | 35.3% | 9.1% |
| FF | Kazuma Okamoto | 111 | 0.327 | 0.643 | 0.316 | 0.443 | 0.426 | 21.7% | 37.4% | 25.9% |
| SL | Yohendrick Pinango | 15 | 0.333 | 0.600 | 0.267 | 0.397 | 0.343 | 20.0% | 50.0% | 37.9% |
| SL | Kazuma Okamoto | 50 | 0.262 | 0.524 | 0.262 | 0.390 | 0.368 | 19.0% | 26.8% | 47.7% |
| FF | Daulton Varsho | 95 | 0.214 | 0.476 | 0.262 | 0.335 | 0.320 | 20.8% | 25.9% | 20.0% |
| FF | George Springer | 79 | 0.262 | 0.523 | 0.262 | 0.396 | 0.352 | 11.1% | 22.3% | 18.6% |
| FC | Vladimir Guerrero | 32 | 0.160 | 0.400 | 0.240 | 0.312 | 0.395 | 13.6% | 23.1% | 25.9% |
| SI | Yohendrick Pinango | 18 | 0.235 | 0.471 | 0.235 | 0.319 | 0.348 | 14.3% | 47.8% | 7.4% |
| FF | Ernie Clement | 82 | 0.333 | 0.551 | 0.218 | 0.404 | 0.275 | 0.0% | 14.5% | 9.2% |
| SL | Nathan Lukes | 17 | 0.286 | 0.500 | 0.214 | 0.400 | 0.363 | 0.0% | 20.0% | 20.0% |
| SI | Kazuma Okamoto | 66 | 0.207 | 0.414 | 0.207 | 0.304 | 0.331 | 11.1% | 33.0% | 26.4% |
| FF | Andrés Giménez | 86 | 0.266 | 0.468 | 0.203 | 0.338 | 0.250 | 3.2% | 11.9% | 20.0% |
| SL | Jesús Sánchez | 26 | 0.240 | 0.440 | 0.200 | 0.304 | 0.376 | 20.0% | 33.3% | 24.5% |
| SL | Daulton Varsho | 43 | 0.225 | 0.400 | 0.175 | 0.337 | 0.262 | 3.1% | 16.4% | 21.4% |
| FC | Ernie Clement | 26 | 0.200 | 0.360 | 0.160 | 0.227 | 0.235 | 8.0% | 23.3% | 17.0% |
| FC | Andrés Giménez | 19 | 0.263 | 0.421 | 0.158 | 0.295 | 0.307 | 6.2% | 13.9% | 19.1% |
| FF | Jesús Sánchez | 75 | 0.309 | 0.456 | 0.147 | 0.337 | 0.325 | 8.0% | 22.8% | 21.0% |
| FF | Vladimir Guerrero | 61 | 0.340 | 0.472 | 0.132 | 0.387 | 0.390 | 8.9% | 27.7% | 15.7% |
| SI | Daulton Varsho | 44 | 0.375 | 0.500 | 0.125 | 0.452 | 0.330 | 3.0% | 25.9% | 13.9% |
| SI | Brandon Valenzuela | 21 | 0.438 | 0.562 | 0.125 | 0.500 | 0.357 | 0.0% | 29.2% | 15.6% |
| SI | Ernie Clement | 71 | 0.358 | 0.478 | 0.119 | 0.385 | 0.308 | 3.1% | 21.2% | 1.9% |
| SL | George Springer | 50 | 0.222 | 0.333 | 0.111 | 0.304 | 0.240 | 3.2% | 20.0% | 35.7% |
| FF | Myles Straw | 55 | 0.304 | 0.413 | 0.109 | 0.342 | 0.370 | 6.8% | 20.3% | 8.3% |
| FC | Myles Straw | 11 | 0.300 | 0.400 | 0.100 | 0.341 | 0.347 | 0.0% | 14.3% | 6.2% |
| SL | Ernie Clement | 53 | 0.327 | 0.423 | 0.096 | 0.336 | 0.263 | 5.0% | 18.3% | 24.4% |
| FF | Brandon Valenzuela | 62 | 0.204 | 0.296 | 0.093 | 0.260 | 0.316 | 5.0% | 18.9% | 18.0% |


## Home Starting Pitcher: Shane Bieber

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 75 |
| Batted/Result Events | 19 |
| Hits Allowed | 9 |
| Walks | 0 |
| Strikeouts | 2 |
| Home Runs | 3 |
| K Event Rate | 10.5% |
| BB Event Rate | 0.0% |
| HR Event Rate | 15.8% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | TOR | 6.3 | 9 | 3 | 0 | 2 | 3 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 9.3% | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.046 | 0.0% | 33.3% | 0.0% |
| CH | vs R | 8.0% | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 75.0% |
| FC | vs L | 5.3% | 4 | 1.000 | 1.000 | 0.000 | 0.900 | 0.890 | 0.0% | 0.0% | 0.0% |
| FC | vs R | 18.7% | 14 | 0.500 | 1.250 | 0.750 | 0.725 | 0.653 | 25.0% | 33.3% | 25.0% |
| FF | vs L | 13.3% | 10 | 0.500 | 2.000 | 1.500 | 1.000 | 0.905 | 50.0% | 50.0% | 0.0% |
| FF | vs R | 17.3% | 13 | 0.250 | 0.500 | 0.250 | 0.312 | 0.310 | 0.0% | 33.3% | 0.0% |
| KC | vs L | 4.0% | 3 | 1.000 | 1.500 | 0.500 | 1.075 | 1.188 | 50.0% | 66.7% | 0.0% |
| KC | vs R | 4.0% | 3 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SL | vs R | 20.0% | 15 | 0.667 | 1.667 | 1.000 | 0.967 | 1.103 | 66.7% | 42.9% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 75 | 9 | 0 | 2 | 3 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KC | Wyatt Langford | 4 | 0.500 | 1.500 | 1.000 | 0.812 | 0.325 | 0.0% | 40.0% | 0.0% |
| KC | Jake Burger | 3 | 0.333 | 1.333 | 1.000 | 0.667 | 0.357 | 100.0% | 100.0% | 75.0% |
| FC | Kyle Higashioka | 8 | 0.375 | 0.875 | 0.500 | 0.631 | 0.292 | 14.3% | 17.6% | 29.2% |
| FC | Josh Jung | 24 | 0.350 | 0.800 | 0.450 | 0.515 | 0.499 | 10.0% | 39.5% | 18.4% |
| CH | Kyle Higashioka | 11 | 0.333 | 0.778 | 0.444 | 0.505 | 0.358 | 20.0% | 40.0% | 41.7% |
| FC | Joc Pederson | 18 | 0.375 | 0.812 | 0.438 | 0.519 | 0.438 | 14.3% | 25.8% | 25.0% |
| FC | Danny Jansen | 8 | 0.143 | 0.571 | 0.429 | 0.338 | 0.288 | 20.0% | 20.0% | 28.6% |
| FC | Corey Seager | 19 | 0.316 | 0.737 | 0.421 | 0.437 | 0.500 | 16.7% | 34.8% | 7.1% |
| SL | Wyatt Langford | 30 | 0.300 | 0.633 | 0.333 | 0.392 | 0.329 | 16.0% | 29.4% | 14.0% |
| KC | Josh Jung | 7 | 0.333 | 0.667 | 0.333 | 0.457 | 0.294 | 0.0% | 0.0% | 33.3% |
| CH | Corey Seager | 32 | 0.241 | 0.552 | 0.310 | 0.394 | 0.401 | 20.0% | 36.7% | 33.3% |
| CH | Wyatt Langford | 13 | 0.231 | 0.538 | 0.308 | 0.319 | 0.332 | 10.0% | 40.0% | 30.3% |
| SL | Danny Jansen | 14 | 0.214 | 0.500 | 0.286 | 0.296 | 0.155 | 11.1% | 15.8% | 27.3% |
| FF | Joc Pederson | 88 | 0.270 | 0.554 | 0.284 | 0.403 | 0.424 | 16.4% | 39.3% | 24.7% |
| CH | Danny Jansen | 12 | 0.364 | 0.636 | 0.273 | 0.446 | 0.278 | 0.0% | 15.4% | 36.4% |
| FC | Wyatt Langford | 16 | 0.200 | 0.467 | 0.267 | 0.303 | 0.295 | 15.4% | 16.0% | 28.9% |
| FC | Brandon Nimmo | 37 | 0.286 | 0.543 | 0.257 | 0.368 | 0.415 | 16.7% | 35.1% | 18.8% |
| KC | Brandon Nimmo | 8 | 0.250 | 0.500 | 0.250 | 0.312 | 0.242 | 14.3% | 33.3% | 18.8% |
| SL | Ezequiel Duran | 38 | 0.343 | 0.571 | 0.229 | 0.414 | 0.238 | 0.0% | 20.0% | 39.1% |
| CH | Jake Burger | 36 | 0.281 | 0.500 | 0.219 | 0.354 | 0.349 | 9.5% | 25.0% | 38.6% |
| FF | Josh Jung | 90 | 0.282 | 0.500 | 0.218 | 0.392 | 0.359 | 15.3% | 28.8% | 13.1% |
| FF | Evan Carter | 83 | 0.186 | 0.400 | 0.214 | 0.312 | 0.355 | 11.7% | 22.0% | 13.8% |
| FF | Corey Seager | 58 | 0.149 | 0.362 | 0.213 | 0.292 | 0.292 | 21.4% | 22.4% | 29.6% |
| SL | Brandon Nimmo | 48 | 0.233 | 0.442 | 0.209 | 0.314 | 0.412 | 16.7% | 32.8% | 26.3% |
| SL | Corey Seager | 35 | 0.129 | 0.323 | 0.194 | 0.246 | 0.258 | 11.1% | 15.2% | 47.9% |
| FC | Alejandro Osuna | 18 | 0.438 | 0.625 | 0.188 | 0.536 | 0.390 | 0.0% | 34.6% | 0.0% |
| SL | Joc Pederson | 36 | 0.250 | 0.438 | 0.188 | 0.339 | 0.293 | 18.8% | 36.1% | 42.0% |
| CH | Josh Jung | 32 | 0.429 | 0.607 | 0.179 | 0.481 | 0.322 | 4.5% | 36.1% | 20.8% |
| FF | Brandon Nimmo | 120 | 0.265 | 0.441 | 0.176 | 0.355 | 0.348 | 7.5% | 25.7% | 16.4% |
| CH | Joc Pederson | 41 | 0.200 | 0.375 | 0.175 | 0.255 | 0.306 | 6.2% | 34.0% | 31.0% |


## Texas Rangers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brandon Nimmo | 369 | 0.261 | 0.421 | 0.161 | 0.333 | 0.382 | 13.4% | 30.9% | 18.3% |
| Josh Jung | 344 | 0.293 | 0.444 | 0.151 | 0.353 | 0.343 | 5.9% | 29.1% | 17.0% |
| Jake Burger | 341 | 0.262 | 0.456 | 0.194 | 0.346 | 0.314 | 9.9% | 31.0% | 31.7% |
| Ezequiel Duran | 286 | 0.264 | 0.425 | 0.161 | 0.334 | 0.303 | 7.2% | 22.4% | 23.5% |
| Joc Pederson | 275 | 0.237 | 0.449 | 0.212 | 0.346 | 0.352 | 11.0% | 31.7% | 28.8% |
| Evan Carter | 241 | 0.168 | 0.307 | 0.139 | 0.276 | 0.294 | 6.8% | 23.0% | 24.9% |
| Corey Seager | 231 | 0.186 | 0.382 | 0.196 | 0.298 | 0.336 | 16.5% | 26.4% | 31.6% |
| Wyatt Langford | 190 | 0.278 | 0.506 | 0.227 | 0.360 | 0.303 | 8.0% | 25.9% | 19.0% |
| Alejandro Osuna | 169 | 0.267 | 0.301 | 0.034 | 0.326 | 0.321 | 0.8% | 21.2% | 12.2% |
| Kyle Higashioka | 166 | 0.242 | 0.389 | 0.148 | 0.326 | 0.296 | 9.6% | 28.9% | 27.3% |
| Danny Jansen | 152 | 0.176 | 0.321 | 0.145 | 0.274 | 0.254 | 6.8% | 25.1% | 24.0% |
| Josh Smith | 137 | 0.214 | 0.239 | 0.026 | 0.268 | 0.284 | 4.4% | 24.9% | 19.0% |


## Toronto Blue Jays Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Vladimir Guerrero | 346 | 0.279 | 0.372 | 0.093 | 0.332 | 0.346 | 7.1% | 30.4% | 17.2% |
| Kazuma Okamoto | 345 | 0.243 | 0.470 | 0.227 | 0.348 | 0.332 | 14.8% | 28.8% | 32.4% |
| Ernie Clement | 329 | 0.297 | 0.435 | 0.139 | 0.332 | 0.272 | 2.5% | 17.1% | 15.0% |
| Andrés Giménez | 290 | 0.247 | 0.397 | 0.150 | 0.299 | 0.266 | 4.2% | 14.0% | 22.4% |
| George Springer | 286 | 0.235 | 0.418 | 0.183 | 0.341 | 0.306 | 9.2% | 22.1% | 21.4% |
| Daulton Varsho | 283 | 0.256 | 0.429 | 0.173 | 0.346 | 0.309 | 8.1% | 23.8% | 18.2% |
| Jesús Sánchez | 251 | 0.283 | 0.452 | 0.170 | 0.339 | 0.335 | 10.7% | 27.1% | 23.6% |
| Nathan Lukes | 182 | 0.315 | 0.418 | 0.103 | 0.359 | 0.301 | 0.7% | 15.9% | 16.0% |
| Brandon Valenzuela | 171 | 0.247 | 0.427 | 0.180 | 0.331 | 0.334 | 8.3% | 22.3% | 24.4% |
| Myles Straw | 156 | 0.237 | 0.324 | 0.086 | 0.283 | 0.304 | 3.3% | 17.2% | 11.4% |
| Yohendrick Pinango | 142 | 0.288 | 0.462 | 0.174 | 0.355 | 0.324 | 8.9% | 27.4% | 21.0% |
| Davis Schneider | 131 | 0.156 | 0.284 | 0.128 | 0.258 | 0.270 | 10.4% | 28.4% | 27.6% |


## Bullpen Fatigue Report

### Texas Rangers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Cole Winn | 2026-06-24 | 0.2 | 15 |
| Jacob Latz | 2026-06-25 | 1.0 | 25 |
| Jacob Latz | 2026-06-26 | 1.0 | 14 |
| Jakob Junis | 2026-06-25 | 1.0 | 18 |
| Jakob Junis | 2026-06-26 | 0.2 | 23 |
| Joe Ross | 2026-06-27 | 1.1 | 29 |
| Peyton Gray | 2026-06-27 | 2.1 | 39 |
| Robby Ahlstrom | 2026-06-24 | 0.1 | 4 |
| Robby Ahlstrom | 2026-06-26 | 0.1 | 15 |
| Robby Ahlstrom | 2026-06-27 | 0.1 | 12 |
| Tyler Alexander | 2026-06-24 | 1.0 | 13 |
| Tyler Alexander | 2026-06-27 | 1.0 | 15 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Joe Ross, Peyton Gray, Robby Ahlstrom, Tyler Alexander


### Toronto Blue Jays Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Adam Macko | 2026-06-26 | 1.0 | 31 |
| Braydon Fisher | 2026-06-27 | 1.0 | 12 |
| Jeff Hoffman | 2026-06-24 | 1.1 | 13 |
| Jeff Hoffman | 2026-06-27 | 1.0 | 20 |
| Louis Varland | 2026-06-26 | 1.0 | 10 |
| Mason Fluharty | 2026-06-24 | 1.0 | 20 |
| Mason Fluharty | 2026-06-27 | 0.1 | 14 |
| Simeon Woods Richardson | 2026-06-25 | 3.0 | 43 |
| Spencer Miles | 2026-06-26 | 2.2 | 35 |
| Tommy Nance | 2026-06-24 | 1.0 | 12 |
| Tommy Nance | 2026-06-27 | 1.0 | 11 |
| Tyler Rogers | 2026-06-27 | 1.0 | 22 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Braydon Fisher, Jeff Hoffman, Mason Fluharty, Tommy Nance, Tyler Rogers



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Brandon Nimmo | 369 | 0.261 | 0.421 | 0.161 | 0.333 | 13.4% | 30.9% |
| 2 | Josh Jung | 344 | 0.293 | 0.444 | 0.151 | 0.353 | 5.9% | 29.1% |
| 3 | Jake Burger | 341 | 0.262 | 0.456 | 0.194 | 0.346 | 9.9% | 31.0% |
| 4 | Ezequiel Duran | 286 | 0.264 | 0.425 | 0.161 | 0.334 | 7.2% | 22.4% |
| 5 | Joc Pederson | 275 | 0.237 | 0.449 | 0.212 | 0.346 | 11.0% | 31.7% |
| 6 | Evan Carter | 241 | 0.168 | 0.307 | 0.139 | 0.276 | 6.8% | 23.0% |
| 7 | Corey Seager | 231 | 0.186 | 0.382 | 0.196 | 0.298 | 16.5% | 26.4% |
| 8 | Wyatt Langford | 190 | 0.278 | 0.506 | 0.227 | 0.360 | 8.0% | 25.9% |
| 9 | Alejandro Osuna | 169 | 0.267 | 0.301 | 0.034 | 0.326 | 0.8% | 21.2% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Vladimir Guerrero | 346 | 0.279 | 0.372 | 0.093 | 0.332 | 7.1% | 30.4% |
| 2 | Kazuma Okamoto | 345 | 0.243 | 0.470 | 0.227 | 0.348 | 14.8% | 28.8% |
| 3 | Ernie Clement | 329 | 0.297 | 0.435 | 0.139 | 0.332 | 2.5% | 17.1% |
| 4 | Andrés Giménez | 290 | 0.247 | 0.397 | 0.150 | 0.299 | 4.2% | 14.0% |
| 5 | George Springer | 286 | 0.235 | 0.418 | 0.183 | 0.341 | 9.2% | 22.1% |
| 6 | Daulton Varsho | 283 | 0.256 | 0.429 | 0.173 | 0.346 | 8.1% | 23.8% |
| 7 | Jesús Sánchez | 251 | 0.283 | 0.452 | 0.170 | 0.339 | 10.7% | 27.1% |
| 8 | Nathan Lukes | 182 | 0.315 | 0.418 | 0.103 | 0.359 | 0.7% | 15.9% |
| 9 | Brandon Valenzuela | 171 | 0.247 | 0.427 | 0.180 | 0.331 | 8.3% | 22.3% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6785 |
| Hits Allowed | 1450 |
| Walks/HBP | 651 |
| Strikeouts | 1550 |
| Home Runs Allowed | 207 |
| K Event Rate | 22.8% |
| BB/HBP Event Rate | 9.6% |
| HR Event Rate | 3.1% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6741 |
| Hits Allowed | 1488 |
| Walks/HBP | 608 |
| Strikeouts | 1443 |
| Home Runs Allowed | 193 |
| K Event Rate | 21.4% |
| BB/HBP Event Rate | 9.0% |
| HR Event Rate | 2.9% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: SL, SI, FC, FF
- Home pitcher pitch mix to inspect: FF, FC, SL, CH, KC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 4. Houston Astros @ Detroit Tigers

## Game Context

| Field | Value |
| --- | --- |
| Park | Comerica Park |
| Time | 2026-06-28T17:40:00Z |
| Away Team | Houston Astros |
| Home Team | Detroit Tigers |
| Away Probable Pitcher | Hunter Brown |
| Home Probable Pitcher | Jack Flaherty |


## Away Starting Pitcher: Hunter Brown

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 440 |
| Batted/Result Events | 101 |
| Hits Allowed | 16 |
| Walks | 14 |
| Strikeouts | 34 |
| Home Runs | 1 |
| K Event Rate | 33.7% |
| BB Event Rate | 13.9% |
| HR Event Rate | 1.0% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | TOR | 5.7 | 4 | 1 | 4 | 4 | 1 |
| 2026-06-16 | HOU | 7.3 | 3 | 0 | 3 | 7 | 0 |
| 2026-03-31 | HOU | 7.0 | 1 | 0 | 2 | 8 | 0 |
| 2026-03-26 | HOU | 7.3 | 4 | 0 | 4 | 9 | 0 |
| 2026-03-20 | HOU | 6.3 | 4 | 0 | 3 | 6 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 6.4% | 28 | 0.200 | 0.400 | 0.200 | 0.379 | 0.520 | 0.0% | 12.5% | 42.9% |
| CH | vs R | 0.9% | 4 | 0.000 | 0.000 | 0.000 | 0.700 | 0.700 | 0.0% | 0.0% | 50.0% |
| FC | vs L | 0.2% | 1 | 0.000 | 0.000 | 0.000 | 0.000 | — | 0.0% | 0.0% | 100.0% |
| FF | vs L | 25.0% | 110 | 0.059 | 0.059 | 0.000 | 0.089 | 0.081 | 0.0% | 23.1% | 28.6% |
| FF | vs R | 10.0% | 44 | 0.286 | 0.429 | 0.143 | 0.356 | 0.303 | 0.0% | 21.4% | 19.0% |
| KC | vs L | 11.4% | 50 | 0.231 | 0.231 | 0.000 | 0.300 | 0.392 | 12.5% | 21.4% | 25.0% |
| KC | vs R | 9.1% | 40 | 0.091 | 0.091 | 0.000 | 0.082 | 0.105 | 0.0% | 14.3% | 46.7% |
| SI | vs L | 5.7% | 25 | 0.333 | 0.333 | 0.000 | 0.400 | 0.254 | 0.0% | 28.6% | 12.5% |
| SI | vs R | 22.0% | 97 | 0.278 | 0.444 | 0.167 | 0.382 | 0.304 | 7.1% | 22.6% | 15.0% |
| SL | vs L | 0.9% | 4 | 0.000 | 0.000 | 0.000 | 0.700 | 0.731 | 0.0% | 0.0% | 0.0% |
| SL | vs R | 8.4% | 37 | 0.143 | 0.143 | 0.000 | 0.200 | 0.092 | 0.0% | 0.0% | 18.8% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 85 | 4 | 2 | 4 | 1 |
| 2026-06-16 | 92 | 3 | 3 | 7 | 0 |
| 2026-03-31 | 78 | 1 | 2 | 8 | 0 |
| 2026-03-26 | 102 | 4 | 4 | 9 | 0 |
| 2026-03-20 | 83 | 4 | 3 | 6 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Dillon Dingler | 32 | 0.448 | 1.069 | 0.621 | 0.636 | 0.429 | 13.0% | 35.7% | 24.6% |
| SI | Jahmai Jones | 23 | 0.167 | 0.500 | 0.333 | 0.365 | 0.494 | 14.3% | 20.0% | 13.3% |
| KC | Kevin Mcgonigle | 6 | 0.333 | 0.667 | 0.333 | 0.417 | 0.245 | 0.0% | 37.5% | 10.0% |
| FF | Kerry Carpenter | 64 | 0.196 | 0.500 | 0.304 | 0.328 | 0.334 | 10.5% | 27.6% | 22.8% |
| FF | Dillon Dingler | 90 | 0.312 | 0.613 | 0.300 | 0.416 | 0.463 | 20.3% | 28.7% | 13.9% |
| SI | Spencer Torkelson | 65 | 0.298 | 0.596 | 0.298 | 0.405 | 0.448 | 19.1% | 33.0% | 12.4% |
| SI | Wenceel Pérez | 35 | 0.290 | 0.581 | 0.290 | 0.404 | 0.395 | 17.2% | 23.3% | 9.6% |
| FF | Spencer Torkelson | 98 | 0.228 | 0.494 | 0.266 | 0.379 | 0.370 | 19.2% | 29.7% | 21.8% |
| SI | Gleyber Torres | 44 | 0.333 | 0.583 | 0.250 | 0.447 | 0.329 | 6.5% | 18.6% | 5.7% |
| SL | Hao-Yu Lee | 12 | 0.167 | 0.417 | 0.250 | 0.242 | 0.106 | 0.0% | 0.0% | 50.0% |
| SL | Spencer Torkelson | 43 | 0.205 | 0.436 | 0.231 | 0.308 | 0.278 | 11.5% | 25.4% | 33.0% |
| SL | Kevin Mcgonigle | 40 | 0.171 | 0.400 | 0.229 | 0.295 | 0.332 | 16.7% | 24.4% | 19.1% |
| FF | Hao-Yu Lee | 43 | 0.250 | 0.475 | 0.225 | 0.334 | 0.298 | 17.4% | 34.7% | 27.4% |
| SL | Matt Vierling | 39 | 0.205 | 0.410 | 0.205 | 0.282 | 0.331 | 8.8% | 28.3% | 16.4% |
| SL | Colt Keith | 28 | 0.185 | 0.370 | 0.185 | 0.282 | 0.218 | 17.6% | 36.4% | 36.8% |
| FF | Riley Greene | 134 | 0.270 | 0.443 | 0.174 | 0.356 | 0.357 | 14.5% | 26.3% | 20.5% |
| SI | Kevin Mcgonigle | 80 | 0.391 | 0.565 | 0.174 | 0.454 | 0.404 | 6.2% | 30.6% | 6.2% |
| FF | Gleyber Torres | 66 | 0.226 | 0.396 | 0.170 | 0.354 | 0.374 | 15.8% | 25.0% | 24.0% |
| FF | Kevin Mcgonigle | 118 | 0.278 | 0.443 | 0.165 | 0.386 | 0.423 | 13.1% | 23.9% | 9.5% |
| SI | Matt Vierling | 44 | 0.154 | 0.308 | 0.154 | 0.251 | 0.341 | 5.9% | 32.1% | 10.3% |
| FF | Zach Mckinstry | 75 | 0.156 | 0.266 | 0.109 | 0.247 | 0.242 | 1.9% | 9.3% | 8.3% |
| FF | Wenceel Pérez | 66 | 0.138 | 0.241 | 0.103 | 0.227 | 0.277 | 6.7% | 20.3% | 13.9% |
| SL | Kerry Carpenter | 29 | 0.069 | 0.172 | 0.103 | 0.100 | 0.149 | 14.3% | 25.6% | 36.8% |
| SI | Dillon Dingler | 82 | 0.229 | 0.329 | 0.100 | 0.328 | 0.392 | 6.7% | 29.9% | 11.7% |
| SI | Riley Greene | 52 | 0.452 | 0.548 | 0.095 | 0.490 | 0.424 | 9.4% | 45.3% | 9.0% |
| FF | Matt Vierling | 65 | 0.138 | 0.224 | 0.086 | 0.228 | 0.300 | 9.3% | 18.6% | 15.5% |
| SL | Jahmai Jones | 13 | 0.077 | 0.154 | 0.077 | 0.165 | 0.111 | 0.0% | 36.4% | 56.7% |
| SL | Riley Greene | 44 | 0.375 | 0.450 | 0.075 | 0.394 | 0.352 | 10.0% | 44.7% | 32.9% |
| FF | Jahmai Jones | 33 | 0.214 | 0.250 | 0.036 | 0.308 | 0.350 | 15.0% | 28.6% | 22.9% |
| SL | Zach Mckinstry | 31 | 0.143 | 0.179 | 0.036 | 0.224 | 0.316 | 0.0% | 15.4% | 25.0% |


## Home Starting Pitcher: Jack Flaherty

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1445 |
| Batted/Result Events | 347 |
| Hits Allowed | 81 |
| Walks | 36 |
| Strikeouts | 87 |
| Home Runs | 11 |
| K Event Rate | 25.1% |
| BB Event Rate | 10.4% |
| HR Event Rate | 3.2% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-12 | CLE | 4.3 | 3 | 0 | 1 | 1 | 0 |
| 2026-06-07 | DET | 7.3 | 6 | 0 | 1 | 7 | 0 |
| 2026-06-02 | TB | 7.3 | 5 | 0 | 2 | 6 | 0 |
| 2026-05-28 | DET | 8.0 | 6 | 0 | 0 | 9 | 0 |
| 2026-05-22 | BAL | 6.3 | 8 | 2 | 0 | 7 | 2 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 2.6% | 37 | 0.000 | 0.000 | 0.000 | 0.233 | 0.700 | 0.0% | 0.0% | 25.0% |
| CH | vs R | 0.5% | 7 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 33.3% |
| FF | vs L | 24.8% | 358 | 0.309 | 0.481 | 0.173 | 0.391 | 0.348 | 10.0% | 30.0% | 12.8% |
| FF | vs R | 24.0% | 347 | 0.250 | 0.434 | 0.184 | 0.331 | 0.349 | 10.9% | 27.4% | 18.2% |
| KC | vs L | 9.8% | 141 | 0.276 | 0.552 | 0.276 | 0.385 | 0.329 | 15.0% | 22.2% | 29.3% |
| KC | vs R | 9.3% | 135 | 0.222 | 0.296 | 0.074 | 0.352 | 0.284 | 0.0% | 13.3% | 40.3% |
| SI | vs L | 2.5% | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.128 | 0.0% | 0.0% | 27.3% |
| SI | vs R | 1.3% | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.005 | 0.0% | 0.0% | 50.0% |
| SL | vs L | 11.8% | 170 | 0.289 | 0.553 | 0.263 | 0.404 | 0.355 | 6.7% | 38.6% | 31.6% |
| SL | vs R | 13.2% | 191 | 0.286 | 0.571 | 0.286 | 0.390 | 0.303 | 10.3% | 24.1% | 27.4% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-12 | 63 | 3 | 1 | 1 | 0 |
| 2026-06-07 | 87 | 6 | 1 | 7 | 0 |
| 2026-06-02 | 94 | 5 | 2 | 6 | 0 |
| 2026-05-28 | 95 | 6 | 1 | 9 | 0 |
| 2026-05-22 | 78 | 8 | 0 | 7 | 2 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KC | Yordan Álvarez | 3 | 0.500 | 1.000 | 0.500 | 0.650 | 0.867 | 50.0% | 60.0% | 14.3% |
| SL | Christian Walker | 62 | 0.283 | 0.700 | 0.417 | 0.416 | 0.271 | 13.6% | 31.1% | 39.3% |
| FF | Yordan Álvarez | 96 | 0.296 | 0.654 | 0.358 | 0.444 | 0.474 | 18.0% | 28.5% | 15.0% |
| SL | Yordan Álvarez | 43 | 0.282 | 0.564 | 0.282 | 0.393 | 0.410 | 19.4% | 19.6% | 22.5% |
| FF | Yainer Diaz | 33 | 0.241 | 0.517 | 0.276 | 0.364 | 0.340 | 13.6% | 20.5% | 23.8% |
| SL | Jeremy Peña | 37 | 0.267 | 0.533 | 0.267 | 0.405 | 0.362 | 0.0% | 17.4% | 33.8% |
| SL | Cam Smith | 41 | 0.200 | 0.457 | 0.257 | 0.340 | 0.354 | 21.7% | 27.1% | 38.4% |
| FF | Christian Walker | 95 | 0.190 | 0.430 | 0.241 | 0.344 | 0.309 | 8.9% | 20.4% | 21.4% |
| FF | Cam Smith | 92 | 0.260 | 0.468 | 0.208 | 0.365 | 0.388 | 16.9% | 31.4% | 20.0% |
| FF | José Altuve | 80 | 0.297 | 0.500 | 0.203 | 0.379 | 0.329 | 11.8% | 39.1% | 25.3% |
| FF | Isaac Paredes | 99 | 0.218 | 0.402 | 0.184 | 0.325 | 0.338 | 8.1% | 24.3% | 10.0% |
| SL | José Altuve | 45 | 0.167 | 0.333 | 0.167 | 0.232 | 0.253 | 6.1% | 7.8% | 27.4% |
| FF | Joey Loperfido | 40 | 0.364 | 0.515 | 0.152 | 0.436 | 0.403 | 7.7% | 32.7% | 18.3% |
| FF | Christian Vázquez | 76 | 0.224 | 0.373 | 0.149 | 0.295 | 0.268 | 3.5% | 13.3% | 14.8% |
| FF | Jeremy Peña | 41 | 0.361 | 0.500 | 0.139 | 0.415 | 0.459 | 6.5% | 21.1% | 10.1% |
| FF | Carlos Correa | 36 | 0.267 | 0.400 | 0.133 | 0.357 | 0.315 | 9.1% | 20.8% | 13.0% |
| FF | Jake Meyers | 49 | 0.267 | 0.400 | 0.133 | 0.340 | 0.286 | 10.8% | 20.5% | 10.2% |
| FF | Brice Matthews | 73 | 0.270 | 0.397 | 0.127 | 0.338 | 0.324 | 12.8% | 25.3% | 37.4% |
| SL | Carlos Correa | 22 | 0.222 | 0.333 | 0.111 | 0.291 | 0.283 | 14.3% | 23.8% | 30.3% |
| SL | Yainer Diaz | 24 | 0.250 | 0.333 | 0.083 | 0.254 | 0.278 | 5.0% | 13.5% | 24.1% |
| SL | Isaac Paredes | 45 | 0.143 | 0.214 | 0.071 | 0.174 | 0.173 | 0.0% | 25.9% | 27.2% |
| SL | Christian Vázquez | 18 | 0.125 | 0.188 | 0.062 | 0.169 | 0.152 | 0.0% | 19.2% | 27.8% |
| SL | Joey Loperfido | 20 | 0.056 | 0.111 | 0.056 | 0.167 | 0.153 | 0.0% | 8.7% | 42.6% |
| SL | Brice Matthews | 29 | 0.111 | 0.148 | 0.037 | 0.167 | 0.174 | 0.0% | 28.0% | 39.3% |
| SL | Jake Meyers | 21 | 0.056 | 0.056 | 0.000 | 0.143 | 0.209 | 0.0% | 11.1% | 41.2% |
| KC | Christian Walker | 6 | 0.167 | 0.167 | 0.000 | 0.300 | 0.169 | 0.0% | 0.0% | 45.5% |
| KC | José Altuve | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.017 | 0.0% | 0.0% | 22.2% |
| KC | Cam Smith | 6 | 0.200 | 0.200 | 0.000 | 0.267 | 0.234 | 0.0% | 50.0% | 81.8% |
| KC | Isaac Paredes | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.267 | 0.0% | 0.0% | 40.0% |


## Houston Astros Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yordan Álvarez | 374 | 0.308 | 0.599 | 0.292 | 0.426 | 0.476 | 18.0% | 30.5% | 16.8% |
| Christian Walker | 359 | 0.236 | 0.466 | 0.230 | 0.347 | 0.305 | 10.1% | 27.3% | 25.6% |
| Isaac Paredes | 335 | 0.247 | 0.410 | 0.163 | 0.341 | 0.316 | 6.0% | 22.7% | 16.8% |
| Cam Smith | 325 | 0.218 | 0.363 | 0.145 | 0.300 | 0.335 | 12.9% | 28.2% | 28.3% |
| José Altuve | 280 | 0.233 | 0.375 | 0.142 | 0.308 | 0.297 | 6.4% | 22.8% | 23.8% |
| Brice Matthews | 220 | 0.200 | 0.345 | 0.145 | 0.287 | 0.265 | 9.2% | 24.3% | 36.3% |
| Jeremy Peña | 197 | 0.298 | 0.449 | 0.152 | 0.369 | 0.351 | 4.1% | 24.6% | 25.2% |
| Christian Vázquez | 186 | 0.214 | 0.321 | 0.107 | 0.267 | 0.237 | 2.2% | 14.4% | 16.5% |
| Carlos Correa | 149 | 0.281 | 0.414 | 0.133 | 0.356 | 0.364 | 9.8% | 22.4% | 21.2% |
| Jake Meyers | 149 | 0.204 | 0.314 | 0.109 | 0.275 | 0.257 | 7.5% | 17.5% | 20.0% |
| Yainer Diaz | 147 | 0.252 | 0.374 | 0.122 | 0.297 | 0.288 | 5.1% | 20.0% | 20.4% |
| Joey Loperfido | 124 | 0.226 | 0.340 | 0.113 | 0.304 | 0.303 | 6.4% | 20.5% | 27.4% |


## Detroit Tigers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kevin Mcgonigle | 375 | 0.279 | 0.420 | 0.141 | 0.363 | 0.368 | 8.6% | 23.4% | 13.4% |
| Riley Greene | 371 | 0.294 | 0.449 | 0.155 | 0.368 | 0.358 | 12.9% | 30.7% | 26.8% |
| Spencer Torkelson | 341 | 0.205 | 0.411 | 0.205 | 0.314 | 0.315 | 14.6% | 27.0% | 28.2% |
| Dillon Dingler | 334 | 0.275 | 0.560 | 0.285 | 0.390 | 0.392 | 12.8% | 29.5% | 19.4% |
| Colt Keith | 259 | 0.251 | 0.368 | 0.117 | 0.309 | 0.316 | 8.4% | 29.2% | 21.0% |
| Matt Vierling | 243 | 0.199 | 0.344 | 0.145 | 0.270 | 0.302 | 6.0% | 21.4% | 14.9% |
| Kerry Carpenter | 214 | 0.213 | 0.447 | 0.234 | 0.322 | 0.306 | 10.5% | 28.6% | 28.3% |
| Zach Mckinstry | 213 | 0.182 | 0.262 | 0.080 | 0.275 | 0.266 | 2.0% | 11.6% | 12.6% |
| Gleyber Torres | 200 | 0.289 | 0.410 | 0.120 | 0.367 | 0.343 | 8.4% | 18.5% | 20.5% |
| Wenceel Pérez | 190 | 0.183 | 0.371 | 0.189 | 0.270 | 0.272 | 8.5% | 23.6% | 16.1% |
| Hao-Yu Lee | 125 | 0.261 | 0.395 | 0.134 | 0.306 | 0.275 | 8.1% | 20.8% | 29.1% |
| Jahmai Jones | 113 | 0.165 | 0.262 | 0.097 | 0.245 | 0.294 | 7.6% | 27.0% | 30.8% |


## Bullpen Fatigue Report

### Houston Astros Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| AJ Blubaugh | 2026-06-25 | 2.0 | 25 |
| AJ Blubaugh | 2026-06-27 | 2.0 | 28 |
| Bryan Abreu | 2026-06-26 | 1.0 | 10 |
| Bryan King | 2026-06-24 | 1.0 | 14 |
| Bryan King | 2026-06-27 | 1.0 | 11 |
| Enyel De Los Santos | 2026-06-25 | 1.0 | 10 |
| Jake Meyers | 2026-06-26 | 1.0 | 9 |
| Josh Hader | 2026-06-24 | 1.0 | 15 |
| Josh Hader | 2026-06-27 | 1.0 | 11 |
| Nate Pearson | 2026-06-26 | 3.0 | 48 |
| Steven Okert | 2026-06-24 | 1.0 | 19 |
| Steven Okert | 2026-06-27 | 1.1 | 15 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** AJ Blubaugh, Bryan King, Josh Hader, Steven Okert


### Detroit Tigers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Drew Anderson | 2026-06-27 | 0.2 | 25 |
| Drew Sommers | 2026-06-27 | 0.1 | 5 |
| Enmanuel De Jesus | 2026-06-24 | 1.1 | 19 |
| Enmanuel De Jesus | 2026-06-26 | 2.0 | 27 |
| Jacob Waguespack | 2026-06-24 | 1.2 | 20 |
| Jacob Waguespack | 2026-06-27 | 1.0 | 14 |
| Kenley Jansen | 2026-06-25 | 1.0 | 15 |
| Kyle Finnegan | 2026-06-25 | 1.0 | 13 |
| Tyler Holton | 2026-06-25 | 1.0 | 18 |
| Will Vest | 2026-06-27 | 1.0 | 26 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Drew Anderson, Drew Sommers, Jacob Waguespack, Will Vest



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Yordan Álvarez | 374 | 0.308 | 0.599 | 0.292 | 0.426 | 18.0% | 30.5% |
| 2 | Christian Walker | 359 | 0.236 | 0.466 | 0.230 | 0.347 | 10.1% | 27.3% |
| 3 | Isaac Paredes | 335 | 0.247 | 0.410 | 0.163 | 0.341 | 6.0% | 22.7% |
| 4 | Cam Smith | 325 | 0.218 | 0.363 | 0.145 | 0.300 | 12.9% | 28.2% |
| 5 | José Altuve | 280 | 0.233 | 0.375 | 0.142 | 0.308 | 6.4% | 22.8% |
| 6 | Brice Matthews | 220 | 0.200 | 0.345 | 0.145 | 0.287 | 9.2% | 24.3% |
| 7 | Jeremy Peña | 197 | 0.298 | 0.449 | 0.152 | 0.369 | 4.1% | 24.6% |
| 8 | Christian Vázquez | 186 | 0.214 | 0.321 | 0.107 | 0.267 | 2.2% | 14.4% |
| 9 | Carlos Correa | 149 | 0.281 | 0.414 | 0.133 | 0.356 | 9.8% | 22.4% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Kevin Mcgonigle | 375 | 0.279 | 0.420 | 0.141 | 0.363 | 8.6% | 23.4% |
| 2 | Riley Greene | 371 | 0.294 | 0.449 | 0.155 | 0.368 | 12.9% | 30.7% |
| 3 | Spencer Torkelson | 341 | 0.205 | 0.411 | 0.205 | 0.314 | 14.6% | 27.0% |
| 4 | Dillon Dingler | 334 | 0.275 | 0.560 | 0.285 | 0.390 | 12.8% | 29.5% |
| 5 | Colt Keith | 259 | 0.251 | 0.368 | 0.117 | 0.309 | 8.4% | 29.2% |
| 6 | Matt Vierling | 243 | 0.199 | 0.344 | 0.145 | 0.270 | 6.0% | 21.4% |
| 7 | Kerry Carpenter | 214 | 0.213 | 0.447 | 0.234 | 0.322 | 10.5% | 28.6% |
| 8 | Zach Mckinstry | 213 | 0.182 | 0.262 | 0.080 | 0.275 | 2.0% | 11.6% |
| 9 | Gleyber Torres | 200 | 0.289 | 0.410 | 0.120 | 0.367 | 8.4% | 18.5% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7002 |
| Hits Allowed | 1467 |
| Walks/HBP | 777 |
| Strikeouts | 1555 |
| Home Runs Allowed | 228 |
| K Event Rate | 22.2% |
| BB/HBP Event Rate | 11.1% |
| HR Event Rate | 3.3% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6787 |
| Hits Allowed | 1453 |
| Walks/HBP | 655 |
| Strikeouts | 1517 |
| Home Runs Allowed | 195 |
| K Event Rate | 22.4% |
| BB/HBP Event Rate | 9.7% |
| HR Event Rate | 2.9% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SI, KC, SL
- Home pitcher pitch mix to inspect: FF, SL, KC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 5. Seattle Mariners @ Cleveland Guardians

## Game Context

| Field | Value |
| --- | --- |
| Park | Progressive Field |
| Time | 2026-06-28T17:40:00Z |
| Away Team | Seattle Mariners |
| Home Team | Cleveland Guardians |
| Away Probable Pitcher | Emerson Hancock |
| Home Probable Pitcher | Gavin Williams |


## Away Starting Pitcher: Emerson Hancock

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1398 |
| Batted/Result Events | 355 |
| Hits Allowed | 76 |
| Walks | 19 |
| Strikeouts | 85 |
| Home Runs | 12 |
| K Event Rate | 23.9% |
| BB Event Rate | 5.4% |
| HR Event Rate | 3.4% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-20 | SEA | 7.3 | 4 | 1 | 2 | 6 | 1 |
| 2026-06-14 | WSH | 7.0 | 9 | 1 | 0 | 2 | 1 |
| 2026-06-08 | BAL | 7.0 | 3 | 0 | 3 | 3 | 0 |
| 2026-06-01 | SEA | 6.7 | 2 | 2 | 0 | 7 | 2 |
| 2026-05-26 | ATH | 7.3 | 1 | 0 | 3 | 3 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 5.2% | 73 | 0.235 | 0.412 | 0.176 | 0.329 | 0.288 | 6.7% | 23.8% | 18.5% |
| CH | vs R | 0.4% | 5 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CU | vs L | 1.7% | 24 | 0.167 | 0.167 | 0.000 | 0.150 | 0.155 | 0.0% | 0.0% | 44.4% |
| CU | vs R | 0.1% | 1 | 1.000 | 1.000 | 0.000 | 0.900 | 0.796 | 0.0% | 0.0% | 0.0% |
| FC | vs L | 9.7% | 136 | 0.190 | 0.524 | 0.333 | 0.315 | 0.395 | 29.4% | 29.7% | 31.6% |
| FC | vs R | 1.9% | 27 | 0.300 | 0.300 | 0.000 | 0.309 | 0.270 | 0.0% | 8.3% | 14.3% |
| FF | vs L | 25.8% | 361 | 0.182 | 0.352 | 0.170 | 0.256 | 0.341 | 17.2% | 25.6% | 18.7% |
| FF | vs R | 11.2% | 157 | 0.184 | 0.447 | 0.263 | 0.306 | 0.367 | 17.4% | 20.0% | 27.3% |
| SI | vs L | 9.0% | 126 | 0.308 | 0.410 | 0.103 | 0.342 | 0.417 | 5.6% | 40.7% | 6.2% |
| SI | vs R | 15.6% | 218 | 0.339 | 0.468 | 0.129 | 0.376 | 0.360 | 5.3% | 29.2% | 12.3% |
| ST | vs L | 7.2% | 100 | 0.267 | 0.400 | 0.133 | 0.312 | 0.272 | 0.0% | 0.0% | 30.3% |
| ST | vs R | 12.1% | 169 | 0.091 | 0.152 | 0.061 | 0.137 | 0.141 | 0.0% | 14.3% | 36.5% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-20 | 76 | 4 | 2 | 6 | 1 |
| 2026-06-14 | 59 | 9 | 0 | 2 | 1 |
| 2026-06-08 | 92 | 3 | 2 | 3 | 0 |
| 2026-06-01 | 91 | 2 | 0 | 7 | 2 |
| 2026-05-26 | 87 | 1 | 2 | 3 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Angel Martínez | 26 | 0.391 | 0.826 | 0.435 | 0.531 | 0.393 | 11.8% | 35.1% | 10.9% |
| FC | Travis Bazzana | 9 | 0.286 | 0.714 | 0.429 | 0.472 | 0.468 | 0.0% | 27.8% | 20.8% |
| FF | José Ramírez | 83 | 0.292 | 0.653 | 0.361 | 0.426 | 0.411 | 10.9% | 30.6% | 10.5% |
| FC | Austin Hedges | 11 | 0.333 | 0.667 | 0.333 | 0.427 | 0.097 | 0.0% | 11.8% | 27.6% |
| FC | Brayan Rocchio | 23 | 0.286 | 0.619 | 0.333 | 0.415 | 0.341 | 10.0% | 26.5% | 11.4% |
| FC | Kyle Manzardo | 24 | 0.211 | 0.526 | 0.316 | 0.358 | 0.339 | 13.3% | 39.5% | 21.7% |
| FC | David Fry | 12 | 0.200 | 0.500 | 0.300 | 0.358 | 0.342 | 14.3% | 6.7% | 32.0% |
| FC | José Ramírez | 35 | 0.250 | 0.531 | 0.281 | 0.384 | 0.309 | 7.7% | 32.2% | 14.1% |
| FC | Chase Delauter | 21 | 0.389 | 0.667 | 0.278 | 0.486 | 0.412 | 13.3% | 33.3% | 16.7% |
| FF | Daniel Schneemann | 64 | 0.211 | 0.474 | 0.263 | 0.330 | 0.352 | 15.8% | 21.2% | 23.5% |
| FC | Rhys Hoskins | 21 | 0.211 | 0.474 | 0.263 | 0.324 | 0.219 | 0.0% | 29.6% | 30.2% |
| SI | David Fry | 25 | 0.348 | 0.609 | 0.261 | 0.430 | 0.358 | 11.8% | 22.9% | 21.6% |
| FF | Travis Bazzana | 85 | 0.293 | 0.547 | 0.253 | 0.398 | 0.321 | 6.5% | 23.0% | 14.2% |
| ST | Brayan Rocchio | 14 | 0.167 | 0.417 | 0.250 | 0.371 | 0.286 | 9.1% | 12.5% | 22.7% |
| ST | Chase Delauter | 19 | 0.235 | 0.471 | 0.235 | 0.339 | 0.355 | 0.0% | 42.1% | 9.1% |
| FF | Angel Martínez | 64 | 0.179 | 0.411 | 0.232 | 0.305 | 0.318 | 11.1% | 19.2% | 11.1% |
| SI | Travis Bazzana | 48 | 0.308 | 0.538 | 0.231 | 0.424 | 0.396 | 8.3% | 32.8% | 15.9% |
| ST | Travis Bazzana | 13 | 0.154 | 0.385 | 0.231 | 0.223 | 0.230 | 12.5% | 18.2% | 29.4% |
| FF | Chase Delauter | 100 | 0.306 | 0.506 | 0.200 | 0.386 | 0.330 | 11.4% | 20.8% | 13.2% |
| FF | David Fry | 52 | 0.195 | 0.390 | 0.195 | 0.342 | 0.277 | 6.7% | 28.8% | 22.4% |
| FF | Rhys Hoskins | 72 | 0.211 | 0.404 | 0.193 | 0.354 | 0.307 | 7.5% | 26.4% | 22.8% |
| FC | Daniel Schneemann | 20 | 0.294 | 0.471 | 0.176 | 0.385 | 0.305 | 7.1% | 19.2% | 17.6% |
| FF | Brayan Rocchio | 97 | 0.325 | 0.494 | 0.169 | 0.391 | 0.369 | 2.8% | 21.3% | 15.2% |
| ST | Kyle Manzardo | 21 | 0.167 | 0.333 | 0.167 | 0.281 | 0.293 | 14.3% | 7.7% | 35.7% |
| SI | Bo Naylor | 15 | 0.462 | 0.615 | 0.154 | 0.500 | 0.343 | 0.0% | 31.0% | 3.2% |
| SI | Kyle Manzardo | 45 | 0.282 | 0.436 | 0.154 | 0.381 | 0.473 | 14.8% | 38.3% | 21.9% |
| FF | Kyle Manzardo | 84 | 0.260 | 0.411 | 0.151 | 0.345 | 0.309 | 10.6% | 19.4% | 25.4% |
| SI | Chase Delauter | 42 | 0.361 | 0.500 | 0.139 | 0.421 | 0.406 | 0.0% | 30.9% | 3.4% |
| SI | Rhys Hoskins | 57 | 0.196 | 0.326 | 0.130 | 0.315 | 0.323 | 13.2% | 32.8% | 20.9% |
| FC | Steven Kwan | 30 | 0.250 | 0.357 | 0.107 | 0.268 | 0.299 | 0.0% | 14.6% | 2.3% |


## Home Starting Pitcher: Gavin Williams

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1661 |
| Batted/Result Events | 431 |
| Hits Allowed | 91 |
| Walks | 32 |
| Strikeouts | 121 |
| Home Runs | 17 |
| K Event Rate | 28.1% |
| BB Event Rate | 7.4% |
| HR Event Rate | 3.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | CWS | 6.7 | 5 | 0 | 1 | 8 | 0 |
| 2026-06-17 | MIL | 8.0 | 7 | 2 | 2 | 4 | 2 |
| 2026-06-08 | CLE | 7.3 | 4 | 2 | 3 | 5 | 2 |
| 2026-06-03 | NYY | 7.0 | 4 | 2 | 1 | 6 | 2 |
| 2026-05-27 | CLE | 8.7 | 3 | 0 | 3 | 4 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 16.9% | 281 | 0.237 | 0.474 | 0.237 | 0.319 | 0.350 | 15.7% | 42.0% | 27.5% |
| CU | vs R | 4.6% | 77 | 0.105 | 0.105 | 0.000 | 0.142 | 0.114 | 0.0% | 28.6% | 28.6% |
| FC | vs L | 7.4% | 123 | 0.286 | 0.607 | 0.321 | 0.397 | 0.371 | 16.7% | 30.2% | 18.6% |
| FC | vs R | 1.9% | 32 | 0.375 | 1.125 | 0.750 | 0.630 | 0.628 | 28.6% | 36.4% | 38.9% |
| FF | vs L | 16.0% | 265 | 0.210 | 0.355 | 0.145 | 0.282 | 0.356 | 11.6% | 18.8% | 25.5% |
| FF | vs R | 7.3% | 121 | 0.259 | 0.444 | 0.185 | 0.373 | 0.359 | 10.0% | 32.4% | 27.6% |
| SI | vs L | 6.6% | 109 | 0.190 | 0.381 | 0.190 | 0.298 | 0.377 | 11.8% | 25.6% | 12.8% |
| SI | vs R | 11.6% | 192 | 0.300 | 0.400 | 0.100 | 0.335 | 0.419 | 15.0% | 43.5% | 10.6% |
| ST | vs L | 10.3% | 171 | 0.125 | 0.275 | 0.150 | 0.215 | 0.203 | 9.5% | 18.0% | 34.0% |
| ST | vs R | 15.6% | 259 | 0.241 | 0.444 | 0.204 | 0.312 | 0.281 | 6.7% | 22.9% | 53.9% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 95 | 5 | 1 | 8 | 0 |
| 2026-06-17 | 87 | 7 | 2 | 4 | 2 |
| 2026-06-08 | 90 | 4 | 3 | 5 | 2 |
| 2026-06-03 | 96 | 4 | 1 | 6 | 2 |
| 2026-05-27 | 94 | 3 | 2 | 4 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Rob Refsnyder | 7 | 0.333 | 1.333 | 1.000 | 0.586 | 0.596 | 33.3% | 25.0% | 20.0% |
| CU | J. P. Crawford | 12 | 0.273 | 0.818 | 0.545 | 0.467 | 0.325 | 28.6% | 31.2% | 21.7% |
| FC | Dominic Canzone | 15 | 0.364 | 0.909 | 0.545 | 0.570 | 0.504 | 20.0% | 18.2% | 20.7% |
| FC | Luke Raley | 28 | 0.333 | 0.875 | 0.542 | 0.559 | 0.427 | 16.7% | 32.3% | 25.5% |
| SI | Cal Raleigh | 15 | 0.455 | 0.909 | 0.455 | 0.560 | 0.582 | 40.0% | 30.0% | 14.3% |
| FF | Brendan Donovan | 41 | 0.323 | 0.774 | 0.452 | 0.498 | 0.326 | 8.0% | 31.1% | 15.0% |
| CU | Dominic Canzone | 19 | 0.294 | 0.706 | 0.412 | 0.445 | 0.378 | 27.3% | 47.1% | 34.5% |
| FF | Luke Raley | 82 | 0.286 | 0.657 | 0.371 | 0.442 | 0.445 | 24.5% | 33.7% | 33.1% |
| FF | Dominic Canzone | 65 | 0.300 | 0.667 | 0.367 | 0.426 | 0.451 | 20.4% | 40.7% | 16.5% |
| CU | Cole Young | 14 | 0.545 | 0.909 | 0.364 | 0.589 | 0.412 | 11.1% | 50.0% | 9.1% |
| CU | Randy Arozarena | 14 | 0.231 | 0.538 | 0.308 | 0.346 | 0.275 | 16.7% | 21.1% | 28.6% |
| FC | Leo Rivas | 11 | 0.300 | 0.600 | 0.300 | 0.405 | 0.189 | 0.0% | 0.0% | 21.4% |
| CU | Brendan Donovan | 10 | 0.429 | 0.714 | 0.286 | 0.550 | 0.494 | 20.0% | 33.3% | 25.0% |
| ST | Cole Young | 25 | 0.136 | 0.409 | 0.273 | 0.252 | 0.167 | 10.0% | 20.0% | 36.8% |
| CU | Luke Raley | 16 | 0.200 | 0.467 | 0.267 | 0.303 | 0.337 | 37.5% | 30.0% | 35.3% |
| ST | Josh Naylor | 18 | 0.250 | 0.500 | 0.250 | 0.358 | 0.339 | 9.1% | 46.7% | 34.8% |
| ST | Luke Raley | 16 | 0.250 | 0.500 | 0.250 | 0.316 | 0.196 | 12.5% | 18.2% | 53.8% |
| SI | Luke Raley | 26 | 0.250 | 0.500 | 0.250 | 0.325 | 0.384 | 21.1% | 27.0% | 25.5% |
| FC | Randy Arozarena | 22 | 0.350 | 0.600 | 0.250 | 0.432 | 0.397 | 5.3% | 30.0% | 17.3% |
| FC | Brendan Donovan | 14 | 0.667 | 0.889 | 0.222 | 0.636 | 0.564 | 10.0% | 33.3% | 0.0% |
| FF | Julio Rodríguez | 91 | 0.231 | 0.436 | 0.205 | 0.342 | 0.348 | 13.0% | 26.0% | 26.2% |
| ST | Randy Arozarena | 39 | 0.229 | 0.429 | 0.200 | 0.322 | 0.339 | 10.7% | 23.4% | 13.8% |
| FF | Randy Arozarena | 106 | 0.244 | 0.430 | 0.186 | 0.360 | 0.393 | 17.5% | 27.5% | 30.5% |
| FF | J. P. Crawford | 96 | 0.239 | 0.423 | 0.183 | 0.391 | 0.416 | 9.1% | 15.6% | 14.6% |
| FF | Josh Naylor | 104 | 0.309 | 0.489 | 0.181 | 0.380 | 0.356 | 5.7% | 21.3% | 7.1% |
| SI | Mitch Garver | 29 | 0.217 | 0.391 | 0.174 | 0.381 | 0.372 | 5.6% | 38.7% | 10.8% |
| FC | Cal Raleigh | 22 | 0.111 | 0.278 | 0.167 | 0.259 | 0.314 | 8.3% | 23.3% | 32.9% |
| SI | Julio Rodríguez | 97 | 0.293 | 0.446 | 0.152 | 0.366 | 0.367 | 8.5% | 34.4% | 7.5% |
| CU | Julio Rodríguez | 22 | 0.200 | 0.350 | 0.150 | 0.277 | 0.372 | 16.7% | 30.0% | 48.9% |
| FF | Cole Young | 128 | 0.228 | 0.377 | 0.149 | 0.304 | 0.321 | 7.3% | 24.0% | 15.3% |


## Seattle Mariners Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Julio Rodríguez | 377 | 0.252 | 0.426 | 0.174 | 0.329 | 0.350 | 9.4% | 29.2% | 25.6% |
| Cole Young | 360 | 0.248 | 0.377 | 0.129 | 0.308 | 0.328 | 5.7% | 24.5% | 17.8% |
| Josh Naylor | 348 | 0.253 | 0.362 | 0.109 | 0.306 | 0.322 | 4.8% | 26.2% | 16.7% |
| Randy Arozarena | 346 | 0.285 | 0.456 | 0.171 | 0.375 | 0.348 | 8.1% | 24.7% | 24.7% |
| J. P. Crawford | 277 | 0.219 | 0.369 | 0.150 | 0.320 | 0.338 | 7.8% | 21.9% | 15.5% |
| Luke Raley | 249 | 0.250 | 0.513 | 0.263 | 0.364 | 0.357 | 17.7% | 29.1% | 38.8% |
| Cal Raleigh | 242 | 0.170 | 0.321 | 0.151 | 0.263 | 0.290 | 11.7% | 23.7% | 30.7% |
| Dominic Canzone | 227 | 0.282 | 0.559 | 0.277 | 0.386 | 0.384 | 15.7% | 31.2% | 25.9% |
| Leo Rivas | 140 | 0.132 | 0.167 | 0.035 | 0.231 | 0.238 | 2.6% | 9.7% | 23.9% |
| Rob Refsnyder | 136 | 0.127 | 0.212 | 0.085 | 0.200 | 0.249 | 7.2% | 22.6% | 25.2% |
| Mitch Garver | 131 | 0.189 | 0.324 | 0.135 | 0.308 | 0.303 | 7.4% | 29.1% | 34.7% |
| Brendan Donovan | 127 | 0.311 | 0.505 | 0.194 | 0.399 | 0.345 | 5.8% | 27.8% | 17.9% |


## Cleveland Guardians Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| José Ramírez | 329 | 0.247 | 0.452 | 0.205 | 0.352 | 0.355 | 7.9% | 30.6% | 15.1% |
| Steven Kwan | 329 | 0.204 | 0.258 | 0.055 | 0.279 | 0.302 | 0.4% | 7.7% | 7.0% |
| Brayan Rocchio | 317 | 0.268 | 0.393 | 0.125 | 0.333 | 0.310 | 2.9% | 21.5% | 21.1% |
| Chase Delauter | 290 | 0.281 | 0.453 | 0.172 | 0.358 | 0.341 | 6.9% | 25.7% | 13.4% |
| Kyle Manzardo | 283 | 0.234 | 0.403 | 0.169 | 0.326 | 0.315 | 12.1% | 24.1% | 29.3% |
| Angel Martínez | 260 | 0.247 | 0.469 | 0.222 | 0.322 | 0.306 | 8.9% | 23.8% | 16.8% |
| Rhys Hoskins | 252 | 0.190 | 0.390 | 0.200 | 0.321 | 0.283 | 11.2% | 28.0% | 28.2% |
| Daniel Schneemann | 243 | 0.208 | 0.344 | 0.136 | 0.282 | 0.292 | 7.4% | 22.8% | 30.1% |
| Travis Bazzana | 233 | 0.276 | 0.478 | 0.202 | 0.370 | 0.313 | 5.8% | 24.1% | 24.8% |
| David Fry | 145 | 0.218 | 0.387 | 0.169 | 0.326 | 0.270 | 7.2% | 22.2% | 28.5% |
| Austin Hedges | 127 | 0.266 | 0.358 | 0.092 | 0.330 | 0.290 | 3.3% | 21.6% | 23.4% |
| Bo Naylor | 108 | 0.152 | 0.242 | 0.091 | 0.207 | 0.295 | 9.7% | 24.3% | 14.9% |


## Bullpen Fatigue Report

### Seattle Mariners Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alex Hoppe | 2026-06-24 | 1.0 | 22 |
| Alex Hoppe | 2026-06-25 | 1.0 | 20 |
| Andrés Muñoz | 2026-06-26 | 1.0 | 15 |
| Eduard Bazardo | 2026-06-25 | 1.0 | 8 |
| Gabe Speier | 2026-06-25 | 0.1 | 1 |
| Gabe Speier | 2026-06-26 | 1.0 | 9 |
| José A. Ferrer | 2026-06-26 | 1.0 | 11 |
| José A. Ferrer | 2026-06-27 | 1.0 | 10 |
| Michael Rucker | 2026-06-24 | 2.0 | 26 |
| Nick Davila | 2026-06-24 | 1.0 | 24 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** José A. Ferrer


### Cleveland Guardians Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Cade Smith | 2026-06-24 | 0.2 | 28 |
| Cade Smith | 2026-06-27 | 1.0 | 14 |
| Colin Holderman | 2026-06-24 | 0.1 | 3 |
| Colin Holderman | 2026-06-27 | 0.2 | 14 |
| Daniel Espino | 2026-06-26 | 0.1 | 18 |
| Erik Sabrowski | 2026-06-24 | 0.2 | 15 |
| Erik Sabrowski | 2026-06-27 | 0.1 | 8 |
| Hunter Gaddis | 2026-06-24 | 0.2 | 13 |
| Hunter Gaddis | 2026-06-26 | 0.2 | 8 |
| Hunter Gaddis | 2026-06-27 | 1.0 | 14 |
| Matt Festa | 2026-06-26 | 1.0 | 18 |
| Shawn Armstrong | 2026-06-24 | 1.1 | 26 |
| Shawn Armstrong | 2026-06-27 | 0.0 | 10 |
| Tim Herrin | 2026-06-24 | 0.1 | 6 |
| Tim Herrin | 2026-06-26 | 1.0 | 23 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Cade Smith, Colin Holderman, Erik Sabrowski, Hunter Gaddis, Shawn Armstrong



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Julio Rodríguez | 377 | 0.252 | 0.426 | 0.174 | 0.329 | 9.4% | 29.2% |
| 2 | Cole Young | 360 | 0.248 | 0.377 | 0.129 | 0.308 | 5.7% | 24.5% |
| 3 | Josh Naylor | 348 | 0.253 | 0.362 | 0.109 | 0.306 | 4.8% | 26.2% |
| 4 | Randy Arozarena | 346 | 0.285 | 0.456 | 0.171 | 0.375 | 8.1% | 24.7% |
| 5 | J. P. Crawford | 277 | 0.219 | 0.369 | 0.150 | 0.320 | 7.8% | 21.9% |
| 6 | Luke Raley | 249 | 0.250 | 0.513 | 0.263 | 0.364 | 17.7% | 29.1% |
| 7 | Cal Raleigh | 242 | 0.170 | 0.321 | 0.151 | 0.263 | 11.7% | 23.7% |
| 8 | Dominic Canzone | 227 | 0.282 | 0.559 | 0.277 | 0.386 | 15.7% | 31.2% |
| 9 | Leo Rivas | 140 | 0.132 | 0.167 | 0.035 | 0.231 | 2.6% | 9.7% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | José Ramírez | 329 | 0.247 | 0.452 | 0.205 | 0.352 | 7.9% | 30.6% |
| 2 | Steven Kwan | 329 | 0.204 | 0.258 | 0.055 | 0.279 | 0.4% | 7.7% |
| 3 | Brayan Rocchio | 317 | 0.268 | 0.393 | 0.125 | 0.333 | 2.9% | 21.5% |
| 4 | Chase Delauter | 290 | 0.281 | 0.453 | 0.172 | 0.358 | 6.9% | 25.7% |
| 5 | Kyle Manzardo | 283 | 0.234 | 0.403 | 0.169 | 0.326 | 12.1% | 24.1% |
| 6 | Angel Martínez | 260 | 0.247 | 0.469 | 0.222 | 0.322 | 8.9% | 23.8% |
| 7 | Rhys Hoskins | 252 | 0.190 | 0.390 | 0.200 | 0.321 | 11.2% | 28.0% |
| 8 | Daniel Schneemann | 243 | 0.208 | 0.344 | 0.136 | 0.282 | 7.4% | 22.8% |
| 9 | Travis Bazzana | 233 | 0.276 | 0.478 | 0.202 | 0.370 | 5.8% | 24.1% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6955 |
| Hits Allowed | 1487 |
| Walks/HBP | 651 |
| Strikeouts | 1621 |
| Home Runs Allowed | 209 |
| K Event Rate | 23.3% |
| BB/HBP Event Rate | 9.4% |
| HR Event Rate | 3.0% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6919 |
| Hits Allowed | 1453 |
| Walks/HBP | 697 |
| Strikeouts | 1606 |
| Home Runs Allowed | 212 |
| K Event Rate | 23.2% |
| BB/HBP Event Rate | 10.1% |
| HR Event Rate | 3.1% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SI, ST, FC
- Home pitcher pitch mix to inspect: ST, FF, CU, SI, FC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 6. Arizona Diamondbacks @ Tampa Bay Rays

## Game Context

| Field | Value |
| --- | --- |
| Park | Tropicana Field |
| Time | 2026-06-28T17:40:00Z |
| Away Team | Arizona Diamondbacks |
| Home Team | Tampa Bay Rays |
| Away Probable Pitcher | Merrill Kelly |
| Home Probable Pitcher | Drew Rasmussen |


## Away Starting Pitcher: Merrill Kelly

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1292 |
| Batted/Result Events | 361 |
| Hits Allowed | 93 |
| Walks | 33 |
| Strikeouts | 45 |
| Home Runs | 17 |
| K Event Rate | 12.5% |
| BB Event Rate | 9.1% |
| HR Event Rate | 4.7% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | STL | 8.7 | 7 | 0 | 3 | 2 | 0 |
| 2026-06-16 | AZ | 9.0 | 11 | 2 | 1 | 4 | 2 |
| 2026-06-11 | MIA | 7.7 | 4 | 0 | 2 | 1 | 0 |
| 2026-06-05 | AZ | 8.3 | 6 | 3 | 4 | 4 | 3 |
| 2026-05-31 | SEA | 9.0 | 8 | 2 | 3 | 2 | 2 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 19.7% | 254 | 0.279 | 0.397 | 0.118 | 0.346 | 0.419 | 13.8% | 30.8% | 25.0% |
| CH | vs R | 5.7% | 73 | 0.167 | 0.292 | 0.125 | 0.208 | 0.298 | 18.8% | 34.5% | 29.4% |
| CU | vs L | 8.5% | 110 | 0.143 | 0.429 | 0.286 | 0.274 | 0.317 | 15.8% | 33.3% | 10.8% |
| CU | vs R | 3.0% | 39 | 0.250 | 0.375 | 0.125 | 0.269 | 0.194 | 0.0% | 25.0% | 35.7% |
| FC | vs L | 8.7% | 113 | 0.419 | 1.000 | 0.581 | 0.618 | 0.401 | 15.4% | 45.7% | 7.3% |
| FC | vs R | 6.3% | 82 | 0.381 | 0.619 | 0.238 | 0.452 | 0.490 | 15.0% | 23.3% | 19.5% |
| FF | vs L | 18.4% | 238 | 0.306 | 0.653 | 0.347 | 0.439 | 0.528 | 20.0% | 34.1% | 12.1% |
| FF | vs R | 7.5% | 97 | 0.333 | 0.476 | 0.143 | 0.435 | 0.443 | 4.8% | 17.5% | 10.6% |
| PO | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| PO | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs L | 3.1% | 40 | 0.222 | 0.333 | 0.111 | 0.323 | 0.349 | 14.3% | 18.8% | 0.0% |
| SI | vs R | 6.8% | 88 | 0.348 | 0.609 | 0.261 | 0.392 | 0.467 | 13.6% | 37.8% | 8.9% |
| SL | vs L | 1.4% | 18 | 0.250 | 0.500 | 0.250 | 0.325 | 0.490 | 25.0% | 11.1% | 16.7% |
| SL | vs R | 10.4% | 134 | 0.256 | 0.395 | 0.140 | 0.309 | 0.256 | 8.6% | 21.7% | 35.1% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 96 | 7 | 3 | 2 | 0 |
| 2026-06-16 | 88 | 11 | 1 | 4 | 2 |
| 2026-06-11 | 74 | 4 | 2 | 1 | 0 |
| 2026-06-05 | 85 | 6 | 3 | 4 | 3 |
| 2026-05-31 | 97 | 8 | 2 | 2 | 2 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Ryan Vilade | 12 | 0.182 | 0.727 | 0.545 | 0.558 | 0.743 | 20.0% | 41.2% | 37.9% |
| CU | Jonathan Aranda | 17 | 0.333 | 0.733 | 0.400 | 0.435 | 0.456 | 33.3% | 40.9% | 26.5% |
| FF | Junior Caminero | 79 | 0.348 | 0.682 | 0.333 | 0.478 | 0.466 | 18.4% | 42.1% | 19.9% |
| FC | Ryan Vilade | 14 | 0.417 | 0.750 | 0.333 | 0.525 | 0.459 | 10.0% | 33.3% | 12.0% |
| FC | Ben Williamson | 18 | 0.308 | 0.615 | 0.308 | 0.486 | 0.387 | 8.3% | 24.1% | 14.3% |
| CU | Junior Caminero | 22 | 0.150 | 0.450 | 0.300 | 0.286 | 0.286 | 20.0% | 33.3% | 34.4% |
| SL | Yandy Díaz | 57 | 0.438 | 0.729 | 0.292 | 0.518 | 0.517 | 19.1% | 34.2% | 11.4% |
| SL | Jonny Deluca | 18 | 0.278 | 0.556 | 0.278 | 0.350 | 0.287 | 6.7% | 20.0% | 35.3% |
| CH | Yandy Díaz | 36 | 0.273 | 0.545 | 0.273 | 0.354 | 0.339 | 3.6% | 35.6% | 14.3% |
| CU | Ryan Vilade | 11 | 0.364 | 0.636 | 0.273 | 0.427 | 0.382 | 11.1% | 33.3% | 11.8% |
| SL | Jonathan Aranda | 42 | 0.243 | 0.514 | 0.270 | 0.363 | 0.303 | 11.5% | 30.2% | 18.5% |
| CH | Cedric Mullins | 24 | 0.261 | 0.522 | 0.261 | 0.346 | 0.372 | 14.3% | 22.2% | 11.6% |
| SL | Richie Palacios | 24 | 0.261 | 0.522 | 0.261 | 0.342 | 0.357 | 5.9% | 17.2% | 20.5% |
| FC | Chandler Simpson | 21 | 0.312 | 0.562 | 0.250 | 0.414 | 0.320 | 0.0% | 11.1% | 6.5% |
| SI | Junior Caminero | 82 | 0.362 | 0.609 | 0.246 | 0.461 | 0.375 | 11.7% | 36.7% | 12.5% |
| FC | Jonny Deluca | 13 | 0.385 | 0.615 | 0.231 | 0.431 | 0.347 | 7.7% | 11.1% | 14.3% |
| FC | Junior Caminero | 24 | 0.389 | 0.611 | 0.222 | 0.469 | 0.429 | 23.5% | 25.0% | 6.1% |
| SI | Jonny Deluca | 38 | 0.333 | 0.556 | 0.222 | 0.407 | 0.334 | 3.1% | 25.0% | 14.5% |
| FC | Richie Palacios | 15 | 0.333 | 0.533 | 0.200 | 0.373 | 0.334 | 8.3% | 23.8% | 15.4% |
| CH | Jonathan Aranda | 34 | 0.250 | 0.438 | 0.188 | 0.316 | 0.289 | 4.2% | 14.3% | 17.3% |
| SL | Chandler Simpson | 32 | 0.333 | 0.500 | 0.167 | 0.381 | 0.265 | 0.0% | 20.6% | 19.1% |
| FF | Jonathan Aranda | 136 | 0.257 | 0.422 | 0.165 | 0.357 | 0.382 | 11.1% | 22.6% | 19.9% |
| SI | Ryan Vilade | 38 | 0.194 | 0.355 | 0.161 | 0.300 | 0.258 | 0.0% | 25.9% | 8.3% |
| FF | Yandy Díaz | 89 | 0.220 | 0.378 | 0.159 | 0.290 | 0.284 | 6.8% | 22.6% | 16.1% |
| SL | Junior Caminero | 59 | 0.193 | 0.351 | 0.158 | 0.247 | 0.306 | 12.8% | 39.4% | 21.2% |
| FF | Hunter Feduccia | 46 | 0.154 | 0.308 | 0.154 | 0.271 | 0.335 | 24.0% | 20.3% | 15.6% |
| SI | Jonathan Aranda | 54 | 0.348 | 0.500 | 0.152 | 0.404 | 0.379 | 5.6% | 28.8% | 11.6% |
| FF | Nick Fortes | 62 | 0.268 | 0.411 | 0.143 | 0.331 | 0.275 | 4.3% | 31.9% | 8.8% |
| FF | Cedric Mullins | 107 | 0.185 | 0.326 | 0.141 | 0.276 | 0.275 | 5.6% | 22.8% | 21.3% |
| SL | Cedric Mullins | 29 | 0.136 | 0.273 | 0.136 | 0.276 | 0.255 | 0.0% | 11.4% | 22.0% |


## Home Starting Pitcher: Drew Rasmussen

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1390 |
| Batted/Result Events | 360 |
| Hits Allowed | 72 |
| Walks | 17 |
| Strikeouts | 92 |
| Home Runs | 12 |
| K Event Rate | 25.6% |
| BB Event Rate | 4.7% |
| HR Event Rate | 3.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | TB | 8.0 | 4 | 0 | 2 | 5 | 0 |
| 2026-06-16 | LAD | 8.7 | 6 | 1 | 0 | 7 | 1 |
| 2026-06-10 | TB | 8.0 | 2 | 0 | 2 | 13 | 0 |
| 2026-06-05 | MIA | 7.3 | 1 | 0 | 0 | 9 | 0 |
| 2026-05-30 | TB | 6.0 | 4 | 1 | 2 | 4 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 9.1% | 127 | 0.200 | 0.200 | 0.000 | 0.210 | 0.234 | 5.0% | 29.0% | 42.6% |
| CH | vs R | 1.7% | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.044 | 0.0% | 0.0% | 53.8% |
| CU | vs L | 4.4% | 61 | 0.100 | 0.100 | 0.000 | 0.090 | 0.272 | 14.3% | 15.4% | 18.8% |
| CU | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.219 | 0.0% | 100.0% | 0.0% |
| FC | vs L | 19.6% | 273 | 0.253 | 0.405 | 0.152 | 0.321 | 0.315 | 4.7% | 24.6% | 22.6% |
| FC | vs R | 12.7% | 177 | 0.140 | 0.163 | 0.023 | 0.167 | 0.264 | 9.7% | 14.0% | 27.3% |
| FF | vs L | 18.9% | 263 | 0.362 | 0.603 | 0.241 | 0.445 | 0.348 | 9.5% | 19.4% | 20.3% |
| FF | vs R | 8.3% | 115 | 0.095 | 0.286 | 0.190 | 0.202 | 0.223 | 8.3% | 21.6% | 23.3% |
| SI | vs L | 7.6% | 106 | 0.091 | 0.227 | 0.136 | 0.157 | 0.187 | 15.4% | 30.8% | 15.2% |
| SI | vs R | 14.4% | 200 | 0.175 | 0.298 | 0.123 | 0.280 | 0.224 | 4.3% | 23.8% | 9.8% |
| ST | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.482 | 0.0% | 0.0% | 0.0% |
| ST | vs R | 3.0% | 42 | 0.364 | 0.727 | 0.364 | 0.459 | 0.413 | 20.0% | 35.7% | 11.1% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 90 | 4 | 2 | 5 | 0 |
| 2026-06-16 | 102 | 6 | 0 | 7 | 1 |
| 2026-06-10 | 97 | 2 | 1 | 13 | 0 |
| 2026-06-05 | 87 | 1 | 0 | 9 | 0 |
| 2026-05-30 | 70 | 4 | 2 | 4 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | Alek Thomas | 11 | 0.364 | 0.909 | 0.545 | 0.523 | 0.281 | 12.5% | 22.2% | 25.9% |
| SI | Jorge Barrosa | 16 | 0.417 | 0.833 | 0.417 | 0.569 | 0.375 | 33.3% | 31.2% | 20.0% |
| FC | Jorge Barrosa | 11 | 0.300 | 0.700 | 0.400 | 0.395 | 0.206 | 28.6% | 28.6% | 38.5% |
| FC | Nolan Arenado | 19 | 0.375 | 0.750 | 0.375 | 0.508 | 0.413 | 7.7% | 32.0% | 26.3% |
| CH | Corbin Carroll | 43 | 0.225 | 0.600 | 0.375 | 0.363 | 0.358 | 11.4% | 31.4% | 24.0% |
| CH | Jorge Barrosa | 14 | 0.364 | 0.727 | 0.364 | 0.439 | 0.420 | 8.3% | 15.0% | 16.0% |
| FC | Ildemaro Vargas | 16 | 0.571 | 0.929 | 0.357 | 0.650 | 0.421 | 7.1% | 18.2% | 5.4% |
| SI | Ketel Marte | 50 | 0.435 | 0.783 | 0.348 | 0.532 | 0.500 | 19.5% | 39.4% | 2.7% |
| SI | Alek Thomas | 10 | 0.333 | 0.667 | 0.333 | 0.450 | 0.333 | 12.5% | 21.4% | 19.0% |
| SI | Ildemaro Vargas | 36 | 0.382 | 0.706 | 0.324 | 0.461 | 0.413 | 11.8% | 41.3% | 4.1% |
| FC | Corbin Carroll | 24 | 0.318 | 0.636 | 0.318 | 0.465 | 0.440 | 11.1% | 38.2% | 25.5% |
| FF | Gabriel Moreno | 69 | 0.264 | 0.547 | 0.283 | 0.404 | 0.401 | 12.2% | 25.5% | 14.8% |
| FC | Jose Fernandez | 14 | 0.364 | 0.636 | 0.273 | 0.450 | 0.371 | 9.1% | 22.7% | 16.1% |
| FF | Corbin Carroll | 112 | 0.213 | 0.483 | 0.270 | 0.376 | 0.360 | 17.2% | 24.6% | 31.2% |
| FF | Nolan Arenado | 83 | 0.270 | 0.527 | 0.257 | 0.367 | 0.383 | 10.8% | 24.3% | 12.2% |
| FF | Geraldo Perdomo | 119 | 0.312 | 0.548 | 0.237 | 0.430 | 0.379 | 4.7% | 22.6% | 9.6% |
| FF | Ketel Marte | 115 | 0.223 | 0.447 | 0.223 | 0.335 | 0.398 | 16.1% | 31.4% | 7.6% |
| CH | Lourdes Gurriel | 19 | 0.158 | 0.368 | 0.211 | 0.218 | 0.161 | 0.0% | 17.6% | 43.8% |
| SI | Nolan Arenado | 57 | 0.367 | 0.571 | 0.204 | 0.437 | 0.339 | 10.9% | 32.9% | 11.9% |
| SI | Adrian Del Castillo | 30 | 0.240 | 0.440 | 0.200 | 0.387 | 0.393 | 13.6% | 23.1% | 12.5% |
| FF | Alek Thomas | 33 | 0.226 | 0.419 | 0.194 | 0.326 | 0.311 | 8.7% | 25.0% | 22.4% |
| SI | Gabriel Moreno | 44 | 0.389 | 0.583 | 0.194 | 0.475 | 0.404 | 5.7% | 26.6% | 1.4% |
| SI | Corbin Carroll | 46 | 0.452 | 0.643 | 0.190 | 0.493 | 0.374 | 8.6% | 33.9% | 21.8% |
| CH | Ildemaro Vargas | 45 | 0.262 | 0.429 | 0.167 | 0.347 | 0.322 | 2.5% | 33.3% | 16.0% |
| FF | Jorge Barrosa | 61 | 0.125 | 0.286 | 0.161 | 0.204 | 0.163 | 2.3% | 17.1% | 20.2% |
| CH | Gabriel Moreno | 26 | 0.280 | 0.440 | 0.160 | 0.325 | 0.371 | 14.3% | 30.8% | 13.5% |
| FF | Adrian Del Castillo | 47 | 0.200 | 0.356 | 0.156 | 0.276 | 0.263 | 9.4% | 21.1% | 25.7% |
| FF | Ryan Waldschmidt | 29 | 0.231 | 0.385 | 0.154 | 0.362 | 0.358 | 17.6% | 17.9% | 20.8% |
| FC | Alek Thomas | 8 | 0.143 | 0.286 | 0.143 | 0.244 | 0.501 | 28.6% | 30.8% | 0.0% |
| FC | Ryan Waldschmidt | 19 | 0.375 | 0.500 | 0.125 | 0.432 | 0.378 | 0.0% | 18.2% | 17.9% |


## Arizona Diamondbacks Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ketel Marte | 353 | 0.261 | 0.460 | 0.199 | 0.340 | 0.371 | 11.3% | 34.6% | 18.8% |
| Corbin Carroll | 352 | 0.273 | 0.529 | 0.256 | 0.386 | 0.361 | 13.2% | 31.1% | 27.2% |
| Geraldo Perdomo | 346 | 0.246 | 0.363 | 0.116 | 0.336 | 0.335 | 3.2% | 21.7% | 10.7% |
| Nolan Arenado | 309 | 0.245 | 0.405 | 0.161 | 0.324 | 0.303 | 6.4% | 22.8% | 20.3% |
| Ildemaro Vargas | 283 | 0.261 | 0.417 | 0.155 | 0.331 | 0.314 | 3.8% | 26.5% | 12.3% |
| Gabriel Moreno | 229 | 0.286 | 0.474 | 0.189 | 0.379 | 0.372 | 9.9% | 27.2% | 15.6% |
| Jose Fernandez | 178 | 0.253 | 0.349 | 0.096 | 0.301 | 0.276 | 3.9% | 24.7% | 23.3% |
| Adrian Del Castillo | 154 | 0.184 | 0.298 | 0.113 | 0.256 | 0.258 | 6.2% | 20.4% | 25.0% |
| Jorge Barrosa | 141 | 0.210 | 0.427 | 0.218 | 0.311 | 0.211 | 7.9% | 18.1% | 24.8% |
| Lourdes Gurriel | 136 | 0.216 | 0.288 | 0.072 | 0.249 | 0.274 | 4.9% | 20.7% | 21.5% |
| Ryan Waldschmidt | 131 | 0.273 | 0.380 | 0.107 | 0.327 | 0.289 | 7.6% | 22.1% | 29.0% |
| Alek Thomas | 117 | 0.193 | 0.394 | 0.202 | 0.280 | 0.292 | 9.9% | 27.6% | 23.7% |


## Tampa Bay Rays Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Junior Caminero | 368 | 0.279 | 0.517 | 0.238 | 0.380 | 0.367 | 13.5% | 36.4% | 21.0% |
| Jonathan Aranda | 364 | 0.284 | 0.467 | 0.183 | 0.371 | 0.369 | 10.2% | 25.3% | 19.3% |
| Yandy Díaz | 362 | 0.340 | 0.514 | 0.175 | 0.410 | 0.372 | 8.3% | 30.5% | 11.7% |
| Chandler Simpson | 325 | 0.268 | 0.325 | 0.056 | 0.298 | 0.254 | 0.0% | 9.2% | 8.2% |
| Cedric Mullins | 291 | 0.206 | 0.325 | 0.119 | 0.293 | 0.267 | 4.1% | 20.4% | 20.3% |
| Taylor Walls | 227 | 0.221 | 0.289 | 0.068 | 0.295 | 0.259 | 4.3% | 12.8% | 20.7% |
| Ben Williamson | 209 | 0.239 | 0.330 | 0.090 | 0.294 | 0.298 | 1.4% | 24.6% | 15.6% |
| Nick Fortes | 207 | 0.246 | 0.330 | 0.084 | 0.282 | 0.272 | 3.0% | 29.5% | 13.6% |
| Richie Palacios | 205 | 0.220 | 0.294 | 0.073 | 0.290 | 0.304 | 3.6% | 16.2% | 19.3% |
| Jonny Deluca | 165 | 0.263 | 0.423 | 0.160 | 0.321 | 0.280 | 4.0% | 20.5% | 22.8% |
| Ryan Vilade | 157 | 0.266 | 0.453 | 0.187 | 0.357 | 0.309 | 4.5% | 21.1% | 17.5% |
| Hunter Feduccia | 128 | 0.205 | 0.268 | 0.062 | 0.255 | 0.305 | 8.6% | 19.4% | 23.7% |


## Bullpen Fatigue Report

### Arizona Diamondbacks Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Drey Jameson | 2026-06-24 | 2.0 | 29 |
| Jonathan Loáisiga | 2026-06-24 | 1.0 | 16 |
| Juan Burgos | 2026-06-26 | 1.1 | 20 |
| Juan Morillo | 2026-06-27 | 1.0 | 23 |
| Kevin Ginkel | 2026-06-27 | 1.0 | 13 |
| Ryan Thompson | 2026-06-24 | 2.0 | 21 |
| Taylor Clarke | 2026-06-24 | 1.0 | 10 |
| Taylor Clarke | 2026-06-27 | 1.0 | 6 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Juan Morillo, Kevin Ginkel, Taylor Clarke


### Tampa Bay Rays Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Bryan Baker | 2026-06-24 | 1.0 | 17 |
| Bryan Baker | 2026-06-27 | 1.0 | 10 |
| Cam Booser | 2026-06-26 | 0.1 | 5 |
| Casey Legumina | 2026-06-27 | 1.2 | 35 |
| Cole Sulser | 2026-06-24 | 1.0 | 14 |
| Craig Kimbrel | 2026-06-25 | 1.0 | 25 |
| Craig Kimbrel | 2026-06-26 | 1.0 | 22 |
| Garrett Cleavinger | 2026-06-24 | 1.0 | 13 |
| Garrett Cleavinger | 2026-06-26 | 1.0 | 12 |
| Ian Seymour | 2026-06-25 | 6.2 | 90 |
| Kevin Kelly | 2026-06-24 | 1.0 | 15 |
| Kevin Kelly | 2026-06-26 | 1.0 | 13 |
| Kevin Kelly | 2026-06-27 | 1.1 | 20 |
| Michael Grove | 2026-06-27 | 3.0 | 34 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Bryan Baker, Casey Legumina, Kevin Kelly, Michael Grove



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Ketel Marte | 353 | 0.261 | 0.460 | 0.199 | 0.340 | 11.3% | 34.6% |
| 2 | Corbin Carroll | 352 | 0.273 | 0.529 | 0.256 | 0.386 | 13.2% | 31.1% |
| 3 | Geraldo Perdomo | 346 | 0.246 | 0.363 | 0.116 | 0.336 | 3.2% | 21.7% |
| 4 | Nolan Arenado | 309 | 0.245 | 0.405 | 0.161 | 0.324 | 6.4% | 22.8% |
| 5 | Ildemaro Vargas | 283 | 0.261 | 0.417 | 0.155 | 0.331 | 3.8% | 26.5% |
| 6 | Gabriel Moreno | 229 | 0.286 | 0.474 | 0.189 | 0.379 | 9.9% | 27.2% |
| 7 | Jose Fernandez | 178 | 0.253 | 0.349 | 0.096 | 0.301 | 3.9% | 24.7% |
| 8 | Adrian Del Castillo | 154 | 0.184 | 0.298 | 0.113 | 0.256 | 6.2% | 20.4% |
| 9 | Jorge Barrosa | 141 | 0.210 | 0.427 | 0.218 | 0.311 | 7.9% | 18.1% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Junior Caminero | 368 | 0.279 | 0.517 | 0.238 | 0.380 | 13.5% | 36.4% |
| 2 | Jonathan Aranda | 364 | 0.284 | 0.467 | 0.183 | 0.371 | 10.2% | 25.3% |
| 3 | Yandy Díaz | 362 | 0.340 | 0.514 | 0.175 | 0.410 | 8.3% | 30.5% |
| 4 | Chandler Simpson | 325 | 0.268 | 0.325 | 0.056 | 0.298 | 0.0% | 9.2% |
| 5 | Cedric Mullins | 291 | 0.206 | 0.325 | 0.119 | 0.293 | 4.1% | 20.4% |
| 6 | Taylor Walls | 227 | 0.221 | 0.289 | 0.068 | 0.295 | 4.3% | 12.8% |
| 7 | Ben Williamson | 209 | 0.239 | 0.330 | 0.090 | 0.294 | 1.4% | 24.6% |
| 8 | Nick Fortes | 207 | 0.246 | 0.330 | 0.084 | 0.282 | 3.0% | 29.5% |
| 9 | Richie Palacios | 205 | 0.220 | 0.294 | 0.073 | 0.290 | 3.6% | 16.2% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6827 |
| Hits Allowed | 1504 |
| Walks/HBP | 626 |
| Strikeouts | 1313 |
| Home Runs Allowed | 199 |
| K Event Rate | 19.2% |
| BB/HBP Event Rate | 9.2% |
| HR Event Rate | 2.9% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6691 |
| Hits Allowed | 1470 |
| Walks/HBP | 603 |
| Strikeouts | 1347 |
| Home Runs Allowed | 190 |
| K Event Rate | 20.1% |
| BB/HBP Event Rate | 9.0% |
| HR Event Rate | 2.8% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, CH, FC, SL, CU, SI
- Home pitcher pitch mix to inspect: FC, FF, SI, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 7. Philadelphia Phillies @ New York Mets

## Game Context

| Field | Value |
| --- | --- |
| Park | Citi Field |
| Time | 2026-06-28T17:40:00Z |
| Away Team | Philadelphia Phillies |
| Home Team | New York Mets |
| Away Probable Pitcher | Jesús Luzardo |
| Home Probable Pitcher | Cionel Pérez |


## Away Starting Pitcher: Jesús Luzardo

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1714 |
| Batted/Result Events | 438 |
| Hits Allowed | 103 |
| Walks | 33 |
| Strikeouts | 121 |
| Home Runs | 10 |
| K Event Rate | 27.6% |
| BB Event Rate | 7.5% |
| HR Event Rate | 2.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | WSH | 9.3 | 6 | 0 | 3 | 13 | 0 |
| 2026-06-16 | PHI | 9.3 | 5 | 1 | 2 | 9 | 1 |
| 2026-06-10 | TOR | 8.3 | 4 | 0 | 4 | 8 | 0 |
| 2026-06-05 | PHI | 9.0 | 7 | 3 | 3 | 2 | 3 |
| 2026-05-30 | LAD | 8.3 | 7 | 0 | 2 | 6 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.9% | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.094 | 0.0% | 0.0% | 27.3% |
| CH | vs R | 20.8% | 357 | 0.284 | 0.432 | 0.148 | 0.344 | 0.312 | 6.7% | 15.9% | 38.9% |
| FF | vs L | 2.9% | 49 | 0.100 | 0.100 | 0.000 | 0.177 | 0.282 | 16.7% | 23.1% | 18.8% |
| FF | vs R | 22.6% | 388 | 0.357 | 0.531 | 0.173 | 0.405 | 0.328 | 6.5% | 17.2% | 11.7% |
| SI | vs L | 8.1% | 138 | 0.316 | 0.421 | 0.105 | 0.350 | 0.264 | 2.7% | 26.9% | 9.7% |
| SI | vs R | 9.2% | 158 | 0.350 | 0.525 | 0.175 | 0.428 | 0.398 | 0.0% | 37.3% | 10.0% |
| SL | vs R | 0.4% | 6 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| ST | vs L | 9.8% | 168 | 0.150 | 0.225 | 0.075 | 0.176 | 0.188 | 5.3% | 10.3% | 53.5% |
| ST | vs R | 25.4% | 435 | 0.148 | 0.222 | 0.074 | 0.214 | 0.215 | 11.8% | 18.1% | 45.1% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 104 | 6 | 3 | 13 | 0 |
| 2026-06-16 | 106 | 5 | 2 | 9 | 1 |
| 2026-06-10 | 96 | 4 | 4 | 8 | 0 |
| 2026-06-05 | 90 | 7 | 2 | 2 | 3 |
| 2026-05-30 | 95 | 7 | 2 | 6 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | Jared Young | 14 | 0.167 | 0.667 | 0.500 | 0.400 | 0.511 | 25.0% | 40.9% | 21.9% |
| ST | Mj Melendez | 11 | 0.200 | 0.600 | 0.400 | 0.359 | 0.296 | 16.7% | 35.7% | 17.6% |
| ST | Juan Soto | 28 | 0.346 | 0.731 | 0.385 | 0.468 | 0.482 | 20.0% | 34.6% | 25.6% |
| FF | Juan Soto | 76 | 0.309 | 0.662 | 0.353 | 0.438 | 0.493 | 22.8% | 34.1% | 15.0% |
| ST | Bo Bichette | 37 | 0.257 | 0.543 | 0.286 | 0.336 | 0.343 | 15.4% | 20.0% | 32.5% |
| CH | Francisco Álvarez | 20 | 0.333 | 0.611 | 0.278 | 0.430 | 0.348 | 14.3% | 33.3% | 29.6% |
| SI | Marcus Semien | 78 | 0.275 | 0.536 | 0.261 | 0.359 | 0.395 | 10.2% | 29.0% | 11.3% |
| CH | Mark Vientos | 41 | 0.263 | 0.500 | 0.237 | 0.333 | 0.304 | 7.1% | 30.4% | 32.5% |
| FF | Mj Melendez | 58 | 0.184 | 0.408 | 0.224 | 0.309 | 0.243 | 6.9% | 24.0% | 32.6% |
| FF | A. J. Ewing | 50 | 0.220 | 0.439 | 0.220 | 0.357 | 0.421 | 15.2% | 25.3% | 9.2% |
| SI | Mark Vientos | 44 | 0.190 | 0.381 | 0.190 | 0.261 | 0.313 | 7.5% | 28.4% | 12.2% |
| FF | Francisco Lindor | 50 | 0.186 | 0.372 | 0.186 | 0.318 | 0.386 | 7.9% | 27.8% | 12.5% |
| CH | Luis Torrens | 12 | 0.273 | 0.455 | 0.182 | 0.300 | 0.233 | 0.0% | 27.3% | 15.8% |
| FF | Francisco Álvarez | 44 | 0.308 | 0.487 | 0.179 | 0.383 | 0.400 | 21.7% | 27.5% | 27.2% |
| SI | A. J. Ewing | 26 | 0.217 | 0.391 | 0.174 | 0.288 | 0.258 | 0.0% | 25.0% | 21.6% |
| FF | Marcus Semien | 90 | 0.205 | 0.372 | 0.167 | 0.291 | 0.353 | 14.3% | 29.1% | 17.6% |
| FF | Mark Vientos | 59 | 0.241 | 0.407 | 0.167 | 0.317 | 0.337 | 11.9% | 23.9% | 24.6% |
| SI | Luis Torrens | 34 | 0.233 | 0.400 | 0.167 | 0.321 | 0.345 | 3.7% | 23.1% | 8.1% |
| FF | Bo Bichette | 90 | 0.225 | 0.388 | 0.163 | 0.310 | 0.333 | 5.2% | 26.0% | 12.2% |
| FF | Carson Benge | 119 | 0.295 | 0.457 | 0.162 | 0.376 | 0.370 | 7.6% | 21.9% | 17.6% |
| CH | Carson Benge | 32 | 0.226 | 0.387 | 0.161 | 0.302 | 0.324 | 7.7% | 26.8% | 22.4% |
| FF | Jared Young | 38 | 0.242 | 0.394 | 0.152 | 0.329 | 0.410 | 19.2% | 21.1% | 14.9% |
| CH | Juan Soto | 28 | 0.333 | 0.481 | 0.148 | 0.366 | 0.405 | 7.7% | 36.8% | 4.5% |
| ST | Carson Benge | 22 | 0.238 | 0.381 | 0.143 | 0.286 | 0.281 | 10.0% | 24.1% | 32.7% |
| SI | Juan Soto | 57 | 0.286 | 0.429 | 0.143 | 0.376 | 0.401 | 15.9% | 37.5% | 13.3% |
| SI | Francisco Álvarez | 53 | 0.222 | 0.356 | 0.133 | 0.334 | 0.357 | 11.4% | 28.2% | 18.9% |
| CH | Francisco Lindor | 24 | 0.167 | 0.292 | 0.125 | 0.231 | 0.285 | 15.0% | 17.5% | 21.7% |
| CH | Marcus Semien | 21 | 0.333 | 0.444 | 0.111 | 0.390 | 0.440 | 15.4% | 16.7% | 31.7% |
| FF | Brett Baty | 103 | 0.215 | 0.312 | 0.097 | 0.284 | 0.288 | 12.7% | 22.8% | 19.6% |
| ST | Jared Young | 12 | 0.182 | 0.273 | 0.091 | 0.238 | 0.226 | 12.5% | 26.7% | 30.8% |


## Home Starting Pitcher: Cionel Pérez

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 531 |
| Batted/Result Events | 140 |
| Hits Allowed | 30 |
| Walks | 12 |
| Strikeouts | 28 |
| Home Runs | 5 |
| K Event Rate | 20.0% |
| BB Event Rate | 8.6% |
| HR Event Rate | 3.6% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-26 | NYM | 2.3 | 2 | 0 | 0 | 1 | 0 |
| 2026-06-23 | NYM | 2.3 | 0 | 0 | 0 | 1 | 0 |
| 2026-06-20 | PHI | 3.3 | 4 | 1 | 0 | 3 | 1 |
| 2026-06-16 | CIN | 2.0 | 3 | 0 | 0 | 2 | 0 |
| 2026-06-14 | NYM | 1.3 | 0 | 0 | 1 | 0 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 0.2% | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.594 | 100.0% | 100.0% | 0.0% |
| CU | vs R | 23.5% | 125 | 0.167 | 0.300 | 0.133 | 0.258 | 0.336 | 9.1% | 42.1% | 27.6% |
| FF | vs L | 3.4% | 18 | 0.333 | 0.333 | 0.000 | 0.300 | 0.472 | 0.0% | 16.7% | 20.0% |
| FF | vs R | 16.8% | 89 | 0.286 | 0.429 | 0.143 | 0.385 | 0.483 | 23.5% | 44.4% | 3.4% |
| SI | vs L | 21.7% | 115 | 0.185 | 0.407 | 0.222 | 0.306 | 0.433 | 16.0% | 34.1% | 11.3% |
| SI | vs R | 7.0% | 37 | 0.200 | 0.200 | 0.000 | 0.180 | 0.222 | 0.0% | 25.0% | 22.2% |
| SV | vs L | 19.6% | 104 | 0.296 | 0.407 | 0.111 | 0.341 | 0.295 | 5.0% | 22.9% | 26.5% |
| SV | vs R | 7.9% | 42 | 0.333 | 0.444 | 0.111 | 0.375 | 0.339 | 0.0% | 25.0% | 41.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-26 | 21 | 2 | 0 | 1 | 0 |
| 2026-06-23 | 29 | 0 | 0 | 1 | 0 |
| 2026-06-20 | 32 | 4 | 0 | 3 | 1 |
| 2026-06-16 | 26 | 3 | 0 | 2 | 0 |
| 2026-06-14 | 20 | 0 | 1 | 0 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SI | Otto Kemp | 6 | 0.333 | 1.333 | 1.000 | 0.667 | 0.102 | 40.0% | 21.4% | 5.9% |
| CU | Brandon Marsh | 20 | 0.444 | 1.056 | 0.611 | 0.630 | 0.405 | 15.4% | 27.3% | 23.9% |
| SV | Bryce Harper | 7 | 0.571 | 1.143 | 0.571 | 0.721 | 0.619 | 14.3% | 33.3% | 0.0% |
| SI | Kyle Schwarber | 58 | 0.391 | 0.891 | 0.500 | 0.584 | 0.544 | 23.7% | 36.1% | 16.3% |
| SV | Bryson Stott | 3 | 0.500 | 1.000 | 0.500 | 0.650 | 0.565 | 0.0% | 100.0% | 0.0% |
| FF | Bryce Harper | 88 | 0.310 | 0.732 | 0.423 | 0.477 | 0.471 | 14.3% | 27.7% | 21.2% |
| FF | Kyle Schwarber | 99 | 0.244 | 0.610 | 0.366 | 0.412 | 0.358 | 18.4% | 34.8% | 21.1% |
| FF | Edmundo Sosa | 43 | 0.421 | 0.763 | 0.342 | 0.493 | 0.474 | 17.1% | 27.2% | 14.4% |
| SI | Brandon Marsh | 51 | 0.370 | 0.630 | 0.261 | 0.472 | 0.442 | 9.5% | 31.8% | 6.7% |
| CU | Kyle Schwarber | 26 | 0.130 | 0.391 | 0.261 | 0.269 | 0.314 | 25.0% | 32.0% | 45.8% |
| CU | Adolis García | 13 | 0.250 | 0.500 | 0.250 | 0.346 | 0.374 | 25.0% | 41.7% | 50.0% |
| SI | Bryson Stott | 47 | 0.267 | 0.444 | 0.178 | 0.320 | 0.335 | 7.3% | 24.2% | 10.7% |
| FF | Rafael Marchán | 39 | 0.108 | 0.270 | 0.162 | 0.185 | 0.206 | 5.7% | 15.6% | 8.2% |
| SI | Trea Turner | 79 | 0.227 | 0.387 | 0.160 | 0.287 | 0.343 | 8.5% | 41.0% | 9.5% |
| FF | Brandon Marsh | 99 | 0.378 | 0.522 | 0.144 | 0.422 | 0.369 | 8.3% | 24.7% | 16.7% |
| SI | Adolis García | 62 | 0.160 | 0.300 | 0.140 | 0.281 | 0.328 | 10.3% | 35.5% | 14.5% |
| FF | Trea Turner | 109 | 0.312 | 0.452 | 0.140 | 0.394 | 0.355 | 7.0% | 29.1% | 18.1% |
| FF | Alec Bohm | 100 | 0.193 | 0.330 | 0.136 | 0.291 | 0.253 | 2.9% | 19.6% | 12.4% |
| CU | Justin Crawford | 17 | 0.188 | 0.312 | 0.125 | 0.241 | 0.243 | 0.0% | 35.0% | 22.2% |
| FF | J. T. Realmuto | 76 | 0.194 | 0.313 | 0.119 | 0.286 | 0.324 | 5.7% | 20.6% | 18.0% |
| SI | Bryce Harper | 51 | 0.302 | 0.419 | 0.116 | 0.361 | 0.349 | 2.6% | 24.1% | 13.6% |
| CU | J. T. Realmuto | 10 | 0.333 | 0.444 | 0.111 | 0.375 | 0.302 | 0.0% | 33.3% | 37.5% |
| SI | Justin Crawford | 45 | 0.231 | 0.333 | 0.103 | 0.304 | 0.295 | 0.0% | 23.4% | 6.2% |
| FF | Justin Crawford | 81 | 0.276 | 0.368 | 0.092 | 0.307 | 0.261 | 3.8% | 15.8% | 18.8% |
| CU | Bryce Harper | 27 | 0.292 | 0.375 | 0.083 | 0.337 | 0.282 | 0.0% | 13.2% | 30.6% |
| FF | Bryson Stott | 100 | 0.216 | 0.295 | 0.080 | 0.275 | 0.311 | 7.1% | 23.6% | 15.6% |
| SI | Alec Bohm | 85 | 0.208 | 0.286 | 0.078 | 0.263 | 0.324 | 5.8% | 35.6% | 11.0% |
| FF | Adolis García | 74 | 0.231 | 0.292 | 0.062 | 0.299 | 0.308 | 7.5% | 25.0% | 29.1% |
| SI | J. T. Realmuto | 57 | 0.200 | 0.260 | 0.060 | 0.263 | 0.351 | 2.3% | 27.8% | 10.8% |
| CU | Trea Turner | 19 | 0.158 | 0.211 | 0.053 | 0.161 | 0.237 | 0.0% | 28.0% | 34.1% |


## Philadelphia Phillies Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Trea Turner | 377 | 0.225 | 0.328 | 0.103 | 0.281 | 0.285 | 4.9% | 27.2% | 25.5% |
| Kyle Schwarber | 362 | 0.251 | 0.583 | 0.332 | 0.405 | 0.388 | 20.8% | 35.5% | 31.6% |
| Bryce Harper | 354 | 0.278 | 0.532 | 0.254 | 0.394 | 0.410 | 12.7% | 28.4% | 27.9% |
| Alec Bohm | 335 | 0.218 | 0.342 | 0.124 | 0.293 | 0.289 | 4.2% | 26.2% | 14.3% |
| Brandon Marsh | 323 | 0.314 | 0.495 | 0.182 | 0.368 | 0.328 | 9.0% | 24.8% | 22.9% |
| Bryson Stott | 313 | 0.245 | 0.406 | 0.161 | 0.312 | 0.317 | 7.2% | 26.0% | 15.8% |
| Adolis García | 278 | 0.207 | 0.358 | 0.150 | 0.290 | 0.294 | 9.9% | 28.4% | 30.8% |
| Justin Crawford | 266 | 0.243 | 0.336 | 0.093 | 0.290 | 0.272 | 1.1% | 18.9% | 16.7% |
| J. T. Realmuto | 229 | 0.208 | 0.332 | 0.124 | 0.293 | 0.321 | 5.0% | 26.9% | 22.3% |
| Edmundo Sosa | 160 | 0.225 | 0.377 | 0.152 | 0.301 | 0.342 | 8.5% | 26.0% | 23.8% |
| Rafael Marchán | 95 | 0.111 | 0.178 | 0.067 | 0.183 | 0.205 | 2.8% | 16.2% | 16.5% |
| Otto Kemp | 48 | 0.156 | 0.311 | 0.156 | 0.228 | 0.205 | 6.9% | 12.3% | 30.9% |


## New York Mets Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bo Bichette | 380 | 0.267 | 0.414 | 0.147 | 0.323 | 0.333 | 7.0% | 27.1% | 16.9% |
| Carson Benge | 339 | 0.262 | 0.398 | 0.136 | 0.335 | 0.345 | 8.2% | 24.5% | 19.5% |
| Marcus Semien | 338 | 0.217 | 0.352 | 0.135 | 0.285 | 0.316 | 8.9% | 21.9% | 21.3% |
| Brett Baty | 289 | 0.214 | 0.296 | 0.082 | 0.279 | 0.292 | 9.0% | 21.6% | 26.8% |
| Juan Soto | 281 | 0.292 | 0.550 | 0.258 | 0.400 | 0.424 | 14.9% | 33.8% | 18.0% |
| Mark Vientos | 254 | 0.206 | 0.382 | 0.176 | 0.276 | 0.312 | 10.5% | 27.1% | 29.8% |
| Francisco Álvarez | 199 | 0.251 | 0.425 | 0.173 | 0.339 | 0.342 | 15.4% | 28.9% | 28.7% |
| A. J. Ewing | 166 | 0.269 | 0.393 | 0.124 | 0.337 | 0.345 | 5.7% | 21.5% | 22.1% |
| Luis Torrens | 154 | 0.218 | 0.303 | 0.085 | 0.257 | 0.266 | 3.8% | 22.5% | 21.6% |
| Mj Melendez | 145 | 0.190 | 0.347 | 0.157 | 0.298 | 0.281 | 11.1% | 28.4% | 30.8% |
| Francisco Lindor | 138 | 0.210 | 0.323 | 0.113 | 0.296 | 0.336 | 6.9% | 25.9% | 21.0% |
| Jared Young | 125 | 0.221 | 0.416 | 0.195 | 0.320 | 0.344 | 15.3% | 26.2% | 23.1% |


## Bullpen Fatigue Report

### Philadelphia Phillies Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alan Rangel | 2026-06-27 | 4.0 | 70 |
| Chase Shugart | 2026-06-25 | 1.0 | 18 |
| Jhoan Duran | 2026-06-24 | 1.0 | 16 |
| Jhoan Duran | 2026-06-26 | 1.0 | 17 |
| Jonathan Bowlan | 2026-06-24 | 0.1 | 12 |
| Jonathan Bowlan | 2026-06-27 | 0.2 | 10 |
| José Alvarado | 2026-06-24 | 1.0 | 26 |
| José Alvarado | 2026-06-25 | 1.0 | 12 |
| Kyle Backhus | 2026-06-24 | 0.2 | 7 |
| Kyle Backhus | 2026-06-27 | 1.0 | 27 |
| Orion Kerkering | 2026-06-25 | 1.0 | 11 |
| Orion Kerkering | 2026-06-26 | 1.0 | 11 |
| Seth Johnson | 2026-06-24 | 1.0 | 10 |
| Seth Johnson | 2026-06-27 | 1.0 | 16 |
| Tim Mayza | 2026-06-25 | 1.0 | 12 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Alan Rangel, Jonathan Bowlan, Kyle Backhus, Seth Johnson


### New York Mets Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| A.J. Minter | 2026-06-24 | 1.0 | 19 |
| A.J. Minter | 2026-06-27 | 1.2 | 22 |
| Austin Warren | 2026-06-24 | 1.0 | 13 |
| Austin Warren | 2026-06-25 | 1.1 | 25 |
| Brooks Raley | 2026-06-24 | 1.0 | 20 |
| Brooks Raley | 2026-06-25 | 1.0 | 17 |
| Cionel Pérez | 2026-06-26 | 2.0 | 21 |
| Devin Williams | 2026-06-24 | 1.0 | 22 |
| Devin Williams | 2026-06-25 | 1.0 | 12 |
| Devin Williams | 2026-06-27 | 1.0 | 14 |
| Huascar Brazobán | 2026-06-24 | 2.0 | 34 |
| Huascar Brazobán | 2026-06-26 | 1.0 | 18 |
| Huascar Brazobán | 2026-06-27 | 1.0 | 10 |
| Jonathan Pintaro | 2026-06-24 | 2.0 | 45 |
| Luke Weaver | 2026-06-24 | 1.0 | 12 |
| Luke Weaver | 2026-06-25 | 1.0 | 11 |
| Luke Weaver | 2026-06-27 | 1.0 | 15 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** A.J. Minter, Devin Williams, Huascar Brazobán, Luke Weaver



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Trea Turner | 377 | 0.225 | 0.328 | 0.103 | 0.281 | 4.9% | 27.2% |
| 2 | Kyle Schwarber | 362 | 0.251 | 0.583 | 0.332 | 0.405 | 20.8% | 35.5% |
| 3 | Bryce Harper | 354 | 0.278 | 0.532 | 0.254 | 0.394 | 12.7% | 28.4% |
| 4 | Alec Bohm | 335 | 0.218 | 0.342 | 0.124 | 0.293 | 4.2% | 26.2% |
| 5 | Brandon Marsh | 323 | 0.314 | 0.495 | 0.182 | 0.368 | 9.0% | 24.8% |
| 6 | Bryson Stott | 313 | 0.245 | 0.406 | 0.161 | 0.312 | 7.2% | 26.0% |
| 7 | Adolis García | 278 | 0.207 | 0.358 | 0.150 | 0.290 | 9.9% | 28.4% |
| 8 | Justin Crawford | 266 | 0.243 | 0.336 | 0.093 | 0.290 | 1.1% | 18.9% |
| 9 | J. T. Realmuto | 229 | 0.208 | 0.332 | 0.124 | 0.293 | 5.0% | 26.9% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bo Bichette | 380 | 0.267 | 0.414 | 0.147 | 0.323 | 7.0% | 27.1% |
| 2 | Carson Benge | 339 | 0.262 | 0.398 | 0.136 | 0.335 | 8.2% | 24.5% |
| 3 | Marcus Semien | 338 | 0.217 | 0.352 | 0.135 | 0.285 | 8.9% | 21.9% |
| 4 | Brett Baty | 289 | 0.214 | 0.296 | 0.082 | 0.279 | 9.0% | 21.6% |
| 5 | Juan Soto | 281 | 0.292 | 0.550 | 0.258 | 0.400 | 14.9% | 33.8% |
| 6 | Mark Vientos | 254 | 0.206 | 0.382 | 0.176 | 0.276 | 10.5% | 27.1% |
| 7 | Francisco Álvarez | 199 | 0.251 | 0.425 | 0.173 | 0.339 | 15.4% | 28.9% |
| 8 | A. J. Ewing | 166 | 0.269 | 0.393 | 0.124 | 0.337 | 5.7% | 21.5% |
| 9 | Luis Torrens | 154 | 0.218 | 0.303 | 0.085 | 0.257 | 3.8% | 22.5% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6903 |
| Hits Allowed | 1516 |
| Walks/HBP | 589 |
| Strikeouts | 1655 |
| Home Runs Allowed | 219 |
| K Event Rate | 24.0% |
| BB/HBP Event Rate | 8.5% |
| HR Event Rate | 3.2% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6856 |
| Hits Allowed | 1422 |
| Walks/HBP | 650 |
| Strikeouts | 1588 |
| Home Runs Allowed | 187 |
| K Event Rate | 23.2% |
| BB/HBP Event Rate | 9.5% |
| HR Event Rate | 2.7% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: ST, FF, CH, SI
- Home pitcher pitch mix to inspect: SI, SV, CU, FF
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 8. Colorado Rockies @ Minnesota Twins

## Game Context

| Field | Value |
| --- | --- |
| Park | Target Field |
| Time | 2026-06-28T18:10:00Z |
| Away Team | Colorado Rockies |
| Home Team | Minnesota Twins |
| Away Probable Pitcher | Ryan Feltner |
| Home Probable Pitcher | Connor Prielipp |


## Away Starting Pitcher: Ryan Feltner

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 876 |
| Batted/Result Events | 234 |
| Hits Allowed | 48 |
| Walks | 25 |
| Strikeouts | 40 |
| Home Runs | 7 |
| K Event Rate | 17.1% |
| BB Event Rate | 10.7% |
| HR Event Rate | 3.0% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | COL | 8.3 | 4 | 0 | 4 | 2 | 0 |
| 2026-06-16 | CHC | 7.7 | 6 | 1 | 3 | 7 | 1 |
| 2026-06-11 | COL | 6.7 | 4 | 1 | 3 | 3 | 1 |
| 2026-06-05 | COL | 7.3 | 1 | 0 | 3 | 4 | 0 |
| 2026-05-30 | COL | 6.7 | 4 | 0 | 0 | 2 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 12.2% | 107 | 0.071 | 0.071 | 0.000 | 0.086 | 0.113 | 0.0% | 13.0% | 54.4% |
| CH | vs R | 3.2% | 28 | 0.571 | 1.143 | 0.571 | 0.719 | 0.426 | 16.7% | 33.3% | 23.1% |
| CU | vs L | 5.1% | 45 | 0.500 | 1.000 | 0.500 | 0.633 | 0.254 | 0.0% | 28.6% | 22.2% |
| CU | vs R | 3.3% | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.538 | 25.0% | 50.0% | 25.0% |
| FF | vs L | 15.8% | 138 | 0.125 | 0.300 | 0.175 | 0.254 | 0.400 | 8.8% | 35.2% | 6.6% |
| FF | vs R | 10.6% | 93 | 0.429 | 0.786 | 0.357 | 0.537 | 0.493 | 20.0% | 39.0% | 8.5% |
| SI | vs L | 1.7% | 15 | 0.143 | 0.286 | 0.143 | 0.179 | 0.298 | 0.0% | 40.0% | 0.0% |
| SI | vs R | 12.0% | 105 | 0.381 | 0.571 | 0.190 | 0.456 | 0.388 | 0.0% | 33.3% | 10.3% |
| SL | vs L | 11.3% | 99 | 0.353 | 0.529 | 0.176 | 0.444 | 0.555 | 11.8% | 26.7% | 22.0% |
| SL | vs R | 13.1% | 115 | 0.130 | 0.261 | 0.130 | 0.208 | 0.261 | 4.8% | 17.6% | 23.5% |
| ST | vs L | 1.6% | 14 | 0.000 | 0.000 | 0.000 | 0.175 | 0.523 | 0.0% | 25.0% | 11.1% |
| ST | vs R | 10.0% | 88 | 0.182 | 0.273 | 0.091 | 0.238 | 0.276 | 7.1% | 13.0% | 35.9% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 93 | 4 | 4 | 2 | 0 |
| 2026-06-16 | 104 | 6 | 3 | 7 | 1 |
| 2026-06-11 | 75 | 4 | 3 | 3 | 1 |
| 2026-06-05 | 81 | 1 | 2 | 4 | 0 |
| 2026-05-30 | 63 | 4 | 0 | 2 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Víctor Caratini | 7 | 0.167 | 0.667 | 0.500 | 0.386 | 0.188 | 50.0% | 25.0% | 38.5% |
| SI | Ryan Jeffers | 31 | 0.560 | 1.000 | 0.440 | 0.671 | 0.536 | 13.6% | 26.1% | 8.9% |
| FF | Byron Buxton | 95 | 0.310 | 0.726 | 0.417 | 0.462 | 0.432 | 35.1% | 36.0% | 25.2% |
| SL | Byron Buxton | 45 | 0.256 | 0.641 | 0.385 | 0.416 | 0.362 | 20.0% | 17.9% | 31.7% |
| CU | Byron Buxton | 17 | 0.353 | 0.706 | 0.353 | 0.444 | 0.290 | 14.3% | 54.5% | 21.4% |
| SL | Kody Clemens | 36 | 0.229 | 0.571 | 0.343 | 0.340 | 0.375 | 19.2% | 35.1% | 24.7% |
| ST | Austin Martin | 16 | 0.467 | 0.800 | 0.333 | 0.550 | 0.369 | 0.0% | 23.5% | 30.8% |
| CU | Royce Lewis | 9 | 0.333 | 0.667 | 0.333 | 0.422 | 0.345 | 14.3% | 21.4% | 11.8% |
| SL | Brooks Lee | 48 | 0.267 | 0.578 | 0.311 | 0.394 | 0.274 | 0.0% | 26.9% | 26.3% |
| ST | Ryan Jeffers | 21 | 0.200 | 0.500 | 0.300 | 0.352 | 0.287 | 13.3% | 22.2% | 24.0% |
| CU | Tristan Gray | 11 | 0.300 | 0.600 | 0.300 | 0.345 | 0.280 | 12.5% | 23.5% | 41.9% |
| SI | Byron Buxton | 67 | 0.308 | 0.585 | 0.277 | 0.400 | 0.377 | 10.5% | 34.4% | 19.4% |
| FF | Brooks Lee | 92 | 0.275 | 0.550 | 0.275 | 0.396 | 0.301 | 8.5% | 16.0% | 15.3% |
| SL | Trevor Larnach | 26 | 0.238 | 0.476 | 0.238 | 0.412 | 0.297 | 15.4% | 22.6% | 47.5% |
| SL | Josh Bell | 33 | 0.200 | 0.433 | 0.233 | 0.332 | 0.380 | 16.7% | 29.4% | 18.9% |
| SL | Royce Lewis | 37 | 0.200 | 0.433 | 0.233 | 0.309 | 0.265 | 20.0% | 20.6% | 43.1% |
| SI | Tristan Gray | 14 | 0.308 | 0.538 | 0.231 | 0.386 | 0.353 | 9.1% | 19.4% | 5.7% |
| ST | Kody Clemens | 15 | 0.231 | 0.462 | 0.231 | 0.313 | 0.242 | 12.5% | 15.0% | 27.6% |
| ST | Matt Wallner | 13 | 0.077 | 0.308 | 0.231 | 0.154 | 0.157 | 100.0% | 16.7% | 66.7% |
| CU | Kody Clemens | 24 | 0.227 | 0.455 | 0.227 | 0.321 | 0.274 | 7.7% | 37.9% | 32.6% |
| CU | Austin Martin | 12 | 0.222 | 0.444 | 0.222 | 0.383 | 0.212 | 0.0% | 0.0% | 25.0% |
| CH | Kody Clemens | 35 | 0.324 | 0.529 | 0.206 | 0.374 | 0.383 | 7.4% | 38.2% | 24.0% |
| SI | Matt Wallner | 25 | 0.250 | 0.450 | 0.200 | 0.378 | 0.436 | 12.5% | 27.0% | 14.0% |
| FF | Josh Bell | 105 | 0.308 | 0.505 | 0.198 | 0.404 | 0.364 | 6.7% | 21.9% | 19.4% |
| CU | Trevor Larnach | 24 | 0.333 | 0.524 | 0.190 | 0.448 | 0.331 | 6.7% | 18.2% | 37.1% |
| FF | Ryan Jeffers | 45 | 0.211 | 0.395 | 0.184 | 0.309 | 0.359 | 25.0% | 25.7% | 8.6% |
| FF | Kody Clemens | 92 | 0.203 | 0.380 | 0.177 | 0.313 | 0.297 | 8.2% | 22.2% | 20.4% |
| FF | Luke Keaschall | 83 | 0.270 | 0.446 | 0.176 | 0.343 | 0.314 | 4.8% | 24.4% | 10.9% |
| FF | Trevor Larnach | 95 | 0.337 | 0.512 | 0.174 | 0.398 | 0.387 | 7.7% | 31.8% | 10.8% |
| ST | Josh Bell | 13 | 0.167 | 0.333 | 0.167 | 0.246 | 0.169 | 0.0% | 11.8% | 33.3% |


## Home Starting Pitcher: Connor Prielipp

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 981 |
| Batted/Result Events | 248 |
| Hits Allowed | 56 |
| Walks | 23 |
| Strikeouts | 55 |
| Home Runs | 6 |
| K Event Rate | 22.2% |
| BB Event Rate | 9.3% |
| HR Event Rate | 2.4% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-19 | AZ | 10.0 | 9 | 1 | 3 | 4 | 1 |
| 2026-06-13 | MIN | 8.7 | 7 | 1 | 3 | 2 | 1 |
| 2026-06-07 | MIN | 6.0 | 4 | 0 | 1 | 7 | 0 |
| 2026-06-02 | MIN | 9.0 | 6 | 0 | 2 | 7 | 0 |
| 2026-05-27 | CWS | 7.7 | 8 | 0 | 3 | 5 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.2% | 2 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CH | vs R | 13.0% | 128 | 0.265 | 0.529 | 0.265 | 0.350 | 0.343 | 10.0% | 34.0% | 17.7% |
| CU | vs L | 4.3% | 42 | 0.333 | 0.500 | 0.167 | 0.358 | 0.116 | 0.0% | 10.0% | 17.6% |
| CU | vs R | 12.6% | 124 | 0.233 | 0.333 | 0.100 | 0.303 | 0.234 | 14.3% | 31.0% | 29.8% |
| FF | vs L | 6.4% | 63 | 0.300 | 0.500 | 0.200 | 0.423 | 0.471 | 28.6% | 25.0% | 16.0% |
| FF | vs R | 23.8% | 233 | 0.282 | 0.513 | 0.231 | 0.424 | 0.403 | 5.6% | 15.9% | 9.8% |
| SI | vs L | 4.1% | 40 | 0.385 | 0.385 | 0.000 | 0.346 | 0.237 | 0.0% | 17.6% | 10.0% |
| SI | vs R | 5.9% | 58 | 0.353 | 0.412 | 0.059 | 0.408 | 0.316 | 0.0% | 26.3% | 9.1% |
| SL | vs L | 10.8% | 106 | 0.200 | 0.400 | 0.200 | 0.266 | 0.344 | 25.0% | 27.0% | 25.0% |
| SL | vs R | 18.8% | 184 | 0.190 | 0.262 | 0.071 | 0.288 | 0.283 | 7.4% | 30.4% | 25.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 97 | 9 | 3 | 4 | 1 |
| 2026-06-13 | 98 | 7 | 2 | 2 | 1 |
| 2026-06-07 | 77 | 4 | 1 | 7 | 0 |
| 2026-06-02 | 94 | 6 | 2 | 7 | 0 |
| 2026-05-27 | 93 | 8 | 3 | 5 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Mickey Moniak | 12 | 0.182 | 0.727 | 0.545 | 0.392 | 0.468 | 66.7% | 41.7% | 45.2% |
| SL | Hunter Goodman | 53 | 0.260 | 0.720 | 0.460 | 0.453 | 0.340 | 24.1% | 29.3% | 38.8% |
| CU | Troy Johnston | 20 | 0.389 | 0.778 | 0.389 | 0.510 | 0.406 | 7.7% | 36.4% | 27.8% |
| SL | Tj Rumfield | 39 | 0.324 | 0.649 | 0.324 | 0.424 | 0.286 | 8.3% | 30.2% | 34.2% |
| CU | Hunter Goodman | 32 | 0.194 | 0.516 | 0.323 | 0.305 | 0.271 | 17.6% | 44.4% | 38.9% |
| SI | Edouard Julien | 18 | 0.438 | 0.750 | 0.312 | 0.528 | 0.461 | 13.3% | 29.4% | 8.1% |
| SI | Hunter Goodman | 47 | 0.400 | 0.700 | 0.300 | 0.503 | 0.455 | 14.3% | 27.0% | 16.7% |
| FF | Brett Sullivan | 40 | 0.270 | 0.568 | 0.297 | 0.360 | 0.300 | 6.7% | 24.3% | 10.6% |
| SL | Mickey Moniak | 20 | 0.167 | 0.444 | 0.278 | 0.295 | 0.311 | 23.1% | 17.2% | 31.2% |
| SL | Troy Johnston | 38 | 0.306 | 0.583 | 0.278 | 0.372 | 0.298 | 3.2% | 34.0% | 16.9% |
| FF | Hunter Goodman | 104 | 0.194 | 0.462 | 0.269 | 0.320 | 0.340 | 22.0% | 27.5% | 22.6% |
| CH | Hunter Goodman | 29 | 0.231 | 0.500 | 0.269 | 0.353 | 0.240 | 11.1% | 24.1% | 43.9% |
| FF | Mickey Moniak | 54 | 0.288 | 0.538 | 0.250 | 0.363 | 0.299 | 7.7% | 20.3% | 18.5% |
| CU | Brenton Doyle | 4 | 0.250 | 0.500 | 0.250 | 0.312 | 0.000 | 100.0% | 66.7% | 25.0% |
| FF | Kyle Karros | 99 | 0.373 | 0.614 | 0.241 | 0.467 | 0.408 | 8.8% | 28.8% | 5.6% |
| CH | Ezequiel Tovar | 25 | 0.200 | 0.440 | 0.240 | 0.304 | 0.225 | 6.7% | 22.2% | 41.0% |
| CU | Ezequiel Tovar | 14 | 0.231 | 0.462 | 0.231 | 0.318 | 0.321 | 25.0% | 15.4% | 27.3% |
| SI | Jake Mccarthy | 47 | 0.409 | 0.636 | 0.227 | 0.465 | 0.378 | 7.9% | 30.2% | 13.7% |
| FF | Tj Rumfield | 113 | 0.299 | 0.505 | 0.206 | 0.388 | 0.363 | 9.0% | 22.0% | 10.9% |
| FF | Jake Mccarthy | 108 | 0.326 | 0.526 | 0.200 | 0.379 | 0.361 | 4.7% | 15.2% | 11.5% |
| CU | Tj Rumfield | 23 | 0.250 | 0.450 | 0.200 | 0.389 | 0.294 | 0.0% | 15.4% | 30.2% |
| SL | Tyler Freeman | 27 | 0.308 | 0.500 | 0.192 | 0.393 | 0.285 | 0.0% | 28.6% | 18.4% |
| SL | Ezequiel Tovar | 47 | 0.267 | 0.444 | 0.178 | 0.291 | 0.299 | 10.5% | 13.5% | 31.7% |
| CH | Brett Sullivan | 18 | 0.176 | 0.353 | 0.176 | 0.208 | 0.178 | 0.0% | 10.0% | 16.0% |
| SI | Tj Rumfield | 42 | 0.286 | 0.457 | 0.171 | 0.365 | 0.354 | 2.8% | 17.5% | 0.0% |
| CH | Tj Rumfield | 45 | 0.214 | 0.381 | 0.167 | 0.303 | 0.264 | 8.3% | 25.8% | 21.4% |
| SI | Willi Castro | 29 | 0.250 | 0.417 | 0.167 | 0.388 | 0.354 | 5.3% | 22.2% | 25.4% |
| CH | Mickey Moniak | 32 | 0.161 | 0.323 | 0.161 | 0.197 | 0.212 | 4.0% | 35.1% | 30.6% |
| CU | Willi Castro | 27 | 0.400 | 0.560 | 0.160 | 0.439 | 0.355 | 4.8% | 29.4% | 23.9% |
| SI | Brenton Doyle | 21 | 0.211 | 0.368 | 0.158 | 0.376 | 0.301 | 6.2% | 20.0% | 10.8% |


## Colorado Rockies Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hunter Goodman | 348 | 0.257 | 0.559 | 0.302 | 0.380 | 0.333 | 17.5% | 29.3% | 32.0% |
| Tj Rumfield | 348 | 0.282 | 0.476 | 0.194 | 0.369 | 0.323 | 6.2% | 21.5% | 17.5% |
| Ezequiel Tovar | 310 | 0.213 | 0.348 | 0.136 | 0.276 | 0.281 | 8.5% | 18.5% | 27.5% |
| Willi Castro | 300 | 0.279 | 0.409 | 0.130 | 0.340 | 0.308 | 6.9% | 23.3% | 27.1% |
| Troy Johnston | 293 | 0.323 | 0.471 | 0.148 | 0.374 | 0.332 | 2.8% | 24.1% | 21.9% |
| Kyle Karros | 277 | 0.256 | 0.393 | 0.136 | 0.339 | 0.334 | 7.1% | 26.9% | 23.7% |
| Jake Mccarthy | 268 | 0.317 | 0.496 | 0.179 | 0.368 | 0.309 | 4.9% | 16.8% | 20.2% |
| Edouard Julien | 239 | 0.238 | 0.340 | 0.102 | 0.316 | 0.341 | 7.8% | 27.2% | 22.3% |
| Tyler Freeman | 211 | 0.279 | 0.372 | 0.093 | 0.332 | 0.318 | 1.2% | 20.3% | 11.0% |
| Mickey Moniak | 192 | 0.264 | 0.539 | 0.275 | 0.360 | 0.316 | 11.7% | 25.9% | 25.8% |
| Brenton Doyle | 145 | 0.227 | 0.295 | 0.068 | 0.283 | 0.248 | 7.0% | 18.4% | 25.6% |
| Brett Sullivan | 128 | 0.227 | 0.429 | 0.202 | 0.299 | 0.264 | 4.1% | 20.8% | 16.3% |


## Minnesota Twins Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Josh Bell | 340 | 0.232 | 0.377 | 0.145 | 0.304 | 0.320 | 9.3% | 22.8% | 23.0% |
| Brooks Lee | 339 | 0.254 | 0.450 | 0.196 | 0.348 | 0.279 | 4.6% | 21.3% | 18.2% |
| Byron Buxton | 334 | 0.272 | 0.593 | 0.321 | 0.391 | 0.354 | 19.7% | 31.0% | 29.5% |
| Luke Keaschall | 329 | 0.255 | 0.348 | 0.093 | 0.318 | 0.295 | 3.7% | 22.1% | 14.2% |
| Kody Clemens | 291 | 0.242 | 0.472 | 0.230 | 0.343 | 0.339 | 12.7% | 29.4% | 22.1% |
| Austin Martin | 263 | 0.261 | 0.338 | 0.077 | 0.338 | 0.309 | 2.3% | 18.2% | 18.2% |
| Trevor Larnach | 259 | 0.284 | 0.436 | 0.151 | 0.371 | 0.335 | 7.3% | 26.0% | 25.8% |
| Víctor Caratini | 247 | 0.236 | 0.380 | 0.144 | 0.317 | 0.338 | 8.4% | 25.2% | 20.4% |
| Royce Lewis | 224 | 0.205 | 0.350 | 0.145 | 0.289 | 0.300 | 12.5% | 25.5% | 29.9% |
| Tristan Gray | 177 | 0.238 | 0.341 | 0.104 | 0.275 | 0.282 | 6.3% | 24.9% | 29.9% |
| Ryan Jeffers | 166 | 0.298 | 0.532 | 0.234 | 0.417 | 0.389 | 15.4% | 27.0% | 15.8% |
| Matt Wallner | 151 | 0.194 | 0.343 | 0.149 | 0.288 | 0.281 | 11.5% | 24.1% | 39.3% |


## Bullpen Fatigue Report

### Colorado Rockies Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Antonio Senzatela | 2026-06-24 | 2.0 | 33 |
| Antonio Senzatela | 2026-06-26 | 1.0 | 20 |
| Brennan Bernardino | 2026-06-27 | 1.0 | 13 |
| Jimmy Herget | 2026-06-24 | 1.0 | 11 |
| Jimmy Herget | 2026-06-26 | 0.0 | 3 |
| Jimmy Herget | 2026-06-27 | 0.2 | 9 |
| John Brebbia | 2026-06-26 | 1.0 | 22 |
| Juan Mejia | 2026-06-26 | 1.0 | 13 |
| Seth Halvorsen | 2026-06-26 | 1.0 | 10 |
| Victor Vodnik | 2026-06-27 | 1.1 | 15 |
| Zach Agnos | 2026-06-27 | 0.1 | 25 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Brennan Bernardino, Jimmy Herget, Victor Vodnik, Zach Agnos


### Minnesota Twins Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Andrew Morris | 2026-06-24 | 1.0 | 7 |
| Andrew Morris | 2026-06-26 | 1.0 | 6 |
| Anthony Banda | 2026-06-24 | 1.0 | 24 |
| Anthony Banda | 2026-06-26 | 0.2 | 11 |
| Eric Orze | 2026-06-26 | 0.1 | 14 |
| Kody Funderburk | 2026-06-26 | 1.0 | 20 |
| Kody Funderburk | 2026-06-27 | 1.0 | 25 |
| Marco Raya | 2026-06-27 | 2.0 | 40 |
| Taylor Rogers | 2026-06-27 | 0.2 | 9 |
| Yoendrys Gómez | 2026-06-24 | 1.0 | 10 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Kody Funderburk, Marco Raya, Taylor Rogers



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Hunter Goodman | 348 | 0.257 | 0.559 | 0.302 | 0.380 | 17.5% | 29.3% |
| 2 | Tj Rumfield | 348 | 0.282 | 0.476 | 0.194 | 0.369 | 6.2% | 21.5% |
| 3 | Ezequiel Tovar | 310 | 0.213 | 0.348 | 0.136 | 0.276 | 8.5% | 18.5% |
| 4 | Willi Castro | 300 | 0.279 | 0.409 | 0.130 | 0.340 | 6.9% | 23.3% |
| 5 | Troy Johnston | 293 | 0.323 | 0.471 | 0.148 | 0.374 | 2.8% | 24.1% |
| 6 | Kyle Karros | 277 | 0.256 | 0.393 | 0.136 | 0.339 | 7.1% | 26.9% |
| 7 | Jake Mccarthy | 268 | 0.317 | 0.496 | 0.179 | 0.368 | 4.9% | 16.8% |
| 8 | Edouard Julien | 239 | 0.238 | 0.340 | 0.102 | 0.316 | 7.8% | 27.2% |
| 9 | Tyler Freeman | 211 | 0.279 | 0.372 | 0.093 | 0.332 | 1.2% | 20.3% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Josh Bell | 340 | 0.232 | 0.377 | 0.145 | 0.304 | 9.3% | 22.8% |
| 2 | Brooks Lee | 339 | 0.254 | 0.450 | 0.196 | 0.348 | 4.6% | 21.3% |
| 3 | Byron Buxton | 334 | 0.272 | 0.593 | 0.321 | 0.391 | 19.7% | 31.0% |
| 4 | Luke Keaschall | 329 | 0.255 | 0.348 | 0.093 | 0.318 | 3.7% | 22.1% |
| 5 | Kody Clemens | 291 | 0.242 | 0.472 | 0.230 | 0.343 | 12.7% | 29.4% |
| 6 | Austin Martin | 263 | 0.261 | 0.338 | 0.077 | 0.338 | 2.3% | 18.2% |
| 7 | Trevor Larnach | 259 | 0.284 | 0.436 | 0.151 | 0.371 | 7.3% | 26.0% |
| 8 | Víctor Caratini | 247 | 0.236 | 0.380 | 0.144 | 0.317 | 8.4% | 25.2% |
| 9 | Royce Lewis | 224 | 0.205 | 0.350 | 0.145 | 0.289 | 12.5% | 25.5% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7151 |
| Hits Allowed | 1749 |
| Walks/HBP | 663 |
| Strikeouts | 1451 |
| Home Runs Allowed | 230 |
| K Event Rate | 20.3% |
| BB/HBP Event Rate | 9.3% |
| HR Event Rate | 3.2% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7143 |
| Hits Allowed | 1599 |
| Walks/HBP | 724 |
| Strikeouts | 1489 |
| Home Runs Allowed | 220 |
| K Event Rate | 20.8% |
| BB/HBP Event Rate | 10.1% |
| HR Event Rate | 3.1% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL, CH, SI, ST, CU
- Home pitcher pitch mix to inspect: FF, SL, CU, CH, SI
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 9. Kansas City Royals @ Chicago White Sox

## Game Context

| Field | Value |
| --- | --- |
| Park | Rate Field |
| Time | 2026-06-28T18:10:00Z |
| Away Team | Kansas City Royals |
| Home Team | Chicago White Sox |
| Away Probable Pitcher | Luinder Avila |
| Home Probable Pitcher | Anthony Kay |


## Away Starting Pitcher: Luinder Avila

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 806 |
| Batted/Result Events | 189 |
| Hits Allowed | 42 |
| Walks | 27 |
| Strikeouts | 39 |
| Home Runs | 4 |
| K Event Rate | 20.6% |
| BB Event Rate | 14.3% |
| HR Event Rate | 2.1% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | TB | 7.3 | 3 | 0 | 5 | 6 | 0 |
| 2026-06-17 | WSH | 7.0 | 3 | 0 | 1 | 5 | 0 |
| 2026-06-12 | KC | 3.3 | 5 | 2 | 3 | 0 | 2 |
| 2026-06-06 | MIN | 6.0 | 2 | 0 | 3 | 3 | 0 |
| 2026-06-01 | CIN | 7.0 | 2 | 1 | 4 | 5 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 9.6% | 77 | 0.250 | 0.300 | 0.050 | 0.264 | 0.260 | 8.3% | 29.4% | 37.5% |
| CU | vs L | 11.3% | 91 | 0.182 | 0.727 | 0.545 | 0.386 | 0.440 | 20.0% | 16.0% | 19.4% |
| CU | vs R | 2.7% | 22 | 0.375 | 0.625 | 0.250 | 0.456 | 0.244 | 0.0% | 50.0% | 11.1% |
| FF | vs L | 16.9% | 136 | 0.308 | 0.538 | 0.231 | 0.415 | 0.351 | 4.8% | 20.0% | 14.5% |
| FF | vs R | 9.2% | 74 | 0.250 | 0.250 | 0.000 | 0.278 | 0.325 | 8.3% | 18.2% | 25.0% |
| SI | vs L | 12.9% | 104 | 0.333 | 0.458 | 0.125 | 0.395 | 0.348 | 10.5% | 20.0% | 22.4% |
| SI | vs R | 12.5% | 101 | 0.294 | 0.353 | 0.059 | 0.393 | 0.312 | 0.0% | 25.8% | 10.5% |
| SL | vs L | 8.2% | 66 | 0.176 | 0.176 | 0.000 | 0.189 | 0.167 | 0.0% | 5.0% | 34.3% |
| SL | vs R | 16.7% | 135 | 0.190 | 0.429 | 0.238 | 0.356 | 0.353 | 7.1% | 16.7% | 30.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 87 | 3 | 4 | 6 | 0 |
| 2026-06-17 | 91 | 3 | 1 | 5 | 0 |
| 2026-06-12 | 49 | 5 | 3 | 0 | 2 |
| 2026-06-06 | 70 | 2 | 3 | 3 | 0 |
| 2026-06-01 | 86 | 2 | 4 | 5 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Edgar Quero | 7 | 0.333 | 0.833 | 0.500 | 0.514 | 0.286 | 0.0% | 33.3% | 36.4% |
| FF | Munetaka Murakami | 90 | 0.257 | 0.714 | 0.457 | 0.476 | 0.462 | 23.9% | 39.3% | 34.9% |
| SL | Everson Pereira | 7 | 0.286 | 0.714 | 0.429 | 0.414 | 0.433 | 20.0% | 40.0% | 44.4% |
| CU | Andrew Benintendi | 5 | 0.400 | 0.800 | 0.400 | 0.500 | 0.380 | 0.0% | 36.4% | 21.1% |
| CH | Colson Montgomery | 36 | 0.273 | 0.667 | 0.394 | 0.415 | 0.406 | 18.2% | 23.8% | 38.7% |
| FF | Drew Romo | 29 | 0.125 | 0.500 | 0.375 | 0.328 | 0.328 | 20.0% | 22.5% | 18.9% |
| CH | Munetaka Murakami | 28 | 0.360 | 0.720 | 0.360 | 0.482 | 0.382 | 25.0% | 44.8% | 43.8% |
| SL | Colson Montgomery | 37 | 0.176 | 0.500 | 0.324 | 0.311 | 0.287 | 16.7% | 28.3% | 37.2% |
| SI | Drew Romo | 19 | 0.312 | 0.625 | 0.312 | 0.442 | 0.480 | 26.7% | 47.4% | 16.7% |
| CH | Everson Pereira | 17 | 0.375 | 0.688 | 0.312 | 0.465 | 0.231 | 10.0% | 33.3% | 43.8% |
| FF | Andrew Benintendi | 74 | 0.277 | 0.585 | 0.308 | 0.399 | 0.346 | 16.0% | 36.1% | 23.4% |
| SI | Munetaka Murakami | 27 | 0.250 | 0.550 | 0.300 | 0.430 | 0.443 | 36.4% | 25.9% | 31.5% |
| CH | Miguel Vargas | 29 | 0.375 | 0.667 | 0.292 | 0.488 | 0.535 | 16.7% | 28.3% | 3.8% |
| FF | Derek Hill | 41 | 0.222 | 0.500 | 0.278 | 0.350 | 0.308 | 20.0% | 29.7% | 38.5% |
| SL | Derek Hill | 22 | 0.364 | 0.636 | 0.273 | 0.427 | 0.377 | 12.5% | 20.0% | 34.1% |
| FF | Miguel Vargas | 110 | 0.230 | 0.494 | 0.264 | 0.400 | 0.407 | 17.5% | 24.5% | 22.3% |
| SI | Miguel Vargas | 81 | 0.200 | 0.457 | 0.257 | 0.331 | 0.415 | 15.5% | 35.0% | 7.0% |
| CU | Munetaka Murakami | 14 | 0.250 | 0.500 | 0.250 | 0.371 | 0.533 | 20.0% | 64.7% | 21.7% |
| SI | Andrew Benintendi | 42 | 0.270 | 0.514 | 0.243 | 0.363 | 0.363 | 12.9% | 27.0% | 15.4% |
| FF | Chase Meidroth | 101 | 0.298 | 0.536 | 0.238 | 0.412 | 0.351 | 9.1% | 25.0% | 14.4% |
| SI | Colson Montgomery | 49 | 0.286 | 0.524 | 0.238 | 0.412 | 0.391 | 14.3% | 40.0% | 32.7% |
| SL | Tristan Peters | 29 | 0.346 | 0.577 | 0.231 | 0.400 | 0.261 | 0.0% | 16.2% | 31.7% |
| SL | Andrew Benintendi | 46 | 0.190 | 0.405 | 0.214 | 0.287 | 0.262 | 18.2% | 26.3% | 48.1% |
| SL | Chase Meidroth | 51 | 0.265 | 0.469 | 0.204 | 0.346 | 0.268 | 11.8% | 20.0% | 23.6% |
| CU | Miguel Vargas | 18 | 0.133 | 0.333 | 0.200 | 0.278 | 0.392 | 7.7% | 28.6% | 17.9% |
| CH | Derek Hill | 18 | 0.375 | 0.562 | 0.188 | 0.411 | 0.444 | 6.7% | 26.3% | 33.3% |
| FF | Sam Antonacci | 82 | 0.354 | 0.538 | 0.185 | 0.463 | 0.450 | 12.5% | 23.2% | 14.5% |
| CU | Colson Montgomery | 13 | 0.364 | 0.545 | 0.182 | 0.438 | 0.351 | 0.0% | 30.0% | 36.1% |
| FF | Tristan Peters | 83 | 0.278 | 0.444 | 0.167 | 0.343 | 0.325 | 5.2% | 20.5% | 18.1% |
| FF | Colson Montgomery | 133 | 0.183 | 0.342 | 0.158 | 0.276 | 0.270 | 9.7% | 26.2% | 31.8% |


## Home Starting Pitcher: Anthony Kay

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1570 |
| Batted/Result Events | 387 |
| Hits Allowed | 87 |
| Walks | 34 |
| Strikeouts | 72 |
| Home Runs | 13 |
| K Event Rate | 18.6% |
| BB Event Rate | 8.8% |
| HR Event Rate | 3.4% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | CWS | 8.0 | 3 | 0 | 3 | 8 | 0 |
| 2026-06-17 | NYY | 7.0 | 6 | 1 | 2 | 2 | 1 |
| 2026-06-12 | CWS | 7.3 | 4 | 0 | 3 | 7 | 0 |
| 2026-06-05 | PHI | 7.0 | 7 | 2 | 2 | 4 | 2 |
| 2026-05-30 | CWS | 7.3 | 6 | 1 | 1 | 3 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs R | 13.6% | 213 | 0.286 | 0.388 | 0.102 | 0.320 | 0.272 | 2.4% | 25.8% | 22.2% |
| FC | vs L | 3.9% | 61 | 0.133 | 0.133 | 0.000 | 0.217 | 0.406 | 9.1% | 16.7% | 19.2% |
| FC | vs R | 14.5% | 227 | 0.300 | 0.650 | 0.350 | 0.466 | 0.458 | 18.9% | 27.3% | 15.7% |
| FF | vs L | 4.5% | 71 | 0.100 | 0.100 | 0.000 | 0.192 | 0.091 | 0.0% | 15.8% | 36.4% |
| FF | vs R | 20.1% | 315 | 0.278 | 0.519 | 0.241 | 0.374 | 0.421 | 16.2% | 25.6% | 11.0% |
| SI | vs L | 8.7% | 136 | 0.182 | 0.394 | 0.212 | 0.366 | 0.277 | 4.3% | 21.6% | 20.3% |
| SI | vs R | 9.2% | 144 | 0.385 | 0.641 | 0.256 | 0.453 | 0.485 | 14.3% | 43.4% | 10.4% |
| SL | vs L | 1.4% | 22 | 0.500 | 0.500 | 0.000 | 0.486 | 0.323 | 0.0% | 66.7% | 14.3% |
| SL | vs R | 3.0% | 47 | 0.111 | 0.111 | 0.000 | 0.205 | 0.163 | 0.0% | 14.3% | 40.0% |
| ST | vs L | 9.4% | 147 | 0.182 | 0.318 | 0.136 | 0.290 | 0.251 | 0.0% | 8.0% | 46.9% |
| ST | vs R | 11.8% | 186 | 0.316 | 0.421 | 0.105 | 0.393 | 0.330 | 5.6% | 20.5% | 23.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 101 | 3 | 2 | 8 | 0 |
| 2026-06-17 | 86 | 6 | 1 | 2 | 1 |
| 2026-06-12 | 89 | 4 | 1 | 7 | 0 |
| 2026-06-05 | 87 | 7 | 2 | 4 | 2 |
| 2026-05-30 | 84 | 6 | 1 | 3 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Carter Jensen | 22 | 0.350 | 0.800 | 0.450 | 0.532 | 0.443 | 21.4% | 36.0% | 23.7% |
| SI | Starling Marte | 11 | 0.500 | 0.900 | 0.400 | 0.605 | 0.614 | 22.2% | 31.6% | 9.1% |
| FC | Nick Loftin | 17 | 0.250 | 0.625 | 0.375 | 0.379 | 0.346 | 18.8% | 45.0% | 15.4% |
| FC | Michael Massey | 16 | 0.214 | 0.571 | 0.357 | 0.338 | 0.350 | 7.7% | 32.1% | 14.7% |
| FF | Jac Caglianone | 77 | 0.309 | 0.662 | 0.353 | 0.441 | 0.440 | 28.2% | 29.8% | 26.0% |
| FC | Bobby Witt | 32 | 0.310 | 0.655 | 0.345 | 0.411 | 0.473 | 18.5% | 27.9% | 23.3% |
| SI | Salvador Pérez | 44 | 0.368 | 0.711 | 0.342 | 0.458 | 0.445 | 15.4% | 29.9% | 10.8% |
| FC | Vinnie Pasquantino | 12 | 0.200 | 0.500 | 0.300 | 0.358 | 0.378 | 11.1% | 29.6% | 15.2% |
| CH | Bobby Witt | 32 | 0.333 | 0.633 | 0.300 | 0.427 | 0.443 | 19.2% | 29.5% | 16.1% |
| CH | Jac Caglianone | 42 | 0.316 | 0.579 | 0.263 | 0.431 | 0.372 | 14.3% | 38.3% | 25.0% |
| CH | Salvador Pérez | 35 | 0.206 | 0.441 | 0.235 | 0.309 | 0.211 | 10.7% | 26.9% | 21.6% |
| ST | Isaac Collins | 14 | 0.231 | 0.462 | 0.231 | 0.321 | 0.293 | 12.5% | 22.2% | 20.0% |
| CH | Vinnie Pasquantino | 28 | 0.308 | 0.538 | 0.231 | 0.416 | 0.327 | 5.9% | 28.9% | 28.8% |
| SI | Carter Jensen | 41 | 0.405 | 0.622 | 0.216 | 0.467 | 0.349 | 3.3% | 34.8% | 13.8% |
| FF | Kyle Isbel | 62 | 0.358 | 0.566 | 0.208 | 0.417 | 0.274 | 4.7% | 15.3% | 7.8% |
| FF | Carter Jensen | 88 | 0.205 | 0.411 | 0.205 | 0.319 | 0.300 | 8.3% | 18.4% | 26.1% |
| FF | Michael Massey | 88 | 0.244 | 0.439 | 0.195 | 0.314 | 0.275 | 8.5% | 21.5% | 14.8% |
| SI | Lane Thomas | 51 | 0.190 | 0.381 | 0.190 | 0.325 | 0.344 | 8.1% | 27.6% | 4.5% |
| FF | Nick Loftin | 65 | 0.245 | 0.434 | 0.189 | 0.335 | 0.314 | 8.5% | 17.1% | 6.6% |
| CH | Maikel García | 17 | 0.312 | 0.500 | 0.188 | 0.368 | 0.182 | 0.0% | 9.1% | 7.7% |
| FF | Lane Thomas | 82 | 0.190 | 0.365 | 0.175 | 0.343 | 0.337 | 8.7% | 22.1% | 12.0% |
| CH | Michael Massey | 25 | 0.400 | 0.560 | 0.160 | 0.418 | 0.327 | 4.5% | 25.6% | 19.6% |
| FF | Bobby Witt | 90 | 0.243 | 0.400 | 0.157 | 0.371 | 0.406 | 12.2% | 26.3% | 16.8% |
| ST | Jac Caglianone | 35 | 0.125 | 0.281 | 0.156 | 0.240 | 0.283 | 15.8% | 29.7% | 32.8% |
| ST | Maikel García | 29 | 0.154 | 0.308 | 0.154 | 0.222 | 0.256 | 5.9% | 12.0% | 30.8% |
| SI | Isaac Collins | 38 | 0.303 | 0.455 | 0.152 | 0.363 | 0.310 | 3.4% | 26.7% | 3.8% |
| FF | Vinnie Pasquantino | 120 | 0.260 | 0.394 | 0.135 | 0.327 | 0.325 | 10.8% | 26.1% | 7.4% |
| FF | Salvador Pérez | 81 | 0.227 | 0.360 | 0.133 | 0.269 | 0.344 | 18.2% | 26.5% | 21.4% |
| ST | Kyle Isbel | 16 | 0.062 | 0.188 | 0.125 | 0.100 | 0.156 | 0.0% | 26.7% | 15.8% |
| SI | Bobby Witt | 61 | 0.304 | 0.429 | 0.125 | 0.364 | 0.407 | 12.8% | 46.7% | 10.2% |


## Kansas City Royals Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bobby Witt | 355 | 0.285 | 0.453 | 0.168 | 0.364 | 0.388 | 12.4% | 32.5% | 20.9% |
| Salvador Pérez | 336 | 0.207 | 0.357 | 0.150 | 0.269 | 0.282 | 10.4% | 24.9% | 23.4% |
| Carter Jensen | 313 | 0.235 | 0.412 | 0.177 | 0.317 | 0.290 | 8.0% | 25.6% | 26.6% |
| Jac Caglianone | 306 | 0.261 | 0.471 | 0.210 | 0.355 | 0.376 | 16.5% | 33.7% | 28.6% |
| Maikel García | 304 | 0.257 | 0.370 | 0.112 | 0.309 | 0.316 | 4.8% | 28.3% | 13.6% |
| Vinnie Pasquantino | 302 | 0.219 | 0.340 | 0.121 | 0.300 | 0.316 | 7.4% | 27.5% | 14.0% |
| Isaac Collins | 286 | 0.220 | 0.307 | 0.087 | 0.299 | 0.309 | 5.6% | 26.1% | 20.3% |
| Lane Thomas | 233 | 0.206 | 0.335 | 0.129 | 0.312 | 0.314 | 5.5% | 20.8% | 17.1% |
| Michael Massey | 203 | 0.268 | 0.453 | 0.184 | 0.322 | 0.297 | 7.4% | 26.6% | 19.2% |
| Kyle Isbel | 196 | 0.263 | 0.383 | 0.120 | 0.317 | 0.275 | 2.9% | 24.5% | 14.6% |
| Nick Loftin | 182 | 0.244 | 0.397 | 0.154 | 0.330 | 0.322 | 6.0% | 22.1% | 15.3% |
| Starling Marte | 118 | 0.260 | 0.337 | 0.077 | 0.309 | 0.314 | 12.2% | 22.0% | 26.5% |


## Chicago White Sox Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Miguel Vargas | 369 | 0.240 | 0.471 | 0.231 | 0.366 | 0.398 | 13.7% | 28.0% | 17.3% |
| Chase Meidroth | 358 | 0.284 | 0.406 | 0.122 | 0.340 | 0.282 | 4.7% | 22.3% | 18.3% |
| Colson Montgomery | 348 | 0.215 | 0.456 | 0.241 | 0.333 | 0.331 | 13.5% | 30.3% | 34.7% |
| Andrew Benintendi | 269 | 0.237 | 0.441 | 0.204 | 0.321 | 0.327 | 12.0% | 28.6% | 27.2% |
| Munetaka Murakami | 264 | 0.236 | 0.546 | 0.310 | 0.394 | 0.379 | 20.5% | 37.1% | 38.9% |
| Sam Antonacci | 264 | 0.295 | 0.415 | 0.121 | 0.378 | 0.374 | 7.1% | 22.8% | 13.7% |
| Tristan Peters | 244 | 0.286 | 0.452 | 0.166 | 0.355 | 0.299 | 5.1% | 20.9% | 19.2% |
| Edgar Quero | 191 | 0.181 | 0.223 | 0.042 | 0.237 | 0.260 | 2.3% | 21.6% | 21.4% |
| Luisangel Acuña | 166 | 0.229 | 0.268 | 0.039 | 0.243 | 0.273 | 4.7% | 26.5% | 21.3% |
| Drew Romo | 113 | 0.140 | 0.340 | 0.200 | 0.254 | 0.261 | 9.7% | 22.3% | 29.7% |
| Derek Hill | 106 | 0.215 | 0.355 | 0.140 | 0.291 | 0.302 | 8.3% | 20.2% | 33.5% |
| Everson Pereira | 92 | 0.244 | 0.451 | 0.207 | 0.331 | 0.303 | 12.3% | 23.9% | 31.7% |


## Bullpen Fatigue Report

### Kansas City Royals Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alex Lange | 2026-06-26 | 0.1 | 26 |
| Beck Way | 2026-06-24 | 1.0 | 16 |
| Beck Way | 2026-06-26 | 1.1 | 23 |
| Connor Seabold | 2026-06-25 | 1.0 | 24 |
| Daniel Lynch IV | 2026-06-24 | 1.0 | 10 |
| Daniel Lynch IV | 2026-06-26 | 0.2 | 9 |
| Daniel Lynch IV | 2026-06-27 | 0.1 | 12 |
| John Schreiber | 2026-06-26 | 1.0 | 26 |
| John Schreiber | 2026-06-27 | 0.1 | 12 |
| Lucas Erceg | 2026-06-24 | 1.0 | 8 |
| Lucas Erceg | 2026-06-26 | 1.0 | 15 |
| Matt Strahm | 2026-06-25 | 1.0 | 15 |
| Mitch Spence | 2026-06-26 | 1.1 | 53 |
| Tyler Tolbert | 2026-06-25 | 1.0 | 24 |
| Tyler Tolbert | 2026-06-26 | 1.0 | 10 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Daniel Lynch IV, John Schreiber


### Chicago White Sox Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brandon Eisert | 2026-06-24 | 1.2 | 24 |
| Brandon Eisert | 2026-06-26 | 1.0 | 10 |
| Erick Fedde | 2026-06-24 | 4.0 | 75 |
| Grant Taylor | 2026-06-24 | 1.0 | 17 |
| Grant Taylor | 2026-06-27 | 2.0 | 19 |
| Joe Rock | 2026-06-24 | 2.0 | 39 |
| Jordan Hicks | 2026-06-26 | 1.0 | 18 |
| Sean Newcomb | 2026-06-27 | 1.2 | 30 |
| Trevor Richards | 2026-06-26 | 1.0 | 9 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Grant Taylor, Sean Newcomb



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bobby Witt | 355 | 0.285 | 0.453 | 0.168 | 0.364 | 12.4% | 32.5% |
| 2 | Salvador Pérez | 336 | 0.207 | 0.357 | 0.150 | 0.269 | 10.4% | 24.9% |
| 3 | Carter Jensen | 313 | 0.235 | 0.412 | 0.177 | 0.317 | 8.0% | 25.6% |
| 4 | Jac Caglianone | 306 | 0.261 | 0.471 | 0.210 | 0.355 | 16.5% | 33.7% |
| 5 | Maikel García | 304 | 0.257 | 0.370 | 0.112 | 0.309 | 4.8% | 28.3% |
| 6 | Vinnie Pasquantino | 302 | 0.219 | 0.340 | 0.121 | 0.300 | 7.4% | 27.5% |
| 7 | Isaac Collins | 286 | 0.220 | 0.307 | 0.087 | 0.299 | 5.6% | 26.1% |
| 8 | Lane Thomas | 233 | 0.206 | 0.335 | 0.129 | 0.312 | 5.5% | 20.8% |
| 9 | Michael Massey | 203 | 0.268 | 0.453 | 0.184 | 0.322 | 7.4% | 26.6% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Miguel Vargas | 369 | 0.240 | 0.471 | 0.231 | 0.366 | 13.7% | 28.0% |
| 2 | Chase Meidroth | 358 | 0.284 | 0.406 | 0.122 | 0.340 | 4.7% | 22.3% |
| 3 | Colson Montgomery | 348 | 0.215 | 0.456 | 0.241 | 0.333 | 13.5% | 30.3% |
| 4 | Andrew Benintendi | 269 | 0.237 | 0.441 | 0.204 | 0.321 | 12.0% | 28.6% |
| 5 | Munetaka Murakami | 264 | 0.236 | 0.546 | 0.310 | 0.394 | 20.5% | 37.1% |
| 6 | Sam Antonacci | 264 | 0.295 | 0.415 | 0.121 | 0.378 | 7.1% | 22.8% |
| 7 | Tristan Peters | 244 | 0.286 | 0.452 | 0.166 | 0.355 | 5.1% | 20.9% |
| 8 | Edgar Quero | 191 | 0.181 | 0.223 | 0.042 | 0.237 | 2.3% | 21.6% |
| 9 | Luisangel Acuña | 166 | 0.229 | 0.268 | 0.039 | 0.243 | 4.7% | 26.5% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7078 |
| Hits Allowed | 1573 |
| Walks/HBP | 722 |
| Strikeouts | 1492 |
| Home Runs Allowed | 212 |
| K Event Rate | 21.1% |
| BB/HBP Event Rate | 10.2% |
| HR Event Rate | 3.0% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6873 |
| Hits Allowed | 1447 |
| Walks/HBP | 766 |
| Strikeouts | 1563 |
| Home Runs Allowed | 226 |
| K Event Rate | 22.7% |
| BB/HBP Event Rate | 11.1% |
| HR Event Rate | 3.3% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SI, SL, CU, CH
- Home pitcher pitch mix to inspect: FF, ST, FC, SI, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 10. Chicago Cubs @ Milwaukee Brewers

## Game Context

| Field | Value |
| --- | --- |
| Park | American Family Field |
| Time | 2026-06-28T18:10:00Z |
| Away Team | Chicago Cubs |
| Home Team | Milwaukee Brewers |
| Away Probable Pitcher | Ryan Rolison |
| Home Probable Pitcher | Brandon Woodruff |


## Away Starting Pitcher: Ryan Rolison

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 434 |
| Batted/Result Events | 114 |
| Hits Allowed | 20 |
| Walks | 13 |
| Strikeouts | 29 |
| Home Runs | 3 |
| K Event Rate | 25.4% |
| BB Event Rate | 11.4% |
| HR Event Rate | 2.6% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | NYM | 1.3 | 1 | 0 | 1 | 0 | 0 |
| 2026-06-23 | NYM | 1.0 | 0 | 0 | 0 | 2 | 0 |
| 2026-06-20 | CHC | 0.3 | 0 | 0 | 0 | 0 | 0 |
| 2026-06-16 | CHC | 2.0 | 1 | 0 | 0 | 3 | 0 |
| 2026-06-14 | SF | 1.3 | 0 | 0 | 0 | 0 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs R | 1.4% | 6 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CU | vs L | 1.8% | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.382 | 0.0% | 16.7% | 0.0% |
| CU | vs R | 17.3% | 75 | 0.250 | 0.438 | 0.188 | 0.339 | 0.299 | 9.1% | 31.6% | 32.4% |
| FF | vs L | 14.7% | 64 | 0.000 | 0.000 | 0.000 | 0.089 | 0.213 | 10.0% | 14.3% | 29.0% |
| FF | vs R | 30.0% | 130 | 0.194 | 0.452 | 0.258 | 0.371 | 0.321 | 8.7% | 28.6% | 6.4% |
| SI | vs L | 2.8% | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.093 | 0.0% | 0.0% | 14.3% |
| SI | vs R | 0.5% | 2 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SL | vs L | 10.8% | 47 | 0.400 | 0.400 | 0.000 | 0.417 | 0.425 | 0.0% | 6.2% | 20.0% |
| SL | vs R | 9.0% | 39 | 0.200 | 0.200 | 0.000 | 0.180 | 0.297 | 0.0% | 35.3% | 10.0% |
| ST | vs L | 10.8% | 47 | 0.250 | 0.250 | 0.000 | 0.225 | 0.172 | 0.0% | 25.0% | 36.4% |
| ST | vs R | 0.7% | 3 | 1.000 | 1.000 | 0.000 | 0.900 | 0.916 | 0.0% | 50.0% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-24 | 18 | 1 | 1 | 0 | 0 |
| 2026-06-23 | 12 | 0 | 0 | 2 | 0 |
| 2026-06-20 | 1 | 0 | 0 | 0 | 0 |
| 2026-06-16 | 17 | 1 | 0 | 3 | 0 |
| 2026-06-14 | 11 | 0 | 0 | 0 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Jake Bauers | 17 | 0.375 | 1.000 | 0.625 | 0.574 | 0.395 | 27.3% | 50.0% | 31.4% |
| CU | Jackson Chourio | 7 | 0.200 | 0.800 | 0.600 | 0.386 | 0.259 | 0.0% | 33.3% | 9.1% |
| CU | Sal Frelick | 14 | 0.571 | 1.143 | 0.571 | 0.786 | 0.468 | 15.4% | 35.3% | 17.4% |
| ST | Gary Sánchez | 7 | 0.167 | 0.667 | 0.500 | 0.386 | 0.690 | 20.0% | 28.6% | 11.1% |
| FF | Andrew Vaughn | 38 | 0.452 | 0.871 | 0.419 | 0.584 | 0.462 | 10.7% | 28.6% | 8.8% |
| CU | Gary Sánchez | 11 | 0.300 | 0.700 | 0.400 | 0.441 | 0.384 | 14.3% | 20.0% | 20.0% |
| FF | Jake Bauers | 84 | 0.384 | 0.726 | 0.342 | 0.499 | 0.402 | 18.9% | 32.1% | 16.6% |
| CU | Christian Yelich | 10 | 0.300 | 0.600 | 0.300 | 0.380 | 0.308 | 20.0% | 22.2% | 47.1% |
| FF | Gary Sánchez | 50 | 0.316 | 0.605 | 0.289 | 0.464 | 0.438 | 13.3% | 20.8% | 19.1% |
| CU | Brice Turang | 21 | 0.333 | 0.619 | 0.286 | 0.405 | 0.372 | 15.4% | 44.4% | 29.6% |
| CU | Garrett Mitchell | 18 | 0.294 | 0.529 | 0.235 | 0.408 | 0.353 | 25.0% | 56.5% | 20.0% |
| FF | William Contreras | 92 | 0.244 | 0.474 | 0.231 | 0.383 | 0.373 | 9.0% | 34.5% | 12.4% |
| FF | Jackson Chourio | 59 | 0.273 | 0.491 | 0.218 | 0.364 | 0.338 | 21.6% | 24.7% | 23.0% |
| ST | Christian Yelich | 24 | 0.174 | 0.391 | 0.217 | 0.254 | 0.281 | 13.3% | 23.8% | 43.2% |
| ST | Luis Rengifo | 16 | 0.312 | 0.500 | 0.188 | 0.350 | 0.295 | 6.7% | 28.0% | 12.1% |
| FF | David Hamilton | 84 | 0.243 | 0.429 | 0.186 | 0.351 | 0.304 | 5.1% | 17.8% | 10.2% |
| SL | Jake Bauers | 46 | 0.154 | 0.333 | 0.179 | 0.279 | 0.296 | 9.5% | 30.6% | 29.7% |
| FF | Brice Turang | 107 | 0.200 | 0.376 | 0.176 | 0.335 | 0.337 | 11.5% | 16.7% | 20.1% |
| SL | Andrew Vaughn | 20 | 0.333 | 0.500 | 0.167 | 0.393 | 0.312 | 6.2% | 31.8% | 23.3% |
| SL | Garrett Mitchell | 42 | 0.135 | 0.297 | 0.162 | 0.226 | 0.299 | 15.0% | 21.2% | 52.7% |
| ST | Jackson Chourio | 25 | 0.120 | 0.280 | 0.160 | 0.166 | 0.315 | 16.7% | 20.0% | 34.9% |
| ST | David Hamilton | 13 | 0.077 | 0.231 | 0.154 | 0.123 | 0.162 | 11.1% | 17.6% | 24.0% |
| SL | Brice Turang | 52 | 0.239 | 0.391 | 0.152 | 0.320 | 0.339 | 9.1% | 37.8% | 22.6% |
| CU | Andrew Vaughn | 7 | 0.143 | 0.286 | 0.143 | 0.179 | 0.341 | 20.0% | 33.3% | 45.5% |
| ST | William Contreras | 31 | 0.129 | 0.258 | 0.129 | 0.192 | 0.211 | 13.6% | 19.4% | 24.5% |
| ST | Garrett Mitchell | 16 | 0.250 | 0.375 | 0.125 | 0.269 | 0.140 | 0.0% | 17.6% | 41.4% |
| FF | Garrett Mitchell | 99 | 0.190 | 0.310 | 0.119 | 0.291 | 0.320 | 15.6% | 26.4% | 28.7% |
| FF | Luis Rengifo | 62 | 0.283 | 0.396 | 0.113 | 0.354 | 0.346 | 4.3% | 19.8% | 6.9% |
| ST | Brice Turang | 21 | 0.167 | 0.278 | 0.111 | 0.229 | 0.247 | 9.1% | 25.0% | 27.3% |
| SL | David Hamilton | 32 | 0.286 | 0.393 | 0.107 | 0.298 | 0.176 | 9.5% | 27.6% | 39.7% |


## Home Starting Pitcher: Brandon Woodruff

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 560 |
| Batted/Result Events | 155 |
| Hits Allowed | 29 |
| Walks | 8 |
| Strikeouts | 39 |
| Home Runs | 6 |
| K Event Rate | 25.2% |
| BB Event Rate | 5.2% |
| HR Event Rate | 3.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | CIN | 6.3 | 1 | 0 | 0 | 10 | 0 |
| 2026-04-30 | MIL | 2.0 | 1 | 0 | 1 | 2 | 0 |
| 2026-04-24 | MIL | 7.0 | 5 | 1 | 2 | 3 | 1 |
| 2026-04-18 | MIA | 8.3 | 3 | 0 | 1 | 4 | 0 |
| 2026-04-12 | MIL | 7.7 | 3 | 1 | 0 | 6 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 16.8% | 94 | 0.211 | 0.263 | 0.053 | 0.232 | 0.267 | 7.1% | 12.0% | 43.5% |
| CH | vs R | 3.0% | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 66.7% | 62.5% |
| CU | vs L | 3.6% | 20 | 0.000 | 0.000 | 0.000 | 0.180 | 0.166 | 0.0% | 40.0% | 14.3% |
| CU | vs R | 1.4% | 8 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| FC | vs L | 3.8% | 21 | 0.167 | 0.333 | 0.167 | 0.208 | 0.254 | 0.0% | 33.3% | 0.0% |
| FC | vs R | 8.6% | 48 | 0.231 | 0.308 | 0.077 | 0.304 | 0.319 | 0.0% | 33.3% | 9.5% |
| FF | vs L | 25.0% | 140 | 0.143 | 0.286 | 0.143 | 0.250 | 0.249 | 13.6% | 14.0% | 26.1% |
| FF | vs R | 17.9% | 100 | 0.133 | 0.433 | 0.300 | 0.259 | 0.271 | 15.8% | 18.8% | 16.7% |
| SI | vs L | 3.2% | 18 | 0.333 | 0.667 | 0.333 | 0.422 | 0.274 | 14.3% | 22.2% | 0.0% |
| SI | vs R | 15.0% | 84 | 0.409 | 0.591 | 0.182 | 0.427 | 0.324 | 5.3% | 16.7% | 14.0% |
| ST | vs R | 1.1% | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.166 | 0.0% | 66.7% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 79 | 1 | 0 | 10 | 0 |
| 2026-04-30 | 21 | 1 | 1 | 2 | 0 |
| 2026-04-24 | 71 | 5 | 2 | 3 | 1 |
| 2026-04-18 | 92 | 3 | 1 | 4 | 0 |
| 2026-04-12 | 74 | 3 | 1 | 6 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Ian Happ | 26 | 0.409 | 1.091 | 0.682 | 0.604 | 0.544 | 31.2% | 37.8% | 21.1% |
| FC | Moisés Ballesteros | 17 | 0.286 | 0.786 | 0.500 | 0.485 | 0.421 | 9.1% | 36.4% | 17.2% |
| SI | Michael Conforto | 25 | 0.619 | 1.095 | 0.476 | 0.696 | 0.593 | 15.8% | 48.3% | 12.1% |
| FC | Michael Conforto | 11 | 0.364 | 0.818 | 0.455 | 0.491 | 0.514 | 22.2% | 28.6% | 16.0% |
| FC | Michael Busch | 26 | 0.300 | 0.750 | 0.450 | 0.467 | 0.464 | 15.8% | 28.1% | 6.2% |
| FC | Dansby Swanson | 19 | 0.353 | 0.706 | 0.353 | 0.474 | 0.389 | 13.3% | 20.0% | 36.4% |
| FC | Alex Bregman | 20 | 0.412 | 0.765 | 0.353 | 0.492 | 0.408 | 5.9% | 24.2% | 16.7% |
| FC | Carson Kelly | 16 | 0.417 | 0.750 | 0.333 | 0.547 | 0.539 | 18.2% | 30.0% | 8.3% |
| FF | Matt Shaw | 54 | 0.326 | 0.652 | 0.326 | 0.483 | 0.353 | 12.5% | 22.5% | 19.8% |
| FF | Moisés Ballesteros | 53 | 0.156 | 0.444 | 0.289 | 0.301 | 0.295 | 23.1% | 32.1% | 35.2% |
| CH | Carson Kelly | 15 | 0.286 | 0.571 | 0.286 | 0.383 | 0.278 | 9.1% | 31.8% | 33.3% |
| FF | Miguel Amaya | 47 | 0.318 | 0.591 | 0.273 | 0.439 | 0.307 | 17.1% | 25.4% | 11.6% |
| FF | Ian Happ | 117 | 0.212 | 0.485 | 0.273 | 0.368 | 0.316 | 15.8% | 24.5% | 26.3% |
| FF | Seiya Suzuki | 76 | 0.286 | 0.556 | 0.270 | 0.416 | 0.350 | 13.0% | 28.3% | 18.0% |
| FC | Pete Crow-Armstrong | 17 | 0.200 | 0.467 | 0.267 | 0.379 | 0.354 | 9.1% | 21.2% | 27.8% |
| FF | Dansby Swanson | 102 | 0.253 | 0.494 | 0.241 | 0.393 | 0.357 | 6.6% | 30.6% | 23.1% |
| SI | Dansby Swanson | 60 | 0.269 | 0.500 | 0.231 | 0.405 | 0.366 | 10.0% | 33.3% | 20.2% |
| SI | Miguel Amaya | 26 | 0.333 | 0.556 | 0.222 | 0.479 | 0.454 | 6.2% | 29.4% | 13.3% |
| FF | Michael Conforto | 44 | 0.205 | 0.410 | 0.205 | 0.308 | 0.303 | 8.0% | 28.3% | 15.9% |
| SI | Pete Crow-Armstrong | 53 | 0.435 | 0.630 | 0.196 | 0.492 | 0.442 | 7.7% | 37.3% | 13.5% |
| SI | Seiya Suzuki | 63 | 0.333 | 0.526 | 0.193 | 0.416 | 0.416 | 9.1% | 31.8% | 13.1% |
| SI | Michael Busch | 72 | 0.250 | 0.442 | 0.192 | 0.419 | 0.485 | 18.2% | 31.9% | 16.3% |
| FF | Pete Crow-Armstrong | 116 | 0.208 | 0.396 | 0.188 | 0.313 | 0.310 | 10.3% | 31.2% | 21.8% |
| FC | Seiya Suzuki | 19 | 0.294 | 0.471 | 0.176 | 0.368 | 0.302 | 8.3% | 15.8% | 39.4% |
| CH | Pete Crow-Armstrong | 45 | 0.225 | 0.400 | 0.175 | 0.298 | 0.332 | 3.3% | 37.0% | 29.5% |
| FF | Michael Busch | 130 | 0.211 | 0.368 | 0.158 | 0.323 | 0.332 | 12.1% | 24.2% | 12.7% |
| SI | Moisés Ballesteros | 28 | 0.346 | 0.500 | 0.154 | 0.389 | 0.311 | 13.6% | 27.9% | 11.3% |
| FF | Alex Bregman | 98 | 0.284 | 0.420 | 0.136 | 0.345 | 0.320 | 5.3% | 29.8% | 9.5% |
| SI | Ian Happ | 39 | 0.242 | 0.364 | 0.121 | 0.329 | 0.332 | 8.0% | 30.2% | 8.3% |
| CH | Matt Shaw | 21 | 0.263 | 0.368 | 0.105 | 0.290 | 0.213 | 6.7% | 12.5% | 30.6% |


## Chicago Cubs Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nico Hoerner | 385 | 0.252 | 0.361 | 0.109 | 0.320 | 0.323 | 1.6% | 18.6% | 10.3% |
| Michael Busch | 383 | 0.236 | 0.392 | 0.156 | 0.349 | 0.353 | 11.2% | 25.6% | 23.7% |
| Alex Bregman | 381 | 0.252 | 0.380 | 0.128 | 0.334 | 0.315 | 5.6% | 27.4% | 16.7% |
| Pete Crow-Armstrong | 367 | 0.273 | 0.497 | 0.224 | 0.371 | 0.361 | 11.0% | 31.2% | 26.3% |
| Ian Happ | 362 | 0.228 | 0.469 | 0.241 | 0.362 | 0.328 | 14.4% | 25.2% | 29.2% |
| Dansby Swanson | 326 | 0.191 | 0.357 | 0.166 | 0.303 | 0.288 | 6.9% | 24.7% | 28.4% |
| Seiya Suzuki | 284 | 0.263 | 0.449 | 0.186 | 0.367 | 0.338 | 8.6% | 26.3% | 24.5% |
| Carson Kelly | 233 | 0.291 | 0.424 | 0.133 | 0.371 | 0.325 | 7.2% | 23.9% | 19.8% |
| Moisés Ballesteros | 193 | 0.246 | 0.439 | 0.193 | 0.335 | 0.310 | 11.3% | 28.2% | 23.3% |
| Matt Shaw | 168 | 0.255 | 0.436 | 0.181 | 0.354 | 0.299 | 5.1% | 22.3% | 18.6% |
| Miguel Amaya | 151 | 0.236 | 0.417 | 0.181 | 0.365 | 0.309 | 9.3% | 20.4% | 22.3% |
| Michael Conforto | 145 | 0.258 | 0.500 | 0.242 | 0.359 | 0.354 | 12.4% | 31.3% | 25.6% |


## Milwaukee Brewers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brice Turang | 357 | 0.251 | 0.442 | 0.191 | 0.355 | 0.347 | 9.0% | 22.9% | 20.1% |
| William Contreras | 344 | 0.308 | 0.464 | 0.156 | 0.375 | 0.354 | 9.1% | 32.3% | 17.3% |
| Jake Bauers | 300 | 0.277 | 0.555 | 0.277 | 0.402 | 0.358 | 15.0% | 34.7% | 24.4% |
| Sal Frelick | 285 | 0.234 | 0.320 | 0.086 | 0.309 | 0.285 | 2.2% | 19.7% | 9.2% |
| Garrett Mitchell | 275 | 0.230 | 0.385 | 0.155 | 0.320 | 0.332 | 13.3% | 28.2% | 36.0% |
| David Hamilton | 237 | 0.252 | 0.359 | 0.107 | 0.312 | 0.266 | 5.0% | 17.6% | 20.0% |
| Christian Yelich | 233 | 0.244 | 0.388 | 0.144 | 0.313 | 0.296 | 7.0% | 20.3% | 29.6% |
| Luis Rengifo | 229 | 0.211 | 0.289 | 0.078 | 0.274 | 0.296 | 5.5% | 23.1% | 15.8% |
| Jackson Chourio | 227 | 0.299 | 0.540 | 0.242 | 0.384 | 0.338 | 14.1% | 28.4% | 21.5% |
| Joey Ortiz | 210 | 0.211 | 0.256 | 0.044 | 0.267 | 0.287 | 2.7% | 21.6% | 18.0% |
| Gary Sánchez | 163 | 0.231 | 0.455 | 0.224 | 0.358 | 0.363 | 9.6% | 27.4% | 23.2% |
| Andrew Vaughn | 158 | 0.328 | 0.496 | 0.168 | 0.406 | 0.360 | 5.0% | 31.4% | 16.3% |


## Bullpen Fatigue Report

### Chicago Cubs Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Caleb Thielbar | 2026-06-24 | 1.0 | 19 |
| Caleb Thielbar | 2026-06-25 | 1.0 | 12 |
| Ethan Roberts | 2026-06-25 | 1.0 | 15 |
| Ethan Roberts | 2026-06-26 | 1.0 | 14 |
| Gavin Hollowell | 2026-06-24 | 0.2 | 13 |
| Hoby Milner | 2026-06-24 | 1.0 | 17 |
| Hoby Milner | 2026-06-25 | 0.0 | 13 |
| Jacob Webb | 2026-06-24 | 1.0 | 26 |
| Jacob Webb | 2026-06-25 | 1.0 | 20 |
| Jacob Webb | 2026-06-27 | 1.0 | 13 |
| Jayden Murray | 2026-06-26 | 2.0 | 46 |
| Phil Maton | 2026-06-25 | 1.1 | 23 |
| Ryan Rolison | 2026-06-24 | 1.0 | 18 |
| Trent Thornton | 2026-06-24 | 1.0 | 13 |
| Trent Thornton | 2026-06-25 | 1.0 | 10 |
| Trent Thornton | 2026-06-27 | 1.0 | 12 |
| Tyler Ferguson | 2026-06-24 | 2.0 | 26 |
| Tyler Ferguson | 2026-06-27 | 0.1 | 10 |
| Vince Velasquez | 2026-06-27 | 1.0 | 12 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Jacob Webb, Trent Thornton, Tyler Ferguson, Vince Velasquez


### Milwaukee Brewers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Aaron Ashby | 2026-06-26 | 1.0 | 15 |
| Abner Uribe | 2026-06-26 | 1.0 | 13 |
| Chad Patrick | 2026-06-24 | 1.2 | 40 |
| Chad Patrick | 2026-06-27 | 0.2 | 30 |
| Craig Yoho | 2026-06-24 | 1.0 | 21 |
| Grant Anderson | 2026-06-24 | 0.2 | 24 |
| Grant Anderson | 2026-06-27 | 1.1 | 26 |
| Jared Koenig | 2026-06-27 | 1.0 | 15 |
| Joel Kuhnel | 2026-06-24 | 1.1 | 31 |
| Joel Kuhnel | 2026-06-27 | 1.0 | 18 |
| Trevor Megill | 2026-06-26 | 1.0 | 26 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Chad Patrick, Grant Anderson, Jared Koenig, Joel Kuhnel



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nico Hoerner | 385 | 0.252 | 0.361 | 0.109 | 0.320 | 1.6% | 18.6% |
| 2 | Michael Busch | 383 | 0.236 | 0.392 | 0.156 | 0.349 | 11.2% | 25.6% |
| 3 | Alex Bregman | 381 | 0.252 | 0.380 | 0.128 | 0.334 | 5.6% | 27.4% |
| 4 | Pete Crow-Armstrong | 367 | 0.273 | 0.497 | 0.224 | 0.371 | 11.0% | 31.2% |
| 5 | Ian Happ | 362 | 0.228 | 0.469 | 0.241 | 0.362 | 14.4% | 25.2% |
| 6 | Dansby Swanson | 326 | 0.191 | 0.357 | 0.166 | 0.303 | 6.9% | 24.7% |
| 7 | Seiya Suzuki | 284 | 0.263 | 0.449 | 0.186 | 0.367 | 8.6% | 26.3% |
| 8 | Carson Kelly | 233 | 0.291 | 0.424 | 0.133 | 0.371 | 7.2% | 23.9% |
| 9 | Moisés Ballesteros | 193 | 0.246 | 0.439 | 0.193 | 0.335 | 11.3% | 28.2% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Brice Turang | 357 | 0.251 | 0.442 | 0.191 | 0.355 | 9.0% | 22.9% |
| 2 | William Contreras | 344 | 0.308 | 0.464 | 0.156 | 0.375 | 9.1% | 32.3% |
| 3 | Jake Bauers | 300 | 0.277 | 0.555 | 0.277 | 0.402 | 15.0% | 34.7% |
| 4 | Sal Frelick | 285 | 0.234 | 0.320 | 0.086 | 0.309 | 2.2% | 19.7% |
| 5 | Garrett Mitchell | 275 | 0.230 | 0.385 | 0.155 | 0.320 | 13.3% | 28.2% |
| 6 | David Hamilton | 237 | 0.252 | 0.359 | 0.107 | 0.312 | 5.0% | 17.6% |
| 7 | Christian Yelich | 233 | 0.244 | 0.388 | 0.144 | 0.313 | 7.0% | 20.3% |
| 8 | Luis Rengifo | 229 | 0.211 | 0.289 | 0.078 | 0.274 | 5.5% | 23.1% |
| 9 | Jackson Chourio | 227 | 0.299 | 0.540 | 0.242 | 0.384 | 14.1% | 28.4% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7177 |
| Hits Allowed | 1556 |
| Walks/HBP | 775 |
| Strikeouts | 1545 |
| Home Runs Allowed | 267 |
| K Event Rate | 21.5% |
| BB/HBP Event Rate | 10.8% |
| HR Event Rate | 3.7% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6855 |
| Hits Allowed | 1439 |
| Walks/HBP | 715 |
| Strikeouts | 1624 |
| Home Runs Allowed | 181 |
| K Event Rate | 23.7% |
| BB/HBP Event Rate | 10.4% |
| HR Event Rate | 2.6% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL, CU, ST
- Home pitcher pitch mix to inspect: FF, CH, SI, FC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 11. Miami Marlins @ St. Louis Cardinals

## Game Context

| Field | Value |
| --- | --- |
| Park | Busch Stadium |
| Time | 2026-06-28T18:15:00Z |
| Away Team | Miami Marlins |
| Home Team | St. Louis Cardinals |
| Away Probable Pitcher | Tyler Phillips |
| Home Probable Pitcher | Kyle Leahy |


## Away Starting Pitcher: Tyler Phillips

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 983 |
| Batted/Result Events | 261 |
| Hits Allowed | 51 |
| Walks | 31 |
| Strikeouts | 52 |
| Home Runs | 6 |
| K Event Rate | 19.9% |
| BB Event Rate | 11.9% |
| HR Event Rate | 2.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | MIA | 8.0 | 5 | 1 | 3 | 4 | 1 |
| 2026-06-16 | PHI | 7.0 | 6 | 3 | 3 | 4 | 3 |
| 2026-06-11 | MIA | 6.0 | 2 | 0 | 2 | 5 | 0 |
| 2026-06-05 | MIA | 8.0 | 7 | 1 | 3 | 3 | 1 |
| 2026-05-30 | NYM | 7.0 | 6 | 0 | 1 | 2 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 13.7% | 135 | 0.176 | 0.235 | 0.059 | 0.253 | 0.300 | 5.6% | 37.0% | 48.3% |
| CU | vs R | 3.4% | 33 | 0.286 | 0.286 | 0.000 | 0.390 | 0.431 | 0.0% | 50.0% | 38.5% |
| FF | vs L | 6.8% | 67 | 0.267 | 0.533 | 0.267 | 0.391 | 0.263 | 0.0% | 21.7% | 7.7% |
| FF | vs R | 2.2% | 22 | 0.333 | 0.833 | 0.500 | 0.483 | 0.263 | 20.0% | 9.1% | 13.3% |
| FS | vs L | 13.9% | 137 | 0.179 | 0.286 | 0.107 | 0.276 | 0.288 | 5.3% | 26.3% | 38.2% |
| FS | vs R | 9.7% | 95 | 0.083 | 0.125 | 0.042 | 0.165 | 0.184 | 0.0% | 19.4% | 26.0% |
| SI | vs L | 12.6% | 124 | 0.333 | 0.519 | 0.185 | 0.450 | 0.441 | 8.0% | 31.0% | 4.2% |
| SI | vs R | 13.7% | 135 | 0.306 | 0.500 | 0.194 | 0.418 | 0.449 | 11.4% | 38.9% | 5.0% |
| ST | vs L | 9.9% | 97 | 0.250 | 0.500 | 0.250 | 0.312 | 0.238 | 18.2% | 42.1% | 36.4% |
| ST | vs R | 14.0% | 138 | 0.171 | 0.229 | 0.057 | 0.228 | 0.255 | 8.0% | 18.9% | 33.9% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 89 | 5 | 3 | 4 | 1 |
| 2026-06-16 | 79 | 6 | 3 | 4 | 3 |
| 2026-06-11 | 70 | 2 | 2 | 5 | 0 |
| 2026-06-05 | 82 | 7 | 3 | 3 | 1 |
| 2026-05-30 | 72 | 6 | 1 | 2 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Lars Nootbaar | 4 | 0.333 | 1.333 | 1.000 | 0.675 | 0.679 | 50.0% | 33.3% | 25.0% |
| FS | Thomas Saggese | 3 | 0.333 | 1.333 | 1.000 | 0.667 | 0.528 | 50.0% | 33.3% | 25.0% |
| CU | Thomas Saggese | 8 | 0.500 | 1.125 | 0.625 | 0.675 | 0.323 | 33.3% | 50.0% | 26.7% |
| FS | Iván Herrera | 7 | 0.286 | 0.714 | 0.429 | 0.414 | 0.336 | 33.3% | 25.0% | 38.5% |
| FF | Lars Nootbaar | 24 | 0.364 | 0.727 | 0.364 | 0.448 | 0.495 | 21.1% | 41.7% | 5.1% |
| CU | Alec Burleson | 26 | 0.375 | 0.708 | 0.333 | 0.477 | 0.427 | 20.0% | 36.6% | 14.3% |
| FF | Jj Wetherholt | 120 | 0.291 | 0.602 | 0.311 | 0.421 | 0.417 | 17.5% | 31.6% | 20.7% |
| FF | Jordan Walker | 88 | 0.280 | 0.561 | 0.280 | 0.370 | 0.367 | 18.6% | 30.5% | 16.1% |
| CU | Victor Scott | 13 | 0.182 | 0.455 | 0.273 | 0.292 | 0.391 | 12.5% | 9.1% | 23.5% |
| FF | Nolan Gorman | 77 | 0.262 | 0.525 | 0.262 | 0.399 | 0.361 | 15.0% | 29.7% | 33.1% |
| FS | Jordan Walker | 5 | 0.250 | 0.500 | 0.250 | 0.390 | 0.293 | 0.0% | 66.7% | 60.0% |
| FF | Alec Burleson | 91 | 0.317 | 0.561 | 0.244 | 0.406 | 0.467 | 14.8% | 34.5% | 21.9% |
| SI | Iván Herrera | 77 | 0.241 | 0.466 | 0.224 | 0.421 | 0.387 | 6.1% | 25.7% | 10.1% |
| ST | Jordan Walker | 50 | 0.222 | 0.444 | 0.222 | 0.341 | 0.335 | 8.8% | 29.6% | 32.3% |
| FF | Iván Herrera | 99 | 0.256 | 0.449 | 0.192 | 0.394 | 0.394 | 9.4% | 30.8% | 12.9% |
| CU | Iván Herrera | 26 | 0.182 | 0.364 | 0.182 | 0.302 | 0.328 | 5.6% | 35.5% | 14.6% |
| FF | Pedro Pagés | 39 | 0.152 | 0.333 | 0.182 | 0.236 | 0.314 | 8.3% | 16.7% | 18.7% |
| SI | Jordan Walker | 71 | 0.258 | 0.435 | 0.177 | 0.361 | 0.394 | 12.0% | 39.0% | 16.7% |
| SI | Pedro Pagés | 28 | 0.391 | 0.565 | 0.174 | 0.423 | 0.397 | 9.1% | 20.0% | 16.0% |
| SI | Nolan Gorman | 25 | 0.217 | 0.391 | 0.174 | 0.266 | 0.292 | 10.5% | 34.4% | 22.2% |
| FF | José Fermín | 49 | 0.196 | 0.370 | 0.174 | 0.282 | 0.216 | 2.5% | 18.7% | 10.2% |
| SI | Nathan Church | 22 | 0.250 | 0.400 | 0.150 | 0.318 | 0.375 | 15.0% | 22.2% | 12.1% |
| SI | Alec Burleson | 57 | 0.283 | 0.415 | 0.132 | 0.330 | 0.374 | 5.9% | 35.4% | 15.7% |
| CU | José Fermín | 8 | 0.375 | 0.500 | 0.125 | 0.381 | 0.385 | 0.0% | 18.2% | 8.3% |
| ST | Masyn Winn | 38 | 0.176 | 0.294 | 0.118 | 0.254 | 0.276 | 3.8% | 15.9% | 26.1% |
| ST | Thomas Saggese | 11 | 0.200 | 0.300 | 0.100 | 0.259 | 0.318 | 0.0% | 6.7% | 37.5% |
| CU | Nathan Church | 12 | 0.273 | 0.364 | 0.091 | 0.404 | 0.314 | 0.0% | 43.8% | 11.1% |
| SI | Masyn Winn | 51 | 0.356 | 0.444 | 0.089 | 0.379 | 0.370 | 4.9% | 35.4% | 6.8% |
| FF | Nathan Church | 66 | 0.263 | 0.351 | 0.088 | 0.327 | 0.319 | 7.7% | 10.8% | 19.4% |
| ST | Nolan Gorman | 15 | 0.071 | 0.143 | 0.071 | 0.130 | 0.128 | 0.0% | 14.3% | 48.5% |


## Home Starting Pitcher: Kyle Leahy

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1342 |
| Batted/Result Events | 357 |
| Hits Allowed | 90 |
| Walks | 29 |
| Strikeouts | 68 |
| Home Runs | 9 |
| K Event Rate | 19.0% |
| BB Event Rate | 8.1% |
| HR Event Rate | 2.5% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | STL | 8.0 | 3 | 0 | 2 | 3 | 0 |
| 2026-06-17 | STL | 8.0 | 7 | 0 | 1 | 7 | 0 |
| 2026-06-12 | MIN | 7.3 | 8 | 1 | 1 | 5 | 1 |
| 2026-06-05 | STL | 6.3 | 5 | 0 | 2 | 1 | 0 |
| 2026-05-30 | STL | 7.0 | 6 | 0 | 1 | 4 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 11.3% | 152 | 0.273 | 0.455 | 0.182 | 0.333 | 0.361 | 12.5% | 31.6% | 39.4% |
| CH | vs R | 1.0% | 13 | 0.286 | 0.429 | 0.143 | 0.356 | 0.244 | 0.0% | 20.0% | 37.5% |
| CU | vs L | 11.1% | 149 | 0.229 | 0.314 | 0.086 | 0.285 | 0.272 | 9.1% | 31.6% | 29.7% |
| CU | vs R | 4.6% | 62 | 0.067 | 0.133 | 0.067 | 0.083 | 0.242 | 9.1% | 35.0% | 20.0% |
| FF | vs L | 18.6% | 249 | 0.321 | 0.566 | 0.245 | 0.416 | 0.460 | 17.4% | 45.5% | 14.1% |
| FF | vs R | 10.0% | 134 | 0.346 | 0.615 | 0.269 | 0.404 | 0.408 | 17.4% | 37.2% | 13.3% |
| PO | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs L | 1.9% | 25 | 0.500 | 0.786 | 0.286 | 0.563 | 0.498 | 10.0% | 81.8% | 0.0% |
| SI | vs R | 12.2% | 164 | 0.204 | 0.204 | 0.000 | 0.314 | 0.366 | 2.4% | 28.6% | 6.7% |
| SL | vs L | 5.4% | 73 | 0.400 | 0.467 | 0.067 | 0.436 | 0.405 | 6.7% | 18.2% | 12.5% |
| SL | vs R | 10.4% | 140 | 0.261 | 0.435 | 0.174 | 0.330 | 0.336 | 14.3% | 25.0% | 18.2% |
| ST | vs L | 3.3% | 44 | 0.273 | 0.364 | 0.091 | 0.312 | 0.408 | 11.1% | 46.2% | 12.5% |
| ST | vs R | 10.1% | 136 | 0.293 | 0.512 | 0.220 | 0.341 | 0.331 | 14.3% | 20.0% | 21.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 85 | 3 | 2 | 3 | 0 |
| 2026-06-17 | 81 | 7 | 1 | 7 | 0 |
| 2026-06-12 | 77 | 8 | 1 | 5 | 1 |
| 2026-06-05 | 79 | 5 | 2 | 1 | 0 |
| 2026-05-30 | 78 | 6 | 0 | 4 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Liam Hicks | 31 | 0.333 | 0.852 | 0.519 | 0.477 | 0.281 | 8.3% | 37.8% | 22.4% |
| ST | Agustín Ramírez | 9 | 0.250 | 0.625 | 0.375 | 0.400 | 0.417 | 14.3% | 15.4% | 40.9% |
| CU | Kyle Stowers | 14 | 0.273 | 0.636 | 0.364 | 0.446 | 0.352 | 0.0% | 28.6% | 34.8% |
| SL | Kyle Stowers | 37 | 0.212 | 0.545 | 0.333 | 0.354 | 0.364 | 15.8% | 24.4% | 38.9% |
| CU | Graham Pauley | 10 | 0.111 | 0.444 | 0.333 | 0.270 | 0.128 | 0.0% | 12.5% | 33.3% |
| CH | Owen Caissie | 31 | 0.310 | 0.621 | 0.310 | 0.389 | 0.299 | 20.0% | 16.7% | 41.5% |
| FF | Xavier Edwards | 116 | 0.394 | 0.677 | 0.283 | 0.487 | 0.415 | 8.4% | 19.9% | 7.1% |
| SL | Heriberto Hernandez | 39 | 0.364 | 0.636 | 0.273 | 0.469 | 0.401 | 13.0% | 31.4% | 40.7% |
| FF | Joe Mack | 33 | 0.333 | 0.567 | 0.233 | 0.414 | 0.337 | 4.5% | 28.3% | 9.5% |
| ST | Connor Norby | 17 | 0.154 | 0.385 | 0.231 | 0.335 | 0.284 | 11.1% | 21.1% | 30.6% |
| FF | Owen Caissie | 63 | 0.226 | 0.453 | 0.226 | 0.329 | 0.332 | 19.4% | 22.1% | 25.2% |
| SL | Javier Sanoja | 36 | 0.333 | 0.556 | 0.222 | 0.454 | 0.232 | 3.1% | 15.7% | 18.5% |
| SI | Otto Lopez | 74 | 0.406 | 0.625 | 0.219 | 0.503 | 0.462 | 10.2% | 45.2% | 4.8% |
| CU | Liam Hicks | 15 | 0.357 | 0.571 | 0.214 | 0.420 | 0.358 | 0.0% | 29.2% | 10.7% |
| SI | Kyle Stowers | 35 | 0.250 | 0.464 | 0.214 | 0.407 | 0.437 | 19.0% | 33.3% | 18.5% |
| SL | Otto Lopez | 68 | 0.394 | 0.606 | 0.212 | 0.454 | 0.363 | 6.8% | 27.7% | 27.1% |
| SI | Joe Mack | 21 | 0.263 | 0.474 | 0.211 | 0.393 | 0.339 | 12.5% | 14.8% | 6.5% |
| SI | Heriberto Hernandez | 34 | 0.241 | 0.448 | 0.207 | 0.379 | 0.403 | 12.0% | 31.7% | 19.4% |
| CH | Liam Hicks | 42 | 0.341 | 0.537 | 0.195 | 0.390 | 0.291 | 2.6% | 19.6% | 13.9% |
| CH | Heriberto Hernandez | 16 | 0.188 | 0.375 | 0.188 | 0.294 | 0.307 | 11.1% | 18.8% | 41.4% |
| FF | Otto Lopez | 80 | 0.380 | 0.563 | 0.183 | 0.432 | 0.435 | 12.1% | 32.8% | 6.6% |
| FF | Connor Norby | 76 | 0.219 | 0.391 | 0.172 | 0.340 | 0.288 | 16.7% | 22.3% | 31.5% |
| FF | Liam Hicks | 106 | 0.207 | 0.379 | 0.172 | 0.325 | 0.360 | 6.0% | 22.4% | 5.4% |
| SL | Connor Norby | 32 | 0.267 | 0.433 | 0.167 | 0.325 | 0.239 | 12.5% | 22.9% | 41.8% |
| ST | Graham Pauley | 7 | 0.167 | 0.333 | 0.167 | 0.307 | 0.249 | 0.0% | 28.6% | 22.2% |
| SI | Connor Norby | 52 | 0.349 | 0.512 | 0.163 | 0.415 | 0.388 | 2.4% | 18.9% | 9.2% |
| CH | Joe Mack | 20 | 0.158 | 0.316 | 0.158 | 0.225 | 0.286 | 11.1% | 40.0% | 53.5% |
| FF | Heriberto Hernandez | 49 | 0.190 | 0.333 | 0.143 | 0.277 | 0.385 | 8.6% | 41.9% | 25.0% |
| SL | Owen Caissie | 31 | 0.179 | 0.321 | 0.143 | 0.273 | 0.273 | 11.1% | 30.6% | 35.5% |
| CH | Jakob Marsee | 32 | 0.300 | 0.433 | 0.133 | 0.353 | 0.362 | 4.2% | 39.0% | 27.0% |


## Miami Marlins Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Otto Lopez | 362 | 0.332 | 0.481 | 0.148 | 0.386 | 0.339 | 6.9% | 29.2% | 18.5% |
| Xavier Edwards | 359 | 0.296 | 0.430 | 0.134 | 0.360 | 0.328 | 4.8% | 18.8% | 14.3% |
| Jakob Marsee | 345 | 0.192 | 0.292 | 0.100 | 0.287 | 0.300 | 3.3% | 22.6% | 18.0% |
| Liam Hicks | 305 | 0.269 | 0.451 | 0.182 | 0.353 | 0.317 | 4.2% | 23.9% | 10.5% |
| Kyle Stowers | 253 | 0.234 | 0.428 | 0.194 | 0.332 | 0.329 | 10.2% | 29.6% | 33.7% |
| Connor Norby | 244 | 0.214 | 0.348 | 0.133 | 0.306 | 0.282 | 9.4% | 21.6% | 29.4% |
| Owen Caissie | 231 | 0.225 | 0.412 | 0.186 | 0.310 | 0.295 | 14.2% | 24.0% | 33.5% |
| Javier Sanoja | 200 | 0.257 | 0.358 | 0.102 | 0.312 | 0.262 | 1.2% | 21.4% | 11.7% |
| Heriberto Hernandez | 189 | 0.232 | 0.405 | 0.173 | 0.330 | 0.347 | 8.9% | 31.7% | 31.4% |
| Agustín Ramírez | 141 | 0.228 | 0.350 | 0.122 | 0.305 | 0.282 | 5.3% | 27.0% | 30.9% |
| Joe Mack | 136 | 0.252 | 0.390 | 0.138 | 0.317 | 0.313 | 8.8% | 25.1% | 20.2% |
| Graham Pauley | 104 | 0.156 | 0.260 | 0.104 | 0.228 | 0.201 | 4.2% | 16.8% | 19.9% |


## St. Louis Cardinals Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Iván Herrera | 370 | 0.255 | 0.416 | 0.161 | 0.373 | 0.367 | 7.6% | 29.9% | 18.6% |
| Alec Burleson | 362 | 0.288 | 0.480 | 0.192 | 0.363 | 0.386 | 10.3% | 31.5% | 18.3% |
| Jj Wetherholt | 360 | 0.255 | 0.397 | 0.142 | 0.334 | 0.351 | 7.9% | 28.5% | 19.0% |
| Jordan Walker | 353 | 0.287 | 0.512 | 0.225 | 0.378 | 0.359 | 13.7% | 32.0% | 28.9% |
| Masyn Winn | 321 | 0.238 | 0.324 | 0.085 | 0.299 | 0.300 | 3.2% | 20.3% | 19.4% |
| Nolan Gorman | 242 | 0.194 | 0.313 | 0.118 | 0.269 | 0.278 | 8.8% | 28.0% | 37.5% |
| Nathan Church | 222 | 0.254 | 0.390 | 0.137 | 0.311 | 0.292 | 8.1% | 18.4% | 21.5% |
| Victor Scott | 200 | 0.196 | 0.262 | 0.065 | 0.264 | 0.273 | 0.8% | 15.6% | 24.2% |
| Pedro Pagés | 155 | 0.213 | 0.340 | 0.128 | 0.257 | 0.282 | 5.6% | 23.0% | 25.4% |
| José Fermín | 147 | 0.250 | 0.360 | 0.110 | 0.299 | 0.282 | 1.7% | 22.5% | 10.8% |
| Thomas Saggese | 92 | 0.198 | 0.314 | 0.116 | 0.251 | 0.274 | 10.5% | 22.6% | 28.6% |
| Lars Nootbaar | 78 | 0.308 | 0.492 | 0.185 | 0.390 | 0.397 | 12.5% | 36.9% | 16.7% |


## Bullpen Fatigue Report

### Miami Marlins Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Anthony Bender | 2026-06-24 | 1.1 | 15 |
| Anthony Bender | 2026-06-27 | 1.1 | 20 |
| Calvin Faucher | 2026-06-26 | 1.0 | 10 |
| John King | 2026-06-24 | 1.0 | 17 |
| John King | 2026-06-27 | 1.1 | 13 |
| Lake Bachar | 2026-06-27 | 2.0 | 31 |
| Michael Petersen | 2026-06-24 | 1.0 | 13 |
| Michael Petersen | 2026-06-26 | 1.0 | 19 |
| Pete Fairbanks | 2026-06-24 | 1.0 | 10 |
| Tyler Zuber | 2026-06-27 | 1.0 | 10 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Anthony Bender, John King, Lake Bachar, Tyler Zuber


### St. Louis Cardinals Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| George Soriano | 2026-06-26 | 1.0 | 27 |
| Gordon Graceffo | 2026-06-24 | 1.2 | 32 |
| JoJo Romero | 2026-06-26 | 1.0 | 12 |
| Justin Bruihl | 2026-06-24 | 2.0 | 43 |
| Justin Bruihl | 2026-06-26 | 0.1 | 2 |
| Justin Bruihl | 2026-06-27 | 2.0 | 21 |
| Matt Svanson | 2026-06-27 | 0.1 | 11 |
| Max Rajcic | 2026-06-26 | 0.2 | 25 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Justin Bruihl, Matt Svanson



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Otto Lopez | 362 | 0.332 | 0.481 | 0.148 | 0.386 | 6.9% | 29.2% |
| 2 | Xavier Edwards | 359 | 0.296 | 0.430 | 0.134 | 0.360 | 4.8% | 18.8% |
| 3 | Jakob Marsee | 345 | 0.192 | 0.292 | 0.100 | 0.287 | 3.3% | 22.6% |
| 4 | Liam Hicks | 305 | 0.269 | 0.451 | 0.182 | 0.353 | 4.2% | 23.9% |
| 5 | Kyle Stowers | 253 | 0.234 | 0.428 | 0.194 | 0.332 | 10.2% | 29.6% |
| 6 | Connor Norby | 244 | 0.214 | 0.348 | 0.133 | 0.306 | 9.4% | 21.6% |
| 7 | Owen Caissie | 231 | 0.225 | 0.412 | 0.186 | 0.310 | 14.2% | 24.0% |
| 8 | Javier Sanoja | 200 | 0.257 | 0.358 | 0.102 | 0.312 | 1.2% | 21.4% |
| 9 | Heriberto Hernandez | 189 | 0.232 | 0.405 | 0.173 | 0.330 | 8.9% | 31.7% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Iván Herrera | 370 | 0.255 | 0.416 | 0.161 | 0.373 | 7.6% | 29.9% |
| 2 | Alec Burleson | 362 | 0.288 | 0.480 | 0.192 | 0.363 | 10.3% | 31.5% |
| 3 | Jj Wetherholt | 360 | 0.255 | 0.397 | 0.142 | 0.334 | 7.9% | 28.5% |
| 4 | Jordan Walker | 353 | 0.287 | 0.512 | 0.225 | 0.378 | 13.7% | 32.0% |
| 5 | Masyn Winn | 321 | 0.238 | 0.324 | 0.085 | 0.299 | 3.2% | 20.3% |
| 6 | Nolan Gorman | 242 | 0.194 | 0.313 | 0.118 | 0.269 | 8.8% | 28.0% |
| 7 | Nathan Church | 222 | 0.254 | 0.390 | 0.137 | 0.311 | 8.1% | 18.4% |
| 8 | Victor Scott | 200 | 0.196 | 0.262 | 0.065 | 0.264 | 0.8% | 15.6% |
| 9 | Pedro Pagés | 155 | 0.213 | 0.340 | 0.128 | 0.257 | 5.6% | 23.0% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6681 |
| Hits Allowed | 1394 |
| Walks/HBP | 681 |
| Strikeouts | 1509 |
| Home Runs Allowed | 161 |
| K Event Rate | 22.6% |
| BB/HBP Event Rate | 10.2% |
| HR Event Rate | 2.4% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6631 |
| Hits Allowed | 1457 |
| Walks/HBP | 660 |
| Strikeouts | 1330 |
| Home Runs Allowed | 189 |
| K Event Rate | 20.1% |
| BB/HBP Event Rate | 10.0% |
| HR Event Rate | 2.9% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: SI, ST, FS, CU, FF
- Home pitcher pitch mix to inspect: FF, SL, CU, SI, ST, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 12. Athletics @ Los Angeles Angels

## Game Context

| Field | Value |
| --- | --- |
| Park | Angel Stadium |
| Time | 2026-06-28T19:15:00Z |
| Away Team | Athletics |
| Home Team | Los Angeles Angels |
| Away Probable Pitcher | Aaron Civale |
| Home Probable Pitcher | Sam Aldegheri |


## Away Starting Pitcher: Aaron Civale

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1165 |
| Batted/Result Events | 305 |
| Hits Allowed | 82 |
| Walks | 19 |
| Strikeouts | 57 |
| Home Runs | 13 |
| K Event Rate | 18.7% |
| BB Event Rate | 6.2% |
| HR Event Rate | 4.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | SF | 6.0 | 6 | 1 | 1 | 5 | 1 |
| 2026-06-17 | ATH | 6.7 | 9 | 0 | 2 | 2 | 0 |
| 2026-05-25 | ATH | 7.3 | 9 | 3 | 1 | 2 | 3 |
| 2026-05-20 | LAA | 7.0 | 5 | 3 | 2 | 2 | 3 |
| 2026-05-15 | ATH | 7.3 | 6 | 2 | 1 | 2 | 2 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 14.5% | 169 | 0.268 | 0.317 | 0.049 | 0.298 | 0.317 | 5.9% | 18.9% | 19.7% |
| CU | vs R | 8.5% | 99 | 0.192 | 0.462 | 0.269 | 0.285 | 0.390 | 16.7% | 34.6% | 35.0% |
| FC | vs L | 20.5% | 239 | 0.244 | 0.444 | 0.200 | 0.351 | 0.319 | 5.0% | 29.5% | 16.5% |
| FC | vs R | 14.4% | 168 | 0.225 | 0.275 | 0.050 | 0.232 | 0.219 | 3.8% | 22.6% | 28.9% |
| FF | vs L | 9.4% | 110 | 0.312 | 0.750 | 0.438 | 0.448 | 0.433 | 19.2% | 40.8% | 12.1% |
| FF | vs R | 4.0% | 47 | 0.333 | 0.333 | 0.000 | 0.307 | 0.469 | 16.7% | 39.1% | 14.3% |
| FS | vs L | 6.0% | 70 | 0.368 | 0.474 | 0.105 | 0.368 | 0.324 | 0.0% | 24.0% | 16.7% |
| FS | vs R | 0.2% | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.017 | 0.0% | 0.0% | 0.0% |
| SI | vs L | 9.8% | 114 | 0.417 | 0.875 | 0.458 | 0.554 | 0.441 | 17.6% | 36.1% | 7.3% |
| SI | vs R | 8.7% | 101 | 0.414 | 0.655 | 0.241 | 0.476 | 0.435 | 15.4% | 40.0% | 10.0% |
| SL | vs L | 0.3% | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.287 | 0.0% | 0.0% | 0.0% |
| SL | vs R | 3.3% | 38 | 0.273 | 0.636 | 0.364 | 0.404 | 0.403 | 14.3% | 27.3% | 38.9% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 84 | 6 | 0 | 5 | 1 |
| 2026-06-17 | 71 | 9 | 2 | 2 | 0 |
| 2026-05-25 | 73 | 9 | 1 | 2 | 3 |
| 2026-05-20 | 61 | 5 | 2 | 2 | 3 |
| 2026-05-15 | 76 | 6 | 1 | 2 | 2 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Mike Trout | 30 | 0.348 | 0.913 | 0.565 | 0.562 | 0.476 | 19.0% | 33.3% | 18.4% |
| FC | Wade Meckler | 11 | 0.222 | 0.667 | 0.444 | 0.423 | 0.481 | 25.0% | 30.0% | 33.3% |
| CU | Yoán Moncada | 9 | 0.250 | 0.625 | 0.375 | 0.400 | 0.406 | 16.7% | 25.0% | 26.3% |
| FC | Zach Neto | 23 | 0.368 | 0.737 | 0.368 | 0.507 | 0.511 | 12.5% | 24.3% | 19.2% |
| CU | Logan O'Hoppe | 13 | 0.545 | 0.909 | 0.364 | 0.631 | 0.472 | 22.2% | 37.5% | 13.0% |
| FF | Jorge Soler | 73 | 0.219 | 0.562 | 0.344 | 0.368 | 0.279 | 17.9% | 32.5% | 29.5% |
| CU | Jorge Soler | 12 | 0.250 | 0.583 | 0.333 | 0.346 | 0.414 | 25.0% | 41.7% | 38.1% |
| CU | Josh Lowe | 13 | 0.333 | 0.667 | 0.333 | 0.388 | 0.365 | 0.0% | 33.3% | 27.3% |
| FF | Zach Neto | 107 | 0.269 | 0.591 | 0.323 | 0.397 | 0.351 | 16.4% | 25.9% | 20.7% |
| SI | Yoán Moncada | 21 | 0.190 | 0.476 | 0.286 | 0.276 | 0.271 | 23.1% | 39.1% | 12.9% |
| FC | Oswald Peraza | 16 | 0.267 | 0.533 | 0.267 | 0.416 | 0.404 | 16.7% | 36.4% | 31.2% |
| FF | Adam Frazier | 39 | 0.233 | 0.500 | 0.267 | 0.371 | 0.282 | 8.3% | 10.3% | 16.2% |
| FF | Jo Adell | 97 | 0.278 | 0.544 | 0.267 | 0.358 | 0.379 | 15.9% | 20.6% | 19.5% |
| FF | Vaughn Grissom | 43 | 0.176 | 0.441 | 0.265 | 0.315 | 0.369 | 13.8% | 22.2% | 18.5% |
| FF | Mike Trout | 141 | 0.292 | 0.547 | 0.255 | 0.467 | 0.470 | 22.2% | 25.0% | 14.0% |
| FC | Adam Frazier | 4 | 0.500 | 0.750 | 0.250 | 0.537 | 0.202 | 0.0% | 9.1% | 16.7% |
| SI | Zach Neto | 59 | 0.271 | 0.521 | 0.250 | 0.403 | 0.429 | 21.2% | 27.0% | 17.5% |
| FF | Josh Lowe | 47 | 0.349 | 0.581 | 0.233 | 0.424 | 0.281 | 16.7% | 18.5% | 25.5% |
| FC | Jorge Soler | 18 | 0.267 | 0.467 | 0.200 | 0.378 | 0.483 | 21.4% | 18.8% | 29.8% |
| SI | Jorge Soler | 56 | 0.273 | 0.455 | 0.182 | 0.370 | 0.377 | 8.1% | 30.3% | 16.7% |
| FF | Nolan Schanuel | 92 | 0.282 | 0.449 | 0.167 | 0.365 | 0.363 | 4.7% | 20.0% | 6.2% |
| CU | Jo Adell | 20 | 0.211 | 0.368 | 0.158 | 0.268 | 0.194 | 0.0% | 36.0% | 31.7% |
| FF | Logan O'Hoppe | 56 | 0.216 | 0.373 | 0.157 | 0.291 | 0.372 | 14.6% | 28.9% | 16.0% |
| CU | Vaughn Grissom | 15 | 0.385 | 0.538 | 0.154 | 0.440 | 0.379 | 7.7% | 30.0% | 16.7% |
| FF | Oswald Peraza | 80 | 0.222 | 0.375 | 0.153 | 0.305 | 0.309 | 8.5% | 20.2% | 20.5% |
| FC | Nolan Schanuel | 25 | 0.208 | 0.333 | 0.125 | 0.252 | 0.288 | 0.0% | 22.7% | 3.8% |
| SI | Josh Lowe | 26 | 0.125 | 0.250 | 0.125 | 0.181 | 0.273 | 5.0% | 12.8% | 6.4% |
| FF | Wade Meckler | 42 | 0.257 | 0.371 | 0.114 | 0.344 | 0.338 | 4.0% | 22.0% | 12.2% |
| SI | Jo Adell | 70 | 0.258 | 0.371 | 0.113 | 0.322 | 0.375 | 3.7% | 26.7% | 16.7% |
| SI | Mike Trout | 55 | 0.289 | 0.400 | 0.111 | 0.373 | 0.461 | 13.2% | 38.8% | 10.6% |


## Home Starting Pitcher: Sam Aldegheri

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 441 |
| Batted/Result Events | 113 |
| Hits Allowed | 25 |
| Walks | 12 |
| Strikeouts | 16 |
| Home Runs | 4 |
| K Event Rate | 14.2% |
| BB Event Rate | 10.6% |
| HR Event Rate | 3.5% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | LAA | 7.0 | 5 | 2 | 1 | 3 | 2 |
| 2026-06-17 | AZ | 6.3 | 6 | 1 | 4 | 1 | 1 |
| 2026-06-12 | LAA | 7.0 | 3 | 0 | 3 | 4 | 0 |
| 2026-06-08 | LAA | 1.3 | 1 | 0 | 0 | 1 | 0 |
| 2026-06-02 | LAA | 7.3 | 4 | 0 | 2 | 5 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 4.5% | 20 | 1.000 | 2.000 | 1.000 | 1.125 | 0.506 | 0.0% | 25.0% | 16.7% |
| CH | vs R | 27.4% | 121 | 0.143 | 0.286 | 0.143 | 0.222 | 0.261 | 9.5% | 26.2% | 33.8% |
| CU | vs L | 1.1% | 5 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 50.0% |
| CU | vs R | 5.9% | 26 | 0.000 | 0.000 | 0.000 | 0.233 | 0.346 | 0.0% | 33.3% | 20.0% |
| FC | vs L | 7.3% | 32 | 0.222 | 0.222 | 0.000 | 0.291 | 0.349 | 0.0% | 23.1% | 6.7% |
| FC | vs R | 5.2% | 23 | 0.333 | 0.667 | 0.333 | 0.488 | 0.450 | 0.0% | 40.0% | 12.5% |
| FF | vs L | 13.4% | 59 | 0.308 | 0.385 | 0.077 | 0.378 | 0.325 | 0.0% | 13.0% | 13.8% |
| FF | vs R | 30.2% | 133 | 0.235 | 0.382 | 0.147 | 0.316 | 0.343 | 12.5% | 17.6% | 6.7% |
| SL | vs L | 4.5% | 20 | 0.500 | 2.000 | 1.500 | 1.000 | 0.518 | 50.0% | 40.0% | 14.3% |
| SL | vs R | 0.5% | 2 | 1.000 | 1.000 | 0.000 | 0.900 | 0.887 | 0.0% | 0.0% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 91 | 5 | 1 | 3 | 2 |
| 2026-06-17 | 77 | 6 | 3 | 1 | 1 |
| 2026-06-12 | 74 | 3 | 3 | 4 | 0 |
| 2026-06-08 | 8 | 1 | 0 | 1 | 0 |
| 2026-06-02 | 89 | 4 | 2 | 5 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Carlos Cortes | 11 | 0.333 | 1.000 | 0.667 | 0.509 | 0.627 | 20.0% | 27.8% | 20.0% |
| FC | Zack Gelof | 12 | 0.500 | 1.100 | 0.600 | 0.633 | 0.560 | 18.2% | 22.2% | 26.7% |
| FC | Max Muncy | 32 | 0.276 | 0.724 | 0.448 | 0.439 | 0.421 | 16.7% | 28.6% | 18.5% |
| FF | Shea Langeliers | 84 | 0.243 | 0.635 | 0.392 | 0.405 | 0.396 | 22.0% | 24.1% | 23.6% |
| FF | Brent Rooker | 58 | 0.184 | 0.571 | 0.388 | 0.356 | 0.355 | 29.6% | 26.3% | 29.3% |
| FC | Brent Rooker | 8 | 0.500 | 0.875 | 0.375 | 0.588 | 0.398 | 28.6% | 33.3% | 23.8% |
| FF | Max Muncy | 134 | 0.360 | 0.730 | 0.369 | 0.500 | 0.474 | 22.6% | 32.9% | 18.1% |
| FF | Nick Kurtz | 112 | 0.253 | 0.621 | 0.368 | 0.437 | 0.465 | 28.0% | 34.1% | 32.4% |
| FC | Jacob Wilson | 12 | 0.250 | 0.583 | 0.333 | 0.346 | 0.261 | 10.0% | 26.7% | 30.8% |
| FF | Zack Gelof | 68 | 0.226 | 0.516 | 0.290 | 0.356 | 0.279 | 10.3% | 27.2% | 27.6% |
| CH | Henry Bolte | 12 | 0.545 | 0.818 | 0.273 | 0.600 | 0.427 | 11.1% | 35.7% | 31.8% |
| FC | Tyler Soderstrom | 28 | 0.308 | 0.577 | 0.269 | 0.398 | 0.390 | 4.8% | 46.7% | 10.5% |
| FC | Lawrence Butler | 24 | 0.211 | 0.421 | 0.211 | 0.356 | 0.402 | 13.3% | 23.3% | 23.3% |
| FF | Henry Bolte | 28 | 0.320 | 0.520 | 0.200 | 0.396 | 0.313 | 21.4% | 25.0% | 35.1% |
| CH | Zack Gelof | 17 | 0.267 | 0.467 | 0.200 | 0.412 | 0.391 | 18.2% | 33.3% | 29.4% |
| FF | Tyler Soderstrom | 96 | 0.237 | 0.434 | 0.197 | 0.371 | 0.379 | 12.1% | 24.6% | 16.1% |
| CH | Jeff Mcneil | 38 | 0.189 | 0.378 | 0.189 | 0.251 | 0.286 | 2.9% | 21.7% | 17.7% |
| FC | Nick Kurtz | 23 | 0.250 | 0.438 | 0.188 | 0.417 | 0.517 | 25.0% | 18.8% | 33.3% |
| FC | Shea Langeliers | 25 | 0.304 | 0.478 | 0.174 | 0.366 | 0.393 | 15.0% | 24.3% | 30.0% |
| CH | Carlos Cortes | 34 | 0.233 | 0.400 | 0.167 | 0.321 | 0.279 | 8.0% | 15.4% | 32.2% |
| FC | Jeff Mcneil | 24 | 0.381 | 0.524 | 0.143 | 0.431 | 0.278 | 0.0% | 14.6% | 23.6% |
| FF | Lawrence Butler | 72 | 0.185 | 0.323 | 0.138 | 0.276 | 0.322 | 7.3% | 26.2% | 26.8% |
| CH | Brent Rooker | 24 | 0.174 | 0.304 | 0.130 | 0.263 | 0.197 | 18.2% | 21.7% | 44.9% |
| FF | Carlos Cortes | 65 | 0.309 | 0.418 | 0.109 | 0.376 | 0.412 | 8.3% | 19.2% | 9.4% |
| CH | Lawrence Butler | 34 | 0.344 | 0.438 | 0.094 | 0.391 | 0.324 | 7.1% | 25.6% | 30.6% |
| FF | Jacob Wilson | 52 | 0.217 | 0.304 | 0.087 | 0.268 | 0.265 | 2.8% | 13.8% | 14.8% |
| CH | Max Muncy | 63 | 0.259 | 0.345 | 0.086 | 0.313 | 0.331 | 8.7% | 29.9% | 30.2% |
| CH | Nick Kurtz | 47 | 0.175 | 0.250 | 0.075 | 0.280 | 0.306 | 15.4% | 20.0% | 33.3% |
| CH | Jacob Wilson | 32 | 0.226 | 0.290 | 0.065 | 0.281 | 0.233 | 0.0% | 20.6% | 16.7% |
| FF | Darell Hernaiz | 43 | 0.257 | 0.314 | 0.057 | 0.312 | 0.285 | 0.0% | 10.7% | 15.0% |


## Athletics Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nick Kurtz | 393 | 0.278 | 0.519 | 0.241 | 0.404 | 0.393 | 19.0% | 32.9% | 32.1% |
| Shea Langeliers | 356 | 0.268 | 0.508 | 0.240 | 0.364 | 0.365 | 14.3% | 28.3% | 24.7% |
| Tyler Soderstrom | 348 | 0.240 | 0.463 | 0.223 | 0.359 | 0.337 | 10.1% | 28.5% | 19.9% |
| Jeff Mcneil | 281 | 0.226 | 0.302 | 0.075 | 0.278 | 0.304 | 0.9% | 18.4% | 14.7% |
| Lawrence Butler | 241 | 0.200 | 0.316 | 0.116 | 0.284 | 0.312 | 7.6% | 26.0% | 26.5% |
| Zack Gelof | 238 | 0.276 | 0.484 | 0.207 | 0.368 | 0.299 | 6.8% | 27.6% | 25.1% |
| Jacob Wilson | 227 | 0.274 | 0.377 | 0.102 | 0.312 | 0.279 | 1.6% | 20.7% | 13.1% |
| Carlos Cortes | 218 | 0.259 | 0.409 | 0.150 | 0.331 | 0.355 | 8.0% | 23.9% | 19.1% |
| Brent Rooker | 215 | 0.214 | 0.411 | 0.198 | 0.316 | 0.315 | 16.5% | 26.9% | 35.2% |
| Max Muncy | 172 | 0.234 | 0.442 | 0.208 | 0.327 | 0.300 | 12.9% | 32.2% | 29.7% |
| Henry Bolte | 160 | 0.297 | 0.391 | 0.094 | 0.352 | 0.306 | 6.7% | 29.5% | 33.0% |
| Darell Hernaiz | 145 | 0.248 | 0.302 | 0.054 | 0.292 | 0.263 | 1.0% | 13.7% | 19.9% |


## Los Angeles Angels Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Zach Neto | 384 | 0.222 | 0.441 | 0.219 | 0.335 | 0.313 | 13.0% | 23.1% | 31.4% |
| Jo Adell | 369 | 0.255 | 0.412 | 0.157 | 0.309 | 0.322 | 8.7% | 26.8% | 25.6% |
| Mike Trout | 353 | 0.240 | 0.473 | 0.233 | 0.390 | 0.412 | 20.2% | 26.5% | 20.4% |
| Nolan Schanuel | 291 | 0.257 | 0.383 | 0.126 | 0.334 | 0.323 | 2.4% | 19.0% | 16.1% |
| Jorge Soler | 283 | 0.226 | 0.435 | 0.210 | 0.330 | 0.310 | 12.0% | 27.0% | 34.6% |
| Oswald Peraza | 265 | 0.257 | 0.402 | 0.145 | 0.327 | 0.299 | 8.0% | 22.1% | 25.6% |
| Logan O'Hoppe | 213 | 0.225 | 0.335 | 0.110 | 0.284 | 0.276 | 9.9% | 25.4% | 26.1% |
| Vaughn Grissom | 177 | 0.234 | 0.377 | 0.143 | 0.316 | 0.341 | 6.6% | 25.6% | 17.5% |
| Josh Lowe | 162 | 0.217 | 0.362 | 0.145 | 0.274 | 0.265 | 7.6% | 17.1% | 25.6% |
| Yoán Moncada | 147 | 0.202 | 0.306 | 0.105 | 0.295 | 0.270 | 8.6% | 22.7% | 29.4% |
| Adam Frazier | 115 | 0.198 | 0.312 | 0.115 | 0.285 | 0.237 | 2.9% | 9.8% | 24.5% |
| Wade Meckler | 113 | 0.270 | 0.400 | 0.130 | 0.353 | 0.311 | 6.7% | 18.3% | 22.7% |


## Bullpen Fatigue Report

### Athletics Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Elvis Alvarado | 2026-06-24 | 0.2 | 12 |
| Elvis Alvarado | 2026-06-26 | 1.0 | 15 |
| Geoff Hartlieb | 2026-06-25 | 2.0 | 25 |
| Geoff Hartlieb | 2026-06-27 | 0.2 | 9 |
| Hogan Harris | 2026-06-24 | 1.0 | 16 |
| Hogan Harris | 2026-06-26 | 0.2 | 15 |
| Justin Sterner | 2026-06-24 | 1.0 | 10 |
| Justin Sterner | 2026-06-25 | 0.1 | 7 |
| Justin Sterner | 2026-06-27 | 1.0 | 17 |
| Luis Medina | 2026-06-24 | 1.0 | 21 |
| Luis Medina | 2026-06-26 | 1.1 | 38 |
| Mason Barnett | 2026-06-25 | 1.0 | 13 |
| Mason Barnett | 2026-06-27 | 0.2 | 7 |
| Matt Krook | 2026-06-25 | 0.1 | 13 |
| Matt Krook | 2026-06-27 | 0.2 | 12 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Geoff Hartlieb, Justin Sterner, Mason Barnett, Matt Krook


### Los Angeles Angels Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brent Suter | 2026-06-26 | 2.1 | 52 |
| Chase Silseth | 2026-06-24 | 1.0 | 12 |
| Chase Silseth | 2026-06-27 | 0.1 | 9 |
| José Fermin | 2026-06-24 | 1.1 | 14 |
| José Fermin | 2026-06-26 | 1.1 | 14 |
| Kirby Yates | 2026-06-26 | 1.0 | 13 |
| Kirby Yates | 2026-06-27 | 1.0 | 9 |
| Mitch Farris | 2026-06-24 | 2.0 | 27 |
| Ryan Zeferjahn | 2026-06-27 | 1.0 | 16 |
| Sam Bachman | 2026-06-24 | 1.0 | 15 |
| Sam Bachman | 2026-06-27 | 1.0 | 26 |
| Samy Natera Jr. | 2026-06-24 | 1.2 | 27 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Chase Silseth, Kirby Yates, Ryan Zeferjahn, Sam Bachman



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nick Kurtz | 393 | 0.278 | 0.519 | 0.241 | 0.404 | 19.0% | 32.9% |
| 2 | Shea Langeliers | 356 | 0.268 | 0.508 | 0.240 | 0.364 | 14.3% | 28.3% |
| 3 | Tyler Soderstrom | 348 | 0.240 | 0.463 | 0.223 | 0.359 | 10.1% | 28.5% |
| 4 | Jeff Mcneil | 281 | 0.226 | 0.302 | 0.075 | 0.278 | 0.9% | 18.4% |
| 5 | Lawrence Butler | 241 | 0.200 | 0.316 | 0.116 | 0.284 | 7.6% | 26.0% |
| 6 | Zack Gelof | 238 | 0.276 | 0.484 | 0.207 | 0.368 | 6.8% | 27.6% |
| 7 | Jacob Wilson | 227 | 0.274 | 0.377 | 0.102 | 0.312 | 1.6% | 20.7% |
| 8 | Carlos Cortes | 218 | 0.259 | 0.409 | 0.150 | 0.331 | 8.0% | 23.9% |
| 9 | Brent Rooker | 215 | 0.214 | 0.411 | 0.198 | 0.316 | 16.5% | 26.9% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Zach Neto | 384 | 0.222 | 0.441 | 0.219 | 0.335 | 13.0% | 23.1% |
| 2 | Jo Adell | 369 | 0.255 | 0.412 | 0.157 | 0.309 | 8.7% | 26.8% |
| 3 | Mike Trout | 353 | 0.240 | 0.473 | 0.233 | 0.390 | 20.2% | 26.5% |
| 4 | Nolan Schanuel | 291 | 0.257 | 0.383 | 0.126 | 0.334 | 2.4% | 19.0% |
| 5 | Jorge Soler | 283 | 0.226 | 0.435 | 0.210 | 0.330 | 12.0% | 27.0% |
| 6 | Oswald Peraza | 265 | 0.257 | 0.402 | 0.145 | 0.327 | 8.0% | 22.1% |
| 7 | Logan O'Hoppe | 213 | 0.225 | 0.335 | 0.110 | 0.284 | 9.9% | 25.4% |
| 8 | Vaughn Grissom | 177 | 0.234 | 0.377 | 0.143 | 0.316 | 6.6% | 25.6% |
| 9 | Josh Lowe | 162 | 0.217 | 0.362 | 0.145 | 0.274 | 7.6% | 17.1% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7100 |
| Hits Allowed | 1595 |
| Walks/HBP | 744 |
| Strikeouts | 1559 |
| Home Runs Allowed | 253 |
| K Event Rate | 22.0% |
| BB/HBP Event Rate | 10.5% |
| HR Event Rate | 3.6% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7254 |
| Hits Allowed | 1502 |
| Walks/HBP | 848 |
| Strikeouts | 1736 |
| Home Runs Allowed | 214 |
| K Event Rate | 23.9% |
| BB/HBP Event Rate | 11.7% |
| HR Event Rate | 3.0% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FC, CU, SI, FF
- Home pitcher pitch mix to inspect: FF, CH, FC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 13. Atlanta Braves @ San Francisco Giants

## Game Context

| Field | Value |
| --- | --- |
| Park | Oracle Park |
| Time | 2026-06-28T20:05:00Z |
| Away Team | Atlanta Braves |
| Home Team | San Francisco Giants |
| Away Probable Pitcher | Chris Sale |
| Home Probable Pitcher | Robbie Ray |


## Away Starting Pitcher: Chris Sale

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1512 |
| Batted/Result Events | 387 |
| Hits Allowed | 74 |
| Walks | 22 |
| Strikeouts | 106 |
| Home Runs | 7 |
| K Event Rate | 27.4% |
| BB Event Rate | 5.7% |
| HR Event Rate | 1.8% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-20 | ATL | 7.7 | 5 | 0 | 1 | 7 | 0 |
| 2026-06-10 | CWS | 8.3 | 6 | 0 | 2 | 6 | 0 |
| 2026-06-04 | ATL | 9.7 | 10 | 0 | 3 | 6 | 0 |
| 2026-05-28 | BOS | 8.3 | 6 | 0 | 4 | 8 | 0 |
| 2026-05-20 | MIA | 8.3 | 4 | 0 | 0 | 8 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.5% | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.171 | 100.0% | 66.7% | 40.0% |
| CH | vs R | 11.5% | 174 | 0.302 | 0.395 | 0.093 | 0.319 | 0.297 | 2.3% | 31.0% | 27.8% |
| FF | vs L | 7.1% | 107 | 0.174 | 0.348 | 0.174 | 0.310 | 0.272 | 7.7% | 16.7% | 24.5% |
| FF | vs R | 32.9% | 497 | 0.245 | 0.400 | 0.155 | 0.316 | 0.363 | 7.2% | 22.5% | 19.5% |
| SI | vs L | 7.3% | 111 | 0.208 | 0.208 | 0.000 | 0.226 | 0.288 | 0.0% | 15.2% | 9.1% |
| SI | vs R | 0.5% | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 33.3% |
| SL | vs L | 10.0% | 151 | 0.184 | 0.289 | 0.105 | 0.227 | 0.208 | 16.7% | 19.4% | 48.5% |
| SL | vs R | 30.1% | 455 | 0.161 | 0.196 | 0.036 | 0.220 | 0.242 | 3.0% | 10.4% | 34.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-20 | 101 | 5 | 1 | 7 | 0 |
| 2026-06-10 | 104 | 6 | 1 | 6 | 0 |
| 2026-06-04 | 108 | 10 | 2 | 6 | 0 |
| 2026-05-28 | 96 | 6 | 3 | 8 | 0 |
| 2026-05-20 | 96 | 4 | 0 | 8 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | Casey Schmitt | 23 | 0.435 | 1.000 | 0.565 | 0.598 | 0.512 | 21.1% | 28.1% | 26.5% |
| SL | Heliot Ramos | 20 | 0.450 | 0.900 | 0.450 | 0.568 | 0.417 | 12.5% | 28.6% | 31.1% |
| FF | Bryce Eldridge | 56 | 0.295 | 0.705 | 0.409 | 0.476 | 0.507 | 25.7% | 34.6% | 11.6% |
| FF | Willy Adames | 97 | 0.239 | 0.609 | 0.370 | 0.368 | 0.333 | 11.8% | 26.9% | 21.9% |
| SL | Harrison Bader | 20 | 0.250 | 0.550 | 0.300 | 0.333 | 0.346 | 16.7% | 37.5% | 48.5% |
| FF | Rafael Devers | 139 | 0.205 | 0.457 | 0.252 | 0.312 | 0.303 | 17.6% | 28.5% | 36.2% |
| SL | Rafael Devers | 39 | 0.243 | 0.486 | 0.243 | 0.309 | 0.281 | 7.1% | 28.3% | 34.6% |
| SL | Bryce Eldridge | 23 | 0.318 | 0.545 | 0.227 | 0.383 | 0.193 | 0.0% | 33.3% | 27.3% |
| FF | Drew Gilbert | 66 | 0.302 | 0.528 | 0.226 | 0.420 | 0.352 | 2.3% | 22.4% | 16.3% |
| FF | Jung Hoo Lee | 106 | 0.398 | 0.602 | 0.204 | 0.445 | 0.341 | 4.4% | 22.1% | 7.9% |
| FF | Harrison Bader | 34 | 0.133 | 0.333 | 0.200 | 0.253 | 0.254 | 4.5% | 21.6% | 20.0% |
| FF | Heliot Ramos | 41 | 0.256 | 0.436 | 0.179 | 0.337 | 0.320 | 13.0% | 14.5% | 25.0% |
| SL | Matt Chapman | 49 | 0.182 | 0.341 | 0.159 | 0.269 | 0.283 | 12.1% | 29.1% | 29.4% |
| CH | Luis Arráez | 36 | 0.152 | 0.303 | 0.152 | 0.194 | 0.239 | 2.9% | 14.5% | 4.9% |
| CH | Matt Chapman | 33 | 0.286 | 0.429 | 0.143 | 0.367 | 0.374 | 10.5% | 38.2% | 22.0% |
| FF | Luis Arráez | 133 | 0.352 | 0.488 | 0.136 | 0.373 | 0.312 | 0.0% | 14.9% | 8.5% |
| CH | Bryce Eldridge | 23 | 0.273 | 0.409 | 0.136 | 0.311 | 0.415 | 20.0% | 21.7% | 35.9% |
| CH | Drew Gilbert | 24 | 0.217 | 0.348 | 0.130 | 0.298 | 0.278 | 0.0% | 18.5% | 25.0% |
| SL | Patrick Bailey | 24 | 0.292 | 0.417 | 0.125 | 0.308 | 0.252 | 6.2% | 22.9% | 30.9% |
| FF | Daniel Susac | 26 | 0.200 | 0.320 | 0.120 | 0.221 | 0.214 | 5.3% | 16.3% | 13.3% |
| SL | Willy Adames | 55 | 0.135 | 0.250 | 0.115 | 0.208 | 0.168 | 11.1% | 23.5% | 42.1% |
| SL | Daniel Susac | 21 | 0.389 | 0.500 | 0.111 | 0.400 | 0.345 | 6.2% | 16.7% | 28.3% |
| CH | Rafael Devers | 37 | 0.216 | 0.324 | 0.108 | 0.232 | 0.349 | 12.5% | 36.5% | 16.4% |
| FF | Casey Schmitt | 94 | 0.247 | 0.348 | 0.101 | 0.282 | 0.339 | 10.8% | 26.1% | 16.5% |
| CH | Harrison Bader | 10 | 0.300 | 0.400 | 0.100 | 0.305 | 0.290 | 20.0% | 23.1% | 34.8% |
| CH | Daniel Susac | 12 | 0.250 | 0.333 | 0.083 | 0.254 | 0.186 | 0.0% | 15.8% | 39.4% |
| FF | Patrick Bailey | 58 | 0.226 | 0.302 | 0.075 | 0.272 | 0.294 | 8.8% | 21.3% | 20.0% |
| SL | Luis Arráez | 30 | 0.222 | 0.296 | 0.074 | 0.233 | 0.284 | 0.0% | 13.8% | 13.2% |
| SL | Casey Schmitt | 41 | 0.195 | 0.268 | 0.073 | 0.201 | 0.264 | 17.2% | 42.9% | 31.8% |
| CH | Heliot Ramos | 15 | 0.286 | 0.357 | 0.071 | 0.310 | 0.399 | 11.1% | 31.2% | 29.6% |


## Home Starting Pitcher: Robbie Ray

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1676 |
| Batted/Result Events | 403 |
| Hits Allowed | 73 |
| Walks | 44 |
| Strikeouts | 94 |
| Home Runs | 15 |
| K Event Rate | 23.3% |
| BB Event Rate | 10.9% |
| HR Event Rate | 3.7% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | SF | 9.7 | 2 | 0 | 4 | 6 | 0 |
| 2026-06-16 | ATL | 7.7 | 2 | 0 | 2 | 8 | 0 |
| 2026-06-10 | SF | 8.0 | 7 | 1 | 0 | 3 | 1 |
| 2026-06-05 | CHC | 7.0 | 2 | 0 | 5 | 4 | 0 |
| 2026-05-31 | COL | 6.3 | 5 | 0 | 2 | 6 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.1% | 2 | 1.000 | 3.000 | 2.000 | 1.600 | 0.836 | 100.0% | 50.0% | 0.0% |
| CH | vs R | 15.3% | 257 | 0.192 | 0.247 | 0.055 | 0.213 | 0.232 | 1.8% | 17.7% | 27.0% |
| FF | vs L | 11.2% | 188 | 0.293 | 0.463 | 0.171 | 0.348 | 0.336 | 12.1% | 20.0% | 20.5% |
| FF | vs R | 30.8% | 517 | 0.212 | 0.500 | 0.288 | 0.358 | 0.387 | 15.4% | 18.9% | 15.4% |
| KC | vs L | 2.5% | 42 | 0.200 | 0.300 | 0.100 | 0.259 | 0.307 | 0.0% | 22.2% | 42.9% |
| KC | vs R | 6.0% | 100 | 0.100 | 0.100 | 0.000 | 0.192 | 0.328 | 0.0% | 33.3% | 30.8% |
| SI | vs L | 1.3% | 22 | 0.000 | 0.000 | 0.000 | 0.100 | 0.292 | 0.0% | 12.5% | 0.0% |
| SI | vs R | 5.4% | 90 | 0.200 | 0.250 | 0.050 | 0.311 | 0.365 | 9.5% | 28.6% | 2.7% |
| SL | vs L | 13.1% | 220 | 0.125 | 0.146 | 0.021 | 0.164 | 0.261 | 3.6% | 15.5% | 38.5% |
| SL | vs R | 14.2% | 238 | 0.282 | 0.615 | 0.333 | 0.459 | 0.444 | 22.2% | 37.1% | 29.5% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 102 | 2 | 4 | 6 | 0 |
| 2026-06-16 | 94 | 2 | 2 | 8 | 0 |
| 2026-06-10 | 93 | 7 | 0 | 3 | 1 |
| 2026-06-05 | 97 | 2 | 5 | 4 | 0 |
| 2026-05-31 | 96 | 5 | 2 | 6 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Eli White | 12 | 0.300 | 0.700 | 0.400 | 0.462 | 0.305 | 14.3% | 30.8% | 34.8% |
| FF | Matt Olson | 107 | 0.250 | 0.587 | 0.337 | 0.390 | 0.405 | 20.0% | 27.3% | 19.5% |
| FF | Drake Baldwin | 76 | 0.277 | 0.600 | 0.323 | 0.415 | 0.436 | 21.3% | 31.2% | 16.7% |
| SL | Matt Olson | 40 | 0.325 | 0.625 | 0.300 | 0.425 | 0.375 | 10.7% | 39.6% | 29.4% |
| SL | Drake Baldwin | 35 | 0.273 | 0.545 | 0.273 | 0.364 | 0.261 | 20.0% | 22.7% | 41.0% |
| SL | Mauricio Dubón | 41 | 0.316 | 0.579 | 0.263 | 0.448 | 0.357 | 10.7% | 21.6% | 26.3% |
| CH | Mike Yastrzemski | 30 | 0.286 | 0.536 | 0.250 | 0.372 | 0.260 | 9.1% | 26.3% | 16.0% |
| FF | Ozzie Albies | 88 | 0.284 | 0.527 | 0.243 | 0.361 | 0.359 | 9.0% | 30.8% | 15.6% |
| CH | Matt Olson | 36 | 0.143 | 0.371 | 0.229 | 0.225 | 0.226 | 12.5% | 26.5% | 20.0% |
| SL | Michael Harris | 46 | 0.261 | 0.478 | 0.217 | 0.348 | 0.329 | 17.1% | 37.0% | 29.1% |
| CH | Michael Harris | 43 | 0.333 | 0.548 | 0.214 | 0.407 | 0.426 | 18.4% | 38.0% | 23.9% |
| FF | Dominic Smith | 62 | 0.389 | 0.593 | 0.204 | 0.440 | 0.467 | 12.0% | 24.0% | 7.0% |
| KC | Matt Olson | 6 | 0.600 | 0.800 | 0.200 | 0.625 | 0.364 | 0.0% | 44.4% | 23.1% |
| SL | Mike Yastrzemski | 28 | 0.115 | 0.308 | 0.192 | 0.211 | 0.256 | 11.1% | 39.3% | 26.8% |
| FF | Michael Harris | 62 | 0.273 | 0.455 | 0.182 | 0.369 | 0.354 | 9.3% | 24.3% | 18.8% |
| FF | Austin Riley | 119 | 0.231 | 0.404 | 0.173 | 0.325 | 0.311 | 11.9% | 32.5% | 27.1% |
| CH | Ronald Acuña | 27 | 0.292 | 0.458 | 0.167 | 0.363 | 0.332 | 11.8% | 27.6% | 26.1% |
| FF | Eli White | 33 | 0.226 | 0.387 | 0.161 | 0.288 | 0.247 | 4.8% | 12.5% | 17.6% |
| FF | Jorge Mateo | 37 | 0.394 | 0.545 | 0.152 | 0.470 | 0.434 | 6.9% | 21.9% | 13.0% |
| CH | Ozzie Albies | 71 | 0.200 | 0.343 | 0.143 | 0.264 | 0.245 | 3.2% | 18.6% | 17.4% |
| SL | Ozzie Albies | 30 | 0.345 | 0.483 | 0.138 | 0.372 | 0.306 | 4.2% | 17.8% | 20.0% |
| FF | Mike Yastrzemski | 83 | 0.233 | 0.356 | 0.123 | 0.329 | 0.303 | 3.6% | 25.7% | 21.9% |
| FF | Mauricio Dubón | 97 | 0.222 | 0.333 | 0.111 | 0.273 | 0.292 | 2.7% | 17.1% | 12.0% |
| SL | Ronald Acuña | 24 | 0.333 | 0.444 | 0.111 | 0.400 | 0.318 | 6.7% | 25.0% | 25.5% |
| CH | Austin Riley | 36 | 0.219 | 0.312 | 0.094 | 0.263 | 0.247 | 4.8% | 41.2% | 41.8% |
| SL | Austin Riley | 33 | 0.333 | 0.400 | 0.067 | 0.336 | 0.362 | 10.7% | 27.9% | 31.9% |
| SL | Jorge Mateo | 18 | 0.176 | 0.235 | 0.059 | 0.169 | 0.208 | 10.0% | 21.1% | 47.4% |
| FF | Ronald Acuña | 74 | 0.138 | 0.172 | 0.034 | 0.258 | 0.289 | 8.8% | 14.9% | 31.4% |
| CH | Drake Baldwin | 36 | 0.258 | 0.290 | 0.032 | 0.307 | 0.306 | 0.0% | 31.4% | 33.9% |
| CH | Mauricio Dubón | 37 | 0.086 | 0.114 | 0.029 | 0.145 | 0.245 | 3.1% | 16.0% | 11.5% |


## Atlanta Braves Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Matt Olson | 372 | 0.275 | 0.536 | 0.260 | 0.374 | 0.362 | 14.0% | 31.1% | 20.2% |
| Ozzie Albies | 365 | 0.270 | 0.426 | 0.156 | 0.332 | 0.304 | 3.8% | 21.6% | 17.9% |
| Austin Riley | 346 | 0.218 | 0.367 | 0.149 | 0.300 | 0.298 | 11.3% | 29.2% | 29.1% |
| Mauricio Dubón | 328 | 0.270 | 0.417 | 0.147 | 0.338 | 0.320 | 5.0% | 18.8% | 14.2% |
| Michael Harris | 307 | 0.289 | 0.478 | 0.189 | 0.354 | 0.377 | 14.8% | 34.4% | 23.0% |
| Drake Baldwin | 277 | 0.270 | 0.496 | 0.225 | 0.372 | 0.377 | 17.5% | 28.3% | 23.8% |
| Ronald Acuña | 244 | 0.254 | 0.428 | 0.174 | 0.359 | 0.378 | 12.8% | 25.3% | 26.3% |
| Mike Yastrzemski | 235 | 0.230 | 0.378 | 0.148 | 0.316 | 0.289 | 4.6% | 25.5% | 21.5% |
| Dominic Smith | 212 | 0.267 | 0.398 | 0.131 | 0.327 | 0.327 | 7.1% | 22.7% | 18.1% |
| Jorge Mateo | 130 | 0.275 | 0.433 | 0.158 | 0.345 | 0.332 | 9.2% | 26.0% | 26.9% |
| Eli White | 121 | 0.245 | 0.436 | 0.191 | 0.344 | 0.284 | 8.2% | 21.7% | 24.8% |
| Ha-Seong Kim | 79 | 0.070 | 0.070 | 0.000 | 0.128 | 0.209 | 4.3% | 14.4% | 18.2% |


## San Francisco Giants Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rafael Devers | 355 | 0.243 | 0.455 | 0.212 | 0.324 | 0.305 | 11.3% | 28.3% | 28.1% |
| Matt Chapman | 352 | 0.245 | 0.395 | 0.150 | 0.334 | 0.293 | 7.5% | 23.5% | 20.4% |
| Willy Adames | 350 | 0.229 | 0.431 | 0.202 | 0.313 | 0.290 | 9.4% | 25.1% | 27.2% |
| Luis Arráez | 347 | 0.321 | 0.442 | 0.122 | 0.351 | 0.304 | 0.3% | 13.1% | 7.0% |
| Casey Schmitt | 327 | 0.289 | 0.500 | 0.211 | 0.351 | 0.358 | 11.7% | 28.1% | 20.4% |
| Jung Hoo Lee | 313 | 0.329 | 0.479 | 0.151 | 0.369 | 0.328 | 3.0% | 20.7% | 10.9% |
| Drew Gilbert | 203 | 0.237 | 0.367 | 0.130 | 0.314 | 0.293 | 2.1% | 22.4% | 19.7% |
| Heliot Ramos | 188 | 0.261 | 0.420 | 0.159 | 0.319 | 0.326 | 12.8% | 24.5% | 24.4% |
| Bryce Eldridge | 171 | 0.274 | 0.473 | 0.199 | 0.368 | 0.374 | 12.3% | 29.4% | 22.1% |
| Daniel Susac | 128 | 0.270 | 0.357 | 0.087 | 0.293 | 0.286 | 5.6% | 17.3% | 23.6% |
| Harrison Bader | 114 | 0.167 | 0.352 | 0.185 | 0.244 | 0.272 | 8.2% | 25.0% | 30.6% |
| Patrick Bailey | 102 | 0.160 | 0.191 | 0.032 | 0.198 | 0.283 | 4.3% | 25.6% | 24.6% |


## Bullpen Fatigue Report

### Atlanta Braves Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Didier Fuentes | 2026-06-24 | 1.0 | 15 |
| Didier Fuentes | 2026-06-26 | 0.1 | 3 |
| Dylan Dodd | 2026-06-24 | 0.1 | 11 |
| Dylan Dodd | 2026-06-26 | 1.0 | 10 |
| Dylan Lee | 2026-06-26 | 1.2 | 13 |
| Grant Holmes | 2026-06-27 | 4.0 | 47 |
| Hurston Waldrep | 2026-06-26 | 2.0 | 55 |
| Ian Hamilton | 2026-06-24 | 1.0 | 14 |
| James Karinchak | 2026-06-24 | 1.0 | 17 |
| Raisel Iglesias | 2026-06-26 | 1.0 | 10 |
| Tyler Kinley | 2026-06-24 | 0.2 | 10 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Grant Holmes


### San Francisco Giants Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Adrian Houser | 2026-06-26 | 2.1 | 35 |
| Caleb Kilian | 2026-06-25 | 0.2 | 23 |
| Dylan Smith | 2026-06-24 | 1.0 | 13 |
| Dylan Smith | 2026-06-25 | 1.0 | 25 |
| Erik Miller | 2026-06-24 | 1.0 | 14 |
| Erik Miller | 2026-06-25 | 0.1 | 12 |
| Matt Gage | 2026-06-25 | 0.1 | 10 |
| Matt Gage | 2026-06-26 | 0.2 | 12 |
| Ryan Walker | 2026-06-24 | 1.0 | 14 |
| Ryan Walker | 2026-06-25 | 0.2 | 7 |
| Ryan Walker | 2026-06-27 | 1.0 | 23 |
| Sam Hentges | 2026-06-24 | 0.1 | 1 |
| Sam Hentges | 2026-06-26 | 0.2 | 11 |
| Sam Hentges | 2026-06-27 | 1.0 | 11 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Ryan Walker, Sam Hentges



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Olson | 372 | 0.275 | 0.536 | 0.260 | 0.374 | 14.0% | 31.1% |
| 2 | Ozzie Albies | 365 | 0.270 | 0.426 | 0.156 | 0.332 | 3.8% | 21.6% |
| 3 | Austin Riley | 346 | 0.218 | 0.367 | 0.149 | 0.300 | 11.3% | 29.2% |
| 4 | Mauricio Dubón | 328 | 0.270 | 0.417 | 0.147 | 0.338 | 5.0% | 18.8% |
| 5 | Michael Harris | 307 | 0.289 | 0.478 | 0.189 | 0.354 | 14.8% | 34.4% |
| 6 | Drake Baldwin | 277 | 0.270 | 0.496 | 0.225 | 0.372 | 17.5% | 28.3% |
| 7 | Ronald Acuña | 244 | 0.254 | 0.428 | 0.174 | 0.359 | 12.8% | 25.3% |
| 8 | Mike Yastrzemski | 235 | 0.230 | 0.378 | 0.148 | 0.316 | 4.6% | 25.5% |
| 9 | Dominic Smith | 212 | 0.267 | 0.398 | 0.131 | 0.327 | 7.1% | 22.7% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Rafael Devers | 355 | 0.243 | 0.455 | 0.212 | 0.324 | 11.3% | 28.3% |
| 2 | Matt Chapman | 352 | 0.245 | 0.395 | 0.150 | 0.334 | 7.5% | 23.5% |
| 3 | Willy Adames | 350 | 0.229 | 0.431 | 0.202 | 0.313 | 9.4% | 25.1% |
| 4 | Luis Arráez | 347 | 0.321 | 0.442 | 0.122 | 0.351 | 0.3% | 13.1% |
| 5 | Casey Schmitt | 327 | 0.289 | 0.500 | 0.211 | 0.351 | 11.7% | 28.1% |
| 6 | Jung Hoo Lee | 313 | 0.329 | 0.479 | 0.151 | 0.369 | 3.0% | 20.7% |
| 7 | Drew Gilbert | 203 | 0.237 | 0.367 | 0.130 | 0.314 | 2.1% | 22.4% |
| 8 | Heliot Ramos | 188 | 0.261 | 0.420 | 0.159 | 0.319 | 12.8% | 24.5% |
| 9 | Bryce Eldridge | 171 | 0.274 | 0.473 | 0.199 | 0.368 | 12.3% | 29.4% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6698 |
| Hits Allowed | 1420 |
| Walks/HBP | 611 |
| Strikeouts | 1478 |
| Home Runs Allowed | 202 |
| K Event Rate | 22.1% |
| BB/HBP Event Rate | 9.1% |
| HR Event Rate | 3.0% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6722 |
| Hits Allowed | 1512 |
| Walks/HBP | 602 |
| Strikeouts | 1389 |
| Home Runs Allowed | 187 |
| K Event Rate | 20.7% |
| BB/HBP Event Rate | 9.0% |
| HR Event Rate | 2.8% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: SL, FF, CH
- Home pitcher pitch mix to inspect: FF, SL, CH, KC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 14. Los Angeles Dodgers @ San Diego Padres

## Game Context

| Field | Value |
| --- | --- |
| Park | Petco Park |
| Time | 2026-06-28T20:10:00Z |
| Away Team | Los Angeles Dodgers |
| Home Team | San Diego Padres |
| Away Probable Pitcher | Emmet Sheehan |
| Home Probable Pitcher | Michael King |


## Away Starting Pitcher: Emmet Sheehan

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1333 |
| Batted/Result Events | 326 |
| Hits Allowed | 74 |
| Walks | 23 |
| Strikeouts | 85 |
| Home Runs | 15 |
| K Event Rate | 26.1% |
| BB Event Rate | 7.1% |
| HR Event Rate | 4.6% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-21 | LAD | 7.0 | 8 | 2 | 3 | 4 | 2 |
| 2026-06-14 | CWS | 7.0 | 4 | 1 | 2 | 8 | 1 |
| 2026-06-07 | LAD | 3.0 | 3 | 0 | 2 | 2 | 0 |
| 2026-06-01 | AZ | 7.3 | 3 | 2 | 0 | 3 | 2 |
| 2026-05-25 | LAD | 8.0 | 5 | 0 | 2 | 8 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 13.4% | 179 | 0.298 | 0.421 | 0.123 | 0.331 | 0.275 | 0.0% | 31.3% | 23.4% |
| CH | vs R | 2.0% | 26 | 0.143 | 0.143 | 0.000 | 0.200 | 0.210 | 0.0% | 22.2% | 16.7% |
| CU | vs L | 6.6% | 88 | 0.273 | 0.364 | 0.091 | 0.312 | 0.286 | 0.0% | 27.3% | 14.8% |
| CU | vs R | 2.7% | 36 | 0.400 | 0.600 | 0.200 | 0.430 | 0.345 | 0.0% | 25.0% | 33.3% |
| FF | vs L | 24.8% | 330 | 0.254 | 0.712 | 0.458 | 0.423 | 0.395 | 22.7% | 24.6% | 26.7% |
| FF | vs R | 18.8% | 251 | 0.240 | 0.500 | 0.260 | 0.371 | 0.397 | 15.0% | 26.9% | 22.1% |
| SL | vs L | 10.7% | 143 | 0.222 | 0.472 | 0.250 | 0.322 | 0.288 | 13.6% | 26.1% | 34.2% |
| SL | vs R | 20.9% | 278 | 0.225 | 0.366 | 0.141 | 0.286 | 0.243 | 8.9% | 19.2% | 41.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-21 | 82 | 8 | 3 | 4 | 2 |
| 2026-06-14 | 85 | 4 | 1 | 8 | 1 |
| 2026-06-07 | 49 | 3 | 2 | 2 | 0 |
| 2026-06-01 | 92 | 3 | 0 | 3 | 2 |
| 2026-05-25 | 92 | 5 | 1 | 8 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Freddy Fermin | 6 | 0.250 | 1.000 | 0.750 | 0.450 | 0.182 | 0.0% | 37.5% | 33.3% |
| SL | Ty France | 23 | 0.217 | 0.652 | 0.435 | 0.354 | 0.314 | 16.7% | 24.2% | 26.0% |
| CU | Miguel Andújar | 10 | 0.400 | 0.800 | 0.400 | 0.505 | 0.421 | 12.5% | 40.0% | 16.7% |
| CH | Ramón Laureano | 25 | 0.261 | 0.652 | 0.391 | 0.404 | 0.298 | 18.8% | 14.8% | 37.3% |
| SL | Nick Castellanos | 23 | 0.182 | 0.545 | 0.364 | 0.283 | 0.213 | 7.7% | 26.9% | 48.1% |
| CH | Ty France | 28 | 0.481 | 0.815 | 0.333 | 0.584 | 0.375 | 15.0% | 50.0% | 27.3% |
| FF | Ty France | 42 | 0.216 | 0.541 | 0.324 | 0.375 | 0.301 | 22.2% | 14.3% | 32.4% |
| SL | Jackson Merrill | 39 | 0.211 | 0.500 | 0.289 | 0.292 | 0.281 | 13.8% | 28.1% | 28.7% |
| FF | Gavin Sheets | 97 | 0.262 | 0.548 | 0.286 | 0.388 | 0.376 | 11.4% | 27.8% | 11.4% |
| SL | Gavin Sheets | 32 | 0.280 | 0.520 | 0.240 | 0.417 | 0.326 | 0.0% | 36.8% | 22.6% |
| FF | Manny Machado | 104 | 0.216 | 0.455 | 0.239 | 0.332 | 0.390 | 13.6% | 25.9% | 22.5% |
| SL | Ramón Laureano | 25 | 0.174 | 0.391 | 0.217 | 0.272 | 0.290 | 18.8% | 21.9% | 33.3% |
| CH | Gavin Sheets | 40 | 0.211 | 0.421 | 0.211 | 0.310 | 0.236 | 7.7% | 19.1% | 22.1% |
| FF | Xander Bogaerts | 90 | 0.250 | 0.447 | 0.197 | 0.362 | 0.354 | 12.3% | 29.1% | 12.8% |
| SL | Manny Machado | 39 | 0.135 | 0.324 | 0.189 | 0.240 | 0.224 | 10.3% | 18.9% | 28.4% |
| FF | Ramón Laureano | 61 | 0.224 | 0.408 | 0.184 | 0.352 | 0.437 | 20.0% | 25.8% | 25.0% |
| FF | Miguel Andújar | 56 | 0.196 | 0.373 | 0.176 | 0.280 | 0.311 | 4.8% | 18.2% | 8.7% |
| CH | Jackson Merrill | 43 | 0.225 | 0.400 | 0.175 | 0.305 | 0.311 | 9.4% | 27.1% | 27.5% |
| SL | Samad Taylor | 7 | 0.500 | 0.667 | 0.167 | 0.536 | 0.429 | 0.0% | 20.0% | 22.2% |
| CU | Ty France | 12 | 0.250 | 0.417 | 0.167 | 0.283 | 0.152 | 0.0% | 35.7% | 22.7% |
| FF | Freddy Fermin | 45 | 0.132 | 0.263 | 0.132 | 0.258 | 0.285 | 3.3% | 12.2% | 15.2% |
| FF | Jackson Merrill | 113 | 0.190 | 0.310 | 0.120 | 0.273 | 0.310 | 13.4% | 23.7% | 25.7% |
| SL | Jake Cronenworth | 10 | 0.111 | 0.222 | 0.111 | 0.195 | 0.108 | 0.0% | 36.4% | 36.8% |
| CH | Manny Machado | 42 | 0.135 | 0.243 | 0.108 | 0.251 | 0.211 | 3.6% | 16.7% | 25.4% |
| FF | Jake Cronenworth | 48 | 0.275 | 0.375 | 0.100 | 0.353 | 0.401 | 8.3% | 15.7% | 7.2% |
| CU | Jake Cronenworth | 11 | 0.100 | 0.200 | 0.100 | 0.177 | 0.300 | 33.3% | 50.0% | 50.0% |
| SL | Fernando Tatís | 52 | 0.295 | 0.386 | 0.091 | 0.361 | 0.340 | 13.8% | 33.3% | 36.0% |
| CU | Jackson Merrill | 25 | 0.318 | 0.409 | 0.091 | 0.364 | 0.353 | 0.0% | 26.7% | 23.8% |
| FF | Fernando Tatís | 96 | 0.286 | 0.369 | 0.083 | 0.348 | 0.384 | 13.1% | 34.5% | 20.0% |
| CU | Manny Machado | 16 | 0.071 | 0.143 | 0.071 | 0.166 | 0.227 | 0.0% | 11.1% | 25.9% |


## Home Starting Pitcher: Michael King

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1565 |
| Batted/Result Events | 401 |
| Hits Allowed | 81 |
| Walks | 37 |
| Strikeouts | 81 |
| Home Runs | 13 |
| K Event Rate | 20.2% |
| BB Event Rate | 9.2% |
| HR Event Rate | 3.2% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | SD | 9.0 | 6 | 0 | 0 | 5 | 0 |
| 2026-06-16 | STL | 7.3 | 5 | 0 | 4 | 1 | 0 |
| 2026-06-10 | SD | 10.0 | 7 | 2 | 3 | 3 | 2 |
| 2026-06-05 | SD | 7.7 | 6 | 2 | 0 | 4 | 2 |
| 2026-05-30 | WSH | 8.3 | 5 | 1 | 2 | 2 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 19.9% | 312 | 0.225 | 0.416 | 0.191 | 0.300 | 0.342 | 12.5% | 22.2% | 25.3% |
| CH | vs R | 6.0% | 94 | 0.229 | 0.286 | 0.057 | 0.263 | 0.259 | 4.3% | 37.1% | 30.5% |
| FF | vs L | 11.6% | 182 | 0.182 | 0.212 | 0.030 | 0.316 | 0.329 | 11.8% | 14.0% | 22.7% |
| FF | vs R | 7.5% | 117 | 0.208 | 0.333 | 0.125 | 0.298 | 0.314 | 7.1% | 14.3% | 28.6% |
| SI | vs L | 15.5% | 242 | 0.218 | 0.400 | 0.182 | 0.327 | 0.341 | 12.8% | 32.9% | 12.9% |
| SI | vs R | 14.3% | 224 | 0.286 | 0.524 | 0.238 | 0.397 | 0.468 | 11.4% | 29.9% | 12.4% |
| SL | vs L | 3.0% | 47 | 0.067 | 0.067 | 0.000 | 0.060 | 0.212 | 0.0% | 31.2% | 22.7% |
| SL | vs R | 2.4% | 38 | 0.200 | 0.200 | 0.000 | 0.267 | 0.218 | 0.0% | 0.0% | 20.0% |
| ST | vs L | 8.2% | 129 | 0.333 | 0.400 | 0.067 | 0.386 | 0.465 | 16.7% | 32.0% | 23.8% |
| ST | vs R | 11.5% | 180 | 0.262 | 0.452 | 0.190 | 0.316 | 0.247 | 5.6% | 22.0% | 23.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 93 | 6 | 0 | 5 | 0 |
| 2026-06-16 | 93 | 5 | 3 | 1 | 0 |
| 2026-06-10 | 106 | 7 | 3 | 3 | 2 |
| 2026-06-05 | 93 | 6 | 0 | 4 | 2 |
| 2026-05-30 | 77 | 5 | 1 | 2 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Dalton Rushing | 7 | 0.143 | 0.571 | 0.429 | 0.286 | 0.233 | 25.0% | 12.5% | 54.5% |
| SI | Shohei Ohtani | 50 | 0.488 | 0.902 | 0.415 | 0.596 | 0.555 | 18.9% | 44.2% | 16.4% |
| FF | Mookie Betts | 62 | 0.255 | 0.655 | 0.400 | 0.426 | 0.366 | 18.4% | 25.0% | 5.3% |
| ST | Kyle Tucker | 20 | 0.250 | 0.625 | 0.375 | 0.428 | 0.311 | 14.3% | 26.3% | 32.1% |
| FF | Max Muncy | 134 | 0.360 | 0.730 | 0.369 | 0.500 | 0.474 | 22.6% | 32.9% | 18.1% |
| FF | Freddie Freeman | 111 | 0.347 | 0.663 | 0.316 | 0.460 | 0.409 | 12.3% | 21.7% | 18.6% |
| CH | Teoscar Hernández | 26 | 0.318 | 0.591 | 0.273 | 0.435 | 0.426 | 13.3% | 22.6% | 30.8% |
| CH | Shohei Ohtani | 46 | 0.366 | 0.634 | 0.268 | 0.455 | 0.415 | 18.5% | 37.2% | 35.8% |
| ST | Andy Pages | 28 | 0.370 | 0.630 | 0.259 | 0.436 | 0.405 | 9.1% | 20.4% | 21.5% |
| SI | Dalton Rushing | 11 | 0.375 | 0.625 | 0.250 | 0.500 | 0.379 | 0.0% | 19.0% | 0.0% |
| ST | Mookie Betts | 12 | 0.333 | 0.583 | 0.250 | 0.392 | 0.382 | 10.0% | 36.8% | 18.5% |
| SI | Max Muncy | 65 | 0.309 | 0.545 | 0.236 | 0.415 | 0.377 | 13.3% | 26.5% | 12.5% |
| FF | Dalton Rushing | 63 | 0.269 | 0.500 | 0.231 | 0.406 | 0.333 | 12.5% | 26.1% | 31.0% |
| FF | Shohei Ohtani | 96 | 0.235 | 0.457 | 0.222 | 0.365 | 0.440 | 25.0% | 24.5% | 18.7% |
| CH | Will Smith | 16 | 0.286 | 0.500 | 0.214 | 0.381 | 0.394 | 10.0% | 22.2% | 15.2% |
| SI | Will Smith | 48 | 0.300 | 0.500 | 0.200 | 0.358 | 0.474 | 22.2% | 33.3% | 4.1% |
| FF | Teoscar Hernández | 54 | 0.283 | 0.478 | 0.196 | 0.368 | 0.367 | 14.3% | 23.8% | 17.1% |
| CH | Andy Pages | 28 | 0.269 | 0.462 | 0.192 | 0.339 | 0.359 | 9.1% | 21.6% | 23.5% |
| SI | Hyeseong Kim | 23 | 0.381 | 0.571 | 0.190 | 0.407 | 0.355 | 5.6% | 20.0% | 16.4% |
| FF | Will Smith | 66 | 0.226 | 0.415 | 0.189 | 0.357 | 0.458 | 20.0% | 27.8% | 14.5% |
| FF | Kyle Tucker | 109 | 0.245 | 0.426 | 0.181 | 0.359 | 0.360 | 11.0% | 22.9% | 18.2% |
| ST | Shohei Ohtani | 31 | 0.214 | 0.393 | 0.179 | 0.300 | 0.301 | 10.5% | 40.7% | 33.3% |
| SI | Freddie Freeman | 69 | 0.263 | 0.439 | 0.175 | 0.370 | 0.378 | 7.8% | 23.7% | 16.7% |
| FF | Alex Freeland | 63 | 0.302 | 0.472 | 0.170 | 0.383 | 0.367 | 6.8% | 29.2% | 16.7% |
| FF | Miguel Rojas | 47 | 0.302 | 0.465 | 0.163 | 0.347 | 0.364 | 10.5% | 37.1% | 11.0% |
| SI | Andy Pages | 78 | 0.304 | 0.464 | 0.159 | 0.365 | 0.389 | 6.6% | 35.3% | 9.0% |
| ST | Teoscar Hernández | 21 | 0.190 | 0.333 | 0.143 | 0.224 | 0.177 | 10.0% | 16.7% | 43.8% |
| SI | Kyle Tucker | 44 | 0.194 | 0.333 | 0.139 | 0.294 | 0.351 | 3.1% | 29.4% | 10.3% |
| CH | Dalton Rushing | 29 | 0.172 | 0.310 | 0.138 | 0.205 | 0.266 | 4.3% | 13.9% | 36.7% |
| FF | Andy Pages | 108 | 0.211 | 0.347 | 0.137 | 0.281 | 0.323 | 8.6% | 22.4% | 21.4% |


## Los Angeles Dodgers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Andy Pages | 374 | 0.266 | 0.462 | 0.195 | 0.346 | 0.342 | 8.1% | 26.1% | 20.3% |
| Freddie Freeman | 371 | 0.291 | 0.497 | 0.206 | 0.380 | 0.387 | 11.1% | 26.0% | 19.1% |
| Shohei Ohtani | 360 | 0.294 | 0.537 | 0.243 | 0.408 | 0.418 | 17.4% | 31.4% | 24.8% |
| Kyle Tucker | 345 | 0.238 | 0.389 | 0.151 | 0.331 | 0.326 | 6.1% | 24.2% | 22.0% |
| Max Muncy | 308 | 0.270 | 0.513 | 0.243 | 0.385 | 0.373 | 15.5% | 29.0% | 24.2% |
| Mookie Betts | 230 | 0.234 | 0.444 | 0.210 | 0.335 | 0.342 | 9.6% | 25.7% | 12.5% |
| Teoscar Hernández | 224 | 0.286 | 0.482 | 0.196 | 0.367 | 0.339 | 12.9% | 25.6% | 27.5% |
| Alex Freeland | 217 | 0.219 | 0.321 | 0.102 | 0.292 | 0.293 | 6.8% | 26.0% | 25.4% |
| Will Smith | 212 | 0.245 | 0.375 | 0.130 | 0.319 | 0.386 | 13.6% | 22.3% | 15.1% |
| Dalton Rushing | 184 | 0.239 | 0.478 | 0.239 | 0.361 | 0.337 | 11.0% | 26.9% | 31.1% |
| Miguel Rojas | 148 | 0.290 | 0.412 | 0.122 | 0.351 | 0.326 | 6.6% | 28.9% | 16.3% |
| Hyeseong Kim | 148 | 0.265 | 0.326 | 0.061 | 0.308 | 0.304 | 3.1% | 14.3% | 23.3% |


## San Diego Padres Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fernando Tatís | 358 | 0.282 | 0.367 | 0.085 | 0.331 | 0.360 | 10.9% | 36.3% | 26.0% |
| Jackson Merrill | 348 | 0.207 | 0.342 | 0.135 | 0.275 | 0.307 | 9.4% | 24.8% | 25.0% |
| Manny Machado | 342 | 0.177 | 0.365 | 0.187 | 0.286 | 0.311 | 9.3% | 24.6% | 23.6% |
| Xander Bogaerts | 321 | 0.228 | 0.342 | 0.114 | 0.321 | 0.318 | 6.7% | 26.4% | 20.4% |
| Gavin Sheets | 283 | 0.241 | 0.482 | 0.241 | 0.350 | 0.334 | 9.5% | 31.1% | 18.0% |
| Miguel Andújar | 227 | 0.238 | 0.388 | 0.150 | 0.292 | 0.289 | 3.9% | 21.8% | 17.7% |
| Ramón Laureano | 224 | 0.209 | 0.383 | 0.173 | 0.301 | 0.312 | 13.4% | 23.3% | 30.5% |
| Ty France | 200 | 0.250 | 0.505 | 0.255 | 0.351 | 0.319 | 12.6% | 26.0% | 26.1% |
| Freddy Fermin | 165 | 0.156 | 0.255 | 0.099 | 0.250 | 0.264 | 2.7% | 15.7% | 22.8% |
| Nick Castellanos | 137 | 0.178 | 0.333 | 0.155 | 0.246 | 0.285 | 7.5% | 20.4% | 30.8% |
| Jake Cronenworth | 132 | 0.162 | 0.216 | 0.054 | 0.257 | 0.304 | 4.7% | 21.2% | 21.2% |
| Samad Taylor | 78 | 0.333 | 0.394 | 0.061 | 0.385 | 0.338 | 2.1% | 16.7% | 19.1% |


## Bullpen Fatigue Report

### Los Angeles Dodgers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alex Vesia | 2026-06-24 | 1.0 | 21 |
| Alex Vesia | 2026-06-27 | 0.2 | 10 |
| Brock Stewart | 2026-06-26 | 1.0 | 12 |
| Edgardo Henriquez | 2026-06-26 | 1.0 | 13 |
| Jack Dreyer | 2026-06-26 | 1.0 | 7 |
| Jack Dreyer | 2026-06-27 | 1.0 | 27 |
| Jonathan Hernández | 2026-06-26 | 1.0 | 30 |
| Kyle Hurt | 2026-06-24 | 1.0 | 26 |
| Kyle Hurt | 2026-06-27 | 0.1 | 19 |
| Miguel Rojas | 2026-06-27 | 1.0 | 5 |
| Tanner Scott | 2026-06-24 | 1.0 | 15 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Alex Vesia, Jack Dreyer, Kyle Hurt, Miguel Rojas


### San Diego Padres Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Adrian Morejon | 2026-06-26 | 1.0 | 9 |
| David Morgan | 2026-06-24 | 1.1 | 16 |
| David Morgan | 2026-06-27 | 1.0 | 17 |
| Jason Adam | 2026-06-24 | 1.0 | 13 |
| Jason Adam | 2026-06-26 | 1.0 | 17 |
| Randy Vásquez | 2026-06-27 | 3.1 | 79 |
| Rodolfo Durán | 2026-06-27 | 1.0 | 14 |
| Ron Marinaccio | 2026-06-27 | 1.2 | 45 |
| Wandy Peralta | 2026-06-24 | 1.0 | 15 |
| Wandy Peralta | 2026-06-26 | 1.0 | 12 |
| Yuki Matsui | 2026-06-26 | 0.2 | 11 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** David Morgan, Randy Vásquez, Rodolfo Durán, Ron Marinaccio



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Andy Pages | 374 | 0.266 | 0.462 | 0.195 | 0.346 | 8.1% | 26.1% |
| 2 | Freddie Freeman | 371 | 0.291 | 0.497 | 0.206 | 0.380 | 11.1% | 26.0% |
| 3 | Shohei Ohtani | 360 | 0.294 | 0.537 | 0.243 | 0.408 | 17.4% | 31.4% |
| 4 | Kyle Tucker | 345 | 0.238 | 0.389 | 0.151 | 0.331 | 6.1% | 24.2% |
| 5 | Max Muncy | 308 | 0.270 | 0.513 | 0.243 | 0.385 | 15.5% | 29.0% |
| 6 | Mookie Betts | 230 | 0.234 | 0.444 | 0.210 | 0.335 | 9.6% | 25.7% |
| 7 | Teoscar Hernández | 224 | 0.286 | 0.482 | 0.196 | 0.367 | 12.9% | 25.6% |
| 8 | Alex Freeland | 217 | 0.219 | 0.321 | 0.102 | 0.292 | 6.8% | 26.0% |
| 9 | Will Smith | 212 | 0.245 | 0.375 | 0.130 | 0.319 | 13.6% | 22.3% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Fernando Tatís | 358 | 0.282 | 0.367 | 0.085 | 0.331 | 10.9% | 36.3% |
| 2 | Jackson Merrill | 348 | 0.207 | 0.342 | 0.135 | 0.275 | 9.4% | 24.8% |
| 3 | Manny Machado | 342 | 0.177 | 0.365 | 0.187 | 0.286 | 9.3% | 24.6% |
| 4 | Xander Bogaerts | 321 | 0.228 | 0.342 | 0.114 | 0.321 | 6.7% | 26.4% |
| 5 | Gavin Sheets | 283 | 0.241 | 0.482 | 0.241 | 0.350 | 9.5% | 31.1% |
| 6 | Miguel Andújar | 227 | 0.238 | 0.388 | 0.150 | 0.292 | 3.9% | 21.8% |
| 7 | Ramón Laureano | 224 | 0.209 | 0.383 | 0.173 | 0.301 | 13.4% | 23.3% |
| 8 | Ty France | 200 | 0.250 | 0.505 | 0.255 | 0.351 | 12.6% | 26.0% |
| 9 | Freddy Fermin | 165 | 0.156 | 0.255 | 0.099 | 0.250 | 2.7% | 15.7% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7012 |
| Hits Allowed | 1476 |
| Walks/HBP | 744 |
| Strikeouts | 1597 |
| Home Runs Allowed | 225 |
| K Event Rate | 22.8% |
| BB/HBP Event Rate | 10.6% |
| HR Event Rate | 3.2% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6702 |
| Hits Allowed | 1390 |
| Walks/HBP | 670 |
| Strikeouts | 1508 |
| Home Runs Allowed | 193 |
| K Event Rate | 22.5% |
| BB/HBP Event Rate | 10.0% |
| HR Event Rate | 2.9% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL, CH, CU
- Home pitcher pitch mix to inspect: SI, CH, ST, FF
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 15. New York Yankees @ Boston Red Sox

## Game Context

| Field | Value |
| --- | --- |
| Park | Fenway Park |
| Time | 2026-06-28T23:20:00Z |
| Away Team | New York Yankees |
| Home Team | Boston Red Sox |
| Away Probable Pitcher | Carlos Rodón |
| Home Probable Pitcher | Sonny Gray |


## Away Starting Pitcher: Carlos Rodón

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 732 |
| Batted/Result Events | 174 |
| Hits Allowed | 31 |
| Walks | 22 |
| Strikeouts | 46 |
| Home Runs | 3 |
| K Event Rate | 26.4% |
| BB Event Rate | 12.6% |
| HR Event Rate | 1.7% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | DET | 7.3 | 6 | 0 | 2 | 5 | 0 |
| 2026-06-17 | NYY | 7.3 | 7 | 1 | 1 | 7 | 1 |
| 2026-06-10 | CLE | 8.3 | 4 | 1 | 3 | 7 | 1 |
| 2026-06-04 | NYY | 7.7 | 2 | 0 | 3 | 7 | 0 |
| 2026-05-29 | ATH | 7.7 | 4 | 1 | 2 | 3 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.4% | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 100.0% |
| CH | vs R | 14.1% | 103 | 0.320 | 0.400 | 0.080 | 0.319 | 0.300 | 5.3% | 19.4% | 35.3% |
| CU | vs R | 1.4% | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.065 | 0.0% | 0.0% | 66.7% |
| FF | vs L | 10.4% | 76 | 0.167 | 0.500 | 0.333 | 0.378 | 0.512 | 22.2% | 16.7% | 18.2% |
| FF | vs R | 33.9% | 248 | 0.154 | 0.179 | 0.026 | 0.308 | 0.372 | 3.7% | 21.2% | 22.9% |
| SI | vs L | 8.5% | 62 | 0.167 | 0.167 | 0.000 | 0.154 | 0.175 | 0.0% | 15.8% | 23.5% |
| SI | vs R | 6.6% | 48 | 0.214 | 0.286 | 0.071 | 0.250 | 0.242 | 0.0% | 19.0% | 8.0% |
| SL | vs L | 8.6% | 63 | 0.400 | 0.733 | 0.333 | 0.465 | 0.292 | 8.3% | 23.8% | 16.1% |
| SL | vs R | 16.3% | 119 | 0.143 | 0.321 | 0.179 | 0.193 | 0.193 | 7.7% | 33.3% | 33.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 87 | 6 | 2 | 5 | 0 |
| 2026-06-17 | 99 | 7 | 1 | 7 | 1 |
| 2026-06-10 | 96 | 4 | 3 | 7 | 1 |
| 2026-06-04 | 96 | 2 | 3 | 7 | 0 |
| 2026-05-29 | 93 | 4 | 2 | 3 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SI | Willson Contreras | 87 | 0.389 | 0.792 | 0.403 | 0.524 | 0.498 | 12.3% | 34.4% | 10.1% |
| CH | Ceddanne Rafaela | 35 | 0.303 | 0.576 | 0.273 | 0.416 | 0.239 | 12.0% | 24.4% | 29.7% |
| FF | Jarren Duran | 100 | 0.186 | 0.442 | 0.256 | 0.315 | 0.326 | 14.8% | 18.8% | 32.7% |
| SI | Trevor Story | 33 | 0.345 | 0.586 | 0.241 | 0.441 | 0.427 | 8.0% | 30.4% | 12.7% |
| SL | Ceddanne Rafaela | 45 | 0.310 | 0.548 | 0.238 | 0.416 | 0.271 | 2.8% | 24.2% | 29.2% |
| CH | Willson Contreras | 43 | 0.310 | 0.548 | 0.238 | 0.372 | 0.309 | 20.0% | 32.6% | 40.9% |
| SL | Willson Contreras | 43 | 0.289 | 0.526 | 0.237 | 0.450 | 0.419 | 21.7% | 27.1% | 41.7% |
| SL | Roman Anthony | 20 | 0.294 | 0.529 | 0.235 | 0.403 | 0.419 | 15.4% | 35.0% | 25.0% |
| FF | Wilyer Abreu | 102 | 0.230 | 0.460 | 0.230 | 0.350 | 0.317 | 13.3% | 20.0% | 20.7% |
| FF | Caleb Durbin | 81 | 0.282 | 0.507 | 0.225 | 0.382 | 0.310 | 5.2% | 25.0% | 7.0% |
| CH | Masataka Yoshida | 27 | 0.304 | 0.522 | 0.217 | 0.404 | 0.408 | 5.3% | 29.0% | 20.0% |
| CH | Andruw Monasterio | 14 | 0.214 | 0.429 | 0.214 | 0.271 | 0.352 | 18.2% | 26.9% | 27.5% |
| FF | Andruw Monasterio | 45 | 0.225 | 0.425 | 0.200 | 0.321 | 0.297 | 7.7% | 13.9% | 18.2% |
| SL | Wilyer Abreu | 48 | 0.267 | 0.467 | 0.200 | 0.336 | 0.345 | 15.2% | 26.3% | 33.0% |
| SL | Masataka Yoshida | 11 | 0.300 | 0.500 | 0.200 | 0.373 | 0.317 | 0.0% | 31.2% | 21.7% |
| SI | Marcelo Mayer | 36 | 0.314 | 0.514 | 0.200 | 0.364 | 0.246 | 3.1% | 25.6% | 9.6% |
| SI | Jarren Duran | 40 | 0.378 | 0.568 | 0.189 | 0.430 | 0.467 | 16.1% | 33.3% | 18.9% |
| CH | Jarren Duran | 46 | 0.163 | 0.326 | 0.163 | 0.223 | 0.260 | 12.1% | 26.5% | 35.0% |
| SL | Isiah Kiner-Falefa | 23 | 0.476 | 0.619 | 0.143 | 0.500 | 0.454 | 5.6% | 20.7% | 23.4% |
| SI | Wilyer Abreu | 57 | 0.327 | 0.462 | 0.135 | 0.365 | 0.392 | 10.2% | 20.9% | 11.9% |
| SI | Andruw Monasterio | 24 | 0.292 | 0.417 | 0.125 | 0.344 | 0.327 | 5.0% | 29.3% | 6.4% |
| CH | Caleb Durbin | 27 | 0.125 | 0.250 | 0.125 | 0.191 | 0.264 | 5.3% | 22.2% | 36.7% |
| FF | Trevor Story | 47 | 0.250 | 0.364 | 0.114 | 0.293 | 0.244 | 3.8% | 19.0% | 25.6% |
| FF | Ceddanne Rafaela | 91 | 0.259 | 0.370 | 0.111 | 0.320 | 0.300 | 5.2% | 19.7% | 20.9% |
| SL | Marcelo Mayer | 34 | 0.222 | 0.333 | 0.111 | 0.315 | 0.267 | 5.0% | 48.3% | 30.2% |
| FF | Willson Contreras | 102 | 0.229 | 0.337 | 0.108 | 0.332 | 0.345 | 6.7% | 20.5% | 26.9% |
| FF | Isiah Kiner-Falefa | 47 | 0.179 | 0.282 | 0.103 | 0.273 | 0.275 | 0.0% | 10.8% | 8.2% |
| SL | Caleb Durbin | 43 | 0.225 | 0.325 | 0.100 | 0.255 | 0.252 | 3.0% | 13.5% | 27.5% |
| SL | Trevor Story | 33 | 0.267 | 0.367 | 0.100 | 0.314 | 0.179 | 0.0% | 19.4% | 29.1% |
| FF | Masataka Yoshida | 72 | 0.306 | 0.403 | 0.097 | 0.355 | 0.330 | 3.4% | 29.0% | 5.1% |


## Home Starting Pitcher: Sonny Gray

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1282 |
| Batted/Result Events | 353 |
| Hits Allowed | 79 |
| Walks | 24 |
| Strikeouts | 78 |
| Home Runs | 10 |
| K Event Rate | 22.1% |
| BB Event Rate | 6.8% |
| HR Event Rate | 2.8% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | COL | 10.0 | 6 | 1 | 3 | 11 | 1 |
| 2026-06-18 | BOS | 9.0 | 6 | 2 | 1 | 4 | 2 |
| 2026-06-12 | BOS | 7.7 | 5 | 0 | 0 | 7 | 0 |
| 2026-06-05 | NYY | 9.0 | 8 | 2 | 2 | 3 | 2 |
| 2026-05-30 | CLE | 8.0 | 4 | 0 | 3 | 7 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 5.0% | 64 | 0.200 | 0.300 | 0.100 | 0.215 | 0.237 | 0.0% | 11.8% | 13.6% |
| CH | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CS | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CU | vs L | 14.7% | 188 | 0.414 | 0.724 | 0.310 | 0.501 | 0.356 | 8.0% | 23.1% | 26.9% |
| CU | vs R | 2.2% | 28 | 0.200 | 0.800 | 0.600 | 0.750 | 0.660 | 25.0% | 40.0% | 22.2% |
| FC | vs L | 9.6% | 123 | 0.333 | 0.583 | 0.250 | 0.434 | 0.421 | 13.0% | 23.5% | 10.8% |
| FC | vs R | 10.6% | 136 | 0.282 | 0.385 | 0.103 | 0.311 | 0.301 | 2.6% | 16.4% | 16.7% |
| FF | vs L | 16.1% | 207 | 0.264 | 0.453 | 0.189 | 0.363 | 0.379 | 6.5% | 25.7% | 13.3% |
| FF | vs R | 3.6% | 46 | 0.500 | 0.500 | 0.000 | 0.518 | 0.281 | 0.0% | 13.3% | 5.9% |
| SI | vs L | 5.5% | 71 | 0.296 | 0.296 | 0.000 | 0.282 | 0.251 | 5.3% | 23.3% | 5.7% |
| SI | vs R | 13.5% | 173 | 0.205 | 0.386 | 0.182 | 0.270 | 0.276 | 10.3% | 25.5% | 14.1% |
| SL | vs R | 0.2% | 3 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 50.0% |
| ST | vs L | 8.9% | 114 | 0.071 | 0.167 | 0.095 | 0.099 | 0.193 | 12.5% | 42.4% | 38.8% |
| ST | vs R | 9.9% | 127 | 0.167 | 0.310 | 0.143 | 0.243 | 0.234 | 4.3% | 23.1% | 38.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 93 | 6 | 3 | 11 | 1 |
| 2026-06-18 | 89 | 6 | 1 | 4 | 2 |
| 2026-06-12 | 88 | 5 | 0 | 7 | 0 |
| 2026-06-05 | 79 | 8 | 2 | 3 | 2 |
| 2026-05-30 | 92 | 4 | 3 | 7 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF | Ben Rice | 80 | 0.358 | 1.000 | 0.642 | 0.593 | 0.556 | 31.4% | 39.2% | 17.0% |
| FF | Paul Goldschmidt | 67 | 0.386 | 0.965 | 0.579 | 0.568 | 0.434 | 22.9% | 27.3% | 17.0% |
| SI | Giancarlo Stanton | 12 | 0.417 | 0.917 | 0.500 | 0.558 | 0.482 | 27.3% | 37.5% | 20.0% |
| ST | Paul Goldschmidt | 10 | 0.250 | 0.625 | 0.375 | 0.430 | 0.242 | 0.0% | 15.0% | 23.1% |
| FC | Amed Rosario | 12 | 0.182 | 0.545 | 0.364 | 0.271 | 0.525 | 18.2% | 50.0% | 14.3% |
| CU | Aaron Judge | 19 | 0.176 | 0.529 | 0.353 | 0.332 | 0.350 | 42.9% | 46.2% | 48.5% |
| FF | Aaron Judge | 54 | 0.233 | 0.558 | 0.326 | 0.404 | 0.467 | 26.9% | 24.7% | 22.9% |
| SI | Aaron Judge | 47 | 0.389 | 0.694 | 0.306 | 0.547 | 0.542 | 17.9% | 30.8% | 10.8% |
| CU | Ben Rice | 40 | 0.176 | 0.471 | 0.294 | 0.331 | 0.296 | 5.3% | 15.8% | 31.3% |
| CU | Ryan Mcmahon | 23 | 0.182 | 0.455 | 0.273 | 0.252 | 0.289 | 13.3% | 42.9% | 35.0% |
| CU | Amed Rosario | 16 | 0.312 | 0.562 | 0.250 | 0.372 | 0.238 | 11.1% | 46.7% | 40.7% |
| CU | Cody Bellinger | 25 | 0.160 | 0.400 | 0.240 | 0.230 | 0.318 | 17.6% | 24.0% | 39.1% |
| SI | Jazz Chisholm | 43 | 0.395 | 0.632 | 0.237 | 0.471 | 0.412 | 6.2% | 27.8% | 17.6% |
| ST | Aaron Judge | 27 | 0.217 | 0.435 | 0.217 | 0.337 | 0.420 | 11.1% | 45.8% | 25.7% |
| SI | Ryan Mcmahon | 33 | 0.179 | 0.393 | 0.214 | 0.336 | 0.377 | 13.6% | 35.1% | 23.5% |
| CU | Paul Goldschmidt | 20 | 0.263 | 0.474 | 0.211 | 0.333 | 0.327 | 6.7% | 27.3% | 20.7% |
| FC | Aaron Judge | 22 | 0.350 | 0.550 | 0.200 | 0.416 | 0.290 | 8.3% | 22.2% | 36.0% |
| FF | Anthony Volpe | 40 | 0.267 | 0.467 | 0.200 | 0.409 | 0.398 | 15.0% | 23.5% | 24.3% |
| ST | Trent Grisham | 19 | 0.250 | 0.438 | 0.188 | 0.368 | 0.369 | 10.0% | 38.9% | 25.0% |
| FF | Austin Wells | 65 | 0.204 | 0.389 | 0.185 | 0.316 | 0.322 | 7.0% | 26.3% | 17.7% |
| FF | Ryan Mcmahon | 66 | 0.295 | 0.475 | 0.180 | 0.351 | 0.374 | 14.0% | 19.3% | 18.1% |
| CU | José Caballero | 20 | 0.294 | 0.471 | 0.176 | 0.350 | 0.234 | 7.1% | 5.9% | 18.2% |
| FF | Trent Grisham | 107 | 0.239 | 0.409 | 0.170 | 0.351 | 0.417 | 16.2% | 35.8% | 10.8% |
| FC | Ryan Mcmahon | 20 | 0.278 | 0.444 | 0.167 | 0.350 | 0.341 | 7.7% | 25.0% | 32.5% |
| ST | Jazz Chisholm | 27 | 0.333 | 0.500 | 0.167 | 0.396 | 0.299 | 16.7% | 31.0% | 26.2% |
| SI | Ben Rice | 56 | 0.269 | 0.423 | 0.154 | 0.327 | 0.322 | 7.1% | 35.1% | 11.4% |
| ST | Ben Rice | 29 | 0.154 | 0.308 | 0.154 | 0.222 | 0.296 | 13.3% | 25.0% | 21.2% |
| SI | Austin Wells | 37 | 0.212 | 0.364 | 0.152 | 0.281 | 0.317 | 7.7% | 34.1% | 13.0% |
| FC | Paul Goldschmidt | 23 | 0.200 | 0.350 | 0.150 | 0.296 | 0.295 | 7.7% | 20.8% | 45.8% |
| FC | Anthony Volpe | 7 | 0.286 | 0.429 | 0.143 | 0.307 | 0.145 | 0.0% | 9.1% | 14.3% |


## New York Yankees Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cody Bellinger | 364 | 0.256 | 0.435 | 0.179 | 0.351 | 0.372 | 7.3% | 24.7% | 17.8% |
| Ben Rice | 351 | 0.268 | 0.559 | 0.291 | 0.396 | 0.376 | 13.9% | 31.2% | 23.2% |
| Jazz Chisholm | 335 | 0.223 | 0.395 | 0.172 | 0.314 | 0.298 | 8.5% | 27.8% | 30.0% |
| Trent Grisham | 281 | 0.232 | 0.397 | 0.165 | 0.337 | 0.360 | 11.4% | 32.6% | 15.1% |
| Aaron Judge | 270 | 0.250 | 0.536 | 0.286 | 0.399 | 0.415 | 21.9% | 31.3% | 30.8% |
| José Caballero | 270 | 0.245 | 0.384 | 0.139 | 0.312 | 0.284 | 4.3% | 16.7% | 24.2% |
| Paul Goldschmidt | 238 | 0.284 | 0.535 | 0.251 | 0.378 | 0.339 | 12.0% | 24.8% | 22.5% |
| Ryan Mcmahon | 220 | 0.217 | 0.365 | 0.148 | 0.282 | 0.304 | 12.6% | 26.7% | 28.2% |
| Austin Wells | 197 | 0.158 | 0.246 | 0.088 | 0.234 | 0.288 | 6.8% | 29.1% | 28.0% |
| Amed Rosario | 156 | 0.257 | 0.451 | 0.194 | 0.325 | 0.320 | 9.6% | 28.0% | 22.7% |
| Anthony Volpe | 127 | 0.255 | 0.355 | 0.100 | 0.330 | 0.311 | 5.0% | 20.9% | 23.9% |
| Giancarlo Stanton | 111 | 0.260 | 0.433 | 0.173 | 0.323 | 0.326 | 23.9% | 30.8% | 34.1% |


## Boston Red Sox Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wilyer Abreu | 356 | 0.263 | 0.434 | 0.172 | 0.333 | 0.339 | 12.0% | 23.7% | 20.6% |
| Jarren Duran | 352 | 0.199 | 0.352 | 0.153 | 0.274 | 0.288 | 11.2% | 25.8% | 32.6% |
| Willson Contreras | 345 | 0.277 | 0.514 | 0.236 | 0.390 | 0.377 | 13.4% | 29.4% | 29.3% |
| Ceddanne Rafaela | 329 | 0.293 | 0.457 | 0.164 | 0.360 | 0.290 | 5.5% | 21.8% | 23.1% |
| Caleb Durbin | 285 | 0.238 | 0.383 | 0.146 | 0.303 | 0.280 | 2.7% | 21.1% | 14.8% |
| Marcelo Mayer | 248 | 0.215 | 0.305 | 0.090 | 0.279 | 0.259 | 6.8% | 27.0% | 24.0% |
| Masataka Yoshida | 195 | 0.243 | 0.347 | 0.104 | 0.307 | 0.309 | 2.0% | 27.7% | 15.4% |
| Trevor Story | 194 | 0.225 | 0.335 | 0.110 | 0.286 | 0.248 | 4.0% | 22.1% | 27.8% |
| Carlos Narváez | 168 | 0.193 | 0.273 | 0.080 | 0.266 | 0.284 | 8.1% | 20.3% | 29.1% |
| Isiah Kiner-Falefa | 151 | 0.255 | 0.328 | 0.073 | 0.300 | 0.312 | 3.4% | 17.1% | 14.8% |
| Andruw Monasterio | 147 | 0.223 | 0.360 | 0.137 | 0.280 | 0.278 | 6.8% | 18.2% | 17.3% |
| Roman Anthony | 145 | 0.240 | 0.322 | 0.083 | 0.318 | 0.352 | 9.6% | 31.2% | 26.6% |


## Bullpen Fatigue Report

### New York Yankees Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brent Headrick | 2026-06-27 | 1.0 | 17 |
| Camilo Doval | 2026-06-24 | 0.2 | 15 |
| Camilo Doval | 2026-06-27 | 0.2 | 9 |
| David Bednar | 2026-06-24 | 1.0 | 12 |
| Fernando Cruz | 2026-06-24 | 1.1 | 22 |
| Paul Blackburn | 2026-06-25 | 1.0 | 17 |
| Paul Blackburn | 2026-06-27 | 1.0 | 4 |
| Ryan Yarbrough | 2026-06-25 | 0.2 | 9 |
| Ryan Yarbrough | 2026-06-26 | 1.1 | 22 |
| Tim Hill | 2026-06-25 | 1.0 | 8 |
| Yerry De los Santos | 2026-06-25 | 0.1 | 11 |
| Yerry De los Santos | 2026-06-26 | 1.0 | 16 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Brent Headrick, Camilo Doval, Paul Blackburn


### Boston Red Sox Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Aroldis Chapman | 2026-06-25 | 1.0 | 23 |
| Aroldis Chapman | 2026-06-27 | 1.0 | 20 |
| Danny Coulombe | 2026-06-24 | 0.1 | 5 |
| Danny Coulombe | 2026-06-25 | 0.1 | 3 |
| Garrett Whitlock | 2026-06-25 | 1.0 | 10 |
| Garrett Whitlock | 2026-06-27 | 1.0 | 7 |
| Greg Weissert | 2026-06-25 | 0.2 | 21 |
| Justin Slaten | 2026-06-24 | 1.0 | 19 |
| Justin Slaten | 2026-06-27 | 0.2 | 12 |
| Ryan Watson | 2026-06-26 | 1.0 | 13 |
| Tommy Kahnle | 2026-06-26 | 1.0 | 21 |
| Tyron Guerrero | 2026-06-24 | 0.2 | 25 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Aroldis Chapman, Garrett Whitlock, Justin Slaten



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cody Bellinger | 364 | 0.256 | 0.435 | 0.179 | 0.351 | 7.3% | 24.7% |
| 2 | Ben Rice | 351 | 0.268 | 0.559 | 0.291 | 0.396 | 13.9% | 31.2% |
| 3 | Jazz Chisholm | 335 | 0.223 | 0.395 | 0.172 | 0.314 | 8.5% | 27.8% |
| 4 | Trent Grisham | 281 | 0.232 | 0.397 | 0.165 | 0.337 | 11.4% | 32.6% |
| 5 | Aaron Judge | 270 | 0.250 | 0.536 | 0.286 | 0.399 | 21.9% | 31.3% |
| 6 | José Caballero | 270 | 0.245 | 0.384 | 0.139 | 0.312 | 4.3% | 16.7% |
| 7 | Paul Goldschmidt | 238 | 0.284 | 0.535 | 0.251 | 0.378 | 12.0% | 24.8% |
| 8 | Ryan Mcmahon | 220 | 0.217 | 0.365 | 0.148 | 0.282 | 12.6% | 26.7% |
| 9 | Austin Wells | 197 | 0.158 | 0.246 | 0.088 | 0.234 | 6.8% | 29.1% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Wilyer Abreu | 356 | 0.263 | 0.434 | 0.172 | 0.333 | 12.0% | 23.7% |
| 2 | Jarren Duran | 352 | 0.199 | 0.352 | 0.153 | 0.274 | 11.2% | 25.8% |
| 3 | Willson Contreras | 345 | 0.277 | 0.514 | 0.236 | 0.390 | 13.4% | 29.4% |
| 4 | Ceddanne Rafaela | 329 | 0.293 | 0.457 | 0.164 | 0.360 | 5.5% | 21.8% |
| 5 | Caleb Durbin | 285 | 0.238 | 0.383 | 0.146 | 0.303 | 2.7% | 21.1% |
| 6 | Marcelo Mayer | 248 | 0.215 | 0.305 | 0.090 | 0.279 | 6.8% | 27.0% |
| 7 | Masataka Yoshida | 195 | 0.243 | 0.347 | 0.104 | 0.307 | 2.0% | 27.7% |
| 8 | Trevor Story | 194 | 0.225 | 0.335 | 0.110 | 0.286 | 4.0% | 22.1% |
| 9 | Carlos Narváez | 168 | 0.193 | 0.273 | 0.080 | 0.266 | 8.1% | 20.3% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6867 |
| Hits Allowed | 1441 |
| Walks/HBP | 685 |
| Strikeouts | 1608 |
| Home Runs Allowed | 219 |
| K Event Rate | 23.4% |
| BB/HBP Event Rate | 10.0% |
| HR Event Rate | 3.2% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6727 |
| Hits Allowed | 1468 |
| Walks/HBP | 619 |
| Strikeouts | 1494 |
| Home Runs Allowed | 171 |
| K Event Rate | 22.2% |
| BB/HBP Event Rate | 9.2% |
| HR Event Rate | 2.5% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL, SI, CH
- Home pitcher pitch mix to inspect: FC, FF, SI, ST, CU
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.

