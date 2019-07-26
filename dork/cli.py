# -*- coding: utf-8 -*-
"""DORK CLI"""

from dork.game import actions

__all__ = ["main", "evaluate", "parser", "repl"]


def evaluate(user_input):
    """using gamedictionary, provide appropriate command"""
    words = parser(user_input)
    response = actions.do_action(words[0], words[1:])
    return response


def parser(user_input):
    """returns list of words"""
    if user_input is None or user_input == "":
        user_input = "default"
    parsed_string = user_input.split()
    return parsed_string


def repl():
    """REPL: Read-Eval-Print Loop"""
    with open("title_screen.txt", encoding="utf8") as file_descriptor:
        contents = file_descriptor.read()
        print(contents)
    output = "Type a command or type 'help' for a list of commands.\n >>"
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
