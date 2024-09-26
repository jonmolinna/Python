from tkinter import *

def monstrar():
    if (x.get() == 1):
        print('Estas de acuerdo')
    else:
        print('No estas de acuerdo')

window = Tk()

window.geometry("300x300")

x = IntVar()

# Checkbox
checkbox = Checkbutton(window, text="Acepto", variable=x, onvalue=1, offvalue=0, command=monstrar)
checkbox.pack()

window.mainloop()