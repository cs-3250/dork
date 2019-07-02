""" Game Engine """

from random import choice
import networkx as nx
from numpy import ndarray, ndenumerate as Np
from dork.objects import Room

__all__ = ["save", "load", "movement", "maze_generation"]


def __init__(self):
    self.world = None


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
        with open(file_name) as file:
            self.world = nx.read_yaml(file_name)
            print("Game has been loaded!")
    except IOError:
        print("There was a problem loading your game.")
    return


def movement(self, direction):
    """ Player movement """
    directions = {'n': 'north',
                  's': 'south',
                  'w': 'west',
                  'e': 'east'}
    if direction not in directions:
        return "Invalid direction! Type a different command."
    for room in self.world[self.player_location]:
        if self.world.edges[self.player_location, room]['direction'] \
           == direction:
            self.player_location = room
            return "You went" + directions[direction] + "."
    return "You are not able to move in that direction. Try again!"


def maze_generation(self, mazelib, Np):
    """ Random maze generation """

    maze_bigness = (3, 3)

    maze = mazelib.Prims(*maze_bigness).generate()
    self.world = nx.DiGraph()

    rooms = Np.ndarray(shape=[d - 2 for d in maze.shape])

    for index, rooms in Np.ndenumerate(rooms):
        x_point = index[0]
        y_point = index[1]
        x_maze = x_point + 1
        y_maze = y_point + 1
        if maze[x_maze, y_maze] == 0:
            rooms[index] = rooms()
            x_north = x_point - 1
            if x_north >= 0 and self.world[(x_north, y_point)] is not None:
                self.world.add_edge(self.world[index],
                                    self.world[(x_north, y_point)],
                                    direction='n')
                self.world.add_edge(self.world[(x_north, y_point)],
                                    self.world[index],
                                    direction='s')
            y_west = y_point - 1
            if y_west >= 0 and self.world[(x_point, y_west)] is not None:
                self.world.add_edge(self.world[index],
                                    self.world[(x_point, y_west)],
                                    direction='w')
                self.world.add_edge(self.world[(x_point, y_west)],
                                    self.world[index],
                                    direction='e')

    self.player_location = choice(list(self.world.nodes))


if __name__ == "__main__":
    pass
