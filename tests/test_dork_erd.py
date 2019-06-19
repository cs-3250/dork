# -*- coding: utf-8 -*-
'''basic tests for state and entity relationships in dork'''
import dork.objects
from tests.utils import has_many, is_a


def test_items_exist():
    '''The dork module should define an Item.'''
    assert "Item" in vars(dork.objects)
    is_a(dork.objects.Item, type)


def test_holders_exist():
    '''The dork module should define an Holder.'''
    assert "Holder" in vars(dork.objects)
    is_a(dork.objects.Holder, type)


def test_players_exist():
    '''The dork module should define an Player.'''
    assert "Player" in vars(dork.objects)
    is_a(dork.objects.Player, type)


def test_rooms_exist():
    '''The dork module should define an Room.'''
    assert "Room" in vars(dork.objects)
    is_a(dork.objects.Room, type)


def test_path_exists():
    '''The dork module should define an Path.'''
    assert "Path" in vars(dork.objects)
    is_a(dork.objects.Path, type)


def test_map_exists():
    '''The dork module should define an Map.'''
    assert "Map" in vars(dork.objects)
    is_a(dork.objects.Map, type)


def test_holder_has_many_items():
    '''A Holder should have many Items.'''
    has_many(dork.objects.Holder, "holder", dork.objects.Item, "items")


def test_player_is_a_holder(player):
    '''A Player should be a Holder.'''
    is_a(player, dork.objects.Holder)


def test_room_is_a_holder(room):
    '''A Room should be a Holder.'''
    is_a(room, dork.objects.Holder)


def test_room_has_many_players():
    '''A Room should have many players.'''
    has_many(dork.objects.Room, "room", dork.objects.Player, "players")


def test_room_has_many_paths():
    '''A Room should have many Paths through exits and entrances.'''
    has_many(dork.objects.Room, "entrance", dork.objects.Path, "entrances")
    has_many(dork.objects.Room, "exit", dork.objects.Path, "exits")


def test_map_has_many_rooms():
    '''A Map should have many Rooms.'''
    has_many(dork.objects.Map, "map", dork.objects.Room, "rooms")
