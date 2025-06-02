def count_in_list(lst, item):
    """Counts the occurrences of an item in a list."""
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")
    return lst.count(item)
