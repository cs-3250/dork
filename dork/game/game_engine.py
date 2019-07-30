# -*- coding: utf-8 -*-
"""GAME ENGINE"""

import yaml


class GameState():
    """Game State"""

    def __init__(self):
        """Maze starting"""
        self.load("ypm_maze")
        self.save_file()

    def save_file(self):
        """Save game state"""
        make_file = "game_save.yml"
        with open(make_file, 'w', encoding='UTF-8') as game_save:
            yaml.safe_dump(self.data, stream=game_save)

    def load(self, file_name):
        """Loading in the yaml file"""
        file_in = file_name + ".yml"
        with open(file_in, "r") as file_descriptor:
            self.data = yaml.safe_load(file_descriptor)

    def neighbor_of(self, current_position, direction):
        """checks neighbors for maze"""
        current_room = self.data['Map'][current_position]
        return current_room.get(direction)

    def current_position(self):
        """get current position of the player"""
        return self.data["current_room"]

    def move(self, direction):
        """maze movement"""
        new_room = self.neighbor_of(self.current_position(), direction)
        if new_room:
            self.data['current_room'] = new_room
            return ("You moved " + direction + " into " + new_room + "\n" +
                    self.data.get('Description').get(new_room,
                                                     'Candy Mountain'))
        return "You have not moved " + direction
