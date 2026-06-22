# MLB-LAB V5.1 Pitch Matchup Engine

Date: 2026-06-21

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
| 1 | Cincinnati Reds @ New York Yankees | Yankee Stadium | Chase Burns | Elmer Rodríguez |
| 2 | Milwaukee Brewers @ Atlanta Braves | Truist Park | Robert Gasser | Bryce Elder |
| 3 | Washington Nationals @ Tampa Bay Rays | Tropicana Field | Andrew Alvarez | Nick Martinez |
| 4 | Chicago White Sox @ Detroit Tigers | Comerica Park | Davis Martin | Keider Montero |
| 5 | San Francisco Giants @ Miami Marlins | loanDepot park | Logan Webb | Ryan Gusto |
| 6 | Cleveland Guardians @ Houston Astros | Daikin Park | Slade Cecconi | Kai-Wei Teng |
| 7 | St. Louis Cardinals @ Kansas City Royals | Kauffman Stadium | Dustin May | Stephen Kolek |
| 8 | San Diego Padres @ Texas Rangers | Globe Life Field | Wandy Peralta | Nathan Eovaldi |
| 9 | Pittsburgh Pirates @ Colorado Rockies | Coors Field | Jared Jones | Michael Lorenzen |
| 10 | Minnesota Twins @ Arizona Diamondbacks | Chase Field | Mike Paredes | Jose Cabrera |
| 11 | Los Angeles Angels @ Athletics | Sutter Health Park | Reid Detmers | Jack Perkins |
| 12 | Baltimore Orioles @ Los Angeles Dodgers | UNIQLO Field at Dodger Stadium | Brandon Young | Emmet Sheehan |
| 13 | Boston Red Sox @ Seattle Mariners | T-Mobile Park | Payton Tolle | Logan Gilbert |
| 14 | New York Mets @ Philadelphia Phillies | Citizens Bank Park | David Peterson | Zack Wheeler |
| 15 | Toronto Blue Jays @ Chicago Cubs | Wrigley Field | Dylan Cease | Shota Imanaga |

---

# Full Game Breakdown Cards

---

# 1. Cincinnati Reds @ New York Yankees

## Game Context

| Field | Value |
| --- | --- |
| Park | Yankee Stadium |
| Time | 2026-06-21T17:35:00Z |
| Away Team | Cincinnati Reds |
| Home Team | New York Yankees |
| Away Probable Pitcher | Chase Burns |
| Home Probable Pitcher | Elmer Rodríguez |


## Away Starting Pitcher: Chase Burns

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1409 |
| Batted/Result Events | 348 |
| Hits Allowed | 63 |
| Walks | 27 |
| Strikeouts | 104 |
| Home Runs | 10 |
| K Event Rate | 29.9% |
| BB Event Rate | 7.8% |
| HR Event Rate | 2.9% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 6.2% | 88 | 0.562 | 1.062 | 0.500 | 0.688 | 0.432 | 21.4% | 21.7% | 28.9% |
| CH | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CU | vs L | 0.2% | 3 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CU | vs R | 0.1% | 2 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 100.0% |
| FF | vs L | 35.3% | 497 | 0.213 | 0.394 | 0.181 | 0.334 | 0.307 | 6.9% | 15.1% | 16.6% |
| FF | vs R | 21.9% | 309 | 0.194 | 0.284 | 0.090 | 0.241 | 0.321 | 10.9% | 23.0% | 18.5% |
| SL | vs L | 17.4% | 245 | 0.118 | 0.265 | 0.147 | 0.194 | 0.145 | 9.5% | 25.5% | 51.5% |
| SL | vs R | 18.7% | 264 | 0.171 | 0.276 | 0.105 | 0.203 | 0.234 | 10.9% | 40.0% | 49.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 100 | 4 | 3 | 7 | 0 |
| 2026-06-09 | 105 | 6 | 2 | 7 | 0 |
| 2026-06-03 | 98 | 4 | 1 | 9 | 1 |
| 2026-05-26 | 90 | 4 | 2 | 8 | 1 |
| 2026-05-19 | 86 | 3 | 0 | 9 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF | Ben Rice | 74 | 0.371 | 1.016 | 0.645 | 0.604 | 0.572 | 34.0% | 38.7% | 16.3% |
| SL | Giancarlo Stanton | 14 | 0.385 | 1.000 | 0.615 | 0.579 | 0.531 | 42.9% | 30.8% | 43.3% |
| FF | Paul Goldschmidt | 63 | 0.389 | 0.944 | 0.556 | 0.561 | 0.445 | 23.9% | 29.1% | 17.2% |
| SL | Cody Bellinger | 39 | 0.375 | 0.875 | 0.500 | 0.558 | 0.460 | 16.7% | 27.5% | 16.9% |
| FF | Aaron Judge | 54 | 0.233 | 0.558 | 0.326 | 0.404 | 0.467 | 26.9% | 24.7% | 22.9% |
| SL | Trent Grisham | 23 | 0.158 | 0.474 | 0.316 | 0.374 | 0.283 | 18.2% | 30.0% | 34.4% |
| SL | José Caballero | 37 | 0.314 | 0.629 | 0.314 | 0.412 | 0.360 | 3.4% | 20.0% | 32.9% |
| SL | Ben Rice | 49 | 0.350 | 0.625 | 0.275 | 0.467 | 0.400 | 13.3% | 41.5% | 33.3% |
| SL | Jazz Chisholm | 45 | 0.225 | 0.500 | 0.275 | 0.347 | 0.294 | 11.1% | 33.3% | 37.7% |
| SL | Amed Rosario | 13 | 0.308 | 0.538 | 0.231 | 0.362 | 0.381 | 12.5% | 22.7% | 33.3% |
| FF | Austin Wells | 58 | 0.213 | 0.426 | 0.213 | 0.339 | 0.327 | 7.9% | 25.9% | 17.9% |
| FF | Ryan Mcmahon | 66 | 0.295 | 0.475 | 0.180 | 0.351 | 0.374 | 14.0% | 19.6% | 18.3% |
| FF | J. C. Escarra | 38 | 0.353 | 0.529 | 0.176 | 0.438 | 0.340 | 9.4% | 34.5% | 8.1% |
| FF | Trent Grisham | 107 | 0.239 | 0.409 | 0.170 | 0.351 | 0.417 | 16.2% | 35.8% | 10.8% |
| FF | Jazz Chisholm | 96 | 0.190 | 0.333 | 0.143 | 0.283 | 0.294 | 6.9% | 27.6% | 20.6% |
| FF | Cody Bellinger | 110 | 0.241 | 0.379 | 0.138 | 0.344 | 0.364 | 3.9% | 16.7% | 14.1% |
| SL | Aaron Judge | 41 | 0.189 | 0.324 | 0.135 | 0.293 | 0.270 | 16.0% | 33.3% | 34.4% |
| FF | José Caballero | 72 | 0.227 | 0.333 | 0.106 | 0.281 | 0.249 | 4.9% | 19.6% | 26.5% |
| FF | Amed Rosario | 34 | 0.138 | 0.207 | 0.069 | 0.209 | 0.228 | 9.1% | 13.3% | 17.7% |
| FF | Giancarlo Stanton | 30 | 0.148 | 0.148 | 0.000 | 0.167 | 0.213 | 23.5% | 15.8% | 28.8% |
| SL | Ryan Mcmahon | 29 | 0.185 | 0.185 | 0.000 | 0.203 | 0.245 | 6.7% | 42.3% | 40.8% |
| SL | Paul Goldschmidt | 33 | 0.367 | 0.367 | 0.000 | 0.364 | 0.290 | 0.0% | 21.7% | 27.9% |
| SL | J. C. Escarra | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.168 | 12.5% | 30.8% | 37.5% |
| SL | Austin Wells | 28 | 0.074 | 0.074 | 0.000 | 0.089 | 0.221 | 0.0% | 38.7% | 43.9% |


## Home Starting Pitcher: Elmer Rodríguez

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 238 |
| Batted/Result Events | 64 |
| Hits Allowed | 15 |
| Walks | 9 |
| Strikeouts | 6 |
| Home Runs | 0 |
| K Event Rate | 9.4% |
| BB Event Rate | 14.1% |
| HR Event Rate | 0.0% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 10.1% | 24 | 0.333 | 0.500 | 0.167 | 0.407 | 0.265 | 0.0% | 25.0% | 27.3% |
| CH | vs R | 0.8% | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.519 | 0.0% | 100.0% | 0.0% |
| CU | vs L | 9.2% | 22 | 0.500 | 0.500 | 0.000 | 0.450 | 0.133 | 0.0% | 0.0% | 33.3% |
| CU | vs R | 1.3% | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.089 | 0.0% | 0.0% | 50.0% |
| FC | vs L | 0.4% | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 0.0% |
| FF | vs L | 20.2% | 48 | 0.222 | 0.222 | 0.000 | 0.354 | 0.481 | 12.5% | 33.3% | 23.5% |
| FF | vs R | 2.1% | 5 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs L | 15.1% | 36 | 0.000 | 0.000 | 0.000 | 0.280 | 0.537 | 20.0% | 36.4% | 26.7% |
| SI | vs R | 26.5% | 63 | 0.444 | 0.500 | 0.056 | 0.460 | 0.366 | 0.0% | 24.0% | 10.7% |
| SL | vs L | 0.4% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SL | vs R | 13.9% | 33 | 0.250 | 0.250 | 0.000 | 0.225 | 0.278 | 0.0% | 14.3% | 50.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-05-17 | 64 | 5 | 1 | 1 | 0 |
| 2026-05-05 | 94 | 6 | 4 | 2 | 0 |
| 2026-04-29 | 80 | 4 | 4 | 3 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Jj Bleday | 13 | 0.455 | 1.364 | 0.909 | 0.735 | 0.604 | 30.0% | 78.6% | 37.5% |
| SL | Nathaniel Lowe | 13 | 0.308 | 0.769 | 0.462 | 0.446 | 0.121 | 12.5% | 23.1% | 25.0% |
| SI | Tyler Stephenson | 40 | 0.394 | 0.818 | 0.424 | 0.565 | 0.551 | 26.9% | 38.1% | 16.9% |
| FF | Jj Bleday | 50 | 0.225 | 0.600 | 0.375 | 0.383 | 0.504 | 22.9% | 24.7% | 8.7% |
| SL | Jj Bleday | 24 | 0.318 | 0.682 | 0.364 | 0.442 | 0.325 | 5.6% | 32.1% | 29.3% |
| FF | Elly De La Cruz | 98 | 0.258 | 0.607 | 0.348 | 0.399 | 0.432 | 29.5% | 37.6% | 15.4% |
| CH | Nathaniel Lowe | 28 | 0.269 | 0.615 | 0.346 | 0.391 | 0.363 | 15.0% | 29.6% | 20.0% |
| SL | Elly De La Cruz | 21 | 0.190 | 0.524 | 0.333 | 0.336 | 0.361 | 15.4% | 42.9% | 25.7% |
| CU | Eugenio Suárez | 11 | 0.300 | 0.600 | 0.300 | 0.409 | 0.495 | 20.0% | 16.7% | 35.0% |
| CH | Spencer Steer | 33 | 0.194 | 0.484 | 0.290 | 0.339 | 0.237 | 15.0% | 27.0% | 27.9% |
| FF | Sal Stewart | 95 | 0.312 | 0.597 | 0.286 | 0.463 | 0.384 | 18.8% | 30.3% | 32.4% |
| CU | Tj Friedl | 13 | 0.182 | 0.455 | 0.273 | 0.277 | 0.293 | 10.0% | 28.6% | 27.3% |
| FF | Spencer Steer | 75 | 0.200 | 0.462 | 0.262 | 0.332 | 0.362 | 24.4% | 27.3% | 26.1% |
| SI | Ke'Bryan Hayes | 35 | 0.219 | 0.469 | 0.250 | 0.323 | 0.401 | 15.4% | 41.5% | 10.9% |
| SI | Dane Myers | 28 | 0.500 | 0.727 | 0.227 | 0.632 | 0.565 | 11.8% | 28.1% | 2.6% |
| CU | Matt Mclain | 16 | 0.071 | 0.286 | 0.214 | 0.212 | 0.302 | 9.1% | 46.7% | 26.1% |
| CH | Sal Stewart | 29 | 0.333 | 0.542 | 0.208 | 0.431 | 0.394 | 6.7% | 24.1% | 30.4% |
| SL | Sal Stewart | 46 | 0.154 | 0.359 | 0.205 | 0.287 | 0.259 | 10.7% | 19.2% | 27.0% |
| SI | Sal Stewart | 79 | 0.232 | 0.435 | 0.203 | 0.335 | 0.440 | 16.7% | 29.3% | 14.5% |
| CH | Jj Bleday | 45 | 0.225 | 0.425 | 0.200 | 0.322 | 0.351 | 9.4% | 30.0% | 33.7% |
| SL | Matt Mclain | 51 | 0.170 | 0.362 | 0.191 | 0.277 | 0.314 | 12.1% | 24.5% | 28.2% |
| SI | Elly De La Cruz | 35 | 0.250 | 0.438 | 0.188 | 0.309 | 0.307 | 15.0% | 33.3% | 18.2% |
| SI | Spencer Steer | 84 | 0.221 | 0.397 | 0.176 | 0.337 | 0.384 | 10.9% | 26.9% | 14.6% |
| SI | Matt Mclain | 59 | 0.275 | 0.451 | 0.176 | 0.367 | 0.378 | 9.5% | 23.4% | 11.1% |
| SL | Spencer Steer | 33 | 0.226 | 0.387 | 0.161 | 0.288 | 0.363 | 8.7% | 25.7% | 27.7% |
| SI | Jj Bleday | 30 | 0.360 | 0.520 | 0.160 | 0.465 | 0.369 | 4.8% | 39.5% | 17.0% |
| FF | Blake Dunn | 31 | 0.280 | 0.440 | 0.160 | 0.384 | 0.342 | 6.2% | 16.7% | 17.3% |
| SI | Tj Friedl | 33 | 0.321 | 0.464 | 0.143 | 0.394 | 0.398 | 4.5% | 38.7% | 4.9% |
| CH | Eugenio Suárez | 16 | 0.214 | 0.357 | 0.143 | 0.356 | 0.163 | 0.0% | 25.0% | 45.0% |
| CU | Blake Dunn | 8 | 0.143 | 0.286 | 0.143 | 0.244 | 0.264 | 0.0% | 0.0% | 25.0% |


## Cincinnati Reds Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sal Stewart | 352 | 0.254 | 0.465 | 0.211 | 0.359 | 0.366 | 14.7% | 25.1% | 23.8% |
| Spencer Steer | 308 | 0.242 | 0.440 | 0.198 | 0.340 | 0.358 | 14.1% | 27.4% | 21.9% |
| Matt Mclain | 303 | 0.220 | 0.386 | 0.167 | 0.318 | 0.327 | 10.7% | 23.2% | 23.1% |
| Elly De La Cruz | 280 | 0.277 | 0.514 | 0.237 | 0.377 | 0.361 | 16.3% | 35.1% | 27.5% |
| Tyler Stephenson | 228 | 0.210 | 0.340 | 0.130 | 0.295 | 0.317 | 11.4% | 25.4% | 26.5% |
| Jj Bleday | 212 | 0.265 | 0.591 | 0.326 | 0.412 | 0.381 | 12.1% | 32.1% | 24.2% |
| Nathaniel Lowe | 203 | 0.263 | 0.503 | 0.240 | 0.380 | 0.372 | 12.7% | 22.5% | 16.6% |
| Eugenio Suárez | 202 | 0.213 | 0.366 | 0.153 | 0.304 | 0.265 | 8.0% | 19.0% | 33.6% |
| Tj Friedl | 193 | 0.201 | 0.284 | 0.083 | 0.261 | 0.250 | 3.3% | 22.3% | 24.3% |
| Ke'Bryan Hayes | 146 | 0.157 | 0.231 | 0.075 | 0.224 | 0.312 | 8.5% | 31.3% | 18.1% |
| Dane Myers | 138 | 0.265 | 0.385 | 0.120 | 0.353 | 0.368 | 7.6% | 22.8% | 16.4% |
| Blake Dunn | 138 | 0.276 | 0.386 | 0.110 | 0.333 | 0.277 | 3.2% | 20.3% | 21.9% |


## New York Yankees Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cody Bellinger | 336 | 0.266 | 0.455 | 0.189 | 0.358 | 0.371 | 7.3% | 24.4% | 17.2% |
| Ben Rice | 324 | 0.279 | 0.586 | 0.307 | 0.412 | 0.394 | 15.2% | 32.1% | 23.5% |
| Jazz Chisholm | 311 | 0.223 | 0.399 | 0.176 | 0.318 | 0.303 | 8.6% | 28.4% | 29.5% |
| Trent Grisham | 281 | 0.232 | 0.397 | 0.165 | 0.337 | 0.360 | 11.4% | 32.6% | 15.1% |
| Aaron Judge | 270 | 0.250 | 0.536 | 0.286 | 0.399 | 0.415 | 21.9% | 31.3% | 30.8% |
| José Caballero | 244 | 0.252 | 0.392 | 0.140 | 0.317 | 0.287 | 4.1% | 16.8% | 23.5% |
| Ryan Mcmahon | 218 | 0.219 | 0.368 | 0.149 | 0.285 | 0.307 | 12.7% | 26.8% | 28.6% |
| Paul Goldschmidt | 212 | 0.283 | 0.529 | 0.246 | 0.376 | 0.353 | 12.0% | 26.2% | 22.9% |
| Austin Wells | 180 | 0.162 | 0.253 | 0.091 | 0.244 | 0.301 | 7.5% | 29.2% | 27.6% |
| Amed Rosario | 138 | 0.262 | 0.460 | 0.198 | 0.333 | 0.323 | 8.8% | 26.8% | 22.9% |
| Giancarlo Stanton | 111 | 0.260 | 0.433 | 0.173 | 0.323 | 0.326 | 23.9% | 30.8% | 34.1% |
| J. C. Escarra | 107 | 0.212 | 0.333 | 0.121 | 0.279 | 0.258 | 6.3% | 25.8% | 24.5% |


## Bullpen Fatigue Report

### Cincinnati Reds Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brock Burke | 2026-06-20 | 1.0 | 13 |
| Caleb Ferguson | 2026-06-19 | 1.2 | 21 |
| Chase Petty | 2026-06-20 | 1.0 | 23 |
| Chris Paddack | 2026-06-17 | 4.1 | 60 |
| Tejay Antone | 2026-06-20 | 2.0 | 23 |
| Zach Maxwell | 2026-06-19 | 1.0 | 21 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Brock Burke, Chase Petty, Tejay Antone


### New York Yankees Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brent Headrick | 2026-06-17 | 0.2 | 6 |
| Brent Headrick | 2026-06-19 | 1.0 | 17 |
| Camilo Doval | 2026-06-18 | 1.2 | 16 |
| David Bednar | 2026-06-19 | 1.0 | 10 |
| Fernando Cruz | 2026-06-18 | 0.2 | 10 |
| Jake Bird | 2026-06-17 | 1.0 | 16 |
| Jake Bird | 2026-06-19 | 1.0 | 21 |
| Jake Bird | 2026-06-20 | 1.0 | 15 |
| Max Schuemann | 2026-06-20 | 1.0 | 14 |
| Paul Blackburn | 2026-06-17 | 2.1 | 33 |
| Ryan Yarbrough | 2026-06-20 | 1.0 | 29 |
| Tim Hill | 2026-06-18 | 0.1 | 10 |
| Tim Hill | 2026-06-20 | 0.1 | 5 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Jake Bird, Max Schuemann, Ryan Yarbrough, Tim Hill



## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL
- Home pitcher pitch mix to inspect: SI, FF, SL, CH, CU
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 2. Milwaukee Brewers @ Atlanta Braves

## Game Context

| Field | Value |
| --- | --- |
| Park | Truist Park |
| Time | 2026-06-21T17:35:00Z |
| Away Team | Milwaukee Brewers |
| Home Team | Atlanta Braves |
| Away Probable Pitcher | Robert Gasser |
| Home Probable Pitcher | Bryce Elder |


## Away Starting Pitcher: Robert Gasser

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 515 |
| Batted/Result Events | 131 |
| Hits Allowed | 27 |
| Walks | 12 |
| Strikeouts | 31 |
| Home Runs | 6 |
| K Event Rate | 23.7% |
| BB Event Rate | 9.2% |
| HR Event Rate | 4.6% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.6% | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 50.0% |
| CH | vs R | 8.9% | 46 | 0.375 | 0.812 | 0.438 | 0.509 | 0.515 | 18.8% | 39.1% | 0.0% |
| FC | vs L | 7.6% | 39 | 0.250 | 1.000 | 0.750 | 0.600 | 0.416 | 0.0% | 25.0% | 42.9% |
| FC | vs R | 11.1% | 57 | 0.100 | 0.100 | 0.000 | 0.293 | 0.323 | 0.0% | 27.3% | 25.8% |
| FF | vs L | 5.2% | 27 | 0.167 | 0.333 | 0.167 | 0.279 | 0.203 | 0.0% | 22.2% | 31.2% |
| FF | vs R | 11.5% | 59 | 0.118 | 0.176 | 0.059 | 0.126 | 0.113 | 0.0% | 10.5% | 37.8% |
| SI | vs L | 10.7% | 55 | 0.300 | 0.500 | 0.200 | 0.400 | 0.392 | 14.3% | 37.5% | 21.4% |
| SI | vs R | 17.5% | 90 | 0.333 | 0.556 | 0.222 | 0.381 | 0.277 | 13.3% | 27.6% | 11.1% |
| ST | vs L | 9.7% | 50 | 0.267 | 0.600 | 0.333 | 0.360 | 0.154 | 0.0% | 20.0% | 23.8% |
| ST | vs R | 17.3% | 89 | 0.167 | 0.333 | 0.167 | 0.324 | 0.285 | 7.7% | 12.5% | 26.7% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-16 | 92 | 2 | 2 | 5 | 0 |
| 2026-06-09 | 93 | 8 | 2 | 7 | 4 |
| 2026-06-03 | 83 | 5 | 1 | 5 | 1 |
| 2026-05-23 | 89 | 4 | 4 | 4 | 1 |
| 2026-05-17 | 79 | 3 | 2 | 3 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Eli White | 7 | 0.200 | 0.800 | 0.600 | 0.486 | 0.473 | 20.0% | 23.1% | 13.3% |
| FC | Michael Harris | 19 | 0.333 | 0.722 | 0.389 | 0.455 | 0.510 | 22.2% | 34.4% | 14.0% |
| FF | Matt Olson | 101 | 0.253 | 0.609 | 0.356 | 0.398 | 0.415 | 20.6% | 28.2% | 18.8% |
| SI | Drake Baldwin | 45 | 0.351 | 0.703 | 0.351 | 0.494 | 0.529 | 15.8% | 30.0% | 9.4% |
| ST | Michael Harris | 32 | 0.241 | 0.586 | 0.345 | 0.355 | 0.342 | 15.8% | 38.5% | 28.1% |
| FF | Drake Baldwin | 73 | 0.290 | 0.629 | 0.339 | 0.432 | 0.454 | 21.7% | 32.7% | 16.9% |
| SI | Ronald Acuña | 54 | 0.362 | 0.681 | 0.319 | 0.479 | 0.529 | 19.1% | 32.0% | 13.7% |
| FC | Dominic Smith | 13 | 0.308 | 0.615 | 0.308 | 0.388 | 0.353 | 15.4% | 33.3% | 21.9% |
| SI | Matt Olson | 66 | 0.339 | 0.643 | 0.304 | 0.448 | 0.406 | 17.4% | 36.2% | 9.1% |
| SI | Jorge Mateo | 21 | 0.450 | 0.750 | 0.300 | 0.521 | 0.413 | 12.5% | 33.3% | 8.1% |
| FC | Austin Riley | 20 | 0.150 | 0.450 | 0.300 | 0.245 | 0.358 | 25.0% | 30.0% | 36.5% |
| SI | Eli White | 27 | 0.333 | 0.630 | 0.296 | 0.407 | 0.311 | 12.5% | 34.3% | 11.4% |
| CH | Mike Yastrzemski | 27 | 0.280 | 0.560 | 0.280 | 0.380 | 0.249 | 10.5% | 23.5% | 17.4% |
| ST | Jorge Mateo | 11 | 0.273 | 0.545 | 0.273 | 0.345 | 0.279 | 11.1% | 17.6% | 12.5% |
| FC | Ozzie Albies | 19 | 0.400 | 0.667 | 0.267 | 0.508 | 0.395 | 0.0% | 24.2% | 21.3% |
| FC | Drake Baldwin | 21 | 0.368 | 0.632 | 0.263 | 0.452 | 0.374 | 25.0% | 30.0% | 20.5% |
| CH | Matt Olson | 32 | 0.161 | 0.419 | 0.258 | 0.253 | 0.248 | 15.0% | 29.5% | 21.5% |
| FF | Ozzie Albies | 84 | 0.286 | 0.543 | 0.257 | 0.367 | 0.371 | 9.5% | 31.9% | 16.3% |
| ST | Drake Baldwin | 14 | 0.250 | 0.500 | 0.250 | 0.421 | 0.462 | 57.1% | 26.3% | 28.6% |
| CH | Michael Harris | 40 | 0.350 | 0.575 | 0.225 | 0.398 | 0.427 | 19.4% | 37.5% | 24.2% |
| FF | Dominic Smith | 61 | 0.377 | 0.585 | 0.208 | 0.433 | 0.462 | 12.2% | 24.2% | 6.5% |
| ST | Austin Riley | 37 | 0.206 | 0.412 | 0.206 | 0.295 | 0.283 | 22.7% | 26.2% | 35.1% |
| ST | Matt Olson | 32 | 0.300 | 0.500 | 0.200 | 0.364 | 0.364 | 14.3% | 40.0% | 30.2% |
| SI | Austin Riley | 60 | 0.235 | 0.431 | 0.196 | 0.375 | 0.340 | 9.5% | 22.6% | 10.8% |
| FF | Michael Harris | 58 | 0.294 | 0.490 | 0.196 | 0.395 | 0.373 | 9.8% | 24.8% | 17.9% |
| FC | Matt Olson | 36 | 0.258 | 0.452 | 0.194 | 0.357 | 0.364 | 8.0% | 35.1% | 18.4% |
| SI | Ozzie Albies | 51 | 0.277 | 0.468 | 0.191 | 0.352 | 0.310 | 4.5% | 18.5% | 15.0% |
| FF | Austin Riley | 111 | 0.237 | 0.423 | 0.186 | 0.334 | 0.311 | 11.1% | 31.5% | 26.7% |
| FF | Eli White | 30 | 0.250 | 0.429 | 0.179 | 0.317 | 0.273 | 5.0% | 13.6% | 14.8% |
| CH | Ronald Acuña | 27 | 0.292 | 0.458 | 0.167 | 0.363 | 0.332 | 11.8% | 27.6% | 26.1% |


## Home Starting Pitcher: Bryce Elder

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1299 |
| Batted/Result Events | 366 |
| Hits Allowed | 74 |
| Walks | 27 |
| Strikeouts | 73 |
| Home Runs | 9 |
| K Event Rate | 19.9% |
| BB Event Rate | 7.4% |
| HR Event Rate | 2.5% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 8.0% | 104 | 0.185 | 0.185 | 0.000 | 0.167 | 0.181 | 0.0% | 14.3% | 27.3% |
| CH | vs R | 1.6% | 21 | 0.333 | 0.500 | 0.167 | 0.358 | 0.200 | 0.0% | 33.3% | 23.1% |
| FC | vs L | 11.9% | 155 | 0.194 | 0.333 | 0.139 | 0.298 | 0.323 | 2.7% | 29.0% | 12.9% |
| FC | vs R | 0.5% | 7 | 0.333 | 0.667 | 0.333 | 0.417 | 0.194 | 0.0% | 66.7% | 0.0% |
| FF | vs L | 21.6% | 281 | 0.245 | 0.327 | 0.082 | 0.276 | 0.302 | 2.2% | 15.7% | 14.8% |
| FF | vs R | 3.1% | 40 | 0.385 | 0.462 | 0.077 | 0.396 | 0.271 | 0.0% | 25.0% | 13.0% |
| SI | vs L | 6.9% | 90 | 0.167 | 0.333 | 0.167 | 0.280 | 0.293 | 5.6% | 26.7% | 16.2% |
| SI | vs R | 18.4% | 239 | 0.273 | 0.409 | 0.136 | 0.337 | 0.333 | 5.7% | 38.8% | 12.2% |
| SL | vs L | 17.6% | 228 | 0.136 | 0.258 | 0.121 | 0.231 | 0.248 | 4.4% | 26.2% | 27.0% |
| SL | vs R | 10.2% | 133 | 0.270 | 0.405 | 0.135 | 0.341 | 0.276 | 7.7% | 24.4% | 33.8% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-14 | 75 | 10 | 2 | 2 | 2 |
| 2026-06-07 | 88 | 2 | 2 | 4 | 1 |
| 2026-06-02 | 103 | 6 | 1 | 6 | 1 |
| 2026-05-27 | 59 | 9 | 1 | 1 | 0 |
| 2026-05-22 | 87 | 5 | 1 | 4 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Brice Turang | 16 | 0.400 | 1.000 | 0.600 | 0.584 | 0.645 | 30.8% | 20.7% | 19.5% |
| FC | Gary Sánchez | 12 | 0.222 | 0.778 | 0.556 | 0.475 | 0.476 | 25.0% | 45.5% | 8.3% |
| CH | Christian Yelich | 19 | 0.400 | 0.933 | 0.533 | 0.584 | 0.347 | 20.0% | 28.6% | 25.8% |
| FC | Jake Bauers | 15 | 0.308 | 0.769 | 0.462 | 0.480 | 0.446 | 18.2% | 26.3% | 24.0% |
| FF | Andrew Vaughn | 36 | 0.483 | 0.931 | 0.448 | 0.617 | 0.474 | 11.5% | 31.1% | 9.8% |
| CH | Jake Bauers | 25 | 0.348 | 0.739 | 0.391 | 0.474 | 0.349 | 23.5% | 45.8% | 43.8% |
| FC | Jackson Chourio | 17 | 0.250 | 0.625 | 0.375 | 0.382 | 0.324 | 7.7% | 30.4% | 35.9% |
| FF | Jake Bauers | 77 | 0.362 | 0.696 | 0.333 | 0.473 | 0.398 | 20.0% | 32.3% | 14.3% |
| FC | William Contreras | 34 | 0.438 | 0.750 | 0.312 | 0.546 | 0.411 | 10.7% | 33.3% | 20.0% |
| FF | Gary Sánchez | 49 | 0.297 | 0.595 | 0.297 | 0.455 | 0.438 | 13.8% | 21.2% | 19.4% |
| FF | William Contreras | 83 | 0.239 | 0.493 | 0.254 | 0.386 | 0.376 | 9.5% | 36.1% | 11.6% |
| CH | Jackson Chourio | 21 | 0.400 | 0.650 | 0.250 | 0.462 | 0.238 | 5.9% | 28.6% | 14.3% |
| FC | Garrett Mitchell | 23 | 0.364 | 0.591 | 0.227 | 0.420 | 0.380 | 16.7% | 32.1% | 44.2% |
| SI | Brice Turang | 59 | 0.260 | 0.480 | 0.220 | 0.393 | 0.361 | 5.0% | 21.2% | 9.4% |
| SI | Jackson Chourio | 42 | 0.378 | 0.595 | 0.216 | 0.474 | 0.452 | 10.3% | 44.2% | 10.1% |
| FF | Jackson Chourio | 55 | 0.255 | 0.471 | 0.216 | 0.352 | 0.336 | 21.2% | 27.0% | 25.5% |
| CH | Gary Sánchez | 17 | 0.267 | 0.467 | 0.200 | 0.318 | 0.268 | 7.7% | 43.8% | 38.2% |
| FF | David Hamilton | 79 | 0.258 | 0.455 | 0.197 | 0.365 | 0.315 | 5.3% | 18.6% | 9.2% |
| FF | Brice Turang | 97 | 0.211 | 0.408 | 0.197 | 0.358 | 0.358 | 12.8% | 17.0% | 18.9% |
| SL | Jake Bauers | 43 | 0.167 | 0.361 | 0.194 | 0.299 | 0.318 | 10.0% | 30.4% | 26.9% |
| SI | Jake Bauers | 53 | 0.250 | 0.432 | 0.182 | 0.360 | 0.389 | 10.0% | 30.9% | 11.6% |
| CH | Brice Turang | 34 | 0.214 | 0.393 | 0.179 | 0.341 | 0.322 | 0.0% | 19.0% | 21.0% |
| SL | Andrew Vaughn | 19 | 0.353 | 0.529 | 0.176 | 0.413 | 0.330 | 6.7% | 33.3% | 21.4% |
| SL | Brice Turang | 47 | 0.244 | 0.415 | 0.171 | 0.335 | 0.334 | 7.1% | 35.9% | 24.1% |
| SL | Garrett Mitchell | 41 | 0.111 | 0.278 | 0.167 | 0.210 | 0.299 | 15.8% | 21.9% | 52.8% |
| CH | Andrew Vaughn | 15 | 0.462 | 0.615 | 0.154 | 0.500 | 0.515 | 0.0% | 56.2% | 18.2% |
| FC | Andrew Vaughn | 9 | 0.714 | 0.857 | 0.143 | 0.694 | 0.274 | 0.0% | 22.2% | 21.7% |
| SI | Gary Sánchez | 28 | 0.273 | 0.409 | 0.136 | 0.382 | 0.407 | 5.0% | 30.3% | 2.9% |
| FF | Garrett Mitchell | 90 | 0.211 | 0.342 | 0.132 | 0.313 | 0.337 | 17.9% | 25.5% | 29.3% |
| SI | Sal Frelick | 56 | 0.300 | 0.420 | 0.120 | 0.387 | 0.318 | 2.1% | 21.2% | 1.4% |


## Milwaukee Brewers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brice Turang | 330 | 0.253 | 0.451 | 0.199 | 0.364 | 0.357 | 9.3% | 22.9% | 19.6% |
| William Contreras | 318 | 0.297 | 0.434 | 0.136 | 0.359 | 0.341 | 8.4% | 32.1% | 16.7% |
| Jake Bauers | 277 | 0.277 | 0.555 | 0.277 | 0.399 | 0.359 | 15.2% | 34.6% | 22.6% |
| Sal Frelick | 268 | 0.229 | 0.312 | 0.083 | 0.305 | 0.282 | 1.9% | 20.3% | 9.7% |
| Garrett Mitchell | 255 | 0.234 | 0.387 | 0.153 | 0.322 | 0.334 | 13.8% | 28.6% | 36.6% |
| Luis Rengifo | 229 | 0.211 | 0.289 | 0.078 | 0.274 | 0.296 | 5.5% | 23.1% | 15.8% |
| David Hamilton | 222 | 0.250 | 0.349 | 0.099 | 0.309 | 0.267 | 4.6% | 17.9% | 18.9% |
| Christian Yelich | 213 | 0.257 | 0.408 | 0.152 | 0.326 | 0.299 | 6.9% | 18.8% | 28.8% |
| Jackson Chourio | 200 | 0.304 | 0.554 | 0.250 | 0.395 | 0.354 | 14.0% | 29.6% | 21.8% |
| Joey Ortiz | 200 | 0.216 | 0.263 | 0.047 | 0.276 | 0.294 | 2.8% | 22.1% | 17.3% |
| Gary Sánchez | 157 | 0.234 | 0.469 | 0.234 | 0.366 | 0.369 | 10.0% | 27.7% | 22.7% |
| Andrew Vaughn | 146 | 0.344 | 0.516 | 0.172 | 0.422 | 0.360 | 4.6% | 32.0% | 17.0% |


## Atlanta Braves Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Matt Olson | 348 | 0.279 | 0.554 | 0.276 | 0.382 | 0.368 | 14.9% | 32.2% | 20.5% |
| Ozzie Albies | 340 | 0.275 | 0.439 | 0.164 | 0.341 | 0.307 | 4.2% | 21.6% | 18.6% |
| Austin Riley | 322 | 0.216 | 0.376 | 0.160 | 0.302 | 0.299 | 11.5% | 29.6% | 28.7% |
| Mauricio Dubón | 303 | 0.259 | 0.397 | 0.138 | 0.329 | 0.318 | 5.5% | 17.9% | 14.3% |
| Michael Harris | 281 | 0.293 | 0.489 | 0.195 | 0.355 | 0.385 | 15.2% | 35.6% | 23.3% |
| Drake Baldwin | 254 | 0.296 | 0.543 | 0.247 | 0.400 | 0.398 | 18.7% | 28.9% | 22.7% |
| Ronald Acuña | 244 | 0.254 | 0.428 | 0.174 | 0.359 | 0.378 | 12.8% | 25.3% | 26.3% |
| Mike Yastrzemski | 222 | 0.239 | 0.396 | 0.157 | 0.328 | 0.288 | 4.2% | 24.7% | 21.9% |
| Dominic Smith | 196 | 0.277 | 0.418 | 0.141 | 0.337 | 0.338 | 7.7% | 22.9% | 18.2% |
| Jorge Mateo | 124 | 0.289 | 0.456 | 0.167 | 0.362 | 0.340 | 9.6% | 25.9% | 26.9% |
| Eli White | 111 | 0.260 | 0.470 | 0.210 | 0.367 | 0.295 | 8.8% | 22.8% | 22.7% |
| Ha-Seong Kim | 66 | 0.085 | 0.085 | 0.000 | 0.142 | 0.213 | 2.4% | 14.8% | 16.1% |


## Bullpen Fatigue Report

### Milwaukee Brewers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Aaron Ashby | 2026-06-17 | 1.0 | 9 |
| Aaron Ashby | 2026-06-20 | 0.1 | 14 |
| Abner Uribe | 2026-06-19 | 1.0 | 13 |
| Abner Uribe | 2026-06-20 | 0.2 | 8 |
| Chad Patrick | 2026-06-17 | 3.1 | 50 |
| Craig Yoho | 2026-06-18 | 1.0 | 17 |
| Craig Yoho | 2026-06-19 | 1.0 | 13 |
| Drew Rom | 2026-06-18 | 1.1 | 32 |
| Grant Anderson | 2026-06-17 | 1.0 | 14 |
| Grant Anderson | 2026-06-18 | 0.2 | 21 |
| Joel Kuhnel | 2026-06-18 | 1.0 | 21 |
| Trevor Megill | 2026-06-20 | 1.0 | 8 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Aaron Ashby, Abner Uribe, Trevor Megill


### Atlanta Braves Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Anthony Molina | 2026-06-17 | 2.0 | 33 |
| Carlos Carrasco | 2026-06-17 | 4.0 | 55 |
| Didier Fuentes | 2026-06-20 | 1.1 | 28 |
| Dylan Dodd | 2026-06-17 | 2.0 | 27 |
| Dylan Lee | 2026-06-19 | 0.2 | 17 |
| Dylan Lee | 2026-06-20 | 1.0 | 11 |
| James Karinchak | 2026-06-17 | 1.0 | 13 |
| James Karinchak | 2026-06-20 | 1.0 | 10 |
| Raisel Iglesias | 2026-06-19 | 1.0 | 20 |
| Reynaldo López | 2026-06-17 | 2.0 | 30 |
| Robert Suarez | 2026-06-19 | 1.1 | 28 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Didier Fuentes, Dylan Lee, James Karinchak



## Final Game Dissection

- Away pitcher pitch mix to inspect: SI, ST, FC, FF, CH
- Home pitcher pitch mix to inspect: SL, SI, FF, FC, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 3. Washington Nationals @ Tampa Bay Rays

## Game Context

| Field | Value |
| --- | --- |
| Park | Tropicana Field |
| Time | 2026-06-21T17:40:00Z |
| Away Team | Washington Nationals |
| Home Team | Tampa Bay Rays |
| Away Probable Pitcher | Andrew Alvarez |
| Home Probable Pitcher | Nick Martinez |


## Away Starting Pitcher: Andrew Alvarez

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 488 |
| Batted/Result Events | 121 |
| Hits Allowed | 29 |
| Walks | 12 |
| Strikeouts | 31 |
| Home Runs | 2 |
| K Event Rate | 25.6% |
| BB Event Rate | 9.9% |
| HR Event Rate | 1.7% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs R | 2.3% | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.429 | 0.0% | 0.0% | 33.3% |
| CU | vs L | 5.1% | 25 | 0.200 | 0.200 | 0.000 | 0.180 | 0.256 | 0.0% | 40.0% | 15.4% |
| CU | vs R | 24.0% | 117 | 0.148 | 0.185 | 0.037 | 0.184 | 0.174 | 0.0% | 28.6% | 39.6% |
| FF | vs L | 3.3% | 16 | 0.667 | 0.667 | 0.000 | 0.625 | 0.297 | 0.0% | 0.0% | 0.0% |
| FF | vs R | 21.1% | 103 | 0.310 | 0.517 | 0.207 | 0.395 | 0.445 | 8.0% | 32.6% | 9.1% |
| SI | vs L | 9.6% | 47 | 0.286 | 0.286 | 0.000 | 0.257 | 0.323 | 0.0% | 45.5% | 13.3% |
| SI | vs R | 5.9% | 29 | 0.286 | 0.286 | 0.000 | 0.312 | 0.439 | 14.3% | 62.5% | 0.0% |
| SL | vs L | 11.9% | 58 | 0.357 | 0.786 | 0.429 | 0.503 | 0.361 | 11.1% | 23.5% | 37.5% |
| SL | vs R | 16.8% | 82 | 0.273 | 0.364 | 0.091 | 0.342 | 0.405 | 11.1% | 17.4% | 36.1% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 58 | 5 | 1 | 5 | 0 |
| 2026-06-09 | 90 | 5 | 5 | 4 | 0 |
| 2026-06-03 | 82 | 4 | 1 | 5 | 1 |
| 2026-05-29 | 74 | 5 | 2 | 1 | 0 |
| 2026-05-24 | 18 | 1 | 1 | 1 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Jonathan Aranda | 15 | 0.385 | 0.846 | 0.462 | 0.493 | 0.517 | 33.3% | 45.0% | 23.3% |
| CU | Ryan Vilade | 7 | 0.571 | 1.000 | 0.429 | 0.671 | 0.588 | 14.3% | 33.3% | 7.7% |
| SL | Ryan Vilade | 10 | 0.111 | 0.444 | 0.333 | 0.470 | 0.656 | 11.1% | 40.0% | 36.0% |
| SL | Jonathan Aranda | 40 | 0.229 | 0.514 | 0.286 | 0.359 | 0.305 | 12.5% | 32.5% | 19.4% |
| SL | Yandy Díaz | 54 | 0.413 | 0.696 | 0.283 | 0.494 | 0.500 | 17.8% | 34.8% | 12.3% |
| SL | Richie Palacios | 23 | 0.273 | 0.545 | 0.273 | 0.357 | 0.368 | 6.2% | 17.9% | 21.1% |
| FF | Junior Caminero | 71 | 0.339 | 0.610 | 0.271 | 0.454 | 0.442 | 15.6% | 41.9% | 21.0% |
| SI | Jonny Deluca | 36 | 0.353 | 0.588 | 0.235 | 0.429 | 0.355 | 3.3% | 26.2% | 13.5% |
| SI | Junior Caminero | 74 | 0.393 | 0.623 | 0.230 | 0.484 | 0.403 | 13.0% | 38.8% | 13.0% |
| SL | Chandler Simpson | 27 | 0.360 | 0.560 | 0.200 | 0.419 | 0.264 | 0.0% | 25.9% | 16.2% |
| CU | Junior Caminero | 20 | 0.111 | 0.278 | 0.167 | 0.215 | 0.267 | 11.1% | 31.2% | 32.1% |
| FF | Yandy Díaz | 85 | 0.228 | 0.392 | 0.165 | 0.296 | 0.289 | 6.8% | 23.6% | 14.5% |
| FF | Jonathan Aranda | 126 | 0.243 | 0.408 | 0.165 | 0.339 | 0.367 | 12.0% | 21.8% | 20.3% |
| FF | Hunter Feduccia | 40 | 0.152 | 0.303 | 0.152 | 0.280 | 0.319 | 20.0% | 20.0% | 17.7% |
| FF | Nick Fortes | 59 | 0.278 | 0.426 | 0.148 | 0.336 | 0.275 | 4.3% | 32.6% | 7.4% |
| SI | Ryan Vilade | 34 | 0.185 | 0.333 | 0.148 | 0.299 | 0.270 | 0.0% | 23.1% | 8.6% |
| SI | Jonathan Aranda | 49 | 0.341 | 0.488 | 0.146 | 0.401 | 0.385 | 6.2% | 30.0% | 12.5% |
| SL | Cedric Mullins | 28 | 0.143 | 0.286 | 0.143 | 0.286 | 0.260 | 0.0% | 12.2% | 23.2% |
| FF | Ryan Vilade | 46 | 0.250 | 0.375 | 0.125 | 0.315 | 0.238 | 3.7% | 9.5% | 20.0% |
| FF | Taylor Walls | 81 | 0.215 | 0.338 | 0.123 | 0.307 | 0.269 | 5.7% | 16.7% | 15.8% |
| FF | Cedric Mullins | 99 | 0.176 | 0.294 | 0.118 | 0.269 | 0.272 | 4.5% | 22.2% | 21.4% |
| SL | Junior Caminero | 54 | 0.173 | 0.288 | 0.115 | 0.216 | 0.280 | 11.9% | 37.1% | 22.5% |
| SI | Nick Fortes | 52 | 0.312 | 0.417 | 0.104 | 0.338 | 0.339 | 6.8% | 26.8% | 2.5% |
| SI | Yandy Díaz | 72 | 0.448 | 0.552 | 0.103 | 0.503 | 0.413 | 5.7% | 38.5% | 4.8% |
| FF | Ben Williamson | 71 | 0.262 | 0.361 | 0.098 | 0.332 | 0.326 | 2.0% | 23.9% | 7.1% |
| FF | Jonny Deluca | 41 | 0.216 | 0.297 | 0.081 | 0.270 | 0.234 | 4.0% | 14.0% | 29.3% |
| SI | Ben Williamson | 31 | 0.259 | 0.333 | 0.074 | 0.316 | 0.310 | 0.0% | 21.1% | 10.6% |
| CU | Cedric Mullins | 16 | 0.200 | 0.267 | 0.067 | 0.278 | 0.208 | 0.0% | 25.0% | 42.3% |
| SL | Jonny Deluca | 15 | 0.200 | 0.267 | 0.067 | 0.203 | 0.219 | 0.0% | 11.8% | 32.1% |
| SL | Taylor Walls | 21 | 0.188 | 0.250 | 0.062 | 0.374 | 0.227 | 0.0% | 4.5% | 28.1% |


## Home Starting Pitcher: Nick Martinez

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1309 |
| Batted/Result Events | 387 |
| Hits Allowed | 104 |
| Walks | 17 |
| Strikeouts | 51 |
| Home Runs | 11 |
| K Event Rate | 13.2% |
| BB Event Rate | 4.4% |
| HR Event Rate | 2.8% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 18.0% | 235 | 0.195 | 0.286 | 0.091 | 0.226 | 0.234 | 3.2% | 16.7% | 29.4% |
| CH | vs R | 9.9% | 129 | 0.074 | 0.074 | 0.000 | 0.110 | 0.172 | 0.0% | 13.9% | 31.7% |
| CU | vs L | 4.4% | 57 | 0.375 | 0.500 | 0.125 | 0.381 | 0.500 | 12.5% | 10.0% | 14.3% |
| CU | vs R | 2.7% | 35 | 0.250 | 0.500 | 0.250 | 0.312 | 0.398 | 25.0% | 22.2% | 10.0% |
| FC | vs L | 12.5% | 163 | 0.283 | 0.509 | 0.226 | 0.349 | 0.338 | 6.1% | 22.2% | 14.6% |
| FC | vs R | 7.3% | 96 | 0.419 | 0.710 | 0.290 | 0.489 | 0.387 | 10.0% | 26.8% | 10.2% |
| FF | vs L | 7.6% | 99 | 0.346 | 0.654 | 0.308 | 0.441 | 0.393 | 13.0% | 33.3% | 14.3% |
| FF | vs R | 4.2% | 55 | 0.375 | 0.625 | 0.250 | 0.458 | 0.522 | 6.7% | 32.0% | 3.6% |
| PO | vs L | 0.2% | 2 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs L | 14.5% | 190 | 0.256 | 0.349 | 0.093 | 0.309 | 0.307 | 9.1% | 38.6% | 4.3% |
| SI | vs R | 15.4% | 201 | 0.308 | 0.446 | 0.138 | 0.326 | 0.367 | 4.9% | 25.7% | 8.9% |
| SL | vs L | 1.2% | 16 | 0.667 | 1.000 | 0.333 | 1.017 | 0.309 | 0.0% | 20.0% | 0.0% |
| SL | vs R | 2.3% | 30 | 0.700 | 1.200 | 0.500 | 0.736 | 0.576 | 18.2% | 40.0% | 6.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 96 | 5 | 1 | 6 | 1 |
| 2026-06-09 | 73 | 6 | 0 | 2 | 0 |
| 2026-06-03 | 58 | 9 | 1 | 1 | 2 |
| 2026-05-29 | 88 | 8 | 0 | 5 | 0 |
| 2026-05-22 | 94 | 9 | 1 | 1 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Keibert Ruiz | 9 | 0.429 | 1.143 | 0.714 | 0.578 | 0.441 | 33.3% | 27.3% | 4.3% |
| FC | Cj Abrams | 27 | 0.458 | 1.167 | 0.708 | 0.681 | 0.402 | 13.0% | 30.6% | 21.3% |
| FC | Curtis Mead | 19 | 0.267 | 0.733 | 0.467 | 0.471 | 0.458 | 15.4% | 29.0% | 20.0% |
| FC | James Wood | 26 | 0.280 | 0.640 | 0.360 | 0.396 | 0.440 | 22.7% | 36.6% | 27.9% |
| FC | José Tena | 9 | 0.222 | 0.556 | 0.333 | 0.417 | 0.412 | 0.0% | 33.3% | 28.0% |
| FF | James Wood | 102 | 0.333 | 0.644 | 0.310 | 0.455 | 0.485 | 25.0% | 36.4% | 18.1% |
| SI | Curtis Mead | 39 | 0.212 | 0.515 | 0.303 | 0.363 | 0.424 | 17.9% | 29.6% | 10.6% |
| FF | Brady House | 53 | 0.224 | 0.490 | 0.265 | 0.345 | 0.343 | 23.1% | 28.8% | 35.8% |
| FF | Keibert Ruiz | 54 | 0.260 | 0.520 | 0.260 | 0.356 | 0.297 | 6.2% | 28.9% | 5.5% |
| CH | Keibert Ruiz | 32 | 0.250 | 0.500 | 0.250 | 0.316 | 0.208 | 4.0% | 32.4% | 28.3% |
| FF | Jacob Young | 74 | 0.231 | 0.477 | 0.246 | 0.358 | 0.349 | 7.7% | 25.5% | 12.0% |
| FF | Cj Abrams | 81 | 0.354 | 0.600 | 0.246 | 0.467 | 0.433 | 13.5% | 19.8% | 21.7% |
| SI | Luis García | 38 | 0.286 | 0.514 | 0.229 | 0.368 | 0.356 | 9.4% | 36.2% | 1.6% |
| SI | Daylen Lile | 48 | 0.341 | 0.561 | 0.220 | 0.436 | 0.460 | 5.0% | 26.6% | 10.8% |
| SI | James Wood | 59 | 0.326 | 0.543 | 0.217 | 0.444 | 0.511 | 21.6% | 42.4% | 15.5% |
| FF | Daylen Lile | 93 | 0.266 | 0.481 | 0.215 | 0.359 | 0.342 | 10.8% | 19.3% | 21.7% |
| FC | Jacob Young | 14 | 0.286 | 0.500 | 0.214 | 0.336 | 0.429 | 20.0% | 22.7% | 20.0% |
| CH | Jacob Young | 23 | 0.150 | 0.350 | 0.200 | 0.250 | 0.309 | 5.6% | 15.4% | 28.9% |
| FF | José Tena | 45 | 0.200 | 0.400 | 0.200 | 0.322 | 0.344 | 9.7% | 23.2% | 20.8% |
| FF | Luis García | 65 | 0.246 | 0.443 | 0.197 | 0.345 | 0.370 | 11.3% | 27.6% | 11.4% |
| CH | Luis García | 46 | 0.261 | 0.457 | 0.196 | 0.305 | 0.272 | 8.1% | 23.3% | 21.2% |
| SI | Drew Millas | 22 | 0.188 | 0.375 | 0.188 | 0.341 | 0.353 | 8.3% | 9.1% | 4.0% |
| FC | Luis García | 16 | 0.312 | 0.500 | 0.188 | 0.350 | 0.306 | 6.7% | 35.5% | 10.3% |
| CH | Curtis Mead | 25 | 0.227 | 0.409 | 0.182 | 0.322 | 0.365 | 5.3% | 35.0% | 12.0% |
| SI | José Tena | 21 | 0.294 | 0.471 | 0.176 | 0.400 | 0.363 | 15.4% | 23.3% | 12.5% |
| SI | Cj Abrams | 44 | 0.293 | 0.463 | 0.171 | 0.350 | 0.396 | 11.8% | 37.0% | 13.5% |
| FF | Curtis Mead | 67 | 0.203 | 0.356 | 0.153 | 0.307 | 0.344 | 9.5% | 20.0% | 12.5% |
| CH | Cj Abrams | 42 | 0.175 | 0.325 | 0.150 | 0.236 | 0.291 | 10.3% | 24.6% | 30.4% |
| SI | Jorbit Vivas | 26 | 0.381 | 0.524 | 0.143 | 0.406 | 0.312 | 0.0% | 20.0% | 11.9% |
| CH | James Wood | 45 | 0.250 | 0.375 | 0.125 | 0.379 | 0.421 | 10.0% | 27.3% | 32.5% |


## Washington Nationals Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| James Wood | 385 | 0.263 | 0.519 | 0.256 | 0.389 | 0.430 | 23.5% | 36.2% | 30.1% |
| Daylen Lile | 353 | 0.250 | 0.406 | 0.156 | 0.319 | 0.322 | 7.2% | 23.4% | 20.6% |
| Cj Abrams | 340 | 0.285 | 0.517 | 0.232 | 0.385 | 0.350 | 10.0% | 27.6% | 25.7% |
| Nasim Nuñez | 269 | 0.227 | 0.271 | 0.044 | 0.287 | 0.275 | 0.0% | 11.4% | 21.2% |
| Luis García | 266 | 0.253 | 0.440 | 0.187 | 0.316 | 0.325 | 9.0% | 29.7% | 17.2% |
| Jacob Young | 264 | 0.221 | 0.369 | 0.148 | 0.301 | 0.307 | 6.2% | 24.9% | 18.7% |
| Curtis Mead | 218 | 0.230 | 0.460 | 0.230 | 0.353 | 0.367 | 11.0% | 26.2% | 15.2% |
| Brady House | 193 | 0.242 | 0.404 | 0.163 | 0.315 | 0.320 | 9.5% | 28.9% | 30.2% |
| Keibert Ruiz | 181 | 0.267 | 0.453 | 0.186 | 0.319 | 0.269 | 5.3% | 28.5% | 11.7% |
| Jorbit Vivas | 160 | 0.245 | 0.317 | 0.072 | 0.310 | 0.304 | 3.3% | 17.7% | 16.1% |
| José Tena | 159 | 0.208 | 0.329 | 0.121 | 0.271 | 0.294 | 9.0% | 29.2% | 31.2% |
| Drew Millas | 133 | 0.178 | 0.263 | 0.085 | 0.270 | 0.279 | 3.5% | 12.6% | 20.9% |


## Tampa Bay Rays Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Junior Caminero | 337 | 0.278 | 0.478 | 0.199 | 0.369 | 0.363 | 12.5% | 36.2% | 21.4% |
| Jonathan Aranda | 334 | 0.270 | 0.448 | 0.178 | 0.358 | 0.368 | 11.2% | 25.3% | 19.8% |
| Yandy Díaz | 333 | 0.329 | 0.503 | 0.175 | 0.399 | 0.362 | 8.5% | 30.1% | 11.5% |
| Chandler Simpson | 300 | 0.267 | 0.320 | 0.053 | 0.292 | 0.251 | 0.0% | 9.2% | 7.8% |
| Cedric Mullins | 273 | 0.199 | 0.314 | 0.114 | 0.289 | 0.263 | 3.8% | 20.2% | 20.5% |
| Taylor Walls | 205 | 0.218 | 0.282 | 0.065 | 0.295 | 0.250 | 3.2% | 12.1% | 20.7% |
| Ben Williamson | 198 | 0.247 | 0.337 | 0.090 | 0.301 | 0.304 | 1.5% | 26.0% | 16.3% |
| Nick Fortes | 195 | 0.250 | 0.339 | 0.089 | 0.287 | 0.282 | 3.2% | 30.7% | 13.4% |
| Richie Palacios | 185 | 0.222 | 0.304 | 0.082 | 0.298 | 0.302 | 4.2% | 16.8% | 20.1% |
| Ryan Vilade | 145 | 0.276 | 0.449 | 0.173 | 0.364 | 0.318 | 3.8% | 20.5% | 16.8% |
| Jonny Deluca | 144 | 0.270 | 0.416 | 0.146 | 0.324 | 0.284 | 3.6% | 20.0% | 21.7% |
| Hunter Feduccia | 114 | 0.224 | 0.286 | 0.061 | 0.276 | 0.308 | 6.6% | 19.3% | 24.4% |


## Bullpen Fatigue Report

### Washington Nationals Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brad Lord | 2026-06-20 | 3.0 | 36 |
| Clayton Beeter | 2026-06-20 | 1.0 | 21 |
| Miles Mikolas | 2026-06-19 | 6.0 | 85 |
| Mitchell Parker | 2026-06-17 | 2.0 | 29 |
| Mitchell Parker | 2026-06-20 | 2.1 | 32 |
| PJ Poulin | 2026-06-17 | 1.0 | 23 |
| Paxton Schultz | 2026-06-17 | 1.0 | 18 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Brad Lord, Clayton Beeter, Mitchell Parker


### Tampa Bay Rays Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Bryan Baker | 2026-06-19 | 1.0 | 13 |
| Cam Booser | 2026-06-20 | 1.0 | 24 |
| Casey Legumina | 2026-06-17 | 0.1 | 19 |
| Cole Sulser | 2026-06-17 | 1.1 | 11 |
| Cole Sulser | 2026-06-20 | 2.0 | 25 |
| Craig Kimbrel | 2026-06-20 | 1.0 | 11 |
| Garrett Cleavinger | 2026-06-17 | 1.0 | 19 |
| Garrett Cleavinger | 2026-06-19 | 1.0 | 9 |
| Kevin Kelly | 2026-06-17 | 1.2 | 33 |
| Kevin Kelly | 2026-06-19 | 0.1 | 10 |
| Steven Matz | 2026-06-19 | 1.2 | 25 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Cam Booser, Cole Sulser, Craig Kimbrel



## Final Game Dissection

- Away pitcher pitch mix to inspect: CU, SL, FF, SI
- Home pitcher pitch mix to inspect: SI, CH, FC, FF
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 4. Chicago White Sox @ Detroit Tigers

## Game Context

| Field | Value |
| --- | --- |
| Park | Comerica Park |
| Time | 2026-06-21T17:40:00Z |
| Away Team | Chicago White Sox |
| Home Team | Detroit Tigers |
| Away Probable Pitcher | Davis Martin |
| Home Probable Pitcher | Keider Montero |


## Away Starting Pitcher: Davis Martin

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1371 |
| Batted/Result Events | 354 |
| Hits Allowed | 79 |
| Walks | 24 |
| Strikeouts | 86 |
| Home Runs | 6 |
| K Event Rate | 24.3% |
| BB Event Rate | 6.8% |
| HR Event Rate | 1.7% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 11.6% | 159 | 0.151 | 0.245 | 0.094 | 0.189 | 0.316 | 11.9% | 35.7% | 15.7% |
| CH | vs R | 3.3% | 45 | 0.300 | 0.500 | 0.200 | 0.373 | 0.411 | 0.0% | 37.5% | 10.0% |
| CU | vs L | 9.3% | 128 | 0.238 | 0.429 | 0.190 | 0.302 | 0.310 | 15.4% | 27.3% | 43.9% |
| CU | vs R | 2.9% | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.141 | 0.0% | 22.2% | 40.0% |
| FC | vs L | 9.7% | 133 | 0.346 | 0.577 | 0.231 | 0.406 | 0.442 | 10.5% | 36.4% | 24.2% |
| FC | vs R | 3.4% | 47 | 0.200 | 0.200 | 0.000 | 0.227 | 0.207 | 0.0% | 9.1% | 45.5% |
| FF | vs L | 16.2% | 222 | 0.289 | 0.400 | 0.111 | 0.357 | 0.305 | 2.7% | 23.8% | 14.7% |
| FF | vs R | 9.1% | 125 | 0.333 | 0.444 | 0.111 | 0.392 | 0.345 | 4.8% | 23.7% | 36.9% |
| SI | vs L | 8.0% | 109 | 0.200 | 0.280 | 0.080 | 0.276 | 0.342 | 4.8% | 28.3% | 9.3% |
| SI | vs R | 9.3% | 127 | 0.312 | 0.375 | 0.062 | 0.357 | 0.338 | 3.2% | 27.8% | 9.2% |
| SL | vs L | 3.1% | 42 | 0.182 | 0.364 | 0.182 | 0.227 | 0.176 | 0.0% | 13.3% | 31.8% |
| SL | vs R | 11.5% | 157 | 0.205 | 0.295 | 0.091 | 0.228 | 0.219 | 7.1% | 28.2% | 47.2% |
| ST | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| ST | vs R | 0.3% | 4 | 0.000 | 0.000 | 0.000 | 0.000 | — | 0.0% | 0.0% | 100.0% |
| UN | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-16 | 88 | 8 | 3 | 4 | 3 |
| 2026-06-10 | 100 | 6 | 0 | 6 | 0 |
| 2026-06-02 | 92 | 10 | 3 | 2 | 0 |
| 2026-05-28 | 84 | 2 | 2 | 5 | 0 |
| 2026-05-22 | 98 | 6 | 2 | 7 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Dillon Dingler | 27 | 0.480 | 1.200 | 0.720 | 0.694 | 0.471 | 14.3% | 35.1% | 22.8% |
| CH | Kerry Carpenter | 32 | 0.385 | 0.846 | 0.462 | 0.577 | 0.366 | 10.5% | 36.8% | 25.9% |
| FC | Dillon Dingler | 27 | 0.360 | 0.800 | 0.440 | 0.474 | 0.467 | 18.2% | 33.3% | 13.8% |
| CU | Dillon Dingler | 16 | 0.200 | 0.600 | 0.400 | 0.350 | 0.290 | 12.5% | 23.5% | 35.7% |
| SI | Jahmai Jones | 21 | 0.125 | 0.500 | 0.375 | 0.357 | 0.536 | 15.4% | 21.7% | 14.3% |
| FC | Riley Greene | 18 | 0.333 | 0.667 | 0.333 | 0.467 | 0.443 | 30.0% | 40.9% | 31.0% |
| CH | Wenceel Pérez | 35 | 0.206 | 0.529 | 0.324 | 0.314 | 0.199 | 7.1% | 22.9% | 23.1% |
| FC | Matt Vierling | 18 | 0.385 | 0.692 | 0.308 | 0.486 | 0.477 | 18.2% | 26.3% | 10.7% |
| CU | Riley Greene | 15 | 0.154 | 0.462 | 0.308 | 0.310 | 0.535 | 42.9% | 33.3% | 37.5% |
| SI | Spencer Torkelson | 63 | 0.286 | 0.589 | 0.304 | 0.393 | 0.435 | 19.6% | 34.0% | 12.7% |
| FF | Kerry Carpenter | 54 | 0.213 | 0.511 | 0.298 | 0.339 | 0.302 | 9.7% | 24.7% | 23.9% |
| SI | Wenceel Pérez | 35 | 0.290 | 0.581 | 0.290 | 0.404 | 0.395 | 17.2% | 23.3% | 9.6% |
| FF | Spencer Torkelson | 87 | 0.214 | 0.486 | 0.271 | 0.363 | 0.354 | 17.4% | 29.0% | 22.5% |
| FC | Wenceel Pérez | 16 | 0.267 | 0.533 | 0.267 | 0.359 | 0.236 | 8.3% | 29.2% | 15.6% |
| FF | Hao-Yu Lee | 36 | 0.206 | 0.471 | 0.265 | 0.304 | 0.281 | 21.1% | 35.9% | 29.5% |
| SL | Spencer Torkelson | 38 | 0.235 | 0.500 | 0.265 | 0.349 | 0.302 | 13.6% | 28.0% | 33.3% |
| SL | Kevin Mcgonigle | 36 | 0.194 | 0.452 | 0.258 | 0.328 | 0.373 | 18.2% | 26.8% | 18.3% |
| SI | Gleyber Torres | 44 | 0.333 | 0.583 | 0.250 | 0.447 | 0.329 | 6.5% | 18.6% | 5.7% |
| CH | Colt Keith | 37 | 0.250 | 0.500 | 0.250 | 0.326 | 0.277 | 7.4% | 25.6% | 31.2% |
| CU | Spencer Torkelson | 12 | 0.083 | 0.333 | 0.250 | 0.167 | 0.114 | 0.0% | 13.3% | 34.6% |
| CH | Dillon Dingler | 35 | 0.212 | 0.455 | 0.242 | 0.334 | 0.281 | 8.7% | 36.4% | 32.4% |
| FC | Kerry Carpenter | 20 | 0.412 | 0.647 | 0.235 | 0.458 | 0.370 | 13.3% | 27.3% | 20.5% |
| FF | Dillon Dingler | 83 | 0.301 | 0.534 | 0.233 | 0.388 | 0.449 | 17.2% | 28.1% | 14.2% |
| CU | Colt Keith | 12 | 0.667 | 0.889 | 0.222 | 0.625 | 0.496 | 25.0% | 45.5% | 33.3% |
| SL | Colt Keith | 25 | 0.208 | 0.417 | 0.208 | 0.280 | 0.217 | 21.4% | 36.8% | 40.0% |
| SL | Matt Vierling | 37 | 0.189 | 0.378 | 0.189 | 0.264 | 0.311 | 9.4% | 27.3% | 15.8% |
| FF | Riley Greene | 118 | 0.257 | 0.446 | 0.188 | 0.352 | 0.346 | 14.1% | 23.2% | 21.7% |
| SI | Kevin Mcgonigle | 75 | 0.385 | 0.569 | 0.185 | 0.451 | 0.395 | 6.7% | 31.9% | 5.8% |
| CH | Spencer Torkelson | 32 | 0.172 | 0.345 | 0.172 | 0.263 | 0.270 | 38.5% | 35.1% | 42.5% |
| FF | Gleyber Torres | 66 | 0.226 | 0.396 | 0.170 | 0.354 | 0.374 | 15.8% | 25.0% | 24.0% |


## Home Starting Pitcher: Keider Montero

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1070 |
| Batted/Result Events | 295 |
| Hits Allowed | 58 |
| Walks | 17 |
| Strikeouts | 50 |
| Home Runs | 8 |
| K Event Rate | 16.9% |
| BB Event Rate | 5.8% |
| HR Event Rate | 2.7% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 13.5% | 144 | 0.128 | 0.256 | 0.128 | 0.200 | 0.240 | 3.2% | 17.0% | 25.0% |
| CH | vs R | 1.4% | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.029 | 0.0% | 0.0% | 22.2% |
| FF | vs L | 24.8% | 265 | 0.197 | 0.364 | 0.167 | 0.270 | 0.332 | 10.5% | 23.8% | 11.1% |
| FF | vs R | 8.1% | 87 | 0.250 | 0.400 | 0.150 | 0.316 | 0.268 | 6.2% | 19.4% | 8.9% |
| KC | vs L | 10.0% | 107 | 0.321 | 0.643 | 0.321 | 0.424 | 0.386 | 20.0% | 34.8% | 7.5% |
| KC | vs R | 4.3% | 46 | 0.111 | 0.111 | 0.000 | 0.100 | 0.259 | 0.0% | 44.4% | 42.1% |
| SI | vs L | 3.1% | 33 | 0.143 | 0.143 | 0.000 | 0.129 | 0.283 | 14.3% | 18.8% | 11.1% |
| SI | vs R | 17.3% | 185 | 0.218 | 0.345 | 0.127 | 0.290 | 0.307 | 6.0% | 34.2% | 8.0% |
| SL | vs L | 8.3% | 89 | 0.286 | 0.286 | 0.000 | 0.335 | 0.336 | 0.0% | 25.9% | 16.2% |
| SL | vs R | 9.2% | 98 | 0.242 | 0.424 | 0.182 | 0.283 | 0.262 | 9.5% | 28.6% | 23.1% |
| UN | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-16 | 30 | 2 | 0 | 2 | 0 |
| 2026-06-11 | 96 | 4 | 1 | 4 | 0 |
| 2026-06-06 | 79 | 6 | 1 | 1 | 1 |
| 2026-05-31 | 65 | 2 | 0 | 4 | 0 |
| 2026-05-26 | 89 | 8 | 1 | 7 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KC | Munetaka Murakami | 4 | 0.500 | 1.250 | 0.750 | 0.725 | 0.613 | 50.0% | 50.0% | 42.9% |
| KC | Colson Montgomery | 6 | 0.500 | 1.000 | 0.500 | 0.633 | 0.465 | 25.0% | 50.0% | 33.3% |
| FF | Munetaka Murakami | 90 | 0.257 | 0.714 | 0.457 | 0.476 | 0.463 | 23.9% | 39.3% | 34.9% |
| SL | Everson Pereira | 7 | 0.286 | 0.714 | 0.429 | 0.414 | 0.433 | 20.0% | 40.0% | 44.4% |
| CH | Colson Montgomery | 35 | 0.281 | 0.688 | 0.406 | 0.427 | 0.419 | 18.2% | 25.0% | 38.9% |
| FF | Drew Romo | 29 | 0.125 | 0.500 | 0.375 | 0.328 | 0.328 | 20.0% | 18.4% | 19.6% |
| CH | Munetaka Murakami | 28 | 0.360 | 0.720 | 0.360 | 0.482 | 0.382 | 25.0% | 44.8% | 43.8% |
| SI | Drew Romo | 18 | 0.333 | 0.667 | 0.333 | 0.467 | 0.508 | 26.7% | 47.4% | 16.7% |
| SL | Colson Montgomery | 35 | 0.156 | 0.469 | 0.312 | 0.293 | 0.255 | 12.5% | 25.6% | 38.6% |
| CH | Everson Pereira | 17 | 0.375 | 0.688 | 0.312 | 0.465 | 0.231 | 10.0% | 33.3% | 43.8% |
| CH | Miguel Vargas | 28 | 0.391 | 0.696 | 0.304 | 0.505 | 0.533 | 17.4% | 26.7% | 3.9% |
| SI | Munetaka Murakami | 27 | 0.250 | 0.550 | 0.300 | 0.430 | 0.443 | 36.4% | 25.9% | 31.5% |
| FF | Miguel Vargas | 104 | 0.235 | 0.519 | 0.284 | 0.414 | 0.404 | 17.2% | 24.6% | 22.2% |
| SI | Andrew Benintendi | 37 | 0.312 | 0.594 | 0.281 | 0.412 | 0.373 | 14.8% | 28.1% | 16.7% |
| FF | Andrew Benintendi | 72 | 0.270 | 0.540 | 0.270 | 0.382 | 0.345 | 16.3% | 36.6% | 23.9% |
| SI | Miguel Vargas | 75 | 0.185 | 0.446 | 0.262 | 0.320 | 0.413 | 16.4% | 34.5% | 6.0% |
| FF | Chase Meidroth | 97 | 0.312 | 0.562 | 0.250 | 0.429 | 0.368 | 9.3% | 26.2% | 14.4% |
| SI | Colson Montgomery | 48 | 0.268 | 0.512 | 0.244 | 0.402 | 0.381 | 14.8% | 43.1% | 34.0% |
| SL | Chase Meidroth | 47 | 0.244 | 0.467 | 0.222 | 0.337 | 0.270 | 12.5% | 21.0% | 22.6% |
| SL | Andrew Benintendi | 45 | 0.195 | 0.415 | 0.220 | 0.293 | 0.261 | 19.0% | 24.3% | 48.7% |
| FF | Derek Hill | 37 | 0.188 | 0.406 | 0.219 | 0.309 | 0.307 | 16.7% | 27.3% | 40.0% |
| FF | Sam Antonacci | 72 | 0.357 | 0.571 | 0.214 | 0.481 | 0.454 | 14.6% | 21.6% | 14.7% |
| SL | Tristan Peters | 26 | 0.333 | 0.542 | 0.208 | 0.398 | 0.266 | 0.0% | 14.7% | 32.1% |
| KC | Sam Antonacci | 6 | 0.600 | 0.800 | 0.200 | 0.625 | 0.476 | 0.0% | 33.3% | 0.0% |
| CH | Derek Hill | 18 | 0.375 | 0.562 | 0.188 | 0.411 | 0.444 | 6.7% | 26.3% | 33.3% |
| FF | Colson Montgomery | 119 | 0.189 | 0.368 | 0.179 | 0.286 | 0.271 | 9.1% | 27.5% | 30.9% |
| FF | Tristan Peters | 79 | 0.294 | 0.471 | 0.176 | 0.360 | 0.342 | 5.5% | 18.7% | 18.1% |
| SI | Sam Antonacci | 49 | 0.262 | 0.429 | 0.167 | 0.344 | 0.441 | 8.3% | 32.3% | 5.6% |
| SL | Derek Hill | 20 | 0.300 | 0.450 | 0.150 | 0.325 | 0.261 | 7.1% | 18.2% | 35.0% |
| CH | Andrew Benintendi | 35 | 0.229 | 0.371 | 0.143 | 0.257 | 0.337 | 8.3% | 17.4% | 26.5% |


## Chicago White Sox Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Miguel Vargas | 345 | 0.231 | 0.455 | 0.224 | 0.359 | 0.395 | 13.9% | 28.1% | 17.2% |
| Chase Meidroth | 332 | 0.281 | 0.414 | 0.132 | 0.342 | 0.288 | 5.0% | 23.7% | 18.3% |
| Colson Montgomery | 324 | 0.214 | 0.470 | 0.256 | 0.336 | 0.330 | 13.3% | 31.3% | 34.8% |
| Munetaka Murakami | 264 | 0.236 | 0.546 | 0.310 | 0.394 | 0.379 | 20.5% | 37.1% | 38.9% |
| Andrew Benintendi | 253 | 0.236 | 0.437 | 0.201 | 0.321 | 0.323 | 12.4% | 28.7% | 28.1% |
| Sam Antonacci | 237 | 0.295 | 0.430 | 0.135 | 0.386 | 0.382 | 8.0% | 22.9% | 13.4% |
| Tristan Peters | 225 | 0.285 | 0.440 | 0.155 | 0.350 | 0.302 | 5.0% | 19.3% | 19.6% |
| Edgar Quero | 187 | 0.179 | 0.222 | 0.043 | 0.237 | 0.262 | 2.4% | 21.3% | 21.4% |
| Luisangel Acuña | 154 | 0.218 | 0.239 | 0.021 | 0.230 | 0.266 | 3.4% | 25.9% | 22.0% |
| Drew Romo | 108 | 0.147 | 0.358 | 0.211 | 0.265 | 0.272 | 10.1% | 21.5% | 30.4% |
| Derek Hill | 106 | 0.215 | 0.355 | 0.140 | 0.291 | 0.302 | 8.3% | 20.2% | 33.5% |
| Everson Pereira | 92 | 0.244 | 0.451 | 0.207 | 0.331 | 0.303 | 12.3% | 23.9% | 31.7% |


## Detroit Tigers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kevin Mcgonigle | 343 | 0.277 | 0.425 | 0.147 | 0.364 | 0.366 | 9.0% | 23.7% | 12.9% |
| Riley Greene | 341 | 0.292 | 0.446 | 0.154 | 0.365 | 0.350 | 12.7% | 29.1% | 27.4% |
| Spencer Torkelson | 312 | 0.202 | 0.415 | 0.213 | 0.311 | 0.314 | 14.8% | 27.7% | 28.2% |
| Dillon Dingler | 307 | 0.275 | 0.562 | 0.286 | 0.393 | 0.397 | 12.5% | 28.8% | 19.2% |
| Colt Keith | 235 | 0.264 | 0.380 | 0.116 | 0.314 | 0.323 | 9.4% | 28.6% | 21.5% |
| Matt Vierling | 227 | 0.195 | 0.346 | 0.151 | 0.271 | 0.302 | 6.5% | 21.3% | 14.8% |
| Gleyber Torres | 200 | 0.289 | 0.410 | 0.120 | 0.367 | 0.343 | 8.4% | 18.5% | 20.5% |
| Kerry Carpenter | 191 | 0.217 | 0.446 | 0.229 | 0.327 | 0.303 | 10.2% | 27.7% | 28.5% |
| Wenceel Pérez | 190 | 0.183 | 0.371 | 0.189 | 0.270 | 0.272 | 8.5% | 23.6% | 16.1% |
| Zach Mckinstry | 188 | 0.165 | 0.232 | 0.067 | 0.264 | 0.253 | 2.3% | 11.9% | 13.0% |
| Jahmai Jones | 108 | 0.163 | 0.265 | 0.102 | 0.248 | 0.305 | 7.8% | 28.1% | 30.2% |
| Hao-Yu Lee | 106 | 0.225 | 0.343 | 0.118 | 0.271 | 0.267 | 9.5% | 20.5% | 28.3% |


## Bullpen Fatigue Report

### Chicago White Sox Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brandon Eisert | 2026-06-17 | 1.0 | 13 |
| Chris Murphy | 2026-06-19 | 1.0 | 8 |
| Chris Murphy | 2026-06-20 | 1.0 | 16 |
| Erick Fedde | 2026-06-19 | 4.2 | 78 |
| Joe Rock | 2026-06-20 | 2.1 | 47 |
| Sean Burke | 2026-06-18 | 7.1 | 88 |
| Sean Newcomb | 2026-06-17 | 0.2 | 14 |
| Seranthony Domínguez | 2026-06-19 | 1.0 | 18 |
| Trevor Richards | 2026-06-17 | 2.0 | 44 |
| Trevor Richards | 2026-06-20 | 1.0 | 16 |
| Tyler Davis | 2026-06-17 | 0.1 | 8 |
| Tyler Davis | 2026-06-20 | 0.2 | 28 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Chris Murphy, Joe Rock, Trevor Richards, Tyler Davis


### Detroit Tigers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Drew Anderson | 2026-06-19 | 1.1 | 16 |
| Drew Sommers | 2026-06-17 | 0.1 | 2 |
| Jacob Waguespack | 2026-06-17 | 2.0 | 20 |
| Kenley Jansen | 2026-06-19 | 1.0 | 10 |
| Kenley Jansen | 2026-06-20 | 1.0 | 10 |
| Kyle Finnegan | 2026-06-17 | 1.0 | 26 |
| Tyler Holton | 2026-06-20 | 2.0 | 21 |
| Will Vest | 2026-06-19 | 1.0 | 20 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Kenley Jansen, Tyler Holton



## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SI, CH, SL, FC, CU
- Home pitcher pitch mix to inspect: FF, SI, SL, CH, KC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 5. San Francisco Giants @ Miami Marlins

## Game Context

| Field | Value |
| --- | --- |
| Park | loanDepot park |
| Time | 2026-06-21T17:40:00Z |
| Away Team | San Francisco Giants |
| Home Team | Miami Marlins |
| Away Probable Pitcher | Logan Webb |
| Home Probable Pitcher | Ryan Gusto |


## Away Starting Pitcher: Logan Webb

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1203 |
| Batted/Result Events | 329 |
| Hits Allowed | 76 |
| Walks | 20 |
| Strikeouts | 68 |
| Home Runs | 5 |
| K Event Rate | 20.7% |
| BB Event Rate | 6.1% |
| HR Event Rate | 1.5% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 18.3% | 220 | 0.310 | 0.379 | 0.069 | 0.323 | 0.322 | 2.3% | 29.6% | 23.2% |
| CH | vs R | 5.6% | 67 | 0.111 | 0.111 | 0.000 | 0.100 | 0.114 | 0.0% | 23.5% | 44.4% |
| FC | vs L | 7.1% | 85 | 0.391 | 0.739 | 0.348 | 0.488 | 0.339 | 15.0% | 25.0% | 20.8% |
| FC | vs R | 3.4% | 41 | 0.200 | 0.200 | 0.000 | 0.417 | 0.242 | 0.0% | 8.3% | 21.1% |
| FF | vs L | 8.9% | 107 | 0.121 | 0.152 | 0.030 | 0.153 | 0.229 | 4.3% | 13.6% | 18.3% |
| FF | vs R | 2.9% | 35 | 0.286 | 0.286 | 0.000 | 0.312 | 0.373 | 0.0% | 11.8% | 14.3% |
| SI | vs L | 14.6% | 176 | 0.348 | 0.522 | 0.174 | 0.408 | 0.343 | 7.3% | 31.2% | 8.2% |
| SI | vs R | 18.7% | 225 | 0.167 | 0.242 | 0.076 | 0.243 | 0.342 | 3.4% | 43.0% | 12.7% |
| ST | vs L | 13.5% | 162 | 0.179 | 0.214 | 0.036 | 0.208 | 0.279 | 17.6% | 25.0% | 28.6% |
| ST | vs R | 7.1% | 85 | 0.381 | 0.571 | 0.190 | 0.425 | 0.271 | 11.1% | 13.8% | 14.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-14 | 106 | 7 | 0 | 7 | 0 |
| 2026-06-08 | 99 | 5 | 0 | 7 | 0 |
| 2026-06-03 | 95 | 1 | 1 | 4 | 0 |
| 2026-05-29 | 86 | 3 | 3 | 5 | 0 |
| 2026-05-05 | 62 | 7 | 0 | 4 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Agustín Ramírez | 9 | 0.250 | 0.625 | 0.375 | 0.400 | 0.417 | 14.3% | 15.4% | 40.9% |
| FF | Xavier Edwards | 111 | 0.383 | 0.670 | 0.287 | 0.481 | 0.420 | 8.9% | 19.4% | 6.8% |
| FC | Owen Caissie | 18 | 0.333 | 0.600 | 0.267 | 0.408 | 0.383 | 15.4% | 24.0% | 24.3% |
| CH | Owen Caissie | 26 | 0.333 | 0.583 | 0.250 | 0.387 | 0.310 | 17.6% | 16.7% | 43.9% |
| ST | Connor Norby | 16 | 0.167 | 0.417 | 0.250 | 0.356 | 0.286 | 12.5% | 16.7% | 29.4% |
| FC | Liam Hicks | 19 | 0.250 | 0.500 | 0.250 | 0.376 | 0.361 | 6.2% | 20.0% | 3.0% |
| FF | Owen Caissie | 60 | 0.220 | 0.460 | 0.240 | 0.331 | 0.320 | 17.2% | 21.7% | 22.8% |
| SI | Joe Mack | 19 | 0.294 | 0.529 | 0.235 | 0.434 | 0.375 | 13.3% | 16.0% | 6.9% |
| SI | Otto Lopez | 65 | 0.429 | 0.661 | 0.232 | 0.528 | 0.473 | 11.8% | 45.2% | 5.3% |
| SI | Heriberto Hernandez | 31 | 0.269 | 0.500 | 0.231 | 0.416 | 0.401 | 13.0% | 29.7% | 19.6% |
| CH | Heriberto Hernandez | 15 | 0.200 | 0.400 | 0.200 | 0.313 | 0.318 | 12.5% | 13.3% | 40.7% |
| CH | Liam Hicks | 42 | 0.341 | 0.537 | 0.195 | 0.390 | 0.291 | 2.6% | 19.6% | 13.9% |
| FF | Otto Lopez | 77 | 0.377 | 0.565 | 0.188 | 0.428 | 0.428 | 12.5% | 33.6% | 6.0% |
| FF | Connor Norby | 72 | 0.233 | 0.417 | 0.183 | 0.359 | 0.304 | 17.6% | 23.1% | 31.2% |
| CH | Joe Mack | 18 | 0.176 | 0.353 | 0.176 | 0.250 | 0.290 | 12.5% | 38.5% | 54.1% |
| FF | Liam Hicks | 106 | 0.207 | 0.379 | 0.172 | 0.325 | 0.360 | 6.0% | 22.4% | 5.4% |
| SI | Connor Norby | 50 | 0.341 | 0.512 | 0.171 | 0.414 | 0.386 | 2.5% | 18.3% | 9.5% |
| ST | Graham Pauley | 7 | 0.167 | 0.333 | 0.167 | 0.307 | 0.249 | 0.0% | 28.6% | 22.2% |
| FF | Heriberto Hernandez | 46 | 0.205 | 0.359 | 0.154 | 0.295 | 0.411 | 9.4% | 43.9% | 23.8% |
| FF | Joe Mack | 28 | 0.308 | 0.462 | 0.154 | 0.359 | 0.319 | 5.6% | 25.5% | 10.5% |
| FC | Xavier Edwards | 27 | 0.269 | 0.423 | 0.154 | 0.313 | 0.320 | 4.2% | 31.2% | 5.3% |
| FC | Jakob Marsee | 27 | 0.150 | 0.300 | 0.150 | 0.320 | 0.311 | 0.0% | 17.1% | 11.1% |
| FF | Kyle Stowers | 76 | 0.229 | 0.371 | 0.143 | 0.292 | 0.330 | 11.5% | 30.3% | 30.4% |
| FC | Kyle Stowers | 9 | 0.286 | 0.429 | 0.143 | 0.394 | 0.441 | 0.0% | 42.9% | 37.9% |
| CH | Jakob Marsee | 32 | 0.300 | 0.433 | 0.133 | 0.353 | 0.362 | 4.2% | 37.5% | 26.7% |
| FC | Joe Mack | 9 | 0.250 | 0.375 | 0.125 | 0.317 | 0.358 | 16.7% | 30.0% | 12.5% |
| CH | Kyle Stowers | 34 | 0.212 | 0.333 | 0.121 | 0.274 | 0.199 | 5.3% | 31.4% | 41.3% |
| SI | Kyle Stowers | 32 | 0.231 | 0.346 | 0.115 | 0.361 | 0.396 | 15.8% | 31.2% | 20.0% |
| FF | Jakob Marsee | 115 | 0.198 | 0.312 | 0.115 | 0.299 | 0.316 | 4.0% | 19.9% | 7.6% |
| CH | Otto Lopez | 41 | 0.256 | 0.359 | 0.103 | 0.255 | 0.161 | 3.3% | 12.5% | 25.7% |


## Home Starting Pitcher: Ryan Gusto

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 242 |
| Batted/Result Events | 66 |
| Hits Allowed | 19 |
| Walks | 5 |
| Strikeouts | 10 |
| Home Runs | 2 |
| K Event Rate | 15.2% |
| BB Event Rate | 7.6% |
| HR Event Rate | 3.0% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 16.1% | 39 | 0.200 | 0.200 | 0.000 | 0.227 | 0.264 | 0.0% | 16.7% | 31.6% |
| CH | vs R | 2.9% | 7 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 50.0% | 33.3% |
| CU | vs L | 5.4% | 13 | 0.500 | 0.750 | 0.250 | 0.570 | 0.578 | 25.0% | 66.7% | 0.0% |
| CU | vs R | 0.8% | 2 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| FC | vs L | 10.3% | 25 | 0.222 | 0.222 | 0.000 | 0.250 | 0.480 | 11.1% | 23.1% | 12.5% |
| FC | vs R | 3.3% | 8 | 1.000 | 1.500 | 0.500 | 1.075 | 0.462 | 50.0% | 50.0% | 20.0% |
| FF | vs L | 16.1% | 39 | 0.400 | 0.400 | 0.000 | 0.417 | 0.268 | 0.0% | 42.9% | 11.1% |
| FF | vs R | 12.0% | 29 | 0.333 | 0.333 | 0.000 | 0.357 | 0.505 | 20.0% | 16.7% | 23.5% |
| SI | vs L | 3.7% | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.298 | 0.0% | 16.7% | 0.0% |
| SI | vs R | 8.3% | 20 | 0.333 | 0.333 | 0.000 | 0.300 | 0.178 | 0.0% | 9.1% | 8.3% |
| SL | vs L | 6.6% | 16 | 0.600 | 1.000 | 0.400 | 0.680 | 0.553 | 0.0% | 62.5% | 20.0% |
| SL | vs R | 5.0% | 12 | 0.250 | 1.000 | 0.750 | 0.725 | 0.550 | 33.3% | 50.0% | 28.6% |
| ST | vs L | 2.9% | 7 | 0.333 | 1.333 | 1.000 | 0.667 | 0.670 | 66.7% | 75.0% | 0.0% |
| ST | vs R | 6.6% | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.065 | 0.0% | 16.7% | 40.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 91 | 8 | 3 | 1 | 2 |
| 2026-06-10 | 66 | 3 | 1 | 4 | 0 |
| 2026-06-05 | 33 | 3 | 1 | 1 | 0 |
| 2026-06-02 | 40 | 5 | 0 | 3 | 0 |
| 2026-04-08 | 12 | 0 | 0 | 1 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | Casey Schmitt | 19 | 0.474 | 1.158 | 0.684 | 0.676 | 0.550 | 26.7% | 34.6% | 26.8% |
| FC | Daniel Susac | 5 | 0.600 | 1.200 | 0.600 | 0.760 | 0.533 | 20.0% | 45.5% | 31.2% |
| SL | Heliot Ramos | 20 | 0.450 | 0.900 | 0.450 | 0.568 | 0.417 | 12.5% | 28.6% | 31.1% |
| FF | Bryce Eldridge | 47 | 0.316 | 0.763 | 0.447 | 0.496 | 0.521 | 30.0% | 31.0% | 12.5% |
| ST | Casey Schmitt | 38 | 0.405 | 0.811 | 0.405 | 0.517 | 0.456 | 20.7% | 26.9% | 21.4% |
| FC | Casey Schmitt | 26 | 0.455 | 0.818 | 0.364 | 0.538 | 0.376 | 5.0% | 26.5% | 18.0% |
| FF | Willy Adames | 94 | 0.225 | 0.573 | 0.348 | 0.348 | 0.333 | 12.1% | 27.1% | 21.3% |
| ST | Jung Hoo Lee | 23 | 0.333 | 0.667 | 0.333 | 0.443 | 0.336 | 10.5% | 10.8% | 5.0% |
| FC | Rafael Devers | 29 | 0.440 | 0.760 | 0.320 | 0.514 | 0.335 | 5.0% | 35.7% | 28.6% |
| SL | Harrison Bader | 20 | 0.250 | 0.550 | 0.300 | 0.333 | 0.346 | 16.7% | 37.5% | 48.5% |
| SL | Bryce Eldridge | 18 | 0.412 | 0.706 | 0.294 | 0.489 | 0.208 | 0.0% | 31.8% | 22.9% |
| FF | Drew Gilbert | 62 | 0.294 | 0.529 | 0.235 | 0.410 | 0.339 | 2.3% | 21.6% | 16.7% |
| FF | Rafael Devers | 128 | 0.188 | 0.402 | 0.214 | 0.286 | 0.278 | 15.0% | 27.3% | 37.2% |
| FC | Willy Adames | 31 | 0.286 | 0.500 | 0.214 | 0.353 | 0.314 | 12.0% | 31.0% | 23.7% |
| FF | Jung Hoo Lee | 100 | 0.402 | 0.609 | 0.207 | 0.450 | 0.348 | 4.7% | 22.4% | 7.3% |
| FF | Harrison Bader | 34 | 0.133 | 0.333 | 0.200 | 0.253 | 0.255 | 4.5% | 21.6% | 20.0% |
| ST | Willy Adames | 32 | 0.200 | 0.400 | 0.200 | 0.309 | 0.311 | 10.5% | 23.5% | 31.0% |
| SI | Rafael Devers | 44 | 0.366 | 0.561 | 0.195 | 0.419 | 0.323 | 6.1% | 30.1% | 12.6% |
| SL | Rafael Devers | 35 | 0.242 | 0.424 | 0.182 | 0.287 | 0.300 | 7.7% | 29.3% | 33.3% |
| ST | Luis Arráez | 14 | 0.364 | 0.545 | 0.182 | 0.371 | 0.248 | 0.0% | 2.9% | 7.5% |
| FF | Heliot Ramos | 41 | 0.256 | 0.436 | 0.179 | 0.337 | 0.320 | 13.0% | 14.5% | 25.0% |
| ST | Matt Chapman | 29 | 0.321 | 0.500 | 0.179 | 0.397 | 0.279 | 4.5% | 23.1% | 18.4% |
| SL | Matt Chapman | 46 | 0.195 | 0.366 | 0.171 | 0.287 | 0.295 | 12.5% | 30.6% | 30.8% |
| SI | Casey Schmitt | 72 | 0.262 | 0.431 | 0.169 | 0.317 | 0.378 | 6.9% | 29.2% | 6.4% |
| FC | Drew Gilbert | 21 | 0.167 | 0.333 | 0.167 | 0.281 | 0.326 | 5.9% | 29.6% | 6.2% |
| SI | Matt Chapman | 89 | 0.291 | 0.456 | 0.165 | 0.376 | 0.286 | 4.3% | 26.1% | 12.8% |
| CH | Matt Chapman | 29 | 0.280 | 0.440 | 0.160 | 0.362 | 0.360 | 11.8% | 34.4% | 21.3% |
| CH | Luis Arráez | 36 | 0.152 | 0.303 | 0.152 | 0.194 | 0.239 | 2.9% | 14.8% | 5.0% |
| FC | Patrick Bailey | 15 | 0.214 | 0.357 | 0.143 | 0.273 | 0.449 | 8.3% | 47.6% | 23.3% |
| CH | Drew Gilbert | 23 | 0.227 | 0.364 | 0.136 | 0.311 | 0.273 | 0.0% | 19.2% | 25.6% |


## San Francisco Giants Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Luis Arráez | 332 | 0.321 | 0.441 | 0.120 | 0.351 | 0.302 | 0.3% | 13.6% | 7.4% |
| Rafael Devers | 332 | 0.244 | 0.439 | 0.195 | 0.320 | 0.301 | 10.2% | 28.2% | 28.4% |
| Matt Chapman | 330 | 0.253 | 0.412 | 0.159 | 0.340 | 0.292 | 7.3% | 24.2% | 20.1% |
| Willy Adames | 327 | 0.225 | 0.425 | 0.199 | 0.309 | 0.294 | 9.6% | 25.6% | 26.5% |
| Casey Schmitt | 303 | 0.292 | 0.521 | 0.229 | 0.361 | 0.357 | 12.3% | 27.7% | 20.5% |
| Jung Hoo Lee | 289 | 0.337 | 0.478 | 0.141 | 0.372 | 0.333 | 2.8% | 20.7% | 11.0% |
| Drew Gilbert | 190 | 0.243 | 0.379 | 0.136 | 0.317 | 0.282 | 2.2% | 21.6% | 20.1% |
| Heliot Ramos | 188 | 0.261 | 0.420 | 0.159 | 0.319 | 0.326 | 12.8% | 24.5% | 24.4% |
| Bryce Eldridge | 148 | 0.299 | 0.512 | 0.213 | 0.390 | 0.384 | 12.8% | 28.2% | 21.1% |
| Daniel Susac | 119 | 0.292 | 0.387 | 0.094 | 0.315 | 0.307 | 5.8% | 18.6% | 22.5% |
| Harrison Bader | 114 | 0.167 | 0.352 | 0.185 | 0.244 | 0.272 | 8.2% | 25.0% | 30.6% |
| Patrick Bailey | 102 | 0.160 | 0.191 | 0.032 | 0.198 | 0.283 | 4.3% | 25.6% | 24.6% |


## Miami Marlins Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Otto Lopez | 337 | 0.328 | 0.465 | 0.137 | 0.379 | 0.336 | 7.1% | 29.5% | 18.4% |
| Xavier Edwards | 335 | 0.284 | 0.418 | 0.134 | 0.352 | 0.331 | 5.2% | 19.3% | 14.5% |
| Jakob Marsee | 319 | 0.201 | 0.306 | 0.104 | 0.299 | 0.309 | 3.6% | 23.3% | 17.5% |
| Liam Hicks | 305 | 0.269 | 0.451 | 0.182 | 0.353 | 0.317 | 4.2% | 23.9% | 10.5% |
| Connor Norby | 236 | 0.218 | 0.356 | 0.139 | 0.312 | 0.287 | 9.8% | 21.2% | 29.1% |
| Kyle Stowers | 229 | 0.225 | 0.405 | 0.180 | 0.322 | 0.326 | 9.7% | 29.5% | 33.3% |
| Owen Caissie | 215 | 0.223 | 0.410 | 0.186 | 0.311 | 0.294 | 13.5% | 23.4% | 32.4% |
| Javier Sanoja | 188 | 0.244 | 0.347 | 0.102 | 0.306 | 0.257 | 1.3% | 20.6% | 12.0% |
| Heriberto Hernandez | 171 | 0.243 | 0.408 | 0.164 | 0.337 | 0.351 | 9.1% | 32.2% | 31.9% |
| Agustín Ramírez | 141 | 0.228 | 0.350 | 0.122 | 0.305 | 0.282 | 5.3% | 27.0% | 30.9% |
| Joe Mack | 118 | 0.255 | 0.387 | 0.132 | 0.319 | 0.314 | 9.0% | 23.6% | 20.0% |
| Graham Pauley | 100 | 0.152 | 0.250 | 0.098 | 0.225 | 0.190 | 2.9% | 15.2% | 19.6% |


## Bullpen Fatigue Report

### San Francisco Giants Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Caleb Kilian | 2026-06-17 | 0.2 | 8 |
| Dylan Smith | 2026-06-17 | 1.0 | 21 |
| Dylan Smith | 2026-06-19 | 0.2 | 18 |
| Erik Miller | 2026-06-19 | 0.1 | 5 |
| JT Brubaker | 2026-06-17 | 1.0 | 15 |
| JT Brubaker | 2026-06-20 | 2.1 | 35 |
| Matt Gage | 2026-06-17 | 0.1 | 23 |
| Matt Gage | 2026-06-20 | 0.2 | 28 |
| Robbie Ray | 2026-06-17 | 6.1 | 94 |
| Ryan Walker | 2026-06-17 | 1.0 | 15 |
| Ryan Walker | 2026-06-19 | 0.2 | 8 |
| Sam Hentges | 2026-06-17 | 1.0 | 16 |
| Sam Hentges | 2026-06-19 | 0.1 | 11 |
| Tristan Beck | 2026-06-17 | 0.2 | 8 |
| Tristan Beck | 2026-06-20 | 2.0 | 18 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** JT Brubaker, Matt Gage, Tristan Beck


### Miami Marlins Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Anthony Bender | 2026-06-19 | 1.1 | 14 |
| Anthony Bender | 2026-06-20 | 0.2 | 13 |
| Cade Gibson | 2026-06-19 | 1.2 | 21 |
| Cade Gibson | 2026-06-20 | 1.0 | 25 |
| Calvin Faucher | 2026-06-19 | 0.2 | 9 |
| John King | 2026-06-17 | 1.0 | 15 |
| John King | 2026-06-19 | 1.1 | 20 |
| Michael Petersen | 2026-06-17 | 1.0 | 17 |
| Michael Petersen | 2026-06-19 | 1.0 | 17 |
| Pete Fairbanks | 2026-06-19 | 1.0 | 17 |
| Pete Fairbanks | 2026-06-20 | 1.0 | 15 |
| Tyler Zuber | 2026-06-17 | 1.0 | 9 |
| Tyler Zuber | 2026-06-19 | 0.2 | 12 |
| Tyler Zuber | 2026-06-20 | 1.1 | 22 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Anthony Bender, Cade Gibson, Pete Fairbanks, Tyler Zuber



## Final Game Dissection

- Away pitcher pitch mix to inspect: SI, CH, ST, FF, FC
- Home pitcher pitch mix to inspect: FF, CH, FC, SI, SL, ST
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 6. Cleveland Guardians @ Houston Astros

## Game Context

| Field | Value |
| --- | --- |
| Park | Daikin Park |
| Time | 2026-06-21T18:10:00Z |
| Away Team | Cleveland Guardians |
| Home Team | Houston Astros |
| Away Probable Pitcher | Slade Cecconi |
| Home Probable Pitcher | Kai-Wei Teng |


## Away Starting Pitcher: Slade Cecconi

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1335 |
| Batted/Result Events | 354 |
| Hits Allowed | 86 |
| Walks | 27 |
| Strikeouts | 67 |
| Home Runs | 11 |
| K Event Rate | 18.9% |
| BB Event Rate | 7.6% |
| HR Event Rate | 3.1% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 1.6% | 21 | 0.500 | 0.500 | 0.000 | 0.450 | 0.249 | 0.0% | 0.0% | 30.0% |
| CH | vs R | 0.1% | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.314 | 0.0% | 100.0% | 0.0% |
| CU | vs L | 11.6% | 155 | 0.129 | 0.226 | 0.097 | 0.208 | 0.239 | 9.1% | 21.1% | 30.6% |
| CU | vs R | 3.7% | 50 | 0.500 | 1.000 | 0.500 | 0.631 | 0.658 | 16.7% | 40.0% | 31.2% |
| FC | vs L | 13.6% | 181 | 0.233 | 0.395 | 0.163 | 0.323 | 0.342 | 9.4% | 31.0% | 16.7% |
| FC | vs R | 12.5% | 167 | 0.200 | 0.314 | 0.114 | 0.259 | 0.223 | 3.7% | 8.2% | 26.4% |
| FF | vs L | 18.5% | 247 | 0.302 | 0.460 | 0.159 | 0.356 | 0.342 | 8.0% | 26.4% | 14.7% |
| FF | vs R | 11.3% | 151 | 0.211 | 0.421 | 0.211 | 0.300 | 0.376 | 22.2% | 25.9% | 17.6% |
| SI | vs L | 8.1% | 108 | 0.321 | 0.321 | 0.000 | 0.303 | 0.356 | 3.7% | 27.3% | 4.1% |
| SI | vs R | 9.7% | 130 | 0.333 | 0.400 | 0.067 | 0.403 | 0.350 | 0.0% | 26.7% | 11.0% |
| SL | vs L | 1.2% | 16 | 0.000 | 0.000 | 0.000 | 0.140 | 0.185 | 0.0% | 66.7% | 57.1% |
| SL | vs R | 1.3% | 17 | 0.250 | 0.250 | 0.000 | 0.225 | 0.253 | 0.0% | 25.0% | 42.9% |
| ST | vs L | 2.1% | 28 | 1.000 | 1.000 | 0.000 | 0.833 | 0.502 | 0.0% | 0.0% | 11.1% |
| ST | vs R | 4.5% | 60 | 0.333 | 0.917 | 0.583 | 0.473 | 0.351 | 18.2% | 27.8% | 32.1% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-16 | 82 | 3 | 2 | 4 | 1 |
| 2026-06-09 | 87 | 6 | 2 | 7 | 1 |
| 2026-06-04 | 82 | 4 | 1 | 4 | 0 |
| 2026-05-29 | 69 | 7 | 0 | 3 | 0 |
| 2026-05-23 | 86 | 6 | 1 | 5 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Isaac Paredes | 26 | 0.438 | 0.875 | 0.438 | 0.583 | 0.490 | 6.2% | 11.4% | 7.1% |
| CU | Yordan Álvarez | 35 | 0.333 | 0.758 | 0.424 | 0.469 | 0.578 | 25.0% | 51.5% | 27.7% |
| FC | Brice Matthews | 15 | 0.333 | 0.733 | 0.400 | 0.567 | 0.521 | 15.4% | 27.8% | 20.8% |
| FF | Yordan Álvarez | 90 | 0.320 | 0.707 | 0.387 | 0.473 | 0.498 | 19.6% | 29.3% | 15.5% |
| SI | Brice Matthews | 35 | 0.276 | 0.621 | 0.345 | 0.454 | 0.385 | 17.4% | 27.5% | 24.1% |
| FF | Yainer Diaz | 31 | 0.250 | 0.536 | 0.286 | 0.365 | 0.339 | 13.6% | 21.4% | 23.3% |
| SI | Isaac Paredes | 64 | 0.392 | 0.647 | 0.255 | 0.511 | 0.378 | 8.5% | 32.4% | 8.1% |
| FC | Yordan Álvarez | 31 | 0.286 | 0.536 | 0.250 | 0.382 | 0.485 | 18.2% | 26.2% | 16.7% |
| CU | José Altuve | 5 | 0.500 | 0.750 | 0.250 | 0.570 | 0.416 | 0.0% | 16.7% | 30.0% |
| FF | Christian Walker | 93 | 0.195 | 0.442 | 0.247 | 0.352 | 0.315 | 9.1% | 21.3% | 21.9% |
| FC | Christian Vázquez | 13 | 0.231 | 0.462 | 0.231 | 0.292 | 0.257 | 9.1% | 12.5% | 10.3% |
| CU | Jeremy Peña | 14 | 0.231 | 0.462 | 0.231 | 0.321 | 0.241 | 16.7% | 33.3% | 52.4% |
| SI | Jake Meyers | 26 | 0.391 | 0.609 | 0.217 | 0.435 | 0.414 | 15.0% | 29.4% | 20.0% |
| FF | Cam Smith | 90 | 0.267 | 0.480 | 0.213 | 0.373 | 0.392 | 17.5% | 32.1% | 20.8% |
| FF | José Altuve | 74 | 0.294 | 0.500 | 0.206 | 0.368 | 0.328 | 13.0% | 39.7% | 23.6% |
| FF | Isaac Paredes | 93 | 0.207 | 0.390 | 0.183 | 0.315 | 0.335 | 8.7% | 25.4% | 11.0% |
| FF | Joey Loperfido | 37 | 0.400 | 0.567 | 0.167 | 0.472 | 0.418 | 8.3% | 36.4% | 20.3% |
| CU | Isaac Paredes | 20 | 0.167 | 0.333 | 0.167 | 0.260 | 0.336 | 15.4% | 18.5% | 22.0% |
| SI | Christian Walker | 69 | 0.295 | 0.459 | 0.164 | 0.407 | 0.377 | 10.7% | 33.7% | 8.3% |
| FC | José Altuve | 19 | 0.211 | 0.368 | 0.158 | 0.247 | 0.352 | 11.8% | 28.0% | 12.9% |
| FF | Jeremy Peña | 37 | 0.344 | 0.500 | 0.156 | 0.411 | 0.446 | 7.4% | 20.6% | 10.0% |
| FF | Christian Vázquez | 73 | 0.219 | 0.375 | 0.156 | 0.295 | 0.265 | 3.7% | 12.7% | 15.2% |
| SI | Yordan Álvarez | 58 | 0.326 | 0.478 | 0.152 | 0.422 | 0.452 | 11.1% | 34.8% | 11.8% |
| FC | Cam Smith | 21 | 0.200 | 0.350 | 0.150 | 0.257 | 0.445 | 10.5% | 20.6% | 20.8% |
| FF | Jake Meyers | 45 | 0.286 | 0.429 | 0.143 | 0.354 | 0.294 | 11.1% | 21.0% | 10.4% |
| CU | Cam Smith | 9 | 0.286 | 0.429 | 0.143 | 0.317 | 0.349 | 0.0% | 20.0% | 12.0% |
| FF | Carlos Correa | 36 | 0.267 | 0.400 | 0.133 | 0.357 | 0.315 | 9.1% | 20.8% | 13.0% |
| FF | Brice Matthews | 72 | 0.274 | 0.403 | 0.129 | 0.343 | 0.329 | 12.8% | 25.6% | 36.4% |
| CU | Christian Walker | 28 | 0.077 | 0.192 | 0.115 | 0.186 | 0.229 | 12.5% | 39.3% | 39.6% |
| SI | Carlos Correa | 42 | 0.324 | 0.432 | 0.108 | 0.374 | 0.430 | 8.8% | 30.9% | 3.3% |


## Home Starting Pitcher: Kai-Wei Teng

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 954 |
| Batted/Result Events | 243 |
| Hits Allowed | 47 |
| Walks | 26 |
| Strikeouts | 59 |
| Home Runs | 9 |
| K Event Rate | 24.3% |
| BB Event Rate | 10.7% |
| HR Event Rate | 3.7% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 8.8% | 84 | 0.250 | 0.500 | 0.250 | 0.333 | 0.432 | 5.9% | 28.6% | 22.5% |
| CH | vs R | 0.7% | 7 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CU | vs L | 8.0% | 76 | 0.250 | 0.250 | 0.000 | 0.293 | 0.293 | 25.0% | 30.0% | 50.0% |
| CU | vs R | 2.2% | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.052 | 0.0% | 25.0% | 44.4% |
| FF | vs L | 14.2% | 135 | 0.462 | 0.923 | 0.462 | 0.600 | 0.373 | 4.5% | 28.3% | 21.7% |
| FF | vs R | 11.5% | 110 | 0.263 | 0.263 | 0.000 | 0.300 | 0.350 | 7.1% | 21.2% | 16.3% |
| SI | vs L | 4.3% | 41 | 0.300 | 0.800 | 0.500 | 0.577 | 0.422 | 10.0% | 41.7% | 13.3% |
| SI | vs R | 13.4% | 128 | 0.154 | 0.192 | 0.038 | 0.225 | 0.318 | 4.5% | 23.3% | 17.0% |
| SL | vs L | 1.3% | 12 | 0.000 | 0.000 | 0.000 | 0.467 | 0.477 | 0.0% | 0.0% | 66.7% |
| SL | vs R | 0.9% | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.031 | 0.0% | 0.0% | 66.7% |
| ST | vs L | 14.2% | 135 | 0.143 | 0.343 | 0.200 | 0.293 | 0.342 | 9.1% | 20.0% | 30.3% |
| ST | vs R | 20.5% | 196 | 0.182 | 0.309 | 0.127 | 0.251 | 0.265 | 5.6% | 22.0% | 31.5% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 81 | 6 | 2 | 9 | 3 |
| 2026-06-09 | 93 | 7 | 3 | 5 | 0 |
| 2026-06-04 | 87 | 7 | 2 | 1 | 1 |
| 2026-05-29 | 91 | 3 | 4 | 7 | 2 |
| 2026-05-23 | 89 | 2 | 3 | 6 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Angel Martínez | 16 | 0.333 | 1.000 | 0.667 | 0.553 | 0.490 | 27.3% | 26.9% | 24.3% |
| FF | José Ramírez | 83 | 0.292 | 0.653 | 0.361 | 0.426 | 0.411 | 10.9% | 30.6% | 10.5% |
| SI | David Fry | 21 | 0.421 | 0.737 | 0.316 | 0.512 | 0.380 | 6.7% | 21.2% | 20.8% |
| CH | Rhys Hoskins | 24 | 0.105 | 0.421 | 0.316 | 0.254 | 0.265 | 16.7% | 42.9% | 40.0% |
| ST | Brayan Rocchio | 12 | 0.200 | 0.500 | 0.300 | 0.433 | 0.297 | 11.1% | 14.3% | 25.0% |
| CU | Rhys Hoskins | 13 | 0.300 | 0.600 | 0.300 | 0.396 | 0.278 | 0.0% | 55.6% | 18.2% |
| CH | Bo Naylor | 11 | 0.200 | 0.500 | 0.300 | 0.327 | 0.356 | 14.3% | 11.1% | 26.9% |
| FF | Travis Bazzana | 75 | 0.313 | 0.597 | 0.284 | 0.421 | 0.333 | 6.9% | 24.5% | 13.4% |
| ST | Travis Bazzana | 11 | 0.182 | 0.455 | 0.273 | 0.264 | 0.241 | 14.3% | 20.0% | 28.6% |
| FF | Daniel Schneemann | 61 | 0.218 | 0.491 | 0.273 | 0.335 | 0.358 | 16.2% | 21.9% | 23.5% |
| SI | Travis Bazzana | 46 | 0.324 | 0.568 | 0.243 | 0.442 | 0.410 | 8.8% | 36.8% | 16.2% |
| ST | Chase Delauter | 19 | 0.235 | 0.471 | 0.235 | 0.339 | 0.355 | 0.0% | 42.1% | 9.1% |
| FF | Angel Martínez | 64 | 0.179 | 0.411 | 0.232 | 0.305 | 0.318 | 11.1% | 19.2% | 11.1% |
| CU | Daniel Schneemann | 13 | 0.308 | 0.538 | 0.231 | 0.431 | 0.325 | 9.1% | 11.1% | 10.0% |
| CU | Chase Delauter | 14 | 0.077 | 0.308 | 0.231 | 0.257 | 0.262 | 8.3% | 25.0% | 15.8% |
| CH | Travis Bazzana | 16 | 0.143 | 0.357 | 0.214 | 0.269 | 0.187 | 0.0% | 16.7% | 51.5% |
| FF | David Fry | 50 | 0.205 | 0.410 | 0.205 | 0.356 | 0.285 | 7.1% | 28.6% | 22.2% |
| FF | Rhys Hoskins | 69 | 0.185 | 0.389 | 0.204 | 0.343 | 0.307 | 7.9% | 24.0% | 22.9% |
| FF | Chase Delauter | 100 | 0.306 | 0.506 | 0.200 | 0.386 | 0.330 | 11.4% | 20.8% | 13.2% |
| ST | Kyle Manzardo | 19 | 0.188 | 0.375 | 0.188 | 0.311 | 0.330 | 16.7% | 9.1% | 36.1% |
| FF | Kyle Manzardo | 75 | 0.277 | 0.446 | 0.169 | 0.375 | 0.334 | 11.6% | 20.2% | 23.2% |
| SI | Kyle Manzardo | 41 | 0.306 | 0.472 | 0.167 | 0.401 | 0.481 | 16.0% | 41.9% | 23.3% |
| CU | José Ramírez | 17 | 0.333 | 0.500 | 0.167 | 0.500 | 0.431 | 0.0% | 37.5% | 20.8% |
| FF | Brayan Rocchio | 88 | 0.311 | 0.473 | 0.162 | 0.382 | 0.371 | 3.1% | 20.8% | 14.7% |
| CH | José Ramírez | 60 | 0.214 | 0.375 | 0.161 | 0.296 | 0.322 | 4.3% | 29.6% | 21.5% |
| SI | Bo Naylor | 15 | 0.462 | 0.615 | 0.154 | 0.500 | 0.343 | 0.0% | 31.0% | 3.2% |
| SI | Rhys Hoskins | 53 | 0.209 | 0.349 | 0.140 | 0.325 | 0.335 | 13.9% | 34.4% | 21.0% |
| SI | Chase Delauter | 42 | 0.361 | 0.500 | 0.139 | 0.421 | 0.406 | 0.0% | 30.9% | 3.4% |
| CH | Austin Hedges | 9 | 0.222 | 0.333 | 0.111 | 0.439 | 0.366 | 12.5% | 41.7% | 23.5% |
| CH | Angel Martínez | 47 | 0.239 | 0.348 | 0.109 | 0.253 | 0.287 | 7.5% | 28.1% | 21.3% |


## Cleveland Guardians Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| José Ramírez | 329 | 0.247 | 0.452 | 0.205 | 0.352 | 0.355 | 7.9% | 30.6% | 15.1% |
| Steven Kwan | 309 | 0.202 | 0.257 | 0.054 | 0.280 | 0.303 | 0.4% | 8.0% | 6.8% |
| Brayan Rocchio | 291 | 0.268 | 0.398 | 0.130 | 0.339 | 0.314 | 3.2% | 21.9% | 20.6% |
| Chase Delauter | 290 | 0.281 | 0.453 | 0.172 | 0.358 | 0.341 | 6.9% | 25.7% | 13.4% |
| Angel Martínez | 260 | 0.247 | 0.469 | 0.222 | 0.322 | 0.306 | 8.9% | 23.8% | 16.8% |
| Kyle Manzardo | 257 | 0.238 | 0.423 | 0.185 | 0.334 | 0.316 | 12.7% | 24.7% | 29.7% |
| Rhys Hoskins | 236 | 0.193 | 0.406 | 0.214 | 0.326 | 0.290 | 11.8% | 28.0% | 28.0% |
| Daniel Schneemann | 227 | 0.218 | 0.364 | 0.146 | 0.295 | 0.293 | 7.4% | 22.7% | 30.3% |
| Travis Bazzana | 207 | 0.291 | 0.520 | 0.229 | 0.392 | 0.332 | 6.4% | 26.5% | 22.9% |
| David Fry | 135 | 0.235 | 0.417 | 0.183 | 0.338 | 0.272 | 6.5% | 21.7% | 28.3% |
| Austin Hedges | 120 | 0.262 | 0.350 | 0.087 | 0.325 | 0.277 | 2.3% | 20.4% | 22.7% |
| Bo Naylor | 108 | 0.152 | 0.242 | 0.091 | 0.207 | 0.295 | 9.7% | 24.3% | 14.9% |


## Houston Astros Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yordan Álvarez | 348 | 0.313 | 0.609 | 0.296 | 0.431 | 0.482 | 18.1% | 31.1% | 17.1% |
| Christian Walker | 332 | 0.237 | 0.480 | 0.243 | 0.352 | 0.313 | 10.9% | 28.2% | 26.3% |
| Isaac Paredes | 304 | 0.235 | 0.408 | 0.173 | 0.340 | 0.324 | 6.7% | 23.4% | 16.3% |
| Cam Smith | 303 | 0.219 | 0.353 | 0.134 | 0.300 | 0.335 | 13.1% | 29.0% | 29.3% |
| José Altuve | 249 | 0.232 | 0.388 | 0.156 | 0.310 | 0.301 | 7.4% | 25.2% | 23.9% |
| Brice Matthews | 204 | 0.210 | 0.366 | 0.156 | 0.300 | 0.274 | 9.8% | 24.2% | 35.9% |
| Christian Vázquez | 175 | 0.222 | 0.335 | 0.114 | 0.278 | 0.239 | 2.3% | 14.2% | 16.9% |
| Jeremy Peña | 171 | 0.284 | 0.452 | 0.168 | 0.364 | 0.348 | 4.7% | 24.5% | 25.2% |
| Carlos Correa | 149 | 0.281 | 0.414 | 0.133 | 0.356 | 0.364 | 9.8% | 22.4% | 21.2% |
| Jake Meyers | 139 | 0.211 | 0.328 | 0.117 | 0.277 | 0.256 | 8.0% | 16.6% | 20.4% |
| Yainer Diaz | 127 | 0.242 | 0.350 | 0.108 | 0.284 | 0.271 | 4.0% | 19.1% | 21.2% |
| Joey Loperfido | 103 | 0.253 | 0.333 | 0.080 | 0.315 | 0.310 | 4.8% | 22.0% | 29.5% |


## Bullpen Fatigue Report

### Cleveland Guardians Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Cade Smith | 2026-06-18 | 1.1 | 22 |
| Colin Holderman | 2026-06-18 | 0.1 | 17 |
| Daniel Espino | 2026-06-17 | 1.0 | 12 |
| Daniel Espino | 2026-06-19 | 1.0 | 20 |
| Erik Sabrowski | 2026-06-19 | 0.1 | 20 |
| Hunter Gaddis | 2026-06-18 | 0.2 | 21 |
| Matt Festa | 2026-06-19 | 0.2 | 7 |
| Matt Festa | 2026-06-20 | 1.0 | 15 |
| Shawn Armstrong | 2026-06-17 | 1.0 | 13 |
| Shawn Armstrong | 2026-06-19 | 0.2 | 17 |
| Tim Herrin | 2026-06-18 | 0.2 | 12 |
| Will Dion | 2026-06-17 | 1.0 | 28 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Matt Festa


### Houston Astros Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| AJ Blubaugh | 2026-06-20 | 1.0 | 16 |
| Bryan Abreu | 2026-06-20 | 1.0 | 11 |
| Enyel De Los Santos | 2026-06-17 | 1.0 | 13 |
| Josh Hader | 2026-06-17 | 1.0 | 15 |
| Mike Burrows | 2026-06-19 | 1.0 | 7 |
| Nate Pearson | 2026-06-20 | 1.0 | 24 |
| Steven Okert | 2026-06-19 | 2.0 | 25 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** AJ Blubaugh, Bryan Abreu, Nate Pearson



## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, FC, SI, CU
- Home pitcher pitch mix to inspect: ST, FF, SI, CU, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 7. St. Louis Cardinals @ Kansas City Royals

## Game Context

| Field | Value |
| --- | --- |
| Park | Kauffman Stadium |
| Time | 2026-06-21T18:10:00Z |
| Away Team | St. Louis Cardinals |
| Home Team | Kansas City Royals |
| Away Probable Pitcher | Dustin May |
| Home Probable Pitcher | Stephen Kolek |


## Away Starting Pitcher: Dustin May

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1332 |
| Batted/Result Events | 352 |
| Hits Allowed | 76 |
| Walks | 22 |
| Strikeouts | 78 |
| Home Runs | 5 |
| K Event Rate | 22.2% |
| BB Event Rate | 6.2% |
| HR Event Rate | 1.4% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 7.4% | 98 | 0.261 | 0.478 | 0.217 | 0.313 | 0.302 | 11.1% | 23.5% | 7.3% |
| CH | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | 0.000 | — | 0.0% | 0.0% | 0.0% |
| CU | vs L | 6.2% | 83 | 0.333 | 0.444 | 0.111 | 0.375 | 0.348 | 0.0% | 33.3% | 38.1% |
| CU | vs R | 0.8% | 10 | 0.333 | 0.667 | 0.333 | 0.417 | 0.448 | 0.0% | 33.3% | 0.0% |
| FC | vs L | 16.9% | 225 | 0.304 | 0.375 | 0.071 | 0.313 | 0.279 | 2.0% | 24.0% | 17.3% |
| FC | vs R | 4.7% | 62 | 0.333 | 0.417 | 0.083 | 0.329 | 0.236 | 10.0% | 23.5% | 41.9% |
| FF | vs L | 17.3% | 230 | 0.306 | 0.490 | 0.184 | 0.391 | 0.361 | 9.8% | 33.3% | 14.4% |
| FF | vs R | 8.1% | 108 | 0.080 | 0.120 | 0.040 | 0.131 | 0.151 | 0.0% | 14.7% | 24.5% |
| PO | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs L | 2.9% | 39 | 0.385 | 0.462 | 0.077 | 0.396 | 0.391 | 9.1% | 41.2% | 5.6% |
| SI | vs R | 15.5% | 206 | 0.175 | 0.281 | 0.105 | 0.251 | 0.302 | 6.4% | 38.8% | 16.7% |
| ST | vs L | 10.7% | 142 | 0.140 | 0.233 | 0.093 | 0.249 | 0.230 | 5.6% | 14.3% | 39.1% |
| ST | vs R | 9.5% | 127 | 0.219 | 0.250 | 0.031 | 0.244 | 0.304 | 8.7% | 25.6% | 25.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 101 | 1 | 1 | 9 | 0 |
| 2026-06-09 | 101 | 4 | 1 | 6 | 0 |
| 2026-06-02 | 90 | 5 | 2 | 9 | 0 |
| 2026-05-27 | 87 | 2 | 0 | 9 | 0 |
| 2026-05-21 | 91 | 6 | 2 | 7 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Carter Jensen | 19 | 0.294 | 0.824 | 0.529 | 0.521 | 0.417 | 27.3% | 33.3% | 26.5% |
| SI | Starling Marte | 11 | 0.500 | 0.900 | 0.400 | 0.605 | 0.614 | 22.2% | 33.3% | 5.0% |
| SI | Salvador Pérez | 42 | 0.361 | 0.722 | 0.361 | 0.458 | 0.440 | 16.2% | 27.0% | 10.2% |
| FC | Michael Massey | 15 | 0.214 | 0.571 | 0.357 | 0.313 | 0.325 | 7.7% | 36.0% | 13.8% |
| FC | Bobby Witt | 32 | 0.310 | 0.655 | 0.345 | 0.411 | 0.473 | 18.5% | 28.6% | 22.4% |
| FF | Jac Caglianone | 69 | 0.323 | 0.661 | 0.339 | 0.443 | 0.445 | 26.3% | 30.6% | 23.9% |
| FC | Vinnie Pasquantino | 12 | 0.200 | 0.500 | 0.300 | 0.358 | 0.378 | 11.1% | 29.6% | 15.2% |
| ST | Isaac Collins | 12 | 0.273 | 0.545 | 0.273 | 0.375 | 0.324 | 14.3% | 28.6% | 23.8% |
| SI | Carter Jensen | 36 | 0.394 | 0.636 | 0.242 | 0.462 | 0.347 | 3.7% | 33.3% | 13.2% |
| SI | Lane Thomas | 43 | 0.206 | 0.441 | 0.235 | 0.344 | 0.379 | 9.7% | 31.4% | 5.2% |
| FF | Nick Loftin | 58 | 0.261 | 0.478 | 0.217 | 0.359 | 0.329 | 9.8% | 18.3% | 6.3% |
| FC | Nick Loftin | 15 | 0.214 | 0.429 | 0.214 | 0.297 | 0.311 | 14.3% | 47.1% | 13.6% |
| FF | Kyle Isbel | 62 | 0.358 | 0.566 | 0.208 | 0.417 | 0.274 | 4.7% | 15.3% | 7.8% |
| FF | Michael Massey | 79 | 0.243 | 0.446 | 0.203 | 0.314 | 0.270 | 9.5% | 22.9% | 16.1% |
| FF | Lane Thomas | 75 | 0.211 | 0.404 | 0.193 | 0.365 | 0.334 | 9.8% | 20.2% | 12.3% |
| FF | Carter Jensen | 76 | 0.188 | 0.375 | 0.188 | 0.291 | 0.274 | 7.1% | 18.3% | 27.3% |
| ST | Jac Caglianone | 33 | 0.133 | 0.300 | 0.167 | 0.255 | 0.300 | 15.8% | 30.6% | 29.0% |
| SI | Isaac Collins | 35 | 0.300 | 0.467 | 0.167 | 0.369 | 0.303 | 3.8% | 29.3% | 4.1% |
| FF | Bobby Witt | 89 | 0.243 | 0.400 | 0.157 | 0.367 | 0.402 | 12.2% | 26.7% | 16.6% |
| ST | Maikel García | 29 | 0.154 | 0.308 | 0.154 | 0.222 | 0.256 | 5.9% | 13.0% | 32.4% |
| FF | Salvador Pérez | 76 | 0.243 | 0.386 | 0.143 | 0.286 | 0.350 | 17.6% | 27.6% | 22.2% |
| FF | Vinnie Pasquantino | 120 | 0.260 | 0.394 | 0.135 | 0.327 | 0.325 | 10.8% | 26.1% | 7.4% |
| SI | Bobby Witt | 60 | 0.309 | 0.436 | 0.127 | 0.370 | 0.413 | 13.0% | 47.3% | 10.3% |
| FC | Maikel García | 27 | 0.292 | 0.417 | 0.125 | 0.350 | 0.330 | 10.0% | 35.9% | 17.0% |
| ST | Kyle Isbel | 16 | 0.062 | 0.188 | 0.125 | 0.100 | 0.156 | 0.0% | 26.7% | 15.8% |
| SI | Vinnie Pasquantino | 57 | 0.188 | 0.312 | 0.125 | 0.295 | 0.356 | 4.8% | 29.2% | 3.8% |
| ST | Lane Thomas | 11 | 0.333 | 0.444 | 0.111 | 0.341 | 0.313 | 0.0% | 27.3% | 4.0% |
| SI | Nick Loftin | 21 | 0.278 | 0.389 | 0.111 | 0.314 | 0.254 | 0.0% | 17.2% | 8.1% |
| FF | Maikel García | 92 | 0.313 | 0.422 | 0.108 | 0.358 | 0.343 | 5.6% | 26.2% | 12.4% |
| ST | Bobby Witt | 48 | 0.362 | 0.468 | 0.106 | 0.371 | 0.318 | 8.6% | 30.6% | 32.5% |


## Home Starting Pitcher: Stephen Kolek

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 738 |
| Batted/Result Events | 199 |
| Hits Allowed | 42 |
| Walks | 10 |
| Strikeouts | 34 |
| Home Runs | 5 |
| K Event Rate | 17.1% |
| BB Event Rate | 5.0% |
| HR Event Rate | 2.5% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 11.8% | 87 | 0.333 | 0.333 | 0.000 | 0.316 | 0.366 | 5.0% | 21.9% | 16.3% |
| CH | vs R | 0.8% | 6 | 0.250 | 0.250 | 0.000 | 0.320 | 0.322 | 0.0% | 33.3% | 40.0% |
| FC | vs L | 10.2% | 75 | 0.167 | 0.500 | 0.333 | 0.272 | 0.272 | 7.7% | 24.1% | 15.8% |
| FC | vs R | 0.9% | 7 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 50.0% |
| FF | vs L | 19.4% | 143 | 0.208 | 0.250 | 0.042 | 0.294 | 0.313 | 4.2% | 12.7% | 13.9% |
| FF | vs R | 8.5% | 63 | 0.083 | 0.167 | 0.083 | 0.150 | 0.175 | 11.1% | 21.1% | 25.0% |
| SI | vs L | 6.1% | 45 | 0.190 | 0.238 | 0.048 | 0.211 | 0.261 | 5.9% | 30.8% | 0.0% |
| SI | vs R | 16.1% | 119 | 0.344 | 0.531 | 0.188 | 0.430 | 0.337 | 9.7% | 40.0% | 5.8% |
| SL | vs L | 5.6% | 41 | 0.118 | 0.118 | 0.000 | 0.106 | 0.115 | 0.0% | 13.3% | 40.0% |
| SL | vs R | 11.1% | 82 | 0.143 | 0.429 | 0.286 | 0.274 | 0.324 | 13.3% | 42.1% | 46.2% |
| ST | vs L | 4.2% | 31 | 0.500 | 1.000 | 0.500 | 0.650 | 0.266 | 0.0% | 50.0% | 33.3% |
| ST | vs R | 5.1% | 38 | 0.231 | 0.308 | 0.077 | 0.235 | 0.344 | 0.0% | 33.3% | 6.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-14 | 98 | 5 | 1 | 4 | 0 |
| 2026-06-09 | 86 | 8 | 1 | 3 | 0 |
| 2026-06-03 | 96 | 6 | 2 | 8 | 1 |
| 2026-05-29 | 91 | 6 | 1 | 5 | 1 |
| 2026-05-23 | 108 | 4 | 1 | 2 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Nathan Church | 12 | 0.600 | 1.500 | 0.900 | 0.838 | 0.513 | 10.0% | 33.3% | 16.1% |
| SL | Ramón Urías | 14 | 0.273 | 0.636 | 0.364 | 0.461 | 0.370 | 10.0% | 31.2% | 23.8% |
| FF | Jj Wetherholt | 111 | 0.266 | 0.574 | 0.309 | 0.405 | 0.425 | 19.7% | 30.5% | 21.8% |
| ST | Ramón Urías | 12 | 0.100 | 0.400 | 0.300 | 0.283 | 0.277 | 11.1% | 10.0% | 33.3% |
| FF | Jordan Walker | 84 | 0.282 | 0.577 | 0.295 | 0.377 | 0.379 | 19.0% | 30.4% | 15.1% |
| CH | Jordan Walker | 39 | 0.333 | 0.611 | 0.278 | 0.469 | 0.350 | 14.3% | 39.4% | 40.3% |
| FC | Alec Burleson | 27 | 0.136 | 0.409 | 0.273 | 0.285 | 0.383 | 11.1% | 27.5% | 18.3% |
| FF | Nolan Gorman | 77 | 0.262 | 0.525 | 0.262 | 0.399 | 0.361 | 15.0% | 29.7% | 33.1% |
| FF | Alec Burleson | 85 | 0.312 | 0.558 | 0.247 | 0.401 | 0.463 | 16.1% | 34.0% | 22.8% |
| ST | Jordan Walker | 46 | 0.220 | 0.463 | 0.244 | 0.351 | 0.355 | 9.7% | 30.0% | 33.7% |
| SI | Iván Herrera | 73 | 0.236 | 0.473 | 0.236 | 0.422 | 0.393 | 6.4% | 27.4% | 10.6% |
| SL | Alec Burleson | 40 | 0.278 | 0.500 | 0.222 | 0.350 | 0.360 | 9.4% | 29.6% | 21.3% |
| SL | Iván Herrera | 34 | 0.192 | 0.385 | 0.192 | 0.350 | 0.415 | 15.0% | 29.7% | 35.5% |
| CH | Masyn Winn | 21 | 0.286 | 0.476 | 0.190 | 0.369 | 0.297 | 5.9% | 21.7% | 24.3% |
| FC | Jordan Walker | 22 | 0.381 | 0.571 | 0.190 | 0.425 | 0.391 | 5.6% | 30.8% | 38.3% |
| SL | Jordan Walker | 38 | 0.351 | 0.541 | 0.189 | 0.392 | 0.331 | 15.4% | 28.0% | 35.7% |
| CH | Alec Burleson | 56 | 0.321 | 0.509 | 0.189 | 0.378 | 0.299 | 6.7% | 21.4% | 16.8% |
| FF | Pedro Pagés | 37 | 0.156 | 0.344 | 0.188 | 0.230 | 0.312 | 8.3% | 17.2% | 18.4% |
| SL | Masyn Winn | 41 | 0.344 | 0.531 | 0.188 | 0.451 | 0.379 | 3.4% | 12.8% | 18.3% |
| SL | Pedro Pagés | 27 | 0.259 | 0.444 | 0.185 | 0.300 | 0.280 | 5.0% | 35.5% | 27.9% |
| SI | Jordan Walker | 69 | 0.267 | 0.450 | 0.183 | 0.371 | 0.406 | 12.2% | 39.5% | 15.4% |
| FF | José Fermín | 43 | 0.175 | 0.350 | 0.175 | 0.271 | 0.207 | 2.9% | 18.2% | 11.4% |
| SI | Pedro Pagés | 28 | 0.391 | 0.565 | 0.174 | 0.423 | 0.397 | 9.1% | 20.0% | 16.0% |
| SI | Nolan Gorman | 25 | 0.217 | 0.391 | 0.174 | 0.266 | 0.292 | 10.5% | 34.4% | 22.2% |
| SI | Nathan Church | 20 | 0.278 | 0.444 | 0.167 | 0.350 | 0.383 | 16.7% | 16.0% | 10.0% |
| FF | Iván Herrera | 94 | 0.257 | 0.419 | 0.162 | 0.387 | 0.391 | 8.2% | 30.1% | 13.0% |
| SL | Victor Scott | 31 | 0.120 | 0.280 | 0.160 | 0.266 | 0.274 | 0.0% | 12.1% | 26.5% |
| FC | Nolan Gorman | 23 | 0.318 | 0.455 | 0.136 | 0.352 | 0.313 | 6.7% | 37.9% | 33.3% |
| CH | Jj Wetherholt | 31 | 0.167 | 0.300 | 0.133 | 0.215 | 0.300 | 4.0% | 19.4% | 23.2% |
| SL | Nathan Church | 34 | 0.188 | 0.312 | 0.125 | 0.222 | 0.239 | 12.0% | 20.0% | 24.1% |


## St. Louis Cardinals Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Iván Herrera | 345 | 0.255 | 0.417 | 0.162 | 0.374 | 0.368 | 7.6% | 30.4% | 18.5% |
| Alec Burleson | 337 | 0.287 | 0.482 | 0.195 | 0.361 | 0.387 | 11.1% | 30.7% | 19.0% |
| Jj Wetherholt | 332 | 0.254 | 0.389 | 0.134 | 0.335 | 0.360 | 8.7% | 28.6% | 19.3% |
| Jordan Walker | 329 | 0.291 | 0.533 | 0.242 | 0.388 | 0.371 | 14.0% | 33.2% | 28.8% |
| Masyn Winn | 301 | 0.238 | 0.318 | 0.080 | 0.300 | 0.307 | 2.9% | 20.1% | 20.1% |
| Nolan Gorman | 242 | 0.194 | 0.313 | 0.118 | 0.269 | 0.279 | 8.8% | 28.0% | 37.5% |
| Nathan Church | 205 | 0.259 | 0.402 | 0.143 | 0.319 | 0.293 | 8.2% | 17.9% | 21.7% |
| Victor Scott | 200 | 0.196 | 0.262 | 0.065 | 0.264 | 0.273 | 0.8% | 15.6% | 24.2% |
| Pedro Pagés | 152 | 0.216 | 0.345 | 0.129 | 0.258 | 0.283 | 5.6% | 23.6% | 25.2% |
| José Fermín | 133 | 0.244 | 0.333 | 0.089 | 0.287 | 0.275 | 0.9% | 22.3% | 11.5% |
| Thomas Saggese | 92 | 0.198 | 0.314 | 0.116 | 0.251 | 0.274 | 10.5% | 22.6% | 28.6% |
| Ramón Urías | 77 | 0.156 | 0.344 | 0.188 | 0.294 | 0.306 | 9.8% | 23.7% | 22.3% |


## Kansas City Royals Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bobby Witt | 347 | 0.288 | 0.456 | 0.168 | 0.367 | 0.392 | 12.2% | 32.7% | 20.9% |
| Salvador Pérez | 309 | 0.215 | 0.372 | 0.156 | 0.277 | 0.290 | 10.3% | 24.7% | 23.6% |
| Vinnie Pasquantino | 302 | 0.219 | 0.340 | 0.121 | 0.300 | 0.316 | 7.4% | 27.5% | 14.0% |
| Maikel García | 295 | 0.262 | 0.375 | 0.112 | 0.314 | 0.322 | 4.9% | 28.5% | 13.7% |
| Carter Jensen | 282 | 0.228 | 0.400 | 0.172 | 0.309 | 0.284 | 7.9% | 25.0% | 27.5% |
| Jac Caglianone | 276 | 0.265 | 0.442 | 0.177 | 0.345 | 0.361 | 14.5% | 33.0% | 28.8% |
| Isaac Collins | 265 | 0.221 | 0.311 | 0.090 | 0.302 | 0.308 | 6.1% | 25.8% | 21.7% |
| Lane Thomas | 207 | 0.225 | 0.367 | 0.142 | 0.333 | 0.324 | 6.2% | 20.5% | 16.4% |
| Kyle Isbel | 196 | 0.263 | 0.383 | 0.120 | 0.317 | 0.275 | 2.9% | 24.5% | 14.6% |
| Michael Massey | 179 | 0.256 | 0.452 | 0.196 | 0.313 | 0.290 | 8.5% | 26.7% | 20.1% |
| Nick Loftin | 155 | 0.246 | 0.385 | 0.138 | 0.335 | 0.316 | 5.4% | 22.3% | 15.6% |
| Starling Marte | 108 | 0.276 | 0.357 | 0.082 | 0.318 | 0.311 | 11.6% | 22.0% | 26.5% |


## Bullpen Fatigue Report

### St. Louis Cardinals Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Chris Roycroft | 2026-06-17 | 1.1 | 42 |
| George Soriano | 2026-06-19 | 1.0 | 18 |
| Gordon Graceffo | 2026-06-18 | 1.2 | 47 |
| Justin Bruihl | 2026-06-17 | 0.1 | 12 |
| Justin Bruihl | 2026-06-18 | 2.2 | 39 |
| Matt Svanson | 2026-06-17 | 1.1 | 16 |
| Matt Svanson | 2026-06-19 | 2.0 | 23 |
| Max Rajcic | 2026-06-18 | 2.0 | 33 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** No relievers flagged for heavy recent use


### Kansas City Royals Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alex Lange | 2026-06-17 | 1.0 | 19 |
| Alex Lange | 2026-06-19 | 0.1 | 10 |
| Beck Way | 2026-06-18 | 2.0 | 36 |
| Daniel Lynch IV | 2026-06-19 | 1.0 | 11 |
| John Schreiber | 2026-06-17 | 1.0 | 15 |
| John Schreiber | 2026-06-19 | 1.0 | 12 |
| Lucas Erceg | 2026-06-17 | 1.0 | 11 |
| Mason Black | 2026-06-18 | 2.0 | 40 |
| Matt Strahm | 2026-06-17 | 0.1 | 6 |
| Matt Strahm | 2026-06-19 | 0.2 | 22 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** No relievers flagged for heavy recent use



## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, FC, ST, SI
- Home pitcher pitch mix to inspect: FF, SI, SL, CH, FC, ST
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 8. San Diego Padres @ Texas Rangers

## Game Context

| Field | Value |
| --- | --- |
| Park | Globe Life Field |
| Time | 2026-06-21T18:35:00Z |
| Away Team | San Diego Padres |
| Home Team | Texas Rangers |
| Away Probable Pitcher | Wandy Peralta |
| Home Probable Pitcher | Nathan Eovaldi |


## Away Starting Pitcher: Wandy Peralta

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 625 |
| Batted/Result Events | 161 |
| Hits Allowed | 31 |
| Walks | 20 |
| Strikeouts | 27 |
| Home Runs | 3 |
| K Event Rate | 16.8% |
| BB Event Rate | 12.4% |
| HR Event Rate | 1.9% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 11.4% | 71 | 0.235 | 0.471 | 0.235 | 0.297 | 0.339 | 10.0% | 20.8% | 23.1% |
| CH | vs R | 22.7% | 142 | 0.171 | 0.195 | 0.024 | 0.187 | 0.307 | 0.0% | 25.0% | 33.7% |
| FF | vs L | 4.0% | 25 | 0.286 | 0.286 | 0.000 | 0.356 | 0.361 | 0.0% | 7.1% | 12.5% |
| FF | vs R | 5.4% | 34 | 0.000 | 0.000 | 0.000 | 0.175 | 0.251 | 0.0% | 0.0% | 16.7% |
| SI | vs L | 27.0% | 169 | 0.294 | 0.441 | 0.147 | 0.383 | 0.306 | 6.9% | 27.0% | 16.5% |
| SI | vs R | 12.2% | 76 | 0.222 | 0.389 | 0.167 | 0.341 | 0.359 | 6.2% | 11.5% | 6.2% |
| SL | vs L | 13.1% | 82 | 0.200 | 0.200 | 0.000 | 0.267 | 0.259 | 0.0% | 9.1% | 34.3% |
| SL | vs R | 3.5% | 22 | 0.250 | 0.750 | 0.500 | 0.500 | 0.477 | 0.0% | 10.0% | 9.1% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-19 | 19 | 0 | 1 | 0 | 0 |
| 2026-06-16 | 13 | 1 | 0 | 0 | 0 |
| 2026-06-15 | 11 | 0 | 0 | 1 | 0 |
| 2026-06-12 | 34 | 1 | 2 | 3 | 0 |
| 2026-06-10 | 14 | 1 | 1 | 0 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | Kyle Higashioka | 10 | 0.333 | 0.778 | 0.444 | 0.485 | 0.324 | 20.0% | 40.0% | 41.7% |
| SI | Jake Burger | 58 | 0.321 | 0.660 | 0.340 | 0.441 | 0.401 | 11.9% | 36.0% | 17.6% |
| CH | Corey Seager | 31 | 0.241 | 0.552 | 0.310 | 0.384 | 0.390 | 20.0% | 37.9% | 31.2% |
| CH | Danny Jansen | 12 | 0.364 | 0.636 | 0.273 | 0.446 | 0.278 | 0.0% | 15.4% | 36.4% |
| SL | Danny Jansen | 15 | 0.200 | 0.467 | 0.267 | 0.277 | 0.164 | 10.0% | 20.0% | 26.5% |
| SL | Ezequiel Duran | 34 | 0.355 | 0.613 | 0.258 | 0.437 | 0.269 | 0.0% | 18.2% | 40.3% |
| SI | Kyle Higashioka | 41 | 0.371 | 0.629 | 0.257 | 0.468 | 0.423 | 14.3% | 33.3% | 13.1% |
| SI | Joc Pederson | 28 | 0.350 | 0.600 | 0.250 | 0.438 | 0.472 | 11.1% | 34.4% | 17.4% |
| SI | Wyatt Langford | 39 | 0.324 | 0.559 | 0.235 | 0.417 | 0.368 | 3.4% | 43.1% | 9.4% |
| CH | Jake Burger | 34 | 0.267 | 0.500 | 0.233 | 0.349 | 0.326 | 10.5% | 24.1% | 40.7% |
| FF | Josh Jung | 80 | 0.290 | 0.522 | 0.232 | 0.405 | 0.363 | 15.1% | 28.3% | 13.1% |
| SL | Joc Pederson | 30 | 0.231 | 0.462 | 0.231 | 0.347 | 0.329 | 21.4% | 33.3% | 36.8% |
| FF | Joc Pederson | 79 | 0.258 | 0.485 | 0.227 | 0.378 | 0.391 | 14.9% | 38.0% | 26.1% |
| FF | Corey Seager | 55 | 0.156 | 0.378 | 0.222 | 0.295 | 0.296 | 21.4% | 23.1% | 29.7% |
| FF | Evan Carter | 83 | 0.186 | 0.400 | 0.214 | 0.312 | 0.355 | 11.7% | 22.0% | 13.8% |
| CH | Joc Pederson | 37 | 0.194 | 0.389 | 0.194 | 0.258 | 0.310 | 6.9% | 31.8% | 31.8% |
| CH | Josh Jung | 30 | 0.407 | 0.593 | 0.185 | 0.460 | 0.295 | 4.8% | 37.1% | 20.0% |
| FF | Ezequiel Duran | 64 | 0.175 | 0.351 | 0.175 | 0.273 | 0.274 | 13.9% | 17.2% | 27.2% |
| SL | Wyatt Langford | 23 | 0.261 | 0.435 | 0.174 | 0.298 | 0.274 | 11.1% | 29.6% | 12.1% |
| SL | Jake Burger | 58 | 0.226 | 0.396 | 0.170 | 0.315 | 0.223 | 7.3% | 28.6% | 43.4% |
| FF | Brandon Nimmo | 111 | 0.274 | 0.442 | 0.168 | 0.357 | 0.335 | 5.4% | 24.7% | 16.6% |
| SL | Evan Carter | 29 | 0.167 | 0.333 | 0.167 | 0.271 | 0.265 | 5.9% | 39.3% | 34.1% |
| FF | Wyatt Langford | 52 | 0.265 | 0.429 | 0.163 | 0.321 | 0.251 | 5.6% | 13.5% | 16.8% |
| FF | Jake Burger | 84 | 0.187 | 0.320 | 0.133 | 0.268 | 0.293 | 5.6% | 38.7% | 25.6% |
| FF | Danny Jansen | 58 | 0.133 | 0.267 | 0.133 | 0.287 | 0.301 | 10.3% | 29.2% | 21.8% |
| CH | Ezequiel Duran | 24 | 0.348 | 0.478 | 0.130 | 0.410 | 0.331 | 0.0% | 14.6% | 11.8% |
| SL | Brandon Nimmo | 45 | 0.200 | 0.325 | 0.125 | 0.262 | 0.356 | 11.1% | 32.8% | 26.4% |
| CH | Evan Carter | 42 | 0.081 | 0.189 | 0.108 | 0.182 | 0.158 | 0.0% | 18.9% | 38.7% |
| SL | Corey Seager | 32 | 0.107 | 0.214 | 0.107 | 0.206 | 0.243 | 6.2% | 14.3% | 51.5% |
| FF | Kyle Higashioka | 32 | 0.250 | 0.357 | 0.107 | 0.317 | 0.306 | 13.0% | 37.5% | 10.0% |


## Home Starting Pitcher: Nathan Eovaldi

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1321 |
| Batted/Result Events | 379 |
| Hits Allowed | 85 |
| Walks | 22 |
| Strikeouts | 83 |
| Home Runs | 17 |
| K Event Rate | 21.9% |
| BB Event Rate | 5.8% |
| HR Event Rate | 4.5% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 12.3% | 163 | 0.333 | 0.567 | 0.233 | 0.385 | 0.281 | 8.0% | 27.1% | 30.1% |
| CU | vs R | 8.3% | 109 | 0.067 | 0.067 | 0.000 | 0.100 | 0.179 | 0.0% | 9.7% | 41.8% |
| FC | vs L | 15.3% | 202 | 0.213 | 0.362 | 0.149 | 0.324 | 0.342 | 7.9% | 21.9% | 29.2% |
| FC | vs R | 5.4% | 71 | 0.438 | 0.812 | 0.375 | 0.558 | 0.552 | 13.3% | 25.0% | 10.3% |
| FF | vs L | 7.8% | 103 | 0.419 | 0.903 | 0.484 | 0.564 | 0.487 | 26.1% | 34.2% | 18.8% |
| FF | vs R | 4.5% | 59 | 0.333 | 0.500 | 0.167 | 0.393 | 0.338 | 6.7% | 33.3% | 17.4% |
| FS | vs L | 23.5% | 310 | 0.202 | 0.326 | 0.124 | 0.255 | 0.317 | 8.8% | 35.2% | 25.6% |
| FS | vs R | 13.4% | 177 | 0.170 | 0.362 | 0.191 | 0.261 | 0.246 | 7.4% | 31.1% | 42.7% |
| SI | vs L | 0.1% | 1 | 1.000 | 1.000 | 0.000 | 0.900 | 0.910 | 0.0% | 0.0% | 0.0% |
| SI | vs R | 8.8% | 116 | 0.237 | 0.421 | 0.184 | 0.342 | 0.329 | 2.8% | 17.2% | 5.8% |
| SL | vs L | 0.2% | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 0.0% |
| SL | vs R | 0.6% | 8 | 1.000 | 1.000 | 0.000 | 0.450 | 0.483 | 0.0% | 66.7% | 0.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-14 | 94 | 6 | 1 | 6 | 2 |
| 2026-06-09 | 88 | 4 | 3 | 3 | 1 |
| 2026-06-02 | 93 | 11 | 1 | 7 | 1 |
| 2026-05-28 | 90 | 4 | 2 | 6 | 2 |
| 2026-05-23 | 97 | 5 | 2 | 6 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Freddy Fermin | 6 | 0.250 | 1.000 | 0.750 | 0.450 | 0.182 | 0.0% | 37.5% | 33.3% |
| FC | Manny Machado | 15 | 0.385 | 0.923 | 0.538 | 0.517 | 0.478 | 21.4% | 40.7% | 16.7% |
| FC | Gavin Sheets | 21 | 0.316 | 0.842 | 0.526 | 0.498 | 0.446 | 23.5% | 36.1% | 12.2% |
| CU | Miguel Andújar | 9 | 0.444 | 0.889 | 0.444 | 0.561 | 0.439 | 14.3% | 41.7% | 20.0% |
| FS | Miguel Andújar | 7 | 0.143 | 0.571 | 0.429 | 0.286 | 0.149 | 0.0% | 33.3% | 33.3% |
| FC | Nick Castellanos | 8 | 0.286 | 0.714 | 0.429 | 0.450 | 0.450 | 40.0% | 33.3% | 40.9% |
| FF | Ty France | 37 | 0.235 | 0.588 | 0.353 | 0.388 | 0.303 | 25.0% | 15.5% | 32.4% |
| FC | Luis Campusano | 3 | 0.333 | 0.667 | 0.333 | 0.417 | 0.288 | 0.0% | 0.0% | 20.0% |
| FF | Luis Campusano | 25 | 0.300 | 0.600 | 0.300 | 0.478 | 0.417 | 18.8% | 48.1% | 23.7% |
| FF | Gavin Sheets | 91 | 0.253 | 0.519 | 0.266 | 0.374 | 0.360 | 10.6% | 28.6% | 11.1% |
| FF | Manny Machado | 96 | 0.220 | 0.463 | 0.244 | 0.332 | 0.380 | 12.3% | 26.5% | 23.0% |
| FC | Ty France | 15 | 0.077 | 0.308 | 0.231 | 0.227 | 0.479 | 30.0% | 30.0% | 32.3% |
| FC | Ramón Laureano | 14 | 0.071 | 0.286 | 0.214 | 0.143 | 0.181 | 14.3% | 16.7% | 39.5% |
| FF | Xander Bogaerts | 83 | 0.254 | 0.465 | 0.211 | 0.364 | 0.356 | 13.3% | 28.4% | 13.0% |
| SI | Ty France | 42 | 0.205 | 0.410 | 0.205 | 0.312 | 0.336 | 5.9% | 23.3% | 16.5% |
| FC | Xander Bogaerts | 20 | 0.250 | 0.438 | 0.188 | 0.375 | 0.438 | 8.3% | 23.5% | 19.0% |
| FF | Ramón Laureano | 61 | 0.224 | 0.408 | 0.184 | 0.352 | 0.437 | 20.0% | 25.8% | 25.0% |
| CU | Ty France | 11 | 0.182 | 0.364 | 0.182 | 0.227 | 0.147 | 0.0% | 38.5% | 23.8% |
| SI | Jackson Merrill | 50 | 0.409 | 0.591 | 0.182 | 0.483 | 0.454 | 8.3% | 27.7% | 9.7% |
| SI | Manny Machado | 66 | 0.153 | 0.322 | 0.169 | 0.248 | 0.344 | 9.4% | 28.3% | 15.3% |
| SI | Luis Campusano | 15 | 0.417 | 0.583 | 0.167 | 0.487 | 0.392 | 9.1% | 35.0% | 13.3% |
| SI | Nick Castellanos | 27 | 0.250 | 0.417 | 0.167 | 0.306 | 0.375 | 4.8% | 23.7% | 21.0% |
| FF | Miguel Andújar | 54 | 0.184 | 0.347 | 0.163 | 0.268 | 0.310 | 5.0% | 17.7% | 8.9% |
| SI | Gavin Sheets | 42 | 0.231 | 0.385 | 0.154 | 0.294 | 0.359 | 6.5% | 37.5% | 10.3% |
| FF | Freddy Fermin | 43 | 0.135 | 0.270 | 0.135 | 0.253 | 0.281 | 3.3% | 12.5% | 15.5% |
| SI | Freddy Fermin | 41 | 0.189 | 0.324 | 0.135 | 0.266 | 0.293 | 3.0% | 25.4% | 10.3% |
| SI | Miguel Andújar | 55 | 0.358 | 0.491 | 0.132 | 0.385 | 0.355 | 3.8% | 29.3% | 4.3% |
| FF | Jackson Merrill | 103 | 0.196 | 0.315 | 0.120 | 0.270 | 0.318 | 13.3% | 23.2% | 25.4% |
| SI | Ramón Laureano | 55 | 0.289 | 0.400 | 0.111 | 0.347 | 0.343 | 7.5% | 29.2% | 16.7% |
| SI | Xander Bogaerts | 90 | 0.238 | 0.345 | 0.107 | 0.343 | 0.308 | 4.1% | 28.4% | 12.2% |


## San Diego Padres Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fernando Tatís | 334 | 0.280 | 0.355 | 0.075 | 0.328 | 0.348 | 10.5% | 35.6% | 26.1% |
| Jackson Merrill | 322 | 0.210 | 0.349 | 0.139 | 0.278 | 0.319 | 9.6% | 25.1% | 24.6% |
| Manny Machado | 316 | 0.172 | 0.355 | 0.183 | 0.277 | 0.304 | 8.9% | 24.8% | 23.5% |
| Xander Bogaerts | 298 | 0.227 | 0.348 | 0.121 | 0.320 | 0.316 | 7.2% | 25.8% | 20.0% |
| Gavin Sheets | 265 | 0.236 | 0.481 | 0.245 | 0.347 | 0.328 | 9.6% | 31.1% | 17.7% |
| Ramón Laureano | 224 | 0.209 | 0.383 | 0.173 | 0.301 | 0.312 | 13.4% | 23.3% | 30.5% |
| Miguel Andújar | 216 | 0.239 | 0.390 | 0.151 | 0.290 | 0.285 | 4.1% | 21.7% | 18.4% |
| Ty France | 183 | 0.247 | 0.482 | 0.235 | 0.343 | 0.315 | 12.1% | 26.1% | 25.5% |
| Freddy Fermin | 157 | 0.162 | 0.265 | 0.103 | 0.253 | 0.266 | 2.8% | 16.4% | 22.8% |
| Nick Castellanos | 137 | 0.178 | 0.333 | 0.155 | 0.246 | 0.285 | 7.5% | 20.4% | 30.8% |
| Jake Cronenworth | 132 | 0.162 | 0.216 | 0.054 | 0.257 | 0.304 | 4.7% | 21.2% | 21.2% |
| Luis Campusano | 71 | 0.290 | 0.565 | 0.274 | 0.415 | 0.340 | 11.4% | 33.3% | 28.3% |


## Texas Rangers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brandon Nimmo | 338 | 0.258 | 0.411 | 0.152 | 0.329 | 0.370 | 11.6% | 31.0% | 18.5% |
| Jake Burger | 317 | 0.253 | 0.450 | 0.197 | 0.338 | 0.307 | 9.7% | 32.1% | 32.3% |
| Josh Jung | 316 | 0.307 | 0.467 | 0.160 | 0.366 | 0.348 | 5.8% | 29.5% | 16.9% |
| Ezequiel Duran | 260 | 0.271 | 0.436 | 0.165 | 0.343 | 0.305 | 7.0% | 22.2% | 25.1% |
| Joc Pederson | 247 | 0.227 | 0.422 | 0.194 | 0.334 | 0.342 | 10.3% | 30.8% | 28.8% |
| Evan Carter | 241 | 0.168 | 0.307 | 0.139 | 0.276 | 0.294 | 6.8% | 23.0% | 24.9% |
| Corey Seager | 221 | 0.188 | 0.375 | 0.188 | 0.293 | 0.335 | 16.3% | 27.2% | 31.7% |
| Wyatt Langford | 162 | 0.267 | 0.467 | 0.200 | 0.341 | 0.296 | 6.8% | 25.4% | 19.6% |
| Danny Jansen | 152 | 0.176 | 0.321 | 0.145 | 0.274 | 0.254 | 6.8% | 25.1% | 24.0% |
| Kyle Higashioka | 150 | 0.243 | 0.404 | 0.162 | 0.328 | 0.302 | 10.4% | 28.4% | 27.3% |
| Alejandro Osuna | 141 | 0.264 | 0.298 | 0.033 | 0.329 | 0.316 | 1.0% | 22.0% | 13.0% |
| Josh Smith | 137 | 0.214 | 0.239 | 0.026 | 0.268 | 0.284 | 4.4% | 24.9% | 19.0% |


## Bullpen Fatigue Report

### San Diego Padres Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Adrian Morejon | 2026-06-17 | 1.0 | 12 |
| Adrian Morejon | 2026-06-20 | 2.0 | 35 |
| David Morgan | 2026-06-19 | 0.1 | 10 |
| Griffin Canning | 2026-06-17 | 4.1 | 77 |
| Jason Adam | 2026-06-17 | 1.0 | 12 |
| Jason Adam | 2026-06-19 | 1.0 | 11 |
| Jason Adam | 2026-06-20 | 1.0 | 28 |
| Kyle Hart | 2026-06-17 | 1.2 | 11 |
| Kyle Hart | 2026-06-20 | 0.2 | 10 |
| Mason Miller | 2026-06-20 | 1.0 | 21 |
| Wandy Peralta | 2026-06-19 | 1.2 | 19 |
| Yuki Matsui | 2026-06-19 | 1.2 | 34 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Adrian Morejon, Jason Adam, Kyle Hart, Mason Miller


### Texas Rangers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Cal Quantrill | 2026-06-18 | 2.0 | 36 |
| Cole Winn | 2026-06-18 | 1.0 | 9 |
| Cole Winn | 2026-06-20 | 0.2 | 14 |
| Jacob Latz | 2026-06-19 | 1.1 | 11 |
| Jacob Latz | 2026-06-20 | 1.0 | 13 |
| Jakob Junis | 2026-06-19 | 1.2 | 31 |
| Joe Ross | 2026-06-20 | 1.0 | 21 |
| Peyton Gray | 2026-06-18 | 1.0 | 10 |
| Peyton Gray | 2026-06-20 | 1.0 | 15 |
| Robby Ahlstrom | 2026-06-18 | 1.0 | 28 |
| Tyler Alexander | 2026-06-20 | 0.1 | 9 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Cole Winn, Jacob Latz, Joe Ross, Peyton Gray, Tyler Alexander



## Final Game Dissection

- Away pitcher pitch mix to inspect: SI, CH, SL, FF
- Home pitcher pitch mix to inspect: FS, FC, CU, FF, SI
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 9. Pittsburgh Pirates @ Colorado Rockies

## Game Context

| Field | Value |
| --- | --- |
| Park | Coors Field |
| Time | 2026-06-21T19:10:00Z |
| Away Team | Pittsburgh Pirates |
| Home Team | Colorado Rockies |
| Away Probable Pitcher | Jared Jones |
| Home Probable Pitcher | Michael Lorenzen |


## Away Starting Pitcher: Jared Jones

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 301 |
| Batted/Result Events | 79 |
| Hits Allowed | 22 |
| Walks | 6 |
| Strikeouts | 18 |
| Home Runs | 4 |
| K Event Rate | 22.8% |
| BB Event Rate | 7.6% |
| HR Event Rate | 5.1% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 12.6% | 38 | 0.500 | 0.875 | 0.375 | 0.588 | 0.327 | 0.0% | 50.0% | 37.5% |
| CH | vs R | 3.3% | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.081 | 0.0% | 33.3% | 33.3% |
| CU | vs L | 8.0% | 24 | 1.000 | 1.333 | 0.333 | 1.017 | 0.502 | 0.0% | 40.0% | 36.4% |
| CU | vs R | 2.3% | 7 | 0.000 | 0.000 | 0.000 | 0.233 | 0.234 | 0.0% | 0.0% | 75.0% |
| FF | vs L | 24.9% | 75 | 0.316 | 0.737 | 0.421 | 0.462 | 0.543 | 28.6% | 38.5% | 23.7% |
| FF | vs R | 15.3% | 46 | 0.154 | 0.231 | 0.077 | 0.204 | 0.194 | 0.0% | 13.3% | 20.0% |
| SL | vs L | 14.3% | 43 | 0.417 | 0.750 | 0.333 | 0.512 | 0.453 | 12.5% | 30.0% | 36.8% |
| SL | vs R | 19.3% | 58 | 0.167 | 0.167 | 0.000 | 0.262 | 0.193 | 0.0% | 16.7% | 25.0% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 75 | 8 | 1 | 4 | 2 |
| 2026-06-10 | 75 | 3 | 1 | 4 | 0 |
| 2026-06-04 | 74 | 4 | 2 | 4 | 0 |
| 2026-05-29 | 77 | 7 | 2 | 6 | 2 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Mickey Moniak | 12 | 0.182 | 0.727 | 0.545 | 0.392 | 0.468 | 66.7% | 41.7% | 45.2% |
| SL | Hunter Goodman | 50 | 0.277 | 0.766 | 0.489 | 0.462 | 0.359 | 25.9% | 30.4% | 38.3% |
| CU | Troy Johnston | 20 | 0.389 | 0.778 | 0.389 | 0.510 | 0.406 | 7.7% | 38.1% | 28.6% |
| SL | Tj Rumfield | 37 | 0.314 | 0.657 | 0.343 | 0.423 | 0.295 | 8.7% | 32.5% | 36.1% |
| CU | Hunter Goodman | 31 | 0.200 | 0.533 | 0.333 | 0.315 | 0.280 | 17.6% | 44.4% | 36.7% |
| FF | Brett Sullivan | 38 | 0.286 | 0.600 | 0.314 | 0.379 | 0.317 | 7.1% | 25.0% | 11.5% |
| SL | Troy Johnston | 38 | 0.306 | 0.583 | 0.278 | 0.372 | 0.298 | 3.2% | 34.0% | 16.9% |
| SL | Mickey Moniak | 20 | 0.167 | 0.444 | 0.278 | 0.295 | 0.311 | 23.1% | 17.2% | 31.2% |
| CH | Hunter Goodman | 28 | 0.231 | 0.500 | 0.269 | 0.366 | 0.245 | 11.8% | 22.2% | 43.3% |
| FF | Mickey Moniak | 51 | 0.306 | 0.571 | 0.265 | 0.384 | 0.307 | 8.3% | 20.5% | 18.8% |
| CU | Brenton Doyle | 4 | 0.250 | 0.500 | 0.250 | 0.312 | 0.000 | 100.0% | 66.7% | 25.0% |
| CU | Ezequiel Tovar | 13 | 0.250 | 0.500 | 0.250 | 0.342 | 0.346 | 25.0% | 15.4% | 23.8% |
| FF | Hunter Goodman | 92 | 0.173 | 0.407 | 0.235 | 0.298 | 0.316 | 19.6% | 25.7% | 22.5% |
| FF | Kyle Karros | 95 | 0.354 | 0.570 | 0.215 | 0.447 | 0.401 | 7.7% | 28.6% | 5.2% |
| FF | Tj Rumfield | 108 | 0.301 | 0.516 | 0.215 | 0.391 | 0.364 | 9.2% | 21.9% | 10.3% |
| CH | Brett Sullivan | 15 | 0.143 | 0.357 | 0.214 | 0.190 | 0.155 | 0.0% | 5.9% | 18.2% |
| SL | Tyler Freeman | 26 | 0.280 | 0.480 | 0.200 | 0.373 | 0.285 | 0.0% | 29.6% | 18.9% |
| CU | Tj Rumfield | 22 | 0.250 | 0.450 | 0.200 | 0.375 | 0.274 | 0.0% | 15.4% | 30.2% |
| FF | Jake Mccarthy | 101 | 0.315 | 0.494 | 0.180 | 0.361 | 0.358 | 3.7% | 14.9% | 11.1% |
| CH | Mickey Moniak | 29 | 0.179 | 0.357 | 0.179 | 0.217 | 0.214 | 4.5% | 37.5% | 33.3% |
| SL | Ezequiel Tovar | 47 | 0.267 | 0.444 | 0.178 | 0.291 | 0.299 | 10.5% | 13.9% | 32.2% |
| CU | Willi Castro | 25 | 0.375 | 0.542 | 0.167 | 0.410 | 0.327 | 5.0% | 30.3% | 24.4% |
| FF | Tyler Freeman | 56 | 0.388 | 0.531 | 0.143 | 0.429 | 0.335 | 2.3% | 16.1% | 8.2% |
| SL | Edouard Julien | 26 | 0.095 | 0.238 | 0.143 | 0.246 | 0.309 | 16.7% | 17.6% | 47.7% |
| CH | Jake Mccarthy | 22 | 0.190 | 0.333 | 0.143 | 0.243 | 0.253 | 6.7% | 9.4% | 29.2% |
| FF | Willi Castro | 102 | 0.292 | 0.427 | 0.135 | 0.361 | 0.326 | 4.9% | 19.6% | 25.0% |
| CH | Ezequiel Tovar | 24 | 0.167 | 0.292 | 0.125 | 0.233 | 0.222 | 7.1% | 20.6% | 42.4% |
| CU | Jake Mccarthy | 18 | 0.312 | 0.438 | 0.125 | 0.378 | 0.314 | 0.0% | 22.2% | 22.2% |
| SL | Willi Castro | 29 | 0.192 | 0.308 | 0.115 | 0.266 | 0.261 | 5.6% | 28.1% | 30.6% |
| CH | Willi Castro | 50 | 0.217 | 0.326 | 0.109 | 0.258 | 0.211 | 10.7% | 29.1% | 33.7% |


## Home Starting Pitcher: Michael Lorenzen

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1383 |
| Batted/Result Events | 363 |
| Hits Allowed | 110 |
| Walks | 28 |
| Strikeouts | 63 |
| Home Runs | 14 |
| K Event Rate | 17.4% |
| BB Event Rate | 7.7% |
| HR Event Rate | 3.9% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 13.4% | 185 | 0.325 | 0.425 | 0.100 | 0.346 | 0.314 | 10.3% | 17.0% | 30.8% |
| CH | vs R | 5.6% | 78 | 0.286 | 0.619 | 0.333 | 0.440 | 0.314 | 7.7% | 38.1% | 36.1% |
| CU | vs L | 7.6% | 105 | 0.375 | 0.812 | 0.438 | 0.509 | 0.419 | 23.1% | 26.9% | 27.9% |
| CU | vs R | 6.4% | 89 | 0.273 | 0.318 | 0.045 | 0.250 | 0.218 | 0.0% | 21.9% | 15.0% |
| FC | vs L | 6.9% | 96 | 0.560 | 1.000 | 0.440 | 0.665 | 0.509 | 12.5% | 34.1% | 10.0% |
| FC | vs R | 7.1% | 98 | 0.200 | 0.300 | 0.100 | 0.246 | 0.329 | 4.8% | 25.0% | 21.4% |
| FF | vs L | 10.6% | 146 | 0.342 | 0.895 | 0.553 | 0.541 | 0.497 | 19.4% | 32.8% | 6.2% |
| FF | vs R | 8.7% | 120 | 0.333 | 0.375 | 0.042 | 0.315 | 0.290 | 0.0% | 29.2% | 13.3% |
| SI | vs L | 5.0% | 69 | 0.421 | 0.579 | 0.158 | 0.480 | 0.414 | 12.5% | 52.6% | 16.7% |
| SI | vs R | 11.0% | 152 | 0.400 | 0.444 | 0.044 | 0.439 | 0.332 | 2.4% | 33.9% | 9.5% |
| SL | vs L | 3.0% | 41 | 0.417 | 0.750 | 0.333 | 0.454 | 0.354 | 12.5% | 38.5% | 20.0% |
| SL | vs R | 5.9% | 82 | 0.231 | 0.385 | 0.154 | 0.327 | 0.357 | 11.8% | 32.1% | 24.4% |
| ST | vs L | 1.4% | 20 | 0.500 | 1.000 | 0.500 | 0.650 | 0.428 | 0.0% | 33.3% | 25.0% |
| ST | vs R | 7.4% | 102 | 0.118 | 0.294 | 0.176 | 0.250 | 0.281 | 18.2% | 32.0% | 35.7% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 89 | 5 | 1 | 5 | 1 |
| 2026-06-10 | 84 | 2 | 2 | 7 | 0 |
| 2026-06-03 | 85 | 10 | 2 | 5 | 1 |
| 2026-05-29 | 70 | 5 | 2 | 2 | 0 |
| 2026-05-23 | 94 | 8 | 1 | 5 | 1 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Oneil Cruz | 18 | 0.333 | 1.000 | 0.667 | 0.569 | 0.552 | 36.4% | 33.3% | 27.5% |
| FC | Henry Davis | 11 | 0.273 | 0.818 | 0.545 | 0.445 | 0.289 | 20.0% | 31.2% | 19.2% |
| FF | Brandon Lowe | 82 | 0.290 | 0.710 | 0.420 | 0.470 | 0.452 | 34.1% | 26.0% | 31.3% |
| CU | Brandon Lowe | 24 | 0.278 | 0.667 | 0.389 | 0.438 | 0.378 | 7.1% | 52.6% | 37.1% |
| ST | Oneil Cruz | 23 | 0.350 | 0.700 | 0.350 | 0.515 | 0.376 | 18.2% | 33.3% | 32.5% |
| CU | Oneil Cruz | 18 | 0.222 | 0.556 | 0.333 | 0.372 | 0.310 | 33.3% | 26.7% | 48.4% |
| SL | Nick Yorke | 7 | 0.333 | 0.667 | 0.333 | 0.457 | 0.286 | 0.0% | 33.3% | 17.6% |
| CU | Bryan Reynolds | 30 | 0.296 | 0.593 | 0.296 | 0.383 | 0.356 | 23.5% | 28.1% | 40.4% |
| FF | Bryan Reynolds | 107 | 0.333 | 0.611 | 0.278 | 0.458 | 0.416 | 14.1% | 30.7% | 17.3% |
| CH | Brandon Lowe | 39 | 0.194 | 0.472 | 0.278 | 0.314 | 0.344 | 10.7% | 23.5% | 32.1% |
| SL | Brandon Lowe | 55 | 0.216 | 0.490 | 0.275 | 0.311 | 0.280 | 12.1% | 30.0% | 36.6% |
| SL | Spencer Horwitz | 34 | 0.300 | 0.567 | 0.267 | 0.406 | 0.289 | 4.5% | 20.5% | 14.8% |
| FF | Ryan O'Hearn | 92 | 0.313 | 0.578 | 0.265 | 0.420 | 0.346 | 10.1% | 26.9% | 12.2% |
| FF | Konnor Griffin | 47 | 0.205 | 0.462 | 0.256 | 0.349 | 0.306 | 11.8% | 14.0% | 25.5% |
| FF | Spencer Horwitz | 110 | 0.270 | 0.506 | 0.236 | 0.395 | 0.373 | 12.7% | 18.7% | 12.4% |
| FC | Ryan O'Hearn | 16 | 0.154 | 0.385 | 0.231 | 0.312 | 0.332 | 11.1% | 14.3% | 16.7% |
| FC | Spencer Horwitz | 26 | 0.208 | 0.417 | 0.208 | 0.269 | 0.203 | 4.8% | 13.2% | 15.6% |
| FC | Brandon Lowe | 31 | 0.280 | 0.480 | 0.200 | 0.397 | 0.347 | 0.0% | 38.2% | 33.3% |
| CU | Jared Triolo | 6 | 0.200 | 0.400 | 0.200 | 0.475 | 0.327 | 0.0% | 28.6% | 11.1% |
| SL | Nick Gonzales | 38 | 0.229 | 0.429 | 0.200 | 0.336 | 0.408 | 6.2% | 25.0% | 22.6% |
| ST | Henry Davis | 15 | 0.133 | 0.333 | 0.200 | 0.193 | 0.237 | 9.1% | 36.4% | 16.7% |
| SI | Henry Davis | 40 | 0.226 | 0.419 | 0.194 | 0.357 | 0.431 | 10.3% | 38.5% | 9.0% |
| FF | Oneil Cruz | 91 | 0.291 | 0.481 | 0.190 | 0.392 | 0.388 | 15.1% | 37.1% | 27.0% |
| FC | Marcell Ozuna | 17 | 0.188 | 0.375 | 0.188 | 0.265 | 0.244 | 9.1% | 17.4% | 34.2% |
| SL | Ryan O'Hearn | 40 | 0.211 | 0.395 | 0.184 | 0.279 | 0.238 | 4.5% | 23.4% | 27.6% |
| FC | Konnor Griffin | 18 | 0.412 | 0.588 | 0.176 | 0.497 | 0.381 | 14.3% | 34.5% | 26.2% |
| CU | Spencer Horwitz | 20 | 0.235 | 0.412 | 0.176 | 0.340 | 0.355 | 25.0% | 31.6% | 17.9% |
| SL | Oneil Cruz | 38 | 0.235 | 0.412 | 0.176 | 0.345 | 0.351 | 15.0% | 36.8% | 44.0% |
| ST | Brandon Lowe | 28 | 0.080 | 0.240 | 0.160 | 0.223 | 0.238 | 0.0% | 27.6% | 36.4% |
| ST | Konnor Griffin | 20 | 0.211 | 0.368 | 0.158 | 0.270 | 0.241 | 6.2% | 41.7% | 25.0% |


## Pittsburgh Pirates Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bryan Reynolds | 348 | 0.285 | 0.462 | 0.177 | 0.385 | 0.371 | 9.7% | 29.6% | 25.4% |
| Brandon Lowe | 327 | 0.244 | 0.502 | 0.258 | 0.362 | 0.349 | 12.7% | 28.8% | 32.4% |
| Nick Gonzales | 305 | 0.286 | 0.357 | 0.071 | 0.316 | 0.323 | 2.6% | 22.0% | 21.0% |
| Spencer Horwitz | 301 | 0.271 | 0.454 | 0.183 | 0.372 | 0.336 | 8.8% | 21.1% | 13.8% |
| Oneil Cruz | 300 | 0.261 | 0.470 | 0.208 | 0.368 | 0.358 | 16.9% | 36.9% | 35.3% |
| Ryan O'Hearn | 272 | 0.264 | 0.431 | 0.167 | 0.337 | 0.321 | 7.4% | 26.1% | 20.8% |
| Marcell Ozuna | 236 | 0.200 | 0.307 | 0.107 | 0.268 | 0.310 | 7.6% | 26.7% | 28.5% |
| Konnor Griffin | 222 | 0.259 | 0.398 | 0.139 | 0.332 | 0.303 | 8.6% | 24.2% | 30.8% |
| Jake Mangum | 188 | 0.285 | 0.337 | 0.052 | 0.321 | 0.282 | 0.7% | 13.7% | 16.5% |
| Henry Davis | 166 | 0.152 | 0.303 | 0.152 | 0.269 | 0.296 | 11.8% | 30.7% | 22.1% |
| Jared Triolo | 162 | 0.223 | 0.270 | 0.047 | 0.282 | 0.269 | 1.0% | 24.6% | 23.3% |
| Nick Yorke | 107 | 0.202 | 0.277 | 0.074 | 0.264 | 0.306 | 5.1% | 28.3% | 14.7% |


## Colorado Rockies Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hunter Goodman | 324 | 0.256 | 0.539 | 0.283 | 0.373 | 0.323 | 16.2% | 28.7% | 31.7% |
| Tj Rumfield | 321 | 0.270 | 0.460 | 0.189 | 0.359 | 0.325 | 6.2% | 22.1% | 16.9% |
| Ezequiel Tovar | 293 | 0.214 | 0.343 | 0.129 | 0.276 | 0.285 | 9.0% | 18.6% | 27.6% |
| Troy Johnston | 282 | 0.321 | 0.472 | 0.151 | 0.374 | 0.332 | 3.0% | 24.1% | 21.7% |
| Willi Castro | 272 | 0.281 | 0.413 | 0.132 | 0.345 | 0.301 | 6.5% | 22.8% | 26.8% |
| Kyle Karros | 263 | 0.249 | 0.371 | 0.122 | 0.329 | 0.336 | 6.8% | 26.5% | 23.3% |
| Jake Mccarthy | 239 | 0.307 | 0.472 | 0.165 | 0.356 | 0.312 | 4.4% | 16.9% | 20.5% |
| Edouard Julien | 225 | 0.236 | 0.338 | 0.103 | 0.313 | 0.338 | 8.2% | 26.9% | 22.3% |
| Tyler Freeman | 187 | 0.265 | 0.364 | 0.099 | 0.325 | 0.321 | 1.4% | 20.4% | 10.6% |
| Mickey Moniak | 179 | 0.273 | 0.570 | 0.297 | 0.376 | 0.324 | 12.7% | 26.3% | 25.9% |
| Brenton Doyle | 145 | 0.227 | 0.295 | 0.068 | 0.283 | 0.248 | 7.0% | 18.4% | 25.6% |
| Brett Sullivan | 121 | 0.232 | 0.446 | 0.214 | 0.309 | 0.272 | 4.4% | 21.2% | 17.3% |


## Bullpen Fatigue Report

### Pittsburgh Pirates Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Carmen Mlodzinski | 2026-06-20 | 2.0 | 32 |
| Dennis Santana | 2026-06-17 | 1.0 | 11 |
| Evan Sisk | 2026-06-17 | 1.0 | 13 |
| Isaac Mattson | 2026-06-17 | 1.0 | 16 |
| Mason Montgomery | 2026-06-19 | 0.2 | 24 |
| Yohan Ramírez | 2026-06-19 | 1.1 | 6 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Carmen Mlodzinski


### Colorado Rockies Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Antonio Senzatela | 2026-06-19 | 1.0 | 19 |
| Brennan Bernardino | 2026-06-20 | 1.0 | 21 |
| Jaden Hill | 2026-06-19 | 0.2 | 10 |
| Jaden Hill | 2026-06-20 | 0.2 | 13 |
| Jimmy Herget | 2026-06-17 | 1.0 | 19 |
| Jimmy Herget | 2026-06-20 | 1.1 | 20 |
| Zach Agnos | 2026-06-17 | 3.0 | 42 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Brennan Bernardino, Jaden Hill, Jimmy Herget



## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL, CH, CU
- Home pitcher pitch mix to inspect: FF, CH, SI, FC, CU, SL, ST
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 10. Minnesota Twins @ Arizona Diamondbacks

## Game Context

| Field | Value |
| --- | --- |
| Park | Chase Field |
| Time | 2026-06-21T19:15:00Z |
| Away Team | Minnesota Twins |
| Home Team | Arizona Diamondbacks |
| Away Probable Pitcher | Mike Paredes |
| Home Probable Pitcher | Jose Cabrera |


## Away Starting Pitcher: Mike Paredes

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 232 |
| Batted/Result Events | 63 |
| Hits Allowed | 9 |
| Walks | 6 |
| Strikeouts | 10 |
| Home Runs | 2 |
| K Event Rate | 15.9% |
| BB Event Rate | 9.5% |
| HR Event Rate | 3.2% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 16.8% | 39 | 0.111 | 0.111 | 0.000 | 0.250 | 0.312 | 0.0% | 14.3% | 16.7% |
| CH | vs R | 7.8% | 18 | 0.500 | 0.500 | 0.000 | 0.450 | 0.283 | 0.0% | 50.0% | 60.0% |
| FC | vs L | 6.5% | 15 | 0.250 | 1.000 | 0.750 | 0.500 | 0.611 | 33.3% | 57.1% | 12.5% |
| FC | vs R | 7.8% | 18 | 0.000 | 0.000 | 0.000 | 0.117 | 0.246 | 0.0% | 33.3% | 25.0% |
| FF | vs L | 20.7% | 48 | 0.154 | 0.385 | 0.231 | 0.312 | 0.264 | 0.0% | 31.6% | 13.0% |
| FF | vs R | 19.8% | 46 | 0.222 | 0.333 | 0.111 | 0.386 | 0.331 | 0.0% | 28.6% | 19.0% |
| ST | vs L | 8.2% | 19 | 0.250 | 0.250 | 0.000 | 0.267 | 0.290 | 0.0% | 0.0% | 11.1% |
| ST | vs R | 12.5% | 29 | 0.125 | 0.125 | 0.000 | 0.113 | 0.318 | 0.0% | 22.2% | 26.7% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 59 | 4 | 0 | 2 | 1 |
| 2026-06-10 | 58 | 1 | 2 | 4 | 0 |
| 2026-06-04 | 50 | 2 | 1 | 1 | 1 |
| 2026-05-31 | 65 | 2 | 3 | 3 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | Alek Thomas | 11 | 0.364 | 0.909 | 0.545 | 0.523 | 0.281 | 12.5% | 22.2% | 25.9% |
| ST | Jorge Barrosa | 7 | 0.167 | 0.667 | 0.500 | 0.386 | 0.215 | 33.3% | 16.7% | 40.0% |
| FC | Nolan Arenado | 17 | 0.357 | 0.786 | 0.429 | 0.515 | 0.397 | 9.1% | 36.4% | 28.6% |
| CH | Jorge Barrosa | 13 | 0.400 | 0.800 | 0.400 | 0.473 | 0.454 | 9.1% | 10.5% | 16.7% |
| FC | Jorge Barrosa | 10 | 0.300 | 0.700 | 0.400 | 0.415 | 0.206 | 33.3% | 30.8% | 40.0% |
| ST | Gabriel Moreno | 14 | 0.385 | 0.769 | 0.385 | 0.500 | 0.430 | 25.0% | 33.3% | 7.1% |
| FC | Ildemaro Vargas | 14 | 0.615 | 1.000 | 0.385 | 0.693 | 0.420 | 7.7% | 20.0% | 0.0% |
| CH | Corbin Carroll | 37 | 0.176 | 0.559 | 0.382 | 0.330 | 0.359 | 10.3% | 32.6% | 24.6% |
| FC | Corbin Carroll | 23 | 0.286 | 0.619 | 0.333 | 0.446 | 0.428 | 11.8% | 41.4% | 26.8% |
| FF | Gabriel Moreno | 66 | 0.260 | 0.560 | 0.300 | 0.408 | 0.403 | 12.8% | 24.7% | 15.7% |
| FF | Corbin Carroll | 102 | 0.225 | 0.512 | 0.287 | 0.394 | 0.364 | 17.0% | 25.0% | 30.1% |
| FF | Nolan Arenado | 78 | 0.275 | 0.551 | 0.275 | 0.379 | 0.393 | 11.5% | 24.6% | 12.6% |
| FC | Jose Fernandez | 14 | 0.364 | 0.636 | 0.273 | 0.450 | 0.371 | 9.1% | 22.7% | 16.1% |
| ST | Jose Fernandez | 15 | 0.333 | 0.600 | 0.267 | 0.397 | 0.318 | 10.0% | 18.8% | 38.5% |
| FF | Geraldo Perdomo | 108 | 0.325 | 0.578 | 0.253 | 0.448 | 0.392 | 4.0% | 22.6% | 9.2% |
| CH | Lourdes Gurriel | 17 | 0.176 | 0.412 | 0.235 | 0.244 | 0.180 | 0.0% | 18.8% | 43.3% |
| FF | Ketel Marte | 105 | 0.223 | 0.457 | 0.234 | 0.340 | 0.390 | 14.3% | 29.8% | 8.4% |
| FF | Alek Thomas | 33 | 0.226 | 0.419 | 0.194 | 0.326 | 0.311 | 8.7% | 25.0% | 22.4% |
| CH | Gabriel Moreno | 23 | 0.227 | 0.409 | 0.182 | 0.289 | 0.333 | 16.7% | 31.4% | 14.6% |
| CH | Ildemaro Vargas | 44 | 0.268 | 0.439 | 0.171 | 0.355 | 0.325 | 2.6% | 34.0% | 15.1% |
| FF | Adrian Del Castillo | 44 | 0.214 | 0.381 | 0.167 | 0.294 | 0.277 | 10.3% | 21.2% | 26.3% |
| FF | Jorge Barrosa | 59 | 0.130 | 0.296 | 0.167 | 0.211 | 0.166 | 2.4% | 13.9% | 20.2% |
| ST | Ildemaro Vargas | 19 | 0.111 | 0.278 | 0.167 | 0.237 | 0.267 | 0.0% | 34.6% | 26.3% |
| FF | Ryan Waldschmidt | 29 | 0.231 | 0.385 | 0.154 | 0.362 | 0.358 | 17.6% | 17.9% | 20.8% |
| FC | Alek Thomas | 8 | 0.143 | 0.286 | 0.143 | 0.244 | 0.501 | 28.6% | 30.8% | 0.0% |
| FC | Ryan Waldschmidt | 19 | 0.375 | 0.500 | 0.125 | 0.432 | 0.378 | 0.0% | 18.2% | 17.9% |
| CH | Nolan Arenado | 29 | 0.240 | 0.360 | 0.120 | 0.295 | 0.288 | 0.0% | 24.3% | 28.8% |
| ST | Geraldo Perdomo | 14 | 0.400 | 0.500 | 0.100 | 0.482 | 0.402 | 0.0% | 13.3% | 13.0% |
| CH | Geraldo Perdomo | 49 | 0.244 | 0.341 | 0.098 | 0.284 | 0.324 | 2.6% | 24.3% | 12.5% |
| FC | Gabriel Moreno | 13 | 0.273 | 0.364 | 0.091 | 0.342 | 0.361 | 10.0% | 61.5% | 30.0% |


## Home Starting Pitcher: Jose Cabrera

### Pitcher Profile

| Stat | Value |
| --- | --- |
| No data | — |


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


## Minnesota Twins Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Josh Bell | 318 | 0.234 | 0.379 | 0.145 | 0.306 | 0.320 | 9.6% | 22.2% | 22.6% |
| Brooks Lee | 315 | 0.256 | 0.443 | 0.187 | 0.347 | 0.279 | 4.9% | 20.6% | 18.1% |
| Luke Keaschall | 311 | 0.266 | 0.365 | 0.099 | 0.329 | 0.298 | 3.5% | 22.4% | 14.0% |
| Byron Buxton | 306 | 0.273 | 0.608 | 0.335 | 0.398 | 0.353 | 20.0% | 30.6% | 28.9% |
| Kody Clemens | 270 | 0.251 | 0.486 | 0.235 | 0.351 | 0.332 | 12.6% | 28.7% | 22.0% |
| Austin Martin | 251 | 0.256 | 0.336 | 0.081 | 0.334 | 0.308 | 2.4% | 18.5% | 18.5% |
| Trevor Larnach | 240 | 0.274 | 0.418 | 0.144 | 0.365 | 0.338 | 8.0% | 25.5% | 26.0% |
| Víctor Caratini | 226 | 0.238 | 0.381 | 0.143 | 0.323 | 0.347 | 8.0% | 23.9% | 21.1% |
| Royce Lewis | 199 | 0.193 | 0.352 | 0.159 | 0.289 | 0.296 | 12.7% | 25.4% | 30.0% |
| Ryan Jeffers | 166 | 0.298 | 0.532 | 0.234 | 0.417 | 0.389 | 15.4% | 27.0% | 15.8% |
| Tristan Gray | 165 | 0.230 | 0.336 | 0.105 | 0.265 | 0.286 | 6.7% | 25.8% | 29.9% |
| Matt Wallner | 151 | 0.194 | 0.343 | 0.149 | 0.288 | 0.281 | 11.5% | 24.1% | 39.3% |


## Arizona Diamondbacks Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Corbin Carroll | 327 | 0.271 | 0.539 | 0.268 | 0.391 | 0.366 | 13.3% | 32.4% | 27.1% |
| Ketel Marte | 326 | 0.257 | 0.446 | 0.189 | 0.335 | 0.369 | 10.4% | 33.6% | 19.0% |
| Geraldo Perdomo | 320 | 0.242 | 0.354 | 0.112 | 0.332 | 0.335 | 2.7% | 21.9% | 10.9% |
| Nolan Arenado | 285 | 0.242 | 0.405 | 0.163 | 0.324 | 0.302 | 6.0% | 23.3% | 21.0% |
| Ildemaro Vargas | 272 | 0.263 | 0.420 | 0.157 | 0.331 | 0.308 | 3.5% | 26.9% | 12.2% |
| Gabriel Moreno | 207 | 0.281 | 0.489 | 0.208 | 0.383 | 0.363 | 10.5% | 26.9% | 16.8% |
| Jose Fernandez | 178 | 0.253 | 0.349 | 0.096 | 0.301 | 0.276 | 3.9% | 24.7% | 23.3% |
| Adrian Del Castillo | 145 | 0.189 | 0.311 | 0.121 | 0.266 | 0.259 | 5.7% | 20.2% | 25.6% |
| Jorge Barrosa | 137 | 0.215 | 0.438 | 0.223 | 0.319 | 0.214 | 8.2% | 16.4% | 25.1% |
| Ryan Waldschmidt | 131 | 0.273 | 0.380 | 0.107 | 0.327 | 0.289 | 7.6% | 22.1% | 29.0% |
| Lourdes Gurriel | 119 | 0.211 | 0.275 | 0.064 | 0.242 | 0.279 | 5.7% | 20.8% | 23.1% |
| Alek Thomas | 117 | 0.193 | 0.394 | 0.202 | 0.280 | 0.292 | 9.9% | 27.6% | 23.7% |


## Bullpen Fatigue Report

### Minnesota Twins Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Andrew Morris | 2026-06-18 | 0.2 | 8 |
| Anthony Banda | 2026-06-20 | 1.0 | 12 |
| Cody Laweryson | 2026-06-18 | 1.0 | 17 |
| Cody Laweryson | 2026-06-19 | 0.2 | 5 |
| Eric Orze | 2026-06-18 | 1.0 | 12 |
| Eric Orze | 2026-06-20 | 1.1 | 24 |
| Justin Lawrence | 2026-06-18 | 1.0 | 18 |
| Justin Lawrence | 2026-06-20 | 0.2 | 40 |
| Taylor Rogers | 2026-06-18 | 0.1 | 15 |
| Travis Adams | 2026-06-19 | 1.1 | 42 |
| Yoendrys Gómez | 2026-06-20 | 1.0 | 7 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Anthony Banda, Eric Orze, Justin Lawrence, Yoendrys Gómez


### Arizona Diamondbacks Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brandyn Garcia | 2026-06-19 | 1.0 | 14 |
| Drey Jameson | 2026-06-19 | 1.2 | 33 |
| Ildemaro Vargas | 2026-06-20 | 1.2 | 20 |
| Jonathan Loáisiga | 2026-06-19 | 1.1 | 10 |
| Juan Morillo | 2026-06-17 | 1.0 | 9 |
| Kevin Ginkel | 2026-06-19 | 1.0 | 16 |
| Paul Sewald | 2026-06-19 | 1.0 | 13 |
| Philip Abner | 2026-06-20 | 2.2 | 44 |
| Ryan Thompson | 2026-06-19 | 1.0 | 20 |
| Taylor Clarke | 2026-06-17 | 1.0 | 14 |
| Taylor Clarke | 2026-06-19 | 1.0 | 11 |
| Yilber Díaz | 2026-06-20 | 0.2 | 44 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Ildemaro Vargas, Philip Abner, Yilber Díaz



## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, CH, ST, FC
- Home pitcher pitch mix to inspect: No current Statcast sample
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 11. Los Angeles Angels @ Athletics

## Game Context

| Field | Value |
| --- | --- |
| Park | Sutter Health Park |
| Time | 2026-06-21T20:05:00Z |
| Away Team | Los Angeles Angels |
| Home Team | Athletics |
| Away Probable Pitcher | Reid Detmers |
| Home Probable Pitcher | Jack Perkins |


## Away Starting Pitcher: Reid Detmers

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1487 |
| Batted/Result Events | 369 |
| Hits Allowed | 66 |
| Walks | 27 |
| Strikeouts | 103 |
| Home Runs | 7 |
| K Event Rate | 27.9% |
| BB Event Rate | 7.3% |
| HR Event Rate | 1.9% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.4% | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% | 66.7% |
| CH | vs R | 11.0% | 163 | 0.286 | 0.600 | 0.314 | 0.379 | 0.342 | 9.7% | 22.9% | 26.0% |
| CU | vs L | 2.4% | 36 | 0.200 | 0.400 | 0.200 | 0.325 | 0.270 | 0.0% | 0.0% | 44.4% |
| CU | vs R | 7.9% | 118 | 0.158 | 0.263 | 0.105 | 0.284 | 0.215 | 0.0% | 4.3% | 35.9% |
| FF | vs L | 11.1% | 165 | 0.179 | 0.256 | 0.077 | 0.232 | 0.300 | 12.9% | 34.0% | 14.7% |
| FF | vs R | 33.4% | 496 | 0.206 | 0.327 | 0.121 | 0.284 | 0.267 | 6.1% | 22.2% | 17.9% |
| PO | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs L | 1.4% | 21 | 0.000 | 0.000 | 0.000 | 0.262 | 0.390 | 0.0% | 0.0% | 0.0% |
| SI | vs R | 0.7% | 10 | 0.500 | 0.500 | 0.000 | 0.450 | 0.500 | 50.0% | 20.0% | 0.0% |
| SL | vs L | 10.0% | 149 | 0.229 | 0.257 | 0.029 | 0.242 | 0.236 | 3.8% | 23.4% | 27.5% |
| SL | vs R | 21.5% | 320 | 0.167 | 0.262 | 0.095 | 0.239 | 0.219 | 4.5% | 13.7% | 33.1% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-16 | 90 | 3 | 0 | 3 | 0 |
| 2026-06-10 | 89 | 1 | 0 | 9 | 1 |
| 2026-06-05 | 91 | 2 | 2 | 6 | 0 |
| 2026-05-30 | 93 | 5 | 3 | 7 | 1 |
| 2026-05-24 | 96 | 1 | 0 | 14 | 1 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Lawrence Butler | 17 | 0.286 | 0.714 | 0.429 | 0.465 | 0.514 | 25.0% | 33.3% | 23.3% |
| CU | Tyler Soderstrom | 14 | 0.357 | 0.786 | 0.429 | 0.475 | 0.240 | 8.3% | 42.1% | 23.3% |
| FF | Shea Langeliers | 76 | 0.250 | 0.676 | 0.426 | 0.417 | 0.413 | 22.9% | 23.8% | 20.8% |
| FF | Nick Kurtz | 105 | 0.272 | 0.667 | 0.395 | 0.460 | 0.479 | 29.2% | 34.1% | 30.8% |
| FF | Brent Rooker | 58 | 0.184 | 0.571 | 0.388 | 0.356 | 0.355 | 29.6% | 26.3% | 29.3% |
| CH | Henry Bolte | 9 | 0.625 | 1.000 | 0.375 | 0.700 | 0.544 | 16.7% | 50.0% | 41.2% |
| FF | Max Muncy | 123 | 0.347 | 0.713 | 0.366 | 0.491 | 0.462 | 23.0% | 32.3% | 18.6% |
| SL | Nick Kurtz | 48 | 0.250 | 0.575 | 0.325 | 0.402 | 0.336 | 20.8% | 35.6% | 38.5% |
| SL | Tyler Soderstrom | 43 | 0.189 | 0.486 | 0.297 | 0.357 | 0.347 | 25.0% | 28.2% | 39.7% |
| FF | Zack Gelof | 66 | 0.200 | 0.483 | 0.283 | 0.334 | 0.266 | 10.8% | 25.3% | 28.1% |
| SL | Max Muncy | 66 | 0.255 | 0.527 | 0.273 | 0.380 | 0.353 | 20.7% | 37.9% | 39.8% |
| FF | Henry Bolte | 24 | 0.318 | 0.545 | 0.227 | 0.396 | 0.318 | 23.1% | 25.0% | 34.0% |
| CH | Zack Gelof | 16 | 0.286 | 0.500 | 0.214 | 0.381 | 0.384 | 20.0% | 36.8% | 32.3% |
| FF | Tyler Soderstrom | 92 | 0.208 | 0.417 | 0.208 | 0.358 | 0.376 | 12.7% | 23.2% | 16.2% |
| CH | Jeff Mcneil | 36 | 0.171 | 0.371 | 0.200 | 0.240 | 0.278 | 3.0% | 22.8% | 18.4% |
| SL | Zack Gelof | 31 | 0.194 | 0.387 | 0.194 | 0.245 | 0.247 | 3.7% | 28.9% | 15.2% |
| CH | Carlos Cortes | 34 | 0.233 | 0.400 | 0.167 | 0.321 | 0.279 | 8.0% | 15.8% | 31.6% |
| SL | Brent Rooker | 31 | 0.290 | 0.452 | 0.161 | 0.377 | 0.210 | 9.5% | 14.7% | 51.4% |
| SL | Carlos Cortes | 22 | 0.316 | 0.474 | 0.158 | 0.391 | 0.394 | 7.7% | 37.0% | 33.3% |
| FF | Lawrence Butler | 69 | 0.177 | 0.323 | 0.145 | 0.275 | 0.323 | 7.5% | 26.0% | 26.9% |
| CU | Shea Langeliers | 17 | 0.400 | 0.533 | 0.133 | 0.441 | 0.470 | 18.2% | 64.3% | 27.3% |
| CH | Brent Rooker | 24 | 0.174 | 0.304 | 0.130 | 0.263 | 0.197 | 18.2% | 21.7% | 44.9% |
| CU | Zack Gelof | 11 | 0.125 | 0.250 | 0.125 | 0.259 | 0.189 | 0.0% | 14.3% | 50.0% |
| FF | Carlos Cortes | 65 | 0.309 | 0.418 | 0.109 | 0.376 | 0.412 | 8.3% | 19.2% | 9.4% |
| SL | Henry Bolte | 21 | 0.263 | 0.368 | 0.105 | 0.281 | 0.271 | 7.7% | 26.1% | 33.3% |
| CH | Lawrence Butler | 31 | 0.367 | 0.467 | 0.100 | 0.406 | 0.330 | 7.7% | 28.6% | 31.6% |
| CH | Max Muncy | 58 | 0.264 | 0.358 | 0.094 | 0.324 | 0.349 | 9.5% | 31.4% | 31.6% |
| FF | Jacob Wilson | 47 | 0.209 | 0.302 | 0.093 | 0.248 | 0.232 | 3.0% | 14.6% | 15.5% |
| CH | Nick Kurtz | 43 | 0.167 | 0.250 | 0.083 | 0.285 | 0.294 | 13.0% | 17.1% | 33.8% |
| SL | Shea Langeliers | 61 | 0.273 | 0.345 | 0.073 | 0.313 | 0.311 | 11.6% | 26.4% | 28.7% |


## Home Starting Pitcher: Jack Perkins

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 786 |
| Batted/Result Events | 202 |
| Hits Allowed | 46 |
| Walks | 16 |
| Strikeouts | 52 |
| Home Runs | 5 |
| K Event Rate | 25.7% |
| BB Event Rate | 7.9% |
| HR Event Rate | 2.5% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 12.7% | 100 | 0.281 | 0.312 | 0.031 | 0.348 | 0.245 | 0.0% | 30.3% | 36.2% |
| CH | vs R | 2.2% | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.051 | 0.0% | 50.0% | 66.7% |
| FC | vs L | 4.8% | 38 | 0.286 | 0.429 | 0.143 | 0.307 | 0.221 | 0.0% | 27.3% | 21.1% |
| FC | vs R | 3.9% | 31 | 0.333 | 0.778 | 0.444 | 0.415 | 0.416 | 10.0% | 25.0% | 20.0% |
| FF | vs L | 20.0% | 157 | 0.375 | 0.542 | 0.167 | 0.473 | 0.459 | 10.0% | 15.5% | 11.0% |
| FF | vs R | 19.1% | 150 | 0.167 | 0.278 | 0.111 | 0.262 | 0.295 | 3.7% | 14.5% | 21.2% |
| SI | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs R | 1.7% | 13 | 0.500 | 1.000 | 0.500 | 0.643 | 0.438 | 16.7% | 57.1% | 22.2% |
| SL | vs L | 0.6% | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.014 | 0.0% | 50.0% | 33.3% |
| SL | vs R | 1.9% | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.266 | 0.0% | 25.0% | 42.9% |
| ST | vs L | 13.9% | 109 | 0.125 | 0.167 | 0.042 | 0.209 | 0.198 | 0.0% | 19.0% | 50.0% |
| ST | vs R | 14.6% | 115 | 0.385 | 0.500 | 0.115 | 0.386 | 0.348 | 10.0% | 16.2% | 25.9% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-16 | 85 | 6 | 2 | 6 | 1 |
| 2026-06-10 | 89 | 5 | 3 | 4 | 2 |
| 2026-06-05 | 75 | 5 | 2 | 6 | 1 |
| 2026-05-31 | 30 | 0 | 0 | 0 | 0 |
| 2026-05-30 | 24 | 1 | 2 | 2 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | Mike Trout | 30 | 0.348 | 0.913 | 0.565 | 0.562 | 0.476 | 19.0% | 33.3% | 18.4% |
| ST | Mike Trout | 21 | 0.222 | 0.778 | 0.556 | 0.488 | 0.506 | 45.5% | 29.2% | 19.4% |
| ST | Vaughn Grissom | 15 | 0.357 | 0.857 | 0.500 | 0.517 | 0.462 | 21.4% | 26.3% | 11.5% |
| FC | Wade Meckler | 9 | 0.250 | 0.750 | 0.500 | 0.439 | 0.422 | 14.3% | 22.2% | 35.7% |
| FC | Zach Neto | 22 | 0.333 | 0.722 | 0.389 | 0.489 | 0.494 | 13.3% | 25.0% | 18.0% |
| FF | Jorge Soler | 66 | 0.220 | 0.542 | 0.322 | 0.367 | 0.254 | 17.1% | 30.3% | 28.7% |
| FF | Vaughn Grissom | 38 | 0.200 | 0.500 | 0.300 | 0.338 | 0.384 | 15.4% | 25.0% | 18.3% |
| ST | Logan O'Hoppe | 10 | 0.100 | 0.400 | 0.300 | 0.200 | 0.171 | 0.0% | 27.3% | 30.6% |
| FF | Zach Neto | 103 | 0.258 | 0.551 | 0.292 | 0.381 | 0.344 | 15.6% | 25.7% | 20.6% |
| FC | Oswald Peraza | 15 | 0.286 | 0.571 | 0.286 | 0.443 | 0.433 | 16.7% | 36.4% | 26.7% |
| FF | Adam Frazier | 39 | 0.233 | 0.500 | 0.267 | 0.371 | 0.282 | 8.3% | 10.3% | 16.2% |
| CH | Oswald Peraza | 28 | 0.296 | 0.556 | 0.259 | 0.373 | 0.292 | 9.5% | 22.9% | 32.7% |
| FF | Mike Trout | 141 | 0.292 | 0.547 | 0.255 | 0.467 | 0.470 | 22.2% | 25.0% | 14.0% |
| FF | Josh Lowe | 44 | 0.350 | 0.600 | 0.250 | 0.433 | 0.298 | 17.4% | 19.7% | 24.5% |
| FF | Jo Adell | 91 | 0.286 | 0.536 | 0.250 | 0.360 | 0.388 | 15.4% | 20.7% | 19.0% |
| ST | Nolan Schanuel | 22 | 0.250 | 0.500 | 0.250 | 0.350 | 0.204 | 6.2% | 22.7% | 33.3% |
| FC | Adam Frazier | 4 | 0.500 | 0.750 | 0.250 | 0.537 | 0.202 | 0.0% | 9.1% | 16.7% |
| ST | Zach Neto | 32 | 0.167 | 0.400 | 0.233 | 0.264 | 0.211 | 11.8% | 23.3% | 44.3% |
| FC | Jorge Soler | 18 | 0.267 | 0.467 | 0.200 | 0.378 | 0.484 | 21.4% | 19.4% | 25.6% |
| ST | Jorge Soler | 24 | 0.190 | 0.381 | 0.190 | 0.269 | 0.257 | 10.0% | 29.2% | 51.0% |
| ST | Jo Adell | 35 | 0.312 | 0.500 | 0.188 | 0.379 | 0.272 | 9.5% | 32.7% | 25.9% |
| FF | Logan O'Hoppe | 51 | 0.239 | 0.413 | 0.174 | 0.320 | 0.404 | 16.2% | 29.6% | 16.8% |
| FF | Nolan Schanuel | 83 | 0.268 | 0.437 | 0.169 | 0.351 | 0.363 | 5.1% | 20.0% | 5.4% |
| ST | Oswald Peraza | 26 | 0.292 | 0.458 | 0.167 | 0.352 | 0.322 | 6.2% | 14.3% | 38.3% |
| FF | Oswald Peraza | 76 | 0.235 | 0.397 | 0.162 | 0.321 | 0.322 | 8.7% | 22.2% | 20.9% |
| CH | Mike Trout | 28 | 0.200 | 0.360 | 0.160 | 0.288 | 0.258 | 10.0% | 16.7% | 33.9% |
| FF | Wade Meckler | 36 | 0.276 | 0.414 | 0.138 | 0.376 | 0.371 | 4.8% | 20.6% | 15.0% |
| CH | Nolan Schanuel | 34 | 0.194 | 0.290 | 0.097 | 0.279 | 0.222 | 0.0% | 6.5% | 23.0% |
| CH | Zach Neto | 39 | 0.094 | 0.188 | 0.094 | 0.246 | 0.245 | 5.9% | 12.2% | 42.1% |
| CH | Jorge Soler | 28 | 0.185 | 0.259 | 0.074 | 0.243 | 0.184 | 0.0% | 24.1% | 34.0% |


## Los Angeles Angels Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Zach Neto | 361 | 0.223 | 0.445 | 0.223 | 0.340 | 0.320 | 13.5% | 22.7% | 30.9% |
| Mike Trout | 353 | 0.240 | 0.473 | 0.233 | 0.390 | 0.412 | 20.2% | 26.5% | 20.4% |
| Jo Adell | 347 | 0.255 | 0.403 | 0.148 | 0.306 | 0.327 | 8.8% | 26.3% | 25.4% |
| Nolan Schanuel | 264 | 0.247 | 0.368 | 0.121 | 0.319 | 0.314 | 2.6% | 18.7% | 16.6% |
| Jorge Soler | 262 | 0.224 | 0.422 | 0.198 | 0.324 | 0.306 | 12.1% | 26.6% | 33.9% |
| Oswald Peraza | 254 | 0.265 | 0.416 | 0.151 | 0.334 | 0.308 | 8.1% | 22.5% | 25.3% |
| Logan O'Hoppe | 194 | 0.233 | 0.355 | 0.122 | 0.298 | 0.291 | 10.9% | 26.1% | 26.1% |
| Vaughn Grissom | 168 | 0.231 | 0.381 | 0.150 | 0.314 | 0.339 | 6.9% | 26.8% | 17.7% |
| Josh Lowe | 152 | 0.204 | 0.359 | 0.155 | 0.268 | 0.263 | 8.2% | 16.3% | 25.4% |
| Yoán Moncada | 147 | 0.202 | 0.306 | 0.105 | 0.295 | 0.270 | 8.6% | 22.7% | 29.4% |
| Adam Frazier | 115 | 0.198 | 0.312 | 0.115 | 0.285 | 0.237 | 2.9% | 9.8% | 24.5% |
| Wade Meckler | 93 | 0.277 | 0.422 | 0.145 | 0.354 | 0.324 | 6.2% | 16.8% | 23.9% |


## Athletics Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nick Kurtz | 366 | 0.285 | 0.536 | 0.251 | 0.415 | 0.389 | 18.2% | 32.7% | 31.9% |
| Shea Langeliers | 334 | 0.272 | 0.526 | 0.255 | 0.371 | 0.372 | 14.6% | 28.3% | 23.9% |
| Tyler Soderstrom | 326 | 0.238 | 0.477 | 0.238 | 0.363 | 0.336 | 10.9% | 29.0% | 20.1% |
| Jeff Mcneil | 261 | 0.227 | 0.309 | 0.082 | 0.282 | 0.303 | 1.0% | 18.1% | 15.0% |
| Zack Gelof | 232 | 0.280 | 0.488 | 0.209 | 0.364 | 0.295 | 7.1% | 27.0% | 25.6% |
| Lawrence Butler | 224 | 0.198 | 0.317 | 0.119 | 0.279 | 0.306 | 7.3% | 26.4% | 26.6% |
| Carlos Cortes | 216 | 0.262 | 0.414 | 0.152 | 0.334 | 0.357 | 8.0% | 24.1% | 19.1% |
| Jacob Wilson | 215 | 0.283 | 0.390 | 0.107 | 0.319 | 0.277 | 1.6% | 20.4% | 13.4% |
| Brent Rooker | 215 | 0.214 | 0.411 | 0.198 | 0.316 | 0.315 | 16.5% | 26.9% | 35.2% |
| Max Muncy | 150 | 0.231 | 0.448 | 0.216 | 0.328 | 0.298 | 13.6% | 34.9% | 30.5% |
| Darell Hernaiz | 145 | 0.248 | 0.302 | 0.054 | 0.292 | 0.263 | 1.0% | 13.7% | 19.9% |
| Henry Bolte | 133 | 0.307 | 0.412 | 0.105 | 0.359 | 0.306 | 6.7% | 30.8% | 33.0% |


## Bullpen Fatigue Report

### Los Angeles Angels Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brent Suter | 2026-06-18 | 2.0 | 28 |
| Brett Kerry | 2026-06-17 | 4.0 | 59 |
| Chase Silseth | 2026-06-19 | 1.0 | 20 |
| José Fermin | 2026-06-17 | 1.0 | 15 |
| Kirby Yates | 2026-06-19 | 0.1 | 10 |
| Kirby Yates | 2026-06-20 | 1.0 | 15 |
| Mitch Farris | 2026-06-19 | 2.0 | 41 |
| Ryan Zeferjahn | 2026-06-18 | 1.0 | 21 |
| Ryan Zeferjahn | 2026-06-20 | 1.2 | 24 |
| Sam Bachman | 2026-06-19 | 1.0 | 21 |
| Samy Natera Jr. | 2026-06-19 | 0.0 | 5 |
| Samy Natera Jr. | 2026-06-20 | 1.1 | 28 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Kirby Yates, Ryan Zeferjahn, Samy Natera Jr.


### Athletics Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Elvis Alvarado | 2026-06-19 | 2.0 | 21 |
| Geoff Hartlieb | 2026-06-20 | 3.0 | 43 |
| Hogan Harris | 2026-06-18 | 1.0 | 25 |
| José Suarez | 2026-06-17 | 2.2 | 43 |
| José Suarez | 2026-06-19 | 2.0 | 30 |
| Justin Sterner | 2026-06-19 | 1.1 | 26 |
| Luis Medina | 2026-06-17 | 3.0 | 45 |
| Mason Barnett | 2026-06-18 | 1.0 | 30 |
| Scott Barlow | 2026-06-17 | 0.1 | 17 |
| Scott Barlow | 2026-06-19 | 1.0 | 11 |
| Scott Barlow | 2026-06-20 | 0.2 | 24 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Geoff Hartlieb, Scott Barlow



## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL, CH, CU
- Home pitcher pitch mix to inspect: FF, ST, CH, FC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 12. Baltimore Orioles @ Los Angeles Dodgers

## Game Context

| Field | Value |
| --- | --- |
| Park | UNIQLO Field at Dodger Stadium |
| Time | 2026-06-21T20:10:00Z |
| Away Team | Baltimore Orioles |
| Home Team | Los Angeles Dodgers |
| Away Probable Pitcher | Brandon Young |
| Home Probable Pitcher | Emmet Sheehan |


## Away Starting Pitcher: Brandon Young

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 957 |
| Batted/Result Events | 266 |
| Hits Allowed | 55 |
| Walks | 23 |
| Strikeouts | 44 |
| Home Runs | 6 |
| K Event Rate | 16.5% |
| BB Event Rate | 8.6% |
| HR Event Rate | 2.3% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 9.1% | 87 | 0.214 | 0.286 | 0.071 | 0.247 | 0.350 | 14.3% | 23.8% | 18.5% |
| CU | vs R | 2.2% | 21 | 0.400 | 0.600 | 0.200 | 0.430 | 0.548 | 20.0% | 20.0% | 9.1% |
| FF | vs L | 26.5% | 254 | 0.123 | 0.231 | 0.108 | 0.217 | 0.308 | 9.1% | 20.9% | 16.0% |
| FF | vs R | 12.4% | 119 | 0.167 | 0.333 | 0.167 | 0.281 | 0.339 | 7.7% | 15.9% | 23.0% |
| FS | vs L | 18.6% | 178 | 0.255 | 0.319 | 0.064 | 0.274 | 0.339 | 2.3% | 33.8% | 14.0% |
| FS | vs R | 2.4% | 23 | 0.333 | 0.333 | 0.000 | 0.417 | 0.382 | 0.0% | 50.0% | 28.6% |
| SI | vs L | 2.7% | 26 | 0.600 | 1.200 | 0.600 | 0.738 | 0.550 | 25.0% | 37.5% | 20.0% |
| SI | vs R | 10.8% | 103 | 0.355 | 0.419 | 0.065 | 0.412 | 0.303 | 3.4% | 25.6% | 6.0% |
| SL | vs L | 1.6% | 15 | 0.333 | 1.000 | 0.667 | 0.542 | 0.406 | 50.0% | 40.0% | 37.5% |
| SL | vs R | 13.7% | 131 | 0.225 | 0.300 | 0.075 | 0.267 | 0.242 | 3.8% | 27.0% | 42.4% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-16 | 92 | 4 | 4 | 2 | 0 |
| 2026-06-10 | 88 | 2 | 2 | 5 | 0 |
| 2026-06-05 | 85 | 7 | 0 | 4 | 1 |
| 2026-05-30 | 86 | 7 | 1 | 7 | 0 |
| 2026-05-24 | 105 | 5 | 2 | 4 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | Dalton Rushing | 16 | 0.400 | 1.100 | 0.700 | 0.647 | 0.581 | 28.6% | 27.3% | 30.0% |
| FS | Shohei Ohtani | 11 | 0.444 | 0.889 | 0.444 | 0.586 | 0.397 | 12.5% | 25.0% | 19.0% |
| SI | Shohei Ohtani | 48 | 0.513 | 0.949 | 0.436 | 0.621 | 0.576 | 19.4% | 43.1% | 16.7% |
| CU | Andy Pages | 14 | 0.333 | 0.750 | 0.417 | 0.436 | 0.284 | 0.0% | 26.7% | 30.4% |
| FS | Freddie Freeman | 10 | 0.500 | 0.900 | 0.400 | 0.595 | 0.395 | 20.0% | 38.5% | 12.5% |
| CU | Freddie Freeman | 23 | 0.316 | 0.684 | 0.368 | 0.467 | 0.403 | 17.6% | 30.0% | 11.1% |
| FF | Max Muncy | 123 | 0.347 | 0.713 | 0.366 | 0.491 | 0.462 | 23.0% | 32.3% | 18.6% |
| FS | Mookie Betts | 4 | 0.333 | 0.667 | 0.333 | 0.487 | 0.327 | 50.0% | 25.0% | 33.3% |
| FS | Alex Freeland | 11 | 0.333 | 0.667 | 0.333 | 0.491 | 0.310 | 0.0% | 50.0% | 38.5% |
| FF | Mookie Betts | 52 | 0.217 | 0.543 | 0.326 | 0.376 | 0.354 | 16.7% | 27.1% | 4.1% |
| FF | Freddie Freeman | 103 | 0.330 | 0.648 | 0.318 | 0.448 | 0.403 | 13.4% | 20.5% | 18.6% |
| SL | Dalton Rushing | 23 | 0.273 | 0.591 | 0.318 | 0.376 | 0.381 | 11.8% | 56.0% | 32.4% |
| SL | Teoscar Hernández | 28 | 0.200 | 0.480 | 0.280 | 0.327 | 0.302 | 21.4% | 21.4% | 37.5% |
| SL | Max Muncy | 66 | 0.255 | 0.527 | 0.273 | 0.380 | 0.353 | 20.7% | 37.9% | 39.8% |
| SL | Shohei Ohtani | 39 | 0.281 | 0.531 | 0.250 | 0.406 | 0.384 | 8.3% | 40.0% | 27.6% |
| SI | Max Muncy | 61 | 0.308 | 0.558 | 0.250 | 0.416 | 0.387 | 14.0% | 28.2% | 11.7% |
| SI | Dalton Rushing | 10 | 0.375 | 0.625 | 0.250 | 0.480 | 0.343 | 0.0% | 19.0% | 0.0% |
| FF | Dalton Rushing | 60 | 0.286 | 0.531 | 0.245 | 0.426 | 0.353 | 12.9% | 29.5% | 29.9% |
| FF | Shohei Ohtani | 90 | 0.224 | 0.461 | 0.237 | 0.362 | 0.431 | 25.0% | 25.2% | 19.7% |
| SL | Mookie Betts | 34 | 0.233 | 0.433 | 0.200 | 0.359 | 0.310 | 4.2% | 21.2% | 24.0% |
| SI | Will Smith | 48 | 0.300 | 0.500 | 0.200 | 0.358 | 0.474 | 22.2% | 33.3% | 4.1% |
| FF | Teoscar Hernández | 54 | 0.283 | 0.478 | 0.196 | 0.368 | 0.367 | 14.3% | 23.8% | 17.1% |
| SI | Hyeseong Kim | 23 | 0.381 | 0.571 | 0.190 | 0.407 | 0.355 | 5.6% | 20.0% | 16.4% |
| FF | Will Smith | 66 | 0.226 | 0.415 | 0.189 | 0.357 | 0.458 | 20.0% | 27.8% | 14.5% |
| FF | Kyle Tucker | 105 | 0.244 | 0.433 | 0.189 | 0.364 | 0.365 | 11.4% | 23.2% | 18.6% |
| SI | Freddie Freeman | 66 | 0.236 | 0.418 | 0.182 | 0.348 | 0.366 | 8.2% | 22.6% | 17.4% |
| FF | Miguel Rojas | 46 | 0.310 | 0.476 | 0.167 | 0.354 | 0.373 | 10.8% | 37.7% | 11.1% |
| FF | Alex Freeland | 58 | 0.306 | 0.469 | 0.163 | 0.383 | 0.369 | 7.3% | 30.0% | 16.7% |
| SI | Andy Pages | 76 | 0.294 | 0.456 | 0.162 | 0.354 | 0.386 | 6.7% | 36.7% | 9.2% |
| SL | Kyle Tucker | 40 | 0.182 | 0.333 | 0.152 | 0.285 | 0.291 | 8.7% | 22.4% | 29.5% |


## Home Starting Pitcher: Emmet Sheehan

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1251 |
| Batted/Result Events | 305 |
| Hits Allowed | 66 |
| Walks | 20 |
| Strikeouts | 81 |
| Home Runs | 13 |
| K Event Rate | 26.6% |
| BB Event Rate | 6.6% |
| HR Event Rate | 4.3% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 13.7% | 172 | 0.286 | 0.411 | 0.125 | 0.321 | 0.273 | 0.0% | 33.3% | 23.6% |
| CH | vs R | 2.0% | 25 | 0.143 | 0.143 | 0.000 | 0.200 | 0.210 | 0.0% | 22.2% | 16.7% |
| CU | vs L | 6.8% | 85 | 0.200 | 0.300 | 0.100 | 0.259 | 0.232 | 0.0% | 23.8% | 15.4% |
| CU | vs R | 2.4% | 30 | 0.333 | 0.667 | 0.333 | 0.417 | 0.315 | 0.0% | 16.7% | 33.3% |
| FF | vs L | 24.9% | 312 | 0.245 | 0.698 | 0.453 | 0.417 | 0.406 | 22.5% | 24.1% | 26.5% |
| FF | vs R | 18.2% | 228 | 0.239 | 0.457 | 0.217 | 0.355 | 0.391 | 13.5% | 26.7% | 21.4% |
| SL | vs L | 11.1% | 139 | 0.200 | 0.429 | 0.229 | 0.297 | 0.279 | 14.3% | 23.3% | 35.7% |
| SL | vs R | 20.6% | 258 | 0.221 | 0.368 | 0.147 | 0.275 | 0.229 | 9.3% | 18.4% | 40.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-14 | 85 | 4 | 1 | 8 | 1 |
| 2026-06-07 | 49 | 3 | 2 | 2 | 0 |
| 2026-06-01 | 92 | 3 | 0 | 3 | 2 |
| 2026-05-25 | 92 | 5 | 1 | 8 | 0 |
| 2026-05-19 | 67 | 5 | 1 | 2 | 2 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Colton Cowser | 29 | 0.286 | 0.750 | 0.464 | 0.436 | 0.382 | 30.8% | 39.1% | 54.5% |
| CU | Leody Taveras | 12 | 0.273 | 0.636 | 0.364 | 0.421 | 0.421 | 25.0% | 37.5% | 34.5% |
| FF | Pete Alonso | 94 | 0.276 | 0.632 | 0.356 | 0.402 | 0.433 | 25.8% | 38.3% | 23.4% |
| CH | Pete Alonso | 33 | 0.290 | 0.613 | 0.323 | 0.397 | 0.373 | 17.4% | 42.9% | 28.6% |
| FF | Jeremiah Jackson | 40 | 0.263 | 0.579 | 0.316 | 0.370 | 0.319 | 10.0% | 23.1% | 15.5% |
| CU | Gunnar Henderson | 24 | 0.304 | 0.609 | 0.304 | 0.398 | 0.348 | 5.0% | 30.0% | 21.2% |
| SL | Coby Mayo | 44 | 0.227 | 0.523 | 0.295 | 0.333 | 0.269 | 17.4% | 51.2% | 48.9% |
| CU | Coby Mayo | 13 | 0.167 | 0.417 | 0.250 | 0.277 | 0.218 | 16.7% | 25.0% | 43.5% |
| SL | Adley Rutschman | 22 | 0.190 | 0.429 | 0.238 | 0.277 | 0.283 | 5.6% | 23.3% | 15.4% |
| FF | Adley Rutschman | 86 | 0.264 | 0.500 | 0.236 | 0.367 | 0.322 | 8.1% | 27.0% | 4.4% |
| SL | Jeremiah Jackson | 46 | 0.233 | 0.465 | 0.233 | 0.290 | 0.320 | 12.1% | 38.3% | 38.6% |
| CH | Samuel Basallo | 39 | 0.270 | 0.486 | 0.216 | 0.364 | 0.295 | 12.5% | 38.5% | 29.7% |
| FF | Samuel Basallo | 78 | 0.268 | 0.479 | 0.211 | 0.351 | 0.343 | 13.7% | 34.7% | 23.9% |
| CU | Samuel Basallo | 21 | 0.211 | 0.421 | 0.211 | 0.274 | 0.277 | 7.7% | 16.0% | 30.0% |
| FF | Dylan Beavers | 43 | 0.237 | 0.421 | 0.184 | 0.334 | 0.385 | 13.3% | 19.4% | 12.3% |
| CH | Gunnar Henderson | 52 | 0.275 | 0.451 | 0.176 | 0.353 | 0.281 | 4.9% | 30.0% | 19.8% |
| SL | Gunnar Henderson | 57 | 0.192 | 0.365 | 0.173 | 0.308 | 0.238 | 8.6% | 28.4% | 30.5% |
| FF | Blaze Alexander | 57 | 0.265 | 0.429 | 0.163 | 0.345 | 0.368 | 14.7% | 20.8% | 28.9% |
| SL | Samuel Basallo | 36 | 0.281 | 0.438 | 0.156 | 0.333 | 0.320 | 4.0% | 27.5% | 34.8% |
| CH | Coby Mayo | 20 | 0.100 | 0.250 | 0.150 | 0.145 | 0.143 | 7.1% | 20.0% | 34.4% |
| FF | Gunnar Henderson | 84 | 0.113 | 0.254 | 0.141 | 0.248 | 0.301 | 10.2% | 21.4% | 17.2% |
| SL | Leody Taveras | 33 | 0.207 | 0.345 | 0.138 | 0.276 | 0.297 | 5.3% | 28.2% | 25.4% |
| FF | Coby Mayo | 57 | 0.217 | 0.348 | 0.130 | 0.331 | 0.374 | 6.5% | 23.9% | 12.0% |
| CU | Pete Alonso | 32 | 0.226 | 0.355 | 0.129 | 0.264 | 0.292 | 0.0% | 36.4% | 29.2% |
| FF | Taylor Ward | 109 | 0.291 | 0.419 | 0.128 | 0.390 | 0.418 | 8.2% | 22.2% | 16.9% |
| FF | Colton Cowser | 60 | 0.205 | 0.318 | 0.114 | 0.352 | 0.423 | 14.3% | 27.2% | 14.4% |
| FF | Tyler O'Neill | 41 | 0.162 | 0.270 | 0.108 | 0.235 | 0.294 | 3.2% | 28.3% | 16.5% |
| CU | Dylan Beavers | 10 | 0.100 | 0.200 | 0.100 | 0.125 | 0.078 | 0.0% | 20.0% | 26.3% |
| FF | Leody Taveras | 90 | 0.203 | 0.297 | 0.095 | 0.293 | 0.297 | 8.8% | 21.1% | 21.3% |
| SL | Blaze Alexander | 23 | 0.286 | 0.381 | 0.095 | 0.357 | 0.357 | 7.7% | 22.2% | 39.2% |


## Baltimore Orioles Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gunnar Henderson | 365 | 0.221 | 0.424 | 0.203 | 0.332 | 0.310 | 9.1% | 26.8% | 21.8% |
| Taylor Ward | 361 | 0.250 | 0.339 | 0.089 | 0.339 | 0.350 | 4.5% | 23.9% | 15.8% |
| Pete Alonso | 359 | 0.244 | 0.454 | 0.210 | 0.338 | 0.368 | 12.5% | 34.5% | 25.7% |
| Samuel Basallo | 251 | 0.264 | 0.480 | 0.216 | 0.353 | 0.337 | 12.9% | 27.9% | 26.7% |
| Leody Taveras | 250 | 0.249 | 0.369 | 0.120 | 0.317 | 0.298 | 5.5% | 19.7% | 24.8% |
| Adley Rutschman | 243 | 0.260 | 0.456 | 0.195 | 0.349 | 0.354 | 8.7% | 27.6% | 12.7% |
| Coby Mayo | 219 | 0.187 | 0.374 | 0.187 | 0.282 | 0.287 | 10.2% | 29.6% | 29.2% |
| Colton Cowser | 203 | 0.214 | 0.370 | 0.156 | 0.311 | 0.325 | 12.1% | 19.4% | 31.7% |
| Jeremiah Jackson | 198 | 0.272 | 0.450 | 0.178 | 0.335 | 0.293 | 8.4% | 28.7% | 23.7% |
| Blaze Alexander | 196 | 0.298 | 0.404 | 0.107 | 0.344 | 0.353 | 6.0% | 24.2% | 25.4% |
| Tyler O'Neill | 151 | 0.185 | 0.274 | 0.089 | 0.258 | 0.275 | 6.3% | 25.8% | 27.1% |
| Dylan Beavers | 123 | 0.234 | 0.355 | 0.121 | 0.309 | 0.308 | 5.0% | 22.1% | 20.1% |


## Los Angeles Dodgers Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Freddie Freeman | 345 | 0.273 | 0.471 | 0.199 | 0.363 | 0.378 | 11.5% | 25.2% | 18.8% |
| Andy Pages | 344 | 0.264 | 0.468 | 0.204 | 0.343 | 0.342 | 8.3% | 26.9% | 20.6% |
| Shohei Ohtani | 333 | 0.293 | 0.546 | 0.253 | 0.413 | 0.422 | 17.9% | 31.1% | 25.0% |
| Kyle Tucker | 332 | 0.238 | 0.385 | 0.147 | 0.330 | 0.323 | 5.9% | 24.4% | 22.2% |
| Max Muncy | 283 | 0.269 | 0.521 | 0.252 | 0.389 | 0.387 | 16.7% | 28.3% | 24.3% |
| Teoscar Hernández | 224 | 0.286 | 0.482 | 0.196 | 0.367 | 0.339 | 12.9% | 25.6% | 27.5% |
| Will Smith | 212 | 0.245 | 0.375 | 0.130 | 0.319 | 0.386 | 13.6% | 22.3% | 15.1% |
| Mookie Betts | 203 | 0.222 | 0.406 | 0.183 | 0.321 | 0.336 | 8.9% | 25.2% | 12.7% |
| Alex Freeland | 195 | 0.220 | 0.327 | 0.107 | 0.294 | 0.291 | 7.7% | 26.4% | 26.8% |
| Dalton Rushing | 170 | 0.253 | 0.493 | 0.240 | 0.375 | 0.345 | 10.0% | 28.7% | 31.5% |
| Hyeseong Kim | 148 | 0.265 | 0.326 | 0.061 | 0.308 | 0.304 | 3.1% | 14.3% | 23.3% |
| Miguel Rojas | 144 | 0.283 | 0.402 | 0.118 | 0.346 | 0.328 | 6.8% | 28.0% | 16.6% |


## Bullpen Fatigue Report

### Baltimore Orioles Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Andrew Kittredge | 2026-06-19 | 1.0 | 24 |
| Andrew Kittredge | 2026-06-20 | 0.1 | 10 |
| Grant Wolfram | 2026-06-20 | 0.1 | 3 |
| Rico Garcia | 2026-06-18 | 1.0 | 10 |
| Rico Garcia | 2026-06-20 | 0.2 | 11 |
| Ryan Helsley | 2026-06-17 | 1.0 | 9 |
| Ryan Helsley | 2026-06-19 | 0.2 | 23 |
| Tyler Wells | 2026-06-19 | 1.2 | 29 |
| Yennier Cano | 2026-06-17 | 0.1 | 9 |
| Yennier Cano | 2026-06-19 | 0.1 | 3 |
| Yennier Cano | 2026-06-20 | 0.2 | 15 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Andrew Kittredge, Grant Wolfram, Rico Garcia, Yennier Cano


### Los Angeles Dodgers Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alex Vesia | 2026-06-17 | 1.0 | 28 |
| Alex Vesia | 2026-06-20 | 1.0 | 20 |
| Blake Treinen | 2026-06-19 | 1.0 | 9 |
| Edgardo Henriquez | 2026-06-17 | 1.1 | 11 |
| Edgardo Henriquez | 2026-06-20 | 1.0 | 14 |
| Jack Dreyer | 2026-06-17 | 0.2 | 8 |
| Jack Dreyer | 2026-06-19 | 0.2 | 11 |
| Jonathan Hernández | 2026-06-20 | 1.0 | 14 |
| Kyle Hurt | 2026-06-19 | 1.0 | 9 |
| Will Klein | 2026-06-19 | 0.2 | 13 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Alex Vesia, Edgardo Henriquez, Jonathan Hernández



## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, FS, SL, SI, CU
- Home pitcher pitch mix to inspect: FF, SL, CH, CU
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 13. Boston Red Sox @ Seattle Mariners

## Game Context

| Field | Value |
| --- | --- |
| Park | T-Mobile Park |
| Time | 2026-06-21T20:10:00Z |
| Away Team | Boston Red Sox |
| Home Team | Seattle Mariners |
| Away Probable Pitcher | Payton Tolle |
| Home Probable Pitcher | Logan Gilbert |


## Away Starting Pitcher: Payton Tolle

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 930 |
| Batted/Result Events | 252 |
| Hits Allowed | 49 |
| Walks | 16 |
| Strikeouts | 65 |
| Home Runs | 5 |
| K Event Rate | 25.8% |
| BB Event Rate | 6.3% |
| HR Event Rate | 2.0% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs R | 3.4% | 32 | 0.143 | 0.571 | 0.429 | 0.286 | 0.384 | 16.7% | 30.0% | 26.7% |
| CU | vs L | 1.4% | 13 | 0.000 | 0.000 | 0.000 | 0.140 | 0.030 | 0.0% | 0.0% | 66.7% |
| CU | vs R | 7.3% | 68 | 0.240 | 0.440 | 0.200 | 0.304 | 0.234 | 6.2% | 37.5% | 41.5% |
| FC | vs L | 4.1% | 38 | 0.091 | 0.364 | 0.273 | 0.225 | 0.354 | 11.1% | 16.7% | 14.3% |
| FC | vs R | 12.2% | 113 | 0.292 | 0.458 | 0.167 | 0.321 | 0.168 | 0.0% | 25.5% | 26.0% |
| FF | vs L | 9.0% | 84 | 0.174 | 0.348 | 0.174 | 0.259 | 0.149 | 0.0% | 13.3% | 22.4% |
| FF | vs R | 39.6% | 368 | 0.146 | 0.183 | 0.037 | 0.207 | 0.199 | 4.0% | 9.0% | 23.0% |
| SI | vs L | 8.0% | 74 | 0.345 | 0.517 | 0.172 | 0.413 | 0.374 | 7.4% | 28.6% | 5.3% |
| SI | vs R | 14.9% | 139 | 0.308 | 0.385 | 0.077 | 0.378 | 0.413 | 9.1% | 30.0% | 15.6% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-16 | 90 | 4 | 2 | 6 | 2 |
| 2026-06-09 | 94 | 9 | 1 | 3 | 0 |
| 2026-06-03 | 99 | 7 | 2 | 5 | 0 |
| 2026-05-28 | 94 | 5 | 2 | 7 | 0 |
| 2026-05-22 | 85 | 4 | 2 | 9 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | J. P. Crawford | 9 | 0.375 | 1.125 | 0.750 | 0.622 | 0.430 | 40.0% | 41.7% | 23.5% |
| FC | Dominic Canzone | 13 | 0.400 | 1.000 | 0.600 | 0.604 | 0.491 | 22.2% | 20.0% | 19.2% |
| FC | Luke Raley | 28 | 0.333 | 0.875 | 0.542 | 0.559 | 0.427 | 16.7% | 32.3% | 25.5% |
| SI | Cal Raleigh | 13 | 0.500 | 1.000 | 0.500 | 0.592 | 0.617 | 44.4% | 31.6% | 14.8% |
| FF | Brendan Donovan | 41 | 0.323 | 0.774 | 0.452 | 0.498 | 0.326 | 8.0% | 31.1% | 15.0% |
| CU | Dominic Canzone | 18 | 0.312 | 0.750 | 0.438 | 0.469 | 0.401 | 27.3% | 50.0% | 28.0% |
| FF | Luke Raley | 73 | 0.290 | 0.710 | 0.419 | 0.462 | 0.456 | 25.6% | 35.1% | 34.3% |
| FF | Dominic Canzone | 60 | 0.291 | 0.636 | 0.345 | 0.413 | 0.450 | 20.0% | 40.0% | 15.9% |
| CU | Cole Young | 12 | 0.556 | 0.889 | 0.333 | 0.583 | 0.395 | 14.3% | 50.0% | 10.5% |
| CU | Luke Raley | 13 | 0.250 | 0.583 | 0.333 | 0.373 | 0.417 | 42.9% | 33.3% | 32.1% |
| CU | Randy Arozarena | 13 | 0.250 | 0.583 | 0.333 | 0.373 | 0.296 | 16.7% | 22.2% | 26.9% |
| FC | Leo Rivas | 11 | 0.300 | 0.600 | 0.300 | 0.405 | 0.189 | 0.0% | 0.0% | 21.4% |
| CU | Brendan Donovan | 10 | 0.429 | 0.714 | 0.286 | 0.550 | 0.494 | 20.0% | 33.3% | 25.0% |
| FC | Randy Arozarena | 22 | 0.350 | 0.600 | 0.250 | 0.432 | 0.397 | 5.3% | 30.0% | 17.3% |
| SI | Luke Raley | 24 | 0.227 | 0.455 | 0.227 | 0.300 | 0.340 | 17.6% | 24.2% | 26.1% |
| FC | Brendan Donovan | 14 | 0.667 | 0.889 | 0.222 | 0.636 | 0.564 | 10.0% | 33.3% | 0.0% |
| FF | Julio Rodríguez | 85 | 0.230 | 0.446 | 0.216 | 0.339 | 0.327 | 11.8% | 24.1% | 26.8% |
| FF | Josh Naylor | 94 | 0.318 | 0.518 | 0.200 | 0.394 | 0.349 | 5.1% | 20.7% | 7.7% |
| FF | J. P. Crawford | 90 | 0.231 | 0.431 | 0.200 | 0.397 | 0.424 | 9.6% | 15.9% | 14.0% |
| CU | Julio Rodríguez | 17 | 0.200 | 0.400 | 0.200 | 0.306 | 0.325 | 11.1% | 25.0% | 45.5% |
| SI | Mitch Garver | 28 | 0.227 | 0.409 | 0.182 | 0.395 | 0.384 | 5.9% | 40.0% | 11.1% |
| FC | Cal Raleigh | 21 | 0.118 | 0.294 | 0.176 | 0.271 | 0.330 | 9.1% | 25.0% | 32.4% |
| SI | Julio Rodríguez | 90 | 0.282 | 0.447 | 0.165 | 0.365 | 0.362 | 9.2% | 33.3% | 7.3% |
| FF | Cole Young | 120 | 0.226 | 0.387 | 0.160 | 0.309 | 0.320 | 7.8% | 24.0% | 15.6% |
| FF | Randy Arozarena | 98 | 0.241 | 0.392 | 0.152 | 0.349 | 0.393 | 16.7% | 27.4% | 29.7% |
| FF | Mitch Garver | 50 | 0.238 | 0.381 | 0.143 | 0.322 | 0.323 | 13.8% | 30.6% | 21.3% |
| FF | Cal Raleigh | 78 | 0.145 | 0.275 | 0.130 | 0.238 | 0.250 | 12.2% | 25.0% | 31.0% |
| FC | Josh Naylor | 36 | 0.303 | 0.424 | 0.121 | 0.368 | 0.369 | 7.7% | 22.2% | 12.5% |
| FF | Rob Refsnyder | 40 | 0.167 | 0.278 | 0.111 | 0.241 | 0.221 | 8.7% | 27.8% | 21.8% |
| SI | Dominic Canzone | 32 | 0.222 | 0.333 | 0.111 | 0.313 | 0.416 | 8.3% | 36.4% | 14.3% |


## Home Starting Pitcher: Logan Gilbert

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1399 |
| Batted/Result Events | 348 |
| Hits Allowed | 69 |
| Walks | 20 |
| Strikeouts | 92 |
| Home Runs | 13 |
| K Event Rate | 26.4% |
| BB Event Rate | 5.7% |
| HR Event Rate | 3.7% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 7.9% | 110 | 0.087 | 0.130 | 0.043 | 0.119 | 0.218 | 6.2% | 18.5% | 29.3% |
| CH | vs R | 0.6% | 8 | 0.333 | 0.333 | 0.000 | 0.300 | 0.304 | 0.0% | 0.0% | 50.0% |
| CU | vs L | 3.2% | 45 | 0.200 | 0.400 | 0.200 | 0.250 | 0.394 | 25.0% | 30.0% | 31.2% |
| CU | vs R | 5.9% | 83 | 0.227 | 0.318 | 0.091 | 0.277 | 0.299 | 5.6% | 13.8% | 34.1% |
| FC | vs L | 7.2% | 101 | 0.400 | 0.800 | 0.400 | 0.530 | 0.370 | 5.9% | 38.2% | 13.6% |
| FC | vs R | 2.1% | 30 | 0.273 | 0.273 | 0.000 | 0.245 | 0.311 | 0.0% | 33.3% | 6.2% |
| FF | vs L | 19.2% | 269 | 0.222 | 0.467 | 0.244 | 0.324 | 0.337 | 20.0% | 17.7% | 23.9% |
| FF | vs R | 15.3% | 214 | 0.283 | 0.609 | 0.326 | 0.386 | 0.431 | 23.3% | 28.6% | 12.0% |
| FS | vs L | 8.4% | 118 | 0.059 | 0.088 | 0.029 | 0.139 | 0.137 | 0.0% | 17.2% | 41.5% |
| FS | vs R | 6.2% | 87 | 0.250 | 0.375 | 0.125 | 0.317 | 0.281 | 6.7% | 27.3% | 35.1% |
| SI | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs R | 0.2% | 3 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SL | vs L | 12.7% | 178 | 0.239 | 0.478 | 0.239 | 0.342 | 0.375 | 9.7% | 35.3% | 37.4% |
| SL | vs R | 10.9% | 152 | 0.167 | 0.333 | 0.167 | 0.232 | 0.268 | 10.3% | 33.3% | 34.2% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-16 | 94 | 2 | 1 | 10 | 0 |
| 2026-06-09 | 105 | 3 | 2 | 5 | 0 |
| 2026-06-02 | 99 | 4 | 1 | 8 | 2 |
| 2026-05-27 | 91 | 5 | 2 | 6 | 0 |
| 2026-05-22 | 94 | 2 | 2 | 6 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FS | Willson Contreras | 4 | 0.333 | 1.333 | 1.000 | 0.675 | 0.245 | 0.0% | 50.0% | 38.5% |
| FS | Ceddanne Rafaela | 9 | 0.444 | 0.778 | 0.333 | 0.517 | 0.264 | 16.7% | 50.0% | 41.2% |
| CU | Carlos Narváez | 4 | 0.667 | 1.000 | 0.333 | 0.588 | 0.830 | 33.3% | 20.0% | 23.1% |
| CH | Ceddanne Rafaela | 32 | 0.333 | 0.633 | 0.300 | 0.455 | 0.239 | 13.6% | 24.3% | 31.7% |
| FC | Roman Anthony | 7 | 0.286 | 0.571 | 0.286 | 0.357 | 0.362 | 0.0% | 60.0% | 14.3% |
| FF | Jarren Duran | 91 | 0.205 | 0.487 | 0.282 | 0.347 | 0.353 | 16.0% | 20.2% | 33.0% |
| FS | Wilyer Abreu | 15 | 0.267 | 0.533 | 0.267 | 0.337 | 0.235 | 7.7% | 27.3% | 13.3% |
| SL | Ceddanne Rafaela | 43 | 0.300 | 0.550 | 0.250 | 0.414 | 0.261 | 2.9% | 25.4% | 27.3% |
| SL | Willson Contreras | 41 | 0.306 | 0.556 | 0.250 | 0.472 | 0.437 | 22.7% | 25.5% | 40.9% |
| CH | Andruw Monasterio | 12 | 0.250 | 0.500 | 0.250 | 0.317 | 0.346 | 11.1% | 22.7% | 30.6% |
| CH | Willson Contreras | 41 | 0.325 | 0.575 | 0.250 | 0.390 | 0.325 | 20.8% | 35.0% | 40.7% |
| CH | Masataka Yoshida | 24 | 0.333 | 0.571 | 0.238 | 0.425 | 0.410 | 5.9% | 29.6% | 12.5% |
| SL | Roman Anthony | 20 | 0.294 | 0.529 | 0.235 | 0.403 | 0.419 | 15.4% | 35.0% | 25.0% |
| FF | Wilyer Abreu | 96 | 0.229 | 0.446 | 0.217 | 0.341 | 0.302 | 12.1% | 20.1% | 20.4% |
| FF | Caleb Durbin | 79 | 0.275 | 0.493 | 0.217 | 0.376 | 0.318 | 5.4% | 26.9% | 7.5% |
| FF | Andruw Monasterio | 41 | 0.243 | 0.459 | 0.216 | 0.335 | 0.298 | 8.3% | 15.4% | 18.9% |
| SL | Wilyer Abreu | 46 | 0.273 | 0.477 | 0.205 | 0.336 | 0.326 | 15.6% | 27.3% | 32.9% |
| SL | Masataka Yoshida | 11 | 0.300 | 0.500 | 0.200 | 0.373 | 0.317 | 0.0% | 31.2% | 21.7% |
| FS | Carlos Narváez | 5 | 0.200 | 0.400 | 0.200 | 0.250 | 0.133 | 0.0% | 20.0% | 33.3% |
| FC | Wilyer Abreu | 32 | 0.333 | 0.533 | 0.200 | 0.392 | 0.430 | 15.4% | 28.6% | 5.8% |
| FC | Willson Contreras | 19 | 0.267 | 0.467 | 0.200 | 0.355 | 0.339 | 20.0% | 64.7% | 46.9% |
| CH | Jarren Duran | 41 | 0.184 | 0.368 | 0.184 | 0.250 | 0.277 | 13.8% | 27.9% | 37.0% |
| CU | Wilyer Abreu | 21 | 0.235 | 0.412 | 0.176 | 0.357 | 0.339 | 6.7% | 12.5% | 10.3% |
| CU | Ceddanne Rafaela | 17 | 0.235 | 0.412 | 0.176 | 0.326 | 0.178 | 0.0% | 11.1% | 32.5% |
| CU | Trevor Story | 18 | 0.118 | 0.294 | 0.176 | 0.250 | 0.255 | 25.0% | 18.8% | 41.4% |
| CU | Andruw Monasterio | 7 | 0.333 | 0.500 | 0.167 | 0.407 | 0.257 | 20.0% | 10.0% | 16.7% |
| SL | Isiah Kiner-Falefa | 23 | 0.476 | 0.619 | 0.143 | 0.500 | 0.454 | 5.6% | 20.7% | 23.4% |
| CH | Caleb Durbin | 24 | 0.143 | 0.286 | 0.143 | 0.215 | 0.278 | 6.2% | 25.0% | 37.8% |
| FC | Jarren Duran | 29 | 0.217 | 0.348 | 0.130 | 0.314 | 0.355 | 5.0% | 31.4% | 22.0% |
| FC | Caleb Durbin | 19 | 0.235 | 0.353 | 0.118 | 0.347 | 0.284 | 0.0% | 17.9% | 11.4% |


## Boston Red Sox Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wilyer Abreu | 330 | 0.268 | 0.430 | 0.161 | 0.330 | 0.337 | 11.5% | 24.4% | 20.4% |
| Jarren Duran | 327 | 0.208 | 0.372 | 0.164 | 0.288 | 0.295 | 12.1% | 27.1% | 32.7% |
| Willson Contreras | 316 | 0.281 | 0.519 | 0.237 | 0.393 | 0.376 | 13.2% | 28.5% | 28.9% |
| Ceddanne Rafaela | 298 | 0.296 | 0.467 | 0.172 | 0.368 | 0.294 | 6.2% | 22.6% | 23.1% |
| Caleb Durbin | 259 | 0.219 | 0.354 | 0.135 | 0.285 | 0.280 | 2.5% | 21.0% | 15.2% |
| Marcelo Mayer | 236 | 0.218 | 0.303 | 0.085 | 0.282 | 0.258 | 6.5% | 27.1% | 23.3% |
| Trevor Story | 194 | 0.225 | 0.335 | 0.110 | 0.286 | 0.248 | 4.0% | 22.1% | 27.8% |
| Masataka Yoshida | 183 | 0.245 | 0.337 | 0.092 | 0.303 | 0.307 | 1.4% | 27.7% | 14.1% |
| Carlos Narváez | 158 | 0.190 | 0.268 | 0.077 | 0.259 | 0.276 | 6.4% | 19.8% | 28.5% |
| Isiah Kiner-Falefa | 151 | 0.255 | 0.328 | 0.073 | 0.300 | 0.312 | 3.4% | 17.1% | 14.8% |
| Roman Anthony | 145 | 0.240 | 0.322 | 0.083 | 0.318 | 0.352 | 9.6% | 31.2% | 26.6% |
| Andruw Monasterio | 136 | 0.233 | 0.357 | 0.124 | 0.283 | 0.279 | 5.3% | 18.0% | 18.4% |


## Seattle Mariners Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Julio Rodríguez | 351 | 0.249 | 0.436 | 0.187 | 0.332 | 0.341 | 9.3% | 28.5% | 25.3% |
| Cole Young | 338 | 0.249 | 0.374 | 0.125 | 0.306 | 0.328 | 6.1% | 24.8% | 18.1% |
| Randy Arozarena | 326 | 0.288 | 0.456 | 0.167 | 0.374 | 0.353 | 8.1% | 24.7% | 24.4% |
| Josh Naylor | 323 | 0.253 | 0.367 | 0.114 | 0.307 | 0.321 | 4.7% | 26.3% | 17.0% |
| J. P. Crawford | 250 | 0.217 | 0.386 | 0.169 | 0.331 | 0.350 | 8.8% | 22.1% | 15.7% |
| Luke Raley | 233 | 0.252 | 0.529 | 0.276 | 0.370 | 0.357 | 17.4% | 29.4% | 39.2% |
| Cal Raleigh | 217 | 0.174 | 0.321 | 0.147 | 0.264 | 0.298 | 13.0% | 23.0% | 30.2% |
| Dominic Canzone | 211 | 0.287 | 0.564 | 0.277 | 0.389 | 0.383 | 15.3% | 31.3% | 25.5% |
| Leo Rivas | 140 | 0.132 | 0.167 | 0.035 | 0.231 | 0.239 | 2.6% | 9.7% | 23.9% |
| Rob Refsnyder | 129 | 0.126 | 0.216 | 0.090 | 0.203 | 0.257 | 7.8% | 23.3% | 24.1% |
| Brendan Donovan | 127 | 0.311 | 0.505 | 0.194 | 0.399 | 0.345 | 5.8% | 27.8% | 17.9% |
| Mitch Garver | 127 | 0.193 | 0.330 | 0.138 | 0.307 | 0.295 | 7.6% | 29.2% | 35.3% |


## Bullpen Fatigue Report

### Boston Red Sox Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Aroldis Chapman | 2026-06-18 | 1.0 | 20 |
| Danny Coulombe | 2026-06-17 | 1.0 | 20 |
| Danny Coulombe | 2026-06-20 | 1.0 | 5 |
| Garrett Whitlock | 2026-06-20 | 1.0 | 15 |
| Greg Weissert | 2026-06-17 | 1.0 | 20 |
| Greg Weissert | 2026-06-19 | 1.0 | 10 |
| Justin Slaten | 2026-06-18 | 1.0 | 15 |
| Justin Slaten | 2026-06-19 | 0.1 | 6 |
| Tommy Kahnle | 2026-06-19 | 1.0 | 19 |
| Tyron Guerrero | 2026-06-17 | 1.2 | 18 |
| Tyron Guerrero | 2026-06-20 | 1.0 | 14 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Danny Coulombe, Garrett Whitlock, Tyron Guerrero


### Seattle Mariners Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Alex Hoppe | 2026-06-17 | 1.0 | 18 |
| Alex Hoppe | 2026-06-20 | 1.0 | 14 |
| Andrés Muñoz | 2026-06-18 | 1.0 | 21 |
| Eduard Bazardo | 2026-06-18 | 1.0 | 11 |
| José A. Ferrer | 2026-06-20 | 0.2 | 18 |
| Luis Castillo | 2026-06-19 | 4.0 | 63 |
| Michael Rucker | 2026-06-17 | 1.0 | 27 |
| Michael Rucker | 2026-06-20 | 1.0 | 15 |
| Nick Davila | 2026-06-17 | 1.0 | 10 |
| Nick Davila | 2026-06-20 | 1.0 | 24 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Alex Hoppe, José A. Ferrer, Michael Rucker, Nick Davila



## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SI, FC, CU
- Home pitcher pitch mix to inspect: FF, SL, FS, FC, CU, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 14. New York Mets @ Philadelphia Phillies

## Game Context

| Field | Value |
| --- | --- |
| Park | Citizens Bank Park |
| Time | 2026-06-21T23:20:00Z |
| Away Team | New York Mets |
| Home Team | Philadelphia Phillies |
| Away Probable Pitcher | David Peterson |
| Home Probable Pitcher | Zack Wheeler |


## Away Starting Pitcher: David Peterson

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1205 |
| Batted/Result Events | 340 |
| Hits Allowed | 86 |
| Walks | 31 |
| Strikeouts | 64 |
| Home Runs | 5 |
| K Event Rate | 18.8% |
| BB Event Rate | 9.1% |
| HR Event Rate | 1.5% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 0.7% | 9 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 50.0% |
| CH | vs R | 11.1% | 134 | 0.333 | 0.455 | 0.121 | 0.414 | 0.309 | 3.6% | 14.9% | 20.6% |
| CU | vs L | 3.3% | 40 | 0.231 | 0.385 | 0.154 | 0.357 | 0.257 | 0.0% | 41.7% | 38.1% |
| CU | vs R | 9.4% | 113 | 0.304 | 0.435 | 0.130 | 0.368 | 0.263 | 0.0% | 28.0% | 29.3% |
| FF | vs L | 2.7% | 32 | 0.143 | 0.429 | 0.286 | 0.333 | 0.247 | 0.0% | 11.1% | 35.7% |
| FF | vs R | 19.3% | 232 | 0.386 | 0.545 | 0.159 | 0.429 | 0.342 | 5.4% | 15.0% | 16.3% |
| SI | vs L | 12.8% | 154 | 0.316 | 0.526 | 0.211 | 0.417 | 0.386 | 11.8% | 37.0% | 16.9% |
| SI | vs R | 16.9% | 204 | 0.269 | 0.327 | 0.058 | 0.391 | 0.525 | 6.2% | 39.7% | 6.9% |
| SL | vs L | 12.0% | 145 | 0.227 | 0.318 | 0.091 | 0.258 | 0.218 | 3.2% | 28.6% | 31.6% |
| SL | vs R | 11.6% | 140 | 0.234 | 0.298 | 0.064 | 0.233 | 0.257 | 9.4% | 37.5% | 25.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 54 | 2 | 2 | 1 | 1 |
| 2026-06-10 | 64 | 7 | 2 | 1 | 2 |
| 2026-05-31 | 51 | 1 | 1 | 3 | 0 |
| 2026-05-26 | 90 | 11 | 3 | 4 | 0 |
| 2026-05-21 | 82 | 4 | 3 | 3 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SI | Otto Kemp | 6 | 0.333 | 1.333 | 1.000 | 0.667 | 0.102 | 40.0% | 21.4% | 5.9% |
| CU | Brandon Marsh | 18 | 0.438 | 0.938 | 0.500 | 0.589 | 0.392 | 8.3% | 25.0% | 22.7% |
| SI | Kyle Schwarber | 55 | 0.395 | 0.860 | 0.465 | 0.564 | 0.545 | 22.2% | 36.2% | 15.9% |
| CH | Kyle Schwarber | 37 | 0.229 | 0.657 | 0.429 | 0.381 | 0.372 | 33.3% | 41.2% | 40.3% |
| FF | Bryce Harper | 82 | 0.292 | 0.708 | 0.415 | 0.465 | 0.467 | 13.0% | 27.9% | 18.3% |
| FF | Kyle Schwarber | 97 | 0.247 | 0.617 | 0.370 | 0.413 | 0.354 | 18.8% | 35.1% | 21.2% |
| SI | Brandon Marsh | 47 | 0.357 | 0.643 | 0.286 | 0.473 | 0.460 | 10.3% | 32.2% | 6.0% |
| SL | Bryson Stott | 31 | 0.357 | 0.643 | 0.286 | 0.452 | 0.319 | 4.8% | 34.2% | 21.4% |
| SL | J. T. Realmuto | 23 | 0.238 | 0.524 | 0.286 | 0.430 | 0.360 | 12.5% | 44.0% | 34.1% |
| SL | Bryce Harper | 49 | 0.222 | 0.500 | 0.278 | 0.378 | 0.518 | 32.1% | 37.3% | 46.2% |
| FF | Edmundo Sosa | 38 | 0.394 | 0.667 | 0.273 | 0.449 | 0.428 | 12.9% | 26.0% | 14.9% |
| CH | Edmundo Sosa | 20 | 0.263 | 0.526 | 0.263 | 0.395 | 0.291 | 8.3% | 27.6% | 32.1% |
| SL | Adolis García | 48 | 0.217 | 0.478 | 0.261 | 0.307 | 0.243 | 7.1% | 26.1% | 36.5% |
| CU | Kyle Schwarber | 26 | 0.130 | 0.391 | 0.261 | 0.269 | 0.314 | 25.0% | 32.0% | 45.8% |
| CU | Adolis García | 13 | 0.250 | 0.500 | 0.250 | 0.346 | 0.374 | 25.0% | 41.7% | 50.0% |
| SL | Brandon Marsh | 37 | 0.216 | 0.459 | 0.243 | 0.281 | 0.216 | 13.6% | 24.4% | 31.0% |
| CH | Alec Bohm | 22 | 0.286 | 0.524 | 0.238 | 0.359 | 0.320 | 5.3% | 20.0% | 12.5% |
| CH | Bryson Stott | 35 | 0.242 | 0.455 | 0.212 | 0.319 | 0.376 | 10.7% | 22.4% | 18.8% |
| SL | Edmundo Sosa | 24 | 0.208 | 0.417 | 0.208 | 0.263 | 0.331 | 17.6% | 25.0% | 36.4% |
| SI | Bryson Stott | 42 | 0.275 | 0.475 | 0.200 | 0.337 | 0.338 | 8.1% | 25.9% | 12.1% |
| SI | Trea Turner | 71 | 0.224 | 0.403 | 0.179 | 0.294 | 0.328 | 7.9% | 39.4% | 8.3% |
| FF | Rafael Marchán | 38 | 0.111 | 0.278 | 0.167 | 0.189 | 0.198 | 5.9% | 15.0% | 8.7% |
| FF | Brandon Marsh | 91 | 0.398 | 0.554 | 0.157 | 0.442 | 0.378 | 9.0% | 24.8% | 16.2% |
| SL | Kyle Schwarber | 49 | 0.217 | 0.370 | 0.152 | 0.297 | 0.353 | 20.8% | 33.9% | 36.0% |
| FF | Alec Bohm | 93 | 0.195 | 0.341 | 0.146 | 0.296 | 0.259 | 3.1% | 20.0% | 12.4% |
| SI | Adolis García | 62 | 0.160 | 0.300 | 0.140 | 0.281 | 0.328 | 10.3% | 35.5% | 14.5% |
| FF | Trea Turner | 101 | 0.291 | 0.430 | 0.140 | 0.379 | 0.352 | 7.5% | 30.2% | 18.1% |
| CU | Justin Crawford | 17 | 0.188 | 0.312 | 0.125 | 0.241 | 0.243 | 0.0% | 35.0% | 22.2% |
| SI | Bryce Harper | 48 | 0.317 | 0.439 | 0.122 | 0.369 | 0.347 | 2.7% | 24.7% | 13.7% |
| SL | Alec Bohm | 36 | 0.235 | 0.353 | 0.118 | 0.285 | 0.311 | 3.4% | 33.3% | 26.6% |


## Home Starting Pitcher: Zack Wheeler

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 947 |
| Batted/Result Events | 236 |
| Hits Allowed | 38 |
| Walks | 15 |
| Strikeouts | 62 |
| Home Runs | 7 |
| K Event Rate | 26.3% |
| BB Event Rate | 6.4% |
| HR Event Rate | 3.0% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 7.5% | 71 | 0.200 | 0.200 | 0.000 | 0.228 | 0.277 | 14.3% | 56.2% | 31.2% |
| CU | vs R | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| FC | vs L | 11.2% | 106 | 0.190 | 0.429 | 0.238 | 0.313 | 0.312 | 5.9% | 22.0% | 15.7% |
| FF | vs L | 26.2% | 248 | 0.132 | 0.321 | 0.189 | 0.240 | 0.239 | 8.1% | 20.4% | 18.7% |
| FF | vs R | 12.0% | 114 | 0.050 | 0.200 | 0.150 | 0.155 | 0.221 | 9.1% | 17.1% | 28.6% |
| FS | vs L | 11.4% | 108 | 0.261 | 0.435 | 0.174 | 0.298 | 0.311 | 5.3% | 18.2% | 39.0% |
| FS | vs R | 1.9% | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.123 | 0.0% | 25.0% | 50.0% |
| SI | vs L | 3.4% | 32 | 0.000 | 0.000 | 0.000 | 0.078 | 0.182 | 0.0% | 0.0% | 6.2% |
| SI | vs R | 13.2% | 125 | 0.293 | 0.488 | 0.195 | 0.342 | 0.342 | 11.1% | 29.6% | 4.5% |
| ST | vs L | 3.6% | 34 | 0.286 | 0.429 | 0.143 | 0.356 | 0.633 | 14.3% | 62.5% | 9.1% |
| ST | vs R | 9.5% | 90 | 0.176 | 0.235 | 0.059 | 0.208 | 0.196 | 0.0% | 5.9% | 33.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-15 | 97 | 2 | 3 | 9 | 0 |
| 2026-06-09 | 96 | 6 | 0 | 5 | 1 |
| 2026-06-04 | 104 | 2 | 3 | 8 | 1 |
| 2026-05-29 | 90 | 5 | 1 | 4 | 4 |
| 2026-05-23 | 99 | 2 | 1 | 6 | 0 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC | A. J. Ewing | 5 | 0.667 | 2.000 | 1.333 | 0.930 | 0.490 | 0.0% | 9.1% | 0.0% |
| FS | Francisco Álvarez | 4 | 0.250 | 1.000 | 0.750 | 0.675 | 0.712 | 50.0% | 50.0% | 25.0% |
| ST | Mj Melendez | 10 | 0.222 | 0.667 | 0.444 | 0.395 | 0.326 | 20.0% | 38.5% | 18.8% |
| FF | Juan Soto | 72 | 0.308 | 0.677 | 0.369 | 0.440 | 0.488 | 21.8% | 33.3% | 13.4% |
| FS | Carson Benge | 11 | 0.273 | 0.636 | 0.364 | 0.377 | 0.375 | 11.1% | 31.2% | 20.0% |
| FS | Francisco Lindor | 6 | 0.167 | 0.500 | 0.333 | 0.267 | 0.161 | 0.0% | 16.7% | 36.4% |
| FC | Juan Soto | 12 | 0.333 | 0.667 | 0.333 | 0.433 | 0.253 | 0.0% | 20.0% | 22.7% |
| ST | Juan Soto | 27 | 0.320 | 0.640 | 0.320 | 0.426 | 0.466 | 21.1% | 33.3% | 27.8% |
| SI | Marcus Semien | 75 | 0.288 | 0.561 | 0.273 | 0.373 | 0.398 | 10.7% | 28.7% | 12.0% |
| FF | Mj Melendez | 55 | 0.196 | 0.435 | 0.239 | 0.325 | 0.246 | 7.4% | 24.6% | 31.3% |
| FC | Mark Vientos | 14 | 0.385 | 0.615 | 0.231 | 0.450 | 0.391 | 8.3% | 25.0% | 33.3% |
| FC | Carson Benge | 28 | 0.296 | 0.519 | 0.222 | 0.393 | 0.523 | 14.8% | 34.2% | 2.5% |
| FC | Bo Bichette | 15 | 0.143 | 0.357 | 0.214 | 0.300 | 0.434 | 16.7% | 22.6% | 17.9% |
| SI | Mark Vientos | 40 | 0.205 | 0.410 | 0.205 | 0.270 | 0.320 | 7.9% | 31.1% | 11.0% |
| FC | Marcus Semien | 17 | 0.333 | 0.533 | 0.200 | 0.371 | 0.387 | 13.3% | 17.1% | 22.4% |
| FF | Tyrone Taylor | 29 | 0.231 | 0.423 | 0.192 | 0.269 | 0.176 | 0.0% | 10.9% | 13.0% |
| SI | Luis Torrens | 29 | 0.231 | 0.423 | 0.192 | 0.321 | 0.360 | 4.2% | 25.5% | 8.8% |
| FF | A. J. Ewing | 41 | 0.250 | 0.438 | 0.188 | 0.387 | 0.420 | 12.0% | 20.3% | 9.3% |
| SI | A. J. Ewing | 25 | 0.227 | 0.409 | 0.182 | 0.300 | 0.265 | 0.0% | 31.0% | 23.3% |
| FF | Marcus Semien | 86 | 0.213 | 0.387 | 0.173 | 0.296 | 0.362 | 14.5% | 30.6% | 15.7% |
| FF | Bo Bichette | 87 | 0.234 | 0.403 | 0.169 | 0.321 | 0.345 | 5.3% | 26.9% | 11.0% |
| FS | Mj Melendez | 7 | 0.333 | 0.500 | 0.167 | 0.407 | 0.362 | 20.0% | 66.7% | 25.0% |
| FF | Francisco Lindor | 46 | 0.179 | 0.333 | 0.154 | 0.311 | 0.395 | 8.8% | 27.4% | 13.3% |
| FF | Carson Benge | 106 | 0.298 | 0.447 | 0.149 | 0.373 | 0.380 | 8.7% | 21.9% | 18.3% |
| SI | Juan Soto | 55 | 0.298 | 0.447 | 0.149 | 0.390 | 0.397 | 14.3% | 38.2% | 13.8% |
| ST | Carson Benge | 21 | 0.238 | 0.381 | 0.143 | 0.267 | 0.261 | 10.0% | 25.9% | 31.8% |
| FF | Mark Vientos | 55 | 0.240 | 0.360 | 0.120 | 0.304 | 0.326 | 10.3% | 25.0% | 24.0% |
| FF | Francisco Álvarez | 39 | 0.294 | 0.412 | 0.118 | 0.358 | 0.400 | 20.0% | 26.1% | 26.4% |
| FS | Marcus Semien | 10 | 0.222 | 0.333 | 0.111 | 0.465 | 0.253 | 0.0% | 9.1% | 18.8% |
| ST | Bo Bichette | 28 | 0.222 | 0.333 | 0.111 | 0.257 | 0.329 | 10.5% | 19.0% | 29.2% |


## New York Mets Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bo Bichette | 350 | 0.265 | 0.399 | 0.134 | 0.317 | 0.333 | 6.7% | 27.3% | 15.5% |
| Marcus Semien | 322 | 0.225 | 0.367 | 0.142 | 0.294 | 0.323 | 9.3% | 22.4% | 20.7% |
| Carson Benge | 306 | 0.261 | 0.396 | 0.136 | 0.334 | 0.349 | 9.0% | 24.7% | 19.5% |
| Brett Baty | 267 | 0.223 | 0.311 | 0.088 | 0.287 | 0.291 | 8.5% | 22.0% | 26.6% |
| Juan Soto | 262 | 0.293 | 0.560 | 0.267 | 0.402 | 0.422 | 14.9% | 34.2% | 18.1% |
| Mark Vientos | 238 | 0.213 | 0.387 | 0.173 | 0.277 | 0.313 | 10.4% | 28.4% | 29.2% |
| Francisco Álvarez | 173 | 0.258 | 0.400 | 0.142 | 0.332 | 0.343 | 14.5% | 29.3% | 26.7% |
| Luis Torrens | 145 | 0.224 | 0.313 | 0.090 | 0.262 | 0.274 | 3.9% | 23.7% | 21.0% |
| A. J. Ewing | 138 | 0.256 | 0.372 | 0.116 | 0.322 | 0.328 | 4.8% | 19.6% | 22.5% |
| Mj Melendez | 133 | 0.189 | 0.360 | 0.171 | 0.300 | 0.272 | 10.6% | 28.6% | 31.4% |
| Francisco Lindor | 125 | 0.214 | 0.321 | 0.107 | 0.302 | 0.340 | 7.9% | 25.0% | 22.7% |
| Tyrone Taylor | 118 | 0.183 | 0.312 | 0.128 | 0.239 | 0.248 | 5.5% | 22.5% | 21.2% |


## Philadelphia Phillies Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Trea Turner | 345 | 0.218 | 0.324 | 0.106 | 0.275 | 0.280 | 4.9% | 27.1% | 25.5% |
| Kyle Schwarber | 340 | 0.252 | 0.593 | 0.341 | 0.404 | 0.387 | 21.4% | 34.9% | 30.9% |
| Bryce Harper | 324 | 0.258 | 0.502 | 0.244 | 0.378 | 0.404 | 12.6% | 29.1% | 28.2% |
| Alec Bohm | 310 | 0.228 | 0.361 | 0.133 | 0.301 | 0.294 | 4.1% | 26.1% | 14.3% |
| Brandon Marsh | 293 | 0.310 | 0.474 | 0.164 | 0.360 | 0.325 | 7.9% | 24.6% | 22.5% |
| Bryson Stott | 284 | 0.245 | 0.406 | 0.161 | 0.310 | 0.312 | 6.8% | 26.8% | 15.3% |
| Adolis García | 278 | 0.207 | 0.358 | 0.150 | 0.290 | 0.294 | 9.9% | 28.4% | 30.8% |
| Justin Crawford | 247 | 0.245 | 0.341 | 0.096 | 0.294 | 0.268 | 1.1% | 18.8% | 16.3% |
| J. T. Realmuto | 207 | 0.213 | 0.333 | 0.120 | 0.299 | 0.324 | 4.9% | 26.9% | 22.4% |
| Edmundo Sosa | 139 | 0.237 | 0.382 | 0.145 | 0.305 | 0.329 | 7.8% | 25.5% | 23.3% |
| Rafael Marchán | 89 | 0.095 | 0.167 | 0.071 | 0.175 | 0.193 | 3.1% | 16.1% | 17.3% |
| Otto Kemp | 48 | 0.156 | 0.311 | 0.156 | 0.228 | 0.205 | 6.9% | 12.3% | 30.9% |


## Bullpen Fatigue Report

### New York Mets Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| A.J. Minter | 2026-06-18 | 0.2 | 8 |
| Austin Warren | 2026-06-17 | 1.0 | 17 |
| Brooks Raley | 2026-06-17 | 1.0 | 14 |
| Cionel Pérez | 2026-06-20 | 2.0 | 32 |
| Devin Williams | 2026-06-18 | 1.0 | 25 |
| Huascar Brazobán | 2026-06-18 | 1.0 | 20 |
| Luke Weaver | 2026-06-18 | 1.0 | 14 |
| Tobias Myers | 2026-06-20 | 2.1 | 41 |
| Zack Short | 2026-06-20 | 1.0 | 10 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Cionel Pérez, Tobias Myers, Zack Short


### Philadelphia Phillies Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Bryse Wilson | 2026-06-18 | 2.0 | 29 |
| Chase Shugart | 2026-06-17 | 0.2 | 10 |
| Garrett Stubbs | 2026-06-17 | 0.1 | 3 |
| Jhoan Duran | 2026-06-20 | 1.0 | 17 |
| Jonathan Bowlan | 2026-06-17 | 1.0 | 11 |
| José Alvarado | 2026-06-18 | 1.0 | 30 |
| Max Lazar | 2026-06-17 | 1.0 | 11 |
| Max Lazar | 2026-06-20 | 2.0 | 26 |
| Orion Kerkering | 2026-06-17 | 1.0 | 26 |
| Seth Johnson | 2026-06-18 | 1.0 | 17 |
| Tanner Banks | 2026-06-17 | 1.0 | 14 |
| Tim Mayza | 2026-06-17 | 2.0 | 31 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Jhoan Duran, Max Lazar



## Final Game Dissection

- Away pitcher pitch mix to inspect: SI, SL, FF, CU, CH
- Home pitcher pitch mix to inspect: FF, SI, FS, ST, FC
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.


---

# 15. Toronto Blue Jays @ Chicago Cubs

## Game Context

| Field | Value |
| --- | --- |
| Park | Wrigley Field |
| Time | 2026-06-21T18:20:00Z |
| Away Team | Toronto Blue Jays |
| Home Team | Chicago Cubs |
| Away Probable Pitcher | Dylan Cease |
| Home Probable Pitcher | Shota Imanaga |


## Away Starting Pitcher: Dylan Cease

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1365 |
| Batted/Result Events | 324 |
| Hits Allowed | 59 |
| Walks | 33 |
| Strikeouts | 116 |
| Home Runs | 5 |
| K Event Rate | 35.8% |
| BB Event Rate | 10.2% |
| HR Event Rate | 1.5% |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 10.9% | 149 | 0.190 | 0.238 | 0.048 | 0.188 | 0.225 | 9.1% | 11.8% | 62.5% |
| CH | vs R | 0.6% | 8 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| FF | vs L | 21.0% | 286 | 0.284 | 0.448 | 0.164 | 0.365 | 0.337 | 4.2% | 22.2% | 16.7% |
| FF | vs R | 13.3% | 181 | 0.233 | 0.349 | 0.116 | 0.336 | 0.251 | 14.3% | 26.8% | 39.1% |
| KC | vs L | 7.4% | 101 | 0.273 | 0.273 | 0.000 | 0.245 | 0.269 | 14.3% | 14.3% | 38.5% |
| KC | vs R | 1.9% | 26 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs L | 3.9% | 53 | 0.000 | 0.000 | 0.000 | 0.184 | 0.257 | 0.0% | 9.1% | 16.7% |
| SI | vs R | 6.3% | 86 | 0.158 | 0.158 | 0.000 | 0.170 | 0.342 | 5.6% | 25.7% | 16.3% |
| SL | vs L | 13.4% | 183 | 0.125 | 0.225 | 0.100 | 0.236 | 0.284 | 5.6% | 25.5% | 45.3% |
| SL | vs R | 16.0% | 219 | 0.172 | 0.207 | 0.034 | 0.215 | 0.220 | 0.0% | 16.7% | 42.7% |
| ST | vs L | 0.9% | 12 | 0.333 | 0.667 | 0.333 | 0.417 | 0.205 | 0.0% | 20.0% | 16.7% |
| ST | vs R | 4.4% | 60 | 0.364 | 0.364 | 0.000 | 0.327 | 0.213 | 0.0% | 23.1% | 26.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-06-16 | 108 | 4 | 4 | 7 | 0 |
| 2026-06-09 | 93 | 3 | 1 | 11 | 0 |
| 2026-05-24 | 77 | 4 | 1 | 8 | 2 |
| 2026-05-19 | 100 | 4 | 4 | 9 | 2 |
| 2026-05-13 | 99 | 3 | 3 | 9 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL | Michael Conforto | 9 | 0.375 | 1.000 | 0.625 | 0.578 | 0.385 | 33.3% | 31.2% | 23.8% |
| SI | Michael Conforto | 21 | 0.647 | 1.176 | 0.529 | 0.726 | 0.618 | 20.0% | 61.9% | 12.5% |
| SL | Pete Crow-Armstrong | 44 | 0.378 | 0.811 | 0.432 | 0.515 | 0.475 | 24.1% | 30.0% | 32.1% |
| FF | Matt Shaw | 47 | 0.310 | 0.667 | 0.357 | 0.472 | 0.335 | 13.8% | 24.6% | 19.1% |
| SL | Ian Happ | 37 | 0.273 | 0.576 | 0.303 | 0.393 | 0.352 | 22.7% | 25.0% | 34.5% |
| FF | Moisés Ballesteros | 53 | 0.156 | 0.444 | 0.289 | 0.301 | 0.295 | 23.1% | 32.1% | 35.2% |
| FF | Miguel Amaya | 45 | 0.333 | 0.619 | 0.286 | 0.459 | 0.318 | 18.2% | 26.6% | 12.7% |
| FF | Ian Happ | 112 | 0.221 | 0.505 | 0.284 | 0.378 | 0.325 | 15.8% | 25.6% | 24.9% |
| CH | Carson Kelly | 13 | 0.250 | 0.500 | 0.250 | 0.346 | 0.291 | 11.1% | 38.9% | 36.4% |
| SI | Miguel Amaya | 23 | 0.375 | 0.625 | 0.250 | 0.511 | 0.485 | 6.7% | 33.3% | 13.2% |
| FF | Seiya Suzuki | 69 | 0.276 | 0.517 | 0.241 | 0.396 | 0.337 | 14.3% | 28.4% | 17.9% |
| SL | Michael Busch | 44 | 0.342 | 0.579 | 0.237 | 0.419 | 0.265 | 9.1% | 18.2% | 41.0% |
| FF | Dansby Swanson | 93 | 0.253 | 0.480 | 0.227 | 0.390 | 0.354 | 5.6% | 30.6% | 23.7% |
| SL | Matt Shaw | 24 | 0.318 | 0.545 | 0.227 | 0.433 | 0.390 | 5.9% | 23.1% | 22.6% |
| FF | Michael Conforto | 41 | 0.222 | 0.444 | 0.222 | 0.330 | 0.313 | 8.7% | 28.6% | 14.8% |
| SL | Miguel Amaya | 35 | 0.222 | 0.444 | 0.222 | 0.389 | 0.349 | 9.5% | 14.7% | 31.5% |
| SI | Seiya Suzuki | 56 | 0.380 | 0.600 | 0.220 | 0.468 | 0.456 | 10.0% | 32.9% | 13.3% |
| SI | Dansby Swanson | 56 | 0.271 | 0.479 | 0.208 | 0.405 | 0.382 | 10.5% | 31.9% | 21.0% |
| SI | Michael Busch | 69 | 0.260 | 0.460 | 0.200 | 0.428 | 0.486 | 19.0% | 32.3% | 16.7% |
| SI | Pete Crow-Armstrong | 48 | 0.463 | 0.659 | 0.195 | 0.518 | 0.457 | 8.3% | 37.3% | 13.9% |
| CH | Pete Crow-Armstrong | 42 | 0.216 | 0.405 | 0.189 | 0.298 | 0.335 | 3.7% | 37.3% | 30.6% |
| SL | Seiya Suzuki | 50 | 0.182 | 0.364 | 0.182 | 0.304 | 0.328 | 6.5% | 24.2% | 29.3% |
| SL | Carson Kelly | 46 | 0.250 | 0.425 | 0.175 | 0.362 | 0.298 | 3.2% | 22.0% | 32.9% |
| FF | Pete Crow-Armstrong | 108 | 0.200 | 0.368 | 0.168 | 0.296 | 0.306 | 9.2% | 32.1% | 18.6% |
| FF | Michael Busch | 119 | 0.219 | 0.381 | 0.162 | 0.331 | 0.339 | 12.9% | 25.2% | 11.9% |
| SI | Moisés Ballesteros | 28 | 0.346 | 0.500 | 0.154 | 0.389 | 0.311 | 13.6% | 27.9% | 11.3% |
| SL | Moisés Ballesteros | 24 | 0.150 | 0.300 | 0.150 | 0.275 | 0.261 | 0.0% | 21.9% | 24.5% |
| FF | Alex Bregman | 91 | 0.296 | 0.444 | 0.148 | 0.362 | 0.336 | 5.6% | 30.8% | 7.9% |
| SL | Nico Hoerner | 47 | 0.295 | 0.432 | 0.136 | 0.339 | 0.311 | 2.4% | 17.2% | 19.3% |
| SI | Ian Happ | 36 | 0.267 | 0.400 | 0.133 | 0.357 | 0.356 | 8.7% | 31.9% | 7.5% |


## Home Starting Pitcher: Shota Imanaga

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


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| CU | vs R | 3.1% | 46 | 0.000 | 0.000 | 0.000 | 0.140 | 0.420 | 25.0% | 22.2% | 10.0% |
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


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FS | Kazuma Okamoto | 4 | 0.333 | 1.333 | 1.000 | 0.675 | 0.622 | 100.0% | 14.3% | 36.4% |
| FS | Brandon Valenzuela | 9 | 0.111 | 0.444 | 0.333 | 0.222 | 0.309 | 16.7% | 25.0% | 50.0% |
| FS | Yohendrick Pinango | 10 | 0.556 | 0.889 | 0.333 | 0.720 | 0.271 | 0.0% | 38.5% | 13.3% |
| FF | Kazuma Okamoto | 105 | 0.315 | 0.620 | 0.304 | 0.432 | 0.420 | 21.9% | 39.6% | 26.5% |
| FF | Daulton Varsho | 86 | 0.224 | 0.513 | 0.289 | 0.352 | 0.330 | 20.4% | 25.6% | 18.5% |
| FF | George Springer | 74 | 0.279 | 0.557 | 0.279 | 0.413 | 0.359 | 11.8% | 22.9% | 18.8% |
| ST | Andrés Giménez | 20 | 0.263 | 0.526 | 0.263 | 0.350 | 0.271 | 7.1% | 7.1% | 28.6% |
| FF | Ernie Clement | 76 | 0.301 | 0.521 | 0.219 | 0.375 | 0.258 | 0.0% | 14.8% | 9.2% |
| FF | Andrés Giménez | 77 | 0.239 | 0.437 | 0.197 | 0.319 | 0.233 | 3.7% | 9.4% | 20.1% |
| FS | Daulton Varsho | 13 | 0.333 | 0.500 | 0.167 | 0.385 | 0.387 | 11.1% | 46.2% | 34.8% |
| ST | Myles Straw | 6 | 0.167 | 0.333 | 0.167 | 0.208 | 0.091 | 0.0% | 11.1% | 10.0% |
| FF | Jesús Sánchez | 74 | 0.313 | 0.463 | 0.149 | 0.342 | 0.329 | 8.0% | 23.6% | 21.4% |
| FF | Vladimir Guerrero | 57 | 0.327 | 0.469 | 0.143 | 0.382 | 0.395 | 9.5% | 28.1% | 16.1% |
| ST | George Springer | 33 | 0.143 | 0.286 | 0.143 | 0.286 | 0.243 | 10.0% | 15.4% | 25.9% |
| ST | Nathan Lukes | 7 | 0.143 | 0.286 | 0.143 | 0.179 | 0.190 | 0.0% | 16.7% | 20.0% |
| FS | Jesús Sánchez | 15 | 0.267 | 0.400 | 0.133 | 0.347 | 0.258 | 0.0% | 24.0% | 18.4% |
| ST | Kazuma Okamoto | 35 | 0.156 | 0.281 | 0.125 | 0.230 | 0.213 | 6.7% | 13.8% | 37.9% |
| FF | Myles Straw | 49 | 0.317 | 0.439 | 0.122 | 0.365 | 0.405 | 7.9% | 21.9% | 9.5% |
| FF | Brandon Valenzuela | 58 | 0.220 | 0.320 | 0.100 | 0.278 | 0.336 | 5.1% | 19.8% | 17.4% |
| FS | Vladimir Guerrero | 12 | 0.091 | 0.182 | 0.091 | 0.163 | 0.285 | 0.0% | 46.7% | 17.4% |
| FS | Nathan Lukes | 11 | 0.455 | 0.545 | 0.091 | 0.441 | 0.198 | 0.0% | 6.7% | 10.5% |
| FF | Davis Schneider | 49 | 0.103 | 0.179 | 0.077 | 0.238 | 0.265 | 9.5% | 23.4% | 32.1% |
| ST | Ernie Clement | 28 | 0.222 | 0.296 | 0.074 | 0.243 | 0.225 | 0.0% | 11.1% | 31.5% |
| ST | Vladimir Guerrero | 31 | 0.250 | 0.321 | 0.071 | 0.271 | 0.358 | 21.7% | 42.4% | 18.2% |
| FF | Yohendrick Pinango | 43 | 0.324 | 0.351 | 0.027 | 0.357 | 0.388 | 6.1% | 19.8% | 13.3% |
| FF | Nathan Lukes | 52 | 0.333 | 0.356 | 0.022 | 0.368 | 0.309 | 0.0% | 13.6% | 15.5% |
| FS | George Springer | 9 | 0.250 | 0.250 | 0.000 | 0.356 | 0.355 | 0.0% | 26.7% | 22.7% |
| FS | Andrés Giménez | 11 | 0.273 | 0.273 | 0.000 | 0.245 | 0.266 | 0.0% | 18.2% | 42.9% |
| FS | Ernie Clement | 7 | 0.429 | 0.429 | 0.000 | 0.386 | 0.347 | 0.0% | 8.3% | 7.1% |
| ST | Davis Schneider | 11 | 0.100 | 0.100 | 0.000 | 0.145 | 0.185 | 0.0% | 10.0% | 26.7% |


## Toronto Blue Jays Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kazuma Okamoto | 319 | 0.231 | 0.441 | 0.210 | 0.332 | 0.329 | 14.8% | 29.8% | 32.7% |
| Vladimir Guerrero | 318 | 0.287 | 0.389 | 0.102 | 0.339 | 0.349 | 7.3% | 30.7% | 16.7% |
| Ernie Clement | 312 | 0.286 | 0.429 | 0.143 | 0.323 | 0.267 | 2.6% | 17.4% | 14.9% |
| Andrés Giménez | 271 | 0.240 | 0.392 | 0.152 | 0.294 | 0.261 | 4.5% | 13.2% | 22.6% |
| George Springer | 262 | 0.243 | 0.443 | 0.200 | 0.354 | 0.317 | 9.8% | 22.5% | 21.0% |
| Daulton Varsho | 260 | 0.253 | 0.421 | 0.167 | 0.343 | 0.307 | 7.7% | 23.8% | 17.2% |
| Jesús Sánchez | 240 | 0.290 | 0.466 | 0.176 | 0.345 | 0.338 | 11.0% | 27.3% | 23.1% |
| Nathan Lukes | 162 | 0.318 | 0.412 | 0.095 | 0.355 | 0.301 | 0.8% | 15.7% | 15.6% |
| Brandon Valenzuela | 160 | 0.262 | 0.454 | 0.191 | 0.345 | 0.345 | 8.7% | 23.2% | 24.0% |
| Myles Straw | 146 | 0.238 | 0.323 | 0.085 | 0.288 | 0.309 | 3.6% | 17.2% | 12.4% |
| Yohendrick Pinango | 138 | 0.289 | 0.445 | 0.156 | 0.351 | 0.319 | 8.2% | 27.0% | 21.1% |
| Davis Schneider | 123 | 0.167 | 0.304 | 0.137 | 0.275 | 0.287 | 11.1% | 27.8% | 26.4% |


## Chicago Cubs Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nico Hoerner | 359 | 0.249 | 0.350 | 0.101 | 0.314 | 0.327 | 1.7% | 19.0% | 10.2% |
| Alex Bregman | 358 | 0.260 | 0.392 | 0.132 | 0.342 | 0.319 | 5.9% | 27.6% | 16.4% |
| Michael Busch | 355 | 0.243 | 0.397 | 0.154 | 0.353 | 0.353 | 11.5% | 26.4% | 24.0% |
| Ian Happ | 340 | 0.229 | 0.472 | 0.243 | 0.365 | 0.327 | 14.1% | 25.8% | 29.1% |
| Pete Crow-Armstrong | 337 | 0.279 | 0.508 | 0.229 | 0.373 | 0.367 | 11.1% | 31.9% | 25.1% |
| Dansby Swanson | 301 | 0.181 | 0.317 | 0.135 | 0.290 | 0.286 | 5.9% | 24.1% | 28.9% |
| Seiya Suzuki | 260 | 0.269 | 0.445 | 0.176 | 0.367 | 0.340 | 8.7% | 26.2% | 24.3% |
| Carson Kelly | 215 | 0.296 | 0.423 | 0.127 | 0.363 | 0.327 | 7.8% | 25.3% | 20.4% |
| Moisés Ballesteros | 193 | 0.246 | 0.439 | 0.193 | 0.335 | 0.310 | 11.3% | 28.2% | 23.3% |
| Matt Shaw | 153 | 0.261 | 0.457 | 0.196 | 0.358 | 0.294 | 5.5% | 23.0% | 18.7% |
| Miguel Amaya | 143 | 0.240 | 0.430 | 0.190 | 0.369 | 0.313 | 9.7% | 21.4% | 22.6% |
| Michael Conforto | 134 | 0.248 | 0.479 | 0.231 | 0.350 | 0.345 | 12.5% | 32.3% | 26.7% |


## Bullpen Fatigue Report

### Toronto Blue Jays Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Braydon Fisher | 2026-06-19 | 1.0 | 20 |
| Brendon Little | 2026-06-19 | 1.0 | 34 |
| Jeff Hoffman | 2026-06-17 | 1.0 | 25 |
| Jeff Hoffman | 2026-06-20 | 1.0 | 22 |
| Lazaro Estrada | 2026-06-20 | 2.1 | 32 |
| Louis Varland | 2026-06-17 | 1.0 | 10 |
| Louis Varland | 2026-06-20 | 2.0 | 28 |
| Mason Fluharty | 2026-06-17 | 0.1 | 11 |
| Mason Fluharty | 2026-06-18 | 1.0 | 5 |
| Mason Fluharty | 2026-06-20 | 0.0 | 11 |
| Myles Straw | 2026-06-19 | 1.1 | 20 |
| Simeon Woods Richardson | 2026-06-17 | 3.0 | 55 |
| Spencer Miles | 2026-06-17 | 1.1 | 22 |
| Spencer Miles | 2026-06-19 | 0.2 | 20 |
| Tommy Nance | 2026-06-18 | 0.2 | 14 |
| Tommy Nance | 2026-06-19 | 1.1 | 19 |
| Tyler Rogers | 2026-06-17 | 1.0 | 11 |
| Tyler Rogers | 2026-06-19 | 0.2 | 28 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Jeff Hoffman, Lazaro Estrada, Louis Varland, Mason Fluharty


### Chicago Cubs Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Caleb Thielbar | 2026-06-17 | 0.2 | 16 |
| Caleb Thielbar | 2026-06-20 | 0.1 | 13 |
| Ethan Roberts | 2026-06-17 | 0.1 | 15 |
| Ethan Roberts | 2026-06-19 | 1.0 | 10 |
| Ethan Roberts | 2026-06-20 | 1.1 | 14 |
| Gavin Hollowell | 2026-06-19 | 1.0 | 13 |
| Hoby Milner | 2026-06-17 | 1.1 | 25 |
| Hoby Milner | 2026-06-19 | 1.0 | 16 |
| Jacob Webb | 2026-06-17 | 1.0 | 16 |
| Jacob Webb | 2026-06-20 | 0.2 | 27 |
| Ryan Rolison | 2026-06-20 | 0.2 | 1 |
| Trent Thornton | 2026-06-20 | 0.2 | 13 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** Caleb Thielbar, Ethan Roberts, Jacob Webb, Ryan Rolison, Trent Thornton



## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, SL, CH, SI, KC
- Home pitcher pitch mix to inspect: FF, FS, ST
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.

