from tkinter import *

root = Tk()

root.title('Ime i prezime')
root.geometry('600x400')

def submit():
    ime = ime_var.get()
    prezime = prezime_var.get()

    print(f'Username: {ime}, Password: {prezime}')

    ime_var.set('')
    prezime_var.set('')
    

ime_var = StringVar()
prezime_var = StringVar()

ime_label = Label(root, text='Ime', font=('calibre', 10, 'bold'))
ime_label.grid(row=0, column=0)

ime_entry = Entry(root, textvariable=ime_var, font=('calibre', 10, 'normal') )
ime_entry.grid(row=0, column=1)

prezime_label = Label(root, text='Prezime', font=('calibre', 10, 'bold'))
prezime_label.grid(row=1, column=0)

#unos prezimena , show='*' ) )  dodatak koji maskira slova
#prezime_entry = Entry(root, textvariable=prezime_var, font=('calibre', 10, 'normal'), show='*' )
prezime_entry = Entry(root, textvariable=prezime_var, font=('calibre', 10, 'normal'))
prezime_entry.grid(row=1, column=1)

submit_button = Button(root, text='Submit', command=submit)
submit_button.grid(row=2,column=1)

root.mainloop()