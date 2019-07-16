# -*- coding: utf-8 -*-
'''basic entity classes and methods for Dork'''

__all__ = ["Item", "Holder", "Player", "Treasury",
           "MainHall", "ThroneRoom", "Balcony"]


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
    # def __init__(self):
    # super().__init__()
    # this room will just be changed to the location the player is at
    # self.room = Room()

    # player_list = []
    # gameItem = input("Pick up what? ")
    # player_list.insert(gameItem)
    # gameItem = input("Drop what item ")
    # player_list.remove(gameItem)


class Treasury(Holder):
    '''a room on the map'''

    def __init__(self, name="treasury",
                 description="there are a couple of items in the room, \
                    a sword and a key"):
        super().__init__()
        self.name = name  # name of the room
        self.description = description  # description of the room

        treasury_list = ["sword", "key"]
        # depending on what item they pick it will be removed from
        # this list and added to the player list
        item = input("Which would you like to pick up? the sword or key?")
        treasury_list.remove(item)


class MainHall(Holder):
    '''a room on the map'''

    def __init__(self, name="Main Hall",
                 description="Welcome you dork, look around and hopefully \
                    you'll figure it out all"):
        super().__init__()
        self.name = name  # name of the room
        self.description = description  # description of the room
        # Don't know what item I could add but we can put an item in here
        main_hall_list = []
        main_hall_list.insert()


class ThroneRoom(Holder):
    '''a room on the map'''

    def __init__(self, name="Throne Room",
                 description="Welcome to the throne room, \
                    there is a blonde with a dragon sitting on the throne"):
        super().__init__()
        self.name = name  # name of the room
        self.description = description  # description of the room

        throne_room_list = []
        throne_room_list.insert()


class Balcony(Holder):
    '''a room on the map'''

    def __init__(self, name="Balcony",
                 description="You came across the balcony \
                    and notice how beautiful the outside world"):
        super().__init__()
        self.name = name  # name of the room
        self.description = description  # description of the room

        balcony_list = []
        balcony_list.insert()
