# -*- coding: utf-8 -*-
'''basic tests for the dork cli'''
import io
from types import FunctionType
from pytest import raises
from mock import Mock, patch
from prompt_toolkit.document import Document
import dork.cli as cli
from dork import actions


# to do: test evaluate()
#     test some known commands
# to do: test repl()
#     hmm, how to get to lines below read()...?
#     execution is terminated in read without stdin...
# to do: test lexer (how?)
# to do: test exiting game with ctrl+c / ctrl+d
#     (how? can this even be simulated non-interactively?)


def test_cli_exists(run):
    '''dork.cli.main should always exist and run.'''
    assert "main" in vars(cli), "Dork.cli should define a main method"
    assert isinstance(cli.main, FunctionType)
    try:
        run(cli.main)
    except io.UnsupportedOperation:  # expected
        # prompt_toolkit raises when run non-interactively (e.g. in a test)
        return
    except:  # noqa: E722
        raise AssertionError("cannot run 'dork' command")


def test_cli_help(run):
    '''The CLI's help command should return helpful information.'''
    out, err = run(cli.main, "-h")
    assert "usage: " in out, \
        "Failed to run the cli.main method: {err}".format(err=err)


def test_lexer():
    """ The lexer class for prompt-toolkit should contain the 'lex_document'
        method, which should return a callback function. The callback function
        should take a string and return a list of (str, str) tuples."""
    lexer = cli.SyntaxLexer()
    assert hasattr(lexer, 'lex_document')
    callback = lexer.lex_document(Document("The quick brown fox "
                                           + "jumped over the lazy dog."))
    result = callback(0)
    assert isinstance(result, list)
    assert all([isinstance(item, tuple)
                and all([isinstance(subitem, str) for subitem in item])
                for item in result])


def test_eof():
    '''The game should exit if the input stream is closed.'''
    with patch('dork.cli.prompt', side_effect=EOFError):
        assert cli.read() == "quit game"


def test_keyboard_interrupt():
    '''The game should exit if the user types CTRL+C.'''
    with patch('dork.cli.prompt', side_effect=KeyboardInterrupt):
        assert cli.read() == "quit game"


def test_evaluate():
    """ evaluate() takes a user_input string and should return a tuple
        (bool, str) or (bool, NoneType) indicating whether to exit the REPL
        and any output generated in response to user input. User input
        corresponding to game actions should call those actions and forward
        their output. User input not matching any game action should return
        None as output."""

    action_list = [action.rstrip('_') for action in actions.__dict__
                   if callable(getattr(actions, action))]

    cli.evaluate('quit')
    for action in action_list:
        response = cli.evaluate(action)
        assert isinstance(response, tuple) \
            and isinstance(response[0], bool) \
            and isinstance(response[1], str)

    test_input = ['', "The quick brown fox jumped over the lazy dog."]
    for i in test_input:
        response = cli.evaluate(i)
        assert isinstance(response, tuple) \
            and isinstance(response[0], bool) \
            and isinstance(response[1], type(None))


def test_repl():
    """ REPL should loop until cli.evaluate returns a tuple
        whose first element is True."""
    with patch('dork.cli.prompt'):
        with raises(SystemExit):
            mock_eval = Mock()
            mock_eval.side_effect = [(False, "Went north!"),
                                     (False, None),  # no command entered
                                     (True, "Goodbye.")]
            cli.evaluate = mock_eval
            cli.repl()
