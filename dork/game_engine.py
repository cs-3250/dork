from random import choice
import networkx as nx
from numpy import ndarray, ndenumerate as np
from dork.objects import Room

__all__ = ["save", "load", "movement", "maze_generation"]

def __init__(self):
    self.world = None

def save(self, file_name='dork_save.dp'):
    """ Save game to file """
    print('Saving Game...')
    self.world = nx.write_yaml(self.world, file_name)
    print('Game progress has been saved.')

def load(self, file_name='dork_save.dp'):
    """ Load game from file """
    print('Loading Game...\n')
    try:
        with open(file_name):
            self.world = nx.read_yaml(file_name)
    except IOError:
        return "There was a problem loading your game."

def movement(self, direction):
    self.player_location
    # check if the direction is in a tuplue with all of our directions
    if direction in ('n', 'e', 's', 'w'):
        pass
    else:
        return "you can't go that way!"

    self.world.add_nodes_from()
    self.world.add_edge()
    self.world.add_edge()

    # GameEngine.movement(w)
    # Returns a string

    # pirateShip = Room()
    # tikiHut = Room()
    # G.add_nodes_from([pirateShip, tikiHut, yurt])
    # G.add_edge(pirateShip, tikiHut, direction='e')
    # G.add_edge(tikiHut, pirateShip, direction='w')
    # G.add_edge(tikiHut, yurt, direction='s')
    # G.add_edge(yurt, tikiHut, direction='n')
    # tikiHut in G[pirateShip]
    # G.edges[pirateShip, tikiHut]['direction']
    # yurt in G[pirateShip]

def maze_generation(self):

    MAZE_BIGNESS = (3, 3)

    MAZE = mazelib.Prims(*MAZE_BIGNESS).generate()
    self.world = nx.DiGraph()

    ROOMS = np.ndarray(shape=[d - 2 for d in MAZE.shape])

    for index, room in np.ndenumerate(ROOMS):
        x = index[0]
        y = index[1]
        x_maze = x + 1
        y_maze = y + 1
        if MAZE[x_maze, y_maze] == 0:
            ROOMS[index] = ROOMS()
            x_north = x - 1
            if x_north >= 0 and self.world[(x_north, y)] is not None:
                    self.world.add_edge(self.world[index],
                               self.world[(x_north, y)],
                               direction='n')
                    self.world.add_edge(self.world[(x_north, y)],
                               self.world[index],
                               direction='s')
            y_west = y - 1
            if y_west >= 0 and self.world[(x, y_west)] is not None:
                    self.world.add_edge(self.world[index],
                               self.world[(x, y_west)],
                               direction='w')
                    self.world.add_edge(self.world[(x, y_west)],
                               self.world[index],
                               direction='e')

    self.player_location = choice(list(self.world.nodes))

if __name__ == "__main__":
    pass