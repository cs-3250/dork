"""Tests save and load"""

import os


def check_filepath(file_path):
    """Checks for a valid filepath"""
    # assert for a file path check? If it is correct return the path,
    # if not throw an error message
    return os.path.isfile(file_path)


def test_load():
    """Load should load previous player gamestate"""
    # Add asserts for testing load


def test_save():
    """Save should write current gamestate to a file"""
    # Continue developing later
