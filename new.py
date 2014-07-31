from __future__ import division
from random import randint

#declare the variables for the results starts at zero so you can add it up in total. 
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0


#simple dietoss function that returns a result
def dietoss():
	return randint(1, 6)

	


#the loop that simulates die throws and performs if statements and adds the results together for the final simulation
for trial in range(0, 10000):
	outcome = dietoss()

	if outcome == 1:
		one = one +1
	elif outcome == 2:
		two = two +1
	elif outcome == 3:
		three = three +1
	elif outcome == 4:
		four = four +1
	elif outcome == 5:
		five = five +1
	elif outcome == 6:
		six = six +1

#add your results to a list get the average and print it doesn't say which variable is actually the average.
#I guess I could do another if statement and just round the values to the closest result with a zipped list.
l = [one, two, three, four, five, six]

r = ["one", "two", "three", "four", "five", "six"]

zipped = zip(l, r)

print zipped
