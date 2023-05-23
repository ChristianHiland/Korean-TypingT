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
    Q = Question(Level)
    if Q > 9:
        # Leveling Up The User.
        LevelUP(Level)
        NewLevel = 1 + Level
        print("User Leveled up\nNew Level ", NewLevel)
    else:
        print("\nOpps you didn't get enough right.\nYou didn't level up.")