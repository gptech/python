#This excercise will stress the point that variables in your functions are not connected to the variables in your script.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "Your have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from the whole script."
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#this shows all the different ways we're able to five our function cheese_and_crackers the values it needs to print them.
#We can give it straight numbers. We can give it variables. We can give it math. We can even combine math and variables.
