import tkinter as tk

rootWindow = tk.Tk()
rootWindow.geometry('600x400')
rootWindow.title('Alg-ekipa')

#  kriranje widgeta Label
myLabel1 = tk.Label(rootWindow, text='Hello World')
myLabel2 = tk.Label(rootWindow, text='Alg-ekipa')

# smještanje widgeta na GUI
'''
myLabel1.pack()
myLabel2.pack()

#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)
'''

myLabel1.place(x=100,y=50)
myLabel2.place(x=450,y=50)



rootWindow.mainloop()