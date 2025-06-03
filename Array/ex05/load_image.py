from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path and convert it to a NumPy array.
    Args:
        path (str): The path to the image file.
    Returns:
        np.ndarray: The image as a NumPy array with shape (H, W, 3).
    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the image format is not supported (not JPEG or JPG).
        UnidentifiedImageError: If the file cannot be identified as an image.
        exception: For any other errors that occur during loading.
    """
    try:
        with Image.open(path) as img:
            if img.format not in ["JPEG", "JPG"]:
                raise ValueError("Unsupported image format.")
            img = img.convert("RGB")
            array = np.array(img)
            print("The shape of image is:", array.shape)
            return array
    except FileNotFoundError:
        raise FileNotFoundError(f"The specified image file '{path}'\
 was not found.")
    except UnidentifiedImageError:
        raise UnidentifiedImageError(
            f"Cannot identify file {path} as an image."
        )
    except Exception as e:
        raise Exception(f"An error occurred while loading the image: {e}")
