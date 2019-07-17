# -*- coding: utf-8 -*-
'''basic entity classes and methods for Dork'''

__all__ = ["Item", "Holder", "Player", "Room"]


class Item:
    '''a holdable/obtainable item'''

    def __init__(self, item_list):
        self.Item = Item
        self.item_list = item_list

class Holder:
    '''a holder/container of items'''

    def __init__(self, item):
        self.Holder = Holder
        self.items = item = list = ['sword']

class Room:
    '''This will be the class all rooms are based out of'''

    def __init__(self, room_Name, description, item_List):
        self.room_Name = room_Name
        self.description = description
        self.item_List = item_List = list = ['example'] 

class Player(Holder):
    '''a player or NPC in the game'''

    def __init__(self, item_List, room):
        super().__init__()
        self.item_List = itemList
        self.room = room

    def pick_up(self, item):
        self.room.items.remove(item)
        self.items.append(item)

    def drop_item(self, item):
        self.room.item.reomve(item)

