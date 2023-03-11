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
import os

stolovi_rjecnik = {
    '0186': ['stol Jack', 700.00, True, 'smeđa', 'drvo', 4],
    '0203': ['stol Kathy', 880.00, True, 'smeđa', 'staklo', 3],
    '1234': ['stol Tomy', 1250.00, True, 'bijela', 'staklo', 4],
    '4002': ['stol Ohm', 940.00, True, 'crna', 'metal', 1],
    '0923': ['stol Heda', 940.00, False, 'crna', 'drvo', 1],
    '1773': ['stol Lucas', 940.00, True, 'crna', 'drvo', 4]
}

stolovi_objekti = []


svjetiljka_rjecnik = {
    '0001': ['svjetiljka Zadar', 1200.00, True, 'zlatna', 'zlato', 'zarulja'],
    '0002': ['svjetiljka Zagreb', 2800.00, True, 'plava', 'staklo', 'zarulja'],
    '0003': ['svjetiljka Dubrava', 800.00, False, 'zelena', 'srebro', 'bez'],
    '0004': ['svjetiljka Rijeka', 400.00, False, 'roza', 'zlato', 'bez'],
    '0005': ['svjetiljka Dubrovnik', 5400.00, True, 'magenta', 'platina', 'zarulja'],
    '0006': ['svjetiljka Madrid', 55950.00, True, 'crvena', 'platina', 'bez']
}


svjetiljka_objekti = []



tepisi_rjecnik = {
    '0007': ['tepih Melita', 8000.00, True, 'zlatna', 'pamuk', 'okrugao'],
    '0008': ['tepih Lana', 7200.00, True, 'plava', 'svila', 'pravokutni'],
    '0009': ['tepih Sanja', 480.00, False, 'zelena', 'pamuk', 'okrugao'],
    '0010': ['tepih Emina', 525.00, False, 'roza', 'plastika', 'pravokutni'],
    '0011': ['tepih Laura', 320.00, True, 'magenta', 'plastika', 'okrugao'],
    '0012': ['tepih Tea', 12524.00, True, 'crvena', 'svila', 'pravokutni']
}

tepisi_objekti= []



class Proizvod:
    #konstruktor je metoda koja se zove __init__(initializacija)

    def __init__(self, sifra, cijena, raspolozivost, boja, materijal):
        self.sifra = sifra
        self.cijena=cijena
        self.raspolozivost=raspolozivost
        self.boja=boja
        self.materijal=materijal
    
    def ispis(self):
        print('proba Proizvod')
        print(f"Proizvod: {self.sifra}, cijena: {self.cijena}, raspolozivpost: {self.raspolozivost}, ima boju: {self.boja}, iz materijala: {self.materijal}")


class Stol(Proizvod):

    def __init__(self, sifra, cijena, raspolozivost, boja, materijal, dimenzije):
        super().__init__(sifra, cijena, raspolozivost, boja, materijal)
        self.dimenzije = dimenzije
        
    def ispis(self):
        print('proba Stolovi')
        print(f"Proizvod: {self.sifra}, cijena: {self.cijena}, raspolozivpost: {self.raspolozivost}, ima boju: {self.boja}, iz materijala: {self.materijal}, dimenzije: {self.dimenzije}")



class Svjetiljka(Proizvod):

    def __init__(self, sifra, cijena, raspolozivost, boja, materijal, zarulja):
        super().__init__(sifra, cijena, raspolozivost, boja, materijal)
        self.zarulja = zarulja
        
    def ispis(self):
        print('proba Stolovi')
        print(f"Proizvod: {self.sifra}, cijena: {self.cijena}, raspolozivpost: {self.raspolozivost}, ima boju: {self.boja}, iz materijala: {self.materijal}, zarulja: {self.zarulja}")



class Tepih(Proizvod):

    def __init__(self, sifra, cijena, raspolozivost, boja, materijal, oblik):
        super().__init__(sifra, cijena, raspolozivost, boja, materijal)
        self.oblik = oblik
        
    def ispis(self):
        print('proba Stolovi')
        print(f"Proizvod: {self.sifra}, cijena: {self.cijena}, raspolozivost: {self.raspolozivost}, ima boju: {self.boja}, iz materijala: {self.materijal}, oblik: {self.oblik}")


os.system('cls')


for stol in stolovi_rjecnik:
    indeks=stol.index
    lista=stol.values()
    a = lista[0]
    b = lista[1]
    c = lista[2]
    d = lista[3]
    e = lista[4]
    f = lista[5]
    stol_objekt = Stol(indeks,a,b,c,d,e,f)
    stol_objekt.ispis()
    stolovi_objekti.append(stol_objekt)





for v in korisnici.values():
            #'user_name': ['naziv tvrtke', 'adresa', 'Lozinka', godište osnivanja, vrsta korisnika]
            print(korisnici.keys())
            print(f' Naziv tvrtke: {v[0]}, adresa: {v[1]}, godište osnivanja: {v[3]}, vrsta korisnika: {v[4]}')




for i in range(6):
    #proizvodac= input ('Unesi proizvodaca automobila:')
    #model = input ('Unesi model automobila:')
    stol=stolovi_rjecnik[i+1]
    stol_objekt= Stol(stol[0],stol[1], stol[2], stol[3], stol[4], stol[5])
    stolovi_objekti.append(stol_objekt)


for stol in stolovi_objekti:
    input()
    stol.ispis()