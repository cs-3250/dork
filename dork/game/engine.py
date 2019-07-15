# -*- coding: utf-8 -*-
""" Game Engine """

from dork.game import actions


class GameEngine:
    '''game engine: stores game map and player location, handles movement'''

    def do_action(self, action_name, *args):
        """ action adapter"""
        action = actions.ACTION_CHOICES.get(
            action_name,
            actions._danger_will_robinson
        )
        response = action(*args)
        return response
