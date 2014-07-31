from __future__ import division
from decimal import Decimal


def invest(amount, rate, time):
	
	print "Principle amount: $%d " %amount

	print "annual rate of return: %r " %rate

	
	#Take the amount of years and use it in a range and print out that corresponding year
	#The year is based off of this total formula $1,000 × (1 + 0.06)

	for y in range(1, time):

		total = (amount * (y + rate))

		print "Year %d: $%r" % (y, total)

		y = y+1




invest(2000, 0.025, 10)