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
    def __init__ (self, naziv, cijena, raspoloživost, boja, materijal):
        self.naziv = naziv
        self.cijena = cijena
        self.raspoloživost = raspoloživost
        self.boja = boja
        self.materijal = materijal
    
    def jeftini(self):
        if self.cijena <1000:
            print (f'\nCijena: {self.cijena}\nNaziv: {self.naziv}\nRaspoloživost: {self.raspoloživost}\nBoja: {self.boja}\nMaterijal: {self.materijal}')
    
    def raspoloživi (self): ############
        if self.raspoloživost == True:
            print (f'\nNaziv: {self.naziv}\nCijena: {self.cijena}\nRaspoloživost: {self.raspoloživost}\nBoja: {self.boja}\nMaterijal: {self.materijal}')

class Stol (Proizvod):
    def __init__(self, naziv, cijena, raspoloživost, boja, materijal, broj_nogu):
        super().__init__(naziv, cijena, raspoloživost, boja, materijal)
        self.broj_nogu = broj_nogu

    def drveni(self):
        if self.materijal == 'drvo':
            print (f'\nMaterijal: {self.materijal}\nNaziv: {self.naziv}\nCijena: {self.cijena}\nRaspoloživost: {self.raspoloživost}\nBoja: {self.boja}')


class Svjetiljka (Proizvod):
    def __init__ (self, naziv, cijena, raspoloživost, boja, materijal, svjetlo):
        super().__init__(naziv, cijena, raspoloživost, boja, materijal)
        self.svjetlo = svjetlo
    
    def svjetli(self):
        if self.svjetlo == 'zarulja':
            print (f'\n Žarulja: {self.svjetlo}\nNaziv: {self.naziv}\nCijena: {self.cijena}\nRaspoloživost: {self.raspoloživost}\nBoja: {self.boja}\nMaterijal: {self.materijal}')
    
    def ukupno (self):
        zbroj = sum (self.cijena) 
        return zbroj

class Tepih (Proizvod):
    def __init__ (self, naziv, cijena, raspoloživost, boja, materijal, oblik):
        super().__init__(naziv, cijena, raspoloživost, boja, materijal)
        self.oblik = oblik
        
    def okrugli(self):
        if self.oblik == 'okrugao':
            print (f'\nOblik: {self.oblik}\nNaziv: {self.naziv}\nCijena: {self.cijena}\nRaspoloživost: {self.raspoloživost}\nBoja: {self.boja}\nMaterijal: {self.materijal}')


lista_objekata_stolovi = []
for vrijednost in stolovi_rjecnik.values():
    i = vrijednost [0]
    ii = vrijednost [1]
    iii = vrijednost [2]
    iv = vrijednost [3]
    v = vrijednost [4]
    vi = vrijednost [5]

    stol_objekt = Stol (i, ii, iii, iv, v, vi)
    stol_objekt.drveni()
    lista_objekata_stolovi.append(stol_objekt)

lista_objekata_svjetiljke = []
for vrijednost in svjetiljka_rjecnik.values():
    i = vrijednost [0]
    ii = vrijednost [1]
    iii = vrijednost [2]
    iv = vrijednost [3]
    v = vrijednost [4]
    vi = vrijednost [5]

    svjetiljka_objekt = Svjetiljka (i, ii, iii, iv, v, vi)
    svjetiljka_objekt.svjetli()
    svjetiljka_objekt.ukupno
    #print('Svjetiljke ukupno iznose:',) #########
    lista_objekata_svjetiljke.append(svjetiljka_objekt)

lista_objekata_tepisi = []
for vrijednost in tepisi_rjecnik.values():
    i = vrijednost [0]
    ii = vrijednost [1]
    iii = vrijednost [2]
    iv = vrijednost [3]
    v = vrijednost [4]
    vi = vrijednost [5]

    tepisi_objekt = Tepih (i, ii, iii, iv, v, vi)
    tepisi_objekt.okrugli()
    lista_objekata_tepisi.append(tepisi_objekt)