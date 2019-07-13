"""Testing pre-made maze"""
from dork.pm_maze import Maze


def test_maze_map():
    """Testing start room"""
    maze = Maze()
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
        direction_names = room.keys()
        assert direction_names
        for next_room in room.values():
            assert next_room is None or next_room in room_names


def test_current_position():
    """test current position"""
    maze = Maze()
    data = maze.get_data()
    start_room = data['start_room']
    current_pos = maze.current_position()
    assert current_pos == start_room, \
        'current position should start at the start room'
    expected_room = 'golbygook not possible room'
    data['current_room'] = expected_room
    current_pos = maze.current_position()
    assert current_pos == expected_room, \
        'current position should change when current room changes'


def test_neighbor_of():
    """testing movement"""
    maze = Maze()
    expected_current = 'testing room'
    expected_next = 'other room'
    maze.data['current_room'] = expected_current
    maze.data['Castle'][expected_current] = dict(north=expected_next)
    current_pos = maze.current_position()
    next_pos = maze.neighbor_of(current_pos, 'north')
    assert next_pos is expected_next
    assert current_pos is expected_current, \
        "moving north should change position"
  
    #We should be checking each cardinal direction for possible movement?
    
    # maze.data['Castle'][expected_current] = dict(east=expected_next)
    # current_pos = maze.current_position()
    # next_pos = maze.neighbor_of(current_pos, 'east')
    # assert next_pos is expected_next
    # assert current_pos is expected_current, \
    #     "moving east should change position"

    # maze.data['Castle'][expected_current] = dict(south=expected_next)
    # current_pos = maze.current_position()
    # next_pos = maze.neighbor_of(current_pos, 'south')
    # assert next_pos is expected_next
    # assert current_pos is expected_current, \
    #     "moving south should change position"
    
    # maze.data['Castle'][expected_current] = dict(west=expected_next)
    # current_pos = maze.current_position()
    # next_pos = maze.neighbor_of(current_pos, 'west')
    # assert next_pos is expected_next
    # assert current_pos is expected_current, \
    #     "moving west should change position"

    expected_no_room = None
    next_pos = maze.neighbor_of(current_pos, 'invalid direction')
    assert expected_no_room is next_pos


    
