from pandas import read_csv, DataFrame
from os import path as os_path


def load(path: str) -> DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    :param path: The file path to the CSV file.
    :return: A pandas DataFrame containing the data from the CSV file.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("The provided path must be a string.")
        if not os_path.isfile(path):
            raise FileNotFoundError(f"The file at {path} does not exist.")
        if not path.endswith('.csv'):
            raise ValueError("The provided path does not point to a CSV file.")
        data = read_csv(path)
        return data
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None
    except ValueError as e:
        print(f"Value error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred while loading the CSV file: {e}")
        return None
