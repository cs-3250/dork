""" Game Engine """

from random import choice
import networkx as nx
from numpy import ndarray, ndenumerate
from mazelib import Prims
from dork.objects import Room


class GameEngine:
    '''game engine: stores game map and player location, handles movement'''

    def __init__(self):
        self.world = None
        self.player_location = None

    def save(self, file_name='dork_save.dp'):
        """ Save game to file """
        print('Saving Game...')
        self.world = nx.write_yaml(self.world, file_name)
        print('Game progress has been saved.')
        return "0"

    def load(self, file_name='dork_save.dp'):
        """ Load game from file """
        print('Loading Game...\n')
        try:
            self.world = nx.read_yaml(file_name)
            print("Game has been loaded!")
            # FIXME need to check that self.world now contains a graph
            # For all we know, we could be importing yaml of just a string.
        except FileNotFoundError:
            print("No such file.")

    def movement(self, direction):
        """ Player movement """

        directions = {'n': 'north',
                      's': 'south',
                      'w': 'west',
                      'e': 'east'}

        if direction not in directions:
            return "Invalid direction! Type a different command."

        for room in self.world[self.player_location]:
            edge = self.world.edges[self.player_location, room]
            if edge['direction'] == direction:
                self.player_location = room
                return "You went" + directions[direction] + "."

        return "You are not able to move in that direction. Try again!"

    def maze_generation(self, size=(3, 3)):
        """ Random maze generation """

        maze = Prims(*size).generate()
        rooms = ndarray(shape=[d - 2 for d in maze.shape], dtype=Room)
        self.world = nx.DiGraph()

        for index, _ in ndenumerate(rooms):
            x_point = index[0]
            y_point = index[1]
            x_maze = x_point + 1
            y_maze = y_point + 1
            if maze[x_maze, y_maze] == 0:
                rooms[index] = Room()
                x_north = x_point - 1
                if x_north >= 0 and rooms[(x_north, y_point)] is not None:
                    self.world.add_edge(rooms[index],
                                        rooms[(x_north, y_point)],
                                        direction='n')
                    self.world.add_edge(rooms[(x_north, y_point)],
                                        rooms[index],
                                        direction='s')
                y_west = y_point - 1
                if y_west >= 0 and rooms[(x_point, y_west)] is not None:
                    self.world.add_edge(rooms[index],
                                        rooms[(x_point, y_west)],
                                        direction='w')
                    self.world.add_edge(rooms[(x_point, y_west)],
                                        rooms[index],
                                        direction='e')

        self.player_location = choice(list(self.world.nodes))
