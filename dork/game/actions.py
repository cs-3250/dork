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


def _cry(word_list):
    """crying action stub"""
    response = 'After curling into a ball you cried. Poor you.'
    return response


def _danger_will_robinson(word_list):
    raise NotImplementedError


def _jump(word_list):
    """jumping action stub"""
    response = 'You have jumped, just not sure why.'
    return response


def _move(word_list):
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


def _pick(word_list):
    """pick up action stub"""
    response = 'You picked up ' + " ".join(word_list)
    return response


def _run(word_list):
    """running action stub"""
    response = 'You ran in place. Are you just bored?'
    return response
