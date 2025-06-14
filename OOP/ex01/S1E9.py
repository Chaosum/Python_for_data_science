from abc import ABC, abstractmethod


class Character(ABC):
    """Class to represent a generic character. Abstract class."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a character with a first name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """method to kill the character"""
        self.is_alive = False


class Stark(Character):
    """Class to represent a Stark character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Stark character with a first name and alive status."""
        super().__init__(first_name, is_alive)
