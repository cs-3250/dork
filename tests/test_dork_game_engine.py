""" Tests for the game engine """
from tests.utils import is_a
from dork import game_engine as ge


def test_save():
    ''' Evaluate if a file is saved '''
    assert ge.save('dork_save.dp') == 'Your file has been saved'


def test_load():
    ''' Evaluate if a file has been loaded '''
    assert ge.load('dork_save.dp') == 'Your file has been loaded'


def test_movement():
    ''' Testing player movement if its  '''
    # testWorld = ge()
