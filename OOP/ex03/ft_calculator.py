class calculator:

    def __init__(self, array):
        # if not isinstance(array, list):
        #     raise TypeError("array must be a list")
        self.array = array

    def __add__(self, object) -> None:
        """Add a number to matrice of shape 1,n."""
        # if not isinstance(object, (int, float)):
        #     raise TypeError("object must be a number")
        new_array = [element + object for element in self.array]
        self.array = new_array
        print(self.array)

    def __mul__(self, object) -> None:
        """Multiply a number with matrice of shape 1,n."""
        # if not isinstance(object, (int, float)):
        #     raise TypeError("object must be a number")
        new_array = [element * object for element in self.array]
        self.array = new_array
        print(self.array)
        return

    def __sub__(self, object) -> None:
        """Subtract a number from matrice of shape 1,n."""
        # if not isinstance(object, (int, float)):
        #     raise TypeError("object must be a number")
        new_array = [element * object for element in self.array]
        self.array = new_array
        print(self.array)
        return

    def __truediv__(self, object) -> None:
        """Divide a number from matrice of shape 1,n."""
        # if not isinstance(object, (int, float)):
        #     raise TypeError("object must be a number")
        if object == 0:
            raise ZeroDivisionError("division by zero")
        new_array = [element / object for element in self.array]
        self.array = new_array
        print(self.array)
        return
