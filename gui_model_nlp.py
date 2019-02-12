from tkinter import *
from PIL import ImageTk, Image
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random
import os
import subprocess
import modified_nlp
import test
import time




def submit():
    x1 = e1.get()
    n = modified_nlp.func1(x1)
    s = str(n) + ".jpg"
    photo1 = ImageTk.PhotoImage(Image.open(s).resize((350, 350), Image.ANTIALIAS))
    panel.configure(image=photo1)
    panel.photo = photo1
    if n==1:
        subprocess.call(" python gui_model.py 1", shell=True)
        



root = Tk()
root.title("Guess the right brand for you")
frame1 = Frame(root)
img = ImageTk.PhotoImage(Image.open("prob.png").resize((350, 350), Image.ANTIALIAS))
panel = Label(frame1, image = img)
frame1.bind("<Button-1>", submit)
panel.pack(side = "bottom", fill = "both", expand = "yes")
frame1.grid(row=0)

frame3 = Frame(root)
label1 = Label(frame3, text="Enter your feedback of brand you are currently using::")
e1 = Entry(frame3)

label1.grid(row=0,column=0)

e1.grid(row=0,column=1)

button = Button(frame3, text="Check for Solution" ,command=submit)
button.grid(row=3)

frame3.grid(row=2)
root.geometry("430x400+100+50")
root.resizable(width=False, height=False)
root.mainloop()
