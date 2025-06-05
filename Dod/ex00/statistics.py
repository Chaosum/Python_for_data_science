from typing import Any


def calc_mean(data):
    """
    Calculate the mean of a list of numbers.
    :param data: List of numbers
    :return: Mean of the numbers
    """
    return sum(data) / len(data)


def calc_median(data):
    """
    Calculate the median of a list of numbers.
    :param data: List of numbers
    :return: Median of the numbers
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    # it should be
    # sorted_data[mid - 1] + sorted_data[mid]) / 2
    # if n % 2 == 0 else sorted_data[mid]
    return sorted_data[mid]


def calc_quartile(data):
    """
    Calculate the first and third quartiles of a list of numbers.
    :param data: List of numbers
    :return: List containing the first and third quartiles
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    q1 = calc_median(sorted_data[:n // 2])
    q3 = calc_median(sorted_data[n // 2:])
    return [q1, q3]


def calc_std(data):
    """
    Calculate the standard deviation of a list of numbers.
    :param data: List of numbers
    :return: Standard deviation of the numbers
    """
    return calc_var(data) ** 0.5


def calc_var(data):
    """
    Calculate the variance of a list of numbers.
    :param data: List of numbers
    :return: Variance of the numbers
    """
    mean = calc_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate and print various statistics for a list of numbers.
    Supported operations: mean, median, quartile, var, std.
    :param args: List of numbers
    :param kwargs: Dictionary of operations to perform
    """

    operation_functions = {
        "mean": calc_mean,
        "median": calc_median,
        "quartile": calc_quartile,
        "var": calc_var,
        "std": calc_std
    }

    for _, operation in kwargs.items():
        try:
            data = list(args)
            if not data:
                raise ValueError("No data provided")
            data = [float(x) for x in data]
            if operation not in operation_functions:
                continue
            result = operation_functions[operation](data)
            print(f"{operation} : {result}")
        except Exception:
            print("ERROR")
            continue
    return
