from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """\
Class representing a King that inherits from Baratheon and Lannister.\
"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the King character with a first name and alive status."""
        super().__init__(first_name, is_alive)
        self.title = "King"

    def set_eyes(self, eyes: str):
        """Set the eye color of the King character."""
        if not isinstance(eyes, str):
            raise TypeError("eyes must be a string")
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """Set the hair color of the King character."""
        if not isinstance(hairs, str):
            raise TypeError("hairs must be a string")
        self.hairs = hairs

    def get_eyes(self):
        """Get the eye color of the King character."""
        return self.eyes

    def get_hairs(self):
        """Get the hair color of the King character."""
        return self.hairs
