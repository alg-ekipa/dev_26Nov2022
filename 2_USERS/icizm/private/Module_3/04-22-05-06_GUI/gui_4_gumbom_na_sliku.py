from tkinter import *

root = Tk()
root.geometry('600x400')

img_py = PhotoImage(file='python-logo.png').subsample(4) # .subsample smanji sample iliti slikuS

label_poruka = Label(root, text = 'Poruka', font=('Segoe UI', 16)) #u font se unosi ntorka jer može imati više obilježja

label_slika = Label(root, text= 'Tekst na slici', 
                    font=('Segoe UI', 20),
                    compound=CENTER,
                    image = img_py)

label_poruka.pack(pady=10)
label_slika.pack(pady=10)





root.mainloop()