""" Tests for the game engine """

# from tests.utils import is_a
from networkx import DiGraph
from dork.game_engine import GameEngine
from dork.objects import Room


def test_save():
    ''' Saves data no matter the test data is '''
    game = GameEngine()
    test_data = "dogs rule"

    out = game.save(test_data)
    assert "0" in out, \
        "Game_Engine.save method couldn't save game data"


def test_load():
    ''' Loads in data to parse '''
    # game = GameEngine()

    # out = game.load("Trash")
    # assert "Try again" in out, \
    #     "Game_Engine.load method couldn't find load data"


def test_maze_generation():
    '''maze_generation should:
         populate world with nonempty graph of Room nodes
         populate player_location with a Room'''
    game_engine = GameEngine()
    game_engine.world = None
    game_engine.player_location = None
    game_engine.maze_generation()
    assert isinstance(game_engine.world, DiGraph)
    assert isinstance(game_engine.player_location, Room)
    assert game_engine.world  # sequence nonempty
    for room in game_engine.world:
        assert isinstance(room, Room)
