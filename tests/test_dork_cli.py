# -*- coding: utf-8 -*-
"""Basic tests for the dork cli
"""
import io
from types import FunctionType
import dork.cli


def test_cli_exists(run):
    """Dork.cli.main should always exist and run
    """
    assert "main" in vars(dork.cli), "Dork.cli should define a main method"
    assert isinstance(dork.cli.main, FunctionType)
    try:
        run(dork.cli.main)
    except io.UnsupportedOperation: # expected
        # prompt_toolkit raises when run non-interactively (e.g. in a test)
        return
    except:  # noqa: E722
        raise AssertionError("cannot run 'dork' command")


def test_cli_help(run):
    """CLI's help command should return helpful information
    """
    out, err = run(dork.cli.main, "-h")
    assert "usage: " in out, \
        "Failed to run the cli.main method: {err}".format(err=err)
