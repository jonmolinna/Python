from tkinter import *

def handleSubmit():
    # selection = listbox.get(listbox.curselection())
    # print(selection)
    soda = []

    for index in listbox.curselection():
        soda.insert(index, listbox.get(index))

    for index in soda:
        print(index)

def addSubmit():
    listbox.insert(listbox.size(), input.get())
    listbox.config(height=listbox.size())

def deleteHandle():
    # listbox.delete(listbox.curselection())

    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

window = Tk()
window.geometry("500x500")

listbox = Listbox(window, font=("Arial", 15), selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Coca Cola")
listbox.insert(2, 'Inca Kola')
listbox.insert(3, 'Pepsi')

listbox.config(height=listbox.size())

input = Entry(window)
input.pack()

button = Button(window, text="Enviar", command=handleSubmit)
button.pack()

addButton = Button(window, text="Añadir", command=addSubmit)
addButton.pack()

deleteButton = Button(window, text='Eliminar', command=deleteHandle)
deleteButton.pack()


window.mainloop()