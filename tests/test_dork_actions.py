# -*- coding: utf-8 -*-
'''tests for dork game actions'''
import builtins
import spacy
from dork import actions
from dork.parser import Arguments

# to do: test that each action returns a string
# to do: check that each action tests its parameters
# to do: test that no action names conflict with builtins

ACTION_FUNCTIONS = [getattr(actions, action)
                    for action in actions.__dict__
                    if callable(getattr(actions, action))]

NLP = spacy.load('en_core_web_sm')


def test_action_function_names():
    """ Action functions should not conflict with builtin method names.
        e.g. help, exit, quit, etc."""
    for action in ACTION_FUNCTIONS:
        try:
            assert action.__name__ not in dir(builtins)
        except AssertionError:
            raise NameError(action.__name__ +
                            " conflicts with builtin method of the same name.")


def test_action_return_types():
    '''Each action function should return either a str or a (bool, str).'''

    doc = NLP("The brown fox quickly picked "
              + "the angry dog a flower for Festivus.")
    predicate = doc[3:]
    quickly = doc[3]
    pick = doc[4]
    dog = doc[5:8]
    flower = doc[8:10]
    festivus = doc[11]

    parameters = [{},
                  {'predicate':        Arguments(predicate)},
                  {'verbs':            Arguments(pick)},
                  {'adverbs':          Arguments(quickly)},
                  {'direct_objects':   Arguments(flower)},
                  {'direct_objects':   Arguments(flower)},
                  {'indirect_objects': Arguments(dog)},
                  {'for':              Arguments(festivus)},
                  {'to':               Arguments(flower)}
                  ]

    for action in ACTION_FUNCTIONS:
        for params in parameters:
            return_value = action(**params)
            try:
                assert isinstance(return_value, str) or \
                    (isinstance(return_value, tuple) and
                     isinstance(return_value[0], bool) and
                     isinstance(return_value[1], str))
            except AssertionError:
                raise TypeError(action.__name__ +
                                "() returned " + type(action()).__name__ +
                                "; expected str or (bool, str).")


def test_exit_game():
    """ The following user input should terminate execution of the game:
        quit
        exit
        Exit game.
        Leave game.
        Quit game.
        """

    response = actions.quit_()
    assert isinstance(response, tuple) and response[0]

    response = actions.exit_()
    assert isinstance(response, tuple) and response[0]

    doc = NLP("Exit game.")
    game = doc[1:2]
    response = actions.exit_(predicate=Arguments(game))
    assert isinstance(response, tuple) and response[0]

    doc = NLP("Leave game.")
    game = doc[1:2]
    response = actions.leave(direct_objects=Arguments(game))
    assert isinstance(response, tuple) and response[0]

    doc = NLP("Quit game.")
    game = doc[1:2]
    response = actions.quit_(direct_objects=Arguments(game))
    assert isinstance(response, tuple) and response[0]
