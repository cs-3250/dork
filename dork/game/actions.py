"""THE GAME DICTIONARY
"""
__all__ = ['ACTION_CHOICE', 'PICK']

PICK = {'up': "nothing picked up you have nowhere to put it"
        }

MOVEMENT = {'north': 'You have moved north',
           'n': 'You have moved north',
           'east': 'You have moved east',
           'e': 'You have moved east',
           'south': 'You have moved south',
           's': 'You have moved south',
           'west': 'You have moved west',
           'w': 'You have moved west'
           }

ACTION_CHOICES = {'jump': '_danger_will_robinson',
          'run': _danger_will_robinson,
          'cry': _danger_will_robinson,
          'go': _move,
          'load': _load,
          'save': _save,
          'pick': PICK
          }

def _danger_will_robinson(engine, *args):
        raise NotImplementedError

def _save(engine, file_name='dork_world.yml'):
        """ Save game to file """
        print('Saving Game...')
        write_yaml(self.world, file_name)
        return "Game progress has been saved."

def _load(self, file_name='dork_world.yml'):
        """ Load game from file """
        print("Loading Game...\n")
        try:
                world = read_yaml(file_name)
        except FileNotFoundError:
                return "No such file!"
        if isinstance(world, DiGraph):
                self.world = world
                return "World has been loaded."
        return "Error loading world!"

def _move(self, direction):
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
                return "You went " + directions[direction] + "."

        return "You are not able to move in that direction. Try again!"

def _maze_generation(self, size=(3, 3)):
        """ Random maze generation """

        maze = Prims(*size).generate()
        rooms = ndarray(shape=[d - 2 for d in maze.shape], dtype=Room)
        self.world = DiGraph()

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
