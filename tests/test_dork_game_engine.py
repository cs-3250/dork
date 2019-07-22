"""Testing Game Engine"""
from dork.game.game_engine import GameState


def test_maze_map():
    """Testing start room"""
    maze = GameState()
    data = maze.get_data()
    assert "Castle" in data

    rooms = data["Castle"]
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
    maze = GameState()
    data = maze.get_data()
    start_room = data['start_room']
    current_pos = maze.current_position()
    assert current_pos == start_room, \
        'current position should start at the start room'
    expected_room = 'Not possible room'
    data['current_room'] = expected_room
    current_pos = maze.current_position()
    assert current_pos == expected_room, \
        'current position should change when current room changes'


def test_neighbor_of():
    """Testing Neighboring nodes for validity"""
    maze = GameState()
    expected_current = 'testing room'
    expected_next = 'other room'

    maze.data['current_room'] = expected_current
    maze.data['Castle'][expected_current] = dict(north=expected_next)
    current_pos = maze.current_position()
    next_pos = maze.neighbor_of(current_pos, 'north')
    assert next_pos is expected_next
    assert current_pos is expected_current, \
        "moving north should change position"

    expected_no_room = None
    next_pos = maze.neighbor_of(current_pos, 'invalid direction')
    assert expected_no_room is next_pos


def test_movement():
    """Test moving through maze"""
    maze = GameState()
    expected_current = 'testing room'
    expected_next = 'other room'
    maze.data['current_room'] = expected_current
    maze.data['Castle'][expected_current] = dict(north=expected_next)
    maze.move('north')
    real_real_current = maze.data['current_room']
    assert real_real_current == expected_next, \
        'check maze movement unexpected result'
