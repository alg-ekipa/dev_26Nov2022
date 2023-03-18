# Izraditi klasu Proizvod te tri klase STOL, SVJETILJKA, TEPIH koje nasljeduju klasu Proizvod
# svojstva: sifra, cijena, raspolozivost, boja, dimenzije, materijal, oblik, zarulja...
# iskoristi pripremljeni rjecnik

# Od pripremljenih rjecnika s podacima izradite objekte za sve elemente

# napisi metodu za pronalazak i ispis:
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

class  Proizvodi:
    def __init__(self, sifra, naziv, cijena, raspolozivost, boja, materijal):
        self.sifra = sifra 
        self.naziv = naziv  
        self.cijena = cijena  
        self.raspolozivost = raspolozivost 
        self.boja = boja  
        self.materijal = materijal

    def ispis(self):
        print(self.sifra, self.naziv)

    # Proizvode sa cijenom ispod 1000kn 
    def ispis_cijena_1000(self):
        if self.cijena < 1000:
            self.ispis() 


class Stolovi(Proizvodi):
    def __init__ (self, sifra, naziv, cijena, raspolozivost, boja, materijal, broj_nogu):
        super().__init__(sifra, naziv, cijena, raspolozivost, boja, materijal)
        self.broj_nogu = broj_nogu

    # Ispisi Drvene stolove
    def ispis_drveni(self):
        if self.materijal == 'drvo':
            self.ispis() 


class Svijetiljke(Proizvodi):
    def __init__ (self, sifra, naziv, cijena, raspolozivost, boja, materijal, zarulja):
        super().__init__(sifra, naziv, cijena, raspolozivost, boja, materijal)
        self.zarulja = zarulja  

    # Ispisi svjetiljke sa zaruljom
    def ispis_sa_zaruljom(self):
        if self.zarulja == 'zarulja':
            self.ispis()

class Tepisi(Proizvodi):
    def __init__ (self, sifra, naziv, cijena, raspolozivost, boja, materijal, oblik):
        super().__init__(sifra, naziv, cijena, raspolozivost, boja, materijal)
        self.oblik = oblik 

    # Ispisi okrugle tepihe
    def ispis_okrugli(self):
        if self.oblik == 'okrugao':
            self.ispis()

#fukcija koja prebacuje rijecinik u listu objekata

def dodavanje(rijecnik, klasa):
    lista_objekata = []
    sifre = []
    sifre = list(rijecnik.keys())
    n= 0

    for vrijednost in rijecnik.values():
        a0 = sifre[n]
        a1 = vrijednost[0]
        a2 = vrijednost[1]
        a3 = vrijednost[2]
        a4 = vrijednost[3]
        a5 = vrijednost[4]
        a6 = vrijednost[5]
        n += 1

        objekt = klasa(a0, a1, a2, a3, a4, a5, a6)
        lista_objekata.append(objekt)

    return lista_objekata

lista_stolova = dodavanje(stolovi_rjecnik, Stolovi)
lista_svjetiljki = dodavanje(svjetiljka_rjecnik, Svijetiljke)
lista_tepisi = dodavanje(tepisi_rjecnik, Tepisi)

print('Svjetiljke sa žaruljom:')
for sv in lista_svjetiljki:
    sv.ispis_sa_zaruljom()

print('Ispisi Drvene stolove:')
for st in lista_stolova:
    st.ispis_drveni()

print('Ispisi okrugle tepihe:')
for te in lista_tepisi:
    te.ispis_okrugli()


print('ispis cijena ispod 1000:')
for a in lista_svjetiljki:
    a.ispis_cijena_1000()
for b in lista_stolova:
    b.ispis_cijena_1000()
for c in lista_tepisi:
    c.ispis_cijena_1000()

