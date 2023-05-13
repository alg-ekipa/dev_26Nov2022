import tkinter as tk


rootWindow = tk.Tk()  # otvaramo GUI
rootWindow.geometry('600x400') # velicina ekrana, moze i bez toga
rootWindow.title('Algebra - Py dev')

#kreiranje widget Label
myLabel1 = tk.Label(rootWindow, text='Hello, world!')
myLabel2 = tk.Label(rootWindow, text='Algebra ekipa')

rootWindow.mainloop()  # sluizi da drzi prozor otvoren

#smještanja widgeta

myLabel1.pack()
myLabel2.pack()

rootWindow.mainloop()