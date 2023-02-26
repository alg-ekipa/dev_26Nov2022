class Ucenik():
    # KONSTRUKTOR je metoda koja se zove __init__ (initialize), u nju se prenose parametri (PROPERTIES), odnosno karakteristike (svojstva) - ostavlja sve varijable prazne
    # prvi argument je uvijek SELF
    def __init__(self, ime, prezime, mbr, adresa, ocjena): #initialise, pokreni?
        # DEFINIRAMO da se pridruživanje vrijednosti uvijek odnosi na objekt koji inicijaliziramo
        self.ime = ime
        self.prezime = prezime
        self.mbr = mbr
        self.adresa = adresa
        self.ocjena = ocjena

       # metoda za ispis
    def ispisi(self): #MORA se napisati self
        print(self.ime, self.prezime, self.mbr, self. adresa, self. ocjena)



# kreiranje objekta sa direktnim unosom vrijednosti 
ucenik1 = Ucenik('Josip', 'Matić', '321654', 'Velika ul. 3', 5)    # kako unosimo properties tako nam pokazuje koji dolazi po redu
print(ucenik1.ime, ucenik1.prezime)  
lista_podataka_ucenik1 = [ucenik1.ime, ucenik1.prezime, ucenik1.mbr, ucenik1.adresa, ucenik1.ocjena]   
print(lista_podataka_ucenik1)

ucenik2 = Ucenik('Ivana', 'Ivić', '987564', 'Liva ulica 4', 4)
print(ucenik2.ime, ucenik2.prezime)  
lista_podataka_ucenik2 = [ucenik2.ime, ucenik2.prezime, ucenik2.mbr, ucenik2.adresa, ucenik2.ocjena]  
print(lista_podataka_ucenik2)

#kreiranje objekta s vrijednostima unesenim preko tipkovnice (varijablama)
'''ime_ucenik3 = input('Unesi ime učenika 3: ')
prezime_ucenik3 = input('Unesi prezime učenika 3: ')
mbr_ucenik3 = input('Unesi mbr učenika 3: ')
adresa_ucenik3 = input('Unesi adresu učenika 3: ')
ocjena_ucenik3 = int(input('Unesi ocjenu učenika 3: '))

ucenik3 = Ucenik(ime_ucenik3, prezime_ucenik3, mbr_ucenik3, adresa_ucenik3, ocjena_ucenik3)
print(ucenik3.ime, ucenik3.prezime)  
lista_podataka_ucenik3 = [ucenik3.ime, ucenik3.prezime, ucenik3.mbr, ucenik3.adresa, ucenik3.ocjena]  
print(lista_podataka_ucenik3)

lista_ocjena = [ucenik1.ocjena, ucenik2.ocjena, ucenik3.ocjena]
print(lista_ocjena)

def Average(lista_ocjena)
    return sum(lista_ocjena) / len(lista_ocjena)

prosjek = Average(lista_ocjena)
print(f'Prosjek ocjena  je: {prosjek}')'''

# ZADATAK - napraviti prosjek ocjena i ispisati



# ZADATAK za doma: napraviti kreiranje objekata kroz petlju: unesite 5 učenika, koje zatim kreirajte kao objekte klase učenik

print(ucenik1) # ispis nema smisla, prikazuje da je riječ o objektu na nekoj memorijskoj lokaciji

ucenik1.ispisi() # koristimo metodu za ispis koja se nalazi unutar klase Ucenik
ucenik2.ispisi()
