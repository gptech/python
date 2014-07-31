



prompt = raw_input("Enter a positive integer: ")

integer = int(prompt)

#print integer

def factorsfunc(arg1):
	factors = range(1, arg1+1)
#use an if statement to only showly cleanly divisable numbers otherwise the continue statement will skip it.
	for i in factors:
		if arg1 % i == 0:
			print "%i is a divisor of the number you picked." %i
		else:
			continue
	return



factorsfunc(integer)