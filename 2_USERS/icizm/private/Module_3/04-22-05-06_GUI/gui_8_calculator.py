from tkinter import *

root = Tk()

root.title('Algebra Py DEV - kalkulator')
root.geometry('600x400')

def zbroji(): 
    entry_rezultat.delete(0, END) # kako se pri promjeni vrijednosti brojeva rezultati nebi lijepili jedne za druge u nizu
    prvi_broj = int(entry_prvi_br.get()) # povlačenje iz unosa sa sučelja i unošenje u varijablu
    drugi_broj = int(entry_drugi_br.get())
    zbroj = prvi_broj + drugi_broj 
    #print(type(prvi_broj), type(drugi_broj))
    entry_rezultat.insert(END, str(zbroj)) # kod .insert potrebna DVA argumenta, prvi je END i onda broj koji stavljamo

'''def oduzmi(): 
    entry_rezultat.delete(0, END) # kako se pri promjeni vrijednosti brojeva rezultati nebi lijepili jedne za druge u nizu
    prvi_broj = int(entry_prvi_br.get()) # povlačenje iz unosa sa sučelja i unošenje u varijablu
    drugi_broj = int(entry_drugi_br.get())
    razlika = prvi_broj - drugi_broj 
    #print(type(prvi_broj), type(drugi_broj))
    entry_rezultat.insert(END, str(razlika))'''

def handle_oduzmi(event): #formula koja hendla neki event sa popisa u zagrade event
    entry_rezultat.delete(0, END)
    prvi_broj = int(entry_prvi_br.get()) # povlačenje iz unosa sa sučelja i unošenje u varijablu
    drugi_broj = int(entry_drugi_br.get())
    razlika = prvi_broj - drugi_broj 
    #print(type(prvi_broj), type(drugi_broj))
    entry_rezultat.insert(END, str(razlika))

# Smještaj elemenata na GUI kroz grid

oznaka_prvi_br = Label(root, text='Prvi broj: ')
oznaka_prvi_br.grid(row=0, column=0, padx=5, pady=5)

entry_prvi_br = Entry(root)
entry_prvi_br.grid(row=0, column=1)

oznaka_drugi_br = Label(root, text='Drugi broj: ')
oznaka_drugi_br.grid(row=1, column=0, padx=5, pady=5)

entry_drugi_br = Entry(root)
entry_drugi_br.grid(row=1, column=1)

button_zbroj = Button(root, text='ZBROJI', command= zbroji) #na kraju dodan argument command da se poveže gumb sa funkcijom
button_zbroj.grid(row=2, column=0, padx=5, pady=5)

button_oduzmi = Button(root, text='ODUZMI')
button_oduzmi.grid(row=2, column=1, padx=5, pady=5)
button_oduzmi.bind("<Button-1>", handle_oduzmi) # povezujemo sa eventom sa popisa i upisujemo ga pod navodnicima (lijevi klik miša na gumb oduzmi) sa funkcijom handle_oduzmi

#znači oba gumba rade na klik ali smo ih povezali sa funkcijama na drugačiji način, ova druga je kao preciznija 

oznaka_rezultat = Label(root, text='REZULTAT: ')
oznaka_rezultat.grid(row=3, column=0, padx=5, pady=5)

entry_rezultat = Entry()
entry_rezultat.grid(row=3, column=1)

root.mainloop()