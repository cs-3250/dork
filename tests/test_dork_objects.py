'''tests for dork game classes'''

from dork.objects import Item, Holder, Player, Room


def test_item():
    '''an Item should have a Holder'''
    item = Item("test")
    assert hasattr(item, "name")


def test_holder():
    '''a Holder's items attribute has a (possibly empty) list of Items'''
    holder = Holder(items=[])
    assert isinstance(holder.items, list)
    for item in holder.items:
        assert isinstance(item, Item)


def test_player_is_holder():
    '''a Player is a Holder'''
    assert isinstance(Player.__base__, type(Holder))


def test_player_has_room():
    '''a Player's room is a Room object'''
    room = Room('test')
    player = Player(room)
    assert isinstance(player.room, Room)


def test_room_is_holder():
    '''a Room is a Holder'''
    assert isinstance(Room.__base__, type(Holder))


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
