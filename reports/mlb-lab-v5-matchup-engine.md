# MLB-LAB V5.1 Pitch Matchup Engine

Date: 2026-07-16

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
| 1 | New York Mets @ Philadelphia Phillies | Citizens Bank Park | Christian Scott | Aaron Nola |

---

# Full Game Breakdown Cards

---

# 1. New York Mets @ Philadelphia Phillies

## Game Context

| Field | Value |
| --- | --- |
| Park | Citizens Bank Park |
| Time | 2026-07-16T22:10:00Z |
| Away Team | New York Mets |
| Home Team | Philadelphia Phillies |
| Away Probable Pitcher | Christian Scott |
| Home Probable Pitcher | Aaron Nola |


## Away Starting Pitcher: Christian Scott

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1000 |
| Batted/Result Events | 233 |
| Hits Allowed | 44 |
| Walks | 26 |
| Strikeouts | 65 |
| Home Runs | 7 |
| K Event Rate | 27.9% |
| BB Event Rate | 11.2% |
| HR Event Rate | 3.0% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | NYM | 6.3 | 3 | 0 | 1 | 5 | 0 |
| 2026-07-03 | ATL | 6.0 | 2 | 2 | 4 | 7 | 2 |
| 2026-06-27 | NYM | 6.0 | 3 | 1 | 2 | 6 | 1 |
| 2026-06-11 | NYM | 7.3 | 7 | 3 | 1 | 6 | 3 |
| 2026-06-05 | SD | 7.0 | 3 | 0 | 2 | 3 | 0 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CU | vs L | 3.4% | 34 | 0.214 | 0.286 | 0.071 | 0.218 | 0.210 | 0.0% | 17.6% | 16.0% |
| CU | vs R | 0.6% | 6 | 1.000 | 2.000 | 1.000 | 1.250 | 0.039 | 0.0% | 0.0% | 0.0% |
| FC | vs L | 13.9% | 139 | 0.129 | 0.194 | 0.065 | 0.188 | 0.281 | 4.0% | 21.1% | 16.0% |
| FC | vs R | 3.6% | 36 | 0.000 | 0.000 | 0.000 | 0.117 | 0.403 | 25.0% | 9.1% | 21.4% |
| FF | vs L | 31.1% | 311 | 0.207 | 0.500 | 0.293 | 0.348 | 0.351 | 13.2% | 15.2% | 28.6% |
| FF | vs R | 18.9% | 189 | 0.257 | 0.343 | 0.086 | 0.366 | 0.381 | 8.7% | 21.7% | 18.1% |
| FS | vs L | 3.3% | 33 | 0.500 | 0.500 | 0.000 | 0.450 | 0.651 | 16.7% | 62.5% | 16.7% |
| FS | vs R | 0.2% | 2 | 0.000 | 0.000 | 0.000 | 0.350 | 0.682 | 0.0% | 0.0% | 0.0% |
| SI | vs L | 0.6% | 6 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SI | vs R | 1.5% | 15 | 0.333 | 0.333 | 0.000 | 0.400 | 0.409 | 0.0% | 75.0% | 16.7% |
| SL | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 100.0% |
| ST | vs L | 9.1% | 91 | 0.227 | 0.364 | 0.136 | 0.274 | 0.156 | 0.0% | 26.9% | 33.3% |
| ST | vs R | 13.6% | 136 | 0.231 | 0.346 | 0.115 | 0.310 | 0.335 | 6.2% | 12.5% | 31.3% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-07-08 | 90 | 3 | 1 | 5 | 0 |
| 2026-07-03 | 82 | 2 | 4 | 7 | 2 |
| 2026-06-27 | 82 | 3 | 2 | 6 | 1 |
| 2026-06-11 | 88 | 7 | 1 | 6 | 3 |
| 2026-06-05 | 98 | 3 | 2 | 3 | 0 |


## Home Hitters vs Away SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST | Gabriel Rincones | 5 | 0.200 | 0.800 | 0.600 | 0.400 | 0.346 | 20.0% | 42.9% | 30.0% |
| FC | Gabriel Rincones | 5 | 0.200 | 0.800 | 0.600 | 0.400 | 0.353 | 20.0% | 33.3% | 0.0% |
| FC | Kyle Schwarber | 29 | 0.333 | 0.778 | 0.444 | 0.479 | 0.439 | 15.0% | 33.3% | 27.3% |
| ST | Bryce Harper | 33 | 0.344 | 0.781 | 0.438 | 0.455 | 0.413 | 20.8% | 25.5% | 33.3% |
| FC | Bryson Stott | 21 | 0.429 | 0.857 | 0.429 | 0.538 | 0.344 | 11.8% | 39.4% | 17.1% |
| FF | Bryce Harper | 104 | 0.293 | 0.695 | 0.402 | 0.465 | 0.469 | 14.3% | 26.5% | 22.8% |
| FF | Kyle Schwarber | 116 | 0.268 | 0.639 | 0.371 | 0.429 | 0.380 | 19.0% | 37.6% | 23.2% |
| FF | Edmundo Sosa | 45 | 0.395 | 0.737 | 0.342 | 0.482 | 0.479 | 17.1% | 28.6% | 13.9% |
| FC | J. T. Realmuto | 18 | 0.214 | 0.500 | 0.286 | 0.347 | 0.326 | 8.3% | 43.8% | 24.0% |
| ST | Bryson Stott | 22 | 0.143 | 0.381 | 0.238 | 0.236 | 0.250 | 12.5% | 16.0% | 24.3% |
| ST | Justin Crawford | 23 | 0.318 | 0.545 | 0.227 | 0.383 | 0.243 | 0.0% | 12.0% | 23.8% |
| FC | Alec Bohm | 37 | 0.306 | 0.500 | 0.194 | 0.355 | 0.290 | 3.1% | 25.9% | 12.5% |
| FC | Bryce Harper | 31 | 0.269 | 0.462 | 0.192 | 0.403 | 0.370 | 8.7% | 40.5% | 21.8% |
| FF | Trea Turner | 119 | 0.314 | 0.480 | 0.167 | 0.401 | 0.351 | 9.2% | 28.1% | 19.9% |
| FF | Rafael Marchán | 41 | 0.105 | 0.263 | 0.158 | 0.193 | 0.224 | 5.6% | 15.5% | 10.8% |
| FF | Brandon Marsh | 112 | 0.382 | 0.539 | 0.157 | 0.429 | 0.359 | 9.0% | 22.8% | 17.2% |
| FF | Alec Bohm | 118 | 0.186 | 0.333 | 0.147 | 0.295 | 0.274 | 3.7% | 19.2% | 11.0% |
| ST | Kyle Schwarber | 39 | 0.062 | 0.188 | 0.125 | 0.227 | 0.248 | 16.7% | 31.4% | 52.4% |
| ST | Brandon Marsh | 34 | 0.219 | 0.344 | 0.125 | 0.249 | 0.235 | 11.1% | 27.0% | 37.7% |
| FC | Brandon Marsh | 24 | 0.292 | 0.417 | 0.125 | 0.306 | 0.256 | 5.6% | 17.9% | 24.6% |
| FF | J. T. Realmuto | 94 | 0.207 | 0.329 | 0.122 | 0.300 | 0.316 | 4.7% | 20.5% | 16.5% |
| ST | Adolis García | 30 | 0.148 | 0.259 | 0.111 | 0.227 | 0.233 | 6.7% | 18.9% | 32.1% |
| FF | Justin Crawford | 91 | 0.286 | 0.381 | 0.095 | 0.331 | 0.280 | 3.2% | 17.1% | 17.4% |
| ST | J. T. Realmuto | 24 | 0.217 | 0.304 | 0.087 | 0.246 | 0.203 | 0.0% | 16.0% | 22.2% |
| FF | Bryson Stott | 122 | 0.208 | 0.292 | 0.085 | 0.270 | 0.322 | 8.3% | 24.9% | 16.9% |
| ST | Trea Turner | 38 | 0.167 | 0.250 | 0.083 | 0.208 | 0.167 | 0.0% | 5.1% | 41.0% |
| FF | Adolis García | 73 | 0.219 | 0.281 | 0.062 | 0.291 | 0.307 | 7.7% | 24.2% | 29.3% |
| FC | Trea Turner | 33 | 0.250 | 0.312 | 0.062 | 0.288 | 0.266 | 8.7% | 16.7% | 27.7% |
| FF | Gabriel Rincones | 22 | 0.150 | 0.200 | 0.050 | 0.202 | 0.191 | 9.1% | 15.4% | 24.1% |
| FC | Justin Crawford | 22 | 0.200 | 0.250 | 0.050 | 0.243 | 0.263 | 0.0% | 23.5% | 20.0% |


## Home Starting Pitcher: Aaron Nola

### Pitcher Profile

| Stat | Value |
| --- | --- |
| Sample Pitches | 1780 |
| Batted/Result Events | 446 |
| Hits Allowed | 114 |
| Walks | 34 |
| Strikeouts | 106 |
| Home Runs | 21 |
| K Event Rate | 23.8% |
| BB Event Rate | 7.6% |
| HR Event Rate | 4.7% |


#### Last 5 Starts

| Date | Opponent | IP | H | ER | BB | K | HR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-10 | DET | 6.7 | 3 | 1 | 2 | 8 | 1 |
| 2026-07-05 | KC | 9.3 | 7 | 0 | 0 | 7 | 0 |
| 2026-06-29 | PHI | 7.7 | 8 | 2 | 2 | 5 | 2 |
| 2026-06-24 | WSH | 7.0 | 3 | 2 | 3 | 5 | 2 |
| 2026-06-18 | PHI | 8.0 | 7 | 2 | 1 | 6 | 2 |


### Full Pitch Arsenal vs L/R

| Pitch | Side | Usage | Pitches | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH | vs L | 11.7% | 208 | 0.154 | 0.179 | 0.026 | 0.190 | 0.291 | 5.4% | 20.9% | 24.0% |
| CH | vs R | 2.0% | 36 | 0.286 | 0.714 | 0.429 | 0.450 | 0.133 | 20.0% | 30.0% | 28.6% |
| FC | vs L | 3.8% | 68 | 0.333 | 0.611 | 0.278 | 0.416 | 0.318 | 8.3% | 41.7% | 23.7% |
| FC | vs R | 4.0% | 71 | 0.444 | 0.611 | 0.167 | 0.471 | 0.384 | 0.0% | 27.6% | 21.1% |
| FF | vs L | 16.9% | 300 | 0.415 | 0.774 | 0.358 | 0.530 | 0.452 | 15.6% | 25.5% | 11.5% |
| FF | vs R | 6.9% | 123 | 0.333 | 0.667 | 0.333 | 0.421 | 0.345 | 16.7% | 27.3% | 16.3% |
| KC | vs L | 20.8% | 370 | 0.198 | 0.358 | 0.160 | 0.280 | 0.232 | 6.2% | 19.8% | 38.1% |
| KC | vs R | 12.9% | 229 | 0.203 | 0.348 | 0.145 | 0.248 | 0.221 | 8.9% | 15.9% | 39.0% |
| SI | vs L | 8.7% | 154 | 0.359 | 0.667 | 0.308 | 0.479 | 0.437 | 12.5% | 38.8% | 7.0% |
| SI | vs R | 11.2% | 200 | 0.333 | 0.625 | 0.292 | 0.412 | 0.351 | 12.8% | 27.0% | 11.7% |
| SL | vs L | 0.1% | 1 | 0.000 | 0.000 | 0.000 | — | — | 0.0% | 0.0% | 0.0% |
| SL | vs R | 1.1% | 19 | 0.167 | 0.167 | 0.000 | 0.229 | 0.239 | 0.0% | 44.4% | 30.8% |


### Last 5 Starts / Appearances

| Date | Pitches | Hits | BB | K | HR |
| --- | --- | --- | --- | --- | --- |
| 2026-07-10 | 84 | 3 | 2 | 8 | 1 |
| 2026-07-05 | 98 | 7 | 0 | 7 | 0 |
| 2026-06-29 | 86 | 8 | 2 | 5 | 2 |
| 2026-06-24 | 86 | 3 | 2 | 5 | 2 |
| 2026-06-18 | 97 | 7 | 1 | 6 | 2 |


## Away Hitters vs Home SP Pitch Mix

| Pitch | Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KC | Brett Baty | 6 | 0.400 | 1.000 | 0.600 | 0.600 | 0.586 | 25.0% | 66.7% | 33.3% |
| CH | Jared Young | 16 | 0.214 | 0.643 | 0.429 | 0.406 | 0.503 | 21.4% | 39.3% | 20.0% |
| FF | Juan Soto | 89 | 0.304 | 0.658 | 0.354 | 0.436 | 0.500 | 22.7% | 35.2% | 17.6% |
| SI | Francisco Lindor | 23 | 0.143 | 0.429 | 0.286 | 0.274 | 0.338 | 16.7% | 30.8% | 15.6% |
| SI | Marcus Semien | 76 | 0.279 | 0.544 | 0.265 | 0.368 | 0.395 | 10.5% | 29.2% | 11.7% |
| KC | Jared Young | 4 | 0.500 | 0.750 | 0.250 | 0.762 | 0.301 | 0.0% | 25.0% | 50.0% |
| FF | A. J. Ewing | 64 | 0.208 | 0.453 | 0.245 | 0.352 | 0.404 | 14.6% | 24.5% | 13.0% |
| CH | Mark Vientos | 41 | 0.263 | 0.500 | 0.237 | 0.333 | 0.296 | 6.9% | 30.4% | 30.3% |
| FF | Mj Melendez | 58 | 0.184 | 0.408 | 0.224 | 0.309 | 0.243 | 6.9% | 24.0% | 32.6% |
| SI | A. J. Ewing | 42 | 0.316 | 0.526 | 0.211 | 0.380 | 0.328 | 7.1% | 32.2% | 16.7% |
| CH | Francisco Álvarez | 21 | 0.263 | 0.474 | 0.211 | 0.350 | 0.319 | 14.3% | 27.3% | 32.4% |
| SI | Juan Soto | 72 | 0.290 | 0.500 | 0.210 | 0.410 | 0.426 | 16.4% | 34.9% | 13.0% |
| FF | Francisco Lindor | 66 | 0.169 | 0.373 | 0.203 | 0.277 | 0.376 | 7.5% | 33.3% | 15.3% |
| FF | Mark Vientos | 64 | 0.237 | 0.441 | 0.203 | 0.323 | 0.338 | 13.0% | 25.3% | 24.5% |
| FF | Francisco Álvarez | 56 | 0.294 | 0.490 | 0.196 | 0.369 | 0.378 | 23.3% | 28.8% | 27.4% |
| SI | Mark Vientos | 47 | 0.182 | 0.364 | 0.182 | 0.260 | 0.310 | 7.3% | 27.9% | 12.0% |
| FF | Marcus Semien | 88 | 0.195 | 0.364 | 0.169 | 0.279 | 0.353 | 14.5% | 28.8% | 17.9% |
| FF | Carson Benge | 131 | 0.304 | 0.470 | 0.165 | 0.385 | 0.377 | 8.3% | 20.5% | 16.6% |
| CH | Carson Benge | 35 | 0.235 | 0.382 | 0.147 | 0.301 | 0.337 | 6.9% | 26.7% | 22.2% |
| SI | Francisco Álvarez | 65 | 0.286 | 0.429 | 0.143 | 0.388 | 0.378 | 11.4% | 29.5% | 17.2% |
| SI | Luis Torrens | 40 | 0.250 | 0.389 | 0.139 | 0.318 | 0.323 | 3.0% | 23.3% | 8.3% |
| FF | Jared Young | 50 | 0.273 | 0.409 | 0.136 | 0.343 | 0.368 | 16.7% | 24.7% | 16.8% |
| FF | Brett Baty | 125 | 0.241 | 0.375 | 0.134 | 0.319 | 0.320 | 14.3% | 25.1% | 20.7% |
| CH | Juan Soto | 31 | 0.333 | 0.467 | 0.133 | 0.360 | 0.404 | 6.9% | 35.4% | 3.7% |
| FF | Bo Bichette | 103 | 0.228 | 0.359 | 0.130 | 0.300 | 0.329 | 4.5% | 26.0% | 11.4% |
| CH | Luis Torrens | 18 | 0.176 | 0.294 | 0.118 | 0.200 | 0.163 | 0.0% | 18.8% | 16.0% |
| CH | Marcus Semien | 21 | 0.333 | 0.444 | 0.111 | 0.390 | 0.440 | 15.4% | 16.7% | 31.7% |
| CH | Francisco Lindor | 28 | 0.214 | 0.321 | 0.107 | 0.295 | 0.329 | 12.5% | 26.1% | 20.6% |
| CH | Brett Baty | 41 | 0.189 | 0.270 | 0.081 | 0.248 | 0.310 | 3.3% | 20.9% | 35.6% |
| SI | Mj Melendez | 16 | 0.231 | 0.308 | 0.077 | 0.322 | 0.415 | 28.6% | 58.3% | 25.0% |


## New York Mets Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bo Bichette | 424 | 0.262 | 0.383 | 0.121 | 0.308 | 0.330 | 6.9% | 26.4% | 16.5% |
| Carson Benge | 396 | 0.262 | 0.398 | 0.135 | 0.332 | 0.349 | 7.7% | 24.1% | 19.4% |
| Juan Soto | 343 | 0.284 | 0.547 | 0.263 | 0.404 | 0.431 | 15.1% | 32.6% | 17.8% |
| Brett Baty | 338 | 0.221 | 0.314 | 0.094 | 0.285 | 0.307 | 10.0% | 22.9% | 26.6% |
| Marcus Semien | 330 | 0.211 | 0.338 | 0.127 | 0.278 | 0.316 | 8.7% | 21.4% | 21.4% |
| Mark Vientos | 265 | 0.206 | 0.389 | 0.182 | 0.281 | 0.310 | 10.2% | 27.5% | 30.0% |
| Francisco Álvarez | 236 | 0.251 | 0.409 | 0.158 | 0.331 | 0.333 | 15.0% | 28.9% | 29.5% |
| A. J. Ewing | 222 | 0.274 | 0.437 | 0.162 | 0.352 | 0.341 | 7.7% | 22.0% | 22.4% |
| Francisco Lindor | 184 | 0.206 | 0.352 | 0.145 | 0.295 | 0.342 | 8.0% | 30.1% | 21.4% |
| Luis Torrens | 181 | 0.218 | 0.315 | 0.097 | 0.267 | 0.271 | 4.0% | 21.7% | 20.9% |
| Jared Young | 165 | 0.235 | 0.403 | 0.168 | 0.326 | 0.325 | 12.2% | 28.0% | 22.5% |
| Mj Melendez | 145 | 0.190 | 0.347 | 0.157 | 0.298 | 0.281 | 11.1% | 28.4% | 30.8% |


## Philadelphia Phillies Team Hitter Pool

| Hitter | PA | AVG | SLG | ISO | wOBA | xwOBA | Barrel% | HardHit% | Whiff% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Trea Turner | 428 | 0.234 | 0.352 | 0.118 | 0.294 | 0.290 | 6.2% | 27.7% | 25.9% |
| Kyle Schwarber | 425 | 0.252 | 0.560 | 0.307 | 0.396 | 0.378 | 19.7% | 34.9% | 31.4% |
| Bryce Harper | 416 | 0.260 | 0.494 | 0.234 | 0.374 | 0.391 | 11.4% | 27.3% | 28.4% |
| Alec Bohm | 389 | 0.215 | 0.351 | 0.136 | 0.297 | 0.299 | 5.1% | 25.7% | 15.2% |
| Brandon Marsh | 374 | 0.304 | 0.490 | 0.186 | 0.362 | 0.322 | 9.8% | 24.4% | 23.8% |
| Bryson Stott | 365 | 0.255 | 0.405 | 0.150 | 0.316 | 0.320 | 7.0% | 26.1% | 16.1% |
| Justin Crawford | 298 | 0.264 | 0.357 | 0.094 | 0.309 | 0.280 | 0.9% | 19.4% | 16.5% |
| Adolis García | 271 | 0.195 | 0.336 | 0.141 | 0.275 | 0.294 | 9.6% | 27.6% | 30.8% |
| J. T. Realmuto | 268 | 0.207 | 0.342 | 0.135 | 0.293 | 0.313 | 5.0% | 25.9% | 22.1% |
| Edmundo Sosa | 172 | 0.214 | 0.358 | 0.145 | 0.293 | 0.340 | 7.9% | 26.1% | 22.8% |
| Rafael Marchán | 100 | 0.096 | 0.160 | 0.064 | 0.172 | 0.212 | 2.6% | 14.2% | 16.5% |
| Gabriel Rincones | 71 | 0.179 | 0.313 | 0.134 | 0.240 | 0.208 | 8.7% | 23.8% | 29.0% |


## Bullpen Fatigue Report

### New York Mets Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Brooks Raley | 2026-07-12 | 1.0 | 7 |
| Devin Williams | 2026-07-12 | 1.0 | 22 |
| Luke Weaver | 2026-07-12 | 1.0 | 13 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** No relievers flagged for heavy recent use


### Philadelphia Phillies Bullpen — Last 4 Days

| Reliever | Date | IP | Pitches |
| --- | --- | --- | --- |
| Jonathan Bowlan | 2026-07-12 | 1.0 | 15 |
| José Alvarado | 2026-07-12 | 1.0 | 13 |
| Orion Kerkering | 2026-07-12 | 1.0 | 15 |


**Caution arms (pitched yesterday, or 3+ appearances in window):** No relievers flagged for heavy recent use



## Projected Lineups

### Away Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bo Bichette | 424 | 0.262 | 0.383 | 0.121 | 0.308 | 6.9% | 26.4% |
| 2 | Carson Benge | 396 | 0.262 | 0.398 | 0.135 | 0.332 | 7.7% | 24.1% |
| 3 | Juan Soto | 343 | 0.284 | 0.547 | 0.263 | 0.404 | 15.1% | 32.6% |
| 4 | Brett Baty | 338 | 0.221 | 0.314 | 0.094 | 0.285 | 10.0% | 22.9% |
| 5 | Marcus Semien | 330 | 0.211 | 0.338 | 0.127 | 0.278 | 8.7% | 21.4% |
| 6 | Mark Vientos | 265 | 0.206 | 0.389 | 0.182 | 0.281 | 10.2% | 27.5% |
| 7 | Francisco Álvarez | 236 | 0.251 | 0.409 | 0.158 | 0.331 | 15.0% | 28.9% |
| 8 | A. J. Ewing | 222 | 0.274 | 0.437 | 0.162 | 0.352 | 7.7% | 22.0% |
| 9 | Francisco Lindor | 184 | 0.206 | 0.352 | 0.145 | 0.295 | 8.0% | 30.1% |


### Home Projected Lineup

| Order | Hitter | PA | AVG | SLG | ISO | wOBA | Barrel% | HardHit% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Trea Turner | 428 | 0.234 | 0.352 | 0.118 | 0.294 | 6.2% | 27.7% |
| 2 | Kyle Schwarber | 425 | 0.252 | 0.560 | 0.307 | 0.396 | 19.7% | 34.9% |
| 3 | Bryce Harper | 416 | 0.260 | 0.494 | 0.234 | 0.374 | 11.4% | 27.3% |
| 4 | Alec Bohm | 389 | 0.215 | 0.351 | 0.136 | 0.297 | 5.1% | 25.7% |
| 5 | Brandon Marsh | 374 | 0.304 | 0.490 | 0.186 | 0.362 | 9.8% | 24.4% |
| 6 | Bryson Stott | 365 | 0.255 | 0.405 | 0.150 | 0.316 | 7.0% | 26.1% |
| 7 | Justin Crawford | 298 | 0.264 | 0.357 | 0.094 | 0.309 | 0.9% | 19.4% |
| 8 | Adolis García | 271 | 0.195 | 0.336 | 0.141 | 0.275 | 9.6% | 27.6% |
| 9 | J. T. Realmuto | 268 | 0.207 | 0.342 | 0.135 | 0.293 | 5.0% | 25.9% |


## Bullpen / Staff Context

### Away Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7752 |
| Hits Allowed | 1618 |
| Walks/HBP | 754 |
| Strikeouts | 1771 |
| Home Runs Allowed | 224 |
| K Event Rate | 22.8% |
| BB/HBP Event Rate | 9.7% |
| HR Event Rate | 2.9% |


### Home Staff

| Metric | Value |
| --- | --- |
| Recent Staff BF | 7767 |
| Hits Allowed | 1711 |
| Walks/HBP | 680 |
| Strikeouts | 1905 |
| Home Runs Allowed | 250 |
| K Event Rate | 24.5% |
| BB/HBP Event Rate | 8.8% |
| HR Event Rate | 3.2% |


## Final Game Dissection

- Away pitcher pitch mix to inspect: FF, ST, FC
- Home pitcher pitch mix to inspect: KC, FF, SI, CH
- Home hitters should be checked against away SP pitch mix above.
- Away hitters should be checked against home SP pitch mix above.
- Lineup advantage: compare wOBA, xwOBA, ISO, Barrel%, HardHit%, Whiff%.
- Handedness advantage: use pitcher arsenal vs L/R tables.
- Bullpen fatigue: see Bullpen Fatigue Report above.
- Final MLB-LAB read: decide from pitch mix, hitter pool, L/R damage, current form, and bullpen fatigue.

