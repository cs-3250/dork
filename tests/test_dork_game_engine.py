""" Tests for the game engine """

# from tests.utils import is_a
import random
import string
from os import path, remove
from networkx import DiGraph, is_isomorphic
from dork.game_engine import GameEngine
from dork.objects import Room


def random_string(length):
    '''generate a random string of {length} characters'''
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def random_nonexistent_filename(length):
    '''generate a random filename which doesn't yet exist'''
    while True:
        filename = random_string(length)
        if not path.exists(filename):
            return filename


def test_load_nonexistent_file():
    '''FileNotFoundError should be handled when for loading nonexistent file'''
    filename = random_nonexistent_filename(64)
    game_engine = GameEngine()
    try:
        game_engine.load(filename)
    except FileNotFoundError:
        assert False


def test_load_invalid_file():
    """attempting to load a file without a valid graph
       should not overwrite the current world"""
    filename = random_nonexistent_filename(64)
    with open(filename, 'w') as output:
        output.write(random_string(64))
    game_engine = GameEngine()
    world_before = game_engine.world
    game_engine.load(filename)
    world_after = game_engine.world
    assert world_before == world_after


def test_save_and_reload():
    '''a given world should remain unchanged when saved, then loaded'''
    filename = random_string(64)
    game_engine = GameEngine()
    game_engine.maze_generation((13, 13))
    world_before = game_engine.world
    game_engine.save(filename)
    game_engine.world = None
    game_engine.load(filename)
    world_after = game_engine.world
    assert is_isomorphic(world_before, world_after)
    remove(filename)


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


def test_movement_in_one_room():
    '''no movement should be possible with no edges'''
    game_engine = GameEngine()
    game_engine.world = DiGraph()
    room = Room()
    game_engine.player_location = room
    game_engine.world.add_node(room)
    game_engine.movement('n')
    assert game_engine.player_location == room
    game_engine.movement('s')
    assert game_engine.player_location == room
    game_engine.movement('w')
    assert game_engine.player_location == room
    game_engine.movement('e')
    assert game_engine.player_location == room
    game_engine.movement("Bob's your uncle.")
    assert game_engine.player_location == room
    assert game_engine


def test_movement_in_two_rooms():
    '''no movement should be possible with no edges'''
    game_engine = GameEngine()
    game_engine.world = DiGraph()
    west_room = Room()
    east_room = Room()
    game_engine.world.add_nodes_from([west_room, east_room])
    game_engine.world.add_edge(west_room, east_room, direction='e')
    game_engine.world.add_edge(east_room, west_room, direction='w')
    game_engine.player_location = west_room
    game_engine.movement('n')
    assert game_engine.player_location == west_room
    game_engine.movement('w')
    assert game_engine.player_location == west_room
    game_engine.movement('s')
    assert game_engine.player_location == west_room
    game_engine.movement('e')
    assert game_engine.player_location == east_room
    game_engine.movement('n')
    assert game_engine.player_location == east_room
    game_engine.movement('e')
    assert game_engine.player_location == east_room
    game_engine.movement('s')
    assert game_engine.player_location == east_room
    game_engine.movement('w')
    assert game_engine.player_location == west_room
