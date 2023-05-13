from tkinter import * 
from tkinter import messagebox

root = Tk()

root.title('SmartKey Vrata')


def pozvoni():
    messagebox.showinfo(title='DIN-DON!', message='Zvono je aktivirano! Uskoro će netko doći otvoriti vrata!')

    
def otkljucaj():

    frameTIP = LabelFrame(root, text='Unesite PIN', padx=30, pady=30, bd=2)
    frameTIP.grid(row=1, column=0, padx=10, pady=10)

    tip_entry = Entry(frameTIP)
    tip_entry.grid(row=0, column=0, columnspan=3, padx=30, pady=30)

    def add_number(number): 
        num = tip_entry.get() # getamo što tipnemo i stavljamo u varijablu num
        tip_entry.delete(0, END)
        tip_entry.insert(0, num+number)

    button0 = Button(frameTIP, text='1', padx=40, pady=20, command=lambda: add_number('1'))
    button0.grid(row=1, column=0)

    button1 = Button(frameTIP, text='2', padx=40, pady=20, command=lambda: add_number('2'))
    button1.grid(row=1, column=1)

    button2 = Button(frameTIP, text='3', padx=40, pady=20, command=lambda: add_number('3'))
    button2.grid(row=1, column=2)

    button3 = Button(frameTIP, text='4', padx=40, pady=20, command=lambda: add_number('4'))
    button3.grid(row=2, column=0)

    button4 = Button(frameTIP, text='5', padx=40, pady=20, command=lambda: add_number('5'))
    button4.grid(row=2, column=1)

    button5 = Button(frameTIP, text='6', padx=40, pady=20, command=lambda: add_number('6'))
    button5.grid(row=2, column=2)

    button6 = Button(frameTIP, text='7', padx=40, pady=20, command=lambda: add_number('7'))
    button6.grid(row=3, column=0)

    button7 = Button(frameTIP, text='8', padx=40, pady=20, command=lambda: add_number('8'))
    button7.grid(row=3, column=1)

    button8 = Button(frameTIP, text='9', padx=40, pady=20, command=lambda: add_number('9'))
    button8.grid(row=3, column=2)

    button9 = Button(frameTIP, text='0', padx=40, pady=20, command=lambda: add_number('0'))
    button9.grid(row=4, column=1)

    frame_poruka = LabelFrame(frameTIP, text='Kako ide?', bd=2, padx=30)
    frame_poruka.grid(row=0, column=6, rowspan= 5, padx=30, pady=10)
    poruka_label = Label(frame_poruka, text='Pokušajte otključati', padx=30, pady=30)
    poruka_label.grid(row=0, column=0)



frame_pocetni=Frame(root)
frame_pocetni.grid(row=0, column=0, padx=50, pady=10)

label_frame_pocetni=LabelFrame(frame_pocetni, text='Ulaz', bd=1 )
label_frame_pocetni.grid(row=0, column=0)

btn_zvono = Button(frame_pocetni, text='ZVONO', padx=30, pady=20, justify='left', command=pozvoni)  
btn_zvono.grid(row=0, column=0, padx=30, pady=20)

btn_otkljucaj = Button(frame_pocetni, text='OTKLJUČAJ', padx=30, pady=20, justify='right', command=otkljucaj)
btn_otkljucaj.grid(row=0, column=2, padx=30, pady=20)






root.mainloop()