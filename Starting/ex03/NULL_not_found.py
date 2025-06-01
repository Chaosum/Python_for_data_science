def NULL_not_found(object: any) -> int:
	if type(object) == str:
		if object == "":
			print(f"Empty: {type(object)}")
			return 0
	elif type(object) == bool:
		if object is False:
			print(f"Fake: {object} {type(object)}")
			return 0
	elif type(object) == int:
		if object == 0:
			print(f"Zero: {object} {type(object)}")
			return 0
	elif type(object) == float:
		if object != object: # Check for NaN
			print(f"Cheese: {object} {type(object)}>")
			return 0
	elif object is None:
		print(f"Nothing: {object} {type(object)}")
		return 0
	print("Type not Found")
	return 1
