from sys import argv

def dead():
	print "Press R to restart..."
def cont(): 
	print raw_input("Press any key to continue ")

def start_car():
	print "Ok, so you answered the call.\n You've just arrived at the spot in your car...\n.....who are you tonight?"

	masks = ['Richard', 'Tony', 'Graham', 'Willem'] 

	selection = raw_input("Richard? Tony? Maybe Graham? ...Willem? > " )
	if selection == "Richard":
		print masks[0]
		room_1()
	elif selection == "Tony":
		print masks[1]
		room_1()
	elif selection == "Graham":
		print masks[2]
		room_1()
	elif selection == "Willem":
		print masks[3]
		room_1()
	else:
		print "You can't even put your fucking mask on correctly\n What makes you think you're gonna survive this?\n CASE SENSITIVE"
		dead()
#So the above block prompts the user and then prints out your function according to the corresponding entry in the list.
#This way you can just add masks to the list and print the corresponding list numbers.


def room_1():
	print "\n Ok, now we're getting somewhere...."
	print "\n\n So you break through the first door. You whack a chump in the face and he drops his crowbar.\n His buddy is over to the right how do you take him out?"
	attack = raw_input("Choose 'bludgeon' or 'throw' ")

	if attack == "bludgeon":
		print "WHACK"
		print ""
		print "WHACK\n"
		print "His head is smashed to pieces, brain matter everywhere....\n Do you want to keep the crowbar?"
		crowbar = raw_input("Yes or No? " )
		room_2(crowbar)

	elif attack == "throw":
		print "You chuck the crowbar and score a direct hit...\n teeth go everywhere...you duck into the next room"
		crowbar = "No"
		room_2(crowbar)
	else:
		print "You took too long and the other guy gets the jump on you and stabs your internals relentlessly..."
		dead()


def room_2(crowbar):
	#so here I've successfully imported the value of crowbar which we can use to do a simple weaponcheck.
	#you can pass down the weaponcheck variable as many times as you want all the way to the bottom.  
	if crowbar == "yes":
		weaponcheck = True
	else: 
		weaponcheck = False

	print "You cut the corner into the next room \n \n \n Whack! \n You push a mobster into a corner. \n As you go to finish him off you notice another scumbag running up behind you. \n Think fast, what are you gonna do about him?"

	choicelist = ['1. Whip around and Kill him?', '2. Duck into the side room?', '3. Duck into the next room',]

	print "%s" % choicelist
	choice = int(raw_input("Select a number like right fucking now! "))
	
	if choice == 1 and weaponcheck == False:
		print "\nYou didn't bring a crowbar with you dipshit. The goon jumps you and beats you senseless..."
		dead()
	elif choice == 1 and weaponcheck == True:
		print "\nYou whip around and sink the crowbar into the goon's neck! Blood sprays everywhere and he goes down.\n\nYou decide to head into the next main room."
		room_3(weaponcheck)	
	elif choice == 2:
		print "\nYou scramble up and run into the side room. Maybe you'll find a better weapon to defend yourself with."
		room_2a(weaponcheck)
	elif choice == 3:
		print"\nWithout a weapon you decide to risk it and jump into the next main room and quickly jam the door behind you."
		room_3(weaponcheck)	
	else:
		print "\nWhatever you decided it got you a shotgun blast aimed at your internal organs..."
		dead()
	
def room_2a(weaponcheck):
	#the point of room 2a is to get you a weapon and set the weapon check to true
	print "\nRunning into the next room you see a large counter in your way. You leap over it and find a lead pipe.\n"

	if weaponcheck	== False:
		choice = raw_input("You probably want this, right? ")
		weaponcheck = True
	else:
		print "Since you have the crowbar already, fuck the pipe. You need to kill the goon coming in with his gun ready. You take a quick peek around the counter corner to find your position in his blind spot. You need to time this right..."
	print "\nOk you now have a weapon. You need to kill the goon coming in with his gun ready.\n You take a quick peek around the counter corner to find your position in his blind spot. You need to time this right..."
	
	wait = int(raw_input("Not a lot of time, how many seconds do you wait so you can get the jump on him? "))
	if wait < 5:
		print "\nShiiit, too soon. The goon catches you coming out and takes your head off"
		dead()
	elif wait > 10:
		print "\nYou gotta be quicker then that. The goon turns to face your direction with his gun ready. You're truly fucked."
		dead()
	elif wait <= 10 and wait  >= 5:
		print "\nPerfect timing. You jump out and nearly knock his head off from his neck!\n\nYes blood is everywhere....you head to the next main room"
		room_3(weaponcheck)
	else:
		print "This isn't highschool motherfucker! You didn't choose correctly and some dogs come running in and jump over the counter ripping you to pieces!"
		
def room_3(weaponcheck):
		def ammo():
			bullets = 6
			while bullets >= 0:
				print "You fire a shot\n"
				bullets = bullets - 1
			print "*click* the clip is empty"
		def ammo2():
			bullets = 6
			while bullets >= 0:
				print "You fire a shot\n"
				print "Do you keep firing? yes or no: "
				answer = raw_input()
				if answer == "yes":
					bullets = bullets - 1
				else:
					bullets = -1
					room_4()
			
	#ok here I want to introduce some gunplay. Maybe do something with get a gun and check the ammo counter compared to the number of goons and use a loop to test.
		print "Ok the next hall is fairly narrow without a lot of room to work with.\nYou begin running down keeping your eyes peeled..."
		print "\n   You come up to a corner and peek around to catch a goon with his back turned. \nThis one should go down easy." 
		print "\n You take your pipe and shove it through his back causing his organs to splatter out the other end.\n\nHe whimpers as he realized what happens."
		print "A silenced pistol falls out of his holster. Of course you're gonna pick it up...\n As soon as you do though the doors at the end of the hall fling open and goons start pouring out."
		print "\n\n\n You open fire.\n"
		ammo()
		print"\n Blood, brains and shell casings are everywhere.\n Like a sick twisted video game by some crazy motherfucker.\n"
		print"Stepping over a body you find a magazine for the handgun you just picked up. You clean off the blood and load it in...\n"
		print"\n At the end of the hall you hear some feet shuffling towards you from around the corner to the next room.\n\n You can probably get the upperhand if you blind fire around the corner."
		print"\nShould you blind fire? "
		answer = raw_input()
		if answer == "yes":
			ammo2()
		else:
			print "You spring around the corner with your lead pipe raised only to get your body torn in two by two shotgun totin' goons."
			dead()

		



def room_4():
	print "Peeking around you see a hallway full of bodies, some still moving, others lifeless\n"
	#aybe in this one I'll have a keycode to enter for the final boss room. Have the player use raw input to punch in the code and append to a list of numbers
	#Then print out that number and check it against a door code
	print "\n You rush ahead and scoop up some ammo. \n You quickly reload your mag just in time to pop a goon between his eyes.\n"
	print "\n He seemed like the last one...up ahead there's a door with a numpad on it. On the other side you can hear shuffling of feet..\n"
	print "There's 6 digits, numbered 1 through 6. It look like you can put in up to 3 entries"
	
	def keypad_function():
		answer = 0
		while answer != 8:
			entry_one = int(raw_input("Make your first Selection: "))
			entry_two = int(raw_input("\nMake your second selection Selection: "))
			entry_three = int(raw_input("\nMake your third Selection: "))
			answer = entry_one + entry_two + entry_three
			print answer

	keypad_function()		
	print "click! The door opens."
	cont()
	room_5()
		



def room_5():
	print "The room is dark as shit\n ...but you know you can't be the only one inside."
	print "\nSuddenly the lights flash to blinding bright light!\n Gunfire begins to open up from an undisclosed direction\n "
	print "You need to take cover, fast!\n"

	action = raw_input("Duck 'N Cover? This is probably a yes or no question: ")

	if action == "yes":
		print "You do the needful and take cover behind some tables. It doesn't help much because the bullets are taking it apart along with you with it"

		dead()
	elif action == "no": 
		print "You stand there taking bullets like a retard. You could have tried something!"
		dead()
	else:
		print "Indecisiveness saved your ass, you feel bullets whiz past your face but manage to get a quick shot off hitting a light casting darkness."
		print "\n You hear an angry Russian swearing something in what is clearly Russian. Sounds like an important dude. You start firing your pistol towards the voice.\n"
		print "\n It doesn't seem like your shots are hitting but you've gained a window so you proceed to some cover."
		print "\The bullets start heading your way again along with more Russian yelling, must be some kind of heavy machine gun."
		print "Amongst all the chaos you get a peek at the bald fuck laying down the trigger at you. Just a piece of shit bigshot with some heavy armor\n"
		print "\nYou spring into action with a gunshot to his knee. He cries out in pain but still keeps his sights on you."
		print "Ok, time to end this.\n"

		print " You place a nice shot in his chest but he's not going down.\n You fire a couple more shots\n"
		print " It seems all you've done is piss him off but he drops his giant as machine gun and starts running at you."
		action2 = raw_input("shoot or bludgeon? ")

		if action2 == "shoot":
			print "You unload a clip into his face, use your imagination for what that would look like."
		elif action2 == "bludgeon":
			print "WHACK!\nWHACK!\nWHACK!\nWHACK!\nWHACK!\nWHACK!\nWHACK!\nWHACK!\n"
		else:
			"Didn't work. He headbutts you and bites your lower lip off and punctures your stomach with his fist. "
			dead()
		print "\nYou win"	


start_car()
