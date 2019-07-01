import networkx as nx
import dork.objects as ob
import dork.game_engine as ge

G = nx.Graph()

class World():
    """ Map that relates to the rooms,
        player, and the items
    """
    def __init__(self):
        self.rooms = dict()
        self.players = dict()

def save(file_name = 'dork_save.dp'):
    """ Save game to file """
    print('Saving Game...')
    data = nx.write_yaml(G, file_name)
    print('Game progress has been saved.')

def load(file_name = 'dork_save.dp'):
    """ Load game from file """
    print('Loading Game...\n')
    try:
        with open(file_name):
            data = nx.read_yaml(file_name)
    except IOError:
        return "There was a problem loading your game. Try again."
    return data

def reset_game():

# def player_start_location(self):

# def movement(self, 'nesw'):
#   location = self.player.
#   GameEngine.movement(w)

#   pirateShip = Room()
#   tikiHut = Room()
#   yurt = Room()
#   G.add_nodes_from([pirateShip, tikiHut, yurt])
#   G.add_edge(pirateShip, tikiHut, direction='e')
#   G.add_edge(tikiHut, pirateShip, direction='w')
#   G.add_edge(tikiHut, yurt, direction='s')
#   G.add_edge(yurt, tikiHut, direction='n')
#   tikiHut in G[pirateShip]
#   G.edges[pirateShip, tikiHut]['direction']
#   yurt in G[pirateShip]

# def maze_generation(self):
#   MAZE_BIGNESS = (3, 3)

#   maze = mazelib.Prims(*MAZE_BIGNESS).generate()
#   G = nx.DiGraph()

#   rooms = np.ndarray(shape=[d - 2 for d in maze.shape], dtype=Room)

#   for index, room in np.ndenumerate(rooms):
#       x = index[0]
#       y = index[1]
#       x_maze = x + 1
#       y_maze = y + 1
#       if maze[x_maze, y_maze] == 0:
#           rooms[index] = Room()
#            x_north = x - 1
#            if x_north >= 0 and rooms[(x_north, y)] is not None:
#               G.add_edge(rooms[index], rooms[(x_north, y)], direction='n')
#               G.add_edge(rooms[(x_north, y)], rooms[index], direction='s')
#            y_west = y - 1
#            if y_west >= 0 and rooms[(x, y_west)] is not None:
#               G.add_edge(rooms[index], rooms[(x, y_west)], direction='w')
#               G.add_edge(rooms[(x, y_west)], rooms[index], direction='e')