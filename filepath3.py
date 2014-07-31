import os

#allows you to use regular expressions in your program
import glob

#state the path you want

myPath = "/home/jason/testdir/"

#use os.walk module to go down through the directory tree which always uses dirPath, subdirnames, and filenames. 
for dirPath, dirNames, fileNames in os.walk(myPath):

	for fileName in fileNames:

		print os.path.join(dirPath, fileName)

