import tkinter as tk

def handleSubmit():
    value = input.get()
    print(value)
    input.config(state=tk.DISABLED)

def resetText():
    input.delete(0, tk.END)

window = tk.Tk()

window.geometry("300x300")

# input
input = tk.Entry(window, font=('Arial', 12))
input.pack(side="left")

# button
button = tk.Button(window, text="Enviar", command=handleSubmit)
button.pack(side="right")

reset = tk.Button(window, text="Reset", command=resetText)
reset.pack(side="right")

window.mainloop()