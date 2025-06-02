def main():
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}

    #your code here

    ft_list[1] = "World!"
    ft_tuple = (ft_tuple[0], "France!")
    ft_set.remove("tutu!")
    ft_set.add("Charbonnière les bains!")
    ft_dict["Hello"] = "42 Lyon!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)

if __name__ == "__main":
    main()

