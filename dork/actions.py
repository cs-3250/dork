# -*- coding: utf-8 -*-
'''Dork CLI commands'''

def move(*args, **kwargs): # example - okay to rewrite or modify
    """move between rooms
        kwargs:
            adverb: which way to move (north, east, south, west, up, down, etc.)
            in:     place to go in
            to:     place to go to
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
