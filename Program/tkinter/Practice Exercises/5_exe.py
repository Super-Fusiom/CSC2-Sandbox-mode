from cgitb import text
from tkinter import *
from tkinter import ttk

from pyparsing import col

root = Tk()

# When enter is pressed
def callback():
    val1 = entry.get()
    val2 = entry2.get()

    print("Your Name is: " + val1)
    print("Your Password is: " + val2)


# create entries
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

#placeholder
entry2.config(show='*')

#button and label creation
button = ttk.Button(root, text='Enterrr', command=callback)
lbltitle = ttk.Label(root, text='TITTTTLE', font=(('Verdana'), 22))
lblname = ttk.Label(root, text="Your name :")
lblpass = ttk.Label(root, text='Your pazzword :')

#Adjusting position
lbltitle.grid(row=0, column=0, columnspan=2, pady=10)
lblname.grid(row=1, column=0, sticky=W+E)
lblpass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, pady=5)


#As always...
root.geometry('400x300')
root.mainloop()