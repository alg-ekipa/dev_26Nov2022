import tkinter as tk

#objekt koji predstavlja glavni prozor i krećemo u svijet grafičkog sučelja preko njega

rootWindow = tk.Tk() # tk je ime Taba iliti prozora
rootWindow.geometry('600x400') # odredili smo veličinu prozora
rootWindow.title('Algebra - Py Dev') # promijenili smo naslov prozora 

# kreiramo widget Label i pridljeljujemo ga nekoj vrijednosti
myLabel1 = tk.Label(rootWindow, text='Hello World!') # 1. vrijednost je lokacija 2. vrijednost je tekst Labela

myLabel2 = tk.Label(rootWindow, text='Algebra ekipa')

'''# smještanje Widgeta na GUI po defoltu je centriran i mjenja se kako se mijenja prozor
myLabel1.pack()
myLabel2.pack()'''

'''myLabel1.grid(row=0, column=0) # stavljeno u prvoj kućici na gridu 
myLabel2.grid(row=1, column=1)
'''
myLabel1.place(x=100, y=50)
myLabel2.place(x=400, y=50)

#moramo prozor staviti u nekakav loop da on uvjek bude vidljiv

rootWindow.mainloop()