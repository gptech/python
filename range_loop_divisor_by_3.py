

def factorsfuncnot3():
	factors = range(1, 51)

	for i in factors:
		if i % 3  == 0:
			continue
		else:
			print "%i" %i
	return



factorsfuncnot3()