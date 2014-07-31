from sys import argv

script, filename = argv

print "We're going to erase %r.:" % filename
print "If you don't what that, hit Ctrl-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# need to open with a 'w' parameter to make sure open will open the file in write mode. You can use a + modifier to do r+w
# this is apparently not the same as using the write function to a file. 
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#Ok so below what I did was take 3 raw_inputs and then concatenate them into the allines variable.
#Since it appears the write module only excepts one arguement I made alllines a string with formatters and just wrote that one string out.

line1 = raw_input("1. ")
line2 = raw_input("2. ")
line3 = raw_input("3. ")
alllines = "%s\n%s\n%s\n" % (line1, line2, line3) 
print "I'm going to write these to the file."

target.write(alllines)

#so below here we close the file but you can't seem to reopen it afterwards.

print "And finally, we close it."
target.close()


