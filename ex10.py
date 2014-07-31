#This excercise introduces escape sequences in strings. Use this to modify the presentation of your strings and values in the strings
# \t tab horizontal tab
# \' single quote
#\" doublequote
# \\ = backslash escape sequence
# \a bell noise
# \b backspace
# \f ascii formfeed
# \n new line
#\v ascii vertical tab

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,
