from matplotlib import pyplot as plt
from load_image import ft_load


def rotate_matrix_90(matrix):
    """Rotate a 2D matrix by 90 degrees clockwise.
    Args:
        matrix (list of list): The 2D matrix to rotate.
    Returns:
        list of list: The rotated matrix.
    """
    rows, cols = len(matrix), len(matrix[0])
    rotated = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            rotated[cols - 1 - j][i] = matrix[i][j]
    return rotated
    # 90 degrees anti clockwise rotation
    # rows, cols = len(matrix), len(matrix[0])
    # rotated = [[0] * rows for _ in range(cols)]
    # for i in range(rows):
    #     for j in range(cols):
    #         rotated[j][rows - 1 - i] = matrix[i][j]
    # return rotated


def main():
    """
    Main function to load an image, rotate it by 90 degrees clockwise,
    and save the rotated image.
    It handles various exceptions that may occur during the image loading
    and rotation process.
    """
    try:
        img = ft_load("animal.jpeg")
    except ValueError as e:
        print("Value Error occurred:", e)
        return
    img = img[100:500, 450:850, 0]
    rotated_matrix = rotate_matrix_90(img)
    try:
        plt.imshow(rotated_matrix, cmap='gray')  # cmap colormap
        plt.show()
    except Exception as e:
        print(f"An error occurred while displaying the image: {e}")


if __name__ == "__main__":
    main()
