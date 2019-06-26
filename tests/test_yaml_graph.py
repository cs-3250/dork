import os.path
from os import path
from unittest import mock

# *** Checking File Tests ***

# Test 1 - Good file

# a) Check if a path exists


def _read(file_path, f):
    file_path = 'maze.yml'
    with open(file_path) as f:
        return f.read()


# b) Open the file
def _good_file(path):
    if os.path.exists('maze.yaml'):
        return True
    else:
        return False


# c) First line == "Rooms"
def _first_line(f):
    first_line = f.readline()
    if first_line == "Rooms":
        return True
    else:
        return False


# d) Second line == "Empty Room"
def _second_line(f):
        second_line = f.readline()
        if second_line == "Empty Room":
                return True
        else:
                return False

    # *** Creating Nodes Tests ***

    # Test 1 - Create a No Nodes
    # Check if nothing exists

    # Test 2 - Create a Node
    # G[0] exists
    # G[0] data

    # Test 3 - Create second Node
    # G[1] exists
    # G[1] data

    # Test 4 - Create Two Nodes
    # G[2] does not exist

    # Test 4 - Create Node Automatically
    # Node exists
    # Node Based on a File Data

    # Test 5 - Create Multiple Node Automatically
    # Last Node == lastFileData

    def runtests():
        _read('file_path', 'f')
        _good_file(path)
        _first_line(f)
        _second_line()


if __name__ == "__main__":
    runtests()
