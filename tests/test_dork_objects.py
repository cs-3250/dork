'''tests for dork game classes'''

from dork.objects import Item, Holder, Player, Room


def test_item():
    '''an Item should have a Holder'''
    item = Item()
    assert isinstance(item_list = item_list)

def test_item_attribute(Item):
        '''The item should have attributes'''
        has_a(Item, "item_list")


def test_holder():
    '''a Holder's items attribute has a (possibly empty) list of Items'''
    holder = Holder()
    assert isinstance(holder.items, list)
    for item in holder.items:
        assert isinstance(item, Item)

def test_holder_attributes(Holder):
        '''test the holder attributes'''
        has_a(Holder, list)


def test_player_is_holder():
    '''a Player is a Holder'''
    assert isinstance(Player.__base__, type(Holder))


def test_player_has_room():
    '''a Player's room is a Room object'''
    player = Player()
    assert isinstance(player.room, Room)

def test_player_attribute(Player):
        '''Test for the player attribute'''
        has_a(Player, "item_List")
        has_a(Player, "room")

def test_room_attribute(Room):
        '''The room should have attributes'''
        has_a(Room, "room_name")
        has_a(Room, "description")
        has_a(Room, list)
