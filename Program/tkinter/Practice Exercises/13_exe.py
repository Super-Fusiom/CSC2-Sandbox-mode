from sqlite3 import paramstyle
from tkinter import *
from tkinter import ttk

root = Tk()

progbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progbar.pack(pady=20)
progbar.config(mode='indeterminate')
#Start of progress bar
progbar.start()
progbar.stop()
# say to go up to 50 and increase by 10
progbar.config(mode='determinate', maximum=50.0, value=10.0)
progbar.start()
progbar.stop()

# adding value to progress bar
value = DoubleVar()

# config the progress bar to show the value when it is run
progbar.config(variable=value)

scale = ttk.Scale(root, orient=HORIZONTAL, length=200, var=value, from_=0.0, to=50.0)

scale.pack()

root.geometry("450x450+650+350")
root.mainloop()
