from give_bmi import give_bmi, apply_limit


def main():
    """
    Test the give_bmi and apply_limit functions with sample data.
    """

    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    stringheight = ["2.71", "1.15"]
    heights = [1.75, 1.80, 1.65, 1.80]
    weights = [70, 80, 60, 50, 90]
    limit = 25
    try:
        bmi_values = give_bmi(stringheight, weights)
    except TypeError as e:
        print("Error:", e)
    try:
        bmi_values = give_bmi(heights, weights)
    except ValueError as e:
        print("Error:", e)
    heights.append(0)  # Adding a valid height to match weights length
    try:
        bmi_values = give_bmi(heights, weights)
    except ValueError as e:
        print("Error:", e)
    heights.pop()  # Remove the last height to remove 0
    heights.append(1.75)  # Adding a valid height to match weights length
    try:
        bmi_values = give_bmi(heights, weights)
        print("BMI values:", bmi_values)

        limits_applied = apply_limit(bmi_values, limit)
        print("Limits applied:", limits_applied)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
