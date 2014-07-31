from Tkinter import *

#you need to make a root widget to base everything off of so make the line below
root = Tk()

#Here you give it a label with the text.
w = Label(root, text="GO FUCKYOURSELF!")
#Use pack to size the text and make it show up. 
w.pack()

#you need to call the mainloop method to get the gui to show up. Don't ask why
root.mainloop()