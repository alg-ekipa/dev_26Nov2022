stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
}

class Stolovi:
    def __init__ (self, naziv, cijena, raspoloživost, dimenzije, boja, materijal):
        self.naziv = naziv
        self.cijena = cijena
        self.raspoloživost = raspoloživost
        self.dimenzije = dimenzije
        self.boja = boja
        self.materijal = materijal

    def ispis (self):
        print (f'\nNaziv: {self.naziv}\nCijena: {self.cijena}\nRaspoloživost: {self.raspoloživost}\nDimenzije: {self.dimenzije}\nBoja: {self.boja}\nMaterijal: {self.materijal}')

#ddodati metode:
#za ispis raspoloživih stolova
    def dostupni (self):
        if self.raspoloživost == True:
            print (f'\nRaspoloživ: {self.raspoloživost}\nNaziv: {self.naziv}\nCijena: {self.cijena}')

#za ispis stolova iznad 1000kn
    def iznad_soma(self):
        if self.cijena > 1000:
            print (f'\nCijena: {self.cijena}\nNaziv: {self.naziv}')

lista_objekata_stolova = []

for vrijednost in stolovi_rjecnik.values():
    v = vrijednost [0]
    p = vrijednost [1]
    r = vrijednost [2]
    g = vrijednost [3]
    c = vrijednost [4]
    m = vrijednost [5]
        
    stol_objekt = Stolovi (v,p,r,g,c,m)
    stol_objekt.ispis()
    lista_objekata_stolova.append(stol_objekt)

for stol in lista_objekata_stolova:
    stol.dostupni()

for stol in lista_objekata_stolova:
    stol.iznad_soma()