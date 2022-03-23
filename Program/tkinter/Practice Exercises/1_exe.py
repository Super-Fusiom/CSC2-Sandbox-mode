from tkinter import * # Import everything from tkinter lib
from tkinter import ttk # Import a sub lib in tk

root = Tk() # top level window 
#Making a label widget
display = root.mainloop
label = Label(root, text="Paul was here")
#What you see on screen

# label config
label.config(text="Paul was here", fg="green")
label.config(bg="yellow")
label.config(font='Times 20')

label.config(text='Paul is still here')
label.config(wraplength='150')
label.config(justify='right')

#Actually show everything above on screen REQUIRED
label.pack()
root.geometry('640x480')

display()