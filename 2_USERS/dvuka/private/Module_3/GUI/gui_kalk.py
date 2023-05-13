from tkinter import *

root=Tk()

root.title('Algebra Py Dev - kalkulator')
root.geometry('600x400')

def zbroji():
    entry_rezultat.delete(0, END)
    prvi_broj=int(entry_prvi_br.get())
    drugi_broj=int(entry_drugi_br.get())
    zbroj=prvi_broj+drugi_broj
    #print(type(prvi_broj), type(drugi_broj))
    entry_rezultat.insert(END,str(zbroj))

def handle_oduzmi(event):
    entry_rezultat.delete(0, END)
    prvi_broj=int(entry_prvi_br.get())
    drugi_broj=int(entry_drugi_br.get())
    razlika=prvi_broj-drugi_broj
    #print(type(prvi_broj), type(drugi_broj))
    entry_rezultat.insert(END,str(razlika))

#smještaj elemenata na GUI

oznaka_prvi_br=Label(root,text='Prvi broj: ')
oznaka_prvi_br.grid(row=0, column=0, padx=5, pady=5)

entry_prvi_br=Entry()
entry_prvi_br.grid(row=0, column=1)

oznaka_drugi_br=Label(root,text='Drugi broj: ')
oznaka_drugi_br.grid(row=1, column=0, padx=5, pady=5)

entry_drugi_br=Entry()
entry_drugi_br.grid(row=1, column=1)

button_zbroji=Button(root, text='ZBROJI',command=zbroji)    #poziv funkcije zbroj ide kao argument command
button_zbroji.grid(row=2, column=0, padx=5, pady=5)

button_oduzmi=Button(root, text='ODUZMII')
button_oduzmi.grid(row=2, column=1, padx=5, pady=5)
button_oduzmi.bind("<Button-1>",handle_oduzmi)   #povezivanje eventa(lijevi klik miša na gumb ODUZMI) s funkcijom handle_oduzmi preko metode bind

oznaka_rezultat=Label(root, text='REZULTAT')
oznaka_rezultat.grid(row=3, column=0, padx=5 ,pady=5)

entry_rezultat=Entry()
entry_rezultat.grid(row=3, column=1)





root.mainloop()