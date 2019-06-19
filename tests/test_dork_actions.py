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

NLP = spacy.load('en_core_web_sm')  # language model
DOC = NLP("The brown fox quickly picked the angry dog a flower for Festivus.")
PREDICATE = DOC[3:]
QUICKLY = DOC[3]
PICK = DOC[4]
DOG = DOC[5:8]
FLOWER = DOC[8:10]
FESTIVUS = DOC[11]

PARAMETERS = [{},
              {'predicate':        Arguments(PREDICATE)},
              {'verbs':            Arguments(PICK)},
              {'adverbs':          Arguments(QUICKLY)},
              {'direct objects':   Arguments(FLOWER)},
              {'indirect objects': Arguments(DOG)},
              {'for':              Arguments(FESTIVUS)}
              ]


def test_action_return_types():
    '''Each action function should return either a str or a (bool, str).'''
    for action in ACTION_FUNCTIONS:
        for params in PARAMETERS:
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


def test_action_function_names():
    """ Action functions should not conflict with builtin method names.
        e.g. help, exit, quit, etc."""
    for action in ACTION_FUNCTIONS:
        try:
            assert action.__name__ not in dir(builtins)
        except AssertionError:
            raise NameError(action.__name__ +
                            " conflicts with builtin method of the same name.")
