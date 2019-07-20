# -*- coding: utf-8 -*-
""" Load in a yaml file test """

from dork.load import load


def test_load():
    """ Testing the load method """
    assert isinstance(load.load(), dict)
