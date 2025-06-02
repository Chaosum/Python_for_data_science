def give_bmi(height: list[int | float], weight: list[int | float])\
     -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for each pair of height and weight.

    :param height: List of heights in meters.
    :param weight: List of weights in kilograms.
    :return: List of BMI values.
    """
    if height is None or not all(isinstance(h, (int, float)) for h in height):
        raise TypeError(f"{type(height).__name__} object is not a list of int\
 or float.")
    if weight is None or not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError(f"{type(weight).__name__} object is not a list of int\
or float.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")

    bmi = []
    for h, w in zip(height, weight):
        if h <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi_value = w / (h ** 2)
        bmi.append(bmi_value)

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to the BMI values.

    :param bmi: List of BMI values.
    :param limit: The limit to apply.
    :return: List of booleans indicating if each BMI value is above the limit.
    """
    return [b > limit for b in bmi]
