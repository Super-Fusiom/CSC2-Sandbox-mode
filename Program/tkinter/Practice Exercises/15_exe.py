from tkinter import *
from tkinter import ttk

root = Tk()

listBox = Listbox(root, width=40, height=15, selectmode=MULTIPLE)
listBox.insert(0, "Python")
listBox.insert(1, "JavaScript")
listBox.insert(2, "C")
listBox.insert(3, "Kotlin")
listBox.pack(pady=25)


root.geometry("650x650+650+200")
root.mainloop()
