import tkinter as tk

rootWindow = tk.Tk()
rootWindow.geometry('600x400')
rootWindow.title('Algebra')

            #kreiranje widgeta Label
myLabel1 = tk.Label(rootWindow, text='Hello, world!')
myLabel2 = tk.Label(rootWindow, text='Algebra ekipa!')

            #smještanje widgeta na GUI ili jedno ili drugo (pack, grid ili place)
#myLabel1.pack()
#myLabel2.pack()

#myLabel1.grid(row=0,column=0)
#myLabel2.grid(row=1, column=1)

myLabel1.place(x=100,y=200)
myLabel2.place(x=150, y=250)

rootWindow.mainloop()