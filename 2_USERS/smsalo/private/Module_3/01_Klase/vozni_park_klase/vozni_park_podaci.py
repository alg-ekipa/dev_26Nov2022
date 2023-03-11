vozni_park = {  
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00]
}

class Vozilo: 
    def __init__(self, vrsta, proizvodac, registracija, god_proizvodnje, cijena):
        self.vrsta = vrsta
        self.proizvodac = proizvodac
        self.registracija = registracija
        self.god_proizvodnje = god_proizvodnje
        self.cijena = cijena

    def ispis(self):
        print(f'\nVrsta: {self.vrsta}\nProizvođač: {self.proizvodac}\nRegistracija: {self.registracija}\nGodina proizvodnje: {self.god_proizvodnje}\nCijena: {self.cijena}')

    def ispis_dostavna(self):
        if self.vrsta == 'Dostavno vozilo':
            self.ispis()
            #print(f'\nVrsta: {self.vrsta}, Registracija: {self.registracija}')

    def trazi_regu(self, trazena_registracija):
        if trazena_registracija == self.registracija:
            self.ispis()