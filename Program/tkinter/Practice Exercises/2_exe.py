from tkinter import * # Import everything from tkinter lib
from tkinter import ttk # Import a sub lib in tk


#Making variables to make life easier
root = Tk() # top level window 
#Making a label widget
display = root.mainloop
label = Label(root, text="Paul was here")
lconfig = label.config 

button = Button(root, text='HI :D')
#What you see on screen

# label config
lconfig(text='Paul is still here')
lconfig(wraplength='150')
lconfig(justify='right')

#Actually show everything above on screen REQUIRED
button.pack()
label.pack()
root.geometry('640x480')

display()