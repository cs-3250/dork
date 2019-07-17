# -*- coding: utf-8 -*-
""" Game Engine """

from dork.game import actions


def do_action(action_name, *args):
    """ action adapter"""
    action = actions.ACTION_CHOICES.get(
        action_name,
        actions.danger_will_robinson
    )
    response = action(*args)
    return response
