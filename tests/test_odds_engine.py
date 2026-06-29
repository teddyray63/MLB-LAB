import pandas as pd

from backend.odds.edge_calculator import calculate_edges
from backend.odds.importer import import_odds_csv
from backend.odds.matcher import match_odds_to_players
from backend.odds.normalizer import normalize_player_name


def test_odds_engine_flow(tmp_path):
    odds_path = tmp_path / "odds.csv"
    odds_path.write_text(
        "book,player_name,team,market,line,odds\n"
        "DraftKings,Smith, Yankees,1+ hit,1.5,-110\n"
        "FanDuel,John Smith,Yankees,1+ hit,1.5,+105\n"
        "BetMGM,John Smith,Yankees,1+ hit,1.5,-115\n",
        encoding="utf-8",
    )

    imported = import_odds_csv(str(odds_path))
    assert not imported.empty
    assert set(imported["book"].tolist()) >= {"DraftKings", "FanDuel", "BetMGM"}

    normalized = normalize_player_name("Smith, John")
    assert normalized == "john smith"

    player_names = ["John Smith", "Mike Trout"]
    matched = match_odds_to_players(imported, player_names, game_team="Yankees")
    assert not matched.empty
    assert matched["player_name"].tolist()[0] == "John Smith"

    model_scores = [{"player_name": "John Smith", "model_probability": 0.62}]
    edges = calculate_edges(matched, model_scores)
    assert not edges.empty
    assert "expected_value" in edges.columns
    assert "edge_pct" in edges.columns
    assert "kelly_fraction" in edges.columns
