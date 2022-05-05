from tkinter import *
from tkinter import ttk

# There will be 2 functions in this program; one for exit and other to calculate
def calculate():
    length = lengthi.get()
    height = heighti.get()
    width = widthi.get()
    area = length * width
    areai.set(area)
    prpost = (length + 1)* width
    cementi.set(round(prpost))
    prposti.set(round(prpost))
    if height <= 1:
        lposts = 1.8
    else:
        lposts = 2.4
    lpostsi.set(lposts)
    bearers = area * 2
    bearersi.set(bearers)
    joists = area/0.4
    joistsi.set(joists)
    decking = area * 11
    deckingi.set(decking)

def quit():
    exit()

root = Tk()
root.title("Decker calculator")
# Input variables; i means input
lengthi = DoubleVar()
heighti = DoubleVar()
widthi = DoubleVar()

# Label and input boxes for the inputs
length_txt = ttk.Label(root, text="Length: ")
height_txt = ttk.Label(root,  text="Height: ")
width_txt = ttk.Label(root, text='Width: ')
width_input = ttk.Entry(root, textvariable=widthi, width=30)
height_input = ttk.Entry(root,textvariable=heighti, width=30)
length_input = ttk.Entry(root, textvariable=lengthi, width=30)

# Buttons to quit and to caculate
quitter = ttk.Button(root, text="Quit", command=quit)
caculate = ttk.Button(root, text="Caculate", command=calculate)
# Result variables
areai = DoubleVar()
prposti = DoubleVar()
lpostsi = DoubleVar()
cementi = DoubleVar()
bearersi = DoubleVar()
joistsi = DoubleVar()
deckingi = DoubleVar()
# Result labels 
area_txt = ttk.Label(root, text="Area: ")
posts_q_txt = ttk.Label(root, text="Post quantity: ")
post_length_txt = ttk.Label(root, text="Post length: ")
cement_txt =  ttk.Label(root, text="Cement Bags: ")
bearers_txt = ttk.Label(root, text="Bearers: ")
joints_txt = ttk.Label(root, text="Joints: ")
decking_txt = ttk.Label(root, text="Decking: ")
# Results...
area_output = ttk.Label(root, textvariable=areai)
posts_q_output = ttk.Label(root, textvariable=prposti)
post_length_output = ttk.Label(root, textvariable=lpostsi)
cement_output =  ttk.Label(root, textvariable=cementi)
bearers_output = ttk.Label(root, textvariable=bearersi)
joints_output = ttk.Label(root, textvariable=joistsi)
decking_output = ttk.Label(root, textvariable=deckingi)

#Grid Placement

# length, width and height input and label
length_txt.grid(row=1, column=0)
width_txt.grid(row=2, column=0)
height_txt.grid(row=3, column=0)
length_input.grid(row=1,column=1)
width_input.grid(row=2, column=1)
height_input.grid(row=3, column=1)
#Result labels
area_txt.grid(row=5, column=0)
posts_q_txt.grid(row=6, column=0)
post_length_txt.grid(row=7, column=0)
cement_txt.grid(row=8,column=0)
bearers_txt.grid(row=9, column=0)
joints_txt.grid(row=10, column=0)
decking_txt.grid(row=11, column=0)
#Result output
area_output.grid(row=5, column=1)
posts_q_output.grid(row=6, column=1)
post_length_output.grid(row=7, column=1)
cement_output.grid(row=8,column=1)
bearers_output.grid(row=9, column=1)
joints_output.grid(row=10, column=1)
decking_output.grid(row=11, column=1)
#buttons
quitter.grid(row=0,column=0)
caculate.grid(row=0,column=1)

# The answer to your question is 42

root.geometry('250x250')
root.mainloop()