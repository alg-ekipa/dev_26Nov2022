from tkinter import *

root=Tk()
root.geometry('600x400')

def klik_gumba():
    #print('Gumbek je kliknut!')
    ispis_label=Label(root, text='Gumbek je kliknut!')
    ispis_label.grid(row=1, column=1)

temperatura_label=Label(root, text='Temperatura: ', bg='red', fg='blue')
unos_temp_entry=Entry(root)
ispis_button=Button(root, text='Ispis poruke', bg='purple', fg='green', command=klik_gumba)

temperatura_label.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=20)

unos_temp_entry.grid(row=0, column=1)

ispis_button.grid(row=1, column=0)



root.mainloop()