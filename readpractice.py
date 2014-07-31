#open the file and read over the lines with a loop write to the output and close it
inputPoem = open("poem.txt", "r")
outputPoem = open("outputpoem.txt", "w")

for line in inputPoem.readlines():
	
	outputPoem.writeline()


inputPoem.close()
outputPoem.close()