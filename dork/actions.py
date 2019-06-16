# -*- coding: utf-8 -*-
'''Dork CLI commands'''

def move(*args, **kwargs): # example - okay to rewrite or modify
    """move between rooms
        kwargs:
            adverb: list of ways to move (north, up, swiftly, etc.)
            in:     list of places to enter
            to:     list of places to go
    """
    if 'adverbs' in kwargs:
        print("Went " + kwargs['adverbs'] + '!')
    elif 'to' in kwargs:
        print("Went to " + kwargs['to'] + '!')
    else:
        print("Go where?")


def pick_up(*args, **kwargs): # example of a phrasal verb
    """pick up an object
        kwargs:
            direct_object: thing to pick up
    """
    print("Picked it up!")

def quit(*args, **kwargs):
    if not args and not kwargs:
        print("Goodbye.")
        exit(0)
