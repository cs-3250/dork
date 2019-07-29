# -*- coding: utf-8 -*-
"""GAME ACTIONS"""

from dork.game.game_engine import GameState

__all__ = ['ACTION_CHOICES', 'cry', 'do_action',
           'jump', 'move', 'run', 'load',
           'save', 'help_menu']

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


def help_menu(_word_list):
    """Shows the help menu"""
    response = ''
    print("                                 Help Menu")
    print("""
    How to move: Type in go in addition with a cardinal
    direction. Example: 'go north', 'go south', 'go east' (Case Sensitive).

    If you need to escape from a dangerous situation that cannot be overcome;
    type run and a cardinal direction to escape the danger.

    If the game is making you sad you can type in 'cry' to express your
    feelings and let out all the pain.

    If you feel excited and wish to express your recent achievements type
    'jump' to jump for no apparent reason.

    To save the game at any point just type 'save'.

    To load the game type 'load game_save'

    If at any point you forget these commands during your quest, type in
    'help' to pull up this menu again
    """)
    return response


def do_action(action_name, *args):
    """ action adapter"""
    action = ACTION_CHOICES.get(action_name)
    if action:
        response = action(*args)
        return response
    return 'What are you doing, my friend?'


ACTION_CHOICES = {'cry': cry,
                  'go': move,
                  'move': move,
                  'jump': jump,
                  'run': run,
                  'save': save,
                  'load': load,
                  'help': help_menu}
