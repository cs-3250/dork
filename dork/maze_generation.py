import mazelib
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

MAZE_BIGNESS = (3, 3)

MAZE = mazelib.Prims(*MAZE_BIGNESS).generate()
G = nx.DiGraph()

ROOMS = np.ndarray(shape=[d - 2 for d in MAZE.shape])

for index, room in np.ndenumerate(ROOMS):
    x = index[0]
    y = index[1]
    x_maze = x + 1
    y_maze = y + 1
    if MAZE[x_maze, y_maze] == 0:
        ROOMS[index] = ROOMS()
        x_north = x - 1
        if x_north >= 0 and ROOMS[(x_north, y)] is not None:
            G.add_edge(ROOMS[index], ROOMS[(x_north, y)], direction='n')
            G.add_edge(ROOMS[(x_north, y)], ROOMS[index], direction='s')
        y_west = y - 1
        if y_west >= 0 and ROOMS[(x, y_west)] is not None:
            G.add_edge(ROOMS[index], ROOMS[(x, y_west)], direction='w')
            G.add_edge(ROOMS[(x, y_west)], ROOMS[index], direction='e')

print(MAZE)
nx.draw(G)
plt.show()

G = nx.read_yaml('maze.yaml')
