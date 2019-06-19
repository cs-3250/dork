# -*- coding: utf-8 -*-
'''basic tests for the dork cli'''
import io
from types import FunctionType
from prompt_toolkit.document import Document
import dork.cli as cli


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
                                           + "jumps over the lazy dog."))
    result = callback(0)
    assert isinstance(result, list)
    assert all([isinstance(item, tuple)
                and all([isinstance(subitem, str) for subitem in item])
                for item in result])
