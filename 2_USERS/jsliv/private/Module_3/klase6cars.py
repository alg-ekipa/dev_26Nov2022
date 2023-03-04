class Vozilo:
    def __init__(self, vrsta, proizvodjac, registracija, godina_proizvodnje, cijena):
        self.vrsta = vrsta
        self.proizvodjac = proizvodjac
        self.registracija = registracija
        self.godina_proizvodnje = godina_proizvodnje
        self.cijena = cijena

    def ispis(self):
        print(f"\nVrsta: {self.vrsta}\nProizvodjac: {self.proizvodjac}\nRegistracija: {self.registracija}\nGodina Proizvodnje: {self.godina_proizvodnje}\nCijena: {self.cijena}")

    def ispis_dostavna(self):
        if self.vrsta == "Dostavno vozilo":
            #self.ispis()
            print(f"Vrsta: {self.vrsta}\nRegistacija: {self.registracija}")

    def trazi_reg(self, trazena_registracija):
        if trazena_registracija == self.registracija:
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

lista_objekta_vozila = []
"""
for vrijednost in vozni_park.values():
    print(vrijednost[0])
"""

for vrijednost in vozni_park.values():
    v = vrijednost[0]
    p = vrijednost[1]
    r = vrijednost[2]
    g = vrijednost[3]
    c = vrijednost[4]
    vozilo_objekt = Vozilo(v, p, r, g, c)
    vozilo_objekt.ispis()
    lista_objekta_vozila.append(vozilo_objekt)

#Zadatak ispisati sva dostavna vozila

for vozilo in lista_objekta_vozila:
    vozilo.ispis_dostavna()

#ZADATAK
#1. Ispišite sva vozila starija od 2015
#2. Ispišite vozila tražene registracije

    
trazena_registracija = input("Upiši traženu registraciju: ")
for vozilo in lista_objekta_vozila:
    vozilo.trazi_reg(trazena_registracija)
