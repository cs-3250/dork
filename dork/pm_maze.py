"""Pre-made maze
"""
# import networkx as nx
# import matplotlib.pyplot as plt
import yaml


class Maze:
    """maze class"""

    def __init__(self, file_name="dork/ypm_maze.yml"):
        """Maze starting"""
        with open(file_name, "r") as file_descriptor:
            self.data = yaml.safe_load(file_descriptor)

    def get_data(self):
        """getter for maze data"""
        return self.data

    def neighbor_of(self, current_position, direction):
        """movement for maze"""
        current_room = self.data['Castle'][current_position]
        if direction in current_room:
            return current_room[direction]
        return None

    def current_position(self):
        """get current position of the player"""
        return self.data["current_room"] or self.data["start_room"]
