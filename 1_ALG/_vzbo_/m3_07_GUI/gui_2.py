from tkinter import *



root = Tk()
root.geometry('600x400')

def klik_gumba():
    #print('Gumbek je kliknut!')
    ispis_label = Label(root, text='Gumbek je kliknut!')
    ispis_label.grid(row=1, column=1)

temperatura_label = Label(root, text='Temperatura: ', bg='#33F3FF')
unos_temp_entry = Entry(root)
ispis_button = Button(root, text='Ispis poruke', fg='white', bg='#C133FF',command=klik_gumba)

temperatura_label.grid(row=0, column=0, padx=20, pady=20)

unos_temp_entry.grid(row=0, column=1)

ispis_button.grid(row=1, column=0)


root.mainloop()