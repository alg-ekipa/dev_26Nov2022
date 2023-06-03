class Ucenik():
    #KONSTRUKTOR je metoda koja se zove __init__ (initialize) u koju se prenose parametri odnosno karakteristike (svojstva)
    #*prvi argument je uvijek SELF

    def __init__(self, ime, prezime, mbr, adresa, ocjena):
        #definiramo da se pridruživanje vrijednosti uvijek odnosi na objekt koji inicijaliziramo
        self.ime = ime
        self.prezime = prezime
        self.mbr = mbr
        self.adresa = adresa
        self.ocjena = ocjena

    #metoda za ispis
    def ispisi(self):
        print (self.ime, self.prezime, self.mbr, self.adresa, self.ocjena)

#kreiranje objekta s direktnim unosom vrijednosti
ucenik1 = Ucenik('Josip', 'Matić', '345678', 'Velika ul. 3', 5)
print (ucenik1.ime, ucenik1.prezime)

lista_podataka_ucenik1 = [ucenik1.ime, ucenik1.prezime, ucenik1.mbr, ucenik1.adresa, ucenik1.ocjena]
print (lista_podataka_ucenik1)

ucenik2 = Ucenik('Ivana', 'Ivić','987654','Uska ul. 2','4')
print (ucenik2.ime, ucenik2.prezime)

lista_podataka_ucenik2 = [ucenik2.ime, ucenik2.prezime, ucenik2.mbr, ucenik2.adresa, ucenik2.ocjena]
print (lista_podataka_ucenik2)

'''ime_ucenik3 = input ('Unesi ime učenika 3: ')
prezime_ucenik3 = input ('Unesi prezime učenika 3: ')
mbr_ucenik3 = input ('Unesi mbr učenika 3: ')
adresa_ucenik3 = input ('Unesi adresu učenika 3: ')
ucenik3_ocjena = int(input ('Unesi ocjenu učenika 3: '))'''

#kreiranje objekta s vrijednostima unesenim preko tipkovnice (varijablama)
'''ucenik3 = Ucenik(ime_ucenik3,prezime_ucenik3,mbr_ucenik3,adresa_ucenik3,ucenik3.ocjena)
print (ucenik3.ime, ucenik3.prezime)

lista_ocjena = [ucenik1.ocjena, ucenik2.ocjena, ucenik3_ocjena]
print (lista_ocjena)

zbroj = ucenik1.ocjena + ucenik2.ocjena + ucenik3_ocjena
avg = zbroj // len(lista_ocjena)
print (avg)'''

#TO DO napraviti kreiranje objekta kroz petlju: unesite 5 učenika, koje zatim kreirajte kao objekte klase učenik


print(ucenik1) #ispis nema smisla, prikazuje samo da je riječ o objektu na nekoj memorijskoj lokaciji

ucenik1.ispisi()        #koristimo metodu za ispis koja se nalazi unutar klase Ucenik
ucenik2.ispisi()