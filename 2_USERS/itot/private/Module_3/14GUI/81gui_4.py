from tkinter import *

root = Tk()
root.geometry('600x400')

img_py = PhotoImage(file='C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/13fotodatoteke/python-logo.png')

label_poruka = Label(root, text='Poruka', font=('Segoe UI',16))

label_slika = Label(root, text='text na slici',
                    font=('Segoe UI',20),
                    compound=CENTER,
                    image= img_py)


label_poruka.pack(pady=10)
label_slika.pack(pady=10)

root.mainloop()