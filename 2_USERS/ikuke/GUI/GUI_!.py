from tkinter import *
import tkinter as tk





rootWindow = tk.Tk()
rootWindow.title("Algebra")


def klik_gumba():
    print ('Gumbek je kliknut')    



myLabel1=tk.Label(rootWindow, text= "Algebra ekipa")
rootWindow.geometry('600x400')

myLabel1.grid(row =0, column= 1)

tk.Button(rootWindow, text = "Hello World ", command=klik_gumba).grid(row=1, column=3)
tk.Button(rootWindow, text = "Hello World2", bg="blue").grid()
tk.Button(rootWindow, text = "Hello World3", bg="green",fg= "yellow").grid()

tempertura_label= Label( rootWindow, text = 'Temperatura: ')
unos_temp_entry= Entry(rootWindow)

tempertura_label.grid(row=5, column= 1)

unos_temp_entry.grid(row=5, column= 2)
tempertura_label.grid(row=6, column= 1)



rootWindow.mainloop()