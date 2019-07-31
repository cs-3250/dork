"""game_engine testing.

This module is meant to test the Game Engine portion of Dork. Designed to
be used with Pytest and fixtures in conftest.py.

Example:
    To test in terminal::

        $ python -m pytest tests/test_dork_game_engine.py

Attributes:
    None

Todo:
    * Add fixture for GameState()
    * Add fixture for a generic testing map (less hardcoding in tests)

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

from dork.game.game_engine import GameState


def test_load_map():
    """ Test to ensure map loads correctly.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError::
            If any tests fail, an assertion error is thrown.

    """
    gamestate = GameState()
    data = gamestate.data
    assert "Map" in data

    rooms = data["Map"]
    assert rooms is not None, 'rooms should exist'
    assert isinstance(rooms, dict)

    room_names = list(rooms.keys())
    assert None not in room_names
    for room in rooms.values():
        assert room is not None
        assert isinstance(room, dict)
        directions = room
        assert directions
        for next_room in directions.values():
            assert next_room is None or next_room in room_names


def test_current_position():
    """ Test to ensure current_position functions correctly.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError::
            If any tests fail, an assertion error is thrown.

    """
    gamestate = GameState()
    data = gamestate.data
    start_room = data['start_room']
    current_pos = gamestate.current_position()
    assert current_pos == start_room, \
        'current position should start at the start room'
    expected_room = 'Not possible room'
    data['current_room'] = expected_room
    current_pos = gamestate.current_position()
    assert current_pos == expected_room, \
        'current position should change when current room changes'


def test_neighbor_of():
    """ Test to ensure neighbor_of provides correct key from provided direction.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError::
            If any tests fail, an assertion error is thrown.

    """
    gamestate = GameState()
    expected_current = 'testing room'
    expected_next = 'other room'

    gamestate.data['current_room'] = expected_current
    gamestate.data['Map'][expected_current] = dict(north=expected_next)
    current_pos = gamestate.current_position()
    next_pos = gamestate.neighbor_of(current_pos, 'north')
    assert next_pos is expected_next
    assert current_pos is expected_current, \
        "moving north should change position"

    expected_no_room = None
    next_pos = gamestate.neighbor_of(current_pos, 'invalid direction')
    assert expected_no_room is next_pos


def test_movement():
    """ Test to ensure movement updates current_postion,
        but not with empty direction.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError::
            If any tests fail, an assertion error is thrown.

    """
    gamestate = GameState()
    expected_current = 'testing room'
    expected_next = 'other room'
    gamestate.data['current_room'] = expected_current
    gamestate.data['Map'][expected_current] = dict(north=expected_next)
    gamestate.move('north')
    real_real_current = gamestate.data['current_room']
    assert real_real_current == expected_next, \
        'check gamestate movement unexpected result'

    # None-room  movement checking
    gamestate.data['current_room'] = expected_current
    gamestate.data['Map'][expected_current] = dict(north=None)
    gamestate.move('north')
    assert gamestate.data['current_room'] is expected_current
