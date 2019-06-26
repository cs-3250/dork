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
    assert cli.evaluate('go').get('north') == 'You have moved north'
    assert cli.evaluate('jump') == 'you have jumped'
    assert cli.evaluate('jump') == 'you have jumped'


def test_repl(mocker):
    """ REPL should loop until user inputs quit"""
    mock_input = mocker.patch('builtins.input')
    mock_input.side_effect = [("jump"),
                              ("quit"),
                              ("nope")]
    cli.repl()
    assert mock_input.call_count == 2  # pylint is a bitch


def test_cli_exists(run):
    '''dork.cli.main should always exist and run.'''
    assert "main" in vars(cli), "Dork.cli should define a main method"
    assert isinstance(cli.main, FunctionType)
    try:
        run(cli.main)
    except io.UnsupportedOperation:  # expected
        # prompt_toolkit raises when run non-interactively (e.g. in a test)
        pass
    except:  # noqa: E722
        raise AssertionError("cannot run 'dork' command")


def test_cli_help(run):
    '''The CLI's help command should return helpful information.'''
    out, err = run(cli.main, "-h")
    assert "usage: " in out, \
        "Failed to run the cli.main method: {err}".format(err=err)
