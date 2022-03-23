from tkinter import *
from tkinter import ttk

root = Tk()





button1 = Button(root, text="Woof")
button2 = ttk.Button(root, text="Wee")


root.geometry('640x480')
button1.pack()
button2.pack()

root.mainloop()