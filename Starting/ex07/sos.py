import sys

NESTED_MORSE = {
    "A": ".- ",    "B": "-... ",  "C": "-.-. ",  "D": "-.. ",   "E": ". ",
    "F": "..-. ",  "G": "--. ",   "H": ".... ",  "I": ".. ",    "J": ".--- ",
    "K": "-.- ",   "L": ".-.. ",  "M": "-- ",    "N": "-. ",    "O": "--- ",
    "P": ".--. ",  "Q": "--.- ",  "R": ".-. ",   "S": "... ",   "T": "- ",
    "U": "..- ",   "V": "...- ",  "W": ".-- ",   "X": "-..- ",  "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ",
    "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. ",
    " ": "/ "
}


def encode_morse(text):
    result = ""
    for char in text:
        upper_char = char.upper()
        if upper_char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        result += NESTED_MORSE[upper_char]
    return result.rstrip()


def main():
    """This script encodes a string into Morse code."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        print(encode_morse(sys.argv[1]))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return


if __name__ == "__main__":
    main()
