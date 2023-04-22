from tkinter import *

root = Tk()
root.geometry('600x600')
slika=PhotoImage(file='python-logo.png').subsample(10)

label_poruka = Label(root, text='Poruka', font=('Segoe UI',16))

label_slika = Label(root, text='Logo', 
                    font=('Verdana', 20),
                    compound=LEFT,
                    image =slika)
label_poruka.pack(pady=10)
label_slika.pack(pady=10)

root.mainloop()