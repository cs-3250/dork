# -*- coding: utf-8 -*-
""" basic Dork CLI
"""
from dork.game.engine import GameEngine as ge

__all__ = ["main", "evaluate", "parser", "repl"]


def evaluate(user_input):
    '''using gamedictionary, provide appropriate command'''
    words = parser(user_input)
    response = ge.do_action(words[0], words[1:])
    return response


def parser(user_input):
    '''returns list of words'''
    if user_input is None:
        user_input = "default default"
    parsed_string = user_input.split()
    if len(parsed_string) == 1:
        if parsed_string[0] in {'go', 'pick'}:
            parsed_string.extend(['default'])
    return parsed_string


def repl():
    ''' REPL: Read-Eval-Print Loop '''
    output = '*This is a title screen*\n'
    while True:
        user_input = input(output)
        if 'quit' in user_input:
            print('You have quit.\n Goodbye!')
            break
        else:
            output = evaluate(user_input) + "\n >>"


def main():
    ''' main to dork '''
    repl()
