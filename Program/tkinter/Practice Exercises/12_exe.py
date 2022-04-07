from tkinter import *
root = Tk()

root.title("Frames")

"""Chreate frame  using frame constructor 
method to make frame visible - use bg 
(background colour)"""

frame = Frame(root, height=300, width=300, bg='green', bd=7, relief=SUNKEN)

frame.pack(fill=X) # using geometry manager for frame
button1=Button(frame,text="Baffon")
button2=Button(frame, text="Free CSGO SKINS")
searchBar= LabelFrame(root, text="Search Box", bg='blue')
searchlbl= Label(searchBar, text="Search", padx=10)
searchent= Entry(searchBar)
searhcbtn=Button(searchBar, text="Search")

button1.pack(side=LEFT, padx=20, pady=50)
button2.pack(side=LEFT, padx=20, pady=50)
searchlbl.pack(side=LEFT, padx=10)
searchBar.pack(padx=20, pady=20)
searchent.pack(side=LEFT, padx=10)
searhcbtn.pack(side=LEFT, padx=10, pady=10)

root.geometry('650x650+450+200')
root.mainloop()
