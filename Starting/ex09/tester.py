from ft_package import count_in_list


def main():
    # output: 2
    print(count_in_list(["toto", "tata", "toto"], "toto"))
    # output: 0
    print(count_in_list(["toto", "tata", "toto"], "tutu"))


if __name__ == "__main__":
    main()
