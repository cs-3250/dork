""" basic Dork CLI

-MH 06/22/2019 - 12:27pm #########################################

*** For now *** if you change something, leave a comment of the thought you
are trying to convey so others can understand the same logic.

-Needs to:
    -be able to have a dictionary for parsing.
    -Have a quit function
    -Be able to perform actions and have cardinal directions.
    -Have a REPL.
-Currently needs:
-Object interaction
    -A way for player movement
        -N, S, E, W
    -Game commands
        -Quit
        -Start-Save-Load
Definition of done:
    -Create test cases for actions in REPL
    -Added actions into CLI dictionaries

"""
from dork import gamedictionary as gd
from dork.game import engine

__all__ = ["main", "evaluate", "parser", "repl"]


def evaluate(user_input, engine):
    '''using gamedictionary, provide appropriate command'''
    words = parser(user_input)
    response = engine.do_action(words[0], words[1:])
    return response


def parser(user_input):
    '''returns list of words'''
    if user_input is None:
        user_input = " "
    parsed_string = user_input.split()
    if len(parsed_string) == 1:
        if parsed_string[0] in {'go', 'pick'}:
            parsed_string.extend(['default'])
    return parsed_string


def repl(ge):
    ''' REPL: Read-Eval-Print Loop '''
    output = '*This is a title screen*\n'
    while True:
        user_input = input(output)
        if 'quit' in user_input:
            print('You have quit.\n Goodbye!')
            break
        else:
            output = evaluate(user_input, ge) + "\n >>"


def main():
    ''' main to dork '''
    ge = game_engine()
    repl(ge)
