from tkinter import *
from PIL import ImageTk, Image
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random

import modified



def submit():
    x1 = int(e1.get())
    x2 = e2.get()
    x3 = int(e3.get())
    n = modified.func1(x1,x3,x2)
    s = n[0]+".jpg"
    photo1 = ImageTk.PhotoImage(Image.open(s).resize((250, 250), Image.ANTIALIAS))
    panel.configure(image=photo1)
    panel.photo = photo1
        



root = Tk()
root.title("Guess the right brand for you")
frame1 = Frame(root)
img = ImageTk.PhotoImage(Image.open("ques.jpg").resize((250, 250), Image.ANTIALIAS))
panel = Label(frame1, image = img)
frame1.bind("<Button-1>", submit)
panel.pack(side = "bottom", fill = "both", expand = "yes")
frame1.grid(row=0)

frame3 = Frame(root)
label1 = Label(frame3, text="Enter your age")
label2 = Label(frame3, text="Choose gender(male/female)")
label3 = Label(frame3, text="Enter price of sport equipment")
e1 = Entry(frame3)
e2 = Entry(frame3)
e3 = Entry(frame3)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

button = Button(frame3, text="Predict" ,command=submit)
button.grid(row=3)
frame3.grid(row=2)
root.geometry("300x350+100+50")
root.resizable(width=False, height=False)
root.mainloop()
