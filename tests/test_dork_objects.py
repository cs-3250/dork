'''tests for dork game classes'''
from tests.utils import has_a
from dork.objects import Room, Player


# def test_item():
#     '''an Item should have a Holder'''
#     item = Item("test")
#     assert hasattr(item, "name")


# def test_holder():
#     '''a Holder's items attribute has a (possibly empty) list of Items'''
#     holder = Holder(items=[])
#     assert isinstance(holder.items, list)
#     for item in holder.items:
#         assert isinstance(item, Item)


# def test_player_is_holder(player):
#     '''a Player is a Holder'''
#     assert isinstance(player, Holder)


def test_player_has_room(player):
    '''a Player's room is a Room object'''
    room = Room('test')
    player = Player(room)
    assert isinstance(player.room, Room)


# def test_room_is_holder():
#     '''a Room is a Holder'''
#     assert isinstance(Room.__base__, type(Holder))


def test_room_has_name():
    '''a Room has a nonempty-string name'''
    room = Room(name='test')
    assert isinstance(room.name, str)
    assert room.name  # nonempty


def test_room_has_description():
    '''a Room has a nonempty-string description'''
    room = Room(name='test')
    assert isinstance(room.description, str)
    assert room.description  # nonempty


# def test_player_attribute(player):
#     '''Test for the player attribute'''
#     has_a(player, "items")
#     has_a(player, "room")


def test_room_attribute(room):
    '''The room should have attributes'''
    has_a(room, "name")
    has_a(room, "description")
