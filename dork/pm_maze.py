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
