from tkinter import *
from tkinter import ttk

def quit():
    exit()

root = Tk()
root.title('Sunshine adventure camp')
# The buttons
updatebtn = ttk.Button(root, text="Update")
quitbtn = ttk.Button(root, text="Quit", command=quit)
delbtn = ttk.Button(root, text="Delete")
printbtn = ttk.Button(root, text="Print")
# Labels
GLlabel = ttk.Label(root, text='Group Leader')
CLabel = ttk.Label(root, text='Num of campers')
WLabel = ttk.Label(root, text='Weather Conditions')
Llabel = ttk.Label(root, text='Location')

# button placement
updatebtn.grid(row=0, column=0)
printbtn.grid(row=0, column=1)
quitbtn.grid(row=0, column=3)

# Yup the same thing again

root.geometry('270x270')
root.mainloop()