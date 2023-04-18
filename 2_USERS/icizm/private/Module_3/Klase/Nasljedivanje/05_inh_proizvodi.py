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

# Riješila Sandra i Irinej ima dobro riješene liste pa pogledaj i riješi za DZ


class Proizvodi: 
    def __init__(self, vrsta, cijena, raspolozivost, boja, materijal):
        self.vrsta = vrsta
        self.cijena = cijena
        self.raspolozivost = raspolozivost
        self.boja = boja
        self.materijal = materijal 

    def na_stanju(self): 
        if self.raspolozivost == True: 
            self.ispis()
       
    
    def ispis(self):
        print(f'Raspoloživi artikl je: \nVrsta: {self.vrsta}\nCijena: {self.cijena}\nRaspoloživost: {self.raspolozivost}\nBoja: {self.boja}\nMaterijal: {self.materijal}')
        print()

class Stolovi(Proizvodi): 
    def __init__(self, vrsta, cijena, raspolozivost, boja, materijal, br_nogu):
        super().__init__(vrsta, cijena, raspolozivost, boja, materijal)
        self.br_nogu = br_nogu
           

class Svjetiljke(Proizvodi): 
     def __init__(self, vrsta, cijena, raspolozivost, boja, materijal, zarulja):
        super().__init__(vrsta, cijena, raspolozivost, boja, materijal)
        self.zarulja = zarulja

class Tepisi(Proizvodi): 
    def __init__(self, vrsta, cijena, raspolozivost, boja, materijal, oblik):
        super().__init__(vrsta, cijena, raspolozivost, boja, materijal)
        self.oblik = oblik

stolovi_rjecnik = {
    '0186': ['stol Jack', 700.00, True, 'smeđa', 'drvo', 4],
    '0203': ['stol Kathy', 880.00, True, 'smeđa', 'staklo', 3],
    '1234': ['stol Tomy', 1250.00, True, 'bijela', 'staklo', 4],
    '4002': ['stol Ohm', 940.00, True, 'crna', 'metal', 1],
    '0923': ['stol Heda', 940.00, False, 'crna', 'drvo', 1],
    '1773': ['stol Lucas', 940.00, True, 'crna', 'drvo', 4]
}

lista_objekata_stolova = []

for vrijednost in stolovi_rjecnik.values():
    v = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    b = vrijednost[3]
    m = vrijednost[4]
    n = vrijednost[5]
    stol_objekt = Stolovi(v, c, r, b, m, n)
    lista_objekata_stolova.append(stol_objekt)

for stol in lista_objekata_stolova:
    stol.ispis()

svjetiljka_rjecnik = {
    '0001': ['svjetiljka Zadar', 1200.00, True, 'zlatna', 'zlato', 'zarulja'],
    '0002': ['svjetiljka Zagreb', 2800.00, True, 'plava', 'staklo', 'zarulja'],
    '0003': ['svjetiljka Dubrava', 800.00, False, 'zelena', 'srebro', 'bez'],
    '0004': ['svjetiljka Rijeka', 400.00, False, 'roza', 'zlato', 'bez'],
    '0005': ['svjetiljka Dubrovnik', 5400.00, True, 'magenta', 'platina', 'zarulja'],
    '0006': ['svjetiljka Madrid', 55950.00, True, 'crvena', 'platina', 'bez']
}

lista_objekata_svjetiljka = []

for vrijednost in svjetiljka_rjecnik.values():
    v = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    b = vrijednost[3]
    m = vrijednost[4]
    n = vrijednost[5]
    svjetiljka_objekt = Svjetiljke(v, c, r, b, m, n)
    lista_objekata_svjetiljka.append(svjetiljka_objekt)

for svjetiljka in lista_objekata_svjetiljka:
    svjetiljka.ispis()

tepisi_rjecnik = {
    '0007': ['tepih Melita', 8000.00, True, 'zlatna', 'pamuk', 'okrugao'],
    '0008': ['tepih Lana', 7200.00, True, 'plava', 'svila', 'pravokutni'],
    '0009': ['tepih Sanja', 480.00, False, 'zelena', 'pamuk', 'okrugao'],
    '0010': ['tepih Emina', 525.00, False, 'roza', 'plastika', 'pravokutni'],
    '0011': ['tepih Laura', 320.00, True, 'magenta', 'plastika', 'okrugao'],
    '0012': ['tepih Tea', 12524.00, True, 'crvena', 'svila', 'pravokutni']
}

lista_objekata_tepisi = []

for vrijednost in tepisi_rjecnik.values():
    v = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    b = vrijednost[3]
    m = vrijednost[4]
    n = vrijednost[5]
    tepisi_objekt = Tepisi(v, c, r, b, m, n)
    lista_objekata_tepisi.append(tepisi_objekt)

for tepisi in lista_objekata_tepisi:
    tepisi.ispis()