# -*- coding: utf-8 -*-
"""Pytest Fixtures for Dork unit-tests
"""
import pytest
import dork

pytest_plugins = ["pytester"]  # pylint: disable=invalid-name


@pytest.fixture
def run(capsys):
    """CLI run method fixture
    """

    def do_run(main, *args):
        main(*args)
        cap = capsys.readouterr()
        return cap.out, cap.err

    return do_run
