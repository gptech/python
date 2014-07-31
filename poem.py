import random


# define lists for the vocabulary

Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]

Verbs = ["kicks", "jungles", "bounces", "slurps", "meows", "explodes", "curdles"]

Adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]

Prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"] 

Adverbs =["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

#use the random.choice method to grab a random part of a list in the function below
#test = random.choice(Nouns)

#works

def makePoem():

	#initially set values for all these

	noun1 = random.choice(Nouns)

	noun2 = random.choice(Nouns) 

	noun3 = random.choice(Nouns)

	verb1 = random.choice(Verbs)

	verb2 = random.choice(Verbs)

	verb3 = random.choice(Verbs)

	adject1 = random.choice(Adjectives)

	adject2 = random.choice(Adjectives)

	adject3 = random.choice(Adjectives)

	prep1 = random.choice(Prepositions)

	prep2 = random.choice(Prepositions)

	adverb = random.choice(Adverbs)

	#ensures all noun selections are random
	while noun1 == noun2 or noun1 == noun3 or noun2 == noun3:
		noun1 = random.choice(Nouns)

		noun2 = random.choice(Nouns) 

		noun3 = random.choice(Nouns)

	#ensures all verb selections are random
	while verb1 == verb2 or verb1 == verb3 or verb2 == verb3:

		verb1 = random.choice(Verbs)

		verb2 = random.choice(Verbs)

		verb3 = random.choice(Verbs)


	#ensures all adjective selection is random
	while adject1 == adject2 or adject1 == adject3 or adject2 == adject3:

		adject1 = random.choice(Adjectives)

		adject2 = random.choice(Adjectives)

		adject3 = random.choice(Adjectives)

	#ensures all preposition selections are random
	while  prep1 == prep2:

		prep1 = random.choice(Prepositions)

		prep2 = random.choice(Prepositions)

	poem = "A %s %s \n \n A %s %s %s %s the %s %s %s the %s %s the %s %s %s a %s %s." % (adject1, noun1, adject1, noun1, verb1, prep1, adject2, noun2, adverb, noun1, verb2, noun2, verb3, prep2, adject3, noun3)

	print poem


makePoem()

