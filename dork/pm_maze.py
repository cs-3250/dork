"""Pre-made maze
"""
# import networkx as nx
# import matplotlib.pyplot as plt
import yaml
from dork.objects import Player, Room, Item

class Maze:
    """maze class"""

    def __init__(self, file_name="dork/ypm_maze.yml", player):
        """Maze starting"""
        with open(file_name, "r") as file_descriptor:
            self.data = yaml.safe_load(file_descriptor)
            self.player = Player()

    def get_data(self):
        """getter for maze data"""
        return self.data

    def neighbor_of(self, current_position, direction):
        """checks neighbors for maze"""
        current_room = self.data['Castle'][current_position]
        if direction in current_room:
            return current_room[direction]
        return None

    def current_position(self):
        """get current position of the player"""
        return self.data["current_room"] or self.data["start_room"]

    def move(self, direction):
        """Moves player"""
        self.data['current_room'] = \
            self.neighbor_of(self.current_position(), direction)

Treasury = Room('treasury', 'You are in a room full of treasure, we should try not to touch anything', list)
    '''a room on the map'''

main_hall = Room('Main Hall', 'You are in what looks like a hall way with four rooms connected at each side', list)
    '''a room on the map'''

throne_room = Room('Throne room', 'You came across a many swords that look to be melted together to make a throne', list)
    '''a room on the map'''

balcony = Room('balcony', 'You came across a balcony but be careful not to fall', list)
    '''a room on the map'''

