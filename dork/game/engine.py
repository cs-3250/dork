# -*- coding: utf-8 -*-
""" Game Engine """

from dork.game import actions


class GameEngine:
    '''game engine: stores game map and player location, handles movement'''

    def do_action(self, action_name, *kwargs):
        """ action adapter"""
        action = actions.ACTION_CHOICES.get(action_name)
        return action(self, *kwargs)
