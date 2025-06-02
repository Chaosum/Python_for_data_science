from sys import argv, stdin


def main():
    #  Add the parent directory to the system path
    arg = ""
    if len(argv) > 2:
        print("AssertionError: more than one argument are provided")
        return
    elif len(argv) == 2:
        arg = argv[1]
    elif len(argv) == 1:
        arg = stdin.readline()
    upper = 0
    lower = 0
    ponctuation = 0
    spaces = 0
    digits = 0
    for char in arg:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            ponctuation += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1

    print(f"The text contains {len(arg)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{ponctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
