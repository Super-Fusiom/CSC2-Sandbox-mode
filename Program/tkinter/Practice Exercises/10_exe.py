from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import _Padding

root = Tk()

# When enter is pressed
def callback():
    exit()

def callback2():
    print()


# create entries and buttons
button1 = ttk.Button(root, text="Quit", command=callback)
button2 = ttk.Button(root, text='Print', command=callback2)
lblentry = ttk.Label(root, text='First Name')
lblentry2 = ttk.Label(root, text='Last name')
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

#Position of 
button1.grid(row=0, column=0, pady=5)
button2.grid(row=0, column=1, pady=5)


#As always...
root.geometry('400x300')
root.mainloop()