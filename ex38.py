ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "\n%s\n" % ten_things

print "Wait there's not 10 things in that list, let's fix that\n"

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn",
"Banana", "Girl", "Boy"]

#So I guess what's happening here is while the (len)gth of stuff is less than 10
#Pop off an element from more stuff to next_one and append it to the specially formatted stuff and print
# out the speciffically formatted stuff

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now.\n" % len(stuff)

print "There we go: ", stuff

#print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop() # Description The method pop() removes and returns last object or obj from the list.
print ' '.join(stuff) # What? Cool! It's fucking the same thing!
print '#'.join(stuff[3:5]) # super steller!