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
    def __init__(self, naziv, cijena, dostupnost, boja, materijal):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupnost = dostupnost
        self.boja = boja
        self.materijal = materijal

    def ispisi(self):
        print(f'\nNaziv proizvoda: {self.naziv} \nCijena proizvoda: {self.cijena}€ \nDostupnost proizvoda: {self.dostupnost} \nBoja proizvoda: {self.boja} \nMaterijal od kojeg je napravljen: {self.materijal}')

    def ispisi_jeftinije(self):
        if self.cijena < 1000:
            self.ispisi()

    def ispisi_raspoložive(self):
        if self.dostupnost == True:
            self.ispisi()

class Stol(Proizvod):
    def __init__(self, naziv, cijena, dostupnost, boja, materijal, broj_nogu):
        super().__init__(naziv, cijena, dostupnost, boja, materijal)
        self.broj_nogu = broj_nogu

    def ispisi_drvene(self):
        if self.materijal == 'drvo':
            print(f'Stol {self.naziv} izrađen je od {self.materijal}.')

class Svjetiljka(Proizvod):
    def __init__(self, naziv, cijena, dostupnost, boja, materijal, žarulja):
        super().__init__(naziv, cijena, dostupnost, boja, materijal)
        self.žarulja = žarulja

    def ispis_žarulje(self):
        if self.žarulja == 'zarulja':
            print(f'Svjetiljaka {self.naziv} se prodaje uključivo sa žaruljom.')

    
class Tepih(Proizvod):
    def __init__(self, naziv, cijena, dostupnost, boja, materijal, oblik):
        super().__init__(naziv, cijena, dostupnost, boja, materijal)
        self.oblik = oblik

    def ispisi_okrugle(self):
        if self.oblik == 'okrugao':
            print(f'Tepih {self.naziv} je {self.oblik}')

lista_objekata_stolovi = []

for vrijednost in stolovi_rjecnik.values():
    n = vrijednost[0]
    c = vrijednost[1]
    d = vrijednost[2]
    b = vrijednost[3]
    m = vrijednost[4]
    bn = vrijednost[5]

    stol_objekt = Stol(n,c,d,b,m,bn)
    #stol_objekt.ispisi()
    lista_objekata_stolovi.append(stol_objekt)

lista_objekata_svjetiljki = []

for vrijednost in svjetiljka_rjecnik.values():
    n = vrijednost[0]
    c = vrijednost[1]
    d = vrijednost[2]
    b = vrijednost[3]
    m = vrijednost[4]
    ž = vrijednost[5]

    svjetiljka_objekt = Svjetiljka(n,c,d,b,m,ž)
    #svjetiljka_objekt.ispisi()
    lista_objekata_svjetiljki.append(svjetiljka_objekt)

lista_objekata_tepisi = []

for vrijednost in tepisi_rjecnik.values():
    n = vrijednost[0]
    c = vrijednost[1]
    d = vrijednost[2]
    b = vrijednost[3]
    m = vrijednost[4]
    o = vrijednost[5]

    tepih_objekt = Tepih(n,c,d,b,m,o)
    #tepiha_objekt.ispisi()
    lista_objekata_tepisi.append(tepih_objekt)

print()
for stol in lista_objekata_stolovi:
    stol.ispisi_drvene()

print()
for svjetiljka in lista_objekata_svjetiljki:
    svjetiljka.ispis_žarulje()

print()
for tepih in lista_objekata_tepisi:
    tepih.ispisi_okrugle()


print('Proizvodi kojim je cijena manja od 1000€:')
for stol in lista_objekata_stolovi:
    stol.ispisi_jeftinije()
for svjetiljka in lista_objekata_svjetiljki:
    svjetiljka.ispisi_jeftinije()
for tepih in lista_objekata_tepisi:
    tepih.ispisi_jeftinije()

print()
print()
print('Proizvodi koji su raspoloživi')
for stol in lista_objekata_stolovi:
    stol.ispisi_raspoložive()
for svjetiljka in lista_objekata_svjetiljki:
    svjetiljka.ispisi_raspoložive()
for tepih in lista_objekata_tepisi:
    tepih.ispisi_raspoložive()


print()
zbroj = 0
for svjetiljka in lista_objekata_svjetiljki:
    zbroj = zbroj + svjetiljka.cijena

print(zbroj)


'''
ispisi_jeftinije(self):
  
ispisi_raspoložive(self):
'''