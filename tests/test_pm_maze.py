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
    assert room_names is not []
    assert None not in room_names
    for room_name, room in rooms.items():
        assert room is not None
        assert isinstance(room, dict)
        direction_names = room.keys()
        assert len(direction_names) > 0
        for direction, next_room in room.items():
            assert next_room is None or next_room in room_names
