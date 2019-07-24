# -*- coding: utf-8 -*-
"""basic entity classes and methods for Dork"""

__all__ = ["Player"]


# class Item:
#     '''a holdable/obtainable item'''

#     def __init__(self, name):
#         self.name = name


# class Holder:
#     '''a holder/container of items'''

#     def __init__(self, items):
#         self.items = items


class Room():
    """This will be the class all rooms are based out of"""

    def __init__(self, name, description='Looks like a room.'):
        self.name = name
        self.description = description
        self.exits = []


class Player():
    '''a player or NPC in the game'''

    def __init__(self, room):
        self.room = room

    # def pick_up(self, item):
    #     """pick up an item from the player's current room"""
    #     self.room.items.remove(item)
    #     self.items.append(item)

    # def drop(self, item):
    #     """drop up an item into the player's current room"""
    #     self.room.items.append(item)
    #     self.items.remove(item)
