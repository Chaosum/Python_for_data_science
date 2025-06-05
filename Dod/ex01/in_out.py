def square(x: int | float) -> int | float:
    """
    Returns the square of the input value.
    Args:
        x (int | float): The value to square.
    Returns:
        int | float: The square of x.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Raises the input value to the power of itself.
    Args:
        x (int | float): The value to exponentiate.
    Returns:
        int | float: The result of x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a closure that applies the given function to the input value
    and raises the result to the power
    of the number of times the closure is called.
    Args:
        x (int | float): The value to process.
        function: A function that takes a single argument.
    Returns:
        object: A closure that applies the function and counts calls.
    """
    count = x

    def inner() -> float:
        """Inner function that applies the function and counts calls."""
        nonlocal count
        count = function(count)
        return count
    return inner
