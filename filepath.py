import os

#state the path you want

myPath = "/home/jason/python/"

fileNamesList = os.listdir(myPath)

for fileName in fileNamesList:

	if fileName.endswith(".py"):

		print "You have a python document called %s" % fileName

	fullFilePath = os.path.join(myPath, fileName)

	print "The full path to the file is %s" % fullFilePath