
#So for this excercise we are getting used to returning something from a function using boring ass math.
def add(a, b):
	print "Adding %d +%d" % (a, b)
	return a + b

def subtract(a, b):
	print "Subtracting %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "Multiplying %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "Dividing %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Wieght: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes ", what, "can you do it by hand?"

derp = int(raw_input("What is the number of derp?" ))
herp = int(raw_input("What is the number of herp?" ))
berp = int(raw_input("What is the number of burp?" ))

# print "Here you go fuckhead: %d, %d, %d" % (derp, herp, berp)

def practicefunction(a, b, c):
	print "This is what happens when you fuck a stranger in the alps Larry."
	return a + b - c
functionanswer = practicefunction(derp, herp, berp)

print functionanswer
