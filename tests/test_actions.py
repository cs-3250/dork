# -*- coding: utf-8 -*-
'''TESTS FOR DORK CLI'''

from dork.game import actions


def test_cry():
    """

    Test calling cry action generates appropriate output

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: if output does not contain 'cried'

    """

    response = actions.cry([('really'), ('hard')])
    assert 'cried' in response


def test_jump():
    """

    Test calling jump action generates appropriate output

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: if output does not contain 'jumped'

    """

    response = actions.jump([('really'), ('hard')])
    assert 'jumped' in response


def test_move():
    """

    Test calling move action generates appropriate output

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError:
            if output for input "move north really hard"
                does not contain "moved north"
            if output for input "move really hard"
                does not contain "I don't understand"

    """

    response = actions.move([('north'), ('really'), ('hard')])
    assert "moved north" in response
    response = actions.move([('really'), ('hard')])
    assert "I don't understand" in response


def test_run():
    """

    Test calling run action generates appropriate output

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: if output does not contain 'ran'

    """

    response = actions.run([('really'), ('hard')])
    assert "ran" in response


def test_load():
    """

    Test calling load action returns non-empty output

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: if actions.load(["ypm_maze")] returns None

    """

    load = actions.load([("ypm_maze")])
    assert load is not None


def test_save():
    """

    Test calling save action returns non-empty output

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: if actions.save("this is silly")] returns None

    """

    response = actions.save("this is silly")
    assert response is not None


def test_help_menu():
    """

    Test calling help menu returns non-empty output

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: if actions.help_menu("Stuff")] returns None

    """

    response = actions.help_menu("Stuff")
    assert response is not None


def test_do_action():
    """

    Test do_action reacts to empty input, calls actions as appropriate

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError:
            if response to empty input does not contain "What are you doing"
            if output for input "jump" does not contain "jumped"
            if output for input "jump really high" does not contain "jumped"

    """

    response = actions.do_action("")
    assert "What are you doing" in response
    response = actions.do_action("jump", "")
    assert "jumped" in response
    response = actions.do_action("jump", [("really"), ("high")])
    assert "jumped" in response
