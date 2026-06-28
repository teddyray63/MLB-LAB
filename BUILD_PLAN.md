# MLB-LAB Build Plan

Goal:
Build a full MLB research platform focused on correct daily reads.

Core outputs:
1. Command Center
2. Prop Boards
3. Game Hub
4. Player Matchup Card
5. Daily HTML/PDF Card

Architecture:
Collectors -> SQLite Database -> Feature Engine -> FastAPI Backend -> React Frontend

Excluded for now:
- EV
- Sportsbook odds
- Prop-line comparison
