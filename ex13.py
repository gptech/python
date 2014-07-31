#This line is an import line so you can add features to python instead of giving all the programs at once.

from sys import argv

#argv takes all these supplied variables and unpacks from left to right
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
