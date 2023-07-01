'''
TODO:
-promjena boje gumba kada se svjetlo upali (sivo-žuto)


Bojanje gumba kada je klinut:
activebackground='yellow'
Provjerava koja je vrijednost upisana na određeni gumb:
gumb_svijetlo_db['bg'] #ovdje pozadinsku boju

'''
velicina_prozora='400x400'
from tkinter import *

root = Tk()
root.title('Pametna kuca')
root.geometry(velicina_prozora)
root.eval('tk::PlaceWindow . center') #centriranje ekrana

#Otvaranje novoga prozora
def otvori_novi(naziv_prozora):
    root2 = Tk()
    window2 = (root2, "Drugi", "500x500", "Poruka 2")
    root2.title(naziv_prozora)
    root2.geometry(velicina_prozora)
    root2.eval(f'tk::PlaceWindow {str(root2)} center')

    back_gumb = Button(root2, text='Back', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='grey',
                     command=root2.destroy) # gašenje prozora
    back_gumb.grid(row=0, column=0)


    root2.mainloop()

# promjena boje gumba i slova pod uvjetom boje
def promjena_boje(naziv_gumba):
    if naziv_gumba['bg'] == 'grey':
        naziv_gumba.configure(fg='black',bg ="yellow") # promjena boje gumba i slova
    else:
        naziv_gumba.configure(fg='white',bg ="grey") 


#dodavanje labela ua polja za upise
oznakaR1 = Label(root, text='Dnevni boravak').grid(row=0, column=1)

#dodavanje gumbi     root pozicija                visina    dužina
gumb_svijetlo_db = Button(root, text='Svijetlo', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='grey',
                     command=lambda:promjena_boje(gumb_svijetlo_db)) # LAMBDA - da prenese u fukciju

gumb_svijetlo_db.grid(row=1, column=0)

gumb_TV_db = Button(root, text='TV', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='green',
                     command=lambda:otvori_novi(gumb_TV_db['text']))
gumb_TV_db.grid(row=2, column=0)
gumb_radio_db = Button(root, text='Radio', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='blue',
                     command=lambda:otvori_novi(gumb_radio_db['text']))
gumb_radio_db.grid(row=2, column=1)


#dodavanje labela ua polja za upise
oznakaR1 = Label(root, text='Hodnik').grid(row=3, column=1)

#dodavanje gumbi     root pozicija                visina    dužina
gumb_svijetlo_hod = Button(root, text='Svijetlo', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='grey',
                     command=lambda:promjena_boje(gumb_svijetlo_hod))
gumb_svijetlo_hod.grid(row=4, column=0)


root.mainloop()
