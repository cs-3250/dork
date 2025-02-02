# -*- coding: utf-8 -*-
"""GAME ENGINE"""


import yaml


class GameState():

    """Game State"""

    def __init__(self):
        """

        Maze starting

        Args:
            the yaml file that contains our maze will be
            loaded up

        returns:
            the loaded up maze from the yaml file which will
            let the player start out game

        """

        self.load("ypm_maze")
        self.save_file()

    def save_file(self):
        """

        Save game state

        Args:
            An empty yaml file that will be used to save
            the users location within the game

        Returns:
            nothing at the moment

        """
        make_file = "game_save.yml"
        with open(make_file, 'w', encoding='UTF-8') as game_save:
            yaml.safe_dump(self.data, stream=game_save)

    def load(self, file_name):
        """

        Loading in the yaml file

        Args:
            the name of the file the user wishes to save
            their game state as
        Returns:
            that the file was successfully created and their
            game state was saved for the future

        """

        file_in = file_name + ".yml"
        with open(file_in, "r") as file_descriptor:
            self.data = yaml.safe_load(file_descriptor)

    def neighbor_of(self, current_position, direction):
        """

        Checks neighbors for maze

        Args:
            the current position of the user within the
            maze, as well as the direction
            the user wishes to move towards.

        Returns:
            the users new location within the maze as well
            as the direction the user went towards

        """

        current_room = self.data['Map'][current_position]
        return current_room.get(direction)

    def current_position(self):
        """

        Get current position of the player

        Args:
            None

        Returns:
            the users current position within the maze

        """

        return self.data["current_room"]

    def move(self, direction):
        """

        Maze movement

        Args: The direction the user wishes to go towards to

        Returns:
             whether the user is able to move in that direction,
            if the user can move in that direction then the rooms description
            will be displayed if not, the phrase "You have not moved in that
            direction" will be displaced telling the user he wasn't able to
            move in that direction.

        """

        new_room = self.neighbor_of(self.current_position(), direction)
        if new_room:
            self.data['current_room'] = new_room
            return ("You moved " + direction + " into " + new_room + "\n" +
                    self.data.get('Description').get(new_room,
                                                     'Candy Mountain'))
        return "You have not moved " + direction
