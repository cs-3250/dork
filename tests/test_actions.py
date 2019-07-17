# -*- coding: utf-8 -*-
'''basic tests for the dork cli-actions'''

from dork.game import actions


def test_cry():
    """testing cry action"""
    response = actions.cry([('really'), ('hard')])
    assert 'cried' in response


def test_danger_will_robinson():
    """testing warning method"""
    try:
        actions.danger_will_robinson([('really'), ('hard')])
    except NotImplementedError:
        pass


def test_jump():
    """testing cry action"""
    response = actions.jump([('really'), ('hard')])
    assert 'jumped' in response


def test_move():
    """testing move action"""
    response = actions.move([('north'), ('really'), ('hard')])
    assert "moved north" in response
    response = actions.move([('really'), ('hard')])
    assert "Sorry" in response


def test_pick():
    """testing pickup action"""
    response = actions.pick([('really'), ('hard')])
    assert "picked up really hard" in response


def test_run():
    """testing run action"""
    response = actions.run([('really'), ('hard')])
    assert "ran" in response
