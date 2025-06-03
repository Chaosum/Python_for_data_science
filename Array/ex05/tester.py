from PIL import UnidentifiedImageError
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def main():
    """Main function to test the image processing functions."""
    try:
        array = ft_load("landscape.jpg")
        if array is None:
            print("The image could not be loaded.")
            return
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
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
