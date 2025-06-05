from typing import Any


def calc_mean(data):
    """
    Calculate the mean of a list of numbers.
    :param data: List of numbers
    :return: Mean of the numbers
    """
    if not data:
        print("ERROR")
        return
    return sum(data) / len(data)


def calc_median(data):
    """
    Calculate the median of a list of numbers.
    :param data: List of numbers
    :return: Median of the numbers
    """
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    return (
        sorted_data[mid - 1] + sorted_data[mid]
        ) / 2 if n % 2 == 0 else sorted_data[mid]


def calc_quartile(data):
    """
    Calculate the first and third quartiles of a list of numbers.
    :param data: List of numbers
    :return: List containing the first and third quartiles
    """
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    q1 = calc_median(sorted_data[:n // 2])
    q3 = calc_median(sorted_data[(n + 1) // 2:])
    return [q1, q3]


def calc_std(data):
    """
    Calculate the standard deviation of a list of numbers.
    :param data: List of numbers
    :return: Standard deviation of the numbers
    """
    if not data:
        print("ERROR")
        return
    mean = calc_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5


def calc_var(data):
    """
    Calculate the variance of a list of numbers.
    :param data: List of numbers
    :return: Variance of the numbers
    """
    if not data:
        print("ERROR")
        return
    mean = calc_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    supported_operations = {
        "mean": False,
        "median": False,
        "quartile": False,
        "var": False,
        "std": False
    }
    operation_functions = {
        "mean": calc_mean,
        "median": calc_median,
        "quartile": calc_quartile,
        "var": calc_var,
        "std": calc_std
    }

    for _, value in kwargs.items():
        if value in supported_operations:
            supported_operations[value] = True

    for op, should_run in supported_operations.items():
        if should_run:
            result = operation_functions[op](args)
            print(f"{op.capitalize()}: {result}")
    return
