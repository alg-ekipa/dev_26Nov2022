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
    def __init__(self, naziv, cijena, raspolozivost, boja, materijal, oblik):
        self.naziv = naziv
        self.cijena = cijena
        self.raspolozivost = raspolozivost
        self.boja = boja
        self.materijal = materijal
        self.oblik = oblik
    
    def ispis(self):
        print(f"{self.naziv} {self.cijena} {self.raspolozivost}")
    

    def trazi(self, naziv_trazenje):
        if naziv_trazenje == self.naziv:
            self.ispis()       

    def zarulja(self):
        if self.oblik == "zarulja":
            print(f"Proizvod {self.naziv} dolazi s zaruljom.")

    def izrada(self):
        if self.materijal == "drvo":
            print(f"Proizvod {self.naziv} izrađen je od drva.")

    def shape(self):
        if self.oblik == "okrugao":
            print(f"Proizvod {self.naziv} okruglog je oblika.")

    def cjenovni_rang(self):
        if self.cijena < 1000.00:
            print(f"Proizvod {self.naziv} kosta manje od 1000,00 Eur, cijena je {self.cijena}.")

    def dostupnost(self):
        if self.raspolozivost == True:
            print(f"Proizvod {self.naziv} nalazi se na stanju.")

        

class Stol(Proizvod):
    def __init__(self, naziv, cijena, raspolozivost, boja, materijal, oblik):
        super().__init__(naziv, cijena, raspolozivost, boja, materijal, oblik)

   
class Svjetiljka(Proizvod):
    def __init__(self, naziv, cijena, raspolozivost, boja, materijal, oblik):
        super().__init__(naziv, cijena, raspolozivost, boja, materijal, oblik)


class Tepih(Proizvod):
    def __init__(self, naziv, cijena, raspolozivost, boja, materijal, oblik):
        super().__init__(naziv, cijena, raspolozivost, boja, materijal, oblik)



lista_stolova = []

for vrijednost in stolovi_rjecnik.values():
    n = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    b = vrijednost[3]
    m = vrijednost[4]
    o = vrijednost[5]
    stol_objekt = Stol(n,c,r,b,m,o)
    stol_objekt.ispis()
    lista_stolova.append(stol_objekt)   
print() 

lista_svjetiljka = []
lista_cijena_svjetiljka = []

for vrijednost in svjetiljka_rjecnik.values():
    n = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    b = vrijednost[3]
    m = vrijednost[4]
    o = vrijednost[5]
    svjetiljka_objekt = Stol(n,c,r,b,m,o)
    svjetiljka_objekt.ispis()
    lista_svjetiljka.append(svjetiljka_objekt) 
print()

lista_tepiha = []

for vrijednost in tepisi_rjecnik.values():
    n = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    b = vrijednost[3]
    m = vrijednost[4]
    o = vrijednost[5]
    tepih_objekt = Stol(n,c,r,b,m,o)
    tepih_objekt.ispis()
    lista_tepiha.append(tepih_objekt) 
print()


trazenje = input("Unesi naziv proizvoda: ")
for vrijednost in lista_stolova:
    vrijednost.trazi(trazenje)
for vrijenost in lista_svjetiljka:
    vrijednost.trazi(trazenje)
for vrijednost in lista_tepiha:
    vrijednost.trazi(trazenje)
print()

for vrijednost in lista_svjetiljka:
    vrijednost.zarulja()
print()

for vrijednost in lista_stolova:
    vrijednost.izrada()
print()

for vrijednost in lista_tepiha:
    vrijednost.shape()
print()

for vrijednost in lista_tepiha:
    vrijednost.cjenovni_rang()
for vrijednost in lista_svjetiljka:
    vrijednost.cjenovni_rang()
for vrijednost in lista_stolova:
    vrijednost.cjenovni_rang()
print()

for vrijednost in lista_tepiha:
    vrijednost.dostupnost()
for vrijednost in lista_svjetiljka:
    vrijednost.dostupnost()
for vrijednost in lista_stolova:
    vrijednost.dostupnost()
print()


ukupna_cijena = 0
for svjetiljka in lista_svjetiljka:
    ukupna_cijena = ukupna_cijena + svjetiljka.cijena
print(f'Ukupna cijena svjetiljki je: {ukupna_cijena}')