#open the files using the with word in the same line and read over the lines and with a loop and close it

#you can combine with statements for a single block of usage which is pretty cool. 
with open("poem.txt", "r") as inputPoem2, open("outputpoem2.txt", "w") as outputPoem2:

	for line in inputPoem2.readlines():

		outputPoem2.write(line)