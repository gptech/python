
#this introduces the built in raw_input function of python...it prompts a user for an arguement and turns it into a string.1
# the comma after the print string makes the raw_input function appear next to the question making it cleaner

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?", 
weight = raw_input()

print "So you're %r old, %r, tall and %r heavy." % ( age, height, weight )
