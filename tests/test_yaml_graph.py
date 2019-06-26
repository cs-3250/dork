import os.path
from os import path
from unittest import mock

# *** Checking File Tests ***

# Test 1 - Bad String/Input
# Check if valid file path

# Test 2 - Good file, bad text
# assert error on read

# Test 3 - Good file

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
def _second_line():

        

        # *** Creating Nodes Tests ***

        # Test 1 - Create a No Nodes
        #

        # Test 2 - Create a Node
        #

        # Test 3 - Create Two Nodes
        #

        # Test 4 - Create Node Automatically
        # Node exists
        # Node Based on a File Data

        # Test 5 - Create Multiple Node Automatically
        # Last Node == lastFileData

    def runtests(file_path, f):
        _read('file_path', 'f')
       # _good_file(path)
       # _first_line(f)
       # _second_line()


if __name__ == "__main__":
    runtests()
