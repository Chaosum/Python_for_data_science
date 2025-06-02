from sys import argv


def main():
    """This script takes a string and an integer as command line arguments.
It splits the string into words and filters out those that are \
longer than the integer.
    """
    try:
        assert len(argv) == 3
        S = argv[1]
        assert isinstance(S, str)
        assert (lambda s: all(c.isalnum() or c.isspace() for c in s))(S)
        N = int(argv[2])
        words = S.split()
        result = [word for word in words if len(word) > N]
        print(result)
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
