
#Create a parent class
class parent(object):

	def implicit(self):
		print "PARENT implicit()"

#The use of pass just tells python to just use this as an empty block.
#All we're saying here is to create a new class called Child which is a type of Parent object
class Child(parent):
	pass


#Here you define some outside variables based on the two classes you made. 
dad = parent()
son = Child()

#Because the son class pretty much directly inherits the Parent class it can also use the implicit method.
#It will print the same shit because both objects are technically the same classes.
#This shows you that if you put functions in a base class, then all subclasses will automatically get those features.

dad.implicit()
son.implicit()



