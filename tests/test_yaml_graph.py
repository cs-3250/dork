import os.path
from unittest import mock
import networkx as nx
import yaml

# *** Checking File Tests ***

# Test 1 - Good file
# a) Check if a path exists
def _read(path):
        os.path.isfile(path)
        yaml.safe_load()



def _check_room(rooms):
        for rooms in rooms
                for path in room
                        assert path in rooms or null

# First line == "Rooms"
def _first_line(f):
    first_line = f.readline()
    if first_line == "Rooms":
        return True
    else:
        return False

def runtests():
        path = "maze.yml"
        rooms = yaml.load(path)
        _read(path)
        _check_room()


if __name__ == "__main__":
    unittest.main()
