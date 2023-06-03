from tkinter import *

class RezultatiOtpornici (Frame):
    def __init__ (self, root, color):
        super().__init__()
        self.root = root
        self.colour = color
        #height=500, width=200, relief=RAISED, bd=5, bg='blue'
        self ['height'] = 500
        self ['width'] = 200
        self ['relief'] = RAISED
        self ['bd'] = 5
        self ['bg'] = color

    def izračunaj_seriju (self, R1, R2):
        Rserija = int(R1) + int (R2)

root = Tk()

uputa = Label (root, text = 'Unesite iznose otpornika', font = ('Segoe UI', 14), fg = 'blue')
uputa.grid (row=0, column=0, columnspan=2)

oznakaR1 = Label (root, text = 'R1').grid(row=1, column=0)
oznakaR2 = Label (root, text = 'R2').grid(row=2, column=0)

unosR1 = Entry (root)
unosR1.grid(row=1, column=1)


unosR2 = Entry (root)
unosR2.grid(row=2, column=1)

gumb_serija = Button (root, text = 'Serijski spoj', height = 2, width = 10,
                    font = ('Segoe UI', 14),
                    fg = 'white',
                    bg='blue')
gumb_serija.grid (row =3, column = 0)

gumb_paralela = Button (root, text = 'Serijski spoj', height = 2, width = 10,
                    font = ('Segoe UI', 14),
                    fg = 'white',
                    bg='green')
gumb_paralela.grid (row =3, column = 1)


#BEZ KORIŠTENJA KLASA
'''frame_serija = Frame (root, height=500, witdh=200, relief = RAISED, bd=2, bg='blue')
frame_serija.grid (row=4, column=0)

frame_paralela = Frame (root, height=500, relief = RAISED, witdh=200, bd=2, bg='blue')
frame_paralela.grid (row=4, column=1)'''

frame_serija = RezultatiOtpornici (root, 'blue')
frame_paralela = RezultatiOtpornici (root, 'green')
frame_serija.grid (row=4, column=0)
frame_paralela.grid (row=4, column=0)

root.mainloop()