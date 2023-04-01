"""Module defining the different disciplines ran in the Tucan Tournament
and auxiliary methods."""

from enum import Enum
from typing import Dict, Tuple

from mvp.calculator.errors import TucanException


class TucanDiscipline(Enum):
    """Provides an enum holding the different disciplines available.

    Notes
    -----
    The pattern on how to process each line of the files for each
    discipline match is stored here. The values in each enum are as
    follows:
        * Enum ID.
        * Regex for processing each player's contribution in a match.
        * Dictionary containing the "evaluation" as a function of the position.
        * Location in which the points are stored inside the evaluation and whether
          the points contributed are considered as an addition or subtraction
          (e.g. goal made or goal received).
    """

    # TODO: force regex to be numbers or letters
    BASKETBALL = (
        0,
        r"^(.*);(.*);(.*);(.*);(.*);(.*);(.*);(.*)$",
        {"G": (2, 3, 1), "F": (2, 2, 2), "C": (2, 1, 3)},
        ((0, True)),
    )
    HANDBALL = (
        1,
        r"^(.*);(.*);(.*);(.*);(.*);(.*);(.*);(.*)$",
        {"G": (50, 5, -2), "F": (20, 1, -1)},
        ((1, True), (2, False)),
    )

    def get_pattern(self) -> str:
        """Accessor method to the line pattern in a match file.

        Returns
        -------
        str
            The regex expression for a match line.
        """
        return self.value[1]

    def get_eval_params(self) -> Dict[str, Tuple[int]]:
        """Accessor method to the evaluation parameters for a player in a match file.

        Returns
        -------
        Dict[str, Tuple[int]]
            Dictionary containing the evaluation parameters as a
            function of the position.
        """
        return self.value[2]

    def get_points_in_eval_params(self) -> Tuple[Tuple[int, bool]]:
        """Accessor method to the positions in the evaluation parameters,
        where points are contributed to a match.

        Returns
        -------
        Tuple[Tuple[int, bool]]
            Tuple of tuples, where each subtuple indicates the location
            where points are contributed and whether they should be considered
            as an addition to the team's score os a subtraction.
        """
        return self.value[3]


def get_discipline_by_name(name: str) -> TucanDiscipline:
    """Method for returning the TucanDiscipline enum class.

    Parameters
    ----------
    name : str
        The name of the discipline.

    Returns
    -------
    TucanDiscipline
        The TucanDiscipline enum.
    """
    for discipline in TucanDiscipline:
        if name.capitalize() == discipline.name:
            return discipline

    return TucanException(
        f"The provided discipline name '{name}' is not implemented. Consider adding it to the TucanDiscipline enum class."  # noqa : E501
    )
