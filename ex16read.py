from sys import argv

script, filename = argv

print "Here's your result from ex16.py"
target = open(filename)
print target.read()
target.close()
