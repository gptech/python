import os

#allows you to use regular expressions in your program
import glob

#state the path you want

myPath = "/home/jason/python/"

#the .path.join method makes it easy to append something to your full path

#this basically says, append a *.py to the path
fileNamesList = os.path.join(myPath, "*.py")

#now use glob to interpret that * to mean the everything wildcard
for fileName in glob.glob(fileNamesList):

	

	print "You have a python document called %s" % fileName

	fullFilePath = os.path.join(myPath, fileName)

	print "The full path to the file is %s" % fullFilePath