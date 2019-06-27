# -*- coding: utf-8 -*-
'''basic tests for the dork cli'''
import io
from types import FunctionType
from dork import cli

# to do: test evaluate()
#     test some known commands


def test_evaluate():
    """ evaluate() is out of date"""
    assert cli.evaluate('jump') == 'you have jumped'
    assert cli.evaluate('go north') == 'You have moved north'
    assert 'ran' in cli.evaluate('run')
    assert 'crying' in cli.evaluate('cry')
    assert "Sorry" in cli.evaluate('')


def test_repl(mocker):
    """ REPL should loop until user inputs quit"""
    mock_input = mocker.patch('builtins.input')
    mock_input.side_effect = [("jump"),
                              ("quit"),
                              ("nope")]
    cli.repl()
    assert mock_input.call_count == 2  # pylint is a bitch


def test_cli_exists(run, mocker):
    '''dork.cli.main should always exist and run.'''
    mock_input = mocker.patch('builtins.input')
    mock_input.side_effect = [("quit")]
    assert "main" in vars(cli), "Dork.cli should define a main method"
    assert isinstance(cli.main, FunctionType)
    run(cli.main)


def test_repl_exists():
    '''The dork module should define an Player.'''
    assert "repl" in vars(dork.objects)
    is_a(dork.objects.repl, type)


def test_evaluate_exists():
    '''The dork module should define an Player.'''
    assert "evaluate" in vars(dork.objects)
    is_a(dork.objects.evaluate, type)


def test_parser_exist():
    '''The dork module should define an Player.'''
    assert "parser" in vars(dork.objects)
    is_a(dork.objects.parser, type)


def test_cli_help(run):
    '''The CLI's help command should return helpful information.'''
    assert "usage: " in cli.evaluate('help'), \
        "Failed to respond with 'usage: '"
