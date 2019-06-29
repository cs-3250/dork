# -*- coding: utf-8 -*-
'''basic tests for the dork cli'''
from types import FunctionType
from dork import cli
from tests.utils import is_a


# to do: test evaluate()
#     test some known commands


def test_evaluate():
    """ evaluate() is out of date"""
    # appropriate responses
    assert cli.evaluate('jump') == 'you have jumped'
    assert cli.evaluate('go north') == 'You have moved north'
    assert cli.evaluate('go n') == 'You have moved north'
    assert cli.evaluate('go south') == 'You have moved south'
    assert cli.evaluate('go s') == 'You have moved south'
    assert cli.evaluate('go east') == 'You have moved east'
    assert cli.evaluate('go e') == 'You have moved east'
    assert cli.evaluate('go west') == 'You have moved west'
    assert cli.evaluate('go w') == 'You have moved west'
    assert 'ran' in cli.evaluate('run')
    assert 'crying' in cli.evaluate('cry')
    assert "load" in cli.evaluate('load')
    assert "save" in cli.evaluate('save')
    assert "picked up" in cli.evaluate('pick up')

    # bad inputs
    assert "Sorry" in cli.evaluate('')
    assert "Sorry" in cli.evaluate('kick butt')
    assert "Sorry" in cli.evaluate('wrong')
    assert "Sorry" in cli.evaluate('too many words')
    assert "Sorry" in cli.evaluate('go die')


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


def test_cli_help():
    '''The CLI's help command should return helpful information.'''
    assert "usage: " in cli.evaluate('help'), \
        "Failed to respond with 'usage: '"
