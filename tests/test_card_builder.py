import pandas as pd

from backend.engine.card_builder import build_betting_card_portfolios


def test_build_betting_card_portfolios_diversifies_and_excludes_duplicates():
    rows = [
        {"player_name": "A", "team": "Yankees", "game_name": "Game 1", "singles_score": 90, "total_bases_score": 80, "runs_score": 70, "rbi_score": 60, "lotto_score": 75},
        {"player_name": "B", "team": "Yankees", "game_name": "Game 1", "singles_score": 88, "total_bases_score": 78, "runs_score": 68, "rbi_score": 58, "lotto_score": 73},
        {"player_name": "C", "team": "Mets", "game_name": "Game 2", "singles_score": 86, "total_bases_score": 76, "runs_score": 66, "rbi_score": 56, "lotto_score": 71},
        {"player_name": "D", "team": "Mets", "game_name": "Game 2", "singles_score": 84, "total_bases_score": 74, "runs_score": 64, "rbi_score": 54, "lotto_score": 69},
        {"player_name": "E", "team": "Dodgers", "game_name": "Game 3", "singles_score": 82, "total_bases_score": 72, "runs_score": 62, "rbi_score": 52, "lotto_score": 67},
        {"player_name": "F", "team": "Dodgers", "game_name": "Game 3", "singles_score": 80, "total_bases_score": 70, "runs_score": 60, "rbi_score": 50, "lotto_score": 65},
        {"player_name": "G", "team": "Astros", "game_name": "Game 4", "singles_score": 78, "total_bases_score": 68, "runs_score": 58, "rbi_score": 48, "lotto_score": 63},
        {"player_name": "H", "team": "Astros", "game_name": "Game 4", "singles_score": 76, "total_bases_score": 66, "runs_score": 56, "rbi_score": 46, "lotto_score": 61},
        {"player_name": "I", "team": "Red Sox", "game_name": "Game 5", "singles_score": 74, "total_bases_score": 64, "runs_score": 54, "rbi_score": 44, "lotto_score": 59},
        {"player_name": "J", "team": "Red Sox", "game_name": "Game 5", "singles_score": 72, "total_bases_score": 62, "runs_score": 52, "rbi_score": 42, "lotto_score": 57},
        {"player_name": "K", "team": "Blue Jays", "game_name": "Game 6", "singles_score": 70, "total_bases_score": 60, "runs_score": 50, "rbi_score": 40, "lotto_score": 55},
        {"player_name": "L", "team": "Blue Jays", "game_name": "Game 6", "singles_score": 68, "total_bases_score": 58, "runs_score": 48, "rbi_score": 38, "lotto_score": 53},
    ]

    cards = build_betting_card_portfolios(pd.DataFrame(rows), {"minimum_confidence": 30.0})

    for card_name in ["top_10_singles", "top_10_total_bases", "top_10_runs", "top_10_rbi", "safest_2_leg", "safest_3_leg", "best_4_leg", "best_6_leg_lotto"]:
        assert card_name in cards

    for card in cards.values():
        if isinstance(card, list):
            continue
        assert card["leg_count"] >= 1
        assert card["confidence_pct"] >= 0
        assert card["risk"] in {"low", "medium", "high"}
        assert card["grade"] in {"A+", "A", "A-", "B+", "B", "B-", "C", "PASS"}
        assert len(card["legs"]) == card["leg_count"]
        assert len({leg["player"] for leg in card["legs"]}) == len(card["legs"])
        team_counts = {}
        for leg in card["legs"]:
            team_counts[leg["team"]] = team_counts.get(leg["team"], 0) + 1
        assert max(team_counts.values(), default=0) <= 2
        assert len({leg["game"] for leg in card["legs"]}) >= 2
