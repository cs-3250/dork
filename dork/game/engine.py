""" Game Engine """

from random import choice
from networkx import read_yaml, write_yaml, DiGraph
from numpy import ndarray, ndenumerate
from mazelib import Prims
from dork.objects import Room
from game.actions import ACTION_CHOICES

class GameEngine:
    '''game engine: stores game map and player location, handles movement'''

    def __init__(self):
        self.world = None
        self.player_location = None

    def do_action(self, action_name, arguments):
        action = ACTION.get(action_name, self._help)
        return action(self, *arguments)

    def _help(self, *args):
        pass
