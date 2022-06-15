# importing whole module 

from tkinter import *
from tkinter.ttk import *

# importing strftime function to retrive system's time 

from time import strftime

# creating tkinter window

root = Tk()
root.title('Clocks')

# This function is used to display time on the label

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

# styling the label widget 

lbl = Label(root, font = ('Calibri',40,'bold'),
                        background ='powder blue',
                        foreground = 'black')

# placing clock at the center of the window

lbl.pack(anchor = 'center')
time()
mainloop()

