# -*- coding: utf-8 -*-
"""TESTS FOR DORK CLI"""

from types import FunctionType
from dork import cli
from tests.utils import is_a


def test_evaluate():
    """

    Testing user commands in order to determine valid input

    Args:
        None

    Return:
        None

    """
    assert 'jumped' in cli.evaluate('jump')
    assert 'moved north' in cli.evaluate('go north')
    assert 'moved north' in cli.evaluate('go n')
    assert 'moved south' in cli.evaluate('go south')
    assert 'moved south' in cli.evaluate('go s')
    assert 'moved east' in cli.evaluate('go east')
    assert 'moved east' in cli.evaluate('go e')
    assert 'moved west' in cli.evaluate('go west')
    assert 'moved west' in cli.evaluate('go w')
    assert 'ran' in cli.evaluate('run')
    assert 'cried' in cli.evaluate('cry')

    for bad_input in ['',
                      'kick butt',
                      'wrong',
                      'too many words']:
        assert "What are you doing" in cli.evaluate(bad_input)

    for bad_input in ['go die',
                      'go ']:
        assert "I don't understand" in cli.evaluate(bad_input)


def test_parser():
    """

    Tests if parser can handle are any empty and/or missmatched
    inputs from the user

    Args:
        None

    Return:
        None

    """
    assert [("one")] == cli.parser("one")
    assert [("go")] == cli.parser("go ")
    assert [("jump")] == cli.parser("jump")
    assert [('default')] == cli.parser("")
    assert [('default')] == cli.parser(None)


def test_repl(mocker):
    """

    Will test if user input equals to "quit" in order to
    stop running the game

     Args:
        mocker:  simulates user input

    Return:
        None

    """
    mock_input = mocker.patch('builtins.input')
    mock_input.side_effect = [("jump"),
                              ("quit"),
                              ("nope")]
    cli.repl()
    assert mock_input.call_count == 2


def test_cli_exists(run, mocker):
    """

    Checking to see if there is an actual "repl" method in cli.py
    and that it runs appropriately

    Args:
        run: Makes sure that the CLI is running?
        mocker: simulates user input

    Return:
        None

    """
    mock_input = mocker.patch('builtins.input')
    mock_input.side_effect = [("quit")]
    assert "main" in vars(cli), "Dork.cli should define a main method"
    assert isinstance(cli.main, FunctionType)
    run(cli.main)


def test_repl_exists():
    """

    Checking to see if there is an actual "repl" method in cli.py
    and that it runs appropriately

    Args:
        None

    Return:
        None

    """
    assert "repl" in vars(cli)
    is_a(cli.repl, object)


def test_evaluate_exists():
    """

    Checking to see if there is an actual "eval" method in cli.py
    and that it runs appropriately

    Args:
        None

    Return:
        None

    """
    assert "evaluate" in vars(cli)
    is_a(cli.evaluate, object)


def test_parser_exist():
    """

    Checking to see if there is an actual "parser" method in cli.py
    and that it runs appropriately

    Args:
        None

    Return:
        None

    """
    assert "parser" in vars(cli)
    is_a(cli.parser, object)
