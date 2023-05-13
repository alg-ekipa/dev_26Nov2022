import tkinter as tk

root = tk.Tk()
root.title('Algebra - PyDev: Unos slova')
root.geometry('600x400')


#VARIJABLE
unesena_slova = ''
label_tekst_var = tk.StringVar()
label_tekst_var.set('Ovdje ide ono što unosimo')



#FUNKCIJE
def handle_keypress(event):         #kada su u pitanju eventovi funkcija u nazivu sadrži handle_....., a argument joj je event
    # unosimo jedan po jedan znak, definiran kao event.char
    print(event.char)
    global unesena_slova
    unesena_slova += event.char
    label_tekst_var.set(unesena_slova)



#smještanje elemenata na GUI (ovo ide na kraj koda, iako smo ga prvo napisali)

label_naslov = tk.Label(root, text=' Key event', font=('Segoe UI',18))
label_naslov.grid(row=0, column=0)

label_ispis = tk.Label(root,textvariable=label_tekst_var,  font=('Segoe UI',18), fg ='red')     # Kada nam je neki label ispisni. koristimo parametar textvariable i navodimo što se ispisuje
label_ispis.grid(row=1,column=0)

#POVEZIVANJE S FUNKCIJOM - nad elementom root
root.bind('<Key>', handle_keypress)

root.mainloop()