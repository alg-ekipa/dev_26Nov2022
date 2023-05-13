from tkinter import *

root = Tk()
root.geometry('600x400')

# komanda koju ćemo staviti u button
def klik_gumba(): 
    #print('Gumbek je kliknut!') # naredba vezana uz standardni izlaz i pojaviti će se samo u Terminalu
    ispis_label = Label(root, text='Gumbek je kliknut!')
    ispis_label.grid(row=1, column=1)


temperatura_label = Label(root, text='Temperatura: ', bg='#F12345', fg='white') 
unos_temp_entry = Entry(root) # Widget koji je prozorčić za unos podataka


#zgodno je koristiti gridanje jer želimo da nam budu jedan za drugim 

temperatura_label.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=20) # pad je da se doda prostor oko teksta kao rub ipadx od recimo ruba ćelije pa dalje
ispis_button = Button(root, text='Ispis poruke', command=klik_gumba, bg='black', fg='white')

unos_temp_entry.grid(row=0, column=1)
ispis_button.grid(row=1, column=0)


# postavljeni u redu jedan za drugim



root.mainloop()