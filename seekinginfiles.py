

myInputFile = open("hello.txt", "r")

print "Line 0 (first line)", myInputFile.readline()

myInputFile.seek(0) # jump back to the top of the file and start reading from there

print "Line 0 again", myInputFile.readline()

print "Line1:", myInputFile.readline()

myInputFile.seek(8) # jump to the character at index part 8 and start reading from there

print "Line 0 (starting at 9th character):", myInputFile.readline()

myInputFile.seek(10, 1) # relative jump forward 10 characters from where we are and start reading from there. 1 means go forward -1 means go back

print "Line 1 (starting at 11th character)", myInputFile.readline()

myInputFile.close()
