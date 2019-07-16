# -*- coding: utf-8 -*-
'''basic entity classes and methods for Dork'''

__all__ = ["Item", "Holder", "Player", "Room"]


class Item:
    '''a holdable/obtainable item'''

    def __init__(self):
        self.holder = Holder()
    
    list = ["sword", "key", "gold", "drug", "note"]


class Holder:
    '''a holder/container of items'''

    def __init__(self):
        self.items = list()

    list = ["sword", "key", "gold", "drug", "note"]    


class Player(Holder):
    '''a player or NPC in the game'''

    def __init__(self):
        super().__init__()
        self.room = Room() #this room will just be changed to the location the player is at 

    list = []
    gameItem = input("Pick up what? ")
    list.insert(gameItem)
    gameItem = input("Drop what item ")
    list.remove(gameItem)




class treasury(Holder):
    '''a room on the map'''

    def __init__(self, name="treasury",
                 description="there are a couple of items in the room, a sword and a key"):
        super().__init__()
        self.name = name  # name of the room
        self.description = description  # description of the room

        list = ["sword", "key"]
        #depending on what item they pick it will be removed from this list and added to the player list
        item = input("Which would you like to pick up? the sword or key?")
        list.remove(item)

class main_hall(Holder):
    '''a room on the map'''

    def __init__(self, name="Main Hall",
                 description="Welcome you dork, look around and hopefully youll figure it out all"):
        super().__init__()
        self.name = name  # name of the room
        self.description = description  # description of the room
        #Don't know what item I could add but we can put an item in here
        list = []
        list.insert()

class throne_room(Holder):
    '''a room on the map'''

    def __init__(self, name="Throne Room",
                 description="Welcome to the throne room, there is a blonde with a dragon sitting on the throne"):
        super().__init__()
        self.name = name  # name of the room
        self.description = description  # description of the room

        list = []
        list.insert()

class balcony(Holder):
    '''a room on the map'''

    def __init__(self, name="Balcony",
                 description="You came across the balcony and notice how beautiful the outside world"):
        super().__init__()
        self.name = name  # name of the room
        self.description = description  # description of the room

        list = []
        list.insert()