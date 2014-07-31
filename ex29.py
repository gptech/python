people = 30
cars = 40
buses = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We Should not take the cars"
else:
	print "We can't decide"

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Mabe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's just stay home."

answer = raw_input("What do you want to do today" ) 

print "You want to %s" % answer