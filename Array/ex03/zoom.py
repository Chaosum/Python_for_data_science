from PIL import UnidentifiedImageError
from matplotlib import pyplot as plt
from load_image import ft_load


def main():
    """
    Main function to load an image, slice it, and display the result.
    It handles various exceptions that may occur during the image loading
    and slicing process.
    """

    try:
        img = ft_load("animal.jpeg")
        print(img)
        zoomed = img[100:500, 450:850, 0]  # 0 1 ou 2 pour R G ou B
        print("New shape after slicing:", zoomed.shape)
        print(zoomed)
        plt.imshow(zoomed, cmap='gray')  # cmap colormap
        plt.show()
    except ValueError as e:
        print("Value Error occurred:", e)
        return
    except FileNotFoundError as e:
        print("File Not Found:", e)
        return
    except UnidentifiedImageError as e:
        print("Unidentified Image Error:", e)
    except Exception as e:
        print(f"An error occurred: {e}")
    return


if __name__ == "__main__":
    main()
