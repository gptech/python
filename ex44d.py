

#Inheritence is useful but another way to do the exact same thing is just to use other classes and modules,rather
#than always rely on implicit inheritence.

class Other(object):

	def override(self):
		print "Other override()"

	def implicit(self):
		print "Other implicit()"

	def altered(self):
		print "OTHER altered()"

class Child(object):

#Defining that this Child object has a "Other"
	def __init__(self):
		self.other = Other() #this is very important!

#Define a method that calls the other method
	def implicit(self):
		self.other.implicit

#Overwrites the other method since you told Child to inherit the Other attributes.
	def override(self):
		print "CHILD override"

#Here you print you define a altered method and print child, then the altered from other and then print child again.
	def altered(self):
		print "CHILD BEFORE OTHER altered."
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()