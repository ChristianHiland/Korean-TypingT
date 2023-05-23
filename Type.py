# Importing modules
import json
from Scripts import LevelGET, Start

def GameStart():
    # Starting The Game.
    LEVEL = LevelGET()
    Start(LEVEL)

GameStart()