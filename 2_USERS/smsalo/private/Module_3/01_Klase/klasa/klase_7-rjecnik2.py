stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
   }

class Stolovi:
    def __init__(self, ime, cijena, stanje, dimenzija, boja, materijal):
        self.ime = ime
        self.cijena = cijena
        self.stanje = stanje
        self.dimenzija = dimenzija
        self.boja = boja
        self.materijal = materijal
    
    def ispis(self):
        print(f'\t\t{self.ime}\ncijena: {self.cijena}\nna stanju: {self.stanje}\ndimanzija: {self.dimenzija}\nboja: {self.boja}\nmaterijal: {self.materijal}\n')

#ispis raspoloživih
    def na_stanju(self):
        if self.stanje == True:
            self.ispis()

#ispis stolova s cijenom iznad 1000kn
    def t_cijena(self):
        if self.cijena>1000:
            self.ispis()

lista_objekata_stolova=[]
for stol in stolovi_rjecnik.values():
    i = stol[0]
    c = stol[1]
    s = stol[2]
    d = stol[3]
    b = stol[4]
    m = stol[5]
    stol_objekt = Stolovi(i, c, s, d, b, m)
    lista_objekata_stolova.append(stol_objekt)

for stol in lista_objekata_stolova:
    stol.ispis()

for stol in lista_objekata_stolova:
    stol.na_stanju()

for stol in lista_objekata_stolova:
    stol.t_cijena()
