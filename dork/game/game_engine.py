# -*- coding: utf-8 -*-
""" Game State """

import yaml


class GameState():
    """Game State"""

    def __init__(self):
        """Maze starting"""
        self.load()

    def load(self):
        """Loading in the yaml file"""
        file_name = "dork/ypm_maze.yml"
        with open(file_name, "r") as file_descriptor:
            self.data = yaml.safe_load(file_descriptor)

    def neighbor_of(self, current_position, direction):
        """checks neighbors for maze"""
        current_room = self.data['Map'][current_position]
        if direction in current_room:
            return current_room[direction]
        return None

    def current_position(self):
        """get current position of the player"""
        return self.data["current_room"] or self.data["start_room"]

    def move(self, direction):
        """Moves player"""
        self.data['current_room'] = \
            self.neighbor_of(self.current_position(), direction)
        return "You moved " + direction
