from tkinter import *

class RezultatiOtpornici(Frame):                #definiramo što je jednako za sve, a prenosimo razlike (colour)
    def __init__(self, root, color):
        super().__init__()
        self.root=root
        self.colour=color
        self['height']=500
        self['width']=200
        self['relief'] =RAISED
        self['bd']=5
        self['bg']=color

    def izracunaj_seriju(self, R1, R2):
        Rserija=int(R1)+int(R2)

        rezltat_serija=Entry(self.root)
        rezltat_serija.grid(row=4, column=0, pady=10, sticky='n')       #STICKY definira položaj na "čeliji" n-north, s-south
        rezltat_serija.insert(END, str(Rserija))

    def izracunaj_paralelu(self, R1, R2):
        Rparalela=int(R1)*int(R2)/(int(R1)+int(R2))
        
        rezltat_paralela=Entry(self.root)
        rezltat_paralela.grid(row=4, column=1, pady=10, sticky='n')
        rezltat_paralela.insert(END, str(Rparalela))

class NatpisUnosR(Label):
    def __init__(self, root, text):
        super().__init__()
        self.root=root
        self.text=text
        self['font']=('Verdana bold', 8)
        self['bg']='gray'
        self['bd']=4
        self['text']=text
        

root=Tk()

uputa=Label(root, text='Unesite iznose otpornika', font=('Segoe UI',14), fg='blue')
uputa.grid(row=0,column=0, columnspan=2)

'''
#BEZ KLASE
oznakaR1=Label(root, text='R1').grid(row=1, column=0)
oznakaR2=Label(root, text='R2').grid(row=2, column=0)'''

#KLASA
oznakaR1=NatpisUnosR(root, 'R1')
oznakaR1.grid(row=1, column=0)
oznakaR2=NatpisUnosR(root, 'R2')
oznakaR2.grid(row=2, column=0)

unosR1=Entry(root)
unosR1.grid(row=1, column=1)

unosR2=Entry(root)
unosR2.grid(row=2, column=1)

gumb_serija=Button(root, text='Serijski spoj', height=2, width=10, 
                   font=('Segoe UI', 14), 
                   fg='white', 
                   bg='blue',
                   command=lambda:frame_serija.izracunaj_seriju(unosR1.get(), unosR2.get()))            #lambda jer koristimo argumente, ako nema dovoljno je ime funkcije
gumb_serija.grid(row=3, column=0)

gumb_paralela=Button(root, text='Paralelni spoj', height=2, width=10, 
                   font=('Segoe UI', 14), 
                   fg='white', 
                   bg='green',
                   command=lambda:frame_paralela.izracunaj_paralelu(unosR1.get(), unosR2.get()))
gumb_paralela.grid(row=3, column=1)

'''
#BEZ KLASA:
frame_serija=Frame(root, height=500, width=200, relief=RAISED, bd=5, bg='blue')
frame_serija.grid(row=4, column=0)

frame_paralela=Frame(root, height=500, width=200, relief=RAISED, bd=5, bg='green')
frame_paralela.grid(row=4, column=1)'''

#S KLASOM
frame_serija = RezultatiOtpornici(root, 'blue')
frame_serija.grid(row=4, column=0)

frame_paralela = RezultatiOtpornici(root, 'green')
frame_paralela.grid(row=4, column=1)

root.mainloop()