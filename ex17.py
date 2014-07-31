
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

#here we are decalring the variable out_file which is the product of opening our to_file with the write permission
out_file = open(to_file, 'w' )
out_file.write(indata)

print "Alright, all done."

#make sure you close your files out so they don't stay in memory.
out_file.close()
in_file.close()
