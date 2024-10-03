from tkinter import *

def handleSubmit():
    selection = var.get()
    print(selection)

window = Tk()
window.geometry('500x500')

var = DoubleVar()

scale = Scale(window, variable=var, length=200,orient=HORIZONTAL, tickinterval=10, resolution=10)
scale.pack(anchor=CENTER)

button = Button(window, text="Enviar", command=handleSubmit)
button.pack()

window.mainloop()