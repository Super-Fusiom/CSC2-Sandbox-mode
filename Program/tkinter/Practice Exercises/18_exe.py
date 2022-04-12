from tkinter import *
from tkinter import ttk

# There will be 2 functions in this program; one for exit and other to calculate
def calculate():
    length = length_input.get
    height = height_input.get
    width = width_input.get
    area = length * width
    prpost = (length + 1)* width
    if height <= 1:
        lposts = 1.8
    else:
        lposts = 2.4
    bearers = area * 2
    joists = area/0.4
    decking = area * 11



def quit():
    exit()

root = Tk()
root.title("Decker calculator")


#Label and input boxes for the inputs
length_txt = ttk.Label(root, text="Length: ")
height_txt = ttk.Label(root, text="Height: ")
width_txt = ttk.Label(root, text='Width: ')
width_input = ttk.Entry(root, width=30)
height_input = ttk.Entry(root, width=30)
length_input = ttk.Entry(root, width=30)
# Buttons to quit and to caculate
quitter = ttk.Button(root, text="Quit", command=quit)
caculate = ttk.Button(root, text="Caculate", command=calculate)

area_txt = ttk.Label(root, text="Area: ")
posts_q_txt = ttk.Label(root, text="Post quantity: ")
post_length_txt = ttk.Label(root, text="Post length: ")
cement_txt =  ttk.Label(root, text="Cement Bags: ")
bearers_txt = ttk.Label(root, text="Bearers: ")
joints_txt = ttk.Label(root, text="Joints: ")
decking_txt = ttk.Label(root, text="Decking: ")

# length, width and height input and label
length_txt.grid(row=1, column=0)
width_txt.grid(row=2, column=0)
height_txt.grid(row=3, column=0)
length_input.grid(row=1,column=1)
width_input.grid(row=2, column=1)
height_input.grid(row=3, column=1)




root.mainloop()


