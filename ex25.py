
#So with this excercise, Zed is having us make up some functions so we can import all of these into the python interpreter as a module for testing. This way when we do something like ex25.break_words you'll be saying to Python, "Hey inside ex25 there's a function called break_words and I want to run it.

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

	
