from tkinter import *

class RezultatiOtpornici(Frame):
    def __init__(self, root, color):        # Samo će im se boja razlikovati, sva ostaloa svojstva su ista
        super().__init__()
        self.root = root
        self.color = color
        # height=500, width=200, relief=RAISED, bd=2, bg='blue'
        self['height'] = 500
        self['width'] = 200
        self['relief'] = RAISED
        self['bd'] = 3
        self['bg'] = color


    def izracunaj_seriju(self,R1,R2):
        Rserija = int(R1) + int(R2)

        rezultat_serija = Entry(self.root)
        rezultat_serija.grid(row=4, column=0, pady=10, sticky='n')
        rezultat_serija.insert(END,str(Rserija))

    def izracunaj_paralelu(self,R1,R2):
        Rparalela = (int(R1)*int(R2))/(int(R1)+int(R2))

        rezultat_paralela = Entry(self.root)
        rezultat_paralela.grid(row=4,column=1, pady=10, sticky='n')
        rezultat_paralela.insert(END,str(Rparalela))


class NatpisUnosR(Label):
    def __init__(self,root, text, color):
        super().__init__()
        self.root = root
        self.color = color
        self.text = text
        self['height'] = 1
        self['width'] = 12
        self['relief'] = RAISED
        self['bd'] = 3
        self['bg'] = color
        self['text'] = text

root = Tk()

uputa = Label(root, text='Unesite iznose otpornika', font=('Segore',14), fg='blue')
uputa.grid(row=0,column=0, columnspan=2)
'''
oznakaR1 = Label(root, text='R1').grid(row=1,column=0)
oznakaR2 = Label(root, text='R2').grid(row=2,column=0)
'''
oznakaR1 = NatpisUnosR(root, 'Otpornik R1', 'blue')
oznakaR1.grid(row=1,column=0)
oznakaR2 = NatpisUnosR(root, 'Otpornik R2', 'green')
oznakaR2.grid(row=2,column=0)

unosR1 = Entry(root)
unosR1.grid(row=1,column=1)

unosR2 = Entry(root)
unosR2.grid(row=2,column=1)

gumb_serija = Button(root, text='Serijski spoj', height=2, width=10,
                    font=('Segore',14), 
                    fg='white',
                    bg='blue',
                    command=lambda: frame_serija.izracunaj_seriju(unosR1.get(),unosR2.get()))
gumb_serija.grid(row=3,column=0)

gumb_paralela = Button(root, text='Serijski spoj', height=2, width=10,
                    font=('Segore',14), 
                    fg='white',
                    bg='green',
                    command=lambda: frame_paralela.izracunaj_paralelu(unosR1.get(),unosR2.get()))
gumb_paralela.grid(row=3,column=1)

frame_serija =RezultatiOtpornici(root, 'blue')
frame_paralela = RezultatiOtpornici(root, 'green')

frame_serija.grid(row=4,column=0)
frame_paralela.grid(row=4,column=1)

root.mainloop()