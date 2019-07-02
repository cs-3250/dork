""" Tests for the game engine """

# from tests.utils import is_a
from dork.game_engine import GameEngine


def test_save():
    ''' Saves data no matter the test data is '''
    game = GameEngine()
    test_data = "dogs rule"

    out = game.save(test_data)
    assert "0" in out, \
        "Game_Engine.save method couldn't save game data"

def test_load():
    ''' Loads in data to parse '''
    game = GameEngine()

    out = game.load("Trash")
    assert "Try again" in out, \
        "Game_Engine.load method couldn't find load data"

# def test_movement():
#     ''' Testing player movement if its  '''
#
# testWorld = ge()
