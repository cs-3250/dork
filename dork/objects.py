# -*- coding: utf-8 -*-
'''basic entity classes and methods for Dork'''

__all__ = ["Item", "Holder", "Player", "Room"]


class Item:
    '''a holdable/obtainable item'''

    def __init__(self, item_list):
        self.item_list = item_list
    
    list = item_list = ["sword", "key", "gold", "drug", "note"]


class Holder:
    '''a holder/container of items'''

    def __init__(self, Item):
        self.Items = list()   

class Room:
    '''This will be the class all rooms are based out of'''

    def __init__(self, roomName, discription, itemList):
        self.roomName = roomName
        self.discription = discription
        self.itemList = itemList

class Player(Holder):
    '''a player or NPC in the game'''

    def __init__(self, itemList):
        super().__init__()
        self.itemList = itemList

    def pick_up(self, item):
        self.room.items.insert(item)

    def drop_item(self, item):
        self.room.item.reomve(item)

