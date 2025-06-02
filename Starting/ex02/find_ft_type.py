def all_thing_is_obj(obj) -> int:
    if type(obj) == str:
        print(f"{obj} is in the kitchen : {type(obj)}")
    elif type(obj) == list:
        print(f"List : {type(obj)}")
    elif type(obj) == tuple:
        print(f"Tuple : {type(obj)}")
    elif type(obj) == set:
        print(f"Set : {type(obj)}")
    elif type(obj) == dict:
        print(f"Dict : {type(obj)}")
    else:
        print("Type not Found")
    return 42
