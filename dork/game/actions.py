# -*- coding: utf-8 -*-
"""THE GAME DICTIONARY
"""

__all__ = ['ACTION_CHOICES', 'cry', 'danger_will_robinson',
           'jump', 'move', 'pick', 'run']


def cry(_word_list):
    """crying action stub"""
    response = 'After curling into a ball you cried. Poor you.'
    return response


def danger_will_robinson(word_list):
    """non-implemented stub
    """
    raise NotImplementedError


def jump(_word_list):
    """jumping action stub"""
    response = 'You have jumped, just not sure why.'
    return response


def move(word_list):
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
    direction = directions.get(word_list[0], 'nowhere')

    if direction not in directions:
        return ("Sorry, that is not a direction you can go. " +
                "Type a different command.")
    return "You moved " + direction


def pick(word_list):
    """pick up action stub"""
    response = 'You picked up ' + " ".join(word_list)
    return response


def run(_word_list):
    """running action stub"""
    response = 'You ran in place. Are you just bored?'
    return response


ACTION_CHOICES = {'cry': cry,
                  'go': move,
                  'jump': jump,
                  'run': run,
                  }
