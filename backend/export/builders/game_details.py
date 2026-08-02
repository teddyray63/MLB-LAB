"""Build export game_details[] shell from normalized games."""

from __future__ import annotations

from backend.export.daily_export_models import Game, GameDetail


def build_game_details_shell(games: list[Game]) -> list[GameDetail]:
    """Build one GameDetail shell per game — identity fields only, empty deferred sections."""
    details: list[GameDetail] = []
    for game in games:
        details.append(
            GameDetail(
                game_pk=game.game_pk,
                game_id=game.game_id,
                away_team=game.away_team,
                home_team=game.home_team,
                away_sp=game.away_sp,
                home_sp=game.home_sp,
                start_time_utc=game.start_time_utc,
                status=game.status,
                venue=game.venue,
                away_hitters=[],
                home_hitters=[],
                away_pitch_mix=[],
                home_pitch_mix=[],
                away_bullpen=[],
                home_bullpen=[],
            )
        )
    return details
