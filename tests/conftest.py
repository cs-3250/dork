# -*- coding: utf-8 -*-
"""PYTEST FIXTURES FOR DORK UNIT TESTS"""

import pytest
import dork

pytest_plugins = ["pytester"]  # pylint: disable=invalid-name


@pytest.fixture
def run(capsys):
    """

    CLI run method fixture

    Args:
        fixture: retrieve stdout and stderr from some code

    Return:
        method closure: Captures the stdout and stderror I/O
        streams of whatever method it gets passed

    """

    def do_run(main, *args):
        main(*args)
        cap = capsys.readouterr()
        return cap.out, cap.err

    return do_run


@pytest.fixture
def maze():
    """

    Functionality for our maze fixture

    Args:
        None

    Return:
        GameState: Calling the GameState to make an instance

    """

    return dork.game.game_engine.GameState()
