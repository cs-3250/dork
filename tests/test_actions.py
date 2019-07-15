# -*- coding: utf-8 -*-
'''basic tests for the dork cli-actions'''

from dork.game import actions


def test_cry():
    """testing cry action"""
    response = actions._cry([('really'), ('hard')])
    assert 'cried' in response


def test_danger_will_robinson():
    """testing warning method"""
    try:
        actions._danger_will_robinson([('really'), ('hard')])
    except NotImplementedError:
        pass


def test_jump():
    """testing cry action"""
    response = actions._jump([('really'), ('hard')])
    assert 'jumped' in response


def test_move():
    """testing move action"""
    response = actions._move([('north'), ('really'), ('hard')])
    assert "moved north" in response
    response = actions._move([('really'), ('hard')])
    assert "Sorry" in response


def test_pick():
    """testing pickup action"""
    response = actions._pick([('really'), ('hard')])
    assert "picked up really hard" in response


def test_run():
    """testing run action"""
    response = actions._run([('really'), ('hard')])
    assert "ran" in response
