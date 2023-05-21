from tkinter import *

def otkljucaj():
    print("Otključano!")

def pozvoni():
    print("Pozvono!")

# Stvaranje Tkinter prozora
window = Tk()

# Stvaranje gumba "Otključaj"
otkljucaj_gumb = Button(window, text="Otključaj", command=otkljucaj)
otkljucaj_gumb.pack()

# Stvaranje gumba "Pozvoni"
pozvoni_gumb = Button(window, text="Pozvoni", command=pozvoni)
pozvoni_gumb.pack()

# Pokretanje Tkinter petlje događaja
window.mainloop()