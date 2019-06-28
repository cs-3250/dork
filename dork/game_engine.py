import shutil


class GameEngine:

    def save(self):
        shutil.copyfile(self.dbfile, args)
        print(('Game progress has been saved.').format(args))

    def load(self):
        pass
    
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
        pass


if __name__ == "__main__":