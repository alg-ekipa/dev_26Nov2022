from tkinter import *
import tkinter as tk
from tkinter  import messagebox


root=tk.Tk()
root.geometry('600x400')
root.title('Smart Key')
def pozvoni():
    messagebox.showinfo('Prestani zvoniti!')


frame_naslov=LabelFrame(root, text='Key')

b1=Button(frame_naslov, text='Zvono', command=pozvoni)
b2=Button(frame_naslov, text='Otkljucaj')

frame_naslov.grid(row=0, column=0, padx=10, pady=10)
b1.grid(row=0, column=0, pady=10, padx=10)
b2.grid(row=0, column=1, padx=10, pady=10)







root.mainloop()
