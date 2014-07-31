## Animal is a object (yes, sort of confusing) look at the extra credit


class Animal(object):
	pass
#Dog is a type of Animal 
class Dog(Animal):
	## The dog class is a real object with a name attribute
	def __init__(self, name):

		self.name = name
	def dogname(self):
		print self.name
#Cat is a type of Animal Class
class Cat(Animal):
	#It is an object with a name attribute as well.
	def __init__(self, name):

		self.name = name

	def catname(self):
		print self.name
#Person is an Object
class Person(object):
#Person is a real object with a self and a name variable there's a pet variable but it doesn't take those arguements
	def __init__(self, name):

		self.name = name

		self.pet = None

	def HiMyNameIs(self):
		print self.name # If you don't declare self python is gonna think it's a global variable which you obviously you didn't declare. self tells how far python to look.

#Employee is a Person that can take a name and salary attribute
class Employee(Person):
#It is a real object with a name and salary attribute
	def __init__(self, name, salary):
# This statement below means since Employee is a subclass we want to specify that only Employee Object is allowed to have the Salary attribute.
# The syntax of the below statement means start at the real Employee object within the muliinheritance object (by name) and specify a Salary attribute.
#just for Employee
		super(Employee, self).__init__(name)

		self.salary = salary

	def summary(self):
		print "Hi, my name is %s and my salary is %s." % (self.name, self.salary)
		
#The Fish Class is an object
class Fish(object):
	pass

#The Salmon Class is a type of Fish Class
class Salmon(Fish):
	pass

#Halibut class Is Also a type of fish class
class Halibut(Fish):
	pass

# The rover variable is an instance of Dog called with the name Rover
rover = Dog("Rover")

# The satan variable is an instance of cat with the name of Satan.
satan = Cat("Satan")

#The Mary variable is an instance of the Person object with the name Mary as a parameter.
mary = Person("Mary")

#Take the pet function of Mary and assign it the satan variable.
#mary.pet = satan

# The frank variable is an instance of Employee called with a name and salary attributes.
Frank = Employee("Frank", 120000)

# assign the Pet function to rover.
#frank.pet = rover
#Flipper is a Fish object
#flipper = Fish()

# Crouse is a instance of the Salmon object
#crouse = Salmon()

#Harry is another instance of the Halibut Object
#harry = Halibut

#So to print out these variables you have to define methods inside the definitions and constantly refer to self. 
rover.dogname()
satan.catname()
mary.HiMyNameIs()
Frank.summary()