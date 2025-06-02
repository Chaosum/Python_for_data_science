from load_image import ft_load


def main():
    """
    Main function to test the load_image function.
    """

    # Test cases for load_image function
    try:
        print(ft_load("animal.jpeg"))
        print(ft_load("landscape.jpg"))
        print(ft_load("non_existent_file.jpg"))
        print(ft_load("tester.py"))
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
