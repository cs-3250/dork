# -*- coding: utf-8 -*-
'''basic tests for the dork cli'''
from dork import gamedictionary
from tests.utils import is_a


def test_dictionaries_exist():
    '''The dork module should define an Player.'''
    assert "ACTION" in vars(gamedictionary)
    is_a(gamedictionary.ACTION, dict)
    is_a(gamedictionary.MOVEMENT, dict)
    is_a(gamedictionary.PICK, dict)
