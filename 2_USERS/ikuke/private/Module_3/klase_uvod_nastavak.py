#preporuka naziv klase velikim slovom bez odvajanja
# općenito


class NazivKlase:
    """docstring"""
    pass

objekt1= NazivKlase()
objekt2= NazivKlase()


class Ucenik():
    #konstruktor je metoda koja se zove __init__(initializacija)

    def __init__(self,ime1,prezime1,mbr1,adresa1,ocjena1):
        self.ime = ime1
        self.prezime=prezime1
        self.mbr=mbr1
        self.adresa=adresa1
        self.ocjena=ocjena1

    def ispis(self):
        print('proba')
        print(self.ime, self.prezime, self.adresa, self.mbr, ' ocjena:', self.ocjena)


   
def input_ucenika():
    ime=input('unesi ime ucenika:')
    prezime=input('unesi prezime ucenika:')
    mbr=input('unesi mbr ucenika:')
    adresa=input('unesi adresu ucenika:')
    ocjena=input('unesi ocjenu ucenika:')
    return Ucenik(ime,prezime,adresa,mbr,ocjena)



ucenik1=Ucenik('Marko', 'Marković', '1234567', 'Zagrebačka 12', '5')

ucenik2=input_ucenika()
ucenik3=input_ucenika()
print(ucenik1.ime, ucenik1.prezime, ucenik1.adresa, ucenik1.mbr, ' ocjena:', ucenik1.ocjena)
ucenik1.ispis()
ucenik2.ispis()
ucenik3.ispis()

lista_ocjena=[ucenik1.ocjena,ucenik2.ocjena,ucenik3.ocjena]
prosjek=0.0
for v in lista_ocjena:
    prosjek=prosjek+float(v)
prosjek=prosjek/len(lista_ocjena)
print('prosjek ocjena je ', prosjek)


