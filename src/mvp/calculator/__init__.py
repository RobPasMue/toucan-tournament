"""Pythonic library used for computing the Most Valuable Player (MVP) of the Toucan Tournament."""

# Version
# ------------------------------------------------------------------------------

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:  # pragma: no cover
    import importlib_metadata  # type: ignore

__version__ = importlib_metadata.version(__name__.replace(".", "-"))
"""Toucan MVP calculator library version."""

# Ease import statements
# ------------------------------------------------------------------------------

from mvp.calculator.tournament import ToucanTournament
