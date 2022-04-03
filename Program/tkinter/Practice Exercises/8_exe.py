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
    if chvar.get() == 1:
        print("O_O")
    else:
        print("oh ok...")
    print(gender.get())
    print(year.get())

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
lblname.grid(row=1, column=0)
lblpass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, pady=5)

chvar = IntVar()
chvar.set(0)


cbox = Checkbutton(root, text='Remeber ye info', variable=chvar, font='Arial 16').grid(row=4, column=0)

#Gender check
gender = StringVar()

ttk.Radiobutton(root, text="Female", value="Female" , variable=gender).grid(row=5, column=0)
ttk.Radiobutton(root, text="Male", value="Male" , variable=gender).grid(row=5, column=1)
ttk.Radiobutton(root, text="Attack Helicopter", value="Attack Helicopter" , variable=gender).grid(row=5, column=2)


#Dropdown menu
months = StringVar()
ComboBox = ttk.Combobox(root, textvariable=months, 
values=('Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'),
state='readonly').grid(row=6,column=0)

#Spinbox

year = StringVar()
Spinbox(root, from_=1990, to=2022, textvariable=year).grid(row=6, column=1)



#As always...
root.geometry('400x300')
root.mainloop()