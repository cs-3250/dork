# -*- coding: utf-8 -*-
"""THE GAME DICTIONARY
"""

__all__ = ['ACTION_CHOICES', '_cry', '_danger_will_robinson',
           '_jump', '_move', '_pick', '_run']


ACTION_CHOICES = {'cry': '_cry',
                  'go': '_move',
                  'jump': '_jump',
                  'load': '_danger_will_robinson',
                  'pick': '_danger_will_robinson',
                  'run': '_run',
                  'save': '_danger_will_robinson',
                  }


def _cry(self, *args):
    """crying action stub"""
    response = 'After curling into a ball you cried. Poor you.'
    return response


def _danger_will_robinson(engine, *args):
    raise NotImplementedError


def _jump(self, *args):
    """jumping action stub"""
    response = 'You have jumped, just not sure why.'
    return response


def _move(self, direction):
    """ Player movement """
    directions = {'n': 'north',
                  's': 'south',
                  'w': 'west',
                  'e': 'east',
                  'north': 'north',
                  'south': 'south',
                  'west': 'west',
                  'east': 'east',
                  }
    if direction not in directions:
        return "Sorry, you can't go that direction. Type a different command."
    return "You moved " + direction


def _pick(self, *args):
    """pick up action stub"""
    response = 'You picked up ' + args
    return response


def _run(self, *args):
    """running action stub"""
    response = 'You ran in place. Are you just bored?'
    return response
