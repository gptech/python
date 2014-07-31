def loop(var1, var2):
	i = 0
	numbers = []

	while i < var1:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + var2
	print "numbers now: ", numbers
	print "At the bottom i is %d" % i

#insert what your variable is going to be here
loop(10, 2)




