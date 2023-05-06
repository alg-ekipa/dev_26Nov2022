from tkinter import *

root = Tk()
root.title("Algebra by DEV - kalkulator")
root.geometry("600x400")

# Sve što povuće s get je string trebao staviti da je interger
def zbroji():
    entry_rezultat.delete(0, END)
    prvi_broj = int(entry_prvi_br.get())
    drugi_broj = int(entry_drugi_br.get())
    zbroj = prvi_broj + drugi_broj
    entry_rezultat.insert(END, str(zbroj))

def handle_oduzmi():
    entry_rezultat.delete(0, END)
    prvi_broj = int(entry_prvi_br.get())
    drugi_broj = int(entry_drugi_br.get())
    razlika = prvi_broj - drugi_broj
    entry_rezultat.insert(END, str(razlika))


#Smještanje elemenata na GUI

oznaka_prvi_br = Label(root, text="Prvi broj")
oznaka_prvi_br.grid(row = 0, column=0, padx=5, pady=5)

entry_prvi_br = Entry(root)
entry_prvi_br.grid(row=0, column=1)

oznaka_drugi_br = Label(root, text="Drugi broj: ")
oznaka_drugi_br.grid(row = 1, column=0, padx=5, pady=5)

entry_drugi_br = Entry(root)
entry_drugi_br.grid(row=1, column=1)

button_zbroji = Button(root, text="ZBROJI", command=zbroji)
button_zbroji.grid(row=3, column=0, padx=5, pady=5)

button_oduzmi = Button(root, text="ODUZMI")
button_oduzmi.grid(row=3, column=1, padx=5,pady=5)
button_oduzmi.bind("Button-1>", handle_oduzmi)  #povezivanje eventa(lijevi klik miša na gumb oduzmi)

oznaka_rezultat = Label(root, text="REZULTAT")
oznaka_rezultat.grid(row=4, column=0, padx=5, pady=5)

entry_rezultat = Entry()
entry_rezultat.grid(row=4, column=1)

root.mainloop()