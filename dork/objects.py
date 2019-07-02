# Rooms will have an id number for the room.
# There will be a name for the room.
# There will be a description of that room.
# List of connected rooms.
# list of items in the room.
# list of NPCs in the room.
# Need a dictionary of neighbors.
# -*- coding: utf-8 -*-
'''basic entity classes and methods for Dork'''


__all__ = ["Item", "Holder", "Player", "Room"]


class Item:
    '''a holdable/obtainable item'''

    def __init__(self):
        self.holder = Holder()


class Holder:
    '''a holder/container of items'''

    def __init__(self):
        self.items = list()


class Player(Holder):
    """a player or NPC in the game"""

    def __init__(self):
        super().__init__()
        self.room = Room()


class Room(Holder):
    '''a room on the map'''
    roomid = 0

    def __init__(self, name="a room",
                 description="an empty room"):
        super().__init__()
        self.name = name  # name of the room
        self.description = description  # description of the room
