# -*- coding: utf-8 -*-
"""THE GAME DICTIONARY
"""
from dork.game.game_engine import GameState

__all__ = ['ACTION_CHOICES', 'cry', 'do_action',
           'jump', 'move', 'pick', 'run', 'load',
           'save']

GAMESTATE = GameState()


def cry(_word_list):
    """crying action stub"""
    response = 'After curling into a ball you cried. Poor you.'
    return response


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
    if not word_list or word_list[0] not in directions:
        return ("I don't understand where you're trying to go. " +
                "Type a different command")
    direction = directions.get(word_list[0])
    return GAMESTATE.move(direction)


def pick(word_list):
    """pick up action stub"""
    response = 'You picked up ' + " ".join(word_list)
    return response


def run(_word_list):
    """running action stub"""
    response = 'You ran in place. Are you just bored?'
    return response


def load(word_list):
    """Loading in a yaml file"""
    GAMESTATE.load(word_list[0])
    return 'Game has been loaded'


def save(_word_list):
    """Saving a yaml the file"""
    GAMESTATE.save_file()
    return 'Game has been saved'


def do_action(action_name, *args):
    """ action adapter"""
    action = ACTION_CHOICES.get(action_name)
    if action:
        response = action(*args)
        return response
    return 'What are you doing, my friend?'


ACTION_CHOICES = {'cry': cry,
                  'go': move,
                  'jump': jump,
                  'run': run,
                  'save': save,
                  'load': load}
