from array2D import slice_me


def main():
    """
    Main function to test the slice_me function.
    """

    # Test cases for slice_me function
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
        print(slice_me(family, -3, -1))
        print(slice_me(family, 0, 0))
        print(slice_me(family, 0, 100))
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
