# -*- coding: utf-8 -*-
"""TESTS FOR DORK CLI"""

from types import FunctionType
from dork import cli
from tests.utils import is_a


# to do: test evaluate()
#     test some known commands


def test_evaluate():
    """ command testing """
    # appropriate responses
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

    # bad inputs
    for bad_input in ['',
                      'kick butt',
                      'wrong',
                      'too many words']:
        assert "What are you doing" in cli.evaluate(bad_input)

    for bad_input in ['go die',
                      'go ']:
        assert "I don't understand" in cli.evaluate(bad_input)


def test_parser():
    """parser should handle empty and missmatched inputs"""
    assert [("one")] == cli.parser("one")
    assert [("go")] == cli.parser("go ")
    assert [("jump")] == cli.parser("jump")
    assert [('default')] == cli.parser("")
    assert [('default')] == cli.parser(None)


def test_repl(mocker):
    """ REPL should loop until user inputs quit"""
    mock_input = mocker.patch('builtins.input')
    mock_input.side_effect = [("jump"),
                              ("quit"),
                              ("nope")]
    cli.repl()
    assert mock_input.call_count == 2


def test_cli_exists(run, mocker):
    '''dork.cli.main should always exist and run.'''
    mock_input = mocker.patch('builtins.input')
    mock_input.side_effect = [("quit")]
    assert "main" in vars(cli), "Dork.cli should define a main method"
    assert isinstance(cli.main, FunctionType)
    run(cli.main)


def test_repl_exists():
    '''The dork module should define an Player.'''
    assert "repl" in vars(cli)
    is_a(cli.repl, object)


def test_evaluate_exists():
    '''The dork module should define an Player.'''
    assert "evaluate" in vars(cli)
    is_a(cli.evaluate, object)


def test_parser_exist():
    '''The dork module should define an Player.'''
    assert "parser" in vars(cli)
    is_a(cli.parser, object)
