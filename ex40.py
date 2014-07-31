class Song(object):
	#so here you "instantiate the Song object that can take the lyrics arguement to pass off."
	def __init__(self, lyrics):
		self.lyrics = lyrics
	#Here define the singmeasong function within the object which you pass a list as the arguement and print it out with a loop. See below.
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line


happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family", "With pcokets full of shells"])

fuck_authority = Song(["Fuck Authority!", "SILENT MAJORITY!", "RAISED BY THE SYSTEM!", "NOW IT'S TIME TO RISE AGAINST THEM"])

uber = Song(["CALIFORNIA!", "UBER ALLIES!"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

fuck_authority.sing_me_a_song()

uber.sing_me_a_song()

#declare the mutante variable
mutante = (["FUCK", "FUCK", "FUCK", "YOU"])

#pass off the mutante variable to the class as another variable
mutante_lyrics = Song(mutante)

#print like before.
mutante_lyrics.sing_me_a_song()



