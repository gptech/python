# this substitues 10 in the string.

x = "There are %d types of people." % 10

# declaring string variables the last line does substiution like ex5
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Substitutes a raw string of X
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# Concatenates a string

w = "This is the left side of...."
e = "a string with a right side."

print w + e


