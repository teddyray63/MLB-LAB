# MLB-LAB V2 Daily Dissection Report

Date: 2026-06-21

Status: Automated full-slate game dissection.

Purpose: show every game the way a research dashboard would, without building a website.

Framework: six-gate betting signal hierarchy converted into game-by-game intelligence sections.

---

## Slate Index

| Rank | Game | Park | Away SP | Home SP | Env | Pitcher | Arsenal | Matchup | Savant | Total | Tier |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Pittsburgh Pirates @ Colorado Rockies | Coors Field | Jared Jones | Michael Lorenzen | 20 | 25 | 8 | 16 | 6 | 75 | Priority |
| 2 | New York Mets @ Philadelphia Phillies | Citizens Bank Park | David Peterson | Zack Wheeler | 15 | 22 | 8 | 16 | 6 | 67 | Watch |
| 3 | Cincinnati Reds @ New York Yankees | Yankee Stadium | Chase Burns | Elmer Rodríguez | 15 | 21 | 8 | 16 | 6 | 66 | Watch |
| 4 | Los Angeles Angels @ Athletics | Sutter Health Park | Reid Detmers | Jack Perkins | 16 | 20 | 8 | 16 | 6 | 66 | Watch |
| 5 | Milwaukee Brewers @ Atlanta Braves | Truist Park | Robert Gasser | Bryce Elder | 14 | 23 | 8 | 12 | 6 | 63 | Watch |
| 6 | San Francisco Giants @ Miami Marlins | loanDepot park | Logan Webb | Ryan Gusto | 10 | 25 | 8 | 12 | 6 | 61 | Watch |
| 7 | Cleveland Guardians @ Houston Astros | Daikin Park | Slade Cecconi | Kai-Wei Teng | 10 | 21 | 8 | 12 | 6 | 57 | Low |
| 8 | Minnesota Twins @ Arizona Diamondbacks | Chase Field | Mike Paredes | Jose Cabrera | 13 | 18 | 8 | 12 | 6 | 57 | Low |
| 9 | Baltimore Orioles @ Los Angeles Dodgers | UNIQLO Field at Dodger Stadium | Brandon Young | Emmet Sheehan | 10 | 18 | 8 | 12 | 6 | 54 | Low |
| 10 | San Diego Padres @ Texas Rangers | Globe Life Field | TBD | Nathan Eovaldi | 14 | 15 | 8 | 8 | 6 | 51 | Low |
| 11 | Washington Nationals @ Tampa Bay Rays | Tropicana Field | Andrew Alvarez | Nick Martinez | 10 | 16 | 8 | 8 | 6 | 48 | Low |
| 12 | Chicago White Sox @ Detroit Tigers | Comerica Park | Davis Martin | Keider Montero | 11 | 12 | 8 | 8 | 6 | 45 | Low |
| 13 | Toronto Blue Jays @ Chicago Cubs | Wrigley Field | Dylan Cease | Shota Imanaga | 6 | 17 | 8 | 8 | 6 | 45 | Low |
| 14 | Boston Red Sox @ Seattle Mariners | T-Mobile Park | Payton Tolle | Logan Gilbert | 10 | 11 | 8 | 8 | 6 | 43 | Ignore |
| 15 | St. Louis Cardinals @ Kansas City Royals | Kauffman Stadium | Dustin May | Stephen Kolek | 8 | 11 | 8 | 8 | 6 | 41 | Ignore |

---

# Game Dissection Cards


---

## 1. Pittsburgh Pirates @ Colorado Rockies — Priority (75)

### Game Context

| Field | Value |
|---|---|
| Park | Coors Field |
| Time | 2026-06-21T19:10:00Z |
| Environment Score | 20 |
| Pitcher Score | 25 |
| Arsenal Score | 8 |
| Matchup Score | 16 |
| Savant Confidence | 6 |

---

### Jared Jones Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 6.23 |
| WHIP | 1.62 |
| K/9 | 9.35 |
| BB/9 | 3.12 |
| HR/9 | 2.08 |
| Vulnerability Score | 25 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Michael Lorenzen Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 7.13 |
| WHIP | 1.85 |
| K/9 | 7.64 |
| BB/9 | 3.18 |
| HR/9 | 1.53 |
| Vulnerability Score | 25 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### Pittsburgh Pirates Lineup

Lineup not confirmed through MLB API at run time.


#### Colorado Rockies Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Home lineup vs away SP
- Primary pitcher concern: Jared Jones
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 2. New York Mets @ Philadelphia Phillies — Watch (67)

### Game Context

| Field | Value |
|---|---|
| Park | Citizens Bank Park |
| Time | 2026-06-21T23:20:00Z |
| Environment Score | 15 |
| Pitcher Score | 22 |
| Arsenal Score | 8 |
| Matchup Score | 16 |
| Savant Confidence | 6 |

---

### David Peterson Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 5.91 |
| WHIP | 1.63 |
| K/9 | 8.16 |
| BB/9 | 3.94 |
| HR/9 | 0.70 |
| Vulnerability Score | 22 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Zack Wheeler Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 2.01 |
| WHIP | 0.85 |
| K/9 | 8.90 |
| BB/9 | 2.15 |
| HR/9 | 1.01 |
| Vulnerability Score | 9 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### New York Mets Lineup

Lineup not confirmed through MLB API at run time.


#### Philadelphia Phillies Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Home lineup vs away SP
- Primary pitcher concern: David Peterson
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 3. Cincinnati Reds @ New York Yankees — Watch (66)

### Game Context

| Field | Value |
|---|---|
| Park | Yankee Stadium |
| Time | 2026-06-21T17:35:00Z |
| Environment Score | 15 |
| Pitcher Score | 21 |
| Arsenal Score | 8 |
| Matchup Score | 16 |
| Savant Confidence | 6 |

---

### Chase Burns Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 2.01 |
| WHIP | 1.02 |
| K/9 | 10.60 |
| BB/9 | 2.90 |
| HR/9 | 1.00 |
| Vulnerability Score | 9 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Elmer Rodríguez Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 4.15 |
| WHIP | 1.85 |
| K/9 | 4.15 |
| BB/9 | 6.23 |
| HR/9 | 0.00 |
| Vulnerability Score | 21 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### Cincinnati Reds Lineup

Lineup not confirmed through MLB API at run time.


#### New York Yankees Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Away lineup vs home SP
- Primary pitcher concern: Elmer Rodríguez
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 4. Los Angeles Angels @ Athletics — Watch (66)

### Game Context

| Field | Value |
|---|---|
| Park | Sutter Health Park |
| Time | 2026-06-21T20:05:00Z |
| Environment Score | 16 |
| Pitcher Score | 20 |
| Arsenal Score | 8 |
| Matchup Score | 16 |
| Savant Confidence | 6 |

---

### Reid Detmers Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 3.68 |
| WHIP | 1.00 |
| K/9 | 10.23 |
| BB/9 | 2.45 |
| HR/9 | 0.72 |
| Vulnerability Score | 8 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Jack Perkins Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 6.15 |
| WHIP | 1.39 |
| K/9 | 10.76 |
| BB/9 | 3.07 |
| HR/9 | 1.10 |
| Vulnerability Score | 20 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### Los Angeles Angels Lineup

Lineup not confirmed through MLB API at run time.


#### Athletics Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Away lineup vs home SP
- Primary pitcher concern: Jack Perkins
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 5. Milwaukee Brewers @ Atlanta Braves — Watch (63)

### Game Context

| Field | Value |
|---|---|
| Park | Truist Park |
| Time | 2026-06-21T17:35:00Z |
| Environment Score | 14 |
| Pitcher Score | 23 |
| Arsenal Score | 8 |
| Matchup Score | 12 |
| Savant Confidence | 6 |

---

### Robert Gasser Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 4.88 |
| WHIP | 1.38 |
| K/9 | 9.00 |
| BB/9 | 4.13 |
| HR/9 | 2.25 |
| Vulnerability Score | 23 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Bryce Elder Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 3.15 |
| WHIP | 1.14 |
| K/9 | 7.41 |
| BB/9 | 2.74 |
| HR/9 | 0.91 |
| Vulnerability Score | 10 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### Milwaukee Brewers Lineup

Lineup not confirmed through MLB API at run time.


#### Atlanta Braves Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Home lineup vs away SP
- Primary pitcher concern: Robert Gasser
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 6. San Francisco Giants @ Miami Marlins — Watch (61)

### Game Context

| Field | Value |
|---|---|
| Park | loanDepot park |
| Time | 2026-06-21T17:40:00Z |
| Environment Score | 10 |
| Pitcher Score | 25 |
| Arsenal Score | 8 |
| Matchup Score | 12 |
| Savant Confidence | 6 |

---

### Logan Webb Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 3.46 |
| WHIP | 1.15 |
| K/9 | 7.77 |
| BB/9 | 2.27 |
| HR/9 | 0.48 |
| Vulnerability Score | 9 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Ryan Gusto Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 7.24 |
| WHIP | 1.76 |
| K/9 | 6.59 |
| BB/9 | 3.29 |
| HR/9 | 1.32 |
| Vulnerability Score | 25 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### San Francisco Giants Lineup

Lineup not confirmed through MLB API at run time.


#### Miami Marlins Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Away lineup vs home SP
- Primary pitcher concern: Ryan Gusto
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 7. Cleveland Guardians @ Houston Astros — Low (57)

### Game Context

| Field | Value |
|---|---|
| Park | Daikin Park |
| Time | 2026-06-21T18:10:00Z |
| Environment Score | 10 |
| Pitcher Score | 21 |
| Arsenal Score | 8 |
| Matchup Score | 12 |
| Savant Confidence | 6 |

---

### Slade Cecconi Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 4.60 |
| WHIP | 1.40 |
| K/9 | 7.47 |
| BB/9 | 2.87 |
| HR/9 | 1.26 |
| Vulnerability Score | 19 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Kai-Wei Teng Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 4.31 |
| WHIP | 1.34 |
| K/9 | 9.61 |
| BB/9 | 4.31 |
| HR/9 | 1.49 |
| Vulnerability Score | 21 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### Cleveland Guardians Lineup

Lineup not confirmed through MLB API at run time.


#### Houston Astros Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Away lineup vs home SP
- Primary pitcher concern: Kai-Wei Teng
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 8. Minnesota Twins @ Arizona Diamondbacks — Low (57)

### Game Context

| Field | Value |
|---|---|
| Park | Chase Field |
| Time | 2026-06-21T19:15:00Z |
| Environment Score | 13 |
| Pitcher Score | 18 |
| Arsenal Score | 8 |
| Matchup Score | 12 |
| Savant Confidence | 6 |

---

### Mike Paredes Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 4.20 |
| WHIP | 1.00 |
| K/9 | 6.00 |
| BB/9 | 3.60 |
| HR/9 | 1.20 |
| Vulnerability Score | 18 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Jose Cabrera Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | — |
| WHIP | — |
| K/9 | — |
| BB/9 | — |
| HR/9 | — |
| Vulnerability Score | 8 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### Minnesota Twins Lineup

Lineup not confirmed through MLB API at run time.


#### Arizona Diamondbacks Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Home lineup vs away SP
- Primary pitcher concern: Mike Paredes
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 9. Baltimore Orioles @ Los Angeles Dodgers — Low (54)

### Game Context

| Field | Value |
|---|---|
| Park | UNIQLO Field at Dodger Stadium |
| Time | 2026-06-21T20:10:00Z |
| Environment Score | 10 |
| Pitcher Score | 18 |
| Arsenal Score | 8 |
| Matchup Score | 12 |
| Savant Confidence | 6 |

---

### Brandon Young Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 3.18 |
| WHIP | 1.25 |
| K/9 | 6.35 |
| BB/9 | 3.32 |
| HR/9 | 0.87 |
| Vulnerability Score | 14 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Emmet Sheehan Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 4.76 |
| WHIP | 1.20 |
| K/9 | 10.07 |
| BB/9 | 2.38 |
| HR/9 | 1.68 |
| Vulnerability Score | 18 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### Baltimore Orioles Lineup

Lineup not confirmed through MLB API at run time.


#### Los Angeles Dodgers Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Away lineup vs home SP
- Primary pitcher concern: Emmet Sheehan
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 10. San Diego Padres @ Texas Rangers — Low (51)

### Game Context

| Field | Value |
|---|---|
| Park | Globe Life Field |
| Time | 2026-06-21T18:35:00Z |
| Environment Score | 14 |
| Pitcher Score | 15 |
| Arsenal Score | 8 |
| Matchup Score | 8 |
| Savant Confidence | 6 |

---

### TBD Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | — |
| WHIP | — |
| K/9 | — |
| BB/9 | — |
| HR/9 | — |
| Vulnerability Score | 8 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: No pitcher ID  
Sample: 0 pitches

---

### Nathan Eovaldi Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 4.23 |
| WHIP | 1.17 |
| K/9 | 8.55 |
| BB/9 | 2.16 |
| HR/9 | 1.75 |
| Vulnerability Score | 15 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### San Diego Padres Lineup

Lineup not confirmed through MLB API at run time.


#### Texas Rangers Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Away lineup vs home SP
- Primary pitcher concern: Nathan Eovaldi
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 11. Washington Nationals @ Tampa Bay Rays — Low (48)

### Game Context

| Field | Value |
|---|---|
| Park | Tropicana Field |
| Time | 2026-06-21T17:40:00Z |
| Environment Score | 10 |
| Pitcher Score | 16 |
| Arsenal Score | 8 |
| Matchup Score | 8 |
| Savant Confidence | 6 |

---

### Andrew Alvarez Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 3.49 |
| WHIP | 1.45 |
| K/9 | 9.85 |
| BB/9 | 3.81 |
| HR/9 | 0.64 |
| Vulnerability Score | 16 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Nick Martinez Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 2.60 |
| WHIP | 1.16 |
| K/9 | 5.42 |
| BB/9 | 1.52 |
| HR/9 | 0.76 |
| Vulnerability Score | 11 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### Washington Nationals Lineup

Lineup not confirmed through MLB API at run time.


#### Tampa Bay Rays Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Home lineup vs away SP
- Primary pitcher concern: Andrew Alvarez
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 12. Chicago White Sox @ Detroit Tigers — Low (45)

### Game Context

| Field | Value |
|---|---|
| Park | Comerica Park |
| Time | 2026-06-21T17:40:00Z |
| Environment Score | 11 |
| Pitcher Score | 12 |
| Arsenal Score | 8 |
| Matchup Score | 8 |
| Savant Confidence | 6 |

---

### Davis Martin Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 3.31 |
| WHIP | 1.19 |
| K/9 | 9.15 |
| BB/9 | 2.20 |
| HR/9 | 0.66 |
| Vulnerability Score | 8 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Keider Montero Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 3.67 |
| WHIP | 1.02 |
| K/9 | 6.11 |
| BB/9 | 2.08 |
| HR/9 | 0.98 |
| Vulnerability Score | 12 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### Chicago White Sox Lineup

Lineup not confirmed through MLB API at run time.


#### Detroit Tigers Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Away lineup vs home SP
- Primary pitcher concern: Keider Montero
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 13. Toronto Blue Jays @ Chicago Cubs — Low (45)

### Game Context

| Field | Value |
|---|---|
| Park | Wrigley Field |
| Time | 2026-06-21T18:20:00Z |
| Environment Score | 6 |
| Pitcher Score | 17 |
| Arsenal Score | 8 |
| Matchup Score | 8 |
| Savant Confidence | 6 |

---

### Dylan Cease Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 2.71 |
| WHIP | 1.19 |
| K/9 | 13.56 |
| BB/9 | 3.82 |
| HR/9 | 0.62 |
| Vulnerability Score | 11 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Shota Imanaga Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 4.26 |
| WHIP | 1.06 |
| K/9 | 8.72 |
| BB/9 | 2.28 |
| HR/9 | 1.77 |
| Vulnerability Score | 17 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### Toronto Blue Jays Lineup

Lineup not confirmed through MLB API at run time.


#### Chicago Cubs Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Away lineup vs home SP
- Primary pitcher concern: Shota Imanaga
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 14. Boston Red Sox @ Seattle Mariners — Ignore (43)

### Game Context

| Field | Value |
|---|---|
| Park | T-Mobile Park |
| Time | 2026-06-21T20:10:00Z |
| Environment Score | 10 |
| Pitcher Score | 11 |
| Arsenal Score | 8 |
| Matchup Score | 8 |
| Savant Confidence | 6 |

---

### Payton Tolle Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 2.93 |
| WHIP | 1.06 |
| K/9 | 9.26 |
| BB/9 | 2.47 |
| HR/9 | 0.77 |
| Vulnerability Score | 8 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Logan Gilbert Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 3.43 |
| WHIP | 1.03 |
| K/9 | 9.55 |
| BB/9 | 2.08 |
| HR/9 | 1.35 |
| Vulnerability Score | 11 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### Boston Red Sox Lineup

Lineup not confirmed through MLB API at run time.


#### Seattle Mariners Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Away lineup vs home SP
- Primary pitcher concern: Logan Gilbert
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

## 15. St. Louis Cardinals @ Kansas City Royals — Ignore (41)

### Game Context

| Field | Value |
|---|---|
| Park | Kauffman Stadium |
| Time | 2026-06-21T18:10:00Z |
| Environment Score | 8 |
| Pitcher Score | 11 |
| Arsenal Score | 8 |
| Matchup Score | 8 |
| Savant Confidence | 6 |

---

### Dustin May Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 3.75 |
| WHIP | 1.14 |
| K/9 | 8.27 |
| BB/9 | 2.31 |
| HR/9 | 0.55 |
| Vulnerability Score | 10 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Stephen Kolek Pitcher Profile

| Stat | Value |
|---|---:|
| Hand | — |
| ERA | 2.68 |
| WHIP | 1.03 |
| K/9 | 6.08 |
| BB/9 | 1.79 |
| HR/9 | 0.89 |
| Vulnerability Score | 11 |

#### Pitch Mix / Damage Profile

| Pitch | Usage | EV | xwOBA | HardHit% |
|---|---:|---:|---:|---:|
| — | — | — | — | — |


Savant note: Savant pull failed  
Sample: 0 pitches

---

### Lineup Status

#### St. Louis Cardinals Lineup

Lineup not confirmed through MLB API at run time.


#### Kansas City Royals Lineup

Lineup not confirmed through MLB API at run time.


---

### What To Inspect

- Which pitcher has the weakest pitch mix?
- Which side has lineup confirmation?
- Which hitters match the pitcher’s most-used weak pitch?
- Is hard contact supported by EV / xwOBA / HardHit%?
- Does park/environment boost or suppress the matchup?
- Does market context agree or disagree?

### MLB-LAB Research Read

- Primary attack side: Away lineup vs home SP
- Primary pitcher concern: Stephen Kolek
- Reason this game ranks here: environment + pitcher risk + pitch-mix damage + Savant sample confidence


---

# End State

This is the complete V2 report:

- every game
- probable pitchers
- pitcher stats
- pitch-mix damage view
- lineup status
- ranked slate index
- game-by-game research cards

No website required.
No manual CSVs required.
