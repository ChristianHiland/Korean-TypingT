# Importing modules
import json

# File Paths
LevelJSON = "Data/Level.json"
Word_Info = "Data/Word_Info.json"

def LevelUP(Level):
    """
    Summary of function:
    This adds a number to the Level JSON file, 
    so when the program starts again it starts,
    on the last level the user was on.
    """
    NewLevel = 1 + Level

    with open(LevelJSON, "w") as LevelUp:
        Data = {
            "User Level": NewLevel,
            "Total Levels": 5
        }
        json.dump(Data, LevelUp, indent=4, ensure_ascii=True)
    return NewLevel

def LevelGET():
    """
    Summary of function:
    This gets the level that the user is on.
    """
    with open(LevelJSON, "r") as Get:
        Data = json.load(Get)
        Level = Data['User Level']
        return Level