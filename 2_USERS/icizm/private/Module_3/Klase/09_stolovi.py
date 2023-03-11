class Stolovi: 
    def __init__(self, vrsta, cijena, raspolozivost, dimenzije, boja, materijal):
        self.vrsta = vrsta
        self.cijena = cijena
        self.raspolozivost = raspolozivost
        self.dimenzije = dimenzije
        self.boja = boja
        self.materijal = materijal

    def na_stanju(self): 
        if self.ispis == True: 
            self.ispis
    

    def ispis(self):
        print(f'\nVrsta: {self.vrsta}\nCijena: {self.cijena}\nRaspoloživost: {self.raspolozivost}\nDimenzije: {self.dimenzije}\nBoja: {self.boja}\nMaterijal: {self.materijal}')



stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
   }

lista_objekata_stolova = []

for vrijednost in stolovi_rjecnik.values():
    v = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    d = vrijednost[3]
    b = vrijednost[4]
    m = vrijednost[5]
    stol_objekt = Stolovi(v, c, r, d, b, m)
    lista_objekata_stolova.append(stol_objekt)

for stol in lista_objekata_stolova:
    stol.ispis()