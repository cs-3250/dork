# -*- coding: utf-8 -*-
'''basic entity classes and methods for Dork'''

__all__ = ["Item", "Holder", "Player", "Room"]


class Item:
    '''a holdable/obtainable item'''

     def __init__(self, name):
        self.name = name

class Holder:
    '''a holder/container of items'''

     def __init__(self, items):
        self.items = items

class Room(Holder):
    '''This will be the class all rooms are based out of'''

   def __init__(self, name, description='', items=[]):
        super().__init__(items=items)
        self.name = name
        self.description = description
        self.exits = []

class Player(Holder):
    '''a player or NPC in the game'''

     def __init__(self, room, items=[]):
        super().__init__(items=items)
        self.room = room

    def pick_up(self, item):
        self.room.items.remove(item)
        self.items.append(item)

    def drop_item(self, item):
        self.room.items.append(item)
        self.items.remove(item)