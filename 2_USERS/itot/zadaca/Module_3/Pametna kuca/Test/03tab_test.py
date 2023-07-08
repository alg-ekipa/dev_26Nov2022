'''
TODO:

'''

import tkinter as tk
from tkinter import *
from tkinter import ttk # ttk module which contains the Notebook widget


root = tk.Tk() # parent window
root.title('Pametna kuca') #Naslov peret windowa
tabControl = ttk.Notebook(root)  #Creating Tab Control
dnevni_boravak = ttk.Frame(tabControl) #Creating the tabs
hodnik = ttk.Frame(tabControl)
tabControl.add(dnevni_boravak, text='Dnevni Boravak')#Adding the tab
tabControl.add(hodnik, text='Hodnik')
tabControl.pack(expand=1, fill="both") #Packing the tab control to make the tabs visible

#Creating Label widget as a child of the parent window (root)
ttk.Label(dnevni_boravak, 
          text ='Welcome to \
          GeeksForGeeks').grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  

ttk.Label(hodnik,
          text ='Lets dive into the \
          world of computers').grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)


root.mainloop()