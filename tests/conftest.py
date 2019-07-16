# -*- coding: utf-8 -*-
"""Pytest Fixtures for Dork unit-tests
"""
import pytest
import dork.objects

pytest_plugins = ["pytester"]  # pylint: disable=invalid-name


@pytest.fixture
def player():
    """A basic dork player fixture
    """
    return dork.objects.Player()


@pytest.fixture
def room():
    """A basic dork room fixture
    """
    # return dork.objects.Room()


@pytest.fixture
def run(capsys):
    """CLI run method fixture
    """

    def do_run(main, *args):
        main(*args)
        cap = capsys.readouterr()
        return cap.out, cap.err

    return do_run


@pytest.fixture
def maze():
    """pm maze functionality
    """
    return dork.pm_maze.Maze()
