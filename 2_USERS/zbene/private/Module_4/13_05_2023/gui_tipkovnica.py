from tkinter import *

root = Tk()

#FUNKCIJE
def add_number(number):
    num = tip_entry.get()
    tip_entry.delete(0,END)
    tip_entry.insert(0,num+number)

frameTIP = LabelFrame (root, text='Tipkovnica', padx=40, pady= 40)
frameTIP.grid(row=0, column=0)

tip_entry = Entry(frameTIP)
tip_entry.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

button0 = Button (frameTIP, text='0', padx=40, pady= 20, command=lambda: add_number('0'))
button0.grid(row=0, column=0)

button0 = Button (frameTIP, text='1', padx=40, pady= 20, command=lambda: add_number('1'))
button0.grid(row=0, column=1)

button0 = Button (frameTIP, text='2', padx=40, pady= 20, command=lambda: add_number('2'))
button0.grid(row=0, column=2)

button0 = Button (frameTIP, text='3', padx=40, pady= 20, command=lambda: add_number('3'))
button0.grid(row=1, column=0)

button0 = Button (frameTIP, text='4', padx=40, pady= 20, command=lambda: add_number('4'))
button0.grid(row=1, column=1)

button0 = Button (frameTIP, text='5', padx=40, pady= 20, command=lambda: add_number('5'))
button0.grid(row=1, column=2)

button0 = Button (frameTIP, text='6', padx=40, pady= 20, command=lambda: add_number('6'))
button0.grid(row=2, column=0)

button0 = Button (frameTIP, text='7', padx=40, pady= 20, command=lambda: add_number('7'))
button0.grid(row=2, column=1)

button0 = Button (frameTIP, text='8', padx=40, pady= 20, command=lambda: add_number('8'))
button0.grid(row=2, column=2)

root.mainloop()