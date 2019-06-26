import os.path
from os import path


def _good_file(path):
    if path.exists("maze.yaml"):
        return True
    else: 
        return False


if __name__ == "__main__":
    _good_file(path)
