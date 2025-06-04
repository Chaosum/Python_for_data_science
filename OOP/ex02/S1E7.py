from S1E9 import Character


class Baratheon(Character):
    """Class representing the Baratheon family."""
    def __init__(
            self,
            first_name: str,
            is_alive: bool = True):
        """\
Initialize the Baratheon character with a first name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Kill the Baratheon character"""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the Baratheon character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """\
Return a detailed string representation of the Baratheon character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Class representing the Lannister family."""
    def __init__(
            self,
            first_name: str,
            is_alive: bool = True):
        """\
Initialize a Lannister character with a first name and alive status."""
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be a boolean")
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Create a Lannister character using the class method."""
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be a boolean")
        return cls(first_name, is_alive)

    def die(self):
        """Kill the Lannister character"""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the Lannister character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """\
Return a detailed string representation of the Lannister character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
