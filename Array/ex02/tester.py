from PIL import UnidentifiedImageError
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
    except ValueError as e:
        print("Value Error occurred:", e)
        return
    except FileNotFoundError as e:
        print("File Not Found Error occurred:", e)
        return
    except UnidentifiedImageError as e:
        print("Unidentified Image Error occurred:", e)
        return
    except Exception as e:
        print("An unexpected error occurred:", e)
        return


if __name__ == "__main__":
    main()
