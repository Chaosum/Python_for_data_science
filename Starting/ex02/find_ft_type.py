def all_thing_is_obj(obj) -> int:
	if type(obj) == str:
		print(f"{obj} is in the kitchen : {type(obj)}")
	elif type(obj) == list \
		or type(obj) == tuple \
		or type(obj) == set \
		or type(obj) == dict:
		print(f"{type(obj).__name__} : {type(obj)}")
	else:
		print("Type not found")
	return 42

