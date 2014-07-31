
#this works, do not use a or statement with the if clause becuase it doesn't fucking work for some reason

while True:
	prompt = raw_input("Type in something or press Q or q to quit: ")

	if prompt == 'q':
		 break
	elif prompt == 'Q':
		break
	else:
		continue