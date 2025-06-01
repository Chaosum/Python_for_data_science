from sys import argv

if len(argv) > 2:
	# raise AssertionError("more than one argument are provided")
	print("AssertionError: more than one argument are provided")
elif len(argv) == 2:
	try:
		print("I'm Even." if int(argv[1]) % 2 == 0 else "I'm Odd.")
	except ValueError:
		# raise AssertionError("argument is not an integer")
		print("AssertionError: argument is not an integer")
