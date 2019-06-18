#Rooms will have an id number for the room.
    #There will be a name for the room.
    #There will be a description of that room.
    #List of connected rooms.
    #list of items in the room.
    #list of NPCs in the room.
    #Need a dictionary of neighbors.
# -*- coding: utf-8 -*-
'''basic entity classes and methods for Dork'''

__all__ = ["Item", "Holder", "Player", "Room", "Path", "Map"]


class Item:
    '''a holdable/obtainable item'''

    def __init__(self):
        self.holder = Holder()


class Holder:
    '''a holder/container of items'''

    def __init__(self):
        self.items = list()


class Player(Holder):
    '''a player or NPC in the game'''  
    def __init__(self):
        super(Player, self).__init__()
        self.room = Room()
        return 


class Room(Holder):
    '''a room on the map'''
    roomid = 0
    def __init__(self, roomid=0, name="A Room", description="An empty room", neighbors={roomid}):
        self.roomid = id # room will have an id number.
        self.name = name # name of the room.
        self.description = description # description of the room.
        self.neighbors = neighbors # dictionary of neighbors.
        return

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def north(self):
        return self._neighbor('n')

    def south(self):
        return self._neighbor('s')

    def east(self):
        return self._neighbor('e')

    def west(self):
        return self._neighbor('w')

    def get_room(self):
    # note: can only be entered through entrances or exited through exits
        return

class Path:
    '''a path between two rooms (i.e. a door or hallway)'''
    def __init__(self):
        self.entrance = Room()
        self.exit = Room()
        self.map = Map()
        self.entrances = list()
        self.exits = list()
        self.players = list()


class Map:
    '''a map relating a room's connectivity and the players/items within it'''

    def __init__(self):
        self.rooms = list()
