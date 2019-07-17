'''tests for dork game classes'''
from tests.utils import has_a
from dork.objects import Holder, Room


def test_player_is_holder(player):
    '''a Player is a Holder'''
    assert isinstance(player, Holder)


def test_player_has_room(player):
    '''a Player's room is a Room object'''
    assert isinstance(player.room, Room)


def test_player_attribute(player):
    '''Test for the player attribute'''
    has_a(player, "items")
    has_a(player, "room")


def test_room_attribute(room):
    '''The room should have attributes'''
    has_a(room, "name")
    has_a(room, "description")
