

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#The following sections use formatters to substitute values into the strings. %s imports data as a string %r reads in the file literally.
#They tell python to take the variable on the right and put in to the formatter to replace its value.
#Not sure what %d does

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's go %s eyes and %s hair." % (eyes, hair)
print "His teeth ore usually %s depending on the coffee." % teeth


#This line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
