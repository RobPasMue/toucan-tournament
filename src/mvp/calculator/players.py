"""Module contaiming the ``Player`` class and auxiliary methods related to them."""

from typing import List

from mvp.calculator.discipline import TucanDiscipline
from mvp.calculator.errors import TucanException


class TucanPlayer:
    """Class representing a player of Tucan tournament sport."""

    def __init__(self, name: str, nickname: str) -> None:
        """Constructor for ``TucanPlayer`` class.

        Parameters
        ----------
        name : str
            The name of the player.
        nickname : str
            The nickname of the player.
        """
        self._name: str = name
        self._nickname: str = nickname
        self._points: List[int] = []

    @property
    def name(self) -> str:
        """Access property for retrieving the name of the player.

        Returns
        -------
        str
            The name of the player.
        """
        return self._name

    @property
    def nickname(self) -> str:
        """Access property for retrieving the nickname of the player.

        Returns
        -------
        str
            The nickname of the player.
        """
        return self._name

    @property
    def points(self) -> List[int]:
        """Access property for retrieving the points of the player.

        Returns
        -------
        List[int]
            The list of points acquired per match.
        """
        return self._points

    @property
    def total_points(self) -> int:
        """Total number of points obtained by a player.

        Returns
        -------
        int
            Total number of points.
        """
        return sum(self._points)

    def add_match_points(
        self, marks: List[int], discipline: TucanDiscipline, position: str
    ) -> None:
        """Computes the number of points acquired in a match and stores them
        inside the player's record track (i.e. self._points).

        Parameters
        ----------
        evaluation : List[int]
            Marks obtained during the match.
        discipline : TucanDiscipline
            Sports discipline in which the marks were obtained.
        position : str
            Player's position in the match.
        """
        # Get the evaluation parameters for the given discipline and player's position
        eval_params = discipline.get_eval_params().get(position, None)
        if not eval_params:
            raise TucanException(
                f"Problems retrieving evaluation parameters for '{discipline.name}' in position '{position}'."
            )

        # Do a quick check to see if the sizes of eval_params and marks are the same
        if len(eval_params) != len(marks):
            raise TucanException(
                f"Evaluation parameters for '{discipline.name}' in position '{position}' do not match the marks given."
            )

        # Compute the amount of points received and store them
        self._points.append(sum([eval * mark for eval, mark in zip(eval_params, marks)]))

    def get_team_score_contribution(self, marks: List[int], discipline: TucanDiscipline) -> int:
        """Retreive the score contribution of a player in a match.

        Parameters
        ----------
        evaluation : List[int]
            Marks obtained during the match.
        discipline : TucanDiscipline
            Sports discipline in which the marks were obtained.

        Returns
        -------
        int
            Score contributed to the team's result.
        """
        # Get tthe score contribution for a given discipline
        score_eval_params = discipline.get_points_in_eval_params()

        # Compute the contribution to the team's score
        contrib = 0
        for elem in score_eval_params:
            score_idx, is_addition = elem
            if is_addition:
                contrib += marks[score_idx]
            else:
                contrib -= marks[score_idx]

        # Return the contribution
        return contrib

    def add_bonus_points(self) -> None:
        """Adds bonus points (i.e. 10) to the last match the player has played."""
        self._points[-1] = self._points[-1] + 10
