from tkinter import *
from tkinter import ttk

def quit():
    exit()

root = Tk()
root.title('Sunshine adventure camp')

def update():
    print('update')
    printe()

# Python will give me an error if i did print...
def printe():
    print('updated and printed')
def delete():
    print('delete')

# The buttons
updatebtn = ttk.Button(root, text="Update", command=update)
quitbtn = ttk.Button(root, text="Quit", command=quit)
delbtn = ttk.Button(root, text="Delete", command=delete)
#Entrys
GLEntry = ttk.Entry(root)
CEntry = ttk.Entry(root)
WEntry = ttk.Entry(root)
LEntry = ttk.Entry(root)

# Labels
GLlabel = ttk.Label(root, text='Group Leader')
CLabel = ttk.Label(root, text='Num of campers')
WLabel = ttk.Label(root, text='Weather Conditions')
Llabel = ttk.Label(root, text='Location')

# Entry Placement
GLEntry.grid(row=1, column=0)
CEntry.grid(row=1, column=1)
WEntry.grid(row=1, column=2)
Llabel.grid(row=1, column=3)
# button placement
updatebtn.grid(row=0, column=0)
quitbtn.grid(row=0, column=1)
# Label placement
GLlabel.grid(row=2, column=0, padx=10)
CLabel.grid(row=2, column=1, padx=10)
WLabel.grid(row=2, column=2, padx=10)
Llabel.grid(row=2, column=3, padx=10)
# Yup the same thing again

root.geometry('500x500')
root.mainloop()
