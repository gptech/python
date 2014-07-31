from Tkinter import *

#you need to make a root widget to base everything off of so make the line below
class Application:

	def __init__(self, master): #master is the king of all widgets in TK so instantiate object with it.

		frame = Frame(master)  #Frame is just a container window. Just defining it here.
		frame.pack()			#frame.pack means show the frame window. 

		self.button =Button(frame, text="quit", fg="red", command=frame.quit)
		self.button.pack(side=LEFT) #show the button here.


		

		self.button2 =Button(frame, text="Die fucker", fg="blue", command=self.diefire) #define the second button here
		self.button2.pack(side=RIGHT) #show the button here.

	def diefire(self):
		while True:
			print "DIE IN A FIRE MOTHERFUCKER!"


root = Tk()

#These are very important
app = Application(root) #
root.mainloop()