"""Module containing the ``ToucanTournament`` class."""
from pathlib import Path
import re
from typing import List, Union

from toucan.mvp.calculator.discipline import get_discipline_by_name
from toucan.mvp.calculator.errors import ToucanException
from toucan.mvp.calculator.players import ToucanPlayer


class ToucanTournament:
    """Class containing the Toucan tournament logic."""

    def __init__(self, name: str) -> None:
        """Instantiate ``ToucanTournament`` onject.

        Parameters
        ----------
        name : str
            The name of the tournament.
        """
        self._name: str = name

        # Initialize the participants and potential MVP
        self._players: dict[str, ToucanPlayer] = {}
        self._mvp: Union[ToucanPlayer, None] = None

    @property
    def name(self) -> str:
        """Access property for retrieving the name of the tournament.

        Returns
        -------
        str
            The name of the tournament.
        """
        return self._name

    @property
    def mvp(self) -> Union[ToucanPlayer, None]:
        """Access property for retrieving the name of the tournament's MVP.

        Returns
        -------
        ToucanPlayer or None
            The MVP of the tournament. ``None`` if no MVP is possible.
        """
        return self._mvp

    @property
    def players(self) -> List[ToucanPlayer]:
        """List containing the player's participating in the tournament.

        Returns
        -------
        List[ToucanPlayer]
            List of tournament's players.
        """
        return self._players.values()

    def process_tournament(self, dir: Union[Path, str]) -> None:
        """Process a tournament given a directory where the match files are located.

        Parameters
        ----------
        dir : Path or str
            Directory where the match files are located.
        """
        # First of all, check that the provided argument is actually
        # a directory. Otherwise raise an error.
        dir_as_path = dir if isinstance(dir, Path) else Path(dir)
        if not dir_as_path.is_dir():
            raise ToucanException(f"The provided directory path {dir} is not a directory.")

        # Now that we have ensured that it is a directory, let's start
        # processing the matches
        for match_file in dir_as_path.iterdir():
            # Skip subdirectories (if any)... we will only process files
            if not match_file.is_file():
                continue

            # Process the match file
            self._process_match(match_file)

        # Once all matches in the tournament have been processed
        # determine who is the MVP!
        for player in self.players:
            # In case no MVP is yet available... the first one in line
            # will be the MVP
            if self._mvp is None:
                self._mvp = player
                continue

            # Now, check if the current player has more points than
            # the "current" MVP
            if player.total_points > self._mvp.total_points:
                self._mvp = player

    def _process_match(self, filepath: Path):
        """Process Toucan tournament match file.

        Parameters
        ----------
        filepath : Path
            The path to the match's file.
        """
        with open(filepath, "r") as file:
            # Read the file
            lines = file.read().splitlines()

            # Read the first line to get the sport/discipline
            discipline = get_discipline_by_name(lines[0])

            # Initialize the scores for each team
            teams: dict[str, int] = {}
            player_teams: dict[str, list[ToucanPlayer]] = {}

            # Now, proceed to reading each line
            line_pattern = re.compile(discipline.get_pattern())
            for line in lines[1:]:
                # Check that line matches the expected pattern and raise error otherwise
                entries = line_pattern.match(line)
                if entries is None:
                    raise ToucanException(
                        f"Failed to process tournament... error on match file '{filepath}'"
                    )
                else:
                    name, nickname, _, team, position, *marks = entries.groups()
                    marks = [int(mark) for mark in marks]  # Reassign to integers

                # Check if player exists, otherwise create it
                player = self._players.get(nickname)
                if player is None:
                    player = self._players[nickname] = ToucanPlayer(name, nickname)

                # Check if the team has already been processed or not... if not, initialize it
                if not team in teams.keys():
                    teams[team] = 0
                    player_teams[team] = []

                # Add the player to the team
                player_teams[team].append(player)

                # Add the player's points and its contribution to the team
                player.add_match_points(marks, discipline, position)
                teams[team] += player.get_team_score_contribution(marks, discipline)

            # Once all player evaluations have been processed... Let's see which team won
            # and provide the bonus points to the winner players
            team_a, team_b = teams.keys()
            team_a_score, team_b_score = teams.values()
            if team_a_score > team_b_score:
                [winner_player.add_bonus_points() for winner_player in player_teams[team_a]]
            elif team_a_score < team_b_score:
                [winner_player.add_bonus_points() for winner_player in player_teams[team_b]]
            else:  # pragma: no cover
                raise Exception("Matches cannot end in a draw. Invalid tournament.")
