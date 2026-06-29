# MLB-LAB V5.1 Pitch Matchup Engine

Date: 2026-06-29

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
| 1 | Chicago White Sox @ Baltimore Orioles | Oriole Park at Camden Yards | Sean Burke | Shane Baz |
| 2 | Pittsburgh Pirates @ Philadelphia Phillies | Citizens Bank Park | Braxton Ashcraft | Aaron Nola |
| 3 | Detroit Tigers @ New York Yankees | Yankee Stadium | Casey Mize | Ryan Weathers |
| 4 | New York Mets @ Toronto Blue Jays | Rogers Centre | Sean Manaea | Trey Yesavage |
| 5 | Washington Nationals @ Boston Red Sox | Fenway Park | Miles Mikolas | Ranger Suarez |
| 6 | Texas Rangers @ Cleveland Guardians | Progressive Field | Tyler Alexander | Parker Messick |
| 7 | Cincinnati Reds @ Milwaukee Brewers | American Family Field | Nick Lodolo | Robert Gasser |
| 8 | San Diego Padres @ Chicago Cubs | Wrigley Field | TBD | Shota Imanaga |
| 9 | Minnesota Twins @ Houston Astros | Daikin Park | Zebby Matthews | Peter Lambert |
| 10 | Miami Marlins @ Colorado Rockies | Coors Field | Sandy Alcantara | TBD |
| 11 | Los Angeles Dodgers @ Athletics | Sutter Health Park | Eric Lauer | Gage Jump |
| 12 | Los Angeles Angels @ Seattle Mariners | T-Mobile Park | Ryan Johnson | George Kirby |
| 13 | San Francisco Giants @ Arizona Diamondbacks | Chase Field | Tyler Mahle | Eduardo Rodriguez |

---

# Full Game Breakdown Cards

---

# 1. Chicago White Sox @ Baltimore Orioles

## Game Context

| Field | Value |
| --- | --- |
| Park | Oriole Park at Camden Yards |
| Time | 2026-06-29T22:35:00Z |
| Away Team | Chicago White Sox |
| Home Team | Baltimore Orioles |
| Away Probable Pitcher | Sean Burke |
| Home Probable Pitcher | Shane Baz |


## Away Starting Pitcher: Sean Burke

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1579 |
| Batted/Result Events | 407 |
| Hits Allowed | 82 |
| Walks | 34 |
| Strikeouts | 97 |
| Home Runs | 12 |
| K Event Rate | 23.8% |
| BB Event Rate | 8.4% |
| HR Event Rate | 2.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | CWS | 9.0 | 6 | 1 | 2 | 6 | 1 |
| 2026-06-18 | NYY | 8.7 | 5 | 1 | 1 | 8 | 1 |
| 2026-06-13 | CWS | 7.3 | 6 | 2 | 5 | 6 | 2 |
| 2026-06-06 | PHI | 7.0 | 3 | 2 | 5 | 7 | 2 |
| 2026-05-31 | CWS | 7.0 | 3 | 0 | 2 | 6 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 3.4% | 54 | 0.250 | 0.375 | 0.125 | 0.269 | 0.467 | 0.0% | 20.0% | 23.8% |
| CH | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CS | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 100.0% |
| FC | vs L | 4.9% | 77 | 0.294 | 0.294 | 0.000 | 0.265 | 0.289 | 0.0% | 28.6% | 23.8% |
| FC | vs R | 0.9% | 14 | 0.500 | 2.000 | 1.500 | 1.000 | 0.629 | 50.0% | 40.0% | 14.3% |
| FF | vs L | 24.6% | 388 | 0.211 | 0.474 | 0.263 | 0.329 | 0.347 | 13.0% | 20.8% | 16.8% |
| FF | vs R | 12.7% | 200 | 0.153 | 0.237 | 0.085 | 0.235 | 0.235 | 11.4% | 17.9% | 25.9% |
| KC | vs L | 16.0% | 253 | 0.185 | 0.278 | 0.093 | 0.261 | 0.245 | 5.9% | 31.0% | 25.2% |
| KC | vs R | 4.8% | 76 | 0.500 | 1.200 | 0.700 | 0.700 | 0.469 | 12.5% | 41.2% | 12.5% |
| SI | vs L | 7.0% | 110 | 0.250 | 0.583 | 0.333 | 0.396 | 0.411 | 11.1% | 28.2% | 10.0% |
| SI | vs R | 7.8% | 123 | 0.242 | 0.303 | 0.061 | 0.289 | 0.319 | 0.0% | 20.8% | 6.6% |
| SL | vs L | 4.7% | 74 | 0.158 | 0.158 | 0.000 | 0.239 | 0.262 | 0.0% | 25.0% | 28.2% |
| SL | vs R | 13.1% | 207 | 0.310 | 0.500 | 0.190 | 0.355 | 0.300 | 6.2% | 23.1% | 32.5% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 90 | 6 | 1 | 6 | 1 |
| 2026-06-18 | 89 | 5 | 1 | 8 | 1 |
| 2026-06-13 | 92 | 6 | 5 | 6 | 2 |
| 2026-06-06 | 90 | 3 | 5 | 7 | 2 |
| 2026-05-31 | 93 | 3 | 2 | 6 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KC | Samuel Basallo | 5 | 0.200 | 0.800 | 0.600 | 0.400 | 0.349 | 100.0% | 40.0% | 53.8% |
| SI | Colton Cowser | 24 | 0.389 | 0.889 | 0.500 | 0.575 | 0.516 | 25.0% | 25.0% | 20.6% |
| SL | Colton Cowser | 34 | 0.273 | 0.667 | 0.394 | 0.399 | 0.358 | 25.0% | 33.3% | 57.4% |
| FF | Pete Alonso | 102 | 0.272 | 0.609 | 0.337 | 0.393 | 0.433 | 25.4% | 37.0% | 23.3% |
| SI | Coby Mayo | 40 | 0.250 | 0.583 | 0.333 | 0.381 | 0.417 | 12.1% | 38.5% | 12.7% |
| FF | Jeremiah Jackson | 44 | 0.238 | 0.524 | 0.286 | 0.336 | 0.299 | 9.1% | 22.6% | 16.2% |
| SL | Coby Mayo | 48 | 0.208 | 0.479 | 0.271 | 0.305 | 0.245 | 16.7% | 52.2% | 48.9% |
| FF | Samuel Basallo | 85 | 0.269 | 0.500 | 0.231 | 0.356 | 0.345 | 15.1% | 33.3% | 25.2% |
| FF | Adley Rutschman | 88 | 0.257 | 0.486 | 0.230 | 0.359 | 0.320 | 7.8% | 26.6% | 4.3% |
| SL | Adley Rutschman | 24 | 0.227 | 0.455 | 0.227 | 0.321 | 0.331 | 5.3% | 22.6% | 15.0% |
| SI | Leody Taveras | 34 | 0.407 | 0.630 | 0.222 | 0.510 | 0.463 | 4.2% | 25.6% | 18.0% |
| SI | Tyler O'Neill | 40 | 0.281 | 0.500 | 0.219 | 0.427 | 0.397 | 14.3% | 30.0% | 9.4% |
| SL | Jeremiah Jackson | 52 | 0.224 | 0.429 | 0.204 | 0.274 | 0.305 | 10.3% | 32.1% | 35.5% |
| FF | Taylor Ward | 118 | 0.309 | 0.500 | 0.191 | 0.426 | 0.425 | 10.6% | 23.0% | 19.0% |
| SI | Pete Alonso | 93 | 0.299 | 0.481 | 0.182 | 0.383 | 0.418 | 9.1% | 37.1% | 15.6% |
| SI | Gunnar Henderson | 73 | 0.288 | 0.470 | 0.182 | 0.386 | 0.362 | 7.1% | 26.4% | 12.2% |
| FF | Dylan Beavers | 44 | 0.231 | 0.410 | 0.179 | 0.326 | 0.376 | 13.3% | 18.6% | 11.8% |
| SL | Gunnar Henderson | 64 | 0.186 | 0.356 | 0.169 | 0.294 | 0.229 | 7.3% | 31.1% | 29.3% |
| SI | Jeremiah Jackson | 36 | 0.389 | 0.556 | 0.167 | 0.460 | 0.257 | 5.9% | 23.6% | 3.2% |
| SI | Adley Rutschman | 32 | 0.233 | 0.400 | 0.167 | 0.325 | 0.401 | 15.4% | 26.5% | 10.3% |
| SL | Pete Alonso | 48 | 0.270 | 0.432 | 0.162 | 0.378 | 0.392 | 12.0% | 19.6% | 37.8% |
| FF | Blaze Alexander | 60 | 0.250 | 0.404 | 0.154 | 0.327 | 0.349 | 13.9% | 20.0% | 27.3% |
| SI | Dylan Beavers | 17 | 0.308 | 0.462 | 0.154 | 0.418 | 0.445 | 0.0% | 32.0% | 7.1% |
| FF | Colton Cowser | 70 | 0.222 | 0.370 | 0.148 | 0.356 | 0.420 | 15.9% | 29.0% | 15.1% |
| SL | Samuel Basallo | 40 | 0.257 | 0.400 | 0.143 | 0.318 | 0.321 | 3.6% | 26.1% | 34.2% |
| SI | Samuel Basallo | 26 | 0.143 | 0.286 | 0.143 | 0.315 | 0.383 | 5.9% | 12.2% | 10.2% |
| SL | Leody Taveras | 36 | 0.194 | 0.323 | 0.129 | 0.272 | 0.291 | 5.3% | 30.2% | 26.2% |
| FF | Gunnar Henderson | 91 | 0.128 | 0.256 | 0.128 | 0.248 | 0.289 | 9.1% | 19.1% | 16.2% |
| FF | Coby Mayo | 62 | 0.196 | 0.314 | 0.118 | 0.304 | 0.344 | 6.1% | 24.7% | 13.7% |
| SL | Blaze Alexander | 30 | 0.296 | 0.407 | 0.111 | 0.368 | 0.367 | 11.1% | 25.0% | 35.7% |


## Home Starting Pitcher: Shane Baz

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1616 |
| Batted/Result Events | 425 |
| Hits Allowed | 98 |
| Walks | 35 |
| Strikeouts | 86 |
| Home Runs | 9 |
| K Event Rate | 20.2% |
| BB Event Rate | 8.2% |
| HR Event Rate | 2.1% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | LAA | 8.0 | 8 | 1 | 1 | 5 | 1 |
| 2026-06-18 | SEA | 9.3 | 5 | 0 | 2 | 9 | 0 |
| 2026-06-12 | BAL | 8.0 | 6 | 0 | 3 | 1 | 0 |
| 2026-06-07 | TOR | 8.7 | 7 | 1 | 1 | 3 | 1 |
| 2026-06-02 | BOS | 8.7 | 4 | 0 | 2 | 6 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 7.7% | 125 | 0.273 | 0.455 | 0.182 | 0.298 | 0.482 | 13.6% | 20.0% | 13.2% |
| CH | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| FA | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | 0.700 | 0.700 | 0.0% | 0.0% | 0.0% |
| FC | vs L | 5.1% | 82 | 0.438 | 0.688 | 0.250 | 0.543 | 0.392 | 0.0% | 22.6% | 20.0% |
| FC | vs R | 12.7% | 206 | 0.219 | 0.375 | 0.156 | 0.281 | 0.327 | 5.3% | 24.2% | 20.2% |
| FF | vs L | 23.6% | 381 | 0.296 | 0.493 | 0.197 | 0.381 | 0.390 | 10.5% | 14.7% | 12.4% |
| FF | vs R | 9.9% | 160 | 0.167 | 0.333 | 0.167 | 0.233 | 0.291 | 9.1% | 18.2% | 13.4% |
| KC | vs L | 21.5% | 347 | 0.248 | 0.390 | 0.143 | 0.285 | 0.264 | 8.0% | 35.6% | 27.5% |
| KC | vs R | 11.4% | 185 | 0.306 | 0.408 | 0.102 | 0.345 | 0.308 | 11.8% | 29.1% | 27.6% |
| SI | vs L | 0.9% | 15 | 0.000 | 0.000 | 0.000 | 0.280 | 0.495 | 0.0% | 33.3% | 0.0% |
| SI | vs R | 6.5% | 105 | 0.222 | 0.278 | 0.056 | 0.292 | 0.303 | 0.0% | 27.5% | 7.8% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 91 | 8 | 1 | 5 | 1 |
| 2026-06-18 | 99 | 5 | 2 | 9 | 0 |
| 2026-06-12 | 103 | 6 | 2 | 1 | 0 |
| 2026-06-07 | 81 | 7 | 1 | 3 | 1 |
| 2026-06-02 | 94 | 4 | 2 | 6 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KC | Munetaka Murakami | 4 | 0.500 | 1.250 | 0.750 | 0.725 | 0.613 | 50.0% | 50.0% | 42.9% |
| FC | Colson Montgomery | 24 | 0.375 | 1.042 | 0.667 | 0.581 | 0.564 | 33.3% | 39.3% | 32.6% |
| FC | Munetaka Murakami | 14 | 0.308 | 0.769 | 0.462 | 0.529 | 0.429 | 10.0% | 33.3% | 29.0% |
| FF | Munetaka Murakami | 90 | 0.257 | 0.714 | 0.457 | 0.476 | 0.462 | 23.9% | 39.3% | 34.9% |
| FC | Miguel Vargas | 28 | 0.318 | 0.773 | 0.455 | 0.505 | 0.393 | 10.5% | 18.9% | 24.5% |
| KC | Colson Montgomery | 7 | 0.429 | 0.857 | 0.429 | 0.543 | 0.433 | 20.0% | 44.4% | 30.8% |
| FF | Drew Romo | 29 | 0.125 | 0.500 | 0.375 | 0.328 | 0.328 | 20.0% | 22.5% | 18.9% |
| FF | Andrew Benintendi | 74 | 0.277 | 0.585 | 0.308 | 0.399 | 0.346 | 16.0% | 36.5% | 23.6% |
| FC | Drew Romo | 10 | 0.200 | 0.500 | 0.300 | 0.290 | 0.232 | 0.0% | 13.3% | 11.8% |
| FF | Derek Hill | 41 | 0.222 | 0.500 | 0.278 | 0.350 | 0.308 | 20.0% | 28.2% | 38.2% |
| FF | Miguel Vargas | 111 | 0.230 | 0.494 | 0.264 | 0.403 | 0.409 | 17.5% | 24.1% | 22.1% |
| FC | Tristan Peters | 23 | 0.286 | 0.524 | 0.238 | 0.372 | 0.301 | 12.5% | 26.3% | 14.6% |
| FF | Chase Meidroth | 102 | 0.294 | 0.529 | 0.235 | 0.408 | 0.347 | 9.1% | 25.0% | 14.4% |
| KC | Sam Antonacci | 6 | 0.600 | 0.800 | 0.200 | 0.625 | 0.476 | 0.0% | 33.3% | 0.0% |
| FF | Sam Antonacci | 84 | 0.358 | 0.537 | 0.179 | 0.463 | 0.449 | 12.1% | 23.4% | 14.1% |
| FF | Tristan Peters | 84 | 0.274 | 0.438 | 0.164 | 0.339 | 0.324 | 5.1% | 20.4% | 17.9% |
| FF | Colson Montgomery | 134 | 0.182 | 0.339 | 0.157 | 0.274 | 0.268 | 9.6% | 25.3% | 31.1% |
| FC | Sam Antonacci | 28 | 0.304 | 0.435 | 0.130 | 0.402 | 0.306 | 4.5% | 21.2% | 17.1% |
| FC | Luisangel Acuña | 13 | 0.250 | 0.333 | 0.083 | 0.250 | 0.292 | 9.1% | 26.7% | 19.0% |
| FC | Derek Hill | 15 | 0.077 | 0.154 | 0.077 | 0.143 | 0.149 | 16.7% | 35.7% | 37.0% |
| FF | Edgar Quero | 75 | 0.136 | 0.197 | 0.061 | 0.189 | 0.258 | 4.3% | 20.2% | 28.2% |
| FC | Andrew Benintendi | 20 | 0.118 | 0.176 | 0.059 | 0.212 | 0.282 | 18.2% | 16.1% | 30.6% |
| FC | Chase Meidroth | 21 | 0.263 | 0.316 | 0.053 | 0.264 | 0.307 | 0.0% | 18.2% | 17.5% |
| FF | Luisangel Acuña | 40 | 0.242 | 0.273 | 0.030 | 0.294 | 0.355 | 7.1% | 25.9% | 13.9% |
| FF | Everson Pereira | 17 | 0.308 | 0.308 | 0.000 | 0.376 | 0.349 | 0.0% | 6.9% | 20.5% |
| KC | Drew Romo | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.003 | 0.0% | 0.0% | 42.9% |
| KC | Andrew Benintendi | 9 | 0.250 | 0.250 | 0.000 | 0.278 | 0.345 | 0.0% | 16.7% | 25.0% |
| KC | Tristan Peters | 4 | 0.333 | 0.333 | 0.000 | 0.400 | 0.394 | 0.0% | 11.1% | 25.0% |
| KC | Miguel Vargas | 6 | 0.000 | 0.000 | 0.000 | 0.117 | 0.268 | 0.0% | 14.3% | 20.0% |
| KC | Chase Meidroth | 8 | 0.143 | 0.143 | 0.000 | 0.138 | 0.149 | 0.0% | 0.0% | 33.3% |


## Chicago White Sox Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Miguel Vargas | 373 | 0.245 | 0.487 | 0.242 | 0.375 | 0.405 | 14.0% | 27.9% | 17.1% |
| Chase Meidroth | 362 | 0.282 | 0.402 | 0.121 | 0.338 | 0.282 | 4.7% | 22.3% | 18.3% |
| Colson Montgomery | 352 | 0.212 | 0.450 | 0.238 | 0.329 | 0.327 | 13.4% | 29.8% | 34.7% |
| Andrew Benintendi | 273 | 0.237 | 0.438 | 0.201 | 0.319 | 0.327 | 11.7% | 28.8% | 27.0% |
| Sam Antonacci | 269 | 0.294 | 0.412 | 0.118 | 0.377 | 0.373 | 7.0% | 22.9% | 13.5% |
| Munetaka Murakami | 264 | 0.236 | 0.546 | 0.310 | 0.394 | 0.379 | 20.5% | 37.1% | 38.9% |
| Tristan Peters | 248 | 0.285 | 0.448 | 0.163 | 0.353 | 0.301 | 5.0% | 21.2% | 19.1% |
| Edgar Quero | 191 | 0.181 | 0.223 | 0.042 | 0.237 | 0.260 | 2.3% | 21.6% | 21.4% |
| Luisangel Acuña | 166 | 0.229 | 0.268 | 0.039 | 0.243 | 0.273 | 4.7% | 26.5% | 21.3% |
| Drew Romo | 113 | 0.140 | 0.340 | 0.200 | 0.254 | 0.261 | 9.7% | 22.3% | 29.7% |
| Derek Hill | 106 | 0.215 | 0.355 | 0.140 | 0.291 | 0.302 | 8.3% | 20.2% | 33.5% |
| Everson Pereira | 92 | 0.244 | 0.451 | 0.207 | 0.331 | 0.302 | 12.3% | 23.9% | 31.7% |


## Baltimore Orioles Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gunnar Henderson | 399 | 0.222 | 0.416 | 0.194 | 0.326 | 0.306 | 8.2% | 26.4% | 21.6% |
| Taylor Ward | 394 | 0.255 | 0.357 | 0.102 | 0.345 | 0.348 | 5.0% | 24.2% | 17.0% |
| Pete Alonso | 391 | 0.251 | 0.469 | 0.218 | 0.349 | 0.381 | 13.3% | 33.5% | 26.1% |
| Leody Taveras | 275 | 0.242 | 0.362 | 0.121 | 0.310 | 0.286 | 5.1% | 19.3% | 25.0% |
| Samuel Basallo | 274 | 0.257 | 0.478 | 0.221 | 0.347 | 0.337 | 12.8% | 27.1% | 26.5% |
| Adley Rutschman | 247 | 0.261 | 0.454 | 0.193 | 0.350 | 0.357 | 8.6% | 27.4% | 12.6% |
| Coby Mayo | 245 | 0.186 | 0.376 | 0.190 | 0.282 | 0.284 | 9.9% | 30.5% | 29.8% |
| Colton Cowser | 223 | 0.223 | 0.378 | 0.155 | 0.312 | 0.325 | 12.2% | 20.7% | 32.4% |
| Jeremiah Jackson | 218 | 0.265 | 0.431 | 0.166 | 0.322 | 0.289 | 7.6% | 27.4% | 23.7% |
| Blaze Alexander | 215 | 0.297 | 0.415 | 0.118 | 0.347 | 0.351 | 6.8% | 24.3% | 24.7% |
| Tyler O'Neill | 166 | 0.184 | 0.272 | 0.088 | 0.260 | 0.284 | 6.9% | 26.0% | 27.4% |
| Dylan Beavers | 126 | 0.229 | 0.349 | 0.119 | 0.308 | 0.306 | 5.0% | 21.8% | 19.7% |


## Bullpen Fatigue Report

### Chicago White Sox Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brandon Eisert | 2026-06-26 | 1.0 | 10 |
| Bryan Hudson | 2026-06-28 | 1.0 | 15 |
| Chris Murphy | 2026-06-28 | 0.2 | 7 |
| Grant Taylor | 2026-06-27 | 2.0 | 19 |
| Jordan Hicks | 2026-06-26 | 1.0 | 18 |
| Jordan Hicks | 2026-06-28 | 1.1 | 13 |
| Sean Newcomb | 2026-06-27 | 1.2 | 30 |
| Seranthony Domínguez | 2026-06-28 | 1.0 | 18 |
| Trevor Richards | 2026-06-26 | 1.0 | 9 |
| Trevor Richards | 2026-06-28 | 1.1 | 16 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Bryan Hudson, Chris Murphy, Jordan Hicks, Seranthony Domínguez, Trevor Richards


### Baltimore Orioles Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Albert Suárez | 2026-06-28 | 3.0 | 37 |
| Andrew Kittredge | 2026-06-27 | 1.0 | 14 |
| Grant Wolfram | 2026-06-26 | 1.0 | 10 |
| Grant Wolfram | 2026-06-28 | 1.0 | 9 |
| Keegan Akin | 2026-06-27 | 2.0 | 35 |
| Rico Garcia | 2026-06-27 | 1.0 | 18 |
| Ryan Helsley | 2026-06-26 | 1.0 | 12 |
| Ryan Helsley | 2026-06-27 | 1.0 | 21 |
| Tyler Wells | 2026-06-26 | 0.2 | 6 |
| Tyler Wells | 2026-06-28 | 1.0 | 16 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Albert Suárez, Grant Wolfram, Tyler Wells



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Miguel Vargas | 373 | 0.245 | 0.487 | 0.242 | 0.375 | 14.0% | 27.9% |
| 2 | Chase Meidroth | 362 | 0.282 | 0.402 | 0.121 | 0.338 | 4.7% | 22.3% |
| 3 | Colson Montgomery | 352 | 0.212 | 0.450 | 0.238 | 0.329 | 13.4% | 29.8% |
| 4 | Andrew Benintendi | 273 | 0.237 | 0.438 | 0.201 | 0.319 | 11.7% | 28.8% |
| 5 | Sam Antonacci | 269 | 0.294 | 0.412 | 0.118 | 0.377 | 7.0% | 22.9% |
| 6 | Munetaka Murakami | 264 | 0.236 | 0.546 | 0.310 | 0.394 | 20.5% | 37.1% |
| 7 | Tristan Peters | 248 | 0.285 | 0.448 | 0.163 | 0.353 | 5.0% | 21.2% |
| 8 | Edgar Quero | 191 | 0.181 | 0.223 | 0.042 | 0.237 | 2.3% | 21.6% |
| 9 | Luisangel Acuña | 166 | 0.229 | 0.268 | 0.039 | 0.243 | 4.7% | 26.5% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Gunnar Henderson | 399 | 0.222 | 0.416 | 0.194 | 0.326 | 8.2% | 26.4% |
| 2 | Taylor Ward | 394 | 0.255 | 0.357 | 0.102 | 0.345 | 5.0% | 24.2% |
| 3 | Pete Alonso | 391 | 0.251 | 0.469 | 0.218 | 0.349 | 13.3% | 33.5% |
| 4 | Leody Taveras | 275 | 0.242 | 0.362 | 0.121 | 0.310 | 5.1% | 19.3% |
| 5 | Samuel Basallo | 274 | 0.257 | 0.478 | 0.221 | 0.347 | 12.8% | 27.1% |
| 6 | Adley Rutschman | 247 | 0.261 | 0.454 | 0.193 | 0.350 | 8.6% | 27.4% |
| 7 | Coby Mayo | 245 | 0.186 | 0.376 | 0.190 | 0.282 | 9.9% | 30.5% |
| 8 | Colton Cowser | 223 | 0.223 | 0.378 | 0.155 | 0.312 | 12.2% | 20.7% |
| 9 | Jeremiah Jackson | 218 | 0.265 | 0.431 | 0.166 | 0.322 | 7.6% | 27.4% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6951 |
| Hits Allowed | 1465 |
| Walks/HBP | 774 |
| Strikeouts | 1577 |
| Home Runs Allowed | 227 |
| K Event Rate | 22.7% |
| BB/HBP Event Rate | 11.1% |
| HR Event Rate | 3.3% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7075 |
| Hits Allowed | 1525 |
| Walks/HBP | 717 |
| Strikeouts | 1617 |
| Home Runs Allowed | 211 |
| K Event Rate | 22.9% |
| BB/HBP Event Rate | 10.1% |
| HR Event Rate | 3.0% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, KC, SL, SI
- Home pitcher pitch mix to inspect: FF, KC, FC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 2. Pittsburgh Pirates @ Philadelphia Phillies

## Game Context

| Field | Value |
| --- | --- |
| Park | Citizens Bank Park |
| Time | 2026-06-29T22:40:00Z |
| Away Team | Pittsburgh Pirates |
| Home Team | Philadelphia Phillies |
| Away Probable Pitcher | Braxton Ashcraft |
| Home Probable Pitcher | Aaron Nola |


## Away Starting Pitcher: Braxton Ashcraft

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1493 |
| Batted/Result Events | 415 |
| Hits Allowed | 88 |
| Walks | 22 |
| Strikeouts | 115 |
| Home Runs | 8 |
| K Event Rate | 27.7% |
| BB Event Rate | 5.3% |
| HR Event Rate | 1.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | PIT | 7.7 | 5 | 0 | 0 | 10 | 0 |
| 2026-06-17 | ATH | 8.3 | 4 | 0 | 3 | 7 | 0 |
| 2026-06-12 | PIT | 7.3 | 5 | 0 | 2 | 4 | 0 |
| 2026-06-06 | ATL | 8.3 | 9 | 1 | 1 | 5 | 1 |
| 2026-05-31 | PIT | 7.3 | 5 | 1 | 0 | 11 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 16.3% | 244 | 0.092 | 0.169 | 0.077 | 0.148 | 0.189 | 10.3% | 34.8% | 42.4% |
| CU | vs R | 9.0% | 135 | 0.176 | 0.265 | 0.088 | 0.219 | 0.219 | 0.0% | 19.4% | 38.6% |
| FF | vs L | 20.0% | 298 | 0.333 | 0.625 | 0.292 | 0.436 | 0.344 | 10.2% | 24.8% | 18.7% |
| FF | vs R | 10.7% | 160 | 0.189 | 0.243 | 0.054 | 0.210 | 0.213 | 12.5% | 16.7% | 9.1% |
| FS | vs L | 4.5% | 67 | 0.357 | 0.357 | 0.000 | 0.321 | 0.266 | 0.0% | 20.0% | 6.9% |
| SI | vs L | 5.2% | 78 | 0.368 | 0.421 | 0.053 | 0.383 | 0.350 | 0.0% | 20.8% | 11.8% |
| SI | vs R | 10.4% | 156 | 0.186 | 0.209 | 0.023 | 0.205 | 0.301 | 0.0% | 36.4% | 19.3% |
| SL | vs L | 11.0% | 164 | 0.250 | 0.306 | 0.056 | 0.352 | 0.301 | 0.0% | 43.1% | 31.9% |
| SL | vs R | 12.8% | 191 | 0.267 | 0.367 | 0.100 | 0.319 | 0.228 | 4.8% | 17.1% | 30.9% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-24 | 86 | 5 | 0 | 10 | 0 |
| 2026-06-17 | 93 | 4 | 3 | 7 | 0 |
| 2026-06-12 | 90 | 5 | 2 | 4 | 0 |
| 2026-06-06 | 86 | 9 | 0 | 5 | 1 |
| 2026-05-31 | 80 | 5 | 0 | 11 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SI | Otto Kemp | 6 | 0.333 | 1.333 | 1.000 | 0.667 | 0.102 | 40.0% | 21.4% | 5.9% |
| CU | Brandon Marsh | 20 | 0.444 | 1.056 | 0.611 | 0.630 | 0.405 | 15.4% | 27.3% | 23.9% |
| SI | Kyle Schwarber | 58 | 0.391 | 0.891 | 0.500 | 0.584 | 0.544 | 23.7% | 36.1% | 16.3% |
| FF | Bryce Harper | 89 | 0.306 | 0.722 | 0.417 | 0.471 | 0.469 | 14.0% | 27.4% | 21.1% |
| FF | Kyle Schwarber | 101 | 0.262 | 0.655 | 0.393 | 0.433 | 0.376 | 19.6% | 35.3% | 21.5% |
| FF | Edmundo Sosa | 43 | 0.421 | 0.763 | 0.342 | 0.493 | 0.474 | 17.1% | 27.2% | 14.4% |
| SL | Bryson Stott | 35 | 0.375 | 0.656 | 0.281 | 0.461 | 0.333 | 8.3% | 30.4% | 19.7% |
| SL | Bryce Harper | 51 | 0.216 | 0.486 | 0.270 | 0.376 | 0.511 | 32.1% | 35.8% | 46.7% |
| CU | Kyle Schwarber | 26 | 0.130 | 0.391 | 0.261 | 0.269 | 0.314 | 25.0% | 32.0% | 45.8% |
| SL | Adolis García | 48 | 0.217 | 0.478 | 0.261 | 0.307 | 0.243 | 7.1% | 26.1% | 36.5% |
| SI | Brandon Marsh | 51 | 0.370 | 0.630 | 0.261 | 0.472 | 0.442 | 9.5% | 31.8% | 6.6% |
| CU | Adolis García | 13 | 0.250 | 0.500 | 0.250 | 0.346 | 0.374 | 25.0% | 41.7% | 50.0% |
| SL | J. T. Realmuto | 27 | 0.208 | 0.458 | 0.250 | 0.367 | 0.319 | 10.5% | 42.9% | 33.3% |
| SL | Brandon Marsh | 40 | 0.225 | 0.450 | 0.225 | 0.283 | 0.229 | 16.0% | 26.1% | 28.9% |
| SL | Edmundo Sosa | 25 | 0.200 | 0.400 | 0.200 | 0.252 | 0.327 | 16.7% | 23.3% | 36.2% |
| SI | Bryson Stott | 48 | 0.267 | 0.444 | 0.178 | 0.328 | 0.344 | 7.3% | 24.2% | 10.7% |
| FF | Rafael Marchán | 39 | 0.108 | 0.270 | 0.162 | 0.185 | 0.206 | 5.7% | 15.6% | 8.2% |
| SI | Trea Turner | 79 | 0.227 | 0.387 | 0.160 | 0.287 | 0.343 | 8.5% | 41.0% | 9.5% |
| FF | Brandon Marsh | 100 | 0.385 | 0.527 | 0.143 | 0.427 | 0.371 | 8.2% | 24.3% | 16.2% |
| SL | Kyle Schwarber | 53 | 0.224 | 0.367 | 0.143 | 0.305 | 0.360 | 19.2% | 36.8% | 36.1% |
| FF | Trea Turner | 109 | 0.312 | 0.452 | 0.140 | 0.394 | 0.355 | 7.0% | 28.9% | 18.0% |
| SI | Adolis García | 62 | 0.160 | 0.300 | 0.140 | 0.281 | 0.328 | 10.3% | 35.5% | 14.5% |
| FF | Alec Bohm | 101 | 0.202 | 0.337 | 0.135 | 0.298 | 0.256 | 2.8% | 19.6% | 12.0% |
| CU | Justin Crawford | 17 | 0.188 | 0.312 | 0.125 | 0.241 | 0.237 | 0.0% | 35.0% | 22.2% |
| SL | Trea Turner | 60 | 0.140 | 0.263 | 0.123 | 0.212 | 0.226 | 2.4% | 19.1% | 32.8% |
| SI | Bryce Harper | 51 | 0.302 | 0.419 | 0.116 | 0.361 | 0.349 | 2.6% | 24.1% | 13.6% |
| FF | J. T. Realmuto | 79 | 0.200 | 0.314 | 0.114 | 0.287 | 0.320 | 5.5% | 21.1% | 18.3% |
| CU | J. T. Realmuto | 10 | 0.333 | 0.444 | 0.111 | 0.375 | 0.302 | 0.0% | 33.3% | 37.5% |
| SL | Alec Bohm | 38 | 0.222 | 0.333 | 0.111 | 0.293 | 0.305 | 3.2% | 34.1% | 25.4% |
| SI | Justin Crawford | 45 | 0.231 | 0.333 | 0.103 | 0.304 | 0.288 | 0.0% | 23.4% | 6.2% |


## Home Starting Pitcher: Aaron Nola

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1512 |
| Batted/Result Events | 375 |
| Hits Allowed | 96 |
| Walks | 30 |
| Strikeouts | 86 |
| Home Runs | 18 |
| K Event Rate | 22.9% |
| BB Event Rate | 8.0% |
| HR Event Rate | 4.8% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | WSH | 7.0 | 3 | 2 | 3 | 5 | 2 |
| 2026-06-18 | PHI | 8.0 | 7 | 2 | 1 | 6 | 2 |
| 2026-06-13 | MIL | 7.3 | 6 | 2 | 2 | 3 | 2 |
| 2026-06-07 | PHI | 7.7 | 6 | 0 | 4 | 4 | 0 |
| 2026-06-02 | PHI | 6.3 | 4 | 1 | 0 | 8 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 10.6% | 161 | 0.100 | 0.100 | 0.000 | 0.145 | 0.272 | 3.6% | 23.5% | 16.7% |
| CH | vs R | 2.0% | 30 | 0.333 | 0.833 | 0.500 | 0.514 | 0.156 | 20.0% | 30.0% | 16.7% |
| FC | vs L | 4.0% | 60 | 0.333 | 0.600 | 0.267 | 0.416 | 0.277 | 0.0% | 38.1% | 24.2% |
| FC | vs R | 4.4% | 67 | 0.444 | 0.611 | 0.167 | 0.471 | 0.384 | 0.0% | 28.6% | 19.4% |
| FF | vs L | 17.0% | 257 | 0.458 | 0.854 | 0.396 | 0.577 | 0.488 | 17.5% | 28.4% | 12.4% |
| FF | vs R | 7.3% | 110 | 0.318 | 0.682 | 0.364 | 0.407 | 0.357 | 21.4% | 25.9% | 18.9% |
| KC | vs L | 20.0% | 302 | 0.220 | 0.424 | 0.203 | 0.320 | 0.258 | 7.7% | 20.9% | 33.8% |
| KC | vs R | 13.5% | 204 | 0.197 | 0.303 | 0.106 | 0.229 | 0.213 | 6.8% | 15.4% | 36.9% |
| SI | vs L | 8.8% | 133 | 0.324 | 0.559 | 0.235 | 0.440 | 0.401 | 7.4% | 38.1% | 8.2% |
| SI | vs R | 11.6% | 175 | 0.316 | 0.579 | 0.263 | 0.388 | 0.344 | 13.3% | 25.5% | 11.1% |
| SL | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SL | vs R | 0.7% | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.145 | 0.0% | 42.9% | 22.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-24 | 86 | 3 | 2 | 5 | 2 |
| 2026-06-18 | 97 | 7 | 1 | 6 | 2 |
| 2026-06-13 | 85 | 6 | 2 | 3 | 2 |
| 2026-06-07 | 99 | 6 | 4 | 4 | 0 |
| 2026-06-02 | 95 | 4 | 0 | 8 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Oneil Cruz | 18 | 0.333 | 1.000 | 0.667 | 0.569 | 0.552 | 36.4% | 33.3% | 27.5% |
| FC | Henry Davis | 11 | 0.273 | 0.818 | 0.545 | 0.445 | 0.289 | 20.0% | 31.2% | 19.2% |
| FC | Ryan O'Hearn | 19 | 0.188 | 0.562 | 0.375 | 0.368 | 0.391 | 18.2% | 18.2% | 16.3% |
| FF | Brandon Lowe | 94 | 0.278 | 0.646 | 0.367 | 0.437 | 0.416 | 27.8% | 25.4% | 29.6% |
| CH | Brandon Lowe | 42 | 0.231 | 0.590 | 0.359 | 0.369 | 0.391 | 12.9% | 24.1% | 31.8% |
| FF | Konnor Griffin | 49 | 0.220 | 0.537 | 0.317 | 0.376 | 0.337 | 15.8% | 15.0% | 24.7% |
| FF | Bryan Reynolds | 114 | 0.347 | 0.621 | 0.274 | 0.469 | 0.428 | 13.3% | 31.3% | 16.5% |
| FF | Ryan O'Hearn | 105 | 0.316 | 0.568 | 0.253 | 0.416 | 0.348 | 8.9% | 26.5% | 12.0% |
| KC | Nick Gonzales | 4 | 0.250 | 0.500 | 0.250 | 0.312 | 0.467 | 33.3% | 20.0% | 37.5% |
| FF | Spencer Horwitz | 115 | 0.269 | 0.495 | 0.226 | 0.391 | 0.378 | 12.3% | 18.5% | 12.8% |
| FC | Spencer Horwitz | 26 | 0.208 | 0.417 | 0.208 | 0.269 | 0.203 | 4.8% | 13.2% | 15.6% |
| FC | Brandon Lowe | 30 | 0.292 | 0.500 | 0.208 | 0.410 | 0.359 | 0.0% | 37.1% | 32.8% |
| FF | Oneil Cruz | 91 | 0.291 | 0.481 | 0.190 | 0.392 | 0.388 | 15.1% | 37.1% | 27.0% |
| SI | Henry Davis | 41 | 0.219 | 0.406 | 0.188 | 0.349 | 0.421 | 10.0% | 37.7% | 8.7% |
| FC | Marcell Ozuna | 17 | 0.188 | 0.375 | 0.188 | 0.265 | 0.243 | 9.1% | 17.4% | 34.2% |
| FF | Marcell Ozuna | 86 | 0.247 | 0.429 | 0.182 | 0.331 | 0.441 | 12.9% | 30.0% | 16.7% |
| FC | Konnor Griffin | 18 | 0.412 | 0.588 | 0.176 | 0.497 | 0.381 | 14.3% | 34.4% | 24.4% |
| FF | Henry Davis | 55 | 0.149 | 0.319 | 0.170 | 0.318 | 0.267 | 13.3% | 25.8% | 25.7% |
| SI | Nick Yorke | 29 | 0.269 | 0.423 | 0.154 | 0.371 | 0.343 | 4.2% | 36.1% | 6.8% |
| SI | Ryan O'Hearn | 55 | 0.360 | 0.500 | 0.140 | 0.420 | 0.426 | 9.3% | 38.1% | 8.2% |
| CH | Oneil Cruz | 41 | 0.216 | 0.351 | 0.135 | 0.288 | 0.273 | 14.3% | 24.2% | 51.4% |
| SI | Bryan Reynolds | 45 | 0.387 | 0.516 | 0.129 | 0.490 | 0.463 | 7.1% | 38.9% | 9.4% |
| CH | Bryan Reynolds | 63 | 0.255 | 0.382 | 0.127 | 0.332 | 0.342 | 4.1% | 26.6% | 25.3% |
| KC | Oneil Cruz | 9 | 0.125 | 0.250 | 0.125 | 0.217 | 0.356 | 20.0% | 42.9% | 42.9% |
| CH | Spencer Horwitz | 28 | 0.280 | 0.400 | 0.120 | 0.339 | 0.381 | 8.3% | 20.8% | 12.3% |
| SI | Marcell Ozuna | 57 | 0.235 | 0.353 | 0.118 | 0.301 | 0.319 | 2.6% | 33.9% | 11.5% |
| FF | Jake Mangum | 59 | 0.362 | 0.468 | 0.106 | 0.434 | 0.351 | 6.1% | 13.9% | 18.4% |
| CH | Nick Gonzales | 23 | 0.350 | 0.450 | 0.100 | 0.396 | 0.348 | 0.0% | 17.9% | 34.0% |
| SI | Jared Triolo | 37 | 0.226 | 0.323 | 0.097 | 0.361 | 0.325 | 0.0% | 32.4% | 12.5% |
| KC | Brandon Lowe | 11 | 0.455 | 0.545 | 0.091 | 0.441 | 0.339 | 0.0% | 23.1% | 34.8% |


## Pittsburgh Pirates Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bryan Reynolds | 381 | 0.286 | 0.463 | 0.178 | 0.387 | 0.374 | 9.7% | 29.7% | 26.0% |
| Brandon Lowe | 361 | 0.242 | 0.497 | 0.255 | 0.354 | 0.346 | 13.1% | 29.0% | 32.4% |
| Nick Gonzales | 334 | 0.293 | 0.368 | 0.075 | 0.327 | 0.326 | 2.9% | 21.9% | 21.1% |
| Spencer Horwitz | 313 | 0.271 | 0.447 | 0.176 | 0.368 | 0.339 | 8.5% | 21.0% | 14.0% |
| Ryan O'Hearn | 303 | 0.272 | 0.453 | 0.181 | 0.345 | 0.326 | 7.6% | 26.2% | 19.5% |
| Oneil Cruz | 300 | 0.261 | 0.470 | 0.208 | 0.368 | 0.358 | 16.9% | 36.9% | 35.3% |
| Marcell Ozuna | 248 | 0.204 | 0.320 | 0.116 | 0.276 | 0.315 | 8.1% | 27.2% | 29.1% |
| Konnor Griffin | 232 | 0.262 | 0.410 | 0.148 | 0.337 | 0.310 | 8.8% | 24.9% | 30.6% |
| Jake Mangum | 218 | 0.289 | 0.338 | 0.050 | 0.323 | 0.274 | 1.2% | 13.8% | 17.5% |
| Jared Triolo | 182 | 0.229 | 0.283 | 0.054 | 0.298 | 0.276 | 0.8% | 25.2% | 22.9% |
| Henry Davis | 175 | 0.162 | 0.331 | 0.169 | 0.284 | 0.295 | 12.0% | 31.5% | 22.4% |
| Nick Yorke | 107 | 0.202 | 0.277 | 0.074 | 0.264 | 0.306 | 5.1% | 28.3% | 14.7% |


## Philadelphia Phillies Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Trea Turner | 382 | 0.225 | 0.326 | 0.101 | 0.280 | 0.287 | 5.2% | 27.1% | 25.4% |
| Kyle Schwarber | 367 | 0.253 | 0.590 | 0.337 | 0.407 | 0.390 | 21.0% | 35.5% | 31.7% |
| Bryce Harper | 358 | 0.275 | 0.526 | 0.252 | 0.389 | 0.409 | 12.5% | 28.5% | 28.1% |
| Alec Bohm | 339 | 0.223 | 0.348 | 0.126 | 0.298 | 0.291 | 4.2% | 26.0% | 14.1% |
| Brandon Marsh | 327 | 0.316 | 0.498 | 0.182 | 0.370 | 0.327 | 8.8% | 24.3% | 22.6% |
| Bryson Stott | 317 | 0.245 | 0.403 | 0.159 | 0.311 | 0.316 | 7.1% | 25.4% | 15.6% |
| Adolis García | 278 | 0.207 | 0.358 | 0.150 | 0.290 | 0.294 | 9.9% | 28.4% | 30.8% |
| Justin Crawford | 270 | 0.243 | 0.335 | 0.092 | 0.289 | 0.268 | 1.0% | 19.2% | 16.7% |
| J. T. Realmuto | 233 | 0.209 | 0.330 | 0.121 | 0.291 | 0.318 | 4.9% | 27.2% | 23.0% |
| Edmundo Sosa | 160 | 0.225 | 0.377 | 0.152 | 0.301 | 0.341 | 8.5% | 26.0% | 23.8% |
| Rafael Marchán | 95 | 0.111 | 0.178 | 0.067 | 0.183 | 0.205 | 2.8% | 16.2% | 16.5% |
| Otto Kemp | 48 | 0.156 | 0.311 | 0.156 | 0.228 | 0.205 | 6.9% | 12.3% | 30.9% |


## Bullpen Fatigue Report

### Pittsburgh Pirates Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brandan Bidois | 2026-06-26 | 1.0 | 10 |
| Carmen Mlodzinski | 2026-06-28 | 2.0 | 42 |
| Dennis Santana | 2026-06-26 | 1.1 | 14 |
| Dennis Santana | 2026-06-28 | 1.0 | 23 |
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


**Caution arms (pitched yesterday, or 3+ appearances in window):** Carmen Mlodzinski, Dennis Santana


### Philadelphia Phillies Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alan Rangel | 2026-06-27 | 4.0 | 70 |
| Chase Shugart | 2026-06-25 | 1.0 | 18 |
| Chase Shugart | 2026-06-28 | 0.1 | 20 |
| Jhoan Duran | 2026-06-26 | 1.0 | 17 |
| Jhoan Duran | 2026-06-28 | 1.0 | 20 |
| Jonathan Bowlan | 2026-06-27 | 0.2 | 10 |
| José Alvarado | 2026-06-25 | 1.0 | 12 |
| José Alvarado | 2026-06-28 | 1.0 | 24 |
| Kyle Backhus | 2026-06-27 | 1.0 | 27 |
| Kyle Backhus | 2026-06-28 | 0.2 | 8 |
| Orion Kerkering | 2026-06-25 | 1.0 | 11 |
| Orion Kerkering | 2026-06-26 | 1.0 | 11 |
| Orion Kerkering | 2026-06-28 | 1.0 | 27 |
| Seth Johnson | 2026-06-27 | 1.0 | 16 |
| Tim Mayza | 2026-06-25 | 1.0 | 12 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Chase Shugart, Jhoan Duran, José Alvarado, Kyle Backhus, Orion Kerkering



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bryan Reynolds | 381 | 0.286 | 0.463 | 0.178 | 0.387 | 9.7% | 29.7% |
| 2 | Brandon Lowe | 361 | 0.242 | 0.497 | 0.255 | 0.354 | 13.1% | 29.0% |
| 3 | Nick Gonzales | 334 | 0.293 | 0.368 | 0.075 | 0.327 | 2.9% | 21.9% |
| 4 | Spencer Horwitz | 313 | 0.271 | 0.447 | 0.176 | 0.368 | 8.5% | 21.0% |
| 5 | Ryan O'Hearn | 303 | 0.272 | 0.453 | 0.181 | 0.345 | 7.6% | 26.2% |
| 6 | Oneil Cruz | 300 | 0.261 | 0.470 | 0.208 | 0.368 | 16.9% | 36.9% |
| 7 | Marcell Ozuna | 248 | 0.204 | 0.320 | 0.116 | 0.276 | 8.1% | 27.2% |
| 8 | Konnor Griffin | 232 | 0.262 | 0.410 | 0.148 | 0.337 | 8.8% | 24.9% |
| 9 | Jake Mangum | 218 | 0.289 | 0.338 | 0.050 | 0.323 | 1.2% | 13.8% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Trea Turner | 382 | 0.225 | 0.326 | 0.101 | 0.280 | 5.2% | 27.1% |
| 2 | Kyle Schwarber | 367 | 0.253 | 0.590 | 0.337 | 0.407 | 21.0% | 35.5% |
| 3 | Bryce Harper | 358 | 0.275 | 0.526 | 0.252 | 0.389 | 12.5% | 28.5% |
| 4 | Alec Bohm | 339 | 0.223 | 0.348 | 0.126 | 0.298 | 4.2% | 26.0% |
| 5 | Brandon Marsh | 327 | 0.316 | 0.498 | 0.182 | 0.370 | 8.8% | 24.3% |
| 6 | Bryson Stott | 317 | 0.245 | 0.403 | 0.159 | 0.311 | 7.1% | 25.4% |
| 7 | Adolis García | 278 | 0.207 | 0.358 | 0.150 | 0.290 | 9.9% | 28.4% |
| 8 | Justin Crawford | 270 | 0.243 | 0.335 | 0.092 | 0.289 | 1.0% | 19.2% |
| 9 | J. T. Realmuto | 233 | 0.209 | 0.330 | 0.121 | 0.291 | 4.9% | 27.2% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7201 |
| Hits Allowed | 1557 |
| Walks/HBP | 766 |
| Strikeouts | 1724 |
| Home Runs Allowed | 204 |
| K Event Rate | 23.9% |
| BB/HBP Event Rate | 10.6% |
| HR Event Rate | 2.8% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6986 |
| Hits Allowed | 1534 |
| Walks/HBP | 599 |
| Strikeouts | 1674 |
| Home Runs Allowed | 221 |
| K Event Rate | 24.0% |
| BB/HBP Event Rate | 8.6% |
| HR Event Rate | 3.2% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, CU, SL, SI
- Home pitcher pitch mix to inspect: KC, FF, SI, CH, FC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 3. Detroit Tigers @ New York Yankees

## Game Context

| Field | Value |
| --- | --- |
| Park | Yankee Stadium |
| Time | 2026-06-29T23:05:00Z |
| Away Team | Detroit Tigers |
| Home Team | New York Yankees |
| Away Probable Pitcher | Casey Mize |
| Home Probable Pitcher | Ryan Weathers |


## Away Starting Pitcher: Casey Mize

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1014 |
| Batted/Result Events | 270 |
| Hits Allowed | 58 |
| Walks | 17 |
| Strikeouts | 67 |
| Home Runs | 5 |
| K Event Rate | 24.8% |
| BB Event Rate | 6.3% |
| HR Event Rate | 1.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | DET | 8.3 | 8 | 1 | 1 | 6 | 1 |
| 2026-06-17 | HOU | 7.0 | 6 | 1 | 1 | 3 | 1 |
| 2026-05-27 | DET | 4.7 | 2 | 0 | 1 | 6 | 0 |
| 2026-05-21 | DET | 8.0 | 4 | 0 | 0 | 4 | 0 |
| 2026-05-16 | DET | 6.3 | 2 | 0 | 0 | 4 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF | vs L | 24.0% | 243 | 0.208 | 0.358 | 0.151 | 0.297 | 0.255 | 2.3% | 18.2% | 15.8% |
| FF | vs R | 10.6% | 107 | 0.286 | 0.571 | 0.286 | 0.389 | 0.353 | 23.1% | 25.0% | 38.3% |
| FS | vs L | 17.6% | 178 | 0.210 | 0.323 | 0.113 | 0.236 | 0.187 | 5.3% | 14.0% | 36.7% |
| FS | vs R | 7.5% | 76 | 0.333 | 0.500 | 0.167 | 0.483 | 0.390 | 0.0% | 34.5% | 31.1% |
| SI | vs R | 11.3% | 115 | 0.294 | 0.382 | 0.088 | 0.329 | 0.324 | 6.2% | 24.5% | 14.8% |
| SL | vs L | 16.1% | 163 | 0.160 | 0.320 | 0.160 | 0.247 | 0.286 | 15.8% | 31.7% | 26.2% |
| SL | vs R | 7.7% | 78 | 0.217 | 0.565 | 0.348 | 0.338 | 0.317 | 13.3% | 30.4% | 40.0% |
| SV | vs L | 1.1% | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.812 | 0.0% | 100.0% | 0.0% |
| SV | vs R | 4.2% | 43 | 0.273 | 0.273 | 0.000 | 0.245 | 0.267 | 0.0% | 15.4% | 23.5% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 97 | 8 | 1 | 6 | 1 |
| 2026-06-17 | 86 | 6 | 1 | 3 | 1 |
| 2026-05-27 | 58 | 2 | 1 | 6 | 0 |
| 2026-05-21 | 95 | 4 | 0 | 4 | 0 |
| 2026-05-16 | 71 | 2 | 0 | 4 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FS | Aaron Judge | 8 | 0.375 | 1.125 | 0.750 | 0.613 | 0.628 | 75.0% | 66.7% | 65.0% |
| FF | Ben Rice | 81 | 0.353 | 0.985 | 0.632 | 0.585 | 0.549 | 30.8% | 39.8% | 16.9% |
| SL | Giancarlo Stanton | 14 | 0.385 | 1.000 | 0.615 | 0.579 | 0.531 | 42.9% | 30.8% | 44.8% |
| FF | Paul Goldschmidt | 67 | 0.386 | 0.965 | 0.579 | 0.568 | 0.434 | 22.9% | 27.3% | 17.0% |
| SI | Giancarlo Stanton | 12 | 0.417 | 0.917 | 0.500 | 0.558 | 0.482 | 27.3% | 37.5% | 20.0% |
| SL | Cody Bellinger | 41 | 0.364 | 0.848 | 0.485 | 0.548 | 0.454 | 16.7% | 26.4% | 20.8% |
| FS | José Caballero | 9 | 0.556 | 1.000 | 0.444 | 0.761 | 0.496 | 14.3% | 18.8% | 24.0% |
| FS | Cody Bellinger | 18 | 0.188 | 0.562 | 0.375 | 0.311 | 0.410 | 33.3% | 44.4% | 15.4% |
| FS | Giancarlo Stanton | 3 | 1.000 | 1.333 | 0.333 | 1.017 | 0.925 | 33.3% | 50.0% | 14.3% |
| SL | Jazz Chisholm | 47 | 0.238 | 0.571 | 0.333 | 0.374 | 0.315 | 13.8% | 34.7% | 38.1% |
| FF | Aaron Judge | 54 | 0.233 | 0.558 | 0.326 | 0.404 | 0.467 | 26.9% | 24.7% | 22.9% |
| SL | Trent Grisham | 23 | 0.158 | 0.474 | 0.316 | 0.374 | 0.283 | 18.2% | 30.0% | 34.4% |
| SI | Aaron Judge | 47 | 0.389 | 0.694 | 0.306 | 0.547 | 0.541 | 17.9% | 30.8% | 10.8% |
| SL | José Caballero | 39 | 0.297 | 0.595 | 0.297 | 0.391 | 0.352 | 3.2% | 20.4% | 31.7% |
| SL | Ben Rice | 53 | 0.318 | 0.568 | 0.250 | 0.432 | 0.374 | 12.1% | 37.7% | 31.9% |
| SI | Jazz Chisholm | 43 | 0.395 | 0.632 | 0.237 | 0.471 | 0.412 | 6.2% | 27.3% | 18.2% |
| SI | Ryan Mcmahon | 33 | 0.179 | 0.393 | 0.214 | 0.336 | 0.376 | 13.6% | 35.1% | 23.5% |
| FF | Anthony Volpe | 41 | 0.267 | 0.467 | 0.200 | 0.416 | 0.405 | 15.0% | 25.0% | 23.9% |
| SL | Amed Rosario | 15 | 0.267 | 0.467 | 0.200 | 0.313 | 0.330 | 12.5% | 22.7% | 36.8% |
| FF | Austin Wells | 66 | 0.200 | 0.382 | 0.182 | 0.325 | 0.320 | 6.8% | 26.0% | 17.6% |
| FF | Ryan Mcmahon | 66 | 0.295 | 0.475 | 0.180 | 0.351 | 0.374 | 14.0% | 19.3% | 18.1% |
| FF | Trent Grisham | 107 | 0.239 | 0.409 | 0.170 | 0.351 | 0.417 | 16.2% | 35.8% | 10.8% |
| SI | Ben Rice | 57 | 0.264 | 0.415 | 0.151 | 0.321 | 0.316 | 7.0% | 34.7% | 11.2% |
| SI | Austin Wells | 38 | 0.206 | 0.353 | 0.147 | 0.274 | 0.318 | 7.4% | 35.7% | 14.3% |
| SI | Trent Grisham | 52 | 0.238 | 0.381 | 0.143 | 0.336 | 0.356 | 8.6% | 32.7% | 6.6% |
| SI | José Caballero | 58 | 0.260 | 0.400 | 0.140 | 0.342 | 0.351 | 7.0% | 19.7% | 11.6% |
| SL | Aaron Judge | 41 | 0.189 | 0.324 | 0.135 | 0.293 | 0.270 | 16.0% | 33.3% | 34.4% |
| SI | Cody Bellinger | 74 | 0.262 | 0.393 | 0.131 | 0.347 | 0.385 | 3.6% | 28.9% | 9.1% |
| FF | Cody Bellinger | 118 | 0.239 | 0.370 | 0.130 | 0.346 | 0.369 | 3.8% | 17.0% | 13.9% |
| FF | Jazz Chisholm | 107 | 0.181 | 0.309 | 0.128 | 0.269 | 0.284 | 6.1% | 26.2% | 20.3% |


## Home Starting Pitcher: Ryan Weathers

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1538 |
| Batted/Result Events | 391 |
| Hits Allowed | 87 |
| Walks | 26 |
| Strikeouts | 104 |
| Home Runs | 19 |
| K Event Rate | 26.6% |
| BB Event Rate | 6.6% |
| HR Event Rate | 4.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | DET | 8.7 | 6 | 0 | 2 | 6 | 0 |
| 2026-06-18 | NYY | 7.3 | 3 | 1 | 1 | 8 | 1 |
| 2026-06-12 | TOR | 6.7 | 5 | 2 | 2 | 2 | 2 |
| 2026-06-05 | NYY | 8.7 | 7 | 2 | 1 | 4 | 2 |
| 2026-05-30 | ATH | 9.7 | 6 | 3 | 3 | 10 | 3 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 1.5% | 23 | 0.143 | 0.143 | 0.000 | 0.129 | 0.199 | 0.0% | 12.5% | 33.3% |
| CH | vs R | 21.0% | 323 | 0.205 | 0.341 | 0.136 | 0.236 | 0.246 | 7.9% | 25.5% | 34.9% |
| FF | vs L | 4.0% | 61 | 0.333 | 0.889 | 0.556 | 0.503 | 0.382 | 41.7% | 52.9% | 28.6% |
| FF | vs R | 24.6% | 378 | 0.278 | 0.595 | 0.316 | 0.403 | 0.441 | 18.3% | 24.1% | 14.5% |
| SI | vs L | 7.0% | 107 | 0.387 | 0.484 | 0.097 | 0.420 | 0.463 | 8.0% | 27.7% | 9.1% |
| SI | vs R | 12.0% | 185 | 0.222 | 0.311 | 0.089 | 0.296 | 0.378 | 7.1% | 27.8% | 6.4% |
| SL | vs L | 2.9% | 44 | 0.167 | 0.167 | 0.000 | 0.192 | 0.211 | 0.0% | 7.7% | 31.6% |
| SL | vs R | 6.4% | 99 | 0.182 | 0.394 | 0.212 | 0.267 | 0.243 | 25.0% | 34.2% | 30.4% |
| ST | vs L | 5.7% | 88 | 0.235 | 0.294 | 0.059 | 0.258 | 0.234 | 0.0% | 21.4% | 51.6% |
| ST | vs R | 14.9% | 229 | 0.188 | 0.375 | 0.188 | 0.277 | 0.246 | 13.3% | 15.6% | 40.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-24 | 97 | 6 | 2 | 6 | 0 |
| 2026-06-18 | 88 | 3 | 1 | 8 | 1 |
| 2026-06-12 | 82 | 5 | 1 | 2 | 2 |
| 2026-06-05 | 93 | 7 | 1 | 4 | 2 |
| 2026-05-30 | 107 | 6 | 3 | 10 | 3 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Dillon Dingler | 34 | 0.419 | 1.000 | 0.581 | 0.599 | 0.405 | 12.5% | 34.9% | 26.5% |
| CH | Kerry Carpenter | 32 | 0.385 | 0.846 | 0.462 | 0.577 | 0.366 | 10.5% | 35.9% | 26.7% |
| ST | Dillon Dingler | 28 | 0.269 | 0.731 | 0.462 | 0.432 | 0.407 | 15.0% | 28.6% | 18.0% |
| ST | Kerry Carpenter | 8 | 0.286 | 0.714 | 0.429 | 0.450 | 0.342 | 20.0% | 36.4% | 31.6% |
| ST | Colt Keith | 9 | 0.250 | 0.625 | 0.375 | 0.400 | 0.409 | 20.0% | 25.0% | 30.8% |
| ST | Zach Mckinstry | 10 | 0.250 | 0.625 | 0.375 | 0.430 | 0.493 | 20.0% | 33.3% | 13.3% |
| SI | Jahmai Jones | 23 | 0.167 | 0.500 | 0.333 | 0.365 | 0.494 | 14.3% | 19.2% | 12.9% |
| CH | Wenceel Pérez | 35 | 0.206 | 0.529 | 0.324 | 0.314 | 0.199 | 7.1% | 22.9% | 23.1% |
| FF | Kerry Carpenter | 64 | 0.214 | 0.518 | 0.304 | 0.342 | 0.338 | 10.5% | 28.7% | 22.8% |
| SI | Spencer Torkelson | 65 | 0.298 | 0.596 | 0.298 | 0.405 | 0.448 | 19.1% | 33.0% | 12.4% |
| FF | Spencer Torkelson | 100 | 0.247 | 0.543 | 0.296 | 0.400 | 0.385 | 20.4% | 31.0% | 22.0% |
| FF | Dillon Dingler | 92 | 0.305 | 0.598 | 0.293 | 0.407 | 0.464 | 19.7% | 28.8% | 13.5% |
| SI | Wenceel Pérez | 35 | 0.290 | 0.581 | 0.290 | 0.404 | 0.395 | 17.2% | 23.3% | 9.6% |
| ST | Riley Greene | 22 | 0.312 | 0.562 | 0.250 | 0.502 | 0.442 | 10.0% | 16.0% | 27.5% |
| SI | Gleyber Torres | 44 | 0.333 | 0.583 | 0.250 | 0.447 | 0.329 | 6.5% | 18.6% | 5.7% |
| CH | Colt Keith | 42 | 0.268 | 0.512 | 0.244 | 0.338 | 0.277 | 6.2% | 27.1% | 29.0% |
| SL | Spencer Torkelson | 43 | 0.205 | 0.436 | 0.231 | 0.308 | 0.278 | 11.5% | 26.7% | 32.6% |
| CH | Dillon Dingler | 37 | 0.229 | 0.457 | 0.229 | 0.341 | 0.297 | 8.0% | 34.8% | 34.2% |
| SL | Kevin Mcgonigle | 41 | 0.171 | 0.400 | 0.229 | 0.305 | 0.343 | 16.7% | 24.4% | 19.1% |
| FF | Hao-Yu Lee | 44 | 0.250 | 0.475 | 0.225 | 0.342 | 0.307 | 17.4% | 34.7% | 27.4% |
| SL | Hao-Yu Lee | 14 | 0.143 | 0.357 | 0.214 | 0.207 | 0.103 | 0.0% | 0.0% | 51.9% |
| ST | Matt Vierling | 25 | 0.320 | 0.520 | 0.200 | 0.358 | 0.287 | 0.0% | 17.1% | 8.3% |
| SL | Matt Vierling | 40 | 0.225 | 0.425 | 0.200 | 0.297 | 0.343 | 8.6% | 29.8% | 16.1% |
| SL | Colt Keith | 29 | 0.179 | 0.357 | 0.179 | 0.272 | 0.235 | 16.7% | 32.0% | 34.1% |
| FF | Riley Greene | 136 | 0.265 | 0.436 | 0.171 | 0.351 | 0.356 | 14.3% | 26.5% | 20.2% |
| SI | Kevin Mcgonigle | 83 | 0.386 | 0.557 | 0.171 | 0.455 | 0.412 | 6.2% | 31.0% | 6.1% |
| FF | Gleyber Torres | 66 | 0.226 | 0.396 | 0.170 | 0.354 | 0.374 | 15.8% | 25.0% | 24.0% |
| CH | Spencer Torkelson | 33 | 0.200 | 0.367 | 0.167 | 0.282 | 0.277 | 35.7% | 35.9% | 40.8% |
| ST | Spencer Torkelson | 41 | 0.194 | 0.361 | 0.167 | 0.291 | 0.224 | 5.6% | 17.1% | 43.3% |
| CH | Riley Greene | 58 | 0.200 | 0.364 | 0.164 | 0.251 | 0.250 | 8.3% | 25.8% | 36.0% |


## Detroit Tigers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kevin Mcgonigle | 380 | 0.277 | 0.417 | 0.140 | 0.364 | 0.370 | 8.6% | 23.6% | 13.4% |
| Riley Greene | 376 | 0.290 | 0.442 | 0.152 | 0.366 | 0.355 | 12.7% | 30.7% | 26.8% |
| Spencer Torkelson | 343 | 0.211 | 0.425 | 0.214 | 0.321 | 0.320 | 14.9% | 27.5% | 28.1% |
| Dillon Dingler | 339 | 0.270 | 0.550 | 0.280 | 0.384 | 0.390 | 12.6% | 29.3% | 19.4% |
| Colt Keith | 263 | 0.251 | 0.370 | 0.119 | 0.309 | 0.316 | 8.2% | 28.8% | 20.6% |
| Matt Vierling | 248 | 0.200 | 0.342 | 0.142 | 0.269 | 0.304 | 5.9% | 21.6% | 14.7% |
| Zach Mckinstry | 218 | 0.188 | 0.281 | 0.094 | 0.282 | 0.268 | 1.9% | 12.3% | 12.7% |
| Kerry Carpenter | 217 | 0.220 | 0.450 | 0.230 | 0.326 | 0.307 | 10.3% | 28.7% | 28.4% |
| Gleyber Torres | 200 | 0.289 | 0.410 | 0.120 | 0.367 | 0.343 | 8.4% | 18.5% | 20.5% |
| Wenceel Pérez | 190 | 0.183 | 0.371 | 0.189 | 0.270 | 0.272 | 8.5% | 23.6% | 16.1% |
| Hao-Yu Lee | 130 | 0.252 | 0.382 | 0.130 | 0.300 | 0.273 | 7.9% | 21.0% | 28.6% |
| Jahmai Jones | 114 | 0.165 | 0.262 | 0.097 | 0.249 | 0.298 | 7.6% | 26.8% | 30.7% |


## New York Yankees Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cody Bellinger | 368 | 0.253 | 0.429 | 0.176 | 0.347 | 0.369 | 7.2% | 24.9% | 17.9% |
| Ben Rice | 355 | 0.265 | 0.552 | 0.287 | 0.391 | 0.372 | 13.7% | 31.3% | 23.0% |
| Jazz Chisholm | 338 | 0.221 | 0.391 | 0.171 | 0.312 | 0.296 | 8.4% | 27.6% | 30.1% |
| Trent Grisham | 281 | 0.232 | 0.397 | 0.165 | 0.337 | 0.360 | 11.4% | 32.6% | 15.1% |
| José Caballero | 274 | 0.245 | 0.382 | 0.137 | 0.311 | 0.284 | 4.2% | 16.8% | 24.2% |
| Aaron Judge | 270 | 0.250 | 0.536 | 0.286 | 0.399 | 0.415 | 21.9% | 31.3% | 30.8% |
| Paul Goldschmidt | 239 | 0.282 | 0.532 | 0.250 | 0.380 | 0.338 | 11.9% | 24.7% | 22.4% |
| Ryan Mcmahon | 220 | 0.217 | 0.365 | 0.148 | 0.282 | 0.304 | 12.6% | 26.7% | 28.2% |
| Austin Wells | 201 | 0.154 | 0.240 | 0.086 | 0.234 | 0.289 | 6.6% | 29.4% | 28.1% |
| Amed Rosario | 160 | 0.265 | 0.456 | 0.190 | 0.332 | 0.330 | 9.3% | 27.6% | 22.5% |
| Anthony Volpe | 129 | 0.252 | 0.351 | 0.099 | 0.330 | 0.313 | 4.9% | 21.1% | 23.6% |
| Giancarlo Stanton | 111 | 0.260 | 0.433 | 0.173 | 0.323 | 0.326 | 23.9% | 30.8% | 34.1% |


## Bullpen Fatigue Report

### Detroit Tigers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Drew Anderson | 2026-06-27 | 0.2 | 25 |
| Drew Sommers | 2026-06-27 | 0.1 | 5 |
| Enmanuel De Jesus | 2026-06-26 | 2.0 | 27 |
| Jacob Waguespack | 2026-06-27 | 1.0 | 14 |
| Jacob Waguespack | 2026-06-28 | 0.2 | 5 |
| Kenley Jansen | 2026-06-25 | 1.0 | 15 |
| Kenley Jansen | 2026-06-28 | 1.1 | 28 |
| Kyle Finnegan | 2026-06-25 | 1.0 | 13 |
| Kyle Finnegan | 2026-06-28 | 1.1 | 27 |
| Tyler Holton | 2026-06-25 | 1.0 | 18 |
| Tyler Holton | 2026-06-28 | 1.2 | 21 |
| Will Vest | 2026-06-27 | 1.0 | 26 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Jacob Waguespack, Kenley Jansen, Kyle Finnegan, Tyler Holton


### New York Yankees Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brent Headrick | 2026-06-27 | 1.0 | 17 |
| Camilo Doval | 2026-06-27 | 0.2 | 9 |
| David Bednar | 2026-06-28 | 2.0 | 33 |
| Fernando Cruz | 2026-06-28 | 0.1 | 10 |
| Paul Blackburn | 2026-06-25 | 1.0 | 17 |
| Paul Blackburn | 2026-06-27 | 1.0 | 4 |
| Paul Blackburn | 2026-06-28 | 2.0 | 14 |
| Ryan Yarbrough | 2026-06-25 | 0.2 | 9 |
| Ryan Yarbrough | 2026-06-26 | 1.1 | 22 |
| Tim Hill | 2026-06-25 | 1.0 | 8 |
| Yerry De los Santos | 2026-06-25 | 0.1 | 11 |
| Yerry De los Santos | 2026-06-26 | 1.0 | 16 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** David Bednar, Fernando Cruz, Paul Blackburn



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Kevin Mcgonigle | 380 | 0.277 | 0.417 | 0.140 | 0.364 | 8.6% | 23.6% |
| 2 | Riley Greene | 376 | 0.290 | 0.442 | 0.152 | 0.366 | 12.7% | 30.7% |
| 3 | Spencer Torkelson | 343 | 0.211 | 0.425 | 0.214 | 0.321 | 14.9% | 27.5% |
| 4 | Dillon Dingler | 339 | 0.270 | 0.550 | 0.280 | 0.384 | 12.6% | 29.3% |
| 5 | Colt Keith | 263 | 0.251 | 0.370 | 0.119 | 0.309 | 8.2% | 28.8% |
| 6 | Matt Vierling | 248 | 0.200 | 0.342 | 0.142 | 0.269 | 5.9% | 21.6% |
| 7 | Zach Mckinstry | 218 | 0.188 | 0.281 | 0.094 | 0.282 | 1.9% | 12.3% |
| 8 | Kerry Carpenter | 217 | 0.220 | 0.450 | 0.230 | 0.326 | 10.3% | 28.7% |
| 9 | Gleyber Torres | 200 | 0.289 | 0.410 | 0.120 | 0.367 | 8.4% | 18.5% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cody Bellinger | 368 | 0.253 | 0.429 | 0.176 | 0.347 | 7.2% | 24.9% |
| 2 | Ben Rice | 355 | 0.265 | 0.552 | 0.287 | 0.391 | 13.7% | 31.3% |
| 3 | Jazz Chisholm | 338 | 0.221 | 0.391 | 0.171 | 0.312 | 8.4% | 27.6% |
| 4 | Trent Grisham | 281 | 0.232 | 0.397 | 0.165 | 0.337 | 11.4% | 32.6% |
| 5 | José Caballero | 274 | 0.245 | 0.382 | 0.137 | 0.311 | 4.2% | 16.8% |
| 6 | Aaron Judge | 270 | 0.250 | 0.536 | 0.286 | 0.399 | 21.9% | 31.3% |
| 7 | Paul Goldschmidt | 239 | 0.282 | 0.532 | 0.250 | 0.380 | 11.9% | 24.7% |
| 8 | Ryan Mcmahon | 220 | 0.217 | 0.365 | 0.148 | 0.282 | 12.6% | 26.7% |
| 9 | Austin Wells | 201 | 0.154 | 0.240 | 0.086 | 0.234 | 6.6% | 29.4% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6876 |
| Hits Allowed | 1469 |
| Walks/HBP | 667 |
| Strikeouts | 1537 |
| Home Runs Allowed | 200 |
| K Event Rate | 22.4% |
| BB/HBP Event Rate | 9.7% |
| HR Event Rate | 2.9% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6941 |
| Hits Allowed | 1450 |
| Walks/HBP | 691 |
| Strikeouts | 1628 |
| Home Runs Allowed | 219 |
| K Event Rate | 23.5% |
| BB/HBP Event Rate | 10.0% |
| HR Event Rate | 3.2% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, FS, SL, SI
- Home pitcher pitch mix to inspect: FF, CH, ST, SI, SL
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 4. New York Mets @ Toronto Blue Jays

## Game Context

| Field | Value |
| --- | --- |
| Park | Rogers Centre |
| Time | 2026-06-29T23:07:00Z |
| Away Team | New York Mets |
| Home Team | Toronto Blue Jays |
| Away Probable Pitcher | Sean Manaea |
| Home Probable Pitcher | Trey Yesavage |


## Away Starting Pitcher: Sean Manaea

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1093 |
| Batted/Result Events | 269 |
| Hits Allowed | 61 |
| Walks | 20 |
| Strikeouts | 64 |
| Home Runs | 6 |
| K Event Rate | 23.8% |
| BB Event Rate | 7.4% |
| HR Event Rate | 2.2% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | NYM | 6.3 | 6 | 0 | 2 | 4 | 0 |
| 2026-06-18 | PHI | 7.7 | 6 | 0 | 2 | 5 | 0 |
| 2026-06-13 | NYM | 7.3 | 4 | 1 | 0 | 6 | 1 |
| 2026-06-07 | SD | 5.7 | 4 | 1 | 1 | 3 | 1 |
| 2026-06-01 | SEA | 5.3 | 1 | 1 | 1 | 4 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.3% | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.017 | 0.0% | 0.0% | 33.3% |
| CH | vs R | 4.0% | 44 | 0.143 | 0.286 | 0.143 | 0.179 | 0.534 | 33.3% | 42.9% | 19.0% |
| FC | vs L | 1.9% | 21 | 0.000 | 0.000 | 0.000 | 0.350 | 0.709 | 0.0% | 0.0% | 77.8% |
| FC | vs R | 5.9% | 65 | 0.273 | 0.636 | 0.364 | 0.377 | 0.390 | 11.1% | 14.3% | 21.9% |
| FF | vs L | 8.1% | 89 | 0.316 | 0.526 | 0.211 | 0.384 | 0.356 | 7.7% | 19.4% | 19.0% |
| FF | vs R | 28.3% | 309 | 0.209 | 0.418 | 0.209 | 0.300 | 0.317 | 10.2% | 23.3% | 19.2% |
| SI | vs L | 10.2% | 112 | 0.300 | 0.367 | 0.067 | 0.293 | 0.274 | 0.0% | 24.4% | 6.2% |
| SI | vs R | 8.8% | 96 | 0.385 | 0.462 | 0.077 | 0.476 | 0.371 | 4.5% | 24.3% | 11.1% |
| ST | vs L | 12.2% | 133 | 0.147 | 0.265 | 0.118 | 0.236 | 0.156 | 14.3% | 16.1% | 44.8% |
| ST | vs R | 20.2% | 221 | 0.302 | 0.465 | 0.163 | 0.382 | 0.345 | 5.6% | 21.4% | 24.5% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-24 | 86 | 6 | 2 | 4 | 0 |
| 2026-06-18 | 95 | 6 | 1 | 5 | 0 |
| 2026-06-13 | 84 | 4 | 0 | 6 | 1 |
| 2026-06-07 | 66 | 4 | 1 | 3 | 1 |
| 2026-06-01 | 63 | 1 | 1 | 4 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SI | Davis Schneider | 15 | 0.364 | 0.727 | 0.364 | 0.490 | 0.464 | 33.3% | 35.3% | 9.1% |
| FF | Kazuma Okamoto | 111 | 0.327 | 0.643 | 0.316 | 0.443 | 0.426 | 21.7% | 36.8% | 26.0% |
| FF | Daulton Varsho | 96 | 0.212 | 0.471 | 0.259 | 0.332 | 0.316 | 20.8% | 25.9% | 20.3% |
| FF | George Springer | 80 | 0.273 | 0.530 | 0.258 | 0.402 | 0.354 | 10.9% | 23.6% | 18.3% |
| ST | Andrés Giménez | 22 | 0.238 | 0.476 | 0.238 | 0.318 | 0.282 | 6.2% | 6.5% | 26.7% |
| SI | Yohendrick Pinango | 19 | 0.222 | 0.444 | 0.222 | 0.303 | 0.343 | 13.3% | 50.0% | 7.1% |
| FF | Ernie Clement | 82 | 0.333 | 0.551 | 0.218 | 0.404 | 0.275 | 0.0% | 14.5% | 9.2% |
| ST | Kazuma Okamoto | 37 | 0.206 | 0.412 | 0.206 | 0.296 | 0.247 | 5.9% | 19.4% | 37.1% |
| FF | Andrés Giménez | 87 | 0.263 | 0.463 | 0.200 | 0.334 | 0.247 | 3.2% | 11.8% | 20.1% |
| SI | Kazuma Okamoto | 68 | 0.200 | 0.400 | 0.200 | 0.295 | 0.325 | 10.6% | 33.7% | 26.7% |
| ST | Myles Straw | 6 | 0.167 | 0.333 | 0.167 | 0.208 | 0.091 | 0.0% | 11.1% | 10.0% |
| FF | Jesús Sánchez | 75 | 0.309 | 0.456 | 0.147 | 0.337 | 0.324 | 8.0% | 22.8% | 21.0% |
| ST | Nathan Lukes | 7 | 0.143 | 0.286 | 0.143 | 0.179 | 0.190 | 0.0% | 16.7% | 20.0% |
| ST | George Springer | 35 | 0.133 | 0.267 | 0.133 | 0.270 | 0.232 | 9.1% | 14.3% | 24.2% |
| FF | Vladimir Guerrero | 61 | 0.340 | 0.472 | 0.132 | 0.387 | 0.390 | 8.9% | 27.7% | 15.7% |
| SI | Brandon Valenzuela | 21 | 0.438 | 0.562 | 0.125 | 0.500 | 0.357 | 0.0% | 29.2% | 15.6% |
| SI | Daulton Varsho | 44 | 0.375 | 0.500 | 0.125 | 0.452 | 0.330 | 3.0% | 27.1% | 14.9% |
| SI | Ernie Clement | 71 | 0.358 | 0.478 | 0.119 | 0.385 | 0.308 | 3.1% | 21.0% | 1.9% |
| FF | Myles Straw | 55 | 0.304 | 0.413 | 0.109 | 0.342 | 0.370 | 6.8% | 20.3% | 8.3% |
| FF | Brandon Valenzuela | 62 | 0.204 | 0.296 | 0.093 | 0.260 | 0.316 | 5.0% | 18.9% | 18.0% |
| SI | Vladimir Guerrero | 89 | 0.405 | 0.494 | 0.089 | 0.422 | 0.335 | 5.3% | 33.1% | 6.4% |
| FF | Nathan Lukes | 61 | 0.346 | 0.423 | 0.077 | 0.402 | 0.321 | 0.0% | 15.2% | 15.4% |
| SI | Jesús Sánchez | 31 | 0.296 | 0.370 | 0.074 | 0.323 | 0.240 | 0.0% | 20.0% | 18.0% |
| FF | Davis Schneider | 52 | 0.098 | 0.171 | 0.073 | 0.224 | 0.253 | 8.7% | 25.5% | 34.4% |
| ST | Ernie Clement | 29 | 0.250 | 0.321 | 0.071 | 0.266 | 0.227 | 0.0% | 10.8% | 32.1% |
| ST | Vladimir Guerrero | 35 | 0.258 | 0.323 | 0.065 | 0.266 | 0.386 | 22.2% | 38.5% | 17.6% |
| SI | Myles Straw | 35 | 0.281 | 0.344 | 0.062 | 0.311 | 0.331 | 0.0% | 17.4% | 4.0% |
| SI | Andrés Giménez | 49 | 0.275 | 0.325 | 0.050 | 0.320 | 0.359 | 2.6% | 20.0% | 13.4% |
| SI | George Springer | 55 | 0.163 | 0.204 | 0.041 | 0.236 | 0.282 | 4.7% | 21.7% | 11.4% |
| FF | Yohendrick Pinango | 45 | 0.308 | 0.333 | 0.026 | 0.341 | 0.370 | 6.1% | 19.3% | 16.2% |


## Home Starting Pitcher: Trey Yesavage

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 988 |
| Batted/Result Events | 249 |
| Hits Allowed | 41 |
| Walks | 30 |
| Strikeouts | 58 |
| Home Runs | 5 |
| K Event Rate | 23.3% |
| BB Event Rate | 12.0% |
| HR Event Rate | 2.0% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | TOR | 8.3 | 2 | 0 | 5 | 5 | 0 |
| 2026-06-18 | BOS | 8.7 | 4 | 2 | 0 | 6 | 2 |
| 2026-06-12 | TOR | 8.3 | 4 | 1 | 6 | 3 | 1 |
| 2026-06-05 | TOR | 8.0 | 5 | 2 | 2 | 5 | 2 |
| 2026-05-30 | BAL | 7.0 | 2 | 0 | 7 | 4 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF | vs L | 24.0% | 237 | 0.275 | 0.451 | 0.176 | 0.368 | 0.306 | 2.4% | 26.9% | 15.2% |
| FF | vs R | 21.4% | 211 | 0.120 | 0.280 | 0.160 | 0.243 | 0.230 | 2.5% | 18.8% | 15.0% |
| FS | vs L | 21.7% | 214 | 0.135 | 0.231 | 0.096 | 0.212 | 0.287 | 7.9% | 17.3% | 43.2% |
| FS | vs R | 8.2% | 81 | 0.091 | 0.091 | 0.000 | 0.123 | 0.127 | 0.0% | 27.3% | 32.4% |
| SL | vs L | 6.0% | 59 | 0.154 | 0.231 | 0.077 | 0.237 | 0.291 | 0.0% | 23.8% | 27.0% |
| SL | vs R | 18.8% | 186 | 0.297 | 0.541 | 0.243 | 0.398 | 0.279 | 7.7% | 23.1% | 38.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-24 | 105 | 2 | 5 | 5 | 0 |
| 2026-06-18 | 95 | 4 | 0 | 6 | 2 |
| 2026-06-12 | 81 | 4 | 6 | 3 | 1 |
| 2026-06-05 | 91 | 5 | 2 | 5 | 2 |
| 2026-05-30 | 92 | 2 | 7 | 4 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FS | Jared Young | 5 | 0.600 | 1.200 | 0.600 | 0.760 | 0.445 | 25.0% | 20.0% | 28.6% |
| FS | Francisco Álvarez | 5 | 0.200 | 0.800 | 0.600 | 0.540 | 0.581 | 33.3% | 40.0% | 41.7% |
| FF | Juan Soto | 76 | 0.309 | 0.662 | 0.353 | 0.438 | 0.493 | 22.8% | 34.1% | 15.0% |
| FS | Carson Benge | 14 | 0.214 | 0.500 | 0.286 | 0.296 | 0.296 | 10.0% | 35.3% | 32.0% |
| SL | Mark Vientos | 37 | 0.200 | 0.486 | 0.286 | 0.307 | 0.370 | 27.3% | 32.5% | 43.1% |
| SL | Bo Bichette | 61 | 0.351 | 0.596 | 0.246 | 0.400 | 0.374 | 12.5% | 32.5% | 20.0% |
| SL | Francisco Álvarez | 38 | 0.263 | 0.500 | 0.237 | 0.346 | 0.347 | 18.8% | 32.7% | 35.0% |
| SL | Jared Young | 14 | 0.154 | 0.385 | 0.231 | 0.257 | 0.269 | 20.0% | 23.5% | 41.2% |
| FF | Mj Melendez | 58 | 0.184 | 0.408 | 0.224 | 0.309 | 0.243 | 6.9% | 24.0% | 32.6% |
| FS | Francisco Lindor | 9 | 0.222 | 0.444 | 0.222 | 0.278 | 0.207 | 0.0% | 16.7% | 23.5% |
| FF | A. J. Ewing | 50 | 0.220 | 0.439 | 0.220 | 0.357 | 0.422 | 15.2% | 25.3% | 9.2% |
| SL | Juan Soto | 39 | 0.188 | 0.375 | 0.188 | 0.321 | 0.403 | 12.0% | 35.7% | 25.9% |
| FF | Francisco Lindor | 50 | 0.186 | 0.372 | 0.186 | 0.318 | 0.386 | 7.9% | 27.8% | 12.5% |
| FF | Francisco Álvarez | 46 | 0.293 | 0.463 | 0.171 | 0.366 | 0.382 | 21.7% | 26.9% | 27.4% |
| FF | Marcus Semien | 90 | 0.205 | 0.372 | 0.167 | 0.291 | 0.353 | 14.3% | 29.1% | 17.6% |
| FF | Mark Vientos | 60 | 0.236 | 0.400 | 0.164 | 0.312 | 0.331 | 11.9% | 23.9% | 25.2% |
| FF | Carson Benge | 119 | 0.295 | 0.457 | 0.162 | 0.376 | 0.370 | 7.6% | 21.7% | 17.5% |
| FF | Bo Bichette | 92 | 0.222 | 0.383 | 0.160 | 0.311 | 0.333 | 5.2% | 26.0% | 12.1% |
| SL | Mj Melendez | 17 | 0.231 | 0.385 | 0.154 | 0.365 | 0.292 | 0.0% | 25.0% | 30.0% |
| FF | Jared Young | 39 | 0.235 | 0.382 | 0.147 | 0.321 | 0.398 | 18.5% | 20.3% | 16.7% |
| FS | Mj Melendez | 8 | 0.286 | 0.429 | 0.143 | 0.356 | 0.316 | 20.0% | 66.7% | 27.3% |
| SL | Carson Benge | 41 | 0.211 | 0.342 | 0.132 | 0.271 | 0.344 | 10.7% | 26.5% | 21.2% |
| FS | Marcus Semien | 10 | 0.222 | 0.333 | 0.111 | 0.465 | 0.253 | 0.0% | 8.3% | 17.6% |
| FF | Brett Baty | 104 | 0.215 | 0.312 | 0.097 | 0.288 | 0.292 | 12.7% | 22.6% | 19.9% |
| FS | Mark Vientos | 12 | 0.091 | 0.182 | 0.091 | 0.163 | 0.264 | 14.3% | 20.0% | 50.0% |
| SL | Marcus Semien | 67 | 0.111 | 0.175 | 0.063 | 0.174 | 0.186 | 0.0% | 19.4% | 33.3% |
| FF | Luis Torrens | 36 | 0.250 | 0.312 | 0.062 | 0.297 | 0.330 | 4.5% | 24.3% | 18.8% |
| FS | Brett Baty | 16 | 0.062 | 0.125 | 0.062 | 0.078 | 0.114 | 0.0% | 0.0% | 48.6% |
| SL | Luis Torrens | 24 | 0.143 | 0.190 | 0.048 | 0.194 | 0.195 | 9.1% | 15.8% | 47.5% |
| SL | Brett Baty | 32 | 0.154 | 0.192 | 0.038 | 0.255 | 0.291 | 5.6% | 19.4% | 34.5% |


## New York Mets Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bo Bichette | 385 | 0.267 | 0.412 | 0.145 | 0.323 | 0.332 | 7.0% | 27.0% | 16.7% |
| Carson Benge | 344 | 0.261 | 0.395 | 0.134 | 0.333 | 0.343 | 8.0% | 24.0% | 19.6% |
| Marcus Semien | 338 | 0.217 | 0.352 | 0.135 | 0.285 | 0.316 | 8.9% | 21.9% | 21.3% |
| Brett Baty | 294 | 0.212 | 0.293 | 0.081 | 0.281 | 0.295 | 8.9% | 21.5% | 26.9% |
| Juan Soto | 286 | 0.293 | 0.550 | 0.256 | 0.404 | 0.427 | 14.8% | 33.7% | 17.9% |
| Mark Vientos | 256 | 0.204 | 0.379 | 0.175 | 0.274 | 0.310 | 10.4% | 27.0% | 29.9% |
| Francisco Álvarez | 204 | 0.250 | 0.424 | 0.174 | 0.337 | 0.339 | 15.2% | 28.8% | 28.8% |
| A. J. Ewing | 169 | 0.277 | 0.419 | 0.142 | 0.348 | 0.352 | 6.5% | 21.6% | 21.9% |
| Luis Torrens | 159 | 0.219 | 0.301 | 0.082 | 0.259 | 0.271 | 3.6% | 22.7% | 21.3% |
| Mj Melendez | 145 | 0.190 | 0.347 | 0.157 | 0.298 | 0.281 | 11.1% | 28.4% | 30.8% |
| Francisco Lindor | 138 | 0.210 | 0.323 | 0.113 | 0.296 | 0.336 | 6.9% | 25.9% | 21.0% |
| Jared Young | 128 | 0.217 | 0.409 | 0.191 | 0.318 | 0.342 | 15.1% | 25.9% | 23.6% |


## Toronto Blue Jays Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Vladimir Guerrero | 350 | 0.275 | 0.367 | 0.092 | 0.328 | 0.346 | 7.4% | 30.7% | 17.4% |
| Kazuma Okamoto | 349 | 0.240 | 0.464 | 0.224 | 0.344 | 0.329 | 14.5% | 28.7% | 32.2% |
| Ernie Clement | 333 | 0.293 | 0.430 | 0.137 | 0.328 | 0.269 | 2.4% | 16.9% | 15.0% |
| Andrés Giménez | 293 | 0.249 | 0.398 | 0.149 | 0.302 | 0.269 | 4.1% | 13.8% | 22.4% |
| George Springer | 290 | 0.239 | 0.420 | 0.180 | 0.345 | 0.308 | 9.0% | 22.6% | 21.2% |
| Daulton Varsho | 287 | 0.256 | 0.426 | 0.171 | 0.344 | 0.305 | 8.0% | 23.9% | 18.8% |
| Jesús Sánchez | 251 | 0.283 | 0.452 | 0.170 | 0.339 | 0.335 | 10.7% | 27.1% | 23.6% |
| Nathan Lukes | 186 | 0.320 | 0.438 | 0.118 | 0.367 | 0.304 | 1.4% | 16.1% | 16.6% |
| Brandon Valenzuela | 171 | 0.247 | 0.427 | 0.180 | 0.331 | 0.334 | 8.3% | 22.3% | 24.4% |
| Myles Straw | 156 | 0.237 | 0.324 | 0.086 | 0.283 | 0.304 | 3.3% | 17.2% | 11.4% |
| Yohendrick Pinango | 145 | 0.281 | 0.452 | 0.170 | 0.348 | 0.319 | 8.8% | 27.5% | 21.8% |
| Davis Schneider | 131 | 0.156 | 0.284 | 0.128 | 0.258 | 0.270 | 10.4% | 28.4% | 27.6% |


## Bullpen Fatigue Report

### New York Mets Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| A.J. Minter | 2026-06-27 | 1.2 | 22 |
| Austin Warren | 2026-06-25 | 1.1 | 25 |
| Brooks Raley | 2026-06-25 | 1.0 | 17 |
| Cionel Pérez | 2026-06-26 | 2.0 | 21 |
| Devin Williams | 2026-06-25 | 1.0 | 12 |
| Devin Williams | 2026-06-27 | 1.0 | 14 |
| Huascar Brazobán | 2026-06-26 | 1.0 | 18 |
| Huascar Brazobán | 2026-06-27 | 1.0 | 10 |
| Kodai Senga | 2026-06-28 | 5.0 | 80 |
| Luke Weaver | 2026-06-25 | 1.0 | 11 |
| Luke Weaver | 2026-06-27 | 1.0 | 15 |
| Tobias Myers | 2026-06-28 | 3.0 | 59 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Kodai Senga, Tobias Myers


### Toronto Blue Jays Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Adam Macko | 2026-06-26 | 1.0 | 31 |
| Adam Macko | 2026-06-28 | 1.1 | 25 |
| Braydon Fisher | 2026-06-27 | 1.0 | 12 |
| Jeff Hoffman | 2026-06-27 | 1.0 | 20 |
| Jeff Hoffman | 2026-06-28 | 1.1 | 24 |
| Louis Varland | 2026-06-26 | 1.0 | 10 |
| Louis Varland | 2026-06-28 | 1.0 | 23 |
| Mason Fluharty | 2026-06-27 | 0.1 | 14 |
| Simeon Woods Richardson | 2026-06-25 | 3.0 | 43 |
| Spencer Miles | 2026-06-26 | 2.2 | 35 |
| Tommy Nance | 2026-06-27 | 1.0 | 11 |
| Tyler Rogers | 2026-06-27 | 1.0 | 22 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Adam Macko, Jeff Hoffman, Louis Varland



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bo Bichette | 385 | 0.267 | 0.412 | 0.145 | 0.323 | 7.0% | 27.0% |
| 2 | Carson Benge | 344 | 0.261 | 0.395 | 0.134 | 0.333 | 8.0% | 24.0% |
| 3 | Marcus Semien | 338 | 0.217 | 0.352 | 0.135 | 0.285 | 8.9% | 21.9% |
| 4 | Brett Baty | 294 | 0.212 | 0.293 | 0.081 | 0.281 | 8.9% | 21.5% |
| 5 | Juan Soto | 286 | 0.293 | 0.550 | 0.256 | 0.404 | 14.8% | 33.7% |
| 6 | Mark Vientos | 256 | 0.204 | 0.379 | 0.175 | 0.274 | 10.4% | 27.0% |
| 7 | Francisco Álvarez | 204 | 0.250 | 0.424 | 0.174 | 0.337 | 15.2% | 28.8% |
| 8 | A. J. Ewing | 169 | 0.277 | 0.419 | 0.142 | 0.348 | 6.5% | 21.6% |
| 9 | Luis Torrens | 159 | 0.219 | 0.301 | 0.082 | 0.259 | 3.6% | 22.7% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Vladimir Guerrero | 350 | 0.275 | 0.367 | 0.092 | 0.328 | 7.4% | 30.7% |
| 2 | Kazuma Okamoto | 349 | 0.240 | 0.464 | 0.224 | 0.344 | 14.5% | 28.7% |
| 3 | Ernie Clement | 333 | 0.293 | 0.430 | 0.137 | 0.328 | 2.4% | 16.9% |
| 4 | Andrés Giménez | 293 | 0.249 | 0.398 | 0.149 | 0.302 | 4.1% | 13.8% |
| 5 | George Springer | 290 | 0.239 | 0.420 | 0.180 | 0.345 | 9.0% | 22.6% |
| 6 | Daulton Varsho | 287 | 0.256 | 0.426 | 0.171 | 0.344 | 8.0% | 23.9% |
| 7 | Jesús Sánchez | 251 | 0.283 | 0.452 | 0.170 | 0.339 | 10.7% | 27.1% |
| 8 | Nathan Lukes | 186 | 0.320 | 0.438 | 0.118 | 0.367 | 1.4% | 16.1% |
| 9 | Brandon Valenzuela | 171 | 0.247 | 0.427 | 0.180 | 0.331 | 8.3% | 22.3% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6939 |
| Hits Allowed | 1441 |
| Walks/HBP | 660 |
| Strikeouts | 1607 |
| Home Runs Allowed | 189 |
| K Event Rate | 23.2% |
| BB/HBP Event Rate | 9.5% |
| HR Event Rate | 2.7% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6815 |
| Hits Allowed | 1502 |
| Walks/HBP | 615 |
| Strikeouts | 1461 |
| Home Runs Allowed | 195 |
| K Event Rate | 21.4% |
| BB/HBP Event Rate | 9.0% |
| HR Event Rate | 2.9% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, ST, SI
- Home pitcher pitch mix to inspect: FF, FS, SL
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 5. Washington Nationals @ Boston Red Sox

## Game Context

| Field | Value |
| --- | --- |
| Park | Fenway Park |
| Time | 2026-06-29T23:10:00Z |
| Away Team | Washington Nationals |
| Home Team | Boston Red Sox |
| Away Probable Pitcher | Miles Mikolas |
| Home Probable Pitcher | Ranger Suarez |


## Away Starting Pitcher: Miles Mikolas

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1300 |
| Batted/Result Events | 350 |
| Hits Allowed | 88 |
| Walks | 20 |
| Strikeouts | 45 |
| Home Runs | 17 |
| K Event Rate | 12.9% |
| BB Event Rate | 5.7% |
| HR Event Rate | 4.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | WSH | 5.3 | 5 | 0 | 0 | 1 | 0 |
| 2026-06-19 | TB | 8.7 | 9 | 2 | 1 | 2 | 2 |
| 2026-06-14 | WSH | 7.7 | 3 | 0 | 0 | 3 | 0 |
| 2026-06-08 | SF | 5.7 | 3 | 0 | 0 | 2 | 0 |
| 2026-06-02 | WSH | 8.3 | 6 | 3 | 2 | 4 | 3 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 8.2% | 107 | 0.375 | 0.792 | 0.417 | 0.534 | 0.419 | 8.3% | 32.4% | 13.3% |
| CH | vs R | 0.6% | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.132 | 0.0% | 0.0% | 0.0% |
| CU | vs L | 10.4% | 135 | 0.316 | 0.316 | 0.000 | 0.367 | 0.341 | 6.2% | 23.1% | 21.2% |
| CU | vs R | 4.2% | 54 | 0.444 | 0.556 | 0.111 | 0.423 | 0.314 | 0.0% | 42.9% | 11.8% |
| FF | vs L | 15.8% | 205 | 0.226 | 0.415 | 0.189 | 0.331 | 0.321 | 11.6% | 25.9% | 14.4% |
| FF | vs R | 9.0% | 117 | 0.385 | 0.577 | 0.192 | 0.436 | 0.365 | 18.2% | 23.5% | 12.5% |
| SI | vs L | 11.4% | 148 | 0.283 | 0.434 | 0.151 | 0.317 | 0.363 | 9.1% | 24.7% | 6.9% |
| SI | vs R | 13.2% | 172 | 0.245 | 0.528 | 0.283 | 0.325 | 0.313 | 10.6% | 25.6% | 7.1% |
| SL | vs L | 11.3% | 147 | 0.233 | 0.400 | 0.167 | 0.321 | 0.297 | 7.1% | 31.4% | 16.2% |
| SL | vs R | 9.2% | 120 | 0.176 | 0.324 | 0.147 | 0.244 | 0.280 | 6.5% | 29.3% | 19.6% |
| ST | vs L | 1.1% | 14 | 0.250 | 0.250 | 0.000 | 0.225 | 0.325 | 0.0% | 16.7% | 14.3% |
| ST | vs R | 5.6% | 73 | 0.312 | 0.688 | 0.375 | 0.435 | 0.443 | 8.3% | 28.6% | 13.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-24 | 60 | 5 | 0 | 1 | 0 |
| 2026-06-19 | 85 | 9 | 1 | 2 | 2 |
| 2026-06-14 | 83 | 3 | 0 | 3 | 0 |
| 2026-06-08 | 54 | 3 | 0 | 2 | 0 |
| 2026-06-02 | 92 | 6 | 2 | 4 | 3 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SI | Willson Contreras | 87 | 0.389 | 0.792 | 0.403 | 0.524 | 0.498 | 12.3% | 34.4% | 10.1% |
| CU | Carlos Narváez | 4 | 0.667 | 1.000 | 0.333 | 0.588 | 0.830 | 33.3% | 20.0% | 23.1% |
| CH | Ceddanne Rafaela | 36 | 0.294 | 0.559 | 0.265 | 0.404 | 0.232 | 11.5% | 23.3% | 28.8% |
| FF | Jarren Duran | 101 | 0.184 | 0.437 | 0.253 | 0.312 | 0.323 | 14.8% | 18.6% | 32.4% |
| SI | Trevor Story | 33 | 0.345 | 0.586 | 0.241 | 0.441 | 0.427 | 8.0% | 30.4% | 12.7% |
| CH | Willson Contreras | 43 | 0.310 | 0.548 | 0.238 | 0.372 | 0.309 | 20.0% | 32.6% | 42.2% |
| SL | Roman Anthony | 20 | 0.294 | 0.529 | 0.235 | 0.403 | 0.419 | 15.4% | 35.0% | 25.0% |
| SL | Ceddanne Rafaela | 46 | 0.302 | 0.535 | 0.233 | 0.407 | 0.268 | 2.7% | 23.8% | 28.9% |
| SL | Willson Contreras | 44 | 0.282 | 0.513 | 0.231 | 0.460 | 0.412 | 20.8% | 28.6% | 41.2% |
| FF | Wilyer Abreu | 103 | 0.230 | 0.460 | 0.230 | 0.354 | 0.321 | 13.3% | 19.5% | 20.7% |
| FF | Caleb Durbin | 82 | 0.292 | 0.514 | 0.222 | 0.388 | 0.316 | 5.1% | 24.8% | 7.7% |
| CH | Masataka Yoshida | 27 | 0.304 | 0.522 | 0.217 | 0.404 | 0.408 | 5.3% | 29.0% | 20.0% |
| CH | Andruw Monasterio | 14 | 0.214 | 0.429 | 0.214 | 0.271 | 0.352 | 18.2% | 26.9% | 27.5% |
| FF | Andruw Monasterio | 45 | 0.225 | 0.425 | 0.200 | 0.321 | 0.297 | 7.7% | 13.9% | 18.2% |
| SI | Marcelo Mayer | 36 | 0.314 | 0.514 | 0.200 | 0.364 | 0.246 | 3.1% | 25.6% | 9.6% |
| SL | Masataka Yoshida | 11 | 0.300 | 0.500 | 0.200 | 0.373 | 0.317 | 0.0% | 31.2% | 21.7% |
| SL | Wilyer Abreu | 49 | 0.267 | 0.467 | 0.200 | 0.344 | 0.352 | 15.2% | 26.3% | 33.0% |
| SI | Jarren Duran | 40 | 0.378 | 0.568 | 0.189 | 0.430 | 0.467 | 16.1% | 33.3% | 18.9% |
| CU | Trevor Story | 18 | 0.118 | 0.294 | 0.176 | 0.250 | 0.255 | 25.0% | 18.8% | 41.4% |
| CU | Wilyer Abreu | 22 | 0.222 | 0.389 | 0.167 | 0.341 | 0.325 | 6.2% | 15.4% | 9.7% |
| CH | Jarren Duran | 46 | 0.163 | 0.326 | 0.163 | 0.223 | 0.260 | 12.1% | 26.5% | 35.0% |
| CU | Ceddanne Rafaela | 19 | 0.211 | 0.368 | 0.158 | 0.292 | 0.169 | 0.0% | 13.8% | 31.0% |
| SL | Isiah Kiner-Falefa | 23 | 0.476 | 0.619 | 0.143 | 0.500 | 0.454 | 5.6% | 20.7% | 23.4% |
| CU | Andruw Monasterio | 8 | 0.286 | 0.429 | 0.143 | 0.356 | 0.229 | 16.7% | 9.1% | 15.4% |
| SI | Wilyer Abreu | 58 | 0.321 | 0.453 | 0.132 | 0.359 | 0.386 | 10.0% | 20.5% | 11.7% |
| SI | Andruw Monasterio | 24 | 0.292 | 0.417 | 0.125 | 0.344 | 0.327 | 5.0% | 29.3% | 6.4% |
| CH | Caleb Durbin | 28 | 0.120 | 0.240 | 0.120 | 0.184 | 0.253 | 5.3% | 22.2% | 40.4% |
| FF | Trevor Story | 47 | 0.250 | 0.364 | 0.114 | 0.293 | 0.244 | 3.8% | 19.0% | 25.6% |
| FF | Masataka Yoshida | 73 | 0.317 | 0.429 | 0.111 | 0.367 | 0.334 | 3.3% | 29.8% | 5.0% |
| SL | Marcelo Mayer | 34 | 0.222 | 0.333 | 0.111 | 0.315 | 0.267 | 5.0% | 48.3% | 30.2% |


## Home Starting Pitcher: Ranger Suarez

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1369 |
| Batted/Result Events | 360 |
| Hits Allowed | 78 |
| Walks | 26 |
| Strikeouts | 88 |
| Home Runs | 6 |
| K Event Rate | 24.4% |
| BB Event Rate | 7.2% |
| HR Event Rate | 1.7% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | COL | 9.0 | 7 | 0 | 1 | 9 | 0 |
| 2026-06-19 | SEA | 8.0 | 1 | 0 | 3 | 5 | 0 |
| 2026-06-13 | BOS | 7.7 | 6 | 0 | 2 | 7 | 0 |
| 2026-06-07 | NYY | 8.3 | 6 | 0 | 0 | 6 | 0 |
| 2026-05-31 | CLE | 8.3 | 8 | 0 | 3 | 10 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 1.9% | 26 | 0.250 | 0.250 | 0.000 | 0.225 | 0.325 | 0.0% | 28.6% | 27.3% |
| CH | vs R | 13.1% | 180 | 0.239 | 0.435 | 0.196 | 0.310 | 0.288 | 5.4% | 15.0% | 28.9% |
| CU | vs L | 4.5% | 61 | 0.059 | 0.118 | 0.059 | 0.139 | 0.120 | 0.0% | 11.8% | 43.8% |
| CU | vs R | 11.5% | 158 | 0.263 | 0.368 | 0.105 | 0.315 | 0.251 | 10.5% | 23.5% | 41.8% |
| FC | vs L | 0.8% | 11 | 0.500 | 2.000 | 1.500 | 1.000 | 1.676 | 50.0% | 25.0% | 0.0% |
| FC | vs R | 20.0% | 274 | 0.227 | 0.333 | 0.106 | 0.292 | 0.270 | 3.4% | 19.0% | 16.7% |
| FF | vs L | 6.9% | 95 | 0.357 | 0.429 | 0.071 | 0.409 | 0.433 | 10.0% | 19.2% | 25.6% |
| FF | vs R | 14.5% | 199 | 0.167 | 0.250 | 0.083 | 0.208 | 0.230 | 14.8% | 16.9% | 12.2% |
| SI | vs L | 10.4% | 143 | 0.302 | 0.442 | 0.140 | 0.331 | 0.272 | 5.9% | 18.3% | 15.4% |
| SI | vs R | 14.0% | 191 | 0.241 | 0.259 | 0.019 | 0.280 | 0.346 | 0.0% | 30.6% | 9.7% |
| SL | vs L | 1.9% | 26 | 0.250 | 0.375 | 0.125 | 0.269 | 0.260 | 0.0% | 14.3% | 33.3% |
| SL | vs R | 0.2% | 3 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 100.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-24 | 102 | 7 | 1 | 9 | 0 |
| 2026-06-19 | 94 | 1 | 3 | 5 | 0 |
| 2026-06-13 | 97 | 6 | 2 | 7 | 0 |
| 2026-06-07 | 90 | 6 | 0 | 6 | 0 |
| 2026-05-31 | 93 | 8 | 2 | 10 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Keibert Ruiz | 9 | 0.429 | 1.143 | 0.714 | 0.578 | 0.440 | 33.3% | 27.3% | 4.3% |
| FC | Cj Abrams | 29 | 0.440 | 1.120 | 0.680 | 0.659 | 0.399 | 13.0% | 28.2% | 21.6% |
| CU | Curtis Mead | 14 | 0.455 | 0.909 | 0.455 | 0.600 | 0.394 | 12.5% | 40.0% | 15.0% |
| FC | Curtis Mead | 23 | 0.211 | 0.579 | 0.368 | 0.389 | 0.408 | 12.5% | 28.6% | 20.0% |
| FC | James Wood | 28 | 0.269 | 0.615 | 0.346 | 0.368 | 0.472 | 25.0% | 36.4% | 27.7% |
| FC | José Tena | 9 | 0.222 | 0.556 | 0.333 | 0.417 | 0.412 | 0.0% | 33.3% | 28.0% |
| SI | Curtis Mead | 48 | 0.190 | 0.500 | 0.310 | 0.336 | 0.419 | 17.1% | 30.0% | 11.5% |
| SI | Luis García | 44 | 0.300 | 0.600 | 0.300 | 0.408 | 0.381 | 11.1% | 35.9% | 2.9% |
| FF | James Wood | 110 | 0.326 | 0.620 | 0.293 | 0.449 | 0.481 | 23.8% | 35.4% | 17.1% |
| CH | Luis García | 54 | 0.259 | 0.537 | 0.278 | 0.334 | 0.308 | 11.4% | 22.5% | 22.9% |
| FF | Luis García | 70 | 0.277 | 0.554 | 0.277 | 0.400 | 0.410 | 14.0% | 26.2% | 10.0% |
| FF | Brady House | 53 | 0.224 | 0.490 | 0.265 | 0.345 | 0.343 | 23.1% | 28.8% | 35.8% |
| CH | Keibert Ruiz | 34 | 0.294 | 0.559 | 0.265 | 0.360 | 0.224 | 3.7% | 32.6% | 26.7% |
| SI | José Tena | 23 | 0.316 | 0.579 | 0.263 | 0.435 | 0.338 | 13.3% | 23.5% | 11.1% |
| FC | Dylan Crews | 13 | 0.250 | 0.500 | 0.250 | 0.346 | 0.316 | 10.0% | 10.5% | 30.0% |
| CU | Jacob Young | 13 | 0.250 | 0.500 | 0.250 | 0.346 | 0.274 | 12.5% | 30.8% | 30.0% |
| FF | Keibert Ruiz | 60 | 0.273 | 0.509 | 0.236 | 0.362 | 0.305 | 5.7% | 26.4% | 5.1% |
| FF | Cj Abrams | 91 | 0.342 | 0.575 | 0.233 | 0.455 | 0.418 | 12.1% | 20.3% | 23.0% |
| FF | Jacob Young | 78 | 0.232 | 0.464 | 0.232 | 0.363 | 0.343 | 7.4% | 24.5% | 12.2% |
| CU | Luis García | 22 | 0.227 | 0.455 | 0.227 | 0.286 | 0.276 | 7.7% | 39.1% | 27.5% |
| FF | Dylan Crews | 38 | 0.222 | 0.444 | 0.222 | 0.303 | 0.321 | 10.3% | 27.4% | 22.6% |
| FF | José Tena | 52 | 0.217 | 0.435 | 0.217 | 0.340 | 0.346 | 8.6% | 23.1% | 22.6% |
| SI | Daylen Lile | 50 | 0.349 | 0.558 | 0.209 | 0.437 | 0.456 | 4.8% | 24.6% | 10.2% |
| FF | Daylen Lile | 99 | 0.259 | 0.459 | 0.200 | 0.346 | 0.340 | 10.0% | 18.8% | 21.6% |
| FC | Jacob Young | 15 | 0.267 | 0.467 | 0.200 | 0.313 | 0.410 | 18.2% | 20.8% | 21.2% |
| CH | Cj Abrams | 47 | 0.178 | 0.378 | 0.200 | 0.253 | 0.295 | 9.1% | 27.4% | 29.6% |
| SI | James Wood | 70 | 0.304 | 0.500 | 0.196 | 0.415 | 0.479 | 18.2% | 41.8% | 14.3% |
| FC | Luis García | 17 | 0.294 | 0.471 | 0.176 | 0.329 | 0.299 | 6.2% | 31.4% | 9.3% |
| CH | Jacob Young | 27 | 0.167 | 0.333 | 0.167 | 0.246 | 0.293 | 4.5% | 19.4% | 28.3% |
| SI | Cj Abrams | 47 | 0.295 | 0.455 | 0.159 | 0.347 | 0.372 | 10.8% | 31.7% | 13.1% |


## Washington Nationals Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| James Wood | 423 | 0.250 | 0.489 | 0.239 | 0.372 | 0.415 | 22.3% | 35.6% | 30.9% |
| Daylen Lile | 381 | 0.247 | 0.397 | 0.149 | 0.312 | 0.312 | 6.6% | 22.0% | 20.6% |
| Cj Abrams | 366 | 0.277 | 0.505 | 0.227 | 0.380 | 0.340 | 9.4% | 27.1% | 26.2% |
| Nasim Nuñez | 294 | 0.234 | 0.274 | 0.040 | 0.289 | 0.269 | 0.0% | 11.5% | 21.0% |
| Luis García | 292 | 0.268 | 0.511 | 0.243 | 0.351 | 0.352 | 10.9% | 29.2% | 16.9% |
| Jacob Young | 282 | 0.218 | 0.359 | 0.141 | 0.296 | 0.299 | 6.2% | 24.3% | 18.8% |
| Curtis Mead | 249 | 0.220 | 0.463 | 0.243 | 0.345 | 0.358 | 11.2% | 26.2% | 15.4% |
| Keibert Ruiz | 200 | 0.266 | 0.441 | 0.176 | 0.319 | 0.272 | 4.9% | 27.4% | 12.7% |
| Brady House | 193 | 0.242 | 0.404 | 0.163 | 0.315 | 0.319 | 9.5% | 28.9% | 30.2% |
| Jorbit Vivas | 180 | 0.255 | 0.357 | 0.102 | 0.336 | 0.305 | 4.4% | 18.2% | 16.2% |
| José Tena | 176 | 0.213 | 0.348 | 0.134 | 0.282 | 0.292 | 8.3% | 28.6% | 30.8% |
| Dylan Crews | 150 | 0.213 | 0.355 | 0.142 | 0.276 | 0.327 | 9.4% | 28.7% | 28.6% |


## Boston Red Sox Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wilyer Abreu | 360 | 0.261 | 0.432 | 0.171 | 0.333 | 0.339 | 11.9% | 23.6% | 20.5% |
| Jarren Duran | 354 | 0.201 | 0.353 | 0.152 | 0.275 | 0.289 | 11.1% | 25.6% | 32.7% |
| Willson Contreras | 349 | 0.277 | 0.510 | 0.233 | 0.391 | 0.376 | 13.3% | 29.3% | 29.6% |
| Ceddanne Rafaela | 333 | 0.289 | 0.451 | 0.162 | 0.356 | 0.287 | 5.4% | 21.4% | 23.1% |
| Caleb Durbin | 289 | 0.238 | 0.381 | 0.143 | 0.302 | 0.280 | 2.7% | 20.9% | 15.4% |
| Marcelo Mayer | 248 | 0.215 | 0.305 | 0.090 | 0.279 | 0.259 | 6.8% | 27.0% | 24.0% |
| Masataka Yoshida | 196 | 0.247 | 0.356 | 0.109 | 0.311 | 0.310 | 2.0% | 28.0% | 15.4% |
| Trevor Story | 194 | 0.225 | 0.335 | 0.110 | 0.286 | 0.248 | 4.0% | 22.1% | 27.8% |
| Carlos Narváez | 168 | 0.193 | 0.273 | 0.080 | 0.266 | 0.284 | 8.1% | 20.3% | 29.1% |
| Isiah Kiner-Falefa | 151 | 0.255 | 0.328 | 0.073 | 0.300 | 0.312 | 3.4% | 17.1% | 14.8% |
| Andruw Monasterio | 147 | 0.223 | 0.360 | 0.137 | 0.280 | 0.278 | 6.8% | 18.2% | 17.3% |
| Roman Anthony | 145 | 0.240 | 0.322 | 0.083 | 0.318 | 0.352 | 9.6% | 31.2% | 26.6% |


## Bullpen Fatigue Report

### Washington Nationals Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brad Lord | 2026-06-26 | 2.2 | 59 |
| Clayton Beeter | 2026-06-25 | 0.2 | 18 |
| Clayton Beeter | 2026-06-27 | 1.0 | 20 |
| Gus Varland | 2026-06-25 | 2.0 | 28 |
| Justin Lawrence | 2026-06-27 | 1.0 | 15 |
| Mitchell Parker | 2026-06-25 | 0.1 | 18 |
| Mitchell Parker | 2026-06-28 | 1.2 | 29 |
| Orlando Ribalta | 2026-06-27 | 0.1 | 12 |
| PJ Poulin | 2026-06-27 | 0.2 | 11 |
| PJ Poulin | 2026-06-28 | 2.0 | 25 |
| Richard Lovelady | 2026-06-28 | 0.1 | 6 |
| Zak Kent | 2026-06-26 | 1.0 | 24 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Mitchell Parker, PJ Poulin, Richard Lovelady


### Boston Red Sox Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Aroldis Chapman | 2026-06-25 | 1.0 | 23 |
| Aroldis Chapman | 2026-06-27 | 1.0 | 20 |
| Aroldis Chapman | 2026-06-28 | 1.0 | 23 |
| Danny Coulombe | 2026-06-25 | 0.1 | 3 |
| Garrett Whitlock | 2026-06-25 | 1.0 | 10 |
| Garrett Whitlock | 2026-06-27 | 1.0 | 7 |
| Greg Weissert | 2026-06-25 | 0.2 | 21 |
| Justin Slaten | 2026-06-27 | 0.2 | 12 |
| Justin Slaten | 2026-06-28 | 1.0 | 16 |
| Ryan Watson | 2026-06-26 | 1.0 | 13 |
| Tommy Kahnle | 2026-06-26 | 1.0 | 21 |
| Tyron Guerrero | 2026-06-28 | 0.2 | 9 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Aroldis Chapman, Justin Slaten, Tyron Guerrero



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | James Wood | 423 | 0.250 | 0.489 | 0.239 | 0.372 | 22.3% | 35.6% |
| 2 | Daylen Lile | 381 | 0.247 | 0.397 | 0.149 | 0.312 | 6.6% | 22.0% |
| 3 | Cj Abrams | 366 | 0.277 | 0.505 | 0.227 | 0.380 | 9.4% | 27.1% |
| 4 | Nasim Nuñez | 294 | 0.234 | 0.274 | 0.040 | 0.289 | 0.0% | 11.5% |
| 5 | Luis García | 292 | 0.268 | 0.511 | 0.243 | 0.351 | 10.9% | 29.2% |
| 6 | Jacob Young | 282 | 0.218 | 0.359 | 0.141 | 0.296 | 6.2% | 24.3% |
| 7 | Curtis Mead | 249 | 0.220 | 0.463 | 0.243 | 0.345 | 11.2% | 26.2% |
| 8 | Keibert Ruiz | 200 | 0.266 | 0.441 | 0.176 | 0.319 | 4.9% | 27.4% |
| 9 | Brady House | 193 | 0.242 | 0.404 | 0.163 | 0.315 | 9.5% | 28.9% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Wilyer Abreu | 360 | 0.261 | 0.432 | 0.171 | 0.333 | 11.9% | 23.6% |
| 2 | Jarren Duran | 354 | 0.201 | 0.353 | 0.152 | 0.275 | 11.1% | 25.6% |
| 3 | Willson Contreras | 349 | 0.277 | 0.510 | 0.233 | 0.391 | 13.3% | 29.3% |
| 4 | Ceddanne Rafaela | 333 | 0.289 | 0.451 | 0.162 | 0.356 | 5.4% | 21.4% |
| 5 | Caleb Durbin | 289 | 0.238 | 0.381 | 0.143 | 0.302 | 2.7% | 20.9% |
| 6 | Marcelo Mayer | 248 | 0.215 | 0.305 | 0.090 | 0.279 | 6.8% | 27.0% |
| 7 | Masataka Yoshida | 196 | 0.247 | 0.356 | 0.109 | 0.311 | 2.0% | 28.0% |
| 8 | Trevor Story | 194 | 0.225 | 0.335 | 0.110 | 0.286 | 4.0% | 22.1% |
| 9 | Carlos Narváez | 168 | 0.193 | 0.273 | 0.080 | 0.266 | 8.1% | 20.3% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7197 |
| Hits Allowed | 1582 |
| Walks/HBP | 701 |
| Strikeouts | 1514 |
| Home Runs Allowed | 246 |
| K Event Rate | 21.0% |
| BB/HBP Event Rate | 9.7% |
| HR Event Rate | 3.4% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6801 |
| Hits Allowed | 1477 |
| Walks/HBP | 625 |
| Strikeouts | 1514 |
| Home Runs Allowed | 171 |
| K Event Rate | 22.3% |
| BB/HBP Event Rate | 9.2% |
| HR Event Rate | 2.5% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SI, SL, CU, CH
- Home pitcher pitch mix to inspect: SI, FF, FC, CU, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 6. Texas Rangers @ Cleveland Guardians

## Game Context

| Field | Value |
| --- | --- |
| Park | Progressive Field |
| Time | 2026-06-29T23:10:00Z |
| Away Team | Texas Rangers |
| Home Team | Cleveland Guardians |
| Away Probable Pitcher | Tyler Alexander |
| Home Probable Pitcher | Parker Messick |


## Away Starting Pitcher: Tyler Alexander

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 559 |
| Batted/Result Events | 151 |
| Hits Allowed | 35 |
| Walks | 12 |
| Strikeouts | 27 |
| Home Runs | 2 |
| K Event Rate | 17.9% |
| BB Event Rate | 7.9% |
| HR Event Rate | 1.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-28 | TOR | 1.0 | 0 | 0 | 0 | 1 | 0 |
| 2026-06-27 | TOR | 1.0 | 0 | 0 | 0 | 0 | 0 |
| 2026-06-24 | MIA | 1.0 | 0 | 0 | 0 | 2 | 0 |
| 2026-06-22 | MIA | 1.0 | 0 | 0 | 0 | 1 | 0 |
| 2026-06-20 | TEX | 1.0 | 1 | 0 | 1 | 0 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 1.4% | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.165 | 0.0% | 25.0% | 0.0% |
| CH | vs R | 24.9% | 139 | 0.222 | 0.311 | 0.089 | 0.280 | 0.251 | 2.7% | 31.6% | 21.5% |
| FC | vs L | 7.5% | 42 | 0.500 | 0.500 | 0.000 | 0.367 | 0.217 | 0.0% | 16.7% | 25.0% |
| FC | vs R | 16.3% | 91 | 0.222 | 0.444 | 0.222 | 0.379 | 0.374 | 12.5% | 12.5% | 13.3% |
| FF | vs L | 2.3% | 13 | 0.500 | 0.500 | 0.000 | 0.450 | 0.354 | 0.0% | 33.3% | 50.0% |
| FF | vs R | 8.1% | 45 | 0.000 | 0.000 | 0.000 | 0.078 | 0.141 | 0.0% | 10.0% | 12.5% |
| SI | vs L | 13.8% | 77 | 0.379 | 0.379 | 0.000 | 0.400 | 0.316 | 0.0% | 22.2% | 5.0% |
| SI | vs R | 8.2% | 46 | 0.200 | 0.300 | 0.100 | 0.296 | 0.218 | 0.0% | 14.3% | 11.8% |
| ST | vs L | 11.1% | 62 | 0.200 | 0.350 | 0.150 | 0.280 | 0.303 | 6.2% | 28.0% | 27.8% |
| ST | vs R | 6.3% | 35 | 0.600 | 1.000 | 0.400 | 0.680 | 0.169 | 0.0% | 28.6% | 11.1% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-28 | 10 | 0 | 0 | 1 | 0 |
| 2026-06-27 | 15 | 0 | 0 | 0 | 0 |
| 2026-06-24 | 13 | 0 | 0 | 2 | 0 |
| 2026-06-22 | 15 | 0 | 0 | 1 | 0 |
| 2026-06-20 | 9 | 1 | 1 | 0 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Angel Martínez | 26 | 0.391 | 0.826 | 0.435 | 0.531 | 0.393 | 11.8% | 35.1% | 10.9% |
| FC | Travis Bazzana | 11 | 0.250 | 0.625 | 0.375 | 0.386 | 0.405 | 0.0% | 35.0% | 22.2% |
| FF | José Ramírez | 83 | 0.292 | 0.653 | 0.361 | 0.426 | 0.411 | 10.9% | 30.6% | 10.5% |
| FC | Austin Hedges | 11 | 0.333 | 0.667 | 0.333 | 0.427 | 0.097 | 0.0% | 11.8% | 27.6% |
| FC | Brayan Rocchio | 24 | 0.318 | 0.636 | 0.318 | 0.435 | 0.333 | 9.5% | 25.0% | 14.6% |
| CH | Rhys Hoskins | 24 | 0.105 | 0.421 | 0.316 | 0.254 | 0.265 | 16.7% | 42.9% | 41.7% |
| FC | Kyle Manzardo | 24 | 0.211 | 0.526 | 0.316 | 0.358 | 0.339 | 13.3% | 39.5% | 21.7% |
| CH | Bo Naylor | 11 | 0.200 | 0.500 | 0.300 | 0.327 | 0.356 | 14.3% | 11.1% | 26.9% |
| FC | David Fry | 12 | 0.200 | 0.500 | 0.300 | 0.358 | 0.342 | 14.3% | 6.7% | 32.0% |
| FC | José Ramírez | 35 | 0.250 | 0.531 | 0.281 | 0.384 | 0.309 | 7.7% | 32.2% | 14.1% |
| FC | Chase Delauter | 22 | 0.368 | 0.632 | 0.263 | 0.464 | 0.406 | 12.5% | 31.2% | 17.9% |
| FC | Rhys Hoskins | 21 | 0.211 | 0.474 | 0.263 | 0.324 | 0.219 | 0.0% | 29.6% | 30.2% |
| SI | David Fry | 25 | 0.348 | 0.609 | 0.261 | 0.430 | 0.358 | 11.8% | 22.9% | 21.6% |
| FF | Daniel Schneemann | 65 | 0.224 | 0.483 | 0.259 | 0.339 | 0.356 | 15.4% | 21.8% | 23.2% |
| FF | Travis Bazzana | 86 | 0.293 | 0.547 | 0.253 | 0.402 | 0.325 | 6.5% | 23.0% | 14.2% |
| ST | Brayan Rocchio | 14 | 0.167 | 0.417 | 0.250 | 0.371 | 0.286 | 9.1% | 12.5% | 22.7% |
| ST | Chase Delauter | 19 | 0.235 | 0.471 | 0.235 | 0.339 | 0.355 | 0.0% | 42.1% | 9.1% |
| FF | Angel Martínez | 64 | 0.179 | 0.411 | 0.232 | 0.305 | 0.318 | 11.1% | 19.2% | 11.1% |
| SI | Travis Bazzana | 48 | 0.308 | 0.538 | 0.231 | 0.424 | 0.395 | 8.3% | 33.3% | 15.5% |
| FF | Rhys Hoskins | 73 | 0.224 | 0.431 | 0.207 | 0.366 | 0.308 | 7.3% | 27.1% | 22.7% |
| ST | Travis Bazzana | 15 | 0.133 | 0.333 | 0.200 | 0.193 | 0.200 | 11.1% | 16.7% | 31.6% |
| FF | Chase Delauter | 101 | 0.302 | 0.500 | 0.198 | 0.382 | 0.327 | 11.4% | 20.8% | 13.2% |
| FF | David Fry | 53 | 0.190 | 0.381 | 0.190 | 0.336 | 0.270 | 6.5% | 28.3% | 23.1% |
| CH | Travis Bazzana | 19 | 0.176 | 0.353 | 0.176 | 0.274 | 0.180 | 0.0% | 12.5% | 51.2% |
| FC | Daniel Schneemann | 20 | 0.294 | 0.471 | 0.176 | 0.385 | 0.304 | 7.1% | 18.5% | 17.1% |
| ST | Kyle Manzardo | 21 | 0.167 | 0.333 | 0.167 | 0.281 | 0.293 | 14.3% | 7.7% | 35.7% |
| FF | Brayan Rocchio | 99 | 0.321 | 0.488 | 0.167 | 0.390 | 0.369 | 2.7% | 21.1% | 15.0% |
| CH | José Ramírez | 60 | 0.214 | 0.375 | 0.161 | 0.296 | 0.322 | 4.3% | 29.6% | 21.5% |
| SI | Kyle Manzardo | 45 | 0.282 | 0.436 | 0.154 | 0.381 | 0.473 | 14.8% | 38.3% | 23.1% |
| SI | Bo Naylor | 15 | 0.462 | 0.615 | 0.154 | 0.500 | 0.343 | 0.0% | 31.0% | 3.2% |


## Home Starting Pitcher: Parker Messick

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1630 |
| Batted/Result Events | 418 |
| Hits Allowed | 83 |
| Walks | 30 |
| Strikeouts | 111 |
| Home Runs | 12 |
| K Event Rate | 26.6% |
| BB Event Rate | 7.2% |
| HR Event Rate | 2.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | CWS | 9.0 | 3 | 1 | 1 | 10 | 1 |
| 2026-06-18 | MIL | 8.3 | 4 | 0 | 2 | 9 | 0 |
| 2026-06-10 | CLE | 8.3 | 5 | 0 | 3 | 4 | 0 |
| 2026-06-05 | TEX | 7.7 | 5 | 2 | 1 | 4 | 2 |
| 2026-05-30 | CLE | 7.3 | 5 | 0 | 1 | 4 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 2.7% | 44 | 0.250 | 0.438 | 0.188 | 0.291 | 0.254 | 0.0% | 50.0% | 33.3% |
| CH | vs R | 21.3% | 348 | 0.234 | 0.330 | 0.096 | 0.275 | 0.232 | 6.9% | 21.0% | 38.6% |
| CU | vs L | 2.2% | 36 | 0.400 | 0.500 | 0.100 | 0.423 | 0.168 | 0.0% | 7.7% | 0.0% |
| CU | vs R | 9.1% | 149 | 0.312 | 0.438 | 0.125 | 0.347 | 0.315 | 6.2% | 25.8% | 10.3% |
| FC | vs L | 0.6% | 9 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 100.0% |
| FC | vs R | 7.5% | 122 | 0.333 | 0.905 | 0.571 | 0.565 | 0.329 | 18.8% | 16.2% | 19.6% |
| FF | vs L | 9.3% | 151 | 0.156 | 0.219 | 0.062 | 0.209 | 0.173 | 10.5% | 20.0% | 38.0% |
| FF | vs R | 22.2% | 362 | 0.170 | 0.298 | 0.128 | 0.232 | 0.228 | 8.8% | 22.3% | 20.2% |
| SI | vs L | 7.6% | 124 | 0.235 | 0.294 | 0.059 | 0.270 | 0.318 | 0.0% | 22.9% | 10.2% |
| SI | vs R | 9.3% | 151 | 0.158 | 0.289 | 0.132 | 0.237 | 0.480 | 7.7% | 37.9% | 5.3% |
| SL | vs L | 6.0% | 98 | 0.238 | 0.524 | 0.286 | 0.352 | 0.425 | 10.5% | 23.5% | 23.4% |
| SL | vs R | 1.8% | 30 | 0.143 | 0.571 | 0.429 | 0.286 | 0.430 | 20.0% | 25.0% | 20.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 95 | 3 | 1 | 10 | 1 |
| 2026-06-18 | 97 | 4 | 3 | 9 | 0 |
| 2026-06-10 | 100 | 5 | 3 | 4 | 0 |
| 2026-06-05 | 85 | 5 | 1 | 4 | 2 |
| 2026-05-30 | 97 | 5 | 2 | 4 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Kyle Higashioka | 8 | 0.375 | 0.875 | 0.500 | 0.631 | 0.292 | 14.3% | 17.6% | 29.2% |
| CH | Kyle Higashioka | 11 | 0.333 | 0.778 | 0.444 | 0.505 | 0.358 | 20.0% | 40.0% | 41.7% |
| FC | Joc Pederson | 18 | 0.375 | 0.812 | 0.438 | 0.519 | 0.438 | 14.3% | 25.8% | 25.0% |
| CU | Corey Seager | 8 | 0.429 | 0.857 | 0.429 | 0.556 | 0.460 | 75.0% | 36.4% | 40.0% |
| FC | Danny Jansen | 8 | 0.143 | 0.571 | 0.429 | 0.338 | 0.288 | 20.0% | 20.0% | 28.6% |
| FC | Josh Jung | 25 | 0.333 | 0.762 | 0.429 | 0.494 | 0.483 | 9.5% | 38.5% | 18.0% |
| FC | Corey Seager | 19 | 0.316 | 0.737 | 0.421 | 0.437 | 0.500 | 16.7% | 34.8% | 7.1% |
| CU | Jake Burger | 16 | 0.333 | 0.667 | 0.333 | 0.494 | 0.438 | 30.0% | 27.3% | 23.3% |
| SI | Jake Burger | 63 | 0.321 | 0.643 | 0.321 | 0.443 | 0.396 | 11.1% | 32.1% | 16.2% |
| CU | Josh Jung | 17 | 0.312 | 0.625 | 0.312 | 0.412 | 0.468 | 14.3% | 45.5% | 17.9% |
| FF | Joc Pederson | 92 | 0.269 | 0.577 | 0.308 | 0.407 | 0.425 | 17.9% | 39.4% | 25.3% |
| CH | Wyatt Langford | 13 | 0.231 | 0.538 | 0.308 | 0.319 | 0.332 | 10.0% | 40.0% | 30.3% |
| CH | Corey Seager | 34 | 0.233 | 0.533 | 0.300 | 0.391 | 0.398 | 20.0% | 35.5% | 34.0% |
| CH | Danny Jansen | 12 | 0.364 | 0.636 | 0.273 | 0.446 | 0.278 | 0.0% | 15.4% | 36.4% |
| FC | Wyatt Langford | 16 | 0.200 | 0.467 | 0.267 | 0.303 | 0.295 | 15.4% | 16.0% | 28.9% |
| SI | Joc Pederson | 28 | 0.350 | 0.600 | 0.250 | 0.438 | 0.472 | 11.1% | 33.3% | 17.0% |
| CU | Wyatt Langford | 5 | 0.250 | 0.500 | 0.250 | 0.390 | 0.438 | 25.0% | 22.2% | 10.0% |
| FC | Brandon Nimmo | 38 | 0.278 | 0.528 | 0.250 | 0.358 | 0.413 | 16.1% | 36.2% | 18.5% |
| SI | Kyle Higashioka | 44 | 0.368 | 0.605 | 0.237 | 0.457 | 0.406 | 12.9% | 33.3% | 12.3% |
| CH | Jake Burger | 36 | 0.281 | 0.500 | 0.219 | 0.354 | 0.349 | 9.5% | 24.2% | 37.9% |
| FF | Evan Carter | 83 | 0.186 | 0.400 | 0.214 | 0.312 | 0.355 | 11.7% | 22.0% | 13.8% |
| FF | Corey Seager | 58 | 0.149 | 0.362 | 0.213 | 0.292 | 0.292 | 21.4% | 22.5% | 28.9% |
| FF | Josh Jung | 92 | 0.275 | 0.487 | 0.212 | 0.383 | 0.357 | 15.0% | 29.2% | 12.8% |
| SI | Wyatt Langford | 46 | 0.325 | 0.525 | 0.200 | 0.408 | 0.354 | 3.0% | 44.6% | 8.6% |
| CH | Josh Jung | 32 | 0.429 | 0.607 | 0.179 | 0.481 | 0.322 | 4.5% | 36.1% | 20.8% |
| FF | Brandon Nimmo | 121 | 0.265 | 0.441 | 0.176 | 0.358 | 0.351 | 7.5% | 25.6% | 16.3% |
| FC | Alejandro Osuna | 19 | 0.412 | 0.588 | 0.176 | 0.508 | 0.391 | 0.0% | 37.0% | 0.0% |
| CH | Joc Pederson | 42 | 0.195 | 0.366 | 0.171 | 0.249 | 0.313 | 6.1% | 35.4% | 30.6% |
| CU | Josh Smith | 7 | 0.333 | 0.500 | 0.167 | 0.407 | 0.218 | 25.0% | 14.3% | 41.7% |
| FF | Ezequiel Duran | 68 | 0.164 | 0.328 | 0.164 | 0.257 | 0.266 | 12.5% | 17.9% | 24.4% |


## Texas Rangers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brandon Nimmo | 373 | 0.259 | 0.419 | 0.160 | 0.336 | 0.383 | 13.3% | 30.9% | 18.2% |
| Josh Jung | 349 | 0.294 | 0.446 | 0.152 | 0.354 | 0.343 | 5.8% | 29.5% | 16.9% |
| Jake Burger | 345 | 0.260 | 0.452 | 0.192 | 0.344 | 0.314 | 9.8% | 31.2% | 31.6% |
| Ezequiel Duran | 290 | 0.268 | 0.426 | 0.158 | 0.335 | 0.306 | 7.1% | 22.7% | 23.3% |
| Joc Pederson | 280 | 0.237 | 0.456 | 0.220 | 0.347 | 0.354 | 11.4% | 31.9% | 29.0% |
| Evan Carter | 243 | 0.167 | 0.304 | 0.137 | 0.274 | 0.291 | 6.8% | 22.9% | 25.2% |
| Corey Seager | 236 | 0.183 | 0.376 | 0.193 | 0.297 | 0.336 | 16.4% | 26.5% | 31.6% |
| Wyatt Langford | 190 | 0.278 | 0.506 | 0.227 | 0.360 | 0.303 | 8.0% | 25.9% | 19.0% |
| Alejandro Osuna | 174 | 0.258 | 0.291 | 0.033 | 0.317 | 0.317 | 0.8% | 21.7% | 11.8% |
| Kyle Higashioka | 166 | 0.242 | 0.389 | 0.148 | 0.326 | 0.296 | 9.6% | 28.9% | 27.3% |
| Danny Jansen | 152 | 0.176 | 0.321 | 0.145 | 0.274 | 0.254 | 6.8% | 25.1% | 24.0% |
| Josh Smith | 137 | 0.214 | 0.239 | 0.026 | 0.268 | 0.284 | 4.4% | 24.9% | 19.0% |


## Cleveland Guardians Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Steven Kwan | 334 | 0.204 | 0.258 | 0.054 | 0.283 | 0.303 | 0.4% | 8.1% | 6.9% |
| José Ramírez | 329 | 0.247 | 0.452 | 0.205 | 0.352 | 0.355 | 7.9% | 30.6% | 15.1% |
| Brayan Rocchio | 322 | 0.268 | 0.391 | 0.123 | 0.333 | 0.308 | 2.9% | 21.0% | 21.1% |
| Chase Delauter | 295 | 0.284 | 0.452 | 0.169 | 0.358 | 0.338 | 6.8% | 26.1% | 13.5% |
| Kyle Manzardo | 286 | 0.231 | 0.398 | 0.167 | 0.323 | 0.314 | 11.9% | 24.0% | 29.0% |
| Angel Martínez | 260 | 0.247 | 0.469 | 0.222 | 0.322 | 0.306 | 8.9% | 23.8% | 16.8% |
| Rhys Hoskins | 254 | 0.198 | 0.401 | 0.203 | 0.327 | 0.283 | 11.0% | 28.5% | 28.1% |
| Daniel Schneemann | 245 | 0.215 | 0.354 | 0.139 | 0.289 | 0.296 | 8.0% | 23.2% | 29.9% |
| Travis Bazzana | 238 | 0.272 | 0.471 | 0.199 | 0.365 | 0.311 | 5.7% | 24.9% | 24.6% |
| David Fry | 147 | 0.216 | 0.384 | 0.168 | 0.326 | 0.272 | 7.1% | 22.1% | 28.7% |
| Austin Hedges | 129 | 0.270 | 0.360 | 0.090 | 0.331 | 0.291 | 3.2% | 21.8% | 23.1% |
| Bo Naylor | 108 | 0.152 | 0.242 | 0.091 | 0.207 | 0.295 | 9.7% | 24.3% | 14.9% |


## Bullpen Fatigue Report

### Texas Rangers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Cole Winn | 2026-06-28 | 2.0 | 28 |
| Jacob Latz | 2026-06-25 | 1.0 | 25 |
| Jacob Latz | 2026-06-26 | 1.0 | 14 |
| Jakob Junis | 2026-06-25 | 1.0 | 18 |
| Jakob Junis | 2026-06-26 | 0.2 | 23 |
| Joe Ross | 2026-06-27 | 1.1 | 29 |
| Peyton Gray | 2026-06-27 | 2.1 | 39 |
| Robby Ahlstrom | 2026-06-26 | 0.1 | 15 |
| Robby Ahlstrom | 2026-06-27 | 0.1 | 12 |
| Tyler Alexander | 2026-06-27 | 1.0 | 15 |
| Tyler Alexander | 2026-06-28 | 1.0 | 10 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Cole Winn, Tyler Alexander


### Cleveland Guardians Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Cade Smith | 2026-06-27 | 1.0 | 14 |
| Cade Smith | 2026-06-28 | 1.0 | 21 |
| Colin Holderman | 2026-06-27 | 0.2 | 14 |
| Daniel Espino | 2026-06-26 | 0.1 | 18 |
| Erik Sabrowski | 2026-06-27 | 0.1 | 8 |
| Hunter Gaddis | 2026-06-26 | 0.2 | 8 |
| Hunter Gaddis | 2026-06-27 | 1.0 | 14 |
| Matt Festa | 2026-06-26 | 1.0 | 18 |
| Matt Festa | 2026-06-28 | 1.1 | 20 |
| Shawn Armstrong | 2026-06-27 | 0.0 | 10 |
| Shawn Armstrong | 2026-06-28 | 0.2 | 18 |
| Tim Herrin | 2026-06-26 | 1.0 | 23 |
| Tim Herrin | 2026-06-28 | 1.0 | 16 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Cade Smith, Matt Festa, Shawn Armstrong, Tim Herrin



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Brandon Nimmo | 373 | 0.259 | 0.419 | 0.160 | 0.336 | 13.3% | 30.9% |
| 2 | Josh Jung | 349 | 0.294 | 0.446 | 0.152 | 0.354 | 5.8% | 29.5% |
| 3 | Jake Burger | 345 | 0.260 | 0.452 | 0.192 | 0.344 | 9.8% | 31.2% |
| 4 | Ezequiel Duran | 290 | 0.268 | 0.426 | 0.158 | 0.335 | 7.1% | 22.7% |
| 5 | Joc Pederson | 280 | 0.237 | 0.456 | 0.220 | 0.347 | 11.4% | 31.9% |
| 6 | Evan Carter | 243 | 0.167 | 0.304 | 0.137 | 0.274 | 6.8% | 22.9% |
| 7 | Corey Seager | 236 | 0.183 | 0.376 | 0.193 | 0.297 | 16.4% | 26.5% |
| 8 | Wyatt Langford | 190 | 0.278 | 0.506 | 0.227 | 0.360 | 8.0% | 25.9% |
| 9 | Alejandro Osuna | 174 | 0.258 | 0.291 | 0.033 | 0.317 | 0.8% | 21.7% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Steven Kwan | 334 | 0.204 | 0.258 | 0.054 | 0.283 | 0.4% | 8.1% |
| 2 | José Ramírez | 329 | 0.247 | 0.452 | 0.205 | 0.352 | 7.9% | 30.6% |
| 3 | Brayan Rocchio | 322 | 0.268 | 0.391 | 0.123 | 0.333 | 2.9% | 21.0% |
| 4 | Chase Delauter | 295 | 0.284 | 0.452 | 0.169 | 0.358 | 6.8% | 26.1% |
| 5 | Kyle Manzardo | 286 | 0.231 | 0.398 | 0.167 | 0.323 | 11.9% | 24.0% |
| 6 | Angel Martínez | 260 | 0.247 | 0.469 | 0.222 | 0.322 | 8.9% | 23.8% |
| 7 | Rhys Hoskins | 254 | 0.198 | 0.401 | 0.203 | 0.327 | 11.0% | 28.5% |
| 8 | Daniel Schneemann | 245 | 0.215 | 0.354 | 0.139 | 0.289 | 8.0% | 23.2% |
| 9 | Travis Bazzana | 238 | 0.272 | 0.471 | 0.199 | 0.365 | 5.7% | 24.9% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6859 |
| Hits Allowed | 1464 |
| Walks/HBP | 658 |
| Strikeouts | 1568 |
| Home Runs Allowed | 209 |
| K Event Rate | 22.9% |
| BB/HBP Event Rate | 9.6% |
| HR Event Rate | 3.0% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7007 |
| Hits Allowed | 1478 |
| Walks/HBP | 708 |
| Strikeouts | 1622 |
| Home Runs Allowed | 212 |
| K Event Rate | 23.1% |
| BB/HBP Event Rate | 10.1% |
| HR Event Rate | 3.0% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: CH, FC, SI, ST, FF
- Home pitcher pitch mix to inspect: FF, CH, SI, CU, FC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 7. Cincinnati Reds @ Milwaukee Brewers

## Game Context

| Field | Value |
| --- | --- |
| Park | American Family Field |
| Time | 2026-06-29T23:40:00Z |
| Away Team | Cincinnati Reds |
| Home Team | Milwaukee Brewers |
| Away Probable Pitcher | Nick Lodolo |
| Home Probable Pitcher | Robert Gasser |


## Away Starting Pitcher: Nick Lodolo

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 903 |
| Batted/Result Events | 234 |
| Hits Allowed | 57 |
| Walks | 20 |
| Strikeouts | 45 |
| Home Runs | 10 |
| K Event Rate | 19.2% |
| BB Event Rate | 8.5% |
| HR Event Rate | 4.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | CIN | 5.0 | 2 | 0 | 1 | 6 | 0 |
| 2026-06-17 | CIN | 8.3 | 11 | 0 | 2 | 2 | 0 |
| 2026-06-12 | CIN | 8.7 | 5 | 0 | 4 | 5 | 0 |
| 2026-06-06 | STL | 8.3 | 10 | 1 | 1 | 3 | 1 |
| 2026-05-31 | CIN | 9.7 | 5 | 2 | 4 | 4 | 2 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.3% | 3 | 0.000 | 0.000 | 0.000 | 0.700 | 0.700 | 0.0% | 0.0% | 100.0% |
| CH | vs R | 21.9% | 198 | 0.250 | 0.350 | 0.100 | 0.286 | 0.369 | 5.1% | 26.5% | 19.0% |
| CU | vs L | 12.4% | 112 | 0.318 | 0.318 | 0.000 | 0.321 | 0.402 | 0.0% | 10.3% | 31.1% |
| CU | vs R | 13.6% | 123 | 0.192 | 0.231 | 0.038 | 0.255 | 0.251 | 0.0% | 36.7% | 41.5% |
| FF | vs L | 4.7% | 42 | 0.500 | 0.875 | 0.375 | 0.540 | 0.552 | 14.3% | 33.3% | 6.7% |
| FF | vs R | 18.5% | 167 | 0.286 | 0.629 | 0.343 | 0.421 | 0.229 | 17.4% | 20.0% | 21.2% |
| SI | vs L | 13.6% | 123 | 0.250 | 0.375 | 0.125 | 0.351 | 0.357 | 0.0% | 31.0% | 13.7% |
| SI | vs R | 15.0% | 135 | 0.371 | 0.857 | 0.486 | 0.534 | 0.548 | 21.9% | 34.0% | 6.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 75 | 2 | 1 | 6 | 0 |
| 2026-06-17 | 90 | 11 | 2 | 2 | 0 |
| 2026-06-12 | 96 | 5 | 1 | 5 | 0 |
| 2026-06-06 | 95 | 10 | 1 | 3 | 1 |
| 2026-05-31 | 100 | 5 | 4 | 4 | 2 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Sal Frelick | 14 | 0.571 | 1.143 | 0.571 | 0.786 | 0.468 | 15.4% | 35.3% | 17.4% |
| CU | Jackson Chourio | 8 | 0.333 | 0.833 | 0.500 | 0.450 | 0.273 | 0.0% | 40.0% | 8.3% |
| CH | Christian Yelich | 20 | 0.375 | 0.875 | 0.500 | 0.555 | 0.333 | 18.2% | 31.8% | 25.0% |
| FF | Andrew Vaughn | 41 | 0.441 | 0.882 | 0.441 | 0.580 | 0.434 | 9.7% | 28.8% | 8.3% |
| CH | Jake Bauers | 32 | 0.345 | 0.759 | 0.414 | 0.483 | 0.399 | 23.8% | 43.8% | 41.7% |
| CU | Gary Sánchez | 12 | 0.273 | 0.636 | 0.364 | 0.404 | 0.353 | 12.5% | 18.2% | 18.8% |
| FF | Gary Sánchez | 52 | 0.325 | 0.675 | 0.350 | 0.485 | 0.464 | 15.6% | 21.8% | 18.6% |
| CU | Christian Yelich | 9 | 0.333 | 0.667 | 0.333 | 0.422 | 0.342 | 20.0% | 22.2% | 43.8% |
| FF | Jake Bauers | 86 | 0.373 | 0.707 | 0.333 | 0.487 | 0.393 | 18.5% | 31.5% | 16.9% |
| CU | Brice Turang | 21 | 0.333 | 0.619 | 0.286 | 0.405 | 0.372 | 15.4% | 44.4% | 29.6% |
| SI | Jackson Chourio | 51 | 0.370 | 0.630 | 0.261 | 0.472 | 0.425 | 13.9% | 43.3% | 10.1% |
| CU | Garrett Mitchell | 18 | 0.294 | 0.529 | 0.235 | 0.408 | 0.353 | 25.0% | 56.5% | 20.0% |
| FF | William Contreras | 91 | 0.247 | 0.481 | 0.234 | 0.387 | 0.377 | 9.1% | 34.7% | 12.5% |
| CH | Jackson Chourio | 23 | 0.364 | 0.591 | 0.227 | 0.422 | 0.236 | 5.6% | 26.7% | 15.0% |
| SI | Brice Turang | 67 | 0.276 | 0.500 | 0.224 | 0.397 | 0.347 | 4.5% | 23.0% | 12.0% |
| FF | Jackson Chourio | 60 | 0.268 | 0.482 | 0.214 | 0.358 | 0.332 | 21.6% | 24.7% | 23.4% |
| CH | Gary Sánchez | 18 | 0.267 | 0.467 | 0.200 | 0.339 | 0.297 | 7.7% | 43.8% | 44.7% |
| FF | David Hamilton | 85 | 0.254 | 0.437 | 0.183 | 0.358 | 0.304 | 5.0% | 17.5% | 10.1% |
| FF | Brice Turang | 108 | 0.198 | 0.372 | 0.174 | 0.340 | 0.335 | 11.3% | 16.5% | 20.2% |
| SI | Jake Bauers | 60 | 0.220 | 0.380 | 0.160 | 0.330 | 0.354 | 9.5% | 29.7% | 12.8% |
| CH | Brice Turang | 38 | 0.219 | 0.375 | 0.156 | 0.329 | 0.319 | 0.0% | 17.0% | 21.4% |
| CU | Andrew Vaughn | 7 | 0.143 | 0.286 | 0.143 | 0.179 | 0.341 | 20.0% | 33.3% | 45.5% |
| CH | Andrew Vaughn | 17 | 0.429 | 0.571 | 0.143 | 0.482 | 0.508 | 0.0% | 58.8% | 20.8% |
| SI | William Contreras | 93 | 0.366 | 0.500 | 0.134 | 0.401 | 0.374 | 11.0% | 37.1% | 6.0% |
| FF | Garrett Mitchell | 99 | 0.190 | 0.310 | 0.119 | 0.291 | 0.320 | 15.6% | 26.1% | 28.6% |
| SI | Gary Sánchez | 32 | 0.231 | 0.346 | 0.115 | 0.334 | 0.378 | 4.3% | 29.7% | 2.6% |
| FF | Luis Rengifo | 62 | 0.283 | 0.396 | 0.113 | 0.354 | 0.346 | 4.3% | 19.8% | 6.9% |
| SI | Sal Frelick | 60 | 0.278 | 0.389 | 0.111 | 0.361 | 0.300 | 1.9% | 18.9% | 1.3% |
| CH | Garrett Mitchell | 22 | 0.316 | 0.421 | 0.105 | 0.373 | 0.333 | 7.7% | 22.2% | 53.3% |
| SI | Andrew Vaughn | 35 | 0.323 | 0.419 | 0.097 | 0.373 | 0.379 | 3.4% | 39.1% | 6.1% |


## Home Starting Pitcher: Robert Gasser

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 612 |
| Batted/Result Events | 154 |
| Hits Allowed | 31 |
| Walks | 13 |
| Strikeouts | 38 |
| Home Runs | 6 |
| K Event Rate | 24.7% |
| BB Event Rate | 8.4% |
| HR Event Rate | 3.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-21 | ATL | 7.7 | 4 | 0 | 1 | 7 | 0 |
| 2026-06-16 | MIL | 6.7 | 2 | 0 | 2 | 5 | 0 |
| 2026-06-09 | ATH | 8.3 | 8 | 4 | 2 | 7 | 4 |
| 2026-06-03 | MIL | 7.0 | 5 | 1 | 1 | 5 | 1 |
| 2026-05-23 | MIL | 7.0 | 4 | 1 | 4 | 4 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.7% | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 50.0% |
| CH | vs R | 7.7% | 47 | 0.375 | 0.812 | 0.438 | 0.509 | 0.515 | 18.8% | 39.1% | 3.7% |
| FC | vs L | 6.7% | 41 | 0.200 | 0.800 | 0.600 | 0.533 | 0.365 | 0.0% | 16.7% | 37.5% |
| FC | vs R | 10.5% | 64 | 0.100 | 0.100 | 0.000 | 0.293 | 0.322 | 0.0% | 30.4% | 26.5% |
| FF | vs L | 6.0% | 37 | 0.125 | 0.250 | 0.125 | 0.217 | 0.173 | 0.0% | 15.4% | 31.8% |
| FF | vs R | 12.9% | 79 | 0.143 | 0.190 | 0.048 | 0.145 | 0.140 | 0.0% | 6.9% | 34.0% |
| SI | vs L | 11.3% | 69 | 0.286 | 0.500 | 0.214 | 0.397 | 0.412 | 10.0% | 41.7% | 15.8% |
| SI | vs R | 17.3% | 106 | 0.318 | 0.500 | 0.182 | 0.352 | 0.308 | 10.5% | 25.0% | 9.3% |
| ST | vs L | 9.5% | 58 | 0.250 | 0.562 | 0.312 | 0.338 | 0.140 | 0.0% | 16.7% | 24.0% |
| ST | vs R | 17.5% | 107 | 0.174 | 0.348 | 0.174 | 0.298 | 0.232 | 5.9% | 15.0% | 28.1% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-21 | 97 | 4 | 1 | 7 | 0 |
| 2026-06-16 | 92 | 2 | 2 | 5 | 0 |
| 2026-06-09 | 93 | 8 | 2 | 7 | 4 |
| 2026-06-03 | 83 | 5 | 1 | 5 | 1 |
| 2026-05-23 | 89 | 4 | 4 | 4 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Eugenio Suárez | 14 | 0.429 | 1.286 | 0.857 | 0.700 | 0.395 | 27.3% | 42.9% | 17.4% |
| FC | Nathaniel Lowe | 14 | 0.462 | 1.154 | 0.692 | 0.732 | 0.480 | 44.4% | 33.3% | 16.0% |
| ST | Jj Bleday | 13 | 0.273 | 0.818 | 0.545 | 0.481 | 0.202 | 0.0% | 20.0% | 40.7% |
| SI | Tyler Stephenson | 43 | 0.429 | 0.829 | 0.400 | 0.584 | 0.568 | 25.0% | 37.8% | 16.1% |
| CH | Nathaniel Lowe | 31 | 0.276 | 0.621 | 0.345 | 0.394 | 0.359 | 13.0% | 30.0% | 18.2% |
| FF | Elly De La Cruz | 105 | 0.253 | 0.579 | 0.326 | 0.388 | 0.423 | 27.7% | 36.4% | 15.6% |
| FF | Jj Bleday | 56 | 0.217 | 0.543 | 0.326 | 0.358 | 0.469 | 20.5% | 22.6% | 9.8% |
| FF | Sal Stewart | 103 | 0.318 | 0.624 | 0.306 | 0.467 | 0.383 | 20.8% | 29.9% | 32.4% |
| FC | Elly De La Cruz | 18 | 0.429 | 0.714 | 0.286 | 0.533 | 0.485 | 7.7% | 30.8% | 12.5% |
| FF | Spencer Steer | 82 | 0.208 | 0.486 | 0.278 | 0.339 | 0.355 | 24.4% | 27.7% | 26.2% |
| FC | Matt Mclain | 13 | 0.182 | 0.455 | 0.273 | 0.331 | 0.325 | 12.5% | 23.5% | 32.1% |
| CH | Spencer Steer | 36 | 0.176 | 0.441 | 0.265 | 0.311 | 0.215 | 15.0% | 27.0% | 30.2% |
| SI | Ke'Bryan Hayes | 35 | 0.219 | 0.469 | 0.250 | 0.323 | 0.401 | 15.4% | 41.5% | 10.9% |
| FC | Jj Bleday | 18 | 0.188 | 0.438 | 0.250 | 0.358 | 0.371 | 9.1% | 32.3% | 13.2% |
| ST | Matt Mclain | 40 | 0.243 | 0.459 | 0.216 | 0.328 | 0.285 | 17.4% | 24.3% | 21.8% |
| ST | Nathaniel Lowe | 6 | 0.200 | 0.400 | 0.200 | 0.325 | 0.261 | 0.0% | 27.3% | 13.3% |
| CH | Sal Stewart | 30 | 0.320 | 0.520 | 0.200 | 0.447 | 0.387 | 6.2% | 29.0% | 31.1% |
| SI | Dane Myers | 32 | 0.462 | 0.654 | 0.192 | 0.581 | 0.514 | 10.0% | 27.8% | 2.4% |
| FC | Spencer Steer | 24 | 0.429 | 0.619 | 0.190 | 0.485 | 0.446 | 6.2% | 29.6% | 20.5% |
| SI | Sal Stewart | 85 | 0.240 | 0.427 | 0.187 | 0.333 | 0.432 | 15.2% | 29.4% | 14.0% |
| CH | Jj Bleday | 50 | 0.200 | 0.378 | 0.178 | 0.304 | 0.340 | 8.8% | 29.6% | 33.7% |
| SI | Matt Mclain | 59 | 0.275 | 0.451 | 0.176 | 0.367 | 0.378 | 9.5% | 22.2% | 11.4% |
| SI | Elly De La Cruz | 40 | 0.243 | 0.405 | 0.162 | 0.292 | 0.313 | 12.5% | 34.2% | 16.0% |
| SI | Spencer Steer | 91 | 0.240 | 0.400 | 0.160 | 0.349 | 0.372 | 10.0% | 27.2% | 13.8% |
| FC | Sal Stewart | 28 | 0.333 | 0.481 | 0.148 | 0.366 | 0.400 | 8.7% | 29.4% | 24.6% |
| ST | Sal Stewart | 45 | 0.171 | 0.317 | 0.146 | 0.223 | 0.257 | 12.9% | 16.1% | 22.0% |
| ST | Spencer Steer | 37 | 0.229 | 0.371 | 0.143 | 0.280 | 0.285 | 16.0% | 22.9% | 17.9% |
| CH | Eugenio Suárez | 16 | 0.214 | 0.357 | 0.143 | 0.356 | 0.163 | 0.0% | 25.0% | 45.0% |
| FF | Eugenio Suárez | 65 | 0.211 | 0.351 | 0.140 | 0.286 | 0.270 | 8.6% | 16.4% | 30.6% |
| SI | Tj Friedl | 34 | 0.310 | 0.448 | 0.138 | 0.382 | 0.382 | 4.3% | 40.6% | 4.8% |


## Cincinnati Reds Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sal Stewart | 382 | 0.256 | 0.464 | 0.208 | 0.359 | 0.358 | 14.8% | 25.4% | 24.5% |
| Spencer Steer | 332 | 0.239 | 0.431 | 0.192 | 0.334 | 0.343 | 13.7% | 27.2% | 22.6% |
| Matt Mclain | 312 | 0.213 | 0.375 | 0.162 | 0.312 | 0.326 | 10.5% | 23.2% | 23.0% |
| Elly De La Cruz | 303 | 0.266 | 0.487 | 0.221 | 0.367 | 0.362 | 15.0% | 34.7% | 26.8% |
| Tyler Stephenson | 246 | 0.223 | 0.363 | 0.140 | 0.310 | 0.336 | 11.6% | 27.3% | 25.9% |
| Jj Bleday | 239 | 0.246 | 0.537 | 0.291 | 0.390 | 0.371 | 10.9% | 31.0% | 23.9% |
| Eugenio Suárez | 229 | 0.209 | 0.369 | 0.160 | 0.304 | 0.261 | 7.1% | 19.2% | 33.2% |
| Nathaniel Lowe | 219 | 0.254 | 0.482 | 0.228 | 0.368 | 0.362 | 11.9% | 21.1% | 17.0% |
| Tj Friedl | 197 | 0.197 | 0.277 | 0.081 | 0.256 | 0.248 | 3.2% | 23.2% | 24.1% |
| Blake Dunn | 158 | 0.276 | 0.379 | 0.103 | 0.326 | 0.280 | 2.8% | 20.6% | 20.7% |
| Dane Myers | 152 | 0.256 | 0.364 | 0.109 | 0.342 | 0.357 | 7.0% | 21.6% | 16.9% |
| Ke'Bryan Hayes | 146 | 0.157 | 0.231 | 0.075 | 0.224 | 0.312 | 8.5% | 31.3% | 18.1% |


## Milwaukee Brewers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brice Turang | 362 | 0.253 | 0.442 | 0.188 | 0.357 | 0.345 | 8.8% | 22.8% | 20.2% |
| William Contreras | 345 | 0.307 | 0.463 | 0.155 | 0.374 | 0.354 | 9.0% | 32.2% | 17.4% |
| Jake Bauers | 305 | 0.272 | 0.544 | 0.272 | 0.395 | 0.354 | 14.8% | 34.4% | 24.6% |
| Sal Frelick | 289 | 0.236 | 0.320 | 0.085 | 0.310 | 0.287 | 2.2% | 19.8% | 9.2% |
| Garrett Mitchell | 276 | 0.230 | 0.385 | 0.155 | 0.322 | 0.334 | 13.3% | 28.1% | 35.9% |
| David Hamilton | 239 | 0.255 | 0.361 | 0.106 | 0.313 | 0.265 | 4.9% | 17.7% | 19.9% |
| Christian Yelich | 238 | 0.248 | 0.388 | 0.140 | 0.314 | 0.295 | 6.9% | 21.0% | 30.0% |
| Jackson Chourio | 232 | 0.298 | 0.535 | 0.237 | 0.383 | 0.337 | 13.9% | 28.9% | 21.9% |
| Luis Rengifo | 229 | 0.211 | 0.289 | 0.078 | 0.274 | 0.296 | 5.5% | 23.1% | 15.8% |
| Joey Ortiz | 211 | 0.210 | 0.254 | 0.044 | 0.266 | 0.285 | 2.7% | 21.6% | 18.5% |
| Gary Sánchez | 168 | 0.232 | 0.471 | 0.239 | 0.364 | 0.371 | 10.2% | 28.0% | 23.5% |
| Andrew Vaughn | 162 | 0.326 | 0.504 | 0.177 | 0.406 | 0.357 | 4.9% | 31.2% | 15.8% |


## Bullpen Fatigue Report

### Cincinnati Reds Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brock Burke | 2026-06-26 | 1.0 | 20 |
| Brock Burke | 2026-06-28 | 1.1 | 9 |
| Caleb Ferguson | 2026-06-26 | 1.0 | 18 |
| Caleb Ferguson | 2026-06-27 | 1.0 | 14 |
| Chase Petty | 2026-06-27 | 1.0 | 12 |
| Julian Garcia | 2026-06-28 | 1.1 | 30 |
| Pierce Johnson | 2026-06-26 | 0.2 | 13 |
| Pierce Johnson | 2026-06-28 | 0.2 | 27 |
| Sam Moll | 2026-06-27 | 0.2 | 20 |
| Tejay Antone | 2026-06-26 | 1.0 | 17 |
| Tejay Antone | 2026-06-27 | 0.1 | 6 |
| Zach McCambley | 2026-06-28 | 0.1 | 15 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Brock Burke, Julian Garcia, Pierce Johnson, Zach McCambley


### Milwaukee Brewers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Aaron Ashby | 2026-06-26 | 1.0 | 15 |
| Aaron Ashby | 2026-06-28 | 0.2 | 24 |
| Abner Uribe | 2026-06-26 | 1.0 | 13 |
| Abner Uribe | 2026-06-28 | 1.2 | 14 |
| Chad Patrick | 2026-06-27 | 0.2 | 30 |
| Grant Anderson | 2026-06-27 | 1.1 | 26 |
| Jared Koenig | 2026-06-27 | 1.0 | 15 |
| Joel Kuhnel | 2026-06-27 | 1.0 | 18 |
| Joel Kuhnel | 2026-06-28 | 1.0 | 26 |
| Trevor Megill | 2026-06-26 | 1.0 | 26 |
| Trevor Megill | 2026-06-28 | 1.0 | 19 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Aaron Ashby, Abner Uribe, Joel Kuhnel, Trevor Megill



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Sal Stewart | 382 | 0.256 | 0.464 | 0.208 | 0.359 | 14.8% | 25.4% |
| 2 | Spencer Steer | 332 | 0.239 | 0.431 | 0.192 | 0.334 | 13.7% | 27.2% |
| 3 | Matt Mclain | 312 | 0.213 | 0.375 | 0.162 | 0.312 | 10.5% | 23.2% |
| 4 | Elly De La Cruz | 303 | 0.266 | 0.487 | 0.221 | 0.367 | 15.0% | 34.7% |
| 5 | Tyler Stephenson | 246 | 0.223 | 0.363 | 0.140 | 0.310 | 11.6% | 27.3% |
| 6 | Jj Bleday | 239 | 0.246 | 0.537 | 0.291 | 0.390 | 10.9% | 31.0% |
| 7 | Eugenio Suárez | 229 | 0.209 | 0.369 | 0.160 | 0.304 | 7.1% | 19.2% |
| 8 | Nathaniel Lowe | 219 | 0.254 | 0.482 | 0.228 | 0.368 | 11.9% | 21.1% |
| 9 | Tj Friedl | 197 | 0.197 | 0.277 | 0.081 | 0.256 | 3.2% | 23.2% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Brice Turang | 362 | 0.253 | 0.442 | 0.188 | 0.357 | 8.8% | 22.8% |
| 2 | William Contreras | 345 | 0.307 | 0.463 | 0.155 | 0.374 | 9.0% | 32.2% |
| 3 | Jake Bauers | 305 | 0.272 | 0.544 | 0.272 | 0.395 | 14.8% | 34.4% |
| 4 | Sal Frelick | 289 | 0.236 | 0.320 | 0.085 | 0.310 | 2.2% | 19.8% |
| 5 | Garrett Mitchell | 276 | 0.230 | 0.385 | 0.155 | 0.322 | 13.3% | 28.1% |
| 6 | David Hamilton | 239 | 0.255 | 0.361 | 0.106 | 0.313 | 4.9% | 17.7% |
| 7 | Christian Yelich | 238 | 0.248 | 0.388 | 0.140 | 0.314 | 6.9% | 21.0% |
| 8 | Jackson Chourio | 232 | 0.298 | 0.535 | 0.237 | 0.383 | 13.9% | 28.9% |
| 9 | Luis Rengifo | 229 | 0.211 | 0.289 | 0.078 | 0.274 | 5.5% | 23.1% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7160 |
| Hits Allowed | 1511 |
| Walks/HBP | 806 |
| Strikeouts | 1616 |
| Home Runs Allowed | 246 |
| K Event Rate | 22.6% |
| BB/HBP Event Rate | 11.3% |
| HR Event Rate | 3.4% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6938 |
| Hits Allowed | 1452 |
| Walks/HBP | 725 |
| Strikeouts | 1648 |
| Home Runs Allowed | 182 |
| K Event Rate | 23.8% |
| BB/HBP Event Rate | 10.4% |
| HR Event Rate | 2.6% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: SI, CU, FF, CH
- Home pitcher pitch mix to inspect: SI, ST, FF, FC, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 8. San Diego Padres @ Chicago Cubs

## Game Context

| Field | Value |
| --- | --- |
| Park | Wrigley Field |
| Time | 2026-06-30T00:05:00Z |
| Away Team | San Diego Padres |
| Home Team | Chicago Cubs |
| Away Probable Pitcher | TBD |
| Home Probable Pitcher | Shota Imanaga |


## Away Starting Pitcher: TBD

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


## Home Starting Pitcher: Shota Imanaga

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1574 |
| Batted/Result Events | 409 |
| Hits Allowed | 82 |
| Walks | 26 |
| Strikeouts | 101 |
| Home Runs | 21 |
| K Event Rate | 24.7% |
| BB Event Rate | 6.4% |
| HR Event Rate | 5.1% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | NYM | 6.7 | 4 | 3 | 1 | 4 | 3 |
| 2026-06-15 | CHC | 7.3 | 5 | 0 | 1 | 3 | 0 |
| 2026-06-10 | COL | 6.3 | 2 | 0 | 2 | 7 | 0 |
| 2026-06-04 | CHC | 8.0 | 6 | 4 | 1 | 5 | 4 |
| 2026-05-29 | STL | 7.7 | 5 | 3 | 3 | 2 | 3 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CU | vs R | 3.0% | 47 | 0.000 | 0.000 | 0.000 | 0.140 | 0.419 | 25.0% | 22.2% | 10.0% |
| FF | vs L | 10.3% | 162 | 0.209 | 0.419 | 0.209 | 0.286 | 0.378 | 13.5% | 36.8% | 7.4% |
| FF | vs R | 32.7% | 514 | 0.278 | 0.519 | 0.241 | 0.380 | 0.349 | 15.2% | 24.3% | 21.2% |
| FS | vs L | 4.4% | 69 | 0.150 | 0.200 | 0.050 | 0.179 | 0.123 | 0.0% | 6.7% | 58.5% |
| FS | vs R | 28.8% | 454 | 0.179 | 0.390 | 0.211 | 0.267 | 0.243 | 9.0% | 20.4% | 39.5% |
| SI | vs L | 2.2% | 35 | 0.214 | 0.429 | 0.214 | 0.347 | 0.363 | 8.3% | 33.3% | 22.7% |
| SI | vs R | 4.5% | 71 | 0.250 | 0.450 | 0.200 | 0.320 | 0.313 | 5.0% | 40.7% | 15.6% |
| SL | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | 0.000 | — | 0.0% | 0.0% | 0.0% |
| SL | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 100.0% |
| ST | vs L | 9.9% | 156 | 0.219 | 0.531 | 0.312 | 0.334 | 0.261 | 14.3% | 15.0% | 41.6% |
| ST | vs R | 3.9% | 62 | 0.250 | 0.333 | 0.083 | 0.318 | 0.343 | 0.0% | 29.4% | 25.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-24 | 69 | 4 | 1 | 4 | 3 |
| 2026-06-15 | 85 | 5 | 1 | 3 | 0 |
| 2026-06-10 | 90 | 2 | 2 | 7 | 0 |
| 2026-06-04 | 84 | 6 | 1 | 5 | 4 |
| 2026-05-29 | 75 | 5 | 1 | 2 | 3 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Samad Taylor | 6 | 0.167 | 0.667 | 0.500 | 0.333 | 0.195 | 33.3% | 20.0% | 40.0% |
| FS | Miguel Andújar | 7 | 0.143 | 0.571 | 0.429 | 0.286 | 0.149 | 0.0% | 33.3% | 30.8% |
| FF | Ty France | 43 | 0.216 | 0.541 | 0.324 | 0.383 | 0.312 | 22.2% | 13.8% | 32.5% |
| ST | Miguel Andújar | 26 | 0.280 | 0.600 | 0.320 | 0.352 | 0.205 | 5.6% | 29.0% | 32.7% |
| FF | Gavin Sheets | 97 | 0.262 | 0.548 | 0.286 | 0.388 | 0.376 | 11.4% | 27.6% | 11.8% |
| ST | Nick Castellanos | 15 | 0.214 | 0.500 | 0.286 | 0.323 | 0.454 | 16.7% | 17.4% | 32.5% |
| ST | Gavin Sheets | 13 | 0.182 | 0.455 | 0.273 | 0.331 | 0.319 | 33.3% | 44.4% | 50.0% |
| FF | Manny Machado | 104 | 0.216 | 0.455 | 0.239 | 0.332 | 0.390 | 13.6% | 25.9% | 22.5% |
| FF | Xander Bogaerts | 92 | 0.269 | 0.462 | 0.192 | 0.373 | 0.361 | 11.9% | 29.4% | 12.7% |
| FF | Ramón Laureano | 61 | 0.224 | 0.408 | 0.184 | 0.352 | 0.437 | 20.0% | 25.8% | 25.0% |
| FF | Miguel Andújar | 56 | 0.196 | 0.373 | 0.176 | 0.280 | 0.311 | 4.8% | 18.2% | 8.7% |
| ST | Ramón Laureano | 17 | 0.059 | 0.235 | 0.176 | 0.118 | 0.146 | 12.5% | 9.5% | 45.0% |
| ST | Xander Bogaerts | 34 | 0.207 | 0.379 | 0.172 | 0.294 | 0.315 | 8.0% | 21.1% | 20.0% |
| FF | Freddy Fermin | 45 | 0.132 | 0.263 | 0.132 | 0.258 | 0.285 | 3.3% | 12.0% | 15.0% |
| ST | Ty France | 26 | 0.217 | 0.348 | 0.130 | 0.269 | 0.239 | 11.8% | 22.9% | 23.4% |
| ST | Jackson Merrill | 24 | 0.125 | 0.250 | 0.125 | 0.158 | 0.260 | 10.5% | 19.0% | 22.8% |
| ST | Manny Machado | 38 | 0.121 | 0.242 | 0.121 | 0.243 | 0.211 | 5.0% | 18.0% | 37.0% |
| FF | Jackson Merrill | 114 | 0.188 | 0.307 | 0.119 | 0.271 | 0.314 | 13.2% | 23.8% | 25.4% |
| FF | Jake Cronenworth | 48 | 0.275 | 0.375 | 0.100 | 0.353 | 0.401 | 8.3% | 15.7% | 7.2% |
| ST | Fernando Tatís | 33 | 0.226 | 0.323 | 0.097 | 0.250 | 0.221 | 4.3% | 30.0% | 30.0% |
| FF | Fernando Tatís | 99 | 0.291 | 0.372 | 0.081 | 0.354 | 0.385 | 12.7% | 34.8% | 20.7% |
| ST | Freddy Fermin | 15 | 0.214 | 0.286 | 0.071 | 0.250 | 0.250 | 0.0% | 13.3% | 41.4% |
| FF | Nick Castellanos | 37 | 0.167 | 0.194 | 0.028 | 0.199 | 0.262 | 3.7% | 16.4% | 15.7% |
| FF | Samad Taylor | 26 | 0.381 | 0.381 | 0.000 | 0.419 | 0.335 | 0.0% | 18.5% | 21.1% |
| FS | Freddy Fermin | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.074 | 0.0% | 0.0% | 0.0% |
| FS | Nick Castellanos | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.091 | 0.0% | 0.0% | 58.3% |
| FS | Fernando Tatís | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.279 | 20.0% | 20.0% | 38.5% |
| FS | Ramón Laureano | 12 | 0.182 | 0.182 | 0.000 | 0.208 | 0.171 | 0.0% | 25.0% | 43.8% |
| FS | Jackson Merrill | 19 | 0.105 | 0.105 | 0.000 | 0.095 | 0.243 | 7.1% | 17.4% | 30.3% |
| FS | Jake Cronenworth | 4 | 0.000 | 0.000 | 0.000 | 0.175 | 0.352 | 0.0% | 0.0% | 16.7% |


## San Diego Padres Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fernando Tatís | 363 | 0.281 | 0.366 | 0.084 | 0.331 | 0.359 | 10.7% | 36.0% | 26.1% |
| Jackson Merrill | 352 | 0.207 | 0.341 | 0.133 | 0.275 | 0.306 | 9.3% | 24.9% | 25.2% |
| Manny Machado | 346 | 0.182 | 0.380 | 0.198 | 0.292 | 0.317 | 10.0% | 25.1% | 23.6% |
| Xander Bogaerts | 325 | 0.232 | 0.344 | 0.112 | 0.323 | 0.320 | 6.6% | 26.7% | 20.8% |
| Gavin Sheets | 286 | 0.238 | 0.477 | 0.238 | 0.346 | 0.331 | 9.4% | 30.8% | 18.2% |
| Miguel Andújar | 231 | 0.235 | 0.382 | 0.147 | 0.290 | 0.292 | 3.9% | 22.2% | 17.9% |
| Ramón Laureano | 224 | 0.209 | 0.383 | 0.173 | 0.301 | 0.312 | 13.4% | 23.3% | 30.5% |
| Ty France | 201 | 0.250 | 0.505 | 0.255 | 0.353 | 0.321 | 12.6% | 25.8% | 26.1% |
| Freddy Fermin | 166 | 0.156 | 0.255 | 0.099 | 0.253 | 0.267 | 2.7% | 15.6% | 22.7% |
| Nick Castellanos | 137 | 0.178 | 0.333 | 0.155 | 0.246 | 0.285 | 7.5% | 20.4% | 30.8% |
| Jake Cronenworth | 132 | 0.162 | 0.216 | 0.054 | 0.257 | 0.304 | 4.7% | 21.2% | 21.2% |
| Samad Taylor | 82 | 0.314 | 0.371 | 0.057 | 0.366 | 0.321 | 2.1% | 16.0% | 22.3% |


## Chicago Cubs Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nico Hoerner | 389 | 0.255 | 0.362 | 0.107 | 0.321 | 0.324 | 1.6% | 18.8% | 10.3% |
| Michael Busch | 388 | 0.233 | 0.387 | 0.154 | 0.347 | 0.350 | 11.1% | 25.5% | 23.9% |
| Alex Bregman | 386 | 0.249 | 0.375 | 0.126 | 0.332 | 0.312 | 5.5% | 27.3% | 16.5% |
| Pete Crow-Armstrong | 372 | 0.272 | 0.494 | 0.222 | 0.371 | 0.361 | 10.9% | 30.9% | 26.3% |
| Ian Happ | 367 | 0.225 | 0.463 | 0.238 | 0.359 | 0.329 | 14.7% | 25.1% | 29.3% |
| Dansby Swanson | 330 | 0.188 | 0.352 | 0.164 | 0.299 | 0.287 | 6.8% | 24.9% | 28.3% |
| Seiya Suzuki | 289 | 0.262 | 0.444 | 0.183 | 0.364 | 0.336 | 8.5% | 25.9% | 24.5% |
| Carson Kelly | 234 | 0.289 | 0.422 | 0.132 | 0.370 | 0.323 | 7.2% | 23.9% | 19.7% |
| Moisés Ballesteros | 193 | 0.246 | 0.439 | 0.193 | 0.335 | 0.310 | 11.3% | 28.2% | 23.3% |
| Matt Shaw | 169 | 0.255 | 0.436 | 0.181 | 0.356 | 0.301 | 5.1% | 22.2% | 18.5% |
| Miguel Amaya | 153 | 0.240 | 0.426 | 0.186 | 0.368 | 0.311 | 9.2% | 20.2% | 22.0% |
| Michael Conforto | 147 | 0.254 | 0.492 | 0.238 | 0.354 | 0.350 | 12.1% | 30.9% | 25.4% |


## Bullpen Fatigue Report

### San Diego Padres Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Adrian Morejon | 2026-06-26 | 1.0 | 9 |
| David Morgan | 2026-06-27 | 1.0 | 17 |
| Jason Adam | 2026-06-26 | 1.0 | 17 |
| Jason Adam | 2026-06-28 | 1.0 | 15 |
| Randy Vásquez | 2026-06-27 | 3.1 | 79 |
| Rodolfo Durán | 2026-06-27 | 1.0 | 14 |
| Ron Marinaccio | 2026-06-27 | 1.2 | 45 |
| Wandy Peralta | 2026-06-26 | 1.0 | 12 |
| Wandy Peralta | 2026-06-28 | 2.0 | 22 |
| Yuki Matsui | 2026-06-26 | 0.2 | 11 |
| Yuki Matsui | 2026-06-28 | 1.2 | 28 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Jason Adam, Wandy Peralta, Yuki Matsui


### Chicago Cubs Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Bryse Wilson | 2026-06-28 | 4.1 | 61 |
| Caleb Thielbar | 2026-06-25 | 1.0 | 12 |
| Caleb Thielbar | 2026-06-28 | 1.0 | 16 |
| Ethan Roberts | 2026-06-25 | 1.0 | 15 |
| Ethan Roberts | 2026-06-26 | 1.0 | 14 |
| Ethan Roberts | 2026-06-28 | 0.0 | 9 |
| Hoby Milner | 2026-06-25 | 0.0 | 13 |
| Jacob Webb | 2026-06-25 | 1.0 | 20 |
| Jacob Webb | 2026-06-27 | 1.0 | 13 |
| Jacob Webb | 2026-06-28 | 1.0 | 21 |
| Jayden Murray | 2026-06-26 | 2.0 | 46 |
| Jordan Wicks | 2026-06-28 | 1.0 | 11 |
| Phil Maton | 2026-06-25 | 1.1 | 23 |
| Trent Thornton | 2026-06-25 | 1.0 | 10 |
| Trent Thornton | 2026-06-27 | 1.0 | 12 |
| Tyler Ferguson | 2026-06-27 | 0.1 | 10 |
| Tyler Ferguson | 2026-06-28 | 0.2 | 8 |
| Vince Velasquez | 2026-06-27 | 1.0 | 12 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Bryse Wilson, Caleb Thielbar, Ethan Roberts, Jacob Webb, Jordan Wicks, Tyler Ferguson



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Fernando Tatís | 363 | 0.281 | 0.366 | 0.084 | 0.331 | 10.7% | 36.0% |
| 2 | Jackson Merrill | 352 | 0.207 | 0.341 | 0.133 | 0.275 | 9.3% | 24.9% |
| 3 | Manny Machado | 346 | 0.182 | 0.380 | 0.198 | 0.292 | 10.0% | 25.1% |
| 4 | Xander Bogaerts | 325 | 0.232 | 0.344 | 0.112 | 0.323 | 6.6% | 26.7% |
| 5 | Gavin Sheets | 286 | 0.238 | 0.477 | 0.238 | 0.346 | 9.4% | 30.8% |
| 6 | Miguel Andújar | 231 | 0.235 | 0.382 | 0.147 | 0.290 | 3.9% | 22.2% |
| 7 | Ramón Laureano | 224 | 0.209 | 0.383 | 0.173 | 0.301 | 13.4% | 23.3% |
| 8 | Ty France | 201 | 0.250 | 0.505 | 0.255 | 0.353 | 12.6% | 25.8% |
| 9 | Freddy Fermin | 166 | 0.156 | 0.255 | 0.099 | 0.253 | 2.7% | 15.6% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nico Hoerner | 389 | 0.255 | 0.362 | 0.107 | 0.321 | 1.6% | 18.8% |
| 2 | Michael Busch | 388 | 0.233 | 0.387 | 0.154 | 0.347 | 11.1% | 25.5% |
| 3 | Alex Bregman | 386 | 0.249 | 0.375 | 0.126 | 0.332 | 5.5% | 27.3% |
| 4 | Pete Crow-Armstrong | 372 | 0.272 | 0.494 | 0.222 | 0.371 | 10.9% | 30.9% |
| 5 | Ian Happ | 367 | 0.225 | 0.463 | 0.238 | 0.359 | 14.7% | 25.1% |
| 6 | Dansby Swanson | 330 | 0.188 | 0.352 | 0.164 | 0.299 | 6.8% | 24.9% |
| 7 | Seiya Suzuki | 289 | 0.262 | 0.444 | 0.183 | 0.364 | 8.5% | 25.9% |
| 8 | Carson Kelly | 234 | 0.289 | 0.422 | 0.132 | 0.370 | 7.2% | 23.9% |
| 9 | Moisés Ballesteros | 193 | 0.246 | 0.439 | 0.193 | 0.335 | 11.3% | 28.2% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6777 |
| Hits Allowed | 1401 |
| Walks/HBP | 682 |
| Strikeouts | 1527 |
| Home Runs Allowed | 194 |
| K Event Rate | 22.5% |
| BB/HBP Event Rate | 10.1% |
| HR Event Rate | 2.9% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7260 |
| Hits Allowed | 1570 |
| Walks/HBP | 785 |
| Strikeouts | 1569 |
| Home Runs Allowed | 268 |
| K Event Rate | 21.6% |
| BB/HBP Event Rate | 10.8% |
| HR Event Rate | 3.7% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: No current Statcast sample
- Home pitcher pitch mix to inspect: FF, FS, ST
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 9. Minnesota Twins @ Houston Astros

## Game Context

| Field | Value |
| --- | --- |
| Park | Daikin Park |
| Time | 2026-06-30T00:10:00Z |
| Away Team | Minnesota Twins |
| Home Team | Houston Astros |
| Away Probable Pitcher | Zebby Matthews |
| Home Probable Pitcher | Peter Lambert |


## Away Starting Pitcher: Zebby Matthews

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 828 |
| Batted/Result Events | 224 |
| Hits Allowed | 52 |
| Walks | 11 |
| Strikeouts | 40 |
| Home Runs | 10 |
| K Event Rate | 17.9% |
| BB Event Rate | 4.9% |
| HR Event Rate | 4.5% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | MIN | 8.7 | 6 | 2 | 2 | 5 | 2 |
| 2026-06-16 | TEX | 9.3 | 8 | 0 | 0 | 4 | 0 |
| 2026-06-11 | DET | 9.3 | 9 | 3 | 1 | 4 | 3 |
| 2026-06-05 | MIN | 9.0 | 5 | 0 | 4 | 2 | 0 |
| 2026-05-31 | PIT | 7.3 | 6 | 2 | 3 | 7 | 2 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 10.7% | 89 | 0.348 | 0.652 | 0.304 | 0.418 | 0.345 | 10.0% | 40.7% | 18.4% |
| CH | vs R | 0.8% | 7 | 0.500 | 1.000 | 0.500 | 0.625 | 0.437 | 0.0% | 50.0% | 0.0% |
| CU | vs L | 7.5% | 62 | 0.000 | 0.000 | 0.000 | 0.000 | 0.165 | 0.0% | 20.0% | 28.0% |
| CU | vs R | 5.4% | 45 | 0.300 | 0.600 | 0.300 | 0.380 | 0.189 | 0.0% | 38.5% | 35.0% |
| FC | vs L | 7.0% | 58 | 0.308 | 0.538 | 0.231 | 0.386 | 0.436 | 7.7% | 37.5% | 3.6% |
| FC | vs R | 5.0% | 41 | 0.300 | 0.700 | 0.400 | 0.505 | 0.389 | 11.1% | 14.3% | 22.2% |
| FF | vs L | 20.7% | 171 | 0.310 | 0.524 | 0.214 | 0.399 | 0.339 | 11.1% | 18.9% | 7.0% |
| FF | vs R | 16.1% | 133 | 0.148 | 0.296 | 0.148 | 0.222 | 0.376 | 16.7% | 25.0% | 13.8% |
| FS | vs L | 0.4% | 3 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| FS | vs R | 0.4% | 3 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs L | 0.2% | 2 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs R | 4.2% | 35 | 0.500 | 0.667 | 0.167 | 0.536 | 0.386 | 20.0% | 33.3% | 14.3% |
| SL | vs L | 9.5% | 79 | 0.192 | 0.346 | 0.154 | 0.253 | 0.344 | 27.8% | 40.0% | 34.9% |
| SL | vs R | 12.1% | 100 | 0.200 | 0.275 | 0.075 | 0.208 | 0.193 | 3.3% | 15.8% | 31.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 108 | 6 | 2 | 5 | 2 |
| 2026-06-16 | 93 | 8 | 0 | 4 | 0 |
| 2026-06-11 | 81 | 9 | 1 | 4 | 3 |
| 2026-06-05 | 100 | 5 | 4 | 2 | 0 |
| 2026-05-31 | 100 | 6 | 2 | 7 | 2 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Joey Loperfido | 7 | 0.286 | 0.714 | 0.429 | 0.414 | 0.416 | 16.7% | 30.0% | 31.2% |
| CU | Yordan Álvarez | 35 | 0.333 | 0.758 | 0.424 | 0.469 | 0.578 | 25.0% | 51.5% | 27.7% |
| SL | Christian Walker | 64 | 0.279 | 0.689 | 0.410 | 0.414 | 0.274 | 13.3% | 29.7% | 38.2% |
| FC | Isaac Paredes | 30 | 0.450 | 0.800 | 0.350 | 0.565 | 0.464 | 5.0% | 12.2% | 11.8% |
| FF | Yordan Álvarez | 100 | 0.286 | 0.631 | 0.345 | 0.433 | 0.467 | 17.5% | 28.2% | 14.6% |
| FC | Brice Matthews | 18 | 0.278 | 0.611 | 0.333 | 0.472 | 0.429 | 13.3% | 26.1% | 21.2% |
| FC | Yordan Álvarez | 35 | 0.290 | 0.613 | 0.323 | 0.416 | 0.508 | 20.8% | 28.3% | 16.9% |
| SL | Yordan Álvarez | 42 | 0.289 | 0.579 | 0.289 | 0.402 | 0.420 | 19.4% | 19.2% | 23.2% |
| CH | Christian Walker | 29 | 0.259 | 0.519 | 0.259 | 0.353 | 0.339 | 15.0% | 29.0% | 34.0% |
| SL | Cam Smith | 41 | 0.200 | 0.457 | 0.257 | 0.340 | 0.358 | 21.7% | 25.5% | 38.8% |
| FF | Yainer Diaz | 36 | 0.219 | 0.469 | 0.250 | 0.333 | 0.316 | 12.5% | 19.1% | 23.9% |
| CU | José Altuve | 5 | 0.500 | 0.750 | 0.250 | 0.570 | 0.416 | 0.0% | 14.3% | 27.3% |
| FC | Yainer Diaz | 12 | 0.417 | 0.667 | 0.250 | 0.467 | 0.436 | 9.1% | 21.1% | 13.6% |
| FF | Christian Walker | 95 | 0.190 | 0.430 | 0.241 | 0.344 | 0.308 | 8.9% | 20.3% | 21.7% |
| SL | Jeremy Peña | 41 | 0.235 | 0.471 | 0.235 | 0.366 | 0.327 | 0.0% | 17.0% | 36.5% |
| CU | Jeremy Peña | 15 | 0.214 | 0.429 | 0.214 | 0.300 | 0.225 | 16.7% | 33.3% | 56.5% |
| FC | Christian Vázquez | 14 | 0.214 | 0.429 | 0.214 | 0.271 | 0.263 | 8.3% | 11.5% | 12.5% |
| CH | Cam Smith | 30 | 0.143 | 0.357 | 0.214 | 0.240 | 0.280 | 23.1% | 30.4% | 59.6% |
| FF | Isaac Paredes | 101 | 0.236 | 0.449 | 0.213 | 0.347 | 0.347 | 9.2% | 24.7% | 9.9% |
| CH | Yordan Álvarez | 46 | 0.302 | 0.512 | 0.209 | 0.391 | 0.447 | 11.4% | 31.3% | 15.5% |
| FF | Cam Smith | 93 | 0.256 | 0.462 | 0.205 | 0.361 | 0.383 | 16.9% | 31.1% | 19.9% |
| FF | José Altuve | 80 | 0.297 | 0.500 | 0.203 | 0.379 | 0.329 | 11.8% | 39.1% | 25.3% |
| CH | Jeremy Peña | 13 | 0.182 | 0.364 | 0.182 | 0.315 | 0.377 | 10.0% | 45.0% | 30.0% |
| SL | José Altuve | 45 | 0.167 | 0.333 | 0.167 | 0.232 | 0.252 | 6.1% | 7.8% | 27.4% |
| FC | Christian Walker | 27 | 0.269 | 0.423 | 0.154 | 0.313 | 0.337 | 4.2% | 25.5% | 18.1% |
| FC | José Altuve | 21 | 0.200 | 0.350 | 0.150 | 0.257 | 0.353 | 11.1% | 25.9% | 12.1% |
| FF | Christian Vázquez | 76 | 0.224 | 0.373 | 0.149 | 0.295 | 0.268 | 3.5% | 13.3% | 14.8% |
| FF | Joey Loperfido | 42 | 0.353 | 0.500 | 0.147 | 0.432 | 0.400 | 7.7% | 31.5% | 18.7% |
| CU | Isaac Paredes | 23 | 0.143 | 0.286 | 0.143 | 0.226 | 0.298 | 13.3% | 16.1% | 21.3% |
| CU | Cam Smith | 9 | 0.286 | 0.429 | 0.143 | 0.317 | 0.349 | 0.0% | 21.7% | 13.3% |


## Home Starting Pitcher: Peter Lambert

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1184 |
| Batted/Result Events | 299 |
| Hits Allowed | 55 |
| Walks | 29 |
| Strikeouts | 65 |
| Home Runs | 7 |
| K Event Rate | 21.7% |
| BB Event Rate | 9.7% |
| HR Event Rate | 2.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | TOR | 7.7 | 6 | 1 | 3 | 6 | 1 |
| 2026-06-17 | HOU | 8.0 | 2 | 1 | 1 | 5 | 1 |
| 2026-06-10 | LAA | 8.0 | 5 | 2 | 0 | 6 | 2 |
| 2026-06-05 | HOU | 8.0 | 5 | 1 | 4 | 4 | 1 |
| 2026-05-30 | HOU | 7.3 | 5 | 0 | 3 | 3 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 15.9% | 188 | 0.200 | 0.229 | 0.029 | 0.308 | 0.287 | 0.0% | 13.0% | 39.5% |
| CH | vs R | 5.7% | 68 | 0.238 | 0.286 | 0.048 | 0.231 | 0.144 | 0.0% | 22.7% | 33.3% |
| CU | vs L | 0.7% | 8 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CU | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| FC | vs L | 7.5% | 89 | 0.190 | 0.286 | 0.095 | 0.315 | 0.324 | 0.0% | 21.4% | 21.1% |
| FC | vs R | 2.1% | 25 | 0.286 | 0.429 | 0.143 | 0.356 | 0.187 | 0.0% | 16.7% | 0.0% |
| FF | vs L | 17.7% | 210 | 0.133 | 0.222 | 0.089 | 0.252 | 0.296 | 9.1% | 22.8% | 15.2% |
| FF | vs R | 12.7% | 150 | 0.250 | 0.550 | 0.300 | 0.344 | 0.420 | 25.8% | 27.3% | 18.4% |
| SI | vs L | 0.5% | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.292 | 0.0% | 25.0% | 0.0% |
| SI | vs R | 10.0% | 118 | 0.357 | 0.464 | 0.107 | 0.372 | 0.281 | 3.7% | 21.2% | 1.8% |
| SL | vs L | 7.9% | 93 | 0.050 | 0.050 | 0.000 | 0.130 | 0.215 | 6.7% | 25.9% | 31.7% |
| SL | vs R | 10.4% | 123 | 0.273 | 0.500 | 0.227 | 0.358 | 0.293 | 10.0% | 29.7% | 21.2% |
| ST | vs L | 3.3% | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.167 | 0.0% | 14.3% | 30.0% |
| ST | vs R | 2.6% | 31 | 0.333 | 0.556 | 0.222 | 0.378 | 0.403 | 0.0% | 60.0% | 14.3% |
| SV | vs L | 1.9% | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.011 | 0.0% | 0.0% | 0.0% |
| SV | vs R | 0.9% | 11 | 0.250 | 0.500 | 0.250 | 0.312 | 0.358 | 0.0% | 50.0% | 16.7% |
| UN | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 92 | 6 | 3 | 6 | 1 |
| 2026-06-17 | 89 | 2 | 0 | 5 | 1 |
| 2026-06-10 | 91 | 5 | 0 | 6 | 2 |
| 2026-06-05 | 94 | 5 | 4 | 4 | 1 |
| 2026-05-30 | 90 | 5 | 3 | 3 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Byron Buxton | 29 | 0.333 | 0.889 | 0.556 | 0.493 | 0.383 | 19.0% | 29.0% | 29.2% |
| FC | Víctor Caratini | 27 | 0.500 | 1.056 | 0.556 | 0.643 | 0.600 | 15.8% | 23.7% | 9.3% |
| FC | Brooks Lee | 23 | 0.500 | 1.000 | 0.500 | 0.639 | 0.526 | 10.0% | 41.0% | 10.2% |
| FC | Matt Wallner | 8 | 0.375 | 0.875 | 0.500 | 0.519 | 0.364 | 16.7% | 25.0% | 36.4% |
| SI | Ryan Jeffers | 31 | 0.560 | 1.000 | 0.440 | 0.671 | 0.536 | 13.6% | 26.1% | 8.9% |
| FC | Tristan Gray | 15 | 0.214 | 0.643 | 0.429 | 0.340 | 0.464 | 25.0% | 42.9% | 24.1% |
| FF | Byron Buxton | 95 | 0.310 | 0.726 | 0.417 | 0.462 | 0.432 | 35.1% | 35.3% | 24.8% |
| SL | Byron Buxton | 45 | 0.256 | 0.641 | 0.385 | 0.416 | 0.368 | 20.0% | 17.9% | 31.0% |
| FC | Trevor Larnach | 15 | 0.364 | 0.727 | 0.364 | 0.583 | 0.353 | 9.1% | 15.0% | 8.7% |
| FC | Ryan Jeffers | 19 | 0.588 | 0.941 | 0.353 | 0.663 | 0.482 | 12.5% | 33.3% | 16.0% |
| SL | Kody Clemens | 37 | 0.222 | 0.556 | 0.333 | 0.331 | 0.375 | 18.5% | 37.3% | 25.0% |
| FC | Kody Clemens | 19 | 0.222 | 0.556 | 0.333 | 0.339 | 0.385 | 30.8% | 25.0% | 23.5% |
| SL | Brooks Lee | 48 | 0.267 | 0.578 | 0.311 | 0.394 | 0.274 | 0.0% | 26.9% | 26.3% |
| SI | Byron Buxton | 69 | 0.299 | 0.567 | 0.269 | 0.388 | 0.365 | 10.2% | 33.3% | 19.0% |
| FF | Brooks Lee | 94 | 0.280 | 0.549 | 0.268 | 0.397 | 0.301 | 8.2% | 15.7% | 14.9% |
| SL | Trevor Larnach | 26 | 0.238 | 0.476 | 0.238 | 0.412 | 0.297 | 15.4% | 22.6% | 47.5% |
| SL | Josh Bell | 33 | 0.200 | 0.433 | 0.233 | 0.332 | 0.380 | 16.7% | 29.4% | 18.9% |
| SI | Tristan Gray | 14 | 0.308 | 0.538 | 0.231 | 0.386 | 0.353 | 9.1% | 20.0% | 5.9% |
| SL | Royce Lewis | 39 | 0.188 | 0.406 | 0.219 | 0.294 | 0.264 | 18.2% | 22.2% | 42.6% |
| FF | Kody Clemens | 95 | 0.207 | 0.415 | 0.207 | 0.324 | 0.310 | 9.4% | 23.7% | 20.3% |
| CH | Kody Clemens | 35 | 0.324 | 0.529 | 0.206 | 0.374 | 0.383 | 7.4% | 38.2% | 24.0% |
| SI | Matt Wallner | 25 | 0.250 | 0.450 | 0.200 | 0.378 | 0.436 | 12.5% | 27.0% | 14.0% |
| FF | Josh Bell | 105 | 0.308 | 0.505 | 0.198 | 0.404 | 0.364 | 6.7% | 21.9% | 19.4% |
| FF | Ryan Jeffers | 45 | 0.211 | 0.395 | 0.184 | 0.309 | 0.359 | 25.0% | 25.7% | 8.6% |
| FF | Trevor Larnach | 96 | 0.333 | 0.506 | 0.172 | 0.394 | 0.383 | 7.6% | 31.2% | 10.6% |
| FF | Luke Keaschall | 85 | 0.263 | 0.434 | 0.171 | 0.335 | 0.307 | 4.6% | 23.8% | 10.7% |
| FF | Royce Lewis | 61 | 0.185 | 0.352 | 0.167 | 0.270 | 0.291 | 22.2% | 21.7% | 26.1% |
| FC | Josh Bell | 31 | 0.233 | 0.400 | 0.167 | 0.284 | 0.416 | 11.1% | 26.1% | 15.8% |
| SI | Royce Lewis | 50 | 0.217 | 0.370 | 0.152 | 0.305 | 0.371 | 10.0% | 33.9% | 20.0% |
| FF | Matt Wallner | 50 | 0.209 | 0.349 | 0.140 | 0.304 | 0.231 | 11.5% | 22.6% | 34.2% |


## Minnesota Twins Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brooks Lee | 342 | 0.258 | 0.452 | 0.194 | 0.350 | 0.279 | 4.5% | 21.1% | 18.0% |
| Josh Bell | 341 | 0.232 | 0.376 | 0.145 | 0.303 | 0.320 | 9.3% | 22.8% | 22.9% |
| Byron Buxton | 338 | 0.269 | 0.586 | 0.317 | 0.386 | 0.351 | 19.5% | 30.5% | 29.2% |
| Luke Keaschall | 332 | 0.253 | 0.345 | 0.092 | 0.316 | 0.293 | 3.7% | 21.9% | 14.1% |
| Kody Clemens | 295 | 0.245 | 0.487 | 0.242 | 0.347 | 0.342 | 12.9% | 30.2% | 22.1% |
| Austin Martin | 266 | 0.262 | 0.338 | 0.076 | 0.338 | 0.311 | 2.2% | 18.7% | 18.1% |
| Trevor Larnach | 262 | 0.285 | 0.439 | 0.154 | 0.372 | 0.335 | 7.7% | 26.0% | 25.7% |
| Víctor Caratini | 247 | 0.236 | 0.380 | 0.144 | 0.317 | 0.338 | 8.4% | 25.2% | 20.4% |
| Royce Lewis | 228 | 0.206 | 0.353 | 0.147 | 0.290 | 0.300 | 12.2% | 25.3% | 29.8% |
| Tristan Gray | 177 | 0.238 | 0.341 | 0.104 | 0.275 | 0.282 | 6.3% | 24.9% | 29.9% |
| Ryan Jeffers | 166 | 0.298 | 0.532 | 0.234 | 0.417 | 0.389 | 15.4% | 27.0% | 15.8% |
| Matt Wallner | 151 | 0.194 | 0.343 | 0.149 | 0.288 | 0.281 | 11.5% | 24.1% | 39.3% |


## Houston Astros Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yordan Álvarez | 379 | 0.305 | 0.594 | 0.289 | 0.424 | 0.475 | 17.8% | 30.4% | 16.7% |
| Christian Walker | 364 | 0.236 | 0.473 | 0.236 | 0.350 | 0.304 | 10.0% | 27.1% | 25.5% |
| Isaac Paredes | 340 | 0.253 | 0.423 | 0.171 | 0.348 | 0.318 | 6.2% | 22.7% | 16.7% |
| Cam Smith | 328 | 0.216 | 0.360 | 0.144 | 0.297 | 0.332 | 12.8% | 27.9% | 28.1% |
| José Altuve | 280 | 0.233 | 0.375 | 0.142 | 0.308 | 0.297 | 6.4% | 22.8% | 23.8% |
| Brice Matthews | 223 | 0.197 | 0.340 | 0.143 | 0.283 | 0.262 | 9.1% | 23.7% | 35.6% |
| Jeremy Peña | 202 | 0.295 | 0.443 | 0.148 | 0.365 | 0.345 | 4.0% | 24.3% | 26.1% |
| Christian Vázquez | 186 | 0.214 | 0.321 | 0.107 | 0.267 | 0.237 | 2.2% | 14.4% | 16.5% |
| Jake Meyers | 153 | 0.206 | 0.319 | 0.113 | 0.282 | 0.259 | 7.3% | 17.0% | 19.8% |
| Yainer Diaz | 152 | 0.243 | 0.361 | 0.118 | 0.287 | 0.280 | 5.0% | 20.2% | 20.6% |
| Carlos Correa | 149 | 0.281 | 0.414 | 0.133 | 0.356 | 0.364 | 9.8% | 22.4% | 21.2% |
| Joey Loperfido | 126 | 0.224 | 0.336 | 0.112 | 0.304 | 0.303 | 6.4% | 20.0% | 27.4% |


## Bullpen Fatigue Report

### Minnesota Twins Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Andrew Morris | 2026-06-26 | 1.0 | 6 |
| Andrew Morris | 2026-06-28 | 1.1 | 15 |
| Anthony Banda | 2026-06-26 | 0.2 | 11 |
| Anthony Banda | 2026-06-28 | 0.2 | 14 |
| Eric Orze | 2026-06-26 | 0.1 | 14 |
| Kody Funderburk | 2026-06-26 | 1.0 | 20 |
| Kody Funderburk | 2026-06-27 | 1.0 | 25 |
| Marco Raya | 2026-06-27 | 2.0 | 40 |
| Taylor Rogers | 2026-06-27 | 0.2 | 9 |
| Yoendrys Gómez | 2026-06-28 | 1.0 | 4 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Andrew Morris, Anthony Banda, Yoendrys Gómez


### Houston Astros Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| AJ Blubaugh | 2026-06-25 | 2.0 | 25 |
| AJ Blubaugh | 2026-06-27 | 2.0 | 28 |
| Bryan Abreu | 2026-06-26 | 1.0 | 10 |
| Bryan Abreu | 2026-06-28 | 0.2 | 15 |
| Bryan King | 2026-06-27 | 1.0 | 11 |
| Bryan King | 2026-06-28 | 1.0 | 8 |
| Enyel De Los Santos | 2026-06-25 | 1.0 | 10 |
| Enyel De Los Santos | 2026-06-28 | 1.0 | 25 |
| Jake Meyers | 2026-06-26 | 1.0 | 9 |
| Josh Hader | 2026-06-27 | 1.0 | 11 |
| Josh Hader | 2026-06-28 | 1.0 | 29 |
| Nate Pearson | 2026-06-26 | 3.0 | 48 |
| Steven Okert | 2026-06-27 | 1.1 | 15 |
| Steven Okert | 2026-06-28 | 0.1 | 3 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Bryan Abreu, Bryan King, Enyel De Los Santos, Josh Hader, Steven Okert



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Brooks Lee | 342 | 0.258 | 0.452 | 0.194 | 0.350 | 4.5% | 21.1% |
| 2 | Josh Bell | 341 | 0.232 | 0.376 | 0.145 | 0.303 | 9.3% | 22.8% |
| 3 | Byron Buxton | 338 | 0.269 | 0.586 | 0.317 | 0.386 | 19.5% | 30.5% |
| 4 | Luke Keaschall | 332 | 0.253 | 0.345 | 0.092 | 0.316 | 3.7% | 21.9% |
| 5 | Kody Clemens | 295 | 0.245 | 0.487 | 0.242 | 0.347 | 12.9% | 30.2% |
| 6 | Austin Martin | 266 | 0.262 | 0.338 | 0.076 | 0.338 | 2.2% | 18.7% |
| 7 | Trevor Larnach | 262 | 0.285 | 0.439 | 0.154 | 0.372 | 7.7% | 26.0% |
| 8 | Víctor Caratini | 247 | 0.236 | 0.380 | 0.144 | 0.317 | 8.4% | 25.2% |
| 9 | Royce Lewis | 228 | 0.206 | 0.353 | 0.147 | 0.290 | 12.2% | 25.3% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Yordan Álvarez | 379 | 0.305 | 0.594 | 0.289 | 0.424 | 17.8% | 30.4% |
| 2 | Christian Walker | 364 | 0.236 | 0.473 | 0.236 | 0.350 | 10.0% | 27.1% |
| 3 | Isaac Paredes | 340 | 0.253 | 0.423 | 0.171 | 0.348 | 6.2% | 22.7% |
| 4 | Cam Smith | 328 | 0.216 | 0.360 | 0.144 | 0.297 | 12.8% | 27.9% |
| 5 | José Altuve | 280 | 0.233 | 0.375 | 0.142 | 0.308 | 6.4% | 22.8% |
| 6 | Brice Matthews | 223 | 0.197 | 0.340 | 0.143 | 0.283 | 9.1% | 23.7% |
| 7 | Jeremy Peña | 202 | 0.295 | 0.443 | 0.148 | 0.365 | 4.0% | 24.3% |
| 8 | Christian Vázquez | 186 | 0.214 | 0.321 | 0.107 | 0.267 | 2.2% | 14.4% |
| 9 | Jake Meyers | 153 | 0.206 | 0.319 | 0.113 | 0.282 | 7.3% | 17.0% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7212 |
| Hits Allowed | 1615 |
| Walks/HBP | 727 |
| Strikeouts | 1504 |
| Home Runs Allowed | 222 |
| K Event Rate | 20.9% |
| BB/HBP Event Rate | 10.1% |
| HR Event Rate | 3.1% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7091 |
| Hits Allowed | 1483 |
| Walks/HBP | 789 |
| Strikeouts | 1575 |
| Home Runs Allowed | 233 |
| K Event Rate | 22.2% |
| BB/HBP Event Rate | 11.1% |
| HR Event Rate | 3.3% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL, CU, FC, CH
- Home pitcher pitch mix to inspect: FF, CH, SL, SI, FC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 10. Miami Marlins @ Colorado Rockies

## Game Context

| Field | Value |
| --- | --- |
| Park | Coors Field |
| Time | 2026-06-30T00:40:00Z |
| Away Team | Miami Marlins |
| Home Team | Colorado Rockies |
| Away Probable Pitcher | Sandy Alcantara |
| Home Probable Pitcher | TBD |


## Away Starting Pitcher: Sandy Alcantara

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1809 |
| Batted/Result Events | 497 |
| Hits Allowed | 117 |
| Walks | 28 |
| Strikeouts | 92 |
| Home Runs | 12 |
| K Event Rate | 18.5% |
| BB Event Rate | 5.6% |
| HR Event Rate | 2.4% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | MIA | 9.0 | 5 | 0 | 3 | 4 | 0 |
| 2026-06-17 | PHI | 9.3 | 8 | 0 | 1 | 6 | 0 |
| 2026-06-12 | PIT | 10.0 | 5 | 2 | 1 | 7 | 2 |
| 2026-06-07 | MIA | 8.3 | 5 | 0 | 2 | 7 | 0 |
| 2026-06-01 | WSH | 9.0 | 7 | 1 | 0 | 5 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 16.6% | 300 | 0.274 | 0.389 | 0.116 | 0.325 | 0.311 | 3.8% | 19.8% | 26.5% |
| CH | vs R | 5.3% | 96 | 0.294 | 0.500 | 0.206 | 0.400 | 0.271 | 4.2% | 48.6% | 30.0% |
| CU | vs L | 2.9% | 53 | 0.111 | 0.111 | 0.000 | 0.100 | 0.099 | 0.0% | 6.7% | 23.8% |
| CU | vs R | 0.8% | 14 | 0.400 | 1.000 | 0.600 | 0.580 | 0.468 | 20.0% | 37.5% | 0.0% |
| FC | vs L | 8.0% | 144 | 0.160 | 0.280 | 0.120 | 0.208 | 0.303 | 5.0% | 16.4% | 13.2% |
| FC | vs R | 5.5% | 100 | 0.190 | 0.190 | 0.000 | 0.238 | 0.289 | 0.0% | 16.7% | 29.3% |
| FF | vs L | 13.1% | 237 | 0.333 | 0.614 | 0.281 | 0.447 | 0.407 | 12.8% | 25.7% | 13.3% |
| FF | vs R | 6.2% | 113 | 0.241 | 0.241 | 0.000 | 0.263 | 0.242 | 4.8% | 27.9% | 17.9% |
| SI | vs L | 13.8% | 249 | 0.227 | 0.303 | 0.076 | 0.285 | 0.315 | 8.8% | 24.8% | 8.7% |
| SI | vs R | 10.5% | 190 | 0.300 | 0.367 | 0.067 | 0.318 | 0.323 | 1.9% | 21.2% | 5.6% |
| SL | vs L | 3.7% | 67 | 0.231 | 0.462 | 0.231 | 0.362 | 0.258 | 14.3% | 25.0% | 27.8% |
| SL | vs R | 5.1% | 93 | 0.222 | 0.333 | 0.111 | 0.263 | 0.175 | 0.0% | 24.0% | 30.8% |
| ST | vs L | 5.1% | 92 | 0.154 | 0.385 | 0.231 | 0.335 | 0.411 | 25.0% | 15.4% | 36.4% |
| ST | vs R | 3.3% | 60 | 0.133 | 0.133 | 0.000 | 0.120 | 0.093 | 0.0% | 4.8% | 21.4% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 109 | 5 | 3 | 4 | 0 |
| 2026-06-17 | 102 | 8 | 1 | 6 | 0 |
| 2026-06-12 | 102 | 5 | 1 | 7 | 2 |
| 2026-06-07 | 90 | 5 | 1 | 7 | 0 |
| 2026-06-01 | 95 | 7 | 0 | 5 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Mickey Moniak | 23 | 0.238 | 0.714 | 0.476 | 0.415 | 0.305 | 30.0% | 36.0% | 36.6% |
| ST | Brett Sullivan | 10 | 0.222 | 0.667 | 0.444 | 0.345 | 0.068 | 0.0% | 8.3% | 31.6% |
| SL | Hunter Goodman | 55 | 0.250 | 0.692 | 0.442 | 0.436 | 0.334 | 22.6% | 31.7% | 38.0% |
| SL | Tj Rumfield | 40 | 0.316 | 0.632 | 0.316 | 0.414 | 0.279 | 8.0% | 29.5% | 35.4% |
| SI | Edouard Julien | 18 | 0.438 | 0.750 | 0.312 | 0.528 | 0.461 | 13.3% | 29.4% | 8.1% |
| FF | Brett Sullivan | 40 | 0.270 | 0.568 | 0.297 | 0.360 | 0.300 | 6.7% | 24.3% | 10.6% |
| SI | Hunter Goodman | 48 | 0.390 | 0.683 | 0.293 | 0.493 | 0.459 | 13.9% | 28.1% | 16.5% |
| FC | Willi Castro | 22 | 0.476 | 0.762 | 0.286 | 0.539 | 0.455 | 18.8% | 23.3% | 17.9% |
| ST | Hunter Goodman | 42 | 0.231 | 0.513 | 0.282 | 0.338 | 0.287 | 14.3% | 26.5% | 50.6% |
| FC | Hunter Goodman | 20 | 0.389 | 0.667 | 0.278 | 0.475 | 0.442 | 17.6% | 30.0% | 25.6% |
| SL | Mickey Moniak | 20 | 0.167 | 0.444 | 0.278 | 0.295 | 0.311 | 23.1% | 17.2% | 31.2% |
| FF | Hunter Goodman | 103 | 0.196 | 0.467 | 0.272 | 0.323 | 0.336 | 22.4% | 26.8% | 22.6% |
| FC | Tj Rumfield | 25 | 0.304 | 0.565 | 0.261 | 0.394 | 0.305 | 8.7% | 15.9% | 12.5% |
| CH | Hunter Goodman | 30 | 0.222 | 0.481 | 0.259 | 0.342 | 0.232 | 11.1% | 24.1% | 43.3% |
| SL | Troy Johnston | 40 | 0.333 | 0.590 | 0.256 | 0.381 | 0.298 | 3.0% | 34.0% | 15.9% |
| FF | Mickey Moniak | 54 | 0.288 | 0.538 | 0.250 | 0.363 | 0.299 | 7.7% | 20.3% | 18.5% |
| FF | Kyle Karros | 99 | 0.373 | 0.614 | 0.241 | 0.467 | 0.407 | 8.8% | 28.6% | 6.1% |
| FC | Mickey Moniak | 18 | 0.353 | 0.588 | 0.235 | 0.419 | 0.406 | 7.1% | 33.3% | 16.7% |
| CH | Ezequiel Tovar | 26 | 0.192 | 0.423 | 0.231 | 0.292 | 0.224 | 6.2% | 21.6% | 40.3% |
| SI | Jake Mccarthy | 47 | 0.409 | 0.636 | 0.227 | 0.465 | 0.378 | 7.9% | 30.2% | 13.7% |
| FF | Tj Rumfield | 113 | 0.299 | 0.505 | 0.206 | 0.388 | 0.363 | 9.0% | 22.0% | 10.9% |
| FF | Jake Mccarthy | 108 | 0.326 | 0.526 | 0.200 | 0.379 | 0.361 | 4.7% | 15.2% | 11.5% |
| SL | Ezequiel Tovar | 48 | 0.283 | 0.478 | 0.196 | 0.311 | 0.303 | 10.3% | 13.2% | 31.5% |
| ST | Troy Johnston | 17 | 0.250 | 0.438 | 0.188 | 0.318 | 0.301 | 0.0% | 33.3% | 22.9% |
| SL | Tyler Freeman | 29 | 0.286 | 0.464 | 0.179 | 0.366 | 0.285 | 0.0% | 27.6% | 22.0% |
| CH | Brett Sullivan | 18 | 0.176 | 0.353 | 0.176 | 0.208 | 0.178 | 0.0% | 10.0% | 16.0% |
| SI | Willi Castro | 29 | 0.250 | 0.417 | 0.167 | 0.388 | 0.354 | 5.3% | 22.2% | 25.0% |
| CH | Tj Rumfield | 45 | 0.214 | 0.381 | 0.167 | 0.303 | 0.264 | 8.3% | 25.8% | 21.4% |
| FC | Edouard Julien | 24 | 0.278 | 0.444 | 0.167 | 0.408 | 0.313 | 10.0% | 11.1% | 17.9% |
| CH | Mickey Moniak | 32 | 0.161 | 0.323 | 0.161 | 0.197 | 0.212 | 4.0% | 35.1% | 30.6% |


## Home Starting Pitcher: TBD

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


## Miami Marlins Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Otto Lopez | 366 | 0.328 | 0.475 | 0.147 | 0.382 | 0.335 | 6.9% | 29.0% | 18.7% |
| Xavier Edwards | 363 | 0.297 | 0.429 | 0.132 | 0.360 | 0.328 | 4.7% | 18.6% | 14.1% |
| Jakob Marsee | 349 | 0.190 | 0.289 | 0.099 | 0.286 | 0.299 | 3.3% | 22.5% | 17.9% |
| Liam Hicks | 305 | 0.269 | 0.451 | 0.182 | 0.353 | 0.316 | 4.2% | 23.9% | 10.5% |
| Kyle Stowers | 257 | 0.230 | 0.420 | 0.190 | 0.327 | 0.324 | 10.1% | 29.6% | 33.9% |
| Connor Norby | 244 | 0.214 | 0.348 | 0.133 | 0.306 | 0.282 | 9.4% | 21.6% | 29.4% |
| Owen Caissie | 233 | 0.229 | 0.420 | 0.190 | 0.316 | 0.300 | 14.9% | 24.3% | 33.3% |
| Javier Sanoja | 202 | 0.254 | 0.354 | 0.101 | 0.309 | 0.260 | 1.2% | 21.6% | 11.9% |
| Heriberto Hernandez | 193 | 0.227 | 0.395 | 0.169 | 0.323 | 0.343 | 8.7% | 31.9% | 31.6% |
| Agustín Ramírez | 141 | 0.228 | 0.350 | 0.122 | 0.305 | 0.282 | 5.3% | 27.0% | 30.9% |
| Joe Mack | 137 | 0.250 | 0.387 | 0.137 | 0.314 | 0.312 | 8.7% | 25.0% | 20.5% |
| Graham Pauley | 106 | 0.163 | 0.276 | 0.112 | 0.236 | 0.209 | 4.1% | 16.9% | 19.4% |


## Colorado Rockies Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hunter Goodman | 352 | 0.254 | 0.552 | 0.298 | 0.376 | 0.330 | 17.2% | 29.5% | 31.9% |
| Tj Rumfield | 352 | 0.284 | 0.476 | 0.192 | 0.370 | 0.320 | 6.1% | 21.3% | 17.8% |
| Ezequiel Tovar | 313 | 0.210 | 0.345 | 0.134 | 0.274 | 0.278 | 8.4% | 18.6% | 27.6% |
| Willi Castro | 305 | 0.277 | 0.405 | 0.128 | 0.337 | 0.304 | 6.8% | 23.3% | 27.2% |
| Troy Johnston | 297 | 0.326 | 0.472 | 0.146 | 0.375 | 0.332 | 2.8% | 24.1% | 22.1% |
| Kyle Karros | 281 | 0.254 | 0.389 | 0.135 | 0.338 | 0.332 | 7.1% | 26.8% | 23.6% |
| Jake Mccarthy | 269 | 0.316 | 0.494 | 0.178 | 0.367 | 0.310 | 4.9% | 17.0% | 20.2% |
| Edouard Julien | 239 | 0.238 | 0.340 | 0.102 | 0.316 | 0.340 | 7.8% | 27.2% | 22.3% |
| Tyler Freeman | 215 | 0.274 | 0.366 | 0.091 | 0.329 | 0.318 | 1.2% | 20.0% | 11.6% |
| Mickey Moniak | 193 | 0.263 | 0.536 | 0.274 | 0.358 | 0.317 | 11.6% | 26.1% | 25.7% |
| Brenton Doyle | 145 | 0.227 | 0.295 | 0.068 | 0.283 | 0.248 | 7.0% | 18.4% | 25.6% |
| Brett Sullivan | 128 | 0.227 | 0.429 | 0.202 | 0.299 | 0.264 | 4.1% | 20.8% | 16.3% |


## Bullpen Fatigue Report

### Miami Marlins Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Anthony Bender | 2026-06-27 | 1.1 | 20 |
| Cade Gibson | 2026-06-28 | 0.2 | 7 |
| Calvin Faucher | 2026-06-26 | 1.0 | 10 |
| John King | 2026-06-27 | 1.1 | 13 |
| Lake Bachar | 2026-06-27 | 2.0 | 31 |
| Michael Petersen | 2026-06-26 | 1.0 | 19 |
| Tyler Zuber | 2026-06-27 | 1.0 | 10 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Cade Gibson


### Colorado Rockies Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Antonio Senzatela | 2026-06-26 | 1.0 | 20 |
| Brennan Bernardino | 2026-06-27 | 1.0 | 13 |
| Brennan Bernardino | 2026-06-28 | 0.1 | 3 |
| Jimmy Herget | 2026-06-26 | 0.0 | 3 |
| Jimmy Herget | 2026-06-27 | 0.2 | 9 |
| John Brebbia | 2026-06-26 | 1.0 | 22 |
| Juan Mejia | 2026-06-26 | 1.0 | 13 |
| Juan Mejia | 2026-06-28 | 1.0 | 16 |
| Seth Halvorsen | 2026-06-26 | 1.0 | 10 |
| Seth Halvorsen | 2026-06-28 | 0.2 | 15 |
| Victor Vodnik | 2026-06-27 | 1.1 | 15 |
| Zach Agnos | 2026-06-27 | 0.1 | 25 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Brennan Bernardino, Juan Mejia, Seth Halvorsen



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Otto Lopez | 366 | 0.328 | 0.475 | 0.147 | 0.382 | 6.9% | 29.0% |
| 2 | Xavier Edwards | 363 | 0.297 | 0.429 | 0.132 | 0.360 | 4.7% | 18.6% |
| 3 | Jakob Marsee | 349 | 0.190 | 0.289 | 0.099 | 0.286 | 3.3% | 22.5% |
| 4 | Liam Hicks | 305 | 0.269 | 0.451 | 0.182 | 0.353 | 4.2% | 23.9% |
| 5 | Kyle Stowers | 257 | 0.230 | 0.420 | 0.190 | 0.327 | 10.1% | 29.6% |
| 6 | Connor Norby | 244 | 0.214 | 0.348 | 0.133 | 0.306 | 9.4% | 21.6% |
| 7 | Owen Caissie | 233 | 0.229 | 0.420 | 0.190 | 0.316 | 14.9% | 24.3% |
| 8 | Javier Sanoja | 202 | 0.254 | 0.354 | 0.101 | 0.309 | 1.2% | 21.6% |
| 9 | Heriberto Hernandez | 193 | 0.227 | 0.395 | 0.169 | 0.323 | 8.7% | 31.9% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Hunter Goodman | 352 | 0.254 | 0.552 | 0.298 | 0.376 | 17.2% | 29.5% |
| 2 | Tj Rumfield | 352 | 0.284 | 0.476 | 0.192 | 0.370 | 6.1% | 21.3% |
| 3 | Ezequiel Tovar | 313 | 0.210 | 0.345 | 0.134 | 0.274 | 8.4% | 18.6% |
| 4 | Willi Castro | 305 | 0.277 | 0.405 | 0.128 | 0.337 | 6.8% | 23.3% |
| 5 | Troy Johnston | 297 | 0.326 | 0.472 | 0.146 | 0.375 | 2.8% | 24.1% |
| 6 | Kyle Karros | 281 | 0.254 | 0.389 | 0.135 | 0.338 | 7.1% | 26.8% |
| 7 | Jake Mccarthy | 269 | 0.316 | 0.494 | 0.178 | 0.367 | 4.9% | 17.0% |
| 8 | Edouard Julien | 239 | 0.238 | 0.340 | 0.102 | 0.316 | 7.8% | 27.2% |
| 9 | Tyler Freeman | 215 | 0.274 | 0.366 | 0.091 | 0.329 | 1.2% | 20.0% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6742 |
| Hits Allowed | 1404 |
| Walks/HBP | 684 |
| Strikeouts | 1520 |
| Home Runs Allowed | 162 |
| K Event Rate | 22.5% |
| BB/HBP Event Rate | 10.1% |
| HR Event Rate | 2.4% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7220 |
| Hits Allowed | 1764 |
| Walks/HBP | 666 |
| Strikeouts | 1466 |
| Home Runs Allowed | 232 |
| K Event Rate | 20.3% |
| BB/HBP Event Rate | 9.2% |
| HR Event Rate | 3.2% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: SI, CH, FF, FC, SL, ST
- Home pitcher pitch mix to inspect: No current Statcast sample
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 11. Los Angeles Dodgers @ Athletics

## Game Context

| Field | Value |
| --- | --- |
| Park | Sutter Health Park |
| Time | 2026-06-30T01:40:00Z |
| Away Team | Los Angeles Dodgers |
| Home Team | Athletics |
| Away Probable Pitcher | Eric Lauer |
| Home Probable Pitcher | Gage Jump |


## Away Starting Pitcher: Eric Lauer

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1035 |
| Batted/Result Events | 272 |
| Hits Allowed | 56 |
| Walks | 24 |
| Strikeouts | 42 |
| Home Runs | 16 |
| K Event Rate | 15.4% |
| BB Event Rate | 8.8% |
| HR Event Rate | 5.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-22 | MIN | 7.0 | 0 | 0 | 3 | 2 | 0 |
| 2026-06-15 | LAD | 8.7 | 6 | 1 | 4 | 4 | 1 |
| 2026-06-09 | PIT | 6.7 | 3 | 2 | 0 | 5 | 2 |
| 2026-06-02 | AZ | 6.7 | 5 | 1 | 1 | 1 | 1 |
| 2026-05-26 | LAD | 7.3 | 4 | 1 | 1 | 4 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.2% | 2 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CH | vs R | 16.3% | 169 | 0.235 | 0.275 | 0.039 | 0.269 | 0.325 | 11.1% | 33.9% | 10.5% |
| CU | vs L | 1.6% | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 25.0% | 20.0% |
| CU | vs R | 10.9% | 113 | 0.227 | 0.545 | 0.318 | 0.337 | 0.317 | 10.5% | 25.0% | 12.8% |
| FC | vs L | 3.6% | 37 | 0.222 | 0.556 | 0.333 | 0.322 | 0.261 | 0.0% | 15.4% | 33.3% |
| FC | vs R | 14.7% | 152 | 0.303 | 0.606 | 0.303 | 0.421 | 0.424 | 9.4% | 22.8% | 16.7% |
| FF | vs L | 8.7% | 90 | 0.273 | 0.545 | 0.273 | 0.421 | 0.396 | 13.3% | 22.6% | 16.3% |
| FF | vs R | 36.7% | 380 | 0.182 | 0.466 | 0.284 | 0.300 | 0.354 | 19.1% | 18.1% | 14.7% |
| SL | vs L | 3.9% | 40 | 0.500 | 0.875 | 0.375 | 0.610 | 0.437 | 0.0% | 38.5% | 18.8% |
| SL | vs R | 3.3% | 34 | 0.111 | 0.111 | 0.000 | 0.100 | 0.247 | 0.0% | 13.3% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-22 | 84 | 0 | 3 | 2 | 0 |
| 2026-06-15 | 94 | 6 | 3 | 4 | 1 |
| 2026-06-09 | 89 | 3 | 0 | 5 | 2 |
| 2026-06-02 | 70 | 5 | 1 | 1 | 1 |
| 2026-05-26 | 96 | 4 | 1 | 4 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Carlos Cortes | 11 | 0.333 | 1.000 | 0.667 | 0.509 | 0.627 | 20.0% | 27.8% | 20.0% |
| FC | Zack Gelof | 12 | 0.500 | 1.100 | 0.600 | 0.633 | 0.560 | 18.2% | 22.2% | 26.7% |
| FC | Max Muncy | 32 | 0.276 | 0.724 | 0.448 | 0.439 | 0.421 | 16.7% | 28.6% | 18.5% |
| CU | Tyler Soderstrom | 14 | 0.357 | 0.786 | 0.429 | 0.475 | 0.240 | 8.3% | 40.0% | 24.2% |
| FF | Brent Rooker | 58 | 0.184 | 0.571 | 0.388 | 0.356 | 0.355 | 29.6% | 26.3% | 29.3% |
| FF | Shea Langeliers | 87 | 0.237 | 0.618 | 0.382 | 0.399 | 0.390 | 22.0% | 23.9% | 24.8% |
| FC | Brent Rooker | 8 | 0.500 | 0.875 | 0.375 | 0.588 | 0.398 | 28.6% | 33.3% | 23.8% |
| FF | Max Muncy | 138 | 0.351 | 0.711 | 0.360 | 0.491 | 0.465 | 22.1% | 32.4% | 18.5% |
| FF | Nick Kurtz | 114 | 0.247 | 0.607 | 0.360 | 0.429 | 0.461 | 27.5% | 34.6% | 32.2% |
| FC | Jacob Wilson | 12 | 0.250 | 0.583 | 0.333 | 0.346 | 0.261 | 10.0% | 26.7% | 30.8% |
| FF | Zack Gelof | 68 | 0.226 | 0.516 | 0.290 | 0.356 | 0.279 | 10.3% | 27.2% | 27.6% |
| FC | Tyler Soderstrom | 28 | 0.308 | 0.577 | 0.269 | 0.398 | 0.390 | 4.8% | 46.7% | 10.5% |
| CH | Henry Bolte | 13 | 0.500 | 0.750 | 0.250 | 0.554 | 0.391 | 11.1% | 35.7% | 34.8% |
| FC | Lawrence Butler | 24 | 0.211 | 0.421 | 0.211 | 0.356 | 0.401 | 13.3% | 23.3% | 23.3% |
| FC | Nick Kurtz | 22 | 0.267 | 0.467 | 0.200 | 0.436 | 0.517 | 25.0% | 18.8% | 33.3% |
| CH | Zack Gelof | 17 | 0.267 | 0.467 | 0.200 | 0.412 | 0.390 | 18.2% | 33.3% | 29.4% |
| FF | Tyler Soderstrom | 96 | 0.237 | 0.434 | 0.197 | 0.371 | 0.379 | 12.1% | 24.6% | 16.1% |
| CH | Jeff Mcneil | 38 | 0.189 | 0.378 | 0.189 | 0.251 | 0.286 | 2.9% | 21.3% | 17.5% |
| FF | Henry Bolte | 31 | 0.296 | 0.481 | 0.185 | 0.381 | 0.338 | 25.0% | 23.7% | 33.8% |
| FC | Shea Langeliers | 25 | 0.304 | 0.478 | 0.174 | 0.366 | 0.393 | 15.0% | 24.3% | 30.0% |
| CH | Carlos Cortes | 34 | 0.233 | 0.400 | 0.167 | 0.321 | 0.279 | 8.0% | 15.4% | 32.2% |
| FC | Jeff Mcneil | 24 | 0.381 | 0.524 | 0.143 | 0.431 | 0.278 | 0.0% | 14.6% | 23.6% |
| FF | Lawrence Butler | 74 | 0.194 | 0.328 | 0.134 | 0.280 | 0.318 | 7.1% | 25.2% | 26.6% |
| CH | Brent Rooker | 24 | 0.174 | 0.304 | 0.130 | 0.263 | 0.197 | 18.2% | 21.7% | 44.9% |
| CU | Zack Gelof | 11 | 0.125 | 0.250 | 0.125 | 0.259 | 0.189 | 0.0% | 14.3% | 50.0% |
| CU | Shea Langeliers | 19 | 0.353 | 0.471 | 0.118 | 0.395 | 0.416 | 16.7% | 60.0% | 32.0% |
| FF | Carlos Cortes | 65 | 0.309 | 0.418 | 0.109 | 0.376 | 0.411 | 8.3% | 19.2% | 9.4% |
| CH | Lawrence Butler | 35 | 0.333 | 0.424 | 0.091 | 0.380 | 0.332 | 6.9% | 25.0% | 31.2% |
| FF | Jacob Wilson | 52 | 0.217 | 0.304 | 0.087 | 0.268 | 0.265 | 2.8% | 13.8% | 14.8% |
| CH | Max Muncy | 66 | 0.262 | 0.344 | 0.082 | 0.312 | 0.327 | 8.2% | 28.4% | 29.2% |


## Home Starting Pitcher: Gage Jump

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 548 |
| Batted/Result Events | 138 |
| Hits Allowed | 24 |
| Walks | 10 |
| Strikeouts | 35 |
| Home Runs | 0 |
| K Event Rate | 25.4% |
| BB Event Rate | 7.2% |
| HR Event Rate | 0.0% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | SF | 6.0 | 3 | 0 | 1 | 9 | 0 |
| 2026-06-18 | ATH | 8.3 | 1 | 0 | 3 | 7 | 0 |
| 2026-06-12 | ATH | 7.0 | 5 | 0 | 1 | 6 | 0 |
| 2026-06-07 | HOU | 8.0 | 3 | 0 | 3 | 3 | 0 |
| 2026-06-02 | CHC | 8.3 | 3 | 0 | 2 | 5 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs R | 8.4% | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.165 | 0.0% | 0.0% | 40.0% |
| CU | vs L | 1.5% | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.253 | 0.0% | 40.0% | 14.3% |
| CU | vs R | 10.6% | 58 | 0.125 | 0.125 | 0.000 | 0.200 | 0.190 | 0.0% | 25.0% | 29.6% |
| FF | vs L | 9.9% | 54 | 0.429 | 0.571 | 0.143 | 0.515 | 0.350 | 0.0% | 5.9% | 13.0% |
| FF | vs R | 38.1% | 209 | 0.191 | 0.213 | 0.021 | 0.211 | 0.266 | 2.9% | 14.3% | 20.8% |
| SI | vs L | 0.2% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs R | 0.5% | 3 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 100.0% |
| SL | vs L | 6.6% | 36 | 0.250 | 0.250 | 0.000 | 0.250 | 0.424 | 12.5% | 35.7% | 21.1% |
| SL | vs R | 19.2% | 105 | 0.148 | 0.185 | 0.037 | 0.218 | 0.275 | 0.0% | 23.5% | 21.2% |
| ST | vs L | 3.6% | 20 | 0.286 | 0.286 | 0.000 | 0.225 | 0.133 | 0.0% | 0.0% | 27.3% |
| ST | vs R | 1.5% | 8 | 0.500 | 0.750 | 0.250 | 0.537 | 0.368 | 0.0% | 66.7% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-24 | 97 | 3 | 1 | 9 | 0 |
| 2026-06-18 | 107 | 1 | 3 | 7 | 0 |
| 2026-06-12 | 75 | 5 | 1 | 6 | 0 |
| 2026-06-07 | 96 | 3 | 3 | 3 | 0 |
| 2026-06-02 | 85 | 3 | 1 | 5 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Dalton Rushing | 17 | 0.364 | 1.000 | 0.636 | 0.609 | 0.545 | 28.6% | 25.0% | 28.6% |
| CU | Andy Pages | 17 | 0.400 | 0.867 | 0.467 | 0.506 | 0.282 | 9.1% | 29.4% | 30.8% |
| FF | Mookie Betts | 62 | 0.255 | 0.655 | 0.400 | 0.426 | 0.366 | 18.4% | 24.7% | 5.2% |
| CU | Freddie Freeman | 25 | 0.333 | 0.714 | 0.381 | 0.480 | 0.407 | 15.8% | 31.2% | 10.5% |
| FF | Max Muncy | 138 | 0.351 | 0.711 | 0.360 | 0.491 | 0.465 | 22.1% | 32.4% | 18.5% |
| SL | Dalton Rushing | 22 | 0.286 | 0.619 | 0.333 | 0.393 | 0.397 | 12.5% | 48.1% | 32.5% |
| FF | Freddie Freeman | 112 | 0.344 | 0.656 | 0.312 | 0.456 | 0.407 | 12.2% | 21.5% | 18.4% |
| SL | Teoscar Hernández | 28 | 0.200 | 0.480 | 0.280 | 0.327 | 0.302 | 21.4% | 21.4% | 37.5% |
| CH | Teoscar Hernández | 26 | 0.318 | 0.591 | 0.273 | 0.435 | 0.426 | 13.3% | 22.6% | 30.8% |
| CH | Shohei Ohtani | 47 | 0.357 | 0.619 | 0.262 | 0.446 | 0.405 | 18.5% | 35.6% | 35.7% |
| FF | Dalton Rushing | 63 | 0.269 | 0.500 | 0.231 | 0.406 | 0.333 | 12.5% | 26.1% | 31.0% |
| SL | Shohei Ohtani | 43 | 0.257 | 0.486 | 0.229 | 0.385 | 0.366 | 8.0% | 35.6% | 30.4% |
| SL | Max Muncy | 78 | 0.224 | 0.448 | 0.224 | 0.333 | 0.329 | 16.7% | 34.9% | 37.3% |
| FF | Shohei Ohtani | 97 | 0.232 | 0.451 | 0.220 | 0.361 | 0.437 | 24.6% | 24.3% | 18.6% |
| CH | Will Smith | 16 | 0.286 | 0.500 | 0.214 | 0.381 | 0.394 | 10.0% | 22.2% | 15.2% |
| FF | Teoscar Hernández | 54 | 0.283 | 0.478 | 0.196 | 0.368 | 0.367 | 14.3% | 23.8% | 17.1% |
| CH | Andy Pages | 28 | 0.269 | 0.462 | 0.192 | 0.339 | 0.359 | 9.1% | 21.1% | 23.1% |
| FF | Will Smith | 66 | 0.226 | 0.415 | 0.189 | 0.357 | 0.458 | 20.0% | 27.8% | 14.5% |
| FF | Kyle Tucker | 110 | 0.253 | 0.432 | 0.179 | 0.364 | 0.362 | 10.8% | 23.4% | 18.4% |
| SL | Mookie Betts | 38 | 0.265 | 0.441 | 0.176 | 0.368 | 0.314 | 3.7% | 21.6% | 26.3% |
| FF | Alex Freeland | 63 | 0.302 | 0.472 | 0.170 | 0.383 | 0.367 | 6.8% | 29.2% | 16.7% |
| FF | Miguel Rojas | 47 | 0.302 | 0.465 | 0.163 | 0.347 | 0.364 | 10.5% | 37.1% | 11.0% |
| SL | Kyle Tucker | 40 | 0.182 | 0.333 | 0.152 | 0.285 | 0.291 | 8.7% | 21.0% | 29.7% |
| CU | Will Smith | 8 | 0.143 | 0.286 | 0.143 | 0.356 | 0.140 | 25.0% | 18.2% | 31.2% |
| CU | Teoscar Hernández | 7 | 0.429 | 0.571 | 0.143 | 0.436 | 0.230 | 0.0% | 12.5% | 35.7% |
| CH | Dalton Rushing | 29 | 0.172 | 0.310 | 0.138 | 0.205 | 0.266 | 4.3% | 13.9% | 36.7% |
| FF | Andy Pages | 109 | 0.208 | 0.344 | 0.135 | 0.279 | 0.319 | 8.5% | 22.3% | 21.3% |
| CH | Mookie Betts | 26 | 0.167 | 0.292 | 0.125 | 0.235 | 0.317 | 4.8% | 22.2% | 19.6% |
| SL | Alex Freeland | 22 | 0.111 | 0.222 | 0.111 | 0.241 | 0.333 | 37.5% | 21.1% | 43.2% |
| SL | Freddie Freeman | 45 | 0.175 | 0.275 | 0.100 | 0.249 | 0.383 | 14.8% | 27.6% | 26.2% |


## Los Angeles Dodgers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Andy Pages | 379 | 0.264 | 0.457 | 0.194 | 0.345 | 0.343 | 8.1% | 26.0% | 20.5% |
| Freddie Freeman | 375 | 0.288 | 0.492 | 0.204 | 0.377 | 0.386 | 11.0% | 25.8% | 19.0% |
| Shohei Ohtani | 365 | 0.293 | 0.533 | 0.240 | 0.407 | 0.417 | 17.2% | 31.0% | 25.0% |
| Kyle Tucker | 349 | 0.238 | 0.387 | 0.149 | 0.329 | 0.324 | 6.1% | 24.1% | 22.0% |
| Max Muncy | 312 | 0.267 | 0.507 | 0.241 | 0.382 | 0.370 | 15.3% | 28.4% | 24.0% |
| Mookie Betts | 234 | 0.239 | 0.445 | 0.206 | 0.337 | 0.342 | 9.4% | 25.4% | 12.3% |
| Teoscar Hernández | 224 | 0.286 | 0.482 | 0.196 | 0.367 | 0.339 | 12.9% | 25.6% | 27.5% |
| Alex Freeland | 220 | 0.222 | 0.323 | 0.101 | 0.296 | 0.296 | 6.8% | 25.9% | 25.7% |
| Will Smith | 212 | 0.245 | 0.375 | 0.130 | 0.319 | 0.385 | 13.6% | 22.3% | 15.1% |
| Dalton Rushing | 184 | 0.239 | 0.478 | 0.239 | 0.361 | 0.337 | 11.0% | 26.9% | 31.1% |
| Miguel Rojas | 149 | 0.288 | 0.409 | 0.121 | 0.349 | 0.327 | 6.6% | 28.7% | 16.2% |
| Hyeseong Kim | 148 | 0.265 | 0.326 | 0.061 | 0.308 | 0.304 | 3.1% | 14.3% | 23.3% |


## Athletics Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nick Kurtz | 394 | 0.278 | 0.517 | 0.240 | 0.403 | 0.392 | 18.9% | 33.0% | 32.1% |
| Shea Langeliers | 360 | 0.269 | 0.506 | 0.238 | 0.364 | 0.365 | 14.2% | 28.4% | 24.9% |
| Tyler Soderstrom | 348 | 0.240 | 0.463 | 0.223 | 0.359 | 0.337 | 10.1% | 28.5% | 19.9% |
| Jeff Mcneil | 285 | 0.227 | 0.301 | 0.074 | 0.277 | 0.303 | 0.9% | 18.3% | 14.5% |
| Lawrence Butler | 245 | 0.205 | 0.320 | 0.114 | 0.286 | 0.315 | 7.5% | 25.8% | 26.6% |
| Zack Gelof | 238 | 0.276 | 0.484 | 0.207 | 0.368 | 0.298 | 6.8% | 27.6% | 25.1% |
| Jacob Wilson | 227 | 0.274 | 0.377 | 0.102 | 0.312 | 0.279 | 1.6% | 20.7% | 13.1% |
| Carlos Cortes | 218 | 0.259 | 0.409 | 0.150 | 0.331 | 0.354 | 8.0% | 23.9% | 19.1% |
| Brent Rooker | 215 | 0.214 | 0.411 | 0.198 | 0.316 | 0.314 | 16.5% | 26.9% | 35.2% |
| Max Muncy | 176 | 0.234 | 0.437 | 0.203 | 0.325 | 0.297 | 12.5% | 31.4% | 29.4% |
| Henry Bolte | 164 | 0.291 | 0.383 | 0.092 | 0.347 | 0.309 | 7.6% | 29.0% | 33.0% |
| Darell Hernaiz | 145 | 0.248 | 0.302 | 0.054 | 0.292 | 0.263 | 1.0% | 13.7% | 19.9% |


## Bullpen Fatigue Report

### Los Angeles Dodgers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alex Vesia | 2026-06-27 | 0.2 | 10 |
| Alex Vesia | 2026-06-28 | 0.2 | 12 |
| Brock Stewart | 2026-06-26 | 1.0 | 12 |
| Edgardo Henriquez | 2026-06-26 | 1.0 | 13 |
| Edgardo Henriquez | 2026-06-28 | 1.0 | 11 |
| Jack Dreyer | 2026-06-26 | 1.0 | 7 |
| Jack Dreyer | 2026-06-27 | 1.0 | 27 |
| Jonathan Hernández | 2026-06-26 | 1.0 | 30 |
| Kyle Hurt | 2026-06-27 | 0.1 | 19 |
| Miguel Rojas | 2026-06-27 | 1.0 | 5 |
| Tanner Scott | 2026-06-28 | 1.1 | 17 |
| Will Klein | 2026-06-28 | 1.0 | 22 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Alex Vesia, Edgardo Henriquez, Tanner Scott, Will Klein


### Athletics Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Elvis Alvarado | 2026-06-26 | 1.0 | 15 |
| Elvis Alvarado | 2026-06-28 | 1.0 | 10 |
| Geoff Hartlieb | 2026-06-25 | 2.0 | 25 |
| Geoff Hartlieb | 2026-06-27 | 0.2 | 9 |
| Hogan Harris | 2026-06-26 | 0.2 | 15 |
| José Suarez | 2026-06-28 | 2.0 | 21 |
| Justin Sterner | 2026-06-25 | 0.1 | 7 |
| Justin Sterner | 2026-06-27 | 1.0 | 17 |
| Luis Medina | 2026-06-26 | 1.1 | 38 |
| Mason Barnett | 2026-06-25 | 1.0 | 13 |
| Mason Barnett | 2026-06-27 | 0.2 | 7 |
| Matt Krook | 2026-06-25 | 0.1 | 13 |
| Matt Krook | 2026-06-27 | 0.2 | 12 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Elvis Alvarado, José Suarez



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Andy Pages | 379 | 0.264 | 0.457 | 0.194 | 0.345 | 8.1% | 26.0% |
| 2 | Freddie Freeman | 375 | 0.288 | 0.492 | 0.204 | 0.377 | 11.0% | 25.8% |
| 3 | Shohei Ohtani | 365 | 0.293 | 0.533 | 0.240 | 0.407 | 17.2% | 31.0% |
| 4 | Kyle Tucker | 349 | 0.238 | 0.387 | 0.149 | 0.329 | 6.1% | 24.1% |
| 5 | Max Muncy | 312 | 0.267 | 0.507 | 0.241 | 0.382 | 15.3% | 28.4% |
| 6 | Mookie Betts | 234 | 0.239 | 0.445 | 0.206 | 0.337 | 9.4% | 25.4% |
| 7 | Teoscar Hernández | 224 | 0.286 | 0.482 | 0.196 | 0.367 | 12.9% | 25.6% |
| 8 | Alex Freeland | 220 | 0.222 | 0.323 | 0.101 | 0.296 | 6.8% | 25.9% |
| 9 | Will Smith | 212 | 0.245 | 0.375 | 0.130 | 0.319 | 13.6% | 22.3% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nick Kurtz | 394 | 0.278 | 0.517 | 0.240 | 0.403 | 18.9% | 33.0% |
| 2 | Shea Langeliers | 360 | 0.269 | 0.506 | 0.238 | 0.364 | 14.2% | 28.4% |
| 3 | Tyler Soderstrom | 348 | 0.240 | 0.463 | 0.223 | 0.359 | 10.1% | 28.5% |
| 4 | Jeff Mcneil | 285 | 0.227 | 0.301 | 0.074 | 0.277 | 0.9% | 18.3% |
| 5 | Lawrence Butler | 245 | 0.205 | 0.320 | 0.114 | 0.286 | 7.5% | 25.8% |
| 6 | Zack Gelof | 238 | 0.276 | 0.484 | 0.207 | 0.368 | 6.8% | 27.6% |
| 7 | Jacob Wilson | 227 | 0.274 | 0.377 | 0.102 | 0.312 | 1.6% | 20.7% |
| 8 | Carlos Cortes | 218 | 0.259 | 0.409 | 0.150 | 0.331 | 8.0% | 23.9% |
| 9 | Brent Rooker | 215 | 0.214 | 0.411 | 0.198 | 0.316 | 16.5% | 26.9% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7087 |
| Hits Allowed | 1487 |
| Walks/HBP | 756 |
| Strikeouts | 1616 |
| Home Runs Allowed | 226 |
| K Event Rate | 22.8% |
| BB/HBP Event Rate | 10.7% |
| HR Event Rate | 3.2% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7167 |
| Hits Allowed | 1607 |
| Walks/HBP | 748 |
| Strikeouts | 1573 |
| Home Runs Allowed | 254 |
| K Event Rate | 21.9% |
| BB/HBP Event Rate | 10.4% |
| HR Event Rate | 3.5% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, FC, CH, CU
- Home pitcher pitch mix to inspect: FF, SL, CU, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 12. Los Angeles Angels @ Seattle Mariners

## Game Context

| Field | Value |
| --- | --- |
| Park | T-Mobile Park |
| Time | 2026-06-30T01:40:00Z |
| Away Team | Los Angeles Angels |
| Home Team | Seattle Mariners |
| Away Probable Pitcher | Ryan Johnson |
| Home Probable Pitcher | George Kirby |


## Away Starting Pitcher: Ryan Johnson

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 487 |
| Batted/Result Events | 128 |
| Hits Allowed | 32 |
| Walks | 12 |
| Strikeouts | 24 |
| Home Runs | 5 |
| K Event Rate | 18.8% |
| BB Event Rate | 9.4% |
| HR Event Rate | 3.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | LAA | 6.3 | 1 | 0 | 1 | 8 | 0 |
| 2026-06-18 | ATH | 8.3 | 8 | 2 | 1 | 2 | 2 |
| 2026-05-19 | LAA | 3.7 | 4 | 2 | 1 | 0 | 2 |
| 2026-05-17 | LAA | 3.3 | 3 | 0 | 1 | 2 | 0 |
| 2026-05-15 | LAA | 1.7 | 1 | 0 | 1 | 1 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | vs L | 16.6% | 81 | 0.182 | 0.318 | 0.136 | 0.288 | 0.323 | 0.0% | 23.1% | 17.3% |
| FC | vs R | 14.2% | 69 | 0.267 | 0.467 | 0.200 | 0.338 | 0.286 | 12.5% | 17.6% | 43.8% |
| FF | vs L | 0.6% | 3 | 1.000 | 1.000 | 0.000 | 0.900 | — | 0.0% | 100.0% | 0.0% |
| FS | vs L | 19.7% | 96 | 0.211 | 0.316 | 0.105 | 0.295 | 0.185 | 6.7% | 25.0% | 34.6% |
| FS | vs R | 4.3% | 21 | 0.167 | 0.167 | 0.000 | 0.129 | 0.062 | 0.0% | 0.0% | 50.0% |
| SI | vs L | 12.7% | 62 | 0.312 | 0.625 | 0.312 | 0.412 | 0.281 | 20.0% | 23.1% | 3.4% |
| SI | vs R | 13.8% | 67 | 0.429 | 0.619 | 0.190 | 0.475 | 0.520 | 4.5% | 41.9% | 3.1% |
| ST | vs L | 4.5% | 22 | 0.333 | 0.667 | 0.333 | 0.487 | 0.591 | 0.0% | 0.0% | 40.0% |
| ST | vs R | 13.6% | 66 | 0.273 | 0.636 | 0.364 | 0.377 | 0.354 | 11.1% | 23.5% | 34.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 90 | 1 | 1 | 8 | 0 |
| 2026-06-18 | 89 | 8 | 1 | 2 | 2 |
| 2026-05-19 | 34 | 4 | 1 | 0 | 2 |
| 2026-05-17 | 35 | 3 | 1 | 2 | 0 |
| 2026-05-15 | 21 | 1 | 1 | 1 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Rob Refsnyder | 8 | 0.250 | 1.000 | 0.750 | 0.512 | 0.525 | 25.0% | 22.2% | 18.2% |
| FC | Dominic Canzone | 15 | 0.364 | 0.909 | 0.545 | 0.570 | 0.504 | 20.0% | 17.4% | 17.2% |
| FC | Luke Raley | 28 | 0.333 | 0.875 | 0.542 | 0.559 | 0.427 | 16.7% | 32.3% | 25.5% |
| ST | Colt Emerson | 11 | 0.182 | 0.636 | 0.455 | 0.327 | 0.195 | 14.3% | 28.6% | 26.3% |
| SI | Cal Raleigh | 16 | 0.500 | 0.917 | 0.417 | 0.581 | 0.552 | 36.4% | 27.3% | 13.3% |
| FC | Leo Rivas | 11 | 0.300 | 0.600 | 0.300 | 0.405 | 0.189 | 0.0% | 0.0% | 21.4% |
| ST | Cole Young | 26 | 0.130 | 0.391 | 0.261 | 0.242 | 0.167 | 9.1% | 19.0% | 35.9% |
| FC | Randy Arozarena | 22 | 0.350 | 0.600 | 0.250 | 0.432 | 0.397 | 5.3% | 30.0% | 17.3% |
| SI | Luke Raley | 26 | 0.250 | 0.500 | 0.250 | 0.325 | 0.384 | 21.1% | 27.0% | 25.5% |
| FS | Dominic Canzone | 12 | 0.333 | 0.583 | 0.250 | 0.388 | 0.387 | 22.2% | 37.5% | 40.7% |
| ST | Luke Raley | 16 | 0.250 | 0.500 | 0.250 | 0.316 | 0.196 | 12.5% | 18.2% | 53.8% |
| ST | Josh Naylor | 18 | 0.250 | 0.500 | 0.250 | 0.358 | 0.339 | 9.1% | 43.8% | 33.3% |
| ST | Randy Arozarena | 43 | 0.231 | 0.410 | 0.179 | 0.313 | 0.333 | 9.7% | 23.5% | 16.7% |
| SI | Mitch Garver | 30 | 0.250 | 0.417 | 0.167 | 0.398 | 0.391 | 5.3% | 37.5% | 10.5% |
| FS | J. P. Crawford | 7 | 0.167 | 0.333 | 0.167 | 0.279 | 0.276 | 0.0% | 28.6% | 11.1% |
| FC | Cal Raleigh | 24 | 0.105 | 0.263 | 0.158 | 0.267 | 0.342 | 7.7% | 25.5% | 31.2% |
| SI | Julio Rodríguez | 97 | 0.293 | 0.446 | 0.152 | 0.366 | 0.367 | 8.5% | 33.8% | 8.1% |
| ST | Cal Raleigh | 8 | 0.143 | 0.286 | 0.143 | 0.244 | 0.160 | 0.0% | 10.5% | 28.6% |
| SI | Dominic Canzone | 37 | 0.226 | 0.355 | 0.129 | 0.323 | 0.400 | 7.4% | 34.2% | 14.6% |
| FC | Josh Naylor | 38 | 0.286 | 0.400 | 0.114 | 0.349 | 0.370 | 7.1% | 24.5% | 11.7% |
| FS | Cole Young | 10 | 0.333 | 0.444 | 0.111 | 0.375 | 0.222 | 0.0% | 15.8% | 12.5% |
| ST | Mitch Garver | 10 | 0.222 | 0.333 | 0.111 | 0.285 | 0.234 | 0.0% | 16.7% | 42.9% |
| SI | Colt Emerson | 25 | 0.211 | 0.316 | 0.105 | 0.340 | 0.360 | 0.0% | 19.4% | 16.7% |
| ST | J. P. Crawford | 12 | 0.273 | 0.364 | 0.091 | 0.312 | 0.392 | 0.0% | 21.4% | 21.1% |
| FC | Cole Young | 27 | 0.391 | 0.478 | 0.087 | 0.430 | 0.407 | 0.0% | 19.5% | 19.3% |
| FS | Cal Raleigh | 15 | 0.167 | 0.250 | 0.083 | 0.283 | 0.384 | 22.2% | 23.5% | 23.1% |
| SI | J. P. Crawford | 61 | 0.314 | 0.392 | 0.078 | 0.375 | 0.349 | 4.5% | 28.4% | 5.5% |
| SI | Randy Arozarena | 65 | 0.321 | 0.396 | 0.075 | 0.400 | 0.358 | 0.0% | 25.0% | 19.8% |
| ST | Julio Rodríguez | 38 | 0.206 | 0.265 | 0.059 | 0.258 | 0.250 | 0.0% | 20.9% | 32.9% |
| SI | Josh Naylor | 64 | 0.279 | 0.328 | 0.049 | 0.288 | 0.307 | 0.0% | 29.3% | 6.6% |


## Home Starting Pitcher: George Kirby

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1628 |
| Batted/Result Events | 446 |
| Hits Allowed | 119 |
| Walks | 26 |
| Strikeouts | 92 |
| Home Runs | 10 |
| K Event Rate | 20.6% |
| BB Event Rate | 5.8% |
| HR Event Rate | 2.2% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | PIT | 9.0 | 9 | 0 | 2 | 5 | 0 |
| 2026-06-17 | SEA | 8.3 | 8 | 1 | 0 | 5 | 1 |
| 2026-06-10 | BAL | 9.0 | 7 | 1 | 3 | 10 | 1 |
| 2026-06-03 | SEA | 7.7 | 9 | 0 | 1 | 5 | 0 |
| 2026-05-29 | SEA | 7.3 | 6 | 1 | 1 | 4 | 1 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 5.8% | 95 | 0.217 | 0.435 | 0.217 | 0.358 | 0.440 | 10.0% | 37.0% | 16.7% |
| CH | vs R | 1.6% | 26 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 60.0% | 56.2% |
| FC | vs L | 3.1% | 51 | 0.154 | 0.231 | 0.077 | 0.237 | 0.343 | 0.0% | 30.4% | 14.8% |
| FC | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 100.0% |
| FF | vs L | 17.1% | 278 | 0.282 | 0.451 | 0.169 | 0.340 | 0.309 | 6.7% | 23.3% | 16.5% |
| FF | vs R | 12.9% | 210 | 0.278 | 0.500 | 0.222 | 0.350 | 0.366 | 10.5% | 25.0% | 23.1% |
| KC | vs L | 8.9% | 145 | 0.452 | 0.548 | 0.097 | 0.462 | 0.324 | 0.0% | 34.7% | 17.6% |
| KC | vs R | 0.7% | 12 | 1.000 | 2.000 | 1.000 | 1.250 | 0.373 | 0.0% | 20.0% | 0.0% |
| SI | vs L | 4.5% | 74 | 0.222 | 0.333 | 0.111 | 0.263 | 0.281 | 8.3% | 26.1% | 25.0% |
| SI | vs R | 16.0% | 260 | 0.355 | 0.447 | 0.092 | 0.378 | 0.316 | 6.5% | 38.5% | 9.5% |
| ST | vs L | 11.7% | 190 | 0.216 | 0.314 | 0.098 | 0.286 | 0.222 | 5.9% | 23.3% | 26.2% |
| ST | vs R | 17.5% | 285 | 0.253 | 0.320 | 0.067 | 0.252 | 0.248 | 7.7% | 15.8% | 25.9% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 91 | 9 | 2 | 5 | 0 |
| 2026-06-17 | 92 | 8 | 0 | 5 | 1 |
| 2026-06-10 | 104 | 7 | 3 | 10 | 1 |
| 2026-06-03 | 89 | 9 | 1 | 5 | 0 |
| 2026-05-29 | 87 | 6 | 1 | 4 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Mike Trout | 21 | 0.222 | 0.778 | 0.556 | 0.488 | 0.505 | 45.5% | 29.2% | 19.4% |
| ST | Vaughn Grissom | 15 | 0.357 | 0.857 | 0.500 | 0.517 | 0.462 | 21.4% | 26.3% | 11.5% |
| KC | Jo Adell | 8 | 0.375 | 0.750 | 0.375 | 0.475 | 0.600 | 25.0% | 57.1% | 30.8% |
| FF | Jorge Soler | 73 | 0.219 | 0.562 | 0.344 | 0.368 | 0.279 | 17.9% | 32.5% | 29.5% |
| FF | Zach Neto | 108 | 0.266 | 0.585 | 0.319 | 0.393 | 0.359 | 17.6% | 26.4% | 20.6% |
| ST | Logan O'Hoppe | 10 | 0.100 | 0.400 | 0.300 | 0.200 | 0.171 | 0.0% | 26.1% | 32.4% |
| SI | Yoán Moncada | 21 | 0.190 | 0.476 | 0.286 | 0.276 | 0.271 | 23.1% | 39.1% | 12.9% |
| FF | Jo Adell | 97 | 0.278 | 0.544 | 0.267 | 0.358 | 0.378 | 15.9% | 20.6% | 19.5% |
| FF | Adam Frazier | 39 | 0.233 | 0.500 | 0.267 | 0.371 | 0.282 | 8.3% | 10.3% | 16.2% |
| FF | Vaughn Grissom | 44 | 0.171 | 0.429 | 0.257 | 0.308 | 0.360 | 13.8% | 21.9% | 19.1% |
| FF | Mike Trout | 141 | 0.292 | 0.547 | 0.255 | 0.467 | 0.470 | 22.2% | 25.0% | 14.0% |
| ST | Jo Adell | 40 | 0.333 | 0.583 | 0.250 | 0.420 | 0.290 | 8.3% | 36.2% | 27.5% |
| SI | Zach Neto | 59 | 0.271 | 0.521 | 0.250 | 0.403 | 0.429 | 21.2% | 26.7% | 17.2% |
| KC | Mike Trout | 4 | 0.250 | 0.500 | 0.250 | 0.312 | 0.136 | 0.0% | 25.0% | 42.9% |
| FF | Josh Lowe | 47 | 0.349 | 0.581 | 0.233 | 0.424 | 0.281 | 16.7% | 18.2% | 25.9% |
| ST | Nolan Schanuel | 24 | 0.227 | 0.455 | 0.227 | 0.321 | 0.214 | 5.6% | 18.5% | 28.9% |
| ST | Zach Neto | 34 | 0.156 | 0.375 | 0.219 | 0.249 | 0.198 | 11.1% | 24.2% | 44.8% |
| KC | Logan O'Hoppe | 5 | 0.200 | 0.400 | 0.200 | 0.250 | 0.000 | 0.0% | 25.0% | 54.5% |
| KC | Yoán Moncada | 6 | 0.400 | 0.600 | 0.200 | 0.475 | 0.485 | 0.0% | 50.0% | 55.6% |
| ST | Jorge Soler | 25 | 0.227 | 0.409 | 0.182 | 0.294 | 0.285 | 9.1% | 32.0% | 49.1% |
| SI | Jorge Soler | 56 | 0.273 | 0.455 | 0.182 | 0.370 | 0.377 | 8.1% | 30.3% | 16.7% |
| FF | Nolan Schanuel | 92 | 0.282 | 0.449 | 0.167 | 0.365 | 0.363 | 4.7% | 20.0% | 6.2% |
| ST | Oswald Peraza | 26 | 0.292 | 0.458 | 0.167 | 0.352 | 0.321 | 6.2% | 14.3% | 38.3% |
| ST | Wade Meckler | 6 | 0.167 | 0.333 | 0.167 | 0.208 | 0.129 | 50.0% | 16.7% | 38.5% |
| FF | Logan O'Hoppe | 56 | 0.216 | 0.373 | 0.157 | 0.291 | 0.372 | 14.6% | 28.9% | 16.0% |
| FF | Oswald Peraza | 80 | 0.222 | 0.375 | 0.153 | 0.305 | 0.309 | 8.5% | 20.2% | 20.5% |
| SI | Josh Lowe | 26 | 0.125 | 0.250 | 0.125 | 0.181 | 0.273 | 5.0% | 12.8% | 6.4% |
| FF | Wade Meckler | 43 | 0.278 | 0.389 | 0.111 | 0.357 | 0.346 | 3.8% | 23.3% | 11.8% |
| SI | Jo Adell | 71 | 0.254 | 0.365 | 0.111 | 0.318 | 0.370 | 3.6% | 26.4% | 16.5% |
| SI | Mike Trout | 55 | 0.289 | 0.400 | 0.111 | 0.373 | 0.461 | 13.2% | 38.8% | 10.6% |


## Los Angeles Angels Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Zach Neto | 388 | 0.220 | 0.436 | 0.217 | 0.331 | 0.313 | 13.3% | 23.3% | 31.3% |
| Jo Adell | 373 | 0.252 | 0.407 | 0.155 | 0.306 | 0.322 | 8.6% | 26.7% | 25.4% |
| Mike Trout | 353 | 0.240 | 0.473 | 0.233 | 0.390 | 0.411 | 20.2% | 26.5% | 20.4% |
| Nolan Schanuel | 295 | 0.257 | 0.381 | 0.125 | 0.333 | 0.322 | 2.3% | 19.2% | 16.1% |
| Jorge Soler | 283 | 0.226 | 0.435 | 0.210 | 0.330 | 0.310 | 12.0% | 27.0% | 34.6% |
| Oswald Peraza | 268 | 0.258 | 0.401 | 0.143 | 0.327 | 0.299 | 7.8% | 22.0% | 25.4% |
| Logan O'Hoppe | 213 | 0.225 | 0.335 | 0.110 | 0.284 | 0.276 | 9.9% | 25.4% | 26.1% |
| Vaughn Grissom | 180 | 0.236 | 0.376 | 0.140 | 0.316 | 0.341 | 6.5% | 25.3% | 18.1% |
| Josh Lowe | 164 | 0.221 | 0.383 | 0.162 | 0.283 | 0.270 | 8.4% | 17.3% | 25.7% |
| Yoán Moncada | 147 | 0.202 | 0.306 | 0.105 | 0.295 | 0.270 | 8.6% | 22.7% | 29.4% |
| Wade Meckler | 116 | 0.275 | 0.402 | 0.127 | 0.357 | 0.319 | 6.5% | 18.4% | 22.5% |
| Adam Frazier | 115 | 0.198 | 0.312 | 0.115 | 0.285 | 0.237 | 2.9% | 9.8% | 24.5% |


## Seattle Mariners Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Julio Rodríguez | 382 | 0.255 | 0.427 | 0.172 | 0.332 | 0.350 | 9.4% | 28.9% | 25.8% |
| Cole Young | 365 | 0.251 | 0.378 | 0.127 | 0.309 | 0.329 | 5.6% | 24.5% | 17.5% |
| Josh Naylor | 353 | 0.256 | 0.367 | 0.111 | 0.309 | 0.324 | 4.7% | 26.1% | 16.6% |
| Randy Arozarena | 351 | 0.281 | 0.449 | 0.168 | 0.372 | 0.344 | 8.0% | 24.8% | 25.1% |
| J. P. Crawford | 283 | 0.222 | 0.368 | 0.146 | 0.320 | 0.336 | 7.6% | 22.7% | 15.1% |
| Luke Raley | 249 | 0.250 | 0.513 | 0.263 | 0.364 | 0.357 | 17.7% | 29.1% | 38.8% |
| Cal Raleigh | 247 | 0.172 | 0.321 | 0.149 | 0.267 | 0.296 | 12.1% | 23.6% | 30.3% |
| Dominic Canzone | 228 | 0.281 | 0.557 | 0.276 | 0.384 | 0.382 | 15.7% | 31.1% | 25.9% |
| Leo Rivas | 140 | 0.132 | 0.167 | 0.035 | 0.231 | 0.238 | 2.6% | 9.7% | 23.9% |
| Rob Refsnyder | 136 | 0.127 | 0.212 | 0.085 | 0.200 | 0.249 | 7.2% | 22.6% | 25.2% |
| Mitch Garver | 135 | 0.193 | 0.325 | 0.132 | 0.311 | 0.307 | 7.2% | 28.9% | 35.7% |
| Colt Emerson | 132 | 0.214 | 0.487 | 0.274 | 0.345 | 0.249 | 7.9% | 20.1% | 28.8% |


## Bullpen Fatigue Report

### Los Angeles Angels Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brent Suter | 2026-06-26 | 2.1 | 52 |
| Chase Silseth | 2026-06-27 | 0.1 | 9 |
| José Fermin | 2026-06-26 | 1.1 | 14 |
| José Fermin | 2026-06-28 | 2.0 | 26 |
| Kirby Yates | 2026-06-26 | 1.0 | 13 |
| Kirby Yates | 2026-06-27 | 1.0 | 9 |
| Ryan Zeferjahn | 2026-06-27 | 1.0 | 16 |
| Ryan Zeferjahn | 2026-06-28 | 0.2 | 19 |
| Sam Bachman | 2026-06-27 | 1.0 | 26 |
| Samy Natera Jr. | 2026-06-28 | 1.1 | 24 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** José Fermin, Ryan Zeferjahn, Samy Natera Jr.


### Seattle Mariners Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alex Hoppe | 2026-06-25 | 1.0 | 20 |
| Andrés Muñoz | 2026-06-26 | 1.0 | 15 |
| Eduard Bazardo | 2026-06-25 | 1.0 | 8 |
| Eduard Bazardo | 2026-06-28 | 0.1 | 10 |
| Gabe Speier | 2026-06-25 | 0.1 | 1 |
| Gabe Speier | 2026-06-26 | 1.0 | 9 |
| Gabe Speier | 2026-06-28 | 1.0 | 13 |
| Josh Simpson | 2026-06-28 | 0.2 | 18 |
| José A. Ferrer | 2026-06-26 | 1.0 | 11 |
| José A. Ferrer | 2026-06-27 | 1.0 | 10 |
| Michael Rucker | 2026-06-28 | 0.1 | 21 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Eduard Bazardo, Gabe Speier, Josh Simpson, Michael Rucker



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Zach Neto | 388 | 0.220 | 0.436 | 0.217 | 0.331 | 13.3% | 23.3% |
| 2 | Jo Adell | 373 | 0.252 | 0.407 | 0.155 | 0.306 | 8.6% | 26.7% |
| 3 | Mike Trout | 353 | 0.240 | 0.473 | 0.233 | 0.390 | 20.2% | 26.5% |
| 4 | Nolan Schanuel | 295 | 0.257 | 0.381 | 0.125 | 0.333 | 2.3% | 19.2% |
| 5 | Jorge Soler | 283 | 0.226 | 0.435 | 0.210 | 0.330 | 12.0% | 27.0% |
| 6 | Oswald Peraza | 268 | 0.258 | 0.401 | 0.143 | 0.327 | 7.8% | 22.0% |
| 7 | Logan O'Hoppe | 213 | 0.225 | 0.335 | 0.110 | 0.284 | 9.9% | 25.4% |
| 8 | Vaughn Grissom | 180 | 0.236 | 0.376 | 0.140 | 0.316 | 6.5% | 25.3% |
| 9 | Josh Lowe | 164 | 0.221 | 0.383 | 0.162 | 0.283 | 8.4% | 17.3% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Julio Rodríguez | 382 | 0.255 | 0.427 | 0.172 | 0.332 | 9.4% | 28.9% |
| 2 | Cole Young | 365 | 0.251 | 0.378 | 0.127 | 0.309 | 5.6% | 24.5% |
| 3 | Josh Naylor | 353 | 0.256 | 0.367 | 0.111 | 0.309 | 4.7% | 26.1% |
| 4 | Randy Arozarena | 351 | 0.281 | 0.449 | 0.168 | 0.372 | 8.0% | 24.8% |
| 5 | J. P. Crawford | 283 | 0.222 | 0.368 | 0.146 | 0.320 | 7.6% | 22.7% |
| 6 | Luke Raley | 249 | 0.250 | 0.513 | 0.263 | 0.364 | 17.7% | 29.1% |
| 7 | Cal Raleigh | 247 | 0.172 | 0.321 | 0.149 | 0.267 | 12.1% | 23.6% |
| 8 | Dominic Canzone | 228 | 0.281 | 0.557 | 0.276 | 0.384 | 15.7% | 31.1% |
| 9 | Leo Rivas | 140 | 0.132 | 0.167 | 0.035 | 0.231 | 2.6% | 9.7% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7321 |
| Hits Allowed | 1514 |
| Walks/HBP | 852 |
| Strikeouts | 1750 |
| Home Runs Allowed | 215 |
| K Event Rate | 23.9% |
| BB/HBP Event Rate | 11.6% |
| HR Event Rate | 2.9% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7043 |
| Hits Allowed | 1513 |
| Walks/HBP | 662 |
| Strikeouts | 1637 |
| Home Runs Allowed | 209 |
| K Event Rate | 23.2% |
| BB/HBP Event Rate | 9.4% |
| HR Event Rate | 3.0% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FC, SI, FS, ST
- Home pitcher pitch mix to inspect: FF, ST, SI, KC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 13. San Francisco Giants @ Arizona Diamondbacks

## Game Context

| Field | Value |
| --- | --- |
| Park | Chase Field |
| Time | 2026-06-30T01:40:00Z |
| Away Team | San Francisco Giants |
| Home Team | Arizona Diamondbacks |
| Away Probable Pitcher | Tyler Mahle |
| Home Probable Pitcher | Eduardo Rodriguez |


## Away Starting Pitcher: Tyler Mahle

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1091 |
| Batted/Result Events | 283 |
| Hits Allowed | 66 |
| Walks | 26 |
| Strikeouts | 67 |
| Home Runs | 11 |
| K Event Rate | 23.7% |
| BB Event Rate | 9.2% |
| HR Event Rate | 3.9% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | SF | 6.3 | 2 | 0 | 2 | 4 | 0 |
| 2026-05-26 | SF | 6.7 | 3 | 1 | 3 | 3 | 1 |
| 2026-05-20 | AZ | 7.7 | 8 | 1 | 0 | 6 | 1 |
| 2026-05-15 | ATH | 8.3 | 10 | 1 | 1 | 6 | 1 |
| 2026-05-10 | SF | 8.0 | 5 | 2 | 2 | 8 | 2 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | vs L | 8.0% | 87 | 0.278 | 0.500 | 0.222 | 0.343 | 0.280 | 6.7% | 33.3% | 13.3% |
| FC | vs R | 6.3% | 69 | 0.368 | 0.526 | 0.158 | 0.405 | 0.383 | 5.6% | 18.8% | 5.4% |
| FF | vs L | 25.8% | 281 | 0.196 | 0.392 | 0.196 | 0.287 | 0.301 | 12.9% | 18.3% | 16.8% |
| FF | vs R | 22.0% | 240 | 0.326 | 0.558 | 0.233 | 0.426 | 0.372 | 11.8% | 23.9% | 14.1% |
| FS | vs L | 16.5% | 180 | 0.200 | 0.350 | 0.150 | 0.245 | 0.216 | 2.1% | 18.2% | 20.6% |
| FS | vs R | 8.4% | 92 | 0.280 | 0.440 | 0.160 | 0.339 | 0.431 | 18.8% | 37.5% | 31.4% |
| SI | vs R | 1.6% | 17 | 1.000 | 1.000 | 0.000 | 0.900 | 0.259 | 0.0% | 25.0% | 14.3% |
| SL | vs L | 0.8% | 9 | 0.500 | 1.000 | 0.500 | 0.625 | 0.507 | 0.0% | 20.0% | 0.0% |
| SL | vs R | 10.5% | 115 | 0.281 | 0.438 | 0.156 | 0.403 | 0.397 | 13.0% | 32.3% | 28.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-24 | 70 | 2 | 2 | 4 | 0 |
| 2026-05-26 | 82 | 3 | 3 | 3 | 1 |
| 2026-05-20 | 79 | 8 | 0 | 6 | 1 |
| 2026-05-15 | 90 | 10 | 1 | 6 | 1 |
| 2026-05-10 | 97 | 5 | 2 | 8 | 2 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FS | Adrian Del Castillo | 10 | 0.200 | 0.600 | 0.400 | 0.325 | 0.152 | 0.0% | 22.2% | 15.4% |
| FC | Jorge Barrosa | 11 | 0.300 | 0.700 | 0.400 | 0.395 | 0.206 | 28.6% | 28.6% | 38.5% |
| FC | Nolan Arenado | 19 | 0.375 | 0.750 | 0.375 | 0.508 | 0.413 | 7.7% | 32.0% | 26.3% |
| FC | Ildemaro Vargas | 16 | 0.571 | 0.929 | 0.357 | 0.650 | 0.421 | 7.1% | 18.2% | 5.4% |
| SL | Corbin Carroll | 54 | 0.312 | 0.667 | 0.354 | 0.456 | 0.384 | 16.7% | 38.1% | 23.3% |
| SL | Ryan Waldschmidt | 19 | 0.471 | 0.824 | 0.353 | 0.563 | 0.296 | 8.3% | 41.2% | 35.5% |
| FC | Corbin Carroll | 25 | 0.304 | 0.609 | 0.304 | 0.446 | 0.421 | 10.5% | 35.1% | 24.0% |
| FF | Gabriel Moreno | 69 | 0.264 | 0.547 | 0.283 | 0.404 | 0.401 | 12.2% | 25.5% | 14.8% |
| FC | Jose Fernandez | 14 | 0.364 | 0.636 | 0.273 | 0.450 | 0.371 | 9.1% | 22.7% | 16.1% |
| FF | Corbin Carroll | 113 | 0.211 | 0.478 | 0.267 | 0.373 | 0.356 | 16.9% | 24.1% | 30.7% |
| SL | Alek Thomas | 17 | 0.200 | 0.467 | 0.267 | 0.297 | 0.374 | 18.2% | 23.5% | 38.2% |
| FS | Alek Thomas | 8 | 0.250 | 0.500 | 0.250 | 0.312 | 0.202 | 0.0% | 50.0% | 37.5% |
| FF | Nolan Arenado | 86 | 0.260 | 0.506 | 0.247 | 0.355 | 0.373 | 10.6% | 24.0% | 13.6% |
| FF | Geraldo Perdomo | 120 | 0.312 | 0.548 | 0.237 | 0.432 | 0.382 | 4.7% | 22.5% | 10.0% |
| FF | Ketel Marte | 115 | 0.223 | 0.447 | 0.223 | 0.335 | 0.398 | 16.1% | 31.4% | 7.6% |
| FF | Alek Thomas | 33 | 0.226 | 0.419 | 0.194 | 0.326 | 0.311 | 8.7% | 25.0% | 22.4% |
| FF | Jorge Barrosa | 61 | 0.125 | 0.286 | 0.161 | 0.204 | 0.163 | 2.3% | 17.1% | 20.2% |
| FF | Adrian Del Castillo | 47 | 0.200 | 0.356 | 0.156 | 0.276 | 0.263 | 9.4% | 20.5% | 26.0% |
| FF | Ryan Waldschmidt | 29 | 0.231 | 0.385 | 0.154 | 0.362 | 0.358 | 17.6% | 17.9% | 20.8% |
| SL | Ketel Marte | 40 | 0.231 | 0.385 | 0.154 | 0.275 | 0.366 | 9.4% | 42.6% | 23.3% |
| FS | Ketel Marte | 22 | 0.200 | 0.350 | 0.150 | 0.275 | 0.190 | 0.0% | 32.0% | 40.0% |
| FC | Alek Thomas | 8 | 0.143 | 0.286 | 0.143 | 0.244 | 0.501 | 28.6% | 30.8% | 0.0% |
| SL | Gabriel Moreno | 37 | 0.278 | 0.417 | 0.139 | 0.341 | 0.284 | 3.4% | 24.5% | 22.5% |
| SL | Ildemaro Vargas | 32 | 0.226 | 0.355 | 0.129 | 0.263 | 0.218 | 0.0% | 25.6% | 23.1% |
| FC | Ryan Waldschmidt | 19 | 0.375 | 0.500 | 0.125 | 0.432 | 0.378 | 0.0% | 18.2% | 17.9% |
| SL | Nolan Arenado | 48 | 0.222 | 0.333 | 0.111 | 0.288 | 0.243 | 3.0% | 11.5% | 30.8% |
| SL | Jose Fernandez | 39 | 0.179 | 0.282 | 0.103 | 0.222 | 0.258 | 6.2% | 27.7% | 16.4% |
| FC | Ketel Marte | 14 | 0.308 | 0.385 | 0.077 | 0.332 | 0.313 | 0.0% | 33.3% | 14.7% |
| FC | Gabriel Moreno | 16 | 0.231 | 0.308 | 0.077 | 0.322 | 0.365 | 8.3% | 47.1% | 25.0% |
| SL | Jorge Barrosa | 14 | 0.231 | 0.308 | 0.077 | 0.268 | 0.118 | 0.0% | 12.5% | 29.2% |


## Home Starting Pitcher: Eduardo Rodriguez

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1508 |
| Batted/Result Events | 388 |
| Hits Allowed | 77 |
| Walks | 38 |
| Strikeouts | 70 |
| Home Runs | 9 |
| K Event Rate | 18.0% |
| BB Event Rate | 9.8% |
| HR Event Rate | 2.3% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-23 | STL | 8.3 | 3 | 0 | 3 | 5 | 0 |
| 2026-06-17 | AZ | 9.0 | 6 | 1 | 3 | 5 | 1 |
| 2026-06-12 | CIN | 5.0 | 2 | 1 | 5 | 3 | 1 |
| 2026-06-06 | AZ | 8.3 | 6 | 2 | 1 | 5 | 2 |
| 2026-06-01 | AZ | 8.0 | 5 | 0 | 1 | 3 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 3.1% | 46 | 0.077 | 0.077 | 0.000 | 0.114 | 0.167 | 0.0% | 20.0% | 27.3% |
| CH | vs R | 24.3% | 366 | 0.212 | 0.365 | 0.154 | 0.289 | 0.328 | 5.3% | 17.4% | 18.0% |
| CU | vs L | 5.8% | 87 | 0.100 | 0.100 | 0.000 | 0.090 | 0.194 | 0.0% | 40.0% | 27.8% |
| CU | vs R | 6.6% | 100 | 0.292 | 0.375 | 0.083 | 0.308 | 0.381 | 8.3% | 37.9% | 12.8% |
| FC | vs L | 4.1% | 62 | 0.333 | 0.750 | 0.417 | 0.450 | 0.572 | 27.3% | 29.4% | 14.3% |
| FC | vs R | 8.9% | 134 | 0.269 | 0.538 | 0.269 | 0.366 | 0.371 | 13.6% | 26.4% | 9.5% |
| FF | vs L | 8.6% | 129 | 0.100 | 0.133 | 0.033 | 0.199 | 0.346 | 13.0% | 29.3% | 17.5% |
| FF | vs R | 30.9% | 466 | 0.231 | 0.418 | 0.187 | 0.328 | 0.334 | 10.3% | 19.4% | 20.0% |
| SI | vs L | 5.4% | 81 | 0.476 | 0.571 | 0.095 | 0.483 | 0.456 | 0.0% | 31.4% | 2.4% |
| SI | vs R | 2.4% | 36 | 0.000 | 0.000 | 0.000 | 0.215 | 0.281 | 0.0% | 30.0% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-23 | 95 | 3 | 3 | 5 | 0 |
| 2026-06-17 | 100 | 6 | 3 | 5 | 1 |
| 2026-06-12 | 85 | 2 | 5 | 3 | 1 |
| 2026-06-06 | 92 | 6 | 1 | 5 | 2 |
| 2026-06-01 | 96 | 5 | 1 | 3 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Matt Chapman | 14 | 0.357 | 1.000 | 0.643 | 0.554 | 0.455 | 16.7% | 26.1% | 14.3% |
| CH | Casey Schmitt | 23 | 0.435 | 1.000 | 0.565 | 0.598 | 0.512 | 21.1% | 28.1% | 26.5% |
| FC | Daniel Susac | 7 | 0.429 | 0.857 | 0.429 | 0.543 | 0.390 | 16.7% | 33.3% | 28.6% |
| FF | Bryce Eldridge | 56 | 0.295 | 0.705 | 0.409 | 0.476 | 0.507 | 25.7% | 34.6% | 11.6% |
| CU | Bryce Eldridge | 12 | 0.250 | 0.625 | 0.375 | 0.475 | 0.261 | 0.0% | 14.3% | 18.2% |
| FF | Willy Adames | 98 | 0.237 | 0.602 | 0.366 | 0.364 | 0.329 | 11.8% | 26.7% | 22.6% |
| FC | Casey Schmitt | 26 | 0.455 | 0.818 | 0.364 | 0.538 | 0.376 | 5.0% | 26.0% | 19.0% |
| FC | Rafael Devers | 30 | 0.423 | 0.731 | 0.308 | 0.497 | 0.324 | 4.8% | 34.4% | 27.8% |
| FF | Rafael Devers | 142 | 0.208 | 0.454 | 0.246 | 0.312 | 0.297 | 17.4% | 28.3% | 36.5% |
| FC | Jung Hoo Lee | 22 | 0.238 | 0.476 | 0.238 | 0.318 | 0.326 | 5.3% | 16.2% | 16.3% |
| FF | Drew Gilbert | 67 | 0.315 | 0.537 | 0.222 | 0.427 | 0.361 | 2.2% | 21.8% | 16.0% |
| FF | Jung Hoo Lee | 106 | 0.398 | 0.602 | 0.204 | 0.445 | 0.341 | 4.4% | 22.1% | 7.9% |
| FF | Harrison Bader | 34 | 0.133 | 0.333 | 0.200 | 0.253 | 0.254 | 4.5% | 21.6% | 20.0% |
| FC | Willy Adames | 33 | 0.267 | 0.467 | 0.200 | 0.332 | 0.295 | 11.1% | 28.9% | 23.8% |
| FF | Heliot Ramos | 43 | 0.250 | 0.425 | 0.175 | 0.337 | 0.321 | 13.0% | 14.1% | 25.8% |
| CU | Casey Schmitt | 14 | 0.154 | 0.308 | 0.154 | 0.229 | 0.265 | 0.0% | 4.8% | 34.4% |
| CH | Luis Arráez | 36 | 0.152 | 0.303 | 0.152 | 0.194 | 0.239 | 2.9% | 14.5% | 4.9% |
| CU | Luis Arráez | 21 | 0.450 | 0.600 | 0.150 | 0.469 | 0.315 | 0.0% | 8.0% | 0.0% |
| CH | Matt Chapman | 33 | 0.286 | 0.429 | 0.143 | 0.367 | 0.374 | 10.5% | 38.2% | 22.0% |
| FC | Drew Gilbert | 24 | 0.143 | 0.286 | 0.143 | 0.246 | 0.327 | 5.0% | 30.0% | 8.1% |
| FC | Patrick Bailey | 15 | 0.214 | 0.357 | 0.143 | 0.273 | 0.449 | 8.3% | 45.5% | 22.6% |
| FF | Luis Arráez | 134 | 0.352 | 0.488 | 0.136 | 0.370 | 0.310 | 0.0% | 15.2% | 8.4% |
| CH | Bryce Eldridge | 23 | 0.273 | 0.409 | 0.136 | 0.311 | 0.415 | 20.0% | 21.7% | 35.9% |
| CU | Jung Hoo Lee | 22 | 0.273 | 0.409 | 0.136 | 0.293 | 0.287 | 0.0% | 28.1% | 9.5% |
| CH | Drew Gilbert | 24 | 0.217 | 0.348 | 0.130 | 0.298 | 0.278 | 0.0% | 18.5% | 25.0% |
| FC | Matt Chapman | 27 | 0.167 | 0.292 | 0.125 | 0.259 | 0.263 | 9.1% | 22.7% | 13.1% |
| FF | Daniel Susac | 26 | 0.200 | 0.320 | 0.120 | 0.221 | 0.214 | 5.3% | 16.3% | 13.3% |
| FC | Bryce Eldridge | 18 | 0.176 | 0.294 | 0.118 | 0.189 | 0.197 | 0.0% | 24.1% | 25.0% |
| CH | Rafael Devers | 37 | 0.216 | 0.324 | 0.108 | 0.232 | 0.349 | 12.5% | 36.5% | 16.4% |
| FF | Casey Schmitt | 94 | 0.247 | 0.348 | 0.101 | 0.282 | 0.339 | 10.8% | 26.1% | 16.5% |


## San Francisco Giants Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rafael Devers | 359 | 0.243 | 0.453 | 0.210 | 0.323 | 0.302 | 11.2% | 28.4% | 28.1% |
| Matt Chapman | 356 | 0.248 | 0.400 | 0.152 | 0.336 | 0.292 | 7.4% | 23.5% | 20.5% |
| Willy Adames | 354 | 0.230 | 0.429 | 0.199 | 0.312 | 0.287 | 9.4% | 24.9% | 27.9% |
| Luis Arráez | 351 | 0.324 | 0.444 | 0.121 | 0.352 | 0.302 | 0.3% | 13.1% | 6.9% |
| Casey Schmitt | 327 | 0.289 | 0.500 | 0.211 | 0.351 | 0.358 | 11.7% | 28.1% | 20.4% |
| Jung Hoo Lee | 317 | 0.328 | 0.476 | 0.149 | 0.368 | 0.325 | 3.0% | 20.5% | 10.8% |
| Drew Gilbert | 204 | 0.242 | 0.371 | 0.129 | 0.317 | 0.296 | 2.1% | 22.2% | 19.6% |
| Heliot Ramos | 192 | 0.263 | 0.419 | 0.156 | 0.320 | 0.327 | 12.6% | 25.0% | 24.5% |
| Bryce Eldridge | 171 | 0.274 | 0.473 | 0.199 | 0.368 | 0.374 | 12.3% | 29.4% | 22.1% |
| Daniel Susac | 128 | 0.270 | 0.357 | 0.087 | 0.293 | 0.286 | 5.6% | 17.3% | 23.6% |
| Harrison Bader | 114 | 0.167 | 0.352 | 0.185 | 0.244 | 0.272 | 8.2% | 25.0% | 30.6% |
| Patrick Bailey | 102 | 0.160 | 0.191 | 0.032 | 0.198 | 0.282 | 4.3% | 25.6% | 24.6% |


## Arizona Diamondbacks Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ketel Marte | 357 | 0.262 | 0.468 | 0.206 | 0.344 | 0.374 | 11.6% | 34.7% | 18.8% |
| Corbin Carroll | 356 | 0.269 | 0.522 | 0.253 | 0.381 | 0.357 | 13.0% | 30.6% | 26.9% |
| Geraldo Perdomo | 350 | 0.247 | 0.362 | 0.115 | 0.337 | 0.334 | 3.2% | 21.5% | 10.9% |
| Nolan Arenado | 313 | 0.241 | 0.399 | 0.158 | 0.320 | 0.300 | 6.4% | 22.6% | 20.7% |
| Ildemaro Vargas | 287 | 0.257 | 0.410 | 0.153 | 0.326 | 0.309 | 3.8% | 26.4% | 12.4% |
| Gabriel Moreno | 230 | 0.284 | 0.472 | 0.188 | 0.377 | 0.370 | 9.9% | 27.1% | 15.6% |
| Jose Fernandez | 178 | 0.253 | 0.349 | 0.096 | 0.301 | 0.276 | 3.9% | 24.7% | 23.3% |
| Adrian Del Castillo | 157 | 0.188 | 0.299 | 0.111 | 0.257 | 0.260 | 6.1% | 20.3% | 24.8% |
| Jorge Barrosa | 141 | 0.210 | 0.427 | 0.218 | 0.311 | 0.211 | 7.9% | 18.1% | 24.8% |
| Lourdes Gurriel | 140 | 0.219 | 0.289 | 0.070 | 0.253 | 0.276 | 4.8% | 21.0% | 21.6% |
| Ryan Waldschmidt | 131 | 0.273 | 0.380 | 0.107 | 0.327 | 0.289 | 7.6% | 22.1% | 29.0% |
| Alek Thomas | 117 | 0.193 | 0.394 | 0.202 | 0.280 | 0.292 | 9.9% | 27.6% | 23.7% |


## Bullpen Fatigue Report

### San Francisco Giants Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Adrian Houser | 2026-06-26 | 2.1 | 35 |
| Caleb Kilian | 2026-06-25 | 0.2 | 23 |
| Caleb Kilian | 2026-06-28 | 1.0 | 18 |
| Dylan Smith | 2026-06-25 | 1.0 | 25 |
| Erik Miller | 2026-06-25 | 0.1 | 12 |
| Matt Gage | 2026-06-25 | 0.1 | 10 |
| Matt Gage | 2026-06-26 | 0.2 | 12 |
| Ryan Walker | 2026-06-25 | 0.2 | 7 |
| Ryan Walker | 2026-06-27 | 1.0 | 23 |
| Sam Hentges | 2026-06-26 | 0.2 | 11 |
| Sam Hentges | 2026-06-27 | 1.0 | 11 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Caleb Kilian


### Arizona Diamondbacks Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Drey Jameson | 2026-06-28 | 1.0 | 14 |
| Jonathan Loáisiga | 2026-06-28 | 1.0 | 12 |
| Juan Burgos | 2026-06-26 | 1.1 | 20 |
| Juan Morillo | 2026-06-27 | 1.0 | 23 |
| Kevin Ginkel | 2026-06-27 | 1.0 | 13 |
| Taylor Clarke | 2026-06-27 | 1.0 | 6 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Drey Jameson, Jonathan Loáisiga



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Rafael Devers | 359 | 0.243 | 0.453 | 0.210 | 0.323 | 11.2% | 28.4% |
| 2 | Matt Chapman | 356 | 0.248 | 0.400 | 0.152 | 0.336 | 7.4% | 23.5% |
| 3 | Willy Adames | 354 | 0.230 | 0.429 | 0.199 | 0.312 | 9.4% | 24.9% |
| 4 | Luis Arráez | 351 | 0.324 | 0.444 | 0.121 | 0.352 | 0.3% | 13.1% |
| 5 | Casey Schmitt | 327 | 0.289 | 0.500 | 0.211 | 0.351 | 11.7% | 28.1% |
| 6 | Jung Hoo Lee | 317 | 0.328 | 0.476 | 0.149 | 0.368 | 3.0% | 20.5% |
| 7 | Drew Gilbert | 204 | 0.242 | 0.371 | 0.129 | 0.317 | 2.1% | 22.2% |
| 8 | Heliot Ramos | 192 | 0.263 | 0.419 | 0.156 | 0.320 | 12.6% | 25.0% |
| 9 | Bryce Eldridge | 171 | 0.274 | 0.473 | 0.199 | 0.368 | 12.3% | 29.4% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Ketel Marte | 357 | 0.262 | 0.468 | 0.206 | 0.344 | 11.6% | 34.7% |
| 2 | Corbin Carroll | 356 | 0.269 | 0.522 | 0.253 | 0.381 | 13.0% | 30.6% |
| 3 | Geraldo Perdomo | 350 | 0.247 | 0.362 | 0.115 | 0.337 | 3.2% | 21.5% |
| 4 | Nolan Arenado | 313 | 0.241 | 0.399 | 0.158 | 0.320 | 6.4% | 22.6% |
| 5 | Ildemaro Vargas | 287 | 0.257 | 0.410 | 0.153 | 0.326 | 3.8% | 26.4% |
| 6 | Gabriel Moreno | 230 | 0.284 | 0.472 | 0.188 | 0.377 | 9.9% | 27.1% |
| 7 | Jose Fernandez | 178 | 0.253 | 0.349 | 0.096 | 0.301 | 3.9% | 24.7% |
| 8 | Adrian Del Castillo | 157 | 0.188 | 0.299 | 0.111 | 0.257 | 6.1% | 20.3% |
| 9 | Jorge Barrosa | 141 | 0.210 | 0.427 | 0.218 | 0.311 | 7.9% | 18.1% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6792 |
| Hits Allowed | 1528 |
| Walks/HBP | 605 |
| Strikeouts | 1404 |
| Home Runs Allowed | 187 |
| K Event Rate | 20.7% |
| BB/HBP Event Rate | 8.9% |
| HR Event Rate | 2.8% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 6896 |
| Hits Allowed | 1520 |
| Walks/HBP | 631 |
| Strikeouts | 1327 |
| Home Runs Allowed | 203 |
| K Event Rate | 19.2% |
| BB/HBP Event Rate | 9.2% |
| HR Event Rate | 2.9% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, FS, FC, SL
- Home pitcher pitch mix to inspect: FF, CH, FC, CU
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.

