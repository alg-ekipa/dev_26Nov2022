from tkinter import *

def klik_gumba():
    print('Gumb je kliknut')        #ispis na terminalu
    ispis_label = Label(root, text='Gumbek je kliknut')     #ispis na prozoru
    ispis_label.grid(row=1, column=1)


root=Tk()
root.geometry('600x600')
root.title('Tablica')

temperatra_label=Label(root, text='Temperatura', bg='#d8a9f8', fg='blue')
unos_temp_entry=Entry(root)
ispis_button=Button(root, text='Ispis poruke', command=klik_gumba, bg='gray')


temperatra_label.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=20)        #pad razmak unutar čelije, ipad razmak prema van od rubova
unos_temp_entry.grid(row=0, column=1)

ispis_button.grid(row=1, column=0)

root.mainloop()