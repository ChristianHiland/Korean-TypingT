# Importing modules
import json
from Scripts import LevelUP
from Scripts.Questions import Question

# File Paths
Word_Info = "Data/Word_Info.json"

def Start(Level):
    """
    Summary of function:
    This Starts the typing program.
    """
    # Vars

    # Starting
    print("Starting\n")
    print("Level ", Level, "\n")

    # Show the Questions for the level.
    Question(Level)

    # Updating The Level.
    LevelUP(Level)
    NewLevel = 1 + Level
    print("User Leveled up\nNew Level ", NewLevel)