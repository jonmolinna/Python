from tkinter import *
from tkinter import messagebox

def handleSubmit():
    # messagebox.showinfo(title="Confirm", message="Se registro con exito")
    selection = messagebox.askokcancel("Confirm", message="¿Eliminar usuario?")

    if (selection):
        print("Se elimino el usuario")


window = Tk()

window.geometry("500x500")

button = Button(window, text="Enviar", command=handleSubmit)
button.pack()


window.mainloop()