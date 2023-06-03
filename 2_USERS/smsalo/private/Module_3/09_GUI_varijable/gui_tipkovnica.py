from tkinter import *

root=Tk()

#funkcija

def dod_broj(broj):
    br = tip_entry.get()
    tip_entry.delete(0, END)
    tip_entry.insert(0, br+broj)

#GUI

frameTIP=LabelFrame(root, text='Tipkovnica', padx=30, pady=30)
frameTIP.grid(row=0, column=0)

tip_entry=Entry(frameTIP)
tip_entry.grid(row=4, columnspan=3, column=0, padx=10, pady=10)

button0=Button(frameTIP, text='0', padx=40, pady=40, command=lambda: dod_broj('0'))
button0.grid(row=0, column=0)

button1=Button(frameTIP, text='1', padx=40, pady=40, command=lambda: dod_broj('1'))
button1.grid(row=0, column=1)

button2=Button(frameTIP, text='2', padx=40, pady=40, command=lambda: dod_broj('2'))
button2.grid(row=0, column=2)

button3=Button(frameTIP, text='3', padx=40, pady=40, command=lambda: dod_broj('3'))
button3.grid(row=1, column=0)

button4=Button(frameTIP, text='4', padx=40, pady=40, command=lambda: dod_broj('4'))
button4.grid(row=1, column=1)

button5=Button(frameTIP, text='5', padx=40, pady=40, command=lambda: dod_broj('5'))
button5.grid(row=1, column=2)

button6=Button(frameTIP, text='6', padx=40, pady=40, command=lambda: dod_broj('6'))
button6.grid(row=2, column=0)

button7=Button(frameTIP, text='7', padx=40, pady=40, command=lambda: dod_broj('7'))
button7.grid(row=2, column=1)

button8=Button(frameTIP, text='8', padx=40, pady=40, command=lambda: dod_broj('8'))
button8.grid(row=2, column=2)

button9=Button(frameTIP, text='9', padx=40, pady=40, command=lambda: dod_broj('9'))
button9.grid(row=3, column=1)

root.mainloop()