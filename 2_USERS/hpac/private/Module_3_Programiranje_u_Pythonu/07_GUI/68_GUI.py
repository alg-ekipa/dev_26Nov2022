from tkinter import *

root = Tk()
root.geometry('800x500')

def klik_gumba():
    print('Gumbek je kliknut')
    ispis_label = Label(root, text='Gumbek je kliknuti!!!!')
    ispis_label.grid(row=1, column=1)


temperatura_label = Label(root, text='Temperatura: ', bg='light grey', fg='black')
unos_temp_entry = Entry(root)
ispis_button = Button(root, text='Ispis poruke', command=klik_gumba, bg='red', fg='white')

temperatura_label.grid(row=0, column=0, ipadx=20, ipady=20)
unos_temp_entry.grid(row=0, column=1)
ispis_button.grid(row=1, column=0)

root.mainloop()