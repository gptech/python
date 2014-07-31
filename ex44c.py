class parent(object):

	def altered(self):
		print "PARENT ALTERED()"

class child(parent):

#The important part here is to see how we call the super function with arguements child and self which basically just means
#super go get the child class and run altered on it which will provide a different value after the fact.
	def altered(self):
		print "CHILD, BEFORE PARENT ALTERED()"
		super(child, self).altered()
		print "Child AFTER PARENT altered."

dad = parent()
son = child()

dad.altered()
son.altered()

#The most common use of super() is actually in __init__ functions in base classes.
#This is pretty much the same as the child.altered example above except I'm setting some variables in the __init__ BEFORE
#having the parent initialize with its parent.__init__