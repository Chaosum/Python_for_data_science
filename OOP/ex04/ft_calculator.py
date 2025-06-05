class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""
        # if not isinstance(V1, list) or not isinstance(V2, list):
        #     raise TypeError("Both inputs must be lists")
        # if not all(isinstance(x, (int, float)) for x in V1) \
        #         or not all(isinstance(y, (int, float)) for y in V2):
        #     raise TypeError("Both vectors must contain only numbers")
        # if len(V1) != len(V2):
        #     raise ValueError("Vectors must be of the same length")
        print(f"Dot product is : {sum(x * y for x, y in zip(V1, V2))}")
        return

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise."""
        # if not isinstance(V1, list) or not isinstance(V2, list):
        #     raise TypeError("Both inputs must be lists")
        # if not all(isinstance(x, (int, float)) for x in V1) \
        #         or not all(isinstance(y, (int, float)) for y in V2):
        #     raise TypeError("Both vectors must contain only numbers")
        # if len(V1) != len(V2):
        #     raise ValueError("Vectors must be of the same length")
        print(f"Add Vectors is : {[x + y for x, y in zip(V1, V2)]}")
        return

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts two vectors element-wise."""
        # if not isinstance(V1, list) or not isinstance(V2, list):
        #     raise TypeError("Both inputs must be lists")
        # if not all(isinstance(x, (int, float)) for x in V1) \
        #         or not all(isinstance(y, (int, float)) for y in V2):
        #     raise TypeError("Both vectors must contain only numbers")
        # if len(V1) != len(V2):
        #     raise ValueError("Vectors must be of the same length")
        print(f"Sous Vectors is : {[x - y for x, y in zip(V1, V2)]}")
        return
