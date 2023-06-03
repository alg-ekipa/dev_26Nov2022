from tkinter import *

root = Tk()

# FUNKCIJE

def add_number(number): 
    num = tip_entry.get() # getamo što tipnemo i stavljamo u varijablu num
    tip_entry.delete(0, END)
    tip_entry.insert(0, num+number)


# SMJEŠTAJ NA GUI

frameTIP = LabelFrame(root, text='Tipkovnica', padx=30, pady=30)
frameTIP.grid(row=0, column=0)

tip_entry = Entry(frameTIP)
tip_entry.grid(row=0, column=0, columnspan=3, padx=30, pady=30)

button0 = Button(frameTIP, text='1', padx=40, pady=20, command=lambda: add_number('1'))
button0.grid(row=1, column=0)

button1 = Button(frameTIP, text='2', padx=40, pady=20, command=lambda: add_number('2'))
button1.grid(row=1, column=1)

button2 = Button(frameTIP, text='3', padx=40, pady=20, command=lambda: add_number('3'))
button2.grid(row=1, column=2)

button3 = Button(frameTIP, text='4', padx=40, pady=20, command=lambda: add_number('4'))
button3.grid(row=2, column=0)

button4 = Button(frameTIP, text='5', padx=40, pady=20, command=lambda: add_number('5'))
button4.grid(row=2, column=1)

button5 = Button(frameTIP, text='6', padx=40, pady=20, command=lambda: add_number('6'))
button5.grid(row=2, column=2)

button6 = Button(frameTIP, text='7', padx=40, pady=20, command=lambda: add_number('7'))
button6.grid(row=3, column=0)

button7 = Button(frameTIP, text='8', padx=40, pady=20, command=lambda: add_number('8'))
button7.grid(row=3, column=1)

button8 = Button(frameTIP, text='9', padx=40, pady=20, command=lambda: add_number('9'))
button8.grid(row=3, column=2)

button9 = Button(frameTIP, text='0', padx=40, pady=20, command=lambda: add_number('0'))
button9.grid(row=4, column=0, columnspan=3)



root.mainloop()