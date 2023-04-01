from pathlib import Path

import pytest

from toucan.mvp.calculator import ToucanTournament
from toucan.mvp.calculator.errors import ToucanException


def test_ref_tournament():
    # Let's test who would be the MVP based on the
    # two example files provided as reference
    DATA_PATH = Path(Path(__file__).parent, "data", "tournament")

    # Create the tournament
    tournament = ToucanTournament("ReferenceTournament")

    # Process the tournament files
    tournament.process_tournament(DATA_PATH)

    # According to the data... P3 should be the MVP with 72 points
    assert tournament.name == "ReferenceTournament"
    assert tournament.mvp.nickname == "nick3"
    assert tournament.mvp.total_points == 72

    ref_str = """Player
......
Name:        player 3
Nickname:    nick3
Points:      72"""
    assert str(tournament.mvp) == ref_str


def test_invalid_data_path():
    # Let's assume we give a file as data path... this should throw an error
    DATA_PATH = Path(__file__)

    # Create the tournament
    tournament = ToucanTournament("InvalidDataPathTournament")

    # Process the tournament
    with pytest.raises(ToucanException, match=f"The provided directory path"):
        tournament.process_tournament(DATA_PATH)


def test_invalid_match_files():
    # Let's assume we give a file as data path... this should throw an error
    DATA_PATH = Path(Path(__file__).parent, "data", "tournament_error1")

    # Create the tournament
    tournament = ToucanTournament("InvalidMatchDataTournament")

    # Process the tournament
    with pytest.raises(
        ToucanException, match=f"Failed to process tournament... error on match file"
    ):
        tournament.process_tournament(DATA_PATH)
