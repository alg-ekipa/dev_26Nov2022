from tkinter import *
import tkinter as tk



#VARIJABLE

global brojac_klika
brojac_klika=0

rootWindow = tk.Tk()
rootWindow.title("Algebra")


#FUNKCIJE

def klik_gumba():
    print ('Gumbek je kliknut')   
    global brojac_klika
    brojac_klika+=1
    tekst_za_ispis=f'Gumbek je kliknut {brojac_klika} puta' 
 
    ispis_label=Label(rootWindow, text=tekst_za_ispis) 
    ispis_label.grid(row=8,column=5)



def klik_gumba2():
    print ('Gumbek je kliknut')   
    global brojac_klika
    brojac_klika-=1
    tekst_za_ispis=f'Gumbek je kliknut {brojac_klika} puta' 
 
    ispis_label=Label(rootWindow, text=tekst_za_ispis) 
    ispis_label.grid(row=8,column=5)



def handle_keypress(event): #kad su u pitanju eventovi, funkcije u nazivu sadrži handle_....,  a argument joj je event


    #unosimo jedan po jedan znak, definiran kao event.char
    print(event.char)
    global unesena_slova
    unesena_slova+=event.char
    label_tekst_var.set(unesena_slova)





#SMJEŠTAJ ELEMENATA NA GUI

label_naslov = tk.Label(rootWindow, text='Key Event', font=('Segoe UI',18))
label_naslov.grid(row=0, column=0)

#label_ispis=tk.Label(rootWindow, textvariable=label_tekst_var, font=('Segoe UI', 18), fg='red') #kada nam je neki label ispisni, koristimo parametar textvariable i navodimo što se ispisuje
#label_ispis.grid(row=1, column=0)


myLabel1=tk.Label(rootWindow, text= "Bartol ekipa")
rootWindow.geometry('800x600')

myLabel1.grid(row =0, column= 1)

tk.Button(rootWindow, text = "Gumbek 1 ", command=klik_gumba).grid(row=1, column=3)
tk.Button(rootWindow, text = "Gumbek 2", bg="blue", command=klik_gumba).grid()
tk.Button(rootWindow, text = "Gumbek 3", bg="green",fg= "yellow", command=klik_gumba).grid()
tk.Button(rootWindow, text = "Gumbek 4", bg="red",fg= "white", command=klik_gumba2).grid(row=8, column=3)

tempertura_label= Label( rootWindow, text = 'Temperatura: ')
unos_temp_entry= Entry(rootWindow)

tempertura_label.grid(row=5, column= 1)

unos_temp_entry.grid(row=5, column= 2)
tempertura_label.grid(row=6, column= 1)



rootWindow.mainloop()


#povezivanje s funkcijom nad elementom root

#root.bind('<Key>', handle_keypress)

#root.mainloop()
