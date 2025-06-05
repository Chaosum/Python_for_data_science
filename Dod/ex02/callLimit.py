def callLimit(limit):
    """
    Decorator to limit the number of times a function can be called.
    :param limit: Maximum number of times the function can be called
    :return: Decorated function that limits calls
    """
    count = 0
    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")

    def callLimiter(func):
        """
        Inner function that wraps the original function to limit calls.
        :param func: Function to be decorated
        :return: Wrapped function that checks call limit
        """
        if not callable(func):
            raise TypeError("func must be callable")

        def limit_function(*args, **kwargs):
            """
            Function that checks the call count and limits calls.
            :param args: Positional arguments for the original function
            :param kwargs: Keyword arguments for the original function
            :return: Result of the original function if limit not exceeded
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {func} call too many times")
            else:
                count += 1
                return func(*args, **kwargs)
        return limit_function

    return callLimiter
