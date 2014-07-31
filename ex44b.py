class parent(object):

	def override(self):
		print "PARENT override()"

#This example basically shows that if you rename a method in a subclass it will overwrite the parent file.
class Child(parent):
	def override(self):
		print "CHILD override()"

dad = parent()
son = Child()

#It will print out a child override because you overwrote it.
dad.override()
son.override()