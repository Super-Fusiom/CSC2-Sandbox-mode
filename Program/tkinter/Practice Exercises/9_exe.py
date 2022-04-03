from cgitb import text
from logging import warning
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pyparsing import col

root = Tk()

# When enter is pressed
def callback():
    mbox = messagebox.askquestion('Delete', 'Are you Sure?', icon='warning')
    if mbox == 'yes':
        print('deleted')
    else:
        print('Oh ok then')

def callback2():
    messagebox.showinfo('Success', 'Well Done!')
    print('You clicked ok!!!')

button1 = ttk.Button(root, text='Delete', command=callback).grid(row=0, column=0)
button2 = ttk.Button(root, text='Info', command=callback2).grid(row=0, column=1)

root.geometry('640x480')
root.mainloop()