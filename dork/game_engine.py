import shelve
import maze.yml


class GameEngine:

    def save(self):
        s = shelve.open('dork_save.db')
        s = ['save'] = {}
        s.close()
        print('Game progress has been saved.')

    def load(self):
        print('Loading Game...\n')
        s = shelve.open('dork_save.db')
        if s:
            d = s['save']
        else: 
            print('There is no game saved!')
    
    def reset_game(self):
        # Objects in game set to start
        pass

    def movement(self, direction):
        if direction not in self.room.exist:
          print('Cannot move in that direction!')  
          return
        new_room_name = self.room.exist['room']
        print('Moving to ', new_room_name)
        self.room = world[new_room_name]


   def maze_generation(self):