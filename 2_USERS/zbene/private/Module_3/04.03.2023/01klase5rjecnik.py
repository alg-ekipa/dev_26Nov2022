class Vozilo:
    def __init__ (self, vrsta, proizvođač, registracija, god_proizvodnje, cijena):
        self.vrsta = vrsta
        self.proizvođač = proizvođač
        self.registracija = registracija
        self.god_proizvodnje = god_proizvodnje
        self.cijena = cijena
    
    def ispis (self):
        print (f'\nVrsta: {self.vrsta}\nProizvođač: {self.proizvođač}\nRegistracija: {self.registracija}\nGodina proizvodnje: {self.god_proizvodnje}\nCijena: {self.cijena}')

    def ispis_dostavna(self):
        if self.vrsta == 'Dostavno vozilo':
            self.ispis()
            print (f'\nVrsta: {self.vrsta}\nRegistracija: {self.registracija}')
    
    def ispis_starija_od_2015(self): #2. zadatak#
        if self.god_proizvodnje <2015:
            self.ispis()
            print (f'\nVrsta {self.vrsta}\nProizvođač: {self.proizvođač}\nRegistracija: {self.registracija}\nGodina proizvodnje: {self.god_proizvodnje}\nCijena: {self.cijena}')

    def traži_regu (self, tražena_registracija): #3. zadatak#
        if tražena_rega == self.registracija:
            self.ispis()

vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00],
}

lista_objekata_vozila = []

for vrijednost in vozni_park.values():
    v = vrijednost [0]
    p = vrijednost [1]
    r = vrijednost [2]
    g = vrijednost [3]
    c = vrijednost [4]
    vozilo_objekt = Vozilo (v, p, r, g, c)
    #vozilo_objekt.ispis()
    lista_objekata_vozila.append(vozilo_objekt)

#print(lista_objekata_vozila)

#ZADATAK: ispisati sva dostavna vozila - metoda ispis_dostavno() piše se u klasu Vozilo

for vozilo in lista_objekata_vozila:
    vozilo.ispis_dostavna()

for vozilo in lista_objekata_vozila: #2 zadatak#
    vozilo.ispis_starija_od_2015()

for vozilo in lista_objekata_vozila: #3. zadatak#
    vozilo.traži_regu(tražena_rega)

#TO DO:
# 1. ispišite sva vozila starija od 2015.g.
# 2. ispis vozila tražene registracije

tražena_registracija = input ('Unesi podatak o registraciji: ')