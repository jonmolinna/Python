from tkinter import *

def clickMe():
    print('Submit...')


windows = Tk()

windows.geometry("500x500")

# Button
button = Button(windows, text='Click me', font=('Arial', 10, 'bold'), width=10, height=5, command=clickMe, state='disabled')
button.pack()

windows.mainloop()