# -*- coding: utf-8 -*-
# basic entity classes and methods for Dork

__all__ = ["Item", "Holder", "Player", "Room", "Path", "Map"]


class Item: # a holdable/obtainable item

  def __init__(self):
    self.holder = Holder()


class Holder: # a holder/container of items

  def __init__(self):
    self.items = list()


class Player(Holder): # a player or NPC in the game

  def __init__(self):
    super(Player, self).__init__()
    self.room = Room()


class Room(Holder): #a room on the map

  # note: can only be entered through entrances or exited through exits

  def __init__(self):
    super(Room, self).__init__()
    self.map = Map()
    self.entrances = list()
    self.exits = list()
    self.players = list()


class Path: # a path between two rooms (i.e. a door or hallway)

  def __init__(self):
    self.entrance = Room()
    self.exit = Room()


class Map: # a map relating a room's connectivity, as well as the players/items within

  def __init__(self):
    self.rooms = list()
