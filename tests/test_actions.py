# -*- coding: utf-8 -*-
'''basic tests for the dork cli-actions'''

from dork.game import actions


def test_cry():
    """testing cry action"""
    response = actions.cry([('really'), ('hard')])
    assert 'cried' in response


def test_jump():
    """testing cry action"""
    response = actions.jump([('really'), ('hard')])
    assert 'jumped' in response


def test_move():
    """testing move action"""
    response = actions.move([('north'), ('really'), ('hard')])
    assert "moved north" in response
    response = actions.move([('really'), ('hard')])
    assert "I don't understand" in response


def test_pick():
    """testing pickup action"""
    response = actions.pick([('really'), ('hard')])
    assert "picked up really hard" in response


def test_run():
    """testing run action"""
    response = actions.run([('really'), ('hard')])
    assert "ran" in response

def test_load():
    """testing the load method"""
    load = actions.load("dork/ypm_maze.yml")
    assert load is not None

def test_save():
    """testing the save method"""
    # open file
    # check yaml_safe.load()
    # assert if


def test_do_action():
    """testing do action"""
    response = actions.do_action("")
    assert "What are you doing" in response
    response = actions.do_action("jump", "")
    assert "jumped" in response
    response = actions.do_action("jump", [("really"), ("high")])
    assert "jumped" in response
