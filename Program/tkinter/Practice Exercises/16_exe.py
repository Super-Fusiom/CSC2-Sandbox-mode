from tkinter import *
from tkinter import ttk

root = Tk()

def printr():
    val = entry.get()
    listBox.insert("end",val)
def deleter():
    listBox.delete("end")

listBox = Listbox(root, width=40, height=15, selectmode=MULTIPLE)
listBox.insert(0, "Python")
listBox.insert(1, "JavaScript")
listBox.insert(2, "C")
listBox.insert(3, "Kotlin")
listBox.pack(pady=25)

button = ttk.Button(root, text='Print', command=printr).place(x=253, y=300)
button2 = ttk.Button(root, text='Delete', command=deleter).place(x=323, y=300) 

entry = ttk.Entry(root)
entry.pack(pady=10)

root.geometry("650x400+650+200")
root.mainloop()