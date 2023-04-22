from tkinter import *

root=Tk()
root.geometry('600x400')

img_py=PhotoImage(file='C:/Users/danij/Downloads/dev_26Nov2022/1_ALG/_vzbo_/m3_05_fotodatoteke/python-logo.png').subsample(18)

label_poruka=Label(root, text='Poruka',font=('Segoe UI', 16))

label_slika=Label(root, text='Tekst na slici',
                  font=('Segoe UI', 20),
                  compound=CENTER, 
                  image=img_py)

label_poruka.pack(pady=10)
label_slika.pack(pady=10)





root.mainloop()