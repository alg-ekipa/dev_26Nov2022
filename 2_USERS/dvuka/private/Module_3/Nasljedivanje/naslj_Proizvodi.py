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

class Proizvod:
    def __init__(self,sifra, cijena, raspolozivost, boja, materijal):
        self.sifra=sifra
        self.cijena=cijena
        self.raspolozivost=raspolozivost
        self.boja=boja
        self.boja=boja
        self.materijal=materijal

    def ispisi(self):
        print(f'\n Šifra: {self.sifra}\n Cijena: {self.cijena}\n Raspolozivost: {self.raspolozivost}\n Dimenzije: {self.dimezije}\n Boja: {self.boja}\n Materijal: {self.materijal}')

    
class Stol(Proizvod):
    def __init__(self, sifra, cijena, raspolozivost, boja, materijal):
        super().__init__(sifra, cijena, raspolozivost, boja, materijal)

class Svjetiljka(Proizvod):
    def __init__(self, sifra, cijena, raspolozivost, boja, materijal):
        super().__init__(sifra, cijena, raspolozivost, boja, materijal)

class Tepih(Proizvod):
    def __init__(self, sifra, cijena, raspolozivost, boja, materijal):
        super().__init__(sifra, cijena, raspolozivost, boja, materijal)

lista_objekata_stolovi=[]
for vrijednost in stolovi_rjecnik.values():
    s = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    d = vrijednost[3]
    b = vrijednost[4]
    m = vrijednost[5]
    stolovi_objekt= Stol(s,c,r,d,b,m)
    stolovi_objekt.ispis()
    
    lista_objekata_stolovi.append(stolovi_objekt)

lista_objekata_svjetiljka=[]
for vrijednost in svjetiljka_rjecnik.values():
    s = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    d = vrijednost[3]
    b = vrijednost[4]
    m = vrijednost[5]
    svjetiljka_objekt= Svjetiljka(s,c,r,d,b,m)
    svjetiljka_objekt.ispis()
    
    lista_objekata_svjetiljka.append(svjetiljka_objekt)

lista_objekata_tepisi=[]
for vrijednost in tepisi_rjecnik.values():
    s = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    d = vrijednost[3]
    b = vrijednost[4]
    m = vrijednost[5]
    tepisi_objekt= Tepih(s,c,r,d,b,m)
    tepisi_objekt.ispis()
    
    lista_objekata_tepisi.append(tepisi_objekt)



