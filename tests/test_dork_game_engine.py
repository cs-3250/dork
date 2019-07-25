"""Testing Game Engine"""
from dork.game.game_engine import GameState


def test_load_map():
    """Testing start room"""
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
        directions = room['paths']
        assert directions
        for next_room in directions.values():
            assert next_room is None or next_room in room_names


def test_current_position():
    """Test current position"""
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
    """Testing Neighboring nodes for validity"""
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
    """Test moving through gamestate"""
    gamestate = GameState()
    expected_current = 'testing room'
    expected_next = 'other room'
    gamestate.data['current_room'] = expected_current
    gamestate.data['Map'][expected_current] = dict(north=expected_next)
    gamestate.move('north')
    real_real_current = gamestate.data['current_room']
    assert real_real_current == expected_next, \
        'check gamestate movement unexpected result'

    gamestate.data['current_room'] = expected_current
    gamestate.data['Map'][expected_current] = dict(north=None)
    gamestate.move('north')
    assert gamestate.data['current_room'] is expected_current
