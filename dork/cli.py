# -*- coding: utf-8 -*-
""" basic Dork CLI
"""
from dork.game.actions import do_action

__all__ = ["main", "evaluate", "parser", "repl"]


def evaluate(user_input):
    """using gamedictionary, provide appropriate command"""
    words = parser(user_input)
    response = do_action(words[0], words[1:])
    return response


def parser(user_input):
    """returns list of words"""
    if user_input is None or user_input == "":
        user_input = "default"
    parsed_string = user_input.split()
    return parsed_string


def repl():
    """REPL: Read-Eval-Print Loop"""
    output = '*This is a title screen*\n'
    while True:
        user_input = input(output)
        if 'quit' in user_input:
            print('You have quit.\n Goodbye!')
            break
        else:
            output = evaluate(user_input) + "\n >>"


def main():
    """main to dork"""
    repl()
