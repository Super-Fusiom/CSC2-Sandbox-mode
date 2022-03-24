from tkinter import *
from tkinter import ttk

root=Tk()
def callback():
    val1=entry.get()
    val2=entry2.get()
    print("Your name is: " + val1)
    print("Your password is: " + val2)

label = Label(root, text="Name")
label.config(justify=("center"))

label2 = Label(root, text="Password")
label2.config(justify=("center"))


entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=20)
entry.insert(0, "")
entry2.config(show='*')

button = ttk.Button(root, text='Display AWAY', command=callback)

entry.config(justify='center')
label.pack()
entry.pack()
label2.pack()
entry2.pack()
button.pack()

root.mainloop()