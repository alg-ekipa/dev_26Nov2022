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

class Vozila:
    def __init__(self, vrsta, proizvodjac, registracija, godina_proizvodnje, cijena):
        self.vrsta = vrsta
        self.proizvodjac = proizvodjac
        self.registracija = registracija
        self.godina_proizvodnje = godina_proizvodnje
        self.cijena = cijena
    
    def ispis(self):
        print(f"Vozilo: {self.proizvodjac} - {self.godina_proizvodnje} - {self.cijena}")
    
    def ispis_dostavna(self):
        if self.vrsta == "Dostavno vozilo":
            print(f"{self.vrsta} {self.registracija}")

    def godiste(self):
        if self.godina_proizvodnje < 2015:
            print(f"Vozilo {self.registracija} je proizvedeno prije 2015.")

    def trazi_registraciju(self, trazena_registracija):
        if trazena_registracija == self.registracija:
            print(f"Trazeno vozilo je {self.proizvodjac}.")

lista_objekata_vozila = []

for value in vozni_park.values():
    v = value[0]
    p = value[1]
    r = value[2]
    g = value[3]
    c = value[4]
    vozilo_objekt = Vozila(v,p,r,g,c)
    #vozilo_objekt.ispis()        

    lista_objekata_vozila.append(vozilo_objekt)

for vozilo in lista_objekata_vozila:
    vozilo.ispis_dostavna()
    print()

for vozilo in lista_objekata_vozila:
    vozilo.godiste()
    print()

trazena_registracija = input("Upišite traženu registraciju: ")
for vozilo in lista_objekata_vozila:
    vozilo.trazi_registraciju(trazena_registracija)