import tkinter as tk

root = tk.Tk()
root.title("Algebra - PyDev: Unos slova")
root.geometry("600x400")

#Varijabe
unesena_slova = ""
label_tekst_var = tk.StringVar()
label_tekst_var.set("Ovdje ide što unosimo")


#Funkcije
def handle_keypress(event):  #kada su u pitanju eventovi, funkcja u nazivu sadrži handle... a argument joj je event
    #unosimo jedan po jedan znak, definiran kao event.char
    print(event.char)
    global unesena_slova
    unesena_slova += event.char
    label_tekst_var.set(unesena_slova)

#Smještanje elemenata na GUI
label_naslov = tk.Label(root, text = "Key Event", font = ("Segoe UI", 18))
label_naslov.grid(row=0, column=0)

label_ispis = tk.Label(root, textvariable=label_tekst_var, font = ("Segoe UI", 18), fg = "red" ) 
label_ispis.grid(row=1, column=0)

#Povezivanje s funkcijom nad elementom root
root.bind("<Key>", handle_keypress)

root.mainloop()