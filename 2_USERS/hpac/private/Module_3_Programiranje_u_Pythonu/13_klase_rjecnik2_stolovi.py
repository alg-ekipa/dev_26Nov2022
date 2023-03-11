stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
   }

class Stol:
    def __init__(self, naziv, cijena, raspoloživost, dimenzija, boja, materijal):
        self.naziv = naziv
        self.cijena = cijena
        self.raspoloživost = raspoloživost
        self.dimenzija = dimenzija
        self.boja = boja
        self.materijal = materijal

    def ispis(self):
        print(f'\nStol: {self.naziv}\nCijena: {self.cijena}€\nRaspoloživost: {self.raspoloživost}\nDimenzije stola: {self.dimenzija}cm\nBoja stola: {self.boja}\nMaterijal: {self.materijal}')

    # DODATI metode:
    # ispis raspoloživih artikala
    def ispis_raspoloživi(self):
        if self.raspoloživost == True:
            print(f'Trenutno je raspoloživ stol {self.naziv}, a cijena mu je {self.cijena}€')

    # ispis artikala sa cijenom većom od 1000
    def ispis_cijena(self):
        if self.cijena > 1000:
            print(f'Stol {self.naziv} ima cijenu {self.cijena}€')


lista_objekata_stolova = []

for vrijednost in stolovi_rjecnik.values():
    n = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    d = vrijednost[3]
    b = vrijednost[4]
    m = vrijednost[5]

    stol_objekt = Stol(n,c,r,d,b,m)
    #stol_objekt.ispis()
    lista_objekata_stolova.append(stol_objekt)


for stol in lista_objekata_stolova:
    stol.ispis_raspoloživi()

print()
for stol in lista_objekata_stolova:
    stol.ispis_cijena()


