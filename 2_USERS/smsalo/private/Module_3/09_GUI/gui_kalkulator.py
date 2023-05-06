from tkinter import *

root=Tk()
root.geometry('225x150')
root.title('Alg-ekipa Kalkulator')

def zbroji():
    entry_rezultat.delete(0,END)
    broj_1 = int(entry_1br.get())            #sve povučeno s get je TYPE STRING!!!
    broj_2 = int(entry_2br.get())
    zbroj = broj_1+broj_2
    entry_rezultat.insert(END, str(zbroj))           #vratitit u string za ispis

def handle_oduzmi(event):
    entry_rezultat.delete(0,END)
    broj_1 = int(entry_1br.get())            #sve povučeno s get je TYPE STRING!!!
    broj_2 = int(entry_2br.get())
    razlika = broj_1-broj_2
    entry_rezultat.insert(END, str(razlika))           #vratitit u string za ispis



# smještaj elemenata na GUI

oznaka_1br = Label(root, text='Prvi broj: ')
oznaka_2br = Label(root, text='Drugi broj: ')

oznaka_1br.grid(row=0, column=0, padx=5, pady=10)
oznaka_2br.grid(row=1, column=0, padx=5, pady=5)

entry_1br =Entry(root)
entry_1br.grid(row=0, column=1)

entry_2br =Entry(root)
entry_2br.grid(row=1, column=1)

gumb_zbroj=Button(root, text='ZBROJ',bg='#CDD4F3', font=('Arial',10), command=zbroji)    #povezati gumb s funkcijom
gumb_zbroj.grid(row=2, column=0)

gumb_oduzmi=Button(root, text='RAZLIKA', bg='#CDD4F3', font=('Arial',10))
gumb_oduzmi.grid(row=2, column=1, padx=5, pady=5)
gumb_oduzmi.bind('<Button-1>', handle_oduzmi)           #povezivanje eventa, lijevi klik miša s funkciom oduzmi


oznaka_rezultat=Label(root, text='REZULTAT=', font=('Arial',10))
oznaka_rezultat.grid(column=0, row= 3)

entry_rezultat=Entry(root)
entry_rezultat.grid(column=1, row= 3)


root.mainloop()