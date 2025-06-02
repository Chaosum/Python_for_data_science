def shape_me(family: list) -> tuple:
    """
    Returns the shape of the family list as a tuple.

    :param
    family: 2D List of family members.
    :return: Tuple representing the shape of the family list.
    """
    return len(family), len(family[0]) if family else 0


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices the family list from start to end index.

    :param family: 2D List of family members.
    :param start: Starting index for slicing.
    :param end: Ending index for slicing.
    :return: Sliced 2D list of family members.
    """
    if not isinstance(family, list) \
            or not all(isinstance(row, list) for row in family):
        raise ValueError("family {type(family).__name__} it must be a 2D list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError(f"start {type(start)} and end must be integers")
    new_family = family[start:end]
    print(f"My shape is : {shape_me(family)}")
    print(f"My new shape is : {shape_me(new_family)}")
    return new_family
