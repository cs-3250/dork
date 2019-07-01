import mazelib
import networkx as nx
from numpy import ndarray, ndenumerate

from dork.objects import Room

class GameEngine:

    def __init__(self):
        self.world = None

    def save(self):
        G = nx.write_yaml('dork_save.dp')

        s.close()
        print('Game progress has been saved.')

    def load(self):
        print('Loading Game...\n')

        #if: # FIXME commented out for now, because syntax error. - Casey

        #else:
            #print('There is no game saved!')

    def reset_game(self):
        # Objects in game set to start
        pass

    def movement(self, direction):
        #
        #
        #
        #
        if direction not in self.world:
            # FIXME self.world contains Rooms - not directions
            # it's the edges of the individual nodes that have edge attributes
            # you need to check the edges coming out from the current location
            # see: https://stackoverflow.com/a/33252014/837710
            # Please delete my comments once you fix this stuff. ;)
            # - Casey
            print('Cannot move in that direction!')
            return
        new_room_name = self.world['room']
        # FIXME this is close, but our graph is indexed by objects - not strings
        # so you could look up a node like self.world[RoomObject]
        # but the problem is that we don't have a reference to that Room yet
        # you need to find the right edge, and that will point to it
        # - Casey
        print('Moving to ', new_room_name)
        self.room = world[new_room_name]
        # this should work once you fix line 42
        # - Casey


    def maze_generation(self, size=(3, 3)):

        maze = mazelib.Prims(*size).generate()
        G = nx.DiGraph()

        self.world = ndarray(shape=[d - 2 for d in maze.shape], dtype=Room)

        for index, room in ndenumerate(self.world):
            x = index[0]
            y = index[1]
            x_maze = x + 1
            y_maze = y + 1
            if maze[x_maze, y_maze] == 0:
                self.world[index] = Room()
                x_north = x - 1
                if x_north >= 0 and self.world[(x_north, y)] is not None:
                    G.add_edge(self.world[index],
                               self.world[(x_north, y)],
                               direction='n')
                    G.add_edge(self.world[(x_north, y)],
                               self.world[index],
                               direction='s')
                y_west = y - 1
                if y_west >= 0 and self.world[(x, y_west)] is not None:
                    G.add_edge(self.world[index],
                               self.world[(x, y_west)],
                               direction='w')
                    G.add_edge(self.world[(x, y_west)],
                               self.world[index],
                               direction='e')
