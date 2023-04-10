"""Example script for selecting the Most Valuable Player (MVP) of the Toucan Tournament."""

# Let's define some common functionalites
import os

from toucan.mvp.calculator import ToucanTournament

# Provide the path to your files directory...
# We will assume in this example that it is stored in an
# environment variable called MY_TOUCAN_TOURNAMENT_FILES_DIRECTORY
DATA_PATH = os.environ.get("MY_TOUCAN_TOURNAMENT_FILES_DIRECTORY")

# Create the tournament
tournament = ToucanTournament("ReferenceTournament")

# Process the tournament files
tournament.process_tournament(DATA_PATH)

# Figure out who is the MVP!
print("And the MVP is...\n")
print(tournament.mvp)
