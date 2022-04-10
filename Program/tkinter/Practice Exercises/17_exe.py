from tkinter import *

root = Tk()
root.title("IMAGGGGE")
# For tiling wm, this doesn't do anything
root.geometry("350x350")

lbl_text = Label(root, text="IMAGE", font=(("Times"), 18))
lbl_text.pack()

logo = PhotoImage(file='icons/lightbulb.png')

lbl_image = Label(root, image=logo)
lbl_image.pack()

root.mainloop()