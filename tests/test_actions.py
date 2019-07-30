# -*- coding: utf-8 -*-
'''TESTS FOR DORK CLI'''

from dork.game import actions


def test_cry():
    """test calling cry action generates appropriate output

    Args:
        None

    Returns:
        None

    """

    response = actions.cry([('really'), ('hard')])
    assert 'cried' in response


def test_jump():
    """test calling jump action generates appropriate output

    Args:
        None

    Returns:
        None

    """

    response = actions.jump([('really'), ('hard')])
    assert 'jumped' in response


def test_move():
    """test calling move action generates appropriate output

    Args:
        None

    Returns:
        None

    """

    response = actions.move([('north'), ('really'), ('hard')])
    assert "moved north" in response
    response = actions.move([('really'), ('hard')])
    assert "I don't understand" in response


def test_run():
    """test calling run action generates appropriate output

    Args:
        None

    Returns:
        None

    """

    response = actions.run([('really'), ('hard')])
    assert "ran" in response


def test_load():
    """test calling load action returns non-empty output

    Args:
        None

    Returns:
        None

    """

    load = actions.load([("ypm_maze")])
    assert load is not None


def test_save():
    """test calling save action returns non-empty output

    Args:
        None

    Returns:
        None

    """

    response = actions.save("this is silly")
    assert response is not None


def test_help_menu():
    """test calling help menu returns non-empty output

    Args:
        None

    Returns:
        None

    """

    response = actions.help_menu("Stuff")
    assert response is not None


def test_do_action():
    """test do_action reacts to empty input, calls actions as appropriate

    Args:
        None

    Returns:
        None

    """

    response = actions.do_action("")
    assert "What are you doing" in response
    response = actions.do_action("jump", "")
    assert "jumped" in response
    response = actions.do_action("jump", [("really"), ("high")])
    assert "jumped" in response
