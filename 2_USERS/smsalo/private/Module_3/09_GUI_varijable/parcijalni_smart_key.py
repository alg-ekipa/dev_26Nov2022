from tkinter import * 
from tkinter import messagebox

root=Tk()
root.title('Zvono')


def pozvoni():
    messagebox.showinfo('Zvono', 'Pozvonili ste!')

def dod_broj(broj):
    br = tip_entry.get()
    tip_entry.delete(0, END)
    tip_entry.insert(0, br+broj)

def otkljucaj():
    frame_kljuc= LabelFrame(root, text='Tipkovnica', padx=50, pady=50)
    frame_kljuc.grid(row=1, column=0, padx=50, pady=50)

    tip_entry=Entry(frame_kljuc)
    tip_entry.grid(row=0, columnspan=3, column=0, padx=10, pady=10)

    button0=Button(frame_kljuc, text='0', padx=30, pady=30, command=lambda: dod_broj('0'))
    button0.grid(row=4, column=1)

    button1=Button(frame_kljuc, text='1', padx=30, pady=30, command=lambda: dod_broj('1'))
    button1.grid(row=1, column=0)

    button2=Button(frame_kljuc, text='2', padx=30, pady=30, command=lambda: dod_broj('2'))
    button2.grid(row=1, column=1)

    button3=Button(frame_kljuc, text='3', padx=30, pady=30, command=lambda: dod_broj('3'))
    button3.grid(row=1, column=2)

    button4=Button(frame_kljuc, text='4', padx=30, pady=30, command=lambda: dod_broj('4'))
    button4.grid(row=2, column=0)

    button5=Button(frame_kljuc, text='5', padx=30, pady=30, command=lambda: dod_broj('5'))
    button5.grid(row=2, column=1)

    button6=Button(frame_kljuc, text='6', padx=30, pady=30, command=lambda: dod_broj('6'))
    button6.grid(row=2, column=2)

    button7=Button(frame_kljuc, text='7', padx=30, pady=30, command=lambda: dod_broj('7'))
    button7.grid(row=3, column=0)

    button8=Button(frame_kljuc, text='8', padx=30, pady=30, command=lambda: dod_broj('8'))
    button8.grid(row=3, column=1)

    button9=Button(frame_kljuc, text='9', padx=30, pady=30, command=lambda: dod_broj('9'))
    button9.grid(row=3, column=2)

    buttonC=Button(frame_kljuc, text='C', padx=30, pady=30)
    buttonC.grid(row=4, column=0)

    buttonE=Button(frame_kljuc, text='E', padx=30, pady=30)
    buttonE.grid(row=4, column=2)


#GUI

frame_pocetni=Frame(root)
frame_pocetni.grid(row=0, column=0, padx=50, pady=50)

label_frame_pocetni=LabelFrame(frame_pocetni, text='Ulaz')
label_frame_pocetni.grid(row=0, column=0)

btn_zvono = Button(frame_pocetni, text='ZVONO', font=('Verdana',10, 'bold' ), bg='#EBDEF0', padx=30, command=pozvoni)         
btn_otkljucaj = Button(frame_pocetni, text='OTKLJUČAJ',font=('Verdana',10, 'bold' ), bg='#EBDEF0', padx=30, command=otkljucaj)

btn_zvono.grid(row=0, column=1, padx=30)
btn_otkljucaj.grid(row=0, column=2, padx=30)


root.mainloop()
