from ft_filter import ft_filter


def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0


def main():
    """Main function to demonstrate the ft_filter functionality."""
    # if len(argv) != 3:
    #     print("Usage: python filterstring.py <string>")
    #     return
    print(filter.__doc__)
    print(ft_filter.__doc__)
    if filter.__doc__ != ft_filter.__doc__:
        print("Differences between __doc__ strings")
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original array:", array)
    filtered = ft_filter(lambda x: x % 2 == 0, array)
    print("Filtered array Odd numbers :\n", list(filtered))
    filtered = ft_filter(is_even, array)
    print("Filtered array Even numbers :\n", list(filtered))
    return


if __name__ == "__main__":
    main()
