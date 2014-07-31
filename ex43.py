from sys import exit
from random import randint

#So go back over the excercise 43 in case you're wondering but Zed does define his classes from lines here.

#Creates a scene object to be referenced later
class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

#Creates the game engine class and object so he can provide a map to it later
class engine(object):

	def __init__(self, scene_map):
		print "Engine __init__ has scene map ", scene_map
		self.scene_map = scene_map
		

	def play(self):
		current_scene = self.scene_map.opening_scene()
		print "Play's first scene", current_scene

		while True:
			print "\n------------"
			next_scene_name = current_scene.enter()
			print "next scene", next_scene_name
			current_scene = self.scene_map.next_scene(next_scene_name)
			print "Map returns the new scene", current_scene

#Creates the death class scene here. Pretty straightforward in randomizing the deathquips.
class Death(Scene):
	
	quips = [" You died. You kinda suck at this.",
	"Your mom would be proud....if she were smarter",
	"Such a loser.",
	"I have a small puppy that's better at this."]


	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

#From here he defines the rest of the scenes although he doesn't actually create them as objects. It's just a demonstration of passing the
#values from here.  At the end of the scene, it returns the the name of the next scene to the game engine which will progress the game.
class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons come and have ruined your home!"
		print "Shit sucks and you're starting at the central corridor."
		print "A gothon attacks you and is blocking the way to the armory."

		action = raw_input("> ")

		if action == "shoot!":
			print "You shoot and miss because you suck."
			print "You are dead. Then he eats you."
			return 'death'
		elif action == "dodge!":
			print "Don't know why you did that because you're dead now."
			return 'death'
		elif action == "tell a joke":
			print "The gothon does a Josh Gutman laugh and you sneak by him."
			return 'laser_weapon_armory'
		else:
			print "What?"
			return 'central_corridor'


class LaserWeaponArmory(Scene):

	def enter(self):
		print "Your dive roll into the weapon armory, crouch and scan the room"
		print "for more gothons. You find a bomb locked in a case. It is protected by "
		print "a keypad and you need to guess the code to get the bomb out."
		print "If you get the code wrong 10 times the lock closes forever and you can't get the bomb."
		print "The code is 3 digits."

		code = "%d%d%d" % (randint(1,9),randint(1,9), randint(1,9))
		guess = raw_input("> ")
		guesses = 0 

		while guess != code and guesses < 9:
			print "BZZZZZZZZZZED!"
			guesses += 1
			guess = raw_input("> ")

		if guess == code:
			print "The container clicks open and the seal breaks. You grab the bomb and go to the bridge."
			return 'the_bridge'
		else:
			print "Well guess you fucked up. The lock closes forever. You decide to play video games while the world goes to shit."	
			return 'death'

class TheBridge(Scene):

	def enter(self):
		print "You burst onto the bridge with the neutron bomb."
		print " The room is full of Gothons and they spot you come in."

		action = raw_input("> ")

		if action == "throw the bomb":
			print "In a panic you throw the bomb at them and when it hits the ground the thing blows up."
			return 'death'

		elif action == "slowly place the bomb":
			print "You take the bomb under your arm and point your plasma pistol at it and slowly back out of the room."
			return 'escape_pod'
		else:
			print "What the fuck?"
			return 'the_bridge'

class EscapePod(Scene):

	def enter(self):
		print "You rush through the ship deperately trying to make it to the escape pods."
		print "You find 5 of them, some of them could be damaged but there's no time to check."
		print "Which one do you take?"

		good_pod = randint(1,5)
		guess = raw_input("> ")

		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			print "Too bad when you hit the eject button it explodes killing you."
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "It rockets off back to earth and you are a hero."

			return 'finished'

#creates a map object with all the scenes detailed in a dictionary so they can be referenced by the game engine. 
class Map(object):

	scenes = {
			'central_corridor': CentralCorridor(),
			'laser_weapon_armory': LaserWeaponArmory(),
			'the_bridge': TheBridge(),
			'escape_pod': EscapePod(),
			'death': Death()
			}

	def __init__(self, start_scene):
		self.start_scene = start_scene
		print "start_scene in __init__", self.start_scene


	def next_scene(self, scene_name):
		print "Start_scene in next_scene"
		val = Map.scenes.get(scene_name)
		print "next_scene returns", val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map= Map('CentralCorridor')
a_game = engine(a_map)
a_game.play()