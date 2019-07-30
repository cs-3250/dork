# -*- coding: utf-8 -*-
"""GAME ACTIONS"""

from dork.game.game_engine import GameState

__all__ = ['ACTION_CHOICES', 'cry', 'do_action',
           'jump', 'move', 'run', 'load',
           'save', 'help_menu']

GAMESTATE = GameState()


def cry(_word_list):
    """crying action stub - causes no change to game state

    Args:
        _word_list (list): variable-length list of string arguments

    Returns:
        str: output for REPL confirming player curled into ball and cried

    """

    response = 'After curling into a ball you cried. Poor you.'
    return response


def jump(_word_list):
    """jumping action stub - causes no change to game state

    Args:
        _word_list (list): variable-length list of string arguments

    Returns:
        str: output for REPL confirming player jumped

    """

    response = 'You have jumped, just not sure why.'
    return response


def move(word_list):
    """delegate movement to game state instance's move() method

    Args:
        _word_list (list): variable-length list of string arguments
                           the first argument should be the direction

    Returns:
        str: output from game state's move() method or error message

    """

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
    """running action stub - causes no change to game state

    Args:
        _word_list (list): variable-length list of string arguments

    Returns:
        str: output for REPL confirming player ran in place

    """

    response = 'You ran in place. Are you just bored?'
    return response


def load(word_list):
    """delegate loading to the game state instance's load_file() method

    Args:
        _word_list (list): variable-length list of string arguments

    Returns:
        str: output for REPL confirming game loaded

    """

    GAMESTATE.load(word_list[0])
    return 'Game has been loaded'


def save(_word_list):
    """delegate saving to the game state instance's save_file() method

    Args:
        _word_list (list): variable-length list of string arguments

    Returns:
        str: output for REPL confirming game saved

    """

    GAMESTATE.save_file()
    return 'Game has been saved'


def help_menu(_word_list):
    """display the help menu

    Args:
        None

    Returns:
        str: empty string

    """

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
    """action adapter - look up and call action name from ACTION_CHOICES

    Args:
        action_name (str): name of action function to call
        *args: variable-length argument list

    Returns:
        str: output forwarded from corresponding action or error message

    """

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
