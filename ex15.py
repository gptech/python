from sys import argv

#Uses argv to suck in the parameters
script, filename = argv

# calls the openfunction of the file and makes it the txt variable
txt = open(filename)

#prints the file you just sucked in and the calls the .read() function to print out what's in the file and then it closes it.
print "Here's your file %r:" % filename
print txt.read()
txt.close()

#similar to above but this time it just uses raw_input to have you type in the file yourself
print "Type the filename again:"
file_again = raw_input("> ")

#User types in a file variable from raw_input. While you could probably just stop there to print it
#here we are opening the file into the txt_again variable and printing that.
txt_again = open(file_again)
print txt_again.read()
txt_again.close()
