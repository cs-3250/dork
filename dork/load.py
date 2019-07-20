# -*- coding: utf-8 -*-
""" Load game state for game """

import yaml


def load(file_name="dork/ypm_maze.yml"):
    """Load in a yaml file, then return its data
    """
    print("Loading previous game. Hold your horses!")

    try:
        load_file = False
        with open(file_name, 'r') as file:
            data = yaml.safe_load(file.read())
            load_file = True
    except (IOError, FileNotFoundError):
        print("ERROR! Invalid file name")
        print("Please try a different file name.")

    print("\n Game loaded successfully. Have fun!\n")
    return data
