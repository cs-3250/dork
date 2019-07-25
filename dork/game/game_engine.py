# -*- coding: utf-8 -*-
""" Game State """

import yaml


class GameState():
    """Game State"""

    def __init__(self):
        """Maze starting"""
        self.load("dork/ypm_maze.yml")
        self.save_file()

    def save_file(self):
        """Save game state"""
        make_file = "dork/game_save.yml"
        with open(make_file, 'w', encoding='UTF-8') as game_save:
            yaml.safe_dump(self.data, stream=game_save)

    def load(self, file_name):
        """Loading in the yaml file"""
        with open(file_name, "r") as file_descriptor:
            self.data = yaml.safe_load(file_descriptor)

    def save(self):
        """Saving in the yaml file"""

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
        """maze movement"""
        new_room = self.neighbor_of(self.current_position(), direction)
        if new_room:
            self.data['current_room'] = new_room
        return "You moved " + direction
