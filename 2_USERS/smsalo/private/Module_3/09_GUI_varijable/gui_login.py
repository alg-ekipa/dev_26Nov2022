from tkinter import *

root=Tk()
root.geometry('600x400')
root.title('Login')

def submit():
    ime_korisnik=ime.get()
    lozinka_korisnik=lozinka.get()

    print(f'User name: {ime_korisnik}, Lozinka: {lozinka_korisnik}')
    ime.set('')
    lozinka.set('')

ime=StringVar()
lozinka=StringVar()

ime_oznaka = Label(root, text='Korisničko ime: ', font=('Arial',10, 'bold'))
lozinka_oznaka = Label(root, text='Lozinka: ',font=('Arial',10, 'normal'))

ime_oznaka.grid(row=0, column=0, padx=5, pady=10)
lozinka_oznaka.grid(row=1, column=0, padx=5, pady=5)

entry_ime =Entry(root, textvariable=ime)
entry_ime.grid(row=0, column=1)

entry_lozinka =Entry(root, textvariable=lozinka, show='*')
entry_lozinka.grid(row=1, column=1)

submit_button=Button(root, text='Submit', command=submit)
submit_button.grid(row=2, column=1)

root.mainloop()