from tkinter import * 
from tkinter import messagebox

root=Tk()
root.title('Zvono')


def pozvoni():
    messagebox.showinfo('Zvoni!')

def otkljucaj():
    frame_kljuc= LabelFrame(root, text='Otključaj', padx=50, pady=50)
    frame_kljuc.grid(row=1, column=0, padx=50, pady=50)
    gubm=Button(frame_kljuc, text='gumb')
    gubm.grid(row=2,column=0)

frame_pocetni=Frame(root)
frame_pocetni.grid(row=0, column=0, padx=50, pady=50)

label_frame_pocetni=LabelFrame(frame_pocetni, text='Ulaz', bd=1 )
label_frame_pocetni.grid(row=0, column=0)

btn_zvono = Button(frame_pocetni, text='ZVONO', padx=30, command=pozvoni)         
btn_otkljucaj = Button(frame_pocetni, text='OTKLJUČAJ', padx=30, command=otkljucaj)

btn_zvono.grid(row=0, column=1, padx=30)
btn_otkljucaj.grid(row=0, column=2, padx=30)

root.mainloop()
