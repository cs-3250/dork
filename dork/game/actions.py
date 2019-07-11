# -*- coding: utf-8 -*-
"""THE GAME DICTIONARY
"""

__all__ = ['ACTION_CHOICES', 'PICK', 'MOVEMENT', '_danger_will_robinson',
           '_move']

PICK = {'up': "nothing picked up you have nowhere to put it"
        }

MOVEMENT = {'north': 'You have moved north',
            'n': 'You have moved north',
            'east': 'You have moved east',
            'e': 'You have moved east',
            'south': 'You have moved south',
            's': 'You have moved south',
            'west': 'You have moved west',
            'w': 'You have moved west'
            }

ACTION_CHOICES = {'jump': '_danger_will_robinson',
                  'run': '_danger_will_robinson',
                  'cry': '_danger_will_robinson',
                  'go': '_move',
                  'load': '_load',
                  'save': '_save',
                  'pick': PICK
                  }


def _danger_will_robinson(engine, *args):
    raise NotImplementedError


def _move(direction):
    """ Player movement """
    directions = {'n': 'north',
                  's': 'south',
                  'w': 'west',
                  'e': 'east'}

    if direction not in directions:
        return "Invalid direction! Type a different command."

    return "You are not able to move in that direction. Try again!"
