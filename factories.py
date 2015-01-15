__author__ = 'jason'

# A factory is a design pattern which lets a function (or the computer) choose what class to return (to create).


BaseClass = type("BaseClass", (object,), {})

# Define the classmethods here in the base class so the below type subclasses I create are aware of them.

#Classmethod that just returns a specific string to create logic in what classes are returned.
@classmethod
def Check1(self,mystr):
    return mystr == "hello"

@classmethod
def Check2(self,mystr):
    return mystr == "world"

#Create the subclasses with the check classmethods you created above
C1 = type("BaseClass", (BaseClass,), {'x': 1, "Check": Check1})
C2 = type("BaseClass", (BaseClass,), {'x': 30, "Check": Check2})

#Create a factory function that returns a class based on what input is passed into the function using the logic in the checks in the subclasses themselves.
def Myfactory(mystr):
    for cls in BaseClass.__subclasses__():
        if cls.Check(mystr):
            return cls()


m = Myfactory('hello')

v = Myfactory('world')

#Print out the variables for each class.
print(m.x, v.x)