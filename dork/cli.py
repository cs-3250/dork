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

__all__ = ["main", "evaluate", "parser", "repl"]


def evaluate(user_input):
    '''evaluate user CLI input'''
    parsed_input = parser(user_input)
    game_response = gd.ACTION.get(parsed_input[0])
    if game_response is None:
        game_response = 'Im Sorry. I didnt understand what you said.'
    elif len(parsed_input) > 1:
        game_response = gd.ACTION.get(parsed_input[0]).get(parsed_input[1])
    return game_response


def parser(user_input):
    '''to do parse text, move action to first, find object and make second'''
    if len(user_input) < 1:
        parsed_string = " "
    else:
        parsed_string = user_input.split()
    return parsed_string


def repl():
    ''' REPL: Read–Eval–Print Loop '''
    output = '*This is a title screen*\n'
    while True:
        user_input = input(output)
        if 'quit' in user_input:
            print('You have quit.  Goodbye!')
            break
        else:
            output = evaluate(user_input)


def main():
    ''' main to dork '''
    repl()


if __name__ == "__main__":
    repl()
