def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        function = bool
    elif not callable(function):
        raise TypeError(f"'{type(function).__name__}' object is not callable")
    yield [item for item in iterable if function(item)]
