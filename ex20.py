

#sets up argv like normal
script, input_file = argv


#defines print_all function by calling the read function
def print_all(f):
	print f.read()

#defines the rewind function by calling the seek function  which moves to a specifc part of the file.
#By providing 0 to the seek function we are moving to the top of the file.
def rewind(f):
	print f.seek(0)

#defines the print_a_line function
def print_a_line(line_count, f):
	print line_count, f.readline()

#note that this is what is being passed down to f in all these functions the next 11 lines have nothing to do with the following increment section all they do is show off the various functions. 
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

#so what we're doing here is starting at the top of the file. Then for each subsequent run of the function we are manually incrementing it.
#would like to use += to shorthand the script but don't know wher to put it syntax wise. It keeps failing. 
#The current_file part is more or less irrelevent only because you're just reusing the same variable each and everytime you call this function.
current_line = 1 
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
