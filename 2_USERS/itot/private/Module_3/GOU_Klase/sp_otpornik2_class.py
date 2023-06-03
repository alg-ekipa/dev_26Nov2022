from tkinter import *

class RezultatiOtpornici(Frame):
    def __init__(self, root, color):
        super().__init__(), 
        self.root = root
        self.color = color
        # height=500, width = 200, relief=RAISED, bd=5, bg='blue'
        self['height']=500
        self['width']=200
        self['relief']= RAISED
        self['bd']= 5
        self['bg'] = color

    def izracunaj_seriju(self, R1, R2):
        Rserija = int(R1) + int(R2)

        rezultat_serija = Entry(self.root)
        rezultat_serija.grid(row=4, column=0, sticky='s') #sticky=s pomicanje entrya SOUTH, gore
        rezultat_serija.insert(END, str(Rserija))

    def izracunaj_paralelu(self, R1, R2):
        Rparalela = (int(R1)*int(R2))/(int(R1)+int(R2))

        rezultat_paralela = Entry(self.root)
        rezultat_paralela.grid(row=4, column=1,sticky='n') #sticky=s pomicanje entrya NORTH, dole
        rezultat_paralela.insert(END, str(Rparalela))

root = Tk()

#dodavanje plavog labla
            # nalazi se na rutu, text,                font i velicina slova, boja
uputa = Label(root, text='Unesite iznos otpornoika', font=('Segoe UI',14), fg='blue')
# pozicija u gridu
uputa.grid(row=0, column=0, columnspan=2)

#dodavanje labela ua polja za upise
oznakaR1 = Label(root, text='R1').grid(row=1, column=0)
oznakaR2 = Label(root, text='R2').grid(row=2, column=0)

unosR1 = Entry(root)
unosR1.grid(row=1, column=1)

unosR2 = Entry(root)
unosR2.grid(row=2, column=1)

#dodavanje gumbi     root pozicija                visina    dužina
gumb_serija = Button(root, text='Serijski spoj', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='yellow',
                     command=lambda: frame_serija.izracunaj_seriju(unosR1.get(),unosR2.get()))    
                    #dodavanje funkcije na gumb;  LAMBDA = jer naredba ima unos izvana
gumb_serija.grid(row=3, column=0)

gumb_paralela = Button(root, text='paralelni spoj', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='red',
                     command=lambda: frame_paralela.izracunaj_paralelu(unosR1.get(),unosR2.get()))
gumb_paralela.grid(row=3, column=1)

''' BEZ KORIŠTENJA KLASA
frame_serija = Frame(root, height=500, width=200, bg='blue')
frame_serija.grid(row=4, column=0)

frame_paralela = Frame(root, height=500, width=200, bg='red')
frame_paralela.grid(row=4, column=0)'''


#SA KLASAMA 
frame_serija = RezultatiOtpornici(root, 'blue')
frame_paralela = RezultatiOtpornici(root, 'green')

frame_serija.grid(row=4, column=0)
frame_paralela.grid(row=4, column=1)


root.mainloop()
