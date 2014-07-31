from __future__ import division

try:
	number = int(raw_input("Enter an integer: "))
except ValueError:
	print "That was not an integer."

#just demonstrates that you can include typevalues with commas for general problems.
def divide(num1, num2):
	try:
		print num1 / num2
	except (TypeError, ZeroDivisionError):
		print "Encountered a problem"


def divide2(num1, num2):
	try:
		print num1 / num2
	except ValueError:
		print "You didn't enter an integer you fuck."
	except ZeroDivisionError:
		print "You cannot enter 0 you fuck."

def divide3(num1, num2):
	try:
		# a bunch of shit that could potentially break. 
	except:
		print "Something broke. Probably user error"
