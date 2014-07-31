



prompt = raw_input("Enter a word that is 5 characters long: ")

prompt_length = len(prompt)

if prompt_length == 5:
	print "Good job, that's five characters."

elif prompt_length < 5:
	print "Nope, that's less than five characters."

elif prompt_length > 5:
	print "Nope, that's more than five characters shithead."

else:
	print "Try again, nothing you put in made any sense."