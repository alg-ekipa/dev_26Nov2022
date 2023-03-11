# Izraditi klasu Proizvod te tri klase STOL, SVJETILJKA, TEPIH koje nasljeduju klasu Proizvod
# svojstva: sifra, cijena, raspolozivost, boja, dimenzije, materijal, oblik, zarulja...
# iskoristi pripremljeni rjecnik

# Od pripremljenih rjecnika s podacima izradite objekte za sve elemente

# napisi metodu za pronalazak i ispis
# Ispisi svjetiljke sa zaruljom
# Ispisi Drvene stolove
# Ispisi okrugle tepihe
# Proizvode sa cijenom ispod 1000kn     
# Raspolozive proizvode    
# Ukupnu cijenu svih svjetiljki   

class Proizvod:
    def __init__(self, ime, cijena, stanje, boja, materijal):
        self.ime=ime
        self.cijena=cijena
        self.stanje=stanje
        self.boja=boja
        self.materijal=materijal
    
    def na_stanju(self):
        if self.stanje==True:
            self.ispis()
    
    def ispis(self):
        print(f'Ime: {self.ime}\nCijena: {self.cijena}\nIma: {self.stanje}\nBoja: {self.boja}\nMaterijal: {self.materijal}')

    def t_cijena(self):
        if self.cijena>1000:
            self.ispis()

class Stol(Proizvod):
    def __init__(self, ime, cijena, stanje, boja, materijal, br_nogu):
        super().__init__(ime, cijena, stanje, boja, materijal)
        self.br_nogu=br_nogu
    
    def ispis_stol(self):
        print(f'Ime: {self.ime}\nCijena: {self.cijena}\nIma: {self.stanje}\nBoja: {self.boja}\nMaterijal: {self.materijal}\nBroj nogu :{self.br_nogu}\n')
    
    def drveni(self):
        if self.materijal == 'drvo':
            self.ispis_stol()

class Svjetiljka(Proizvod):
    def __init__(self, ime, cijena, stanje, boja, materijal, zarulja):
        super().__init__(ime, cijena, stanje, boja, materijal)
        self.zarulja=zarulja

    def ispis_svjetiljka(self):
        print(f'Ime: {self.ime}\nCijena: {self.cijena}\nIma: {self.stanje}\nBoja: {self.boja}\nMaterijal: {self.materijal}\nŽarulja: {self.zarulja}\n')

    def ima_zarulju(self):
        if self.zarulja == 'zarulja':
            self.ispis_svjetiljka()

    
class Tepih(Proizvod):
    def __init__(self, ime, cijena, stanje, boja, materijal, tip):
        super().__init__(ime, cijena, stanje, boja, materijal)
        self.tip=tip

    def ispis_tepih(self):
        print(f'Ime: {self.ime}\nCijena: {self.cijena}\nIma: {self.stanje}\nBoja: {self.boja}\nMaterijal: {self.materijal}\nTip: {self.tip}\n') 

    def okrugli(self):
        if self.tip == 'okrugao':
            self.ispis_tepih()

stolovi_rjecnik = {
    '0186': ['stol Jack', 700.00, True, 'smeđa', 'drvo', 4],
    '0203': ['stol Kathy', 880.00, True, 'smeđa', 'staklo', 3],
    '1234': ['stol Tomy', 1250.00, True, 'bijela', 'staklo', 4],
    '4002': ['stol Ohm', 940.00, True, 'crna', 'metal', 1],
    '0923': ['stol Heda', 940.00, False, 'crna', 'drvo', 1],
    '1773': ['stol Lucas', 940.00, True, 'crna', 'drvo', 4]
}

svjetiljka_rjecnik = {
    '0001': ['svjetiljka Zadar', 1200.00, True, 'zlatna', 'zlato', 'zarulja'],
    '0002': ['svjetiljka Zagreb', 2800.00, True, 'plava', 'staklo', 'zarulja'],
    '0003': ['svjetiljka Dubrava', 800.00, False, 'zelena', 'srebro', 'bez'],
    '0004': ['svjetiljka Rijeka', 400.00, False, 'roza', 'zlato', 'bez'],
    '0005': ['svjetiljka Dubrovnik', 5400.00, True, 'magenta', 'platina', 'zarulja'],
    '0006': ['svjetiljka Madrid', 55950.00, True, 'crvena', 'platina', 'bez']
}

tepisi_rjecnik = {
    '0007': ['tepih Melita', 8000.00, True, 'zlatna', 'pamuk', 'okrugao'],
    '0008': ['tepih Lana', 7200.00, True, 'plava', 'svila', 'pravokutni'],
    '0009': ['tepih Sanja', 480.00, False, 'zelena', 'pamuk', 'okrugao'],
    '0010': ['tepih Emina', 525.00, False, 'roza', 'plastika', 'pravokutni'],
    '0011': ['tepih Laura', 320.00, True, 'magenta', 'plastika', 'okrugao'],
    '0012': ['tepih Tea', 12524.00, True, 'crvena', 'svila', 'pravokutni']
}

lista_stol_objekti=[]
lista_svjetiljka_objekti=[]
lista_tepih_objekti=[]
lista_svi=[]

for stol in stolovi_rjecnik.values():
    i = stol[0]
    c = stol[1]
    s = stol[2]
    b = stol[3]
    m = stol[4]
    n = stol[5]
    stol_objekt = Stol(i, c, s, b, m, n)
    lista_stol_objekti.append(stol_objekt)

for stol in lista_stol_objekti:
    stol.ispis_stol()

for svjetiljka in svjetiljka_rjecnik.values():
    i = svjetiljka[0]
    c = svjetiljka[1]
    s = svjetiljka[2]
    b = svjetiljka[3]
    m = svjetiljka[4]
    n = svjetiljka[5]
    svjetiljka_objekt = Svjetiljka(i, c, s, b, m, n)
    lista_svjetiljka_objekti.append(svjetiljka_objekt)

for svjetiljka in lista_svjetiljka_objekti:
    svjetiljka.ispis_svjetiljka()

for tepih in tepisi_rjecnik.values():
    i = tepih[0]
    c = tepih[1]
    s = tepih[2]
    b = tepih[3]
    m = tepih[4]
    n = tepih[5]
    tepih_objekt = Tepih(i, c, s, b, m, n)
    lista_tepih_objekti.append(tepih_objekt)

lista_svi=lista_stol_objekti+lista_svjetiljka_objekti+lista_tepih_objekti

for tepih in lista_tepih_objekti:
    tepih.ispis_tepih()

for svjetiljka in lista_svjetiljka_objekti:
    svjetiljka.ima_zarulju()

for stol in lista_stol_objekti:
    stol.drveni()

for tepih in lista_tepih_objekti:
    tepih.okrugli()

for proizvod in lista_svi:
    proizvod.t_cijena()

for proizvod in lista_svi:
    proizvod.na_stanju()

ukupna_cijena=0
for svjetiljka in lista_svjetiljka_objekti:
    ukupna_cijena=ukupna_cijena + svjetiljka.cijena
print(f'Ukupna cijena svih svjetiljki je: {ukupna_cijena}')
    
