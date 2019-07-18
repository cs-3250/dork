# -*- coding: utf-8 -*-
"""Pytest Fixtures for Dork unit-tests
"""
import pytest
import dork.objects

pytest_plugins = ["pytester"]  # pylint: disable=invalid-name


@pytest.fixture
def player(room):  # pylint: disable=redefined-outer-name
    """A basic dork player fixture
    """
    return dork.objects.Player(room)


@pytest.fixture
def room():
    """A basic dork room fixture
    """
    return dork.objects.Room('room dummy name')


@pytest.fixture
def holder():
    """A basic dork holder fixture
    """
    return dork.objects.Holder([])


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
