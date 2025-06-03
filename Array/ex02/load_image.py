from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path and convert it to a NumPy array.
    Args:
        path (str): The path to the image file.
    Returns:
        np.ndarray: The image as a NumPy array with shape (H, W, 3).
        None if the image cannot be loaded.
    """
    try:
        with Image.open(path) as img:
            if img.format not in ["JPEG", "JPG"]:
                raise ValueError("Unsupported image format.")
            img = img.convert("RGB")
            array = np.array(img)
            print("The shape of image is:", array.shape)
            return array
    except ValueError as e:
        print(f"Value error: {e}")
        return None
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except UnidentifiedImageError:
        print(f"Cannot identify file {path} as an image.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the image: {e}")
        return None
