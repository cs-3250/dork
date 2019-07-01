""" Tests for the game engine """

from tests.utils import is_a
import dork.game_engine as ge

def test_world(world):
    """ Does the world have a dictionary of rooms? """
    is_a(world, "rooms")
    is_a(world, "players")

def test_save():
    ''' Evaluate if a file is saved '''
    assert ge.save('dork_save.dp') == 'Your file has been saved'

def test_load():
    ''' Evaluate if a file has been loaded '''
    assert ge.load('dork_save.dp') == 'Your file has been loaded'
