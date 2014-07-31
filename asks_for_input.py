
#repeatidly asks for an integer and if the user doesn't input an integer it fails and asks to print it again.


while True:

	try:
		number = int(raw_input("Enter an integer: "))
		print number
		break

	except ValueError:
		print "That was not an integer."
