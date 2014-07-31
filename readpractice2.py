#open the file using the with word and read over the lines with a loop and close it


with open("poem.txt", "r") as inputPoem:

	for line in inputPoem.readlines():

		print line,