from matplotlib import pyplot as plt
from numpy import ndarray


def ft_invert(array) -> ndarray:
    """    Invert the colors of the given array.
    Args:
        array (np.ndarray): The input array containing RGB values.
    Returns:
        np.ndarray: An array with inverted RGB values.
    """
    if not isinstance(array, ndarray):
        raise TypeError("Input must be a numpy ndarray.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("Input array must be of shape (H, W, 3) for RGB.")
    inverted_array = 255 - array
    plt.imshow(inverted_array)
    plt.show()
    return inverted_array


def ft_red(array) -> ndarray:
    """    Filter the red channel from the given array.
    Args:
        array (np.ndarray): The input array containing RGB values.
    Returns:
        np.ndarray: An array with only the red channel values,
            setting green and blue channels to zero.
    """
    if not isinstance(array, ndarray):
        raise TypeError("Input must be a numpy ndarray.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("Input array must be of shape (H, W, 3) for RGB.")
    filtered_array = array.copy()
    filtered_array[:, :, 1] = 0
    filtered_array[:, :, 2] = 0
    plt.imshow(filtered_array)
    plt.show()
    return filtered_array


def ft_green(array) -> ndarray:
    """    Filter the green channel from the given array.
    Args:
        array (np.ndarray): The input array containing RGB values.
    Returns:
        np.ndarray: An array with only the green channel values,
        setting red and blue channels to zero.
    """
    if not isinstance(array, ndarray):
        raise TypeError("Input must be a numpy ndarray.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("Input array must be of shape (H, W, 3) for RGB.")
    filtered_array = array.copy()
    filtered_array[:, :, 0] = 0
    filtered_array[:, :, 2] = 0
    plt.imshow(filtered_array)
    plt.show()
    return filtered_array


def ft_blue(array) -> ndarray:
    """    Filter the blue channel from the given array.
    Args:
        array (np.ndarray): The input array containing RGB values.
    Returns:
        np.ndarray: An array with only the blue channel values,
        setting red and green channels to zero.
    """
    if not isinstance(array, ndarray):
        raise TypeError("Input must be a numpy ndarray.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("Input array must be of shape (H, W, 3) for RGB.")
    filtered_array = array.copy()
    filtered_array[:, :, 0] = 0  # Set red channel to zero
    filtered_array[:, :, 1] = 0  # Set green channel to zero
    plt.imshow(filtered_array)
    plt.show()
    return filtered_array


def ft_grey(array) -> ndarray:
    """    Convert the given array to grayscale.
    Args:
        array (np.ndarray): The input array containing RGB values.
    Returns:
        np.ndarray: An array with grayscale values.
    """
    if not isinstance(array, ndarray):
        raise TypeError("Input must be a numpy ndarray.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("Input array must be of shape (H, W, 3) for RGB.")
    grey_array = array.mean(axis=2, keepdims=True).astype(array.dtype)
    # Repeat the grey channel to match RGB shape
    grey_array = grey_array.repeat(3, axis=2)
    plt.imshow(grey_array)
    plt.show()
    return grey_array
