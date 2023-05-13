import tkinter as tk

root=tk.Tk()
root.title('Algebra-Unos slova')
root.geometry('600x400')

#varijable
unesena_slova=''
label_tekst_var=tk.StringVar()
label_tekst_var.set('Ovdje ide unos')

#funkcije
def handle_keypress(event):     #kada su u pitanju eventovi, finkcija u nazivu sadrži handle_nešto, a argument je event
    #unosimo jedna po jedan znak definiran kao event.char
    #print(event.char)  # na terminalu
    global unesena_slova
    unesena_slova+=event.char
    label_tekst_var.set(unesena_slova)

# smještanje elemenata na GUI
label_naslov = tk.Label(root, text='Key event', font=('Segoe UI', 18))
label_naslov.grid(row=0, column=0)

label_ispis = tk.Label(root, textvariable=label_tekst_var, font=('Segoe UI', 18), fg='red')             #kada nam je neki label ispisni koristimo textvariable i navodimo što se ispisuje
label_ispis.grid(row=1, column=0)

#povezivanje s funkciom na elementu root
root.bind('<Key>', handle_keypress)


root.mainloop()