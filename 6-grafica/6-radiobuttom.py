from tkinter import *

foods = ["pizza", "hamburguesa", "hotdog"]

def handleValue():
    if (x.get() == 0):
        print('Selecionaste una Pizza')
    elif (x.get() == 1):
        print('Seleccionaste una hamburguesa')
    elif(x.get() == 2):
        print('Seleccionaste un HotDog')
    else:
        print('Error')

window = Tk()

window.geometry("200x200")

x = IntVar()

# radio button
for index in range(len(foods)):
    radiobutton = Radiobutton(window, text=foods[index], variable=x, value=index, command=handleValue)
    radiobutton.pack(anchor=W)


window.mainloop()
