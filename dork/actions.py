# -*- coding: utf-8 -*-
""" Dork CLI commands

    Functions should return either a string for the REPL to print,
        or a tuple consisting of an exit flag and a string to output.
    An exit flag with a boolean value of True triggers loop termination.

    Function names should consist of verbs only.
    Phrasal verbs like "sit down" are okay.
        But replace spaces with underscores, e.g. sit_down()
    A verb + a noun is not a valid function name.
        Nouns should be handled as parameters.

    If the function name would conflict with a Python built-in method...
        e.g. exit, quit
    then append an underscore to its name to avert a conflict:
        e.g. exit_(), quit_()

    Parser.Arguments objects are passed in by keyword.

    keywords:
        'direct_objects'
        'indirect_objects'
        'adverb'
        {prepositions}, e.g. 'in', 'from', 'to'"""


def move(**kwargs):  # example - okay to rewrite or modify
    """move between rooms
        kwargs:
            adverb: list of ways to move (north, up, swiftly, etc.)
            in:     list of places to enter
            to:     list of places to go
    """
    if 'adverbs' in kwargs:
        return "Went " + kwargs['adverbs'] + '!'
    if 'to' in kwargs:
        return "Went to " + kwargs['to'] + '!'
    return "Go where?"


def pick_up(**kwargs):  # example of a phrasal verb
    """pick up an object
        kwargs:
            direct_object: thing to pick up
    """
    if 'direct_objects' in kwargs:
        return "Picked up " + kwargs['direct_objects'] + '!'
    return "What do you want to pick up?"


def help_(**kwargs):
    '''return help for a given action'''
    if 'verbs' in kwargs:
        return "Let me tell you all about the '" \
            + kwargs['verbs'] + "' command..."
    return "I don't understand what you need help with."


def exit_(**kwargs):
    '''exit game'''
    if not kwargs:
        return quit_(**kwargs)
    # Spacy sees "exit game" as a compound noun
    # entire predicate tested here as a workaround
    if 'predicate' in kwargs and kwargs['predicate'].strip('., ') == "game":
        return quit_(**kwargs)
    return "I don't understand what you want to exit."


def leave(**kwargs):
    '''exit game'''
    if 'direct_objects' in kwargs and kwargs['direct_objects'] == "game":
        return quit_(**kwargs)
    return "I don't understand what you want to leave."


def quit_(**kwargs):
    '''exit game'''
    if not kwargs:
        return True, "Goodbye."
    if 'direct_objects' in kwargs and kwargs['direct_objects'] == "game":
        return True, "Goodbye."
    return "I don't understand what you want to quit."
