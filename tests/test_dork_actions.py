# -*- coding: utf-8 -*-
'''tests for dork game actions'''
from dork import actions
# from dork.parser import Arguments

# to do: test that each action returns a string
# to do: check that each action tests its parameters
# to do: test that no action names conflict with builtins


def test_action_return_types():
    '''Each action function should return either a str or a (bool, str).'''
    for action_name in actions.__dict__:
        action = getattr(actions, action_name)
        if callable(action):
            try:
                return_value = action()
                assert isinstance(return_value, str) or \
                    (isinstance(return_value, tuple) and
                     isinstance(return_value[0], bool) and
                     isinstance(return_value[1], str))
            except AssertionError:
                raise TypeError(action_name +
                                "() returned " + type(action()).__name__ +
                                "; expected str or (bool, str).")
