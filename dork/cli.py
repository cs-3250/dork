# -*- coding: utf-8 -*-
"""DORK CLI"""

from dork.game import actions

__all__ = ["main", "evaluate", "parser", "repl"]


def evaluate(user_input):
    """
    evaluates command for validity

    Args:
        str: Takes user input from parser

    Return:
        str: Based on input from do_action

    """
    words = parser(user_input)
    response = actions.do_action(words[0], words[1:])
    return response


def parser(user_input):
    """
    using gamedictionary, delegates to evaluate()

    Args:
        str: User input

    Return:
        str: Splits into list at white space

    """
    if user_input is None or user_input == "":
        user_input = "default"
    parsed_string = user_input.split()
    return parsed_string


def repl():
    """
    REPL: Read-Eval-Print Loop
        Response based on input from do_action

    Args:
        None

    Return:
        None

    """
    with open("title_screen.txt", encoding="utf8") as file_descriptor:
        contents = file_descriptor.read()
        print(contents)
    room_location = actions.GAMESTATE.current_position()
    output = "Type a command or type 'help' for a list of commands.\n >> \
             " + room_location + "\n >>"
    while True:
        user_input = input(output)
        if 'quit' in user_input:
            print('You have quit.\n Goodbye!')
            break
        else:
            output = evaluate(user_input) + "\n >>"


def main():
    """
    main method to dork

    Args:
        None

    Return:
        None

    """
    repl()
