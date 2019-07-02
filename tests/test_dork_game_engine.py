""" Tests for the game engine """

from tests.utils import is_a
import dork.game_engine as ge


def test_save():
    ''' Saves data no matter the test data is '''
    test_data = "dogs rule"

    out = ge.save(test_data)
    assert "0" in out, \
        "Game_Engine.save method couldn't save game data"


def test_load(self):
    ''' Loads in data to parse '''
    out = ge.load("Trash")
    assert "Try again" in out, \
        "Game_Engine.load method couldn't find load data"

# def test_movement():
#     ''' Testing player movement if its  '''
#
# testWorld = ge()
