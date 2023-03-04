class Vozilo:
    def __init__(self, vrsta, proizvodac, registracija, god_proizvodnje, cijena):
        self.vrsta=vrsta
        self.proizvodac=proizvodac
        self.registracija=registracija
        self.god_proizvodnje=god_proizvodnje
        self.cijena=cijena
    
    def ispis(self):
        print(f'\nVrsta: {self.vrsta}\nProizvođač: {self.proizvodac}\nRegistracija: {self.registracija}\nGodina proizvodnje: {self.god_proizvodnje}\nCijena: {self.cijena}')
        
    def ispis_dostavna(self):
        if self.vrsta=='Dostavno':
            self.ispis()
            #print(f'Vrsta {self.vrsta}, registracija: {self.registracija}') 
    
    def starost(self):
        if self.god_proizvodnje>2015:
            self.ispis()
    
    def pret_registracije(self, trazena_rega):
        if trazena_rega==self.registracija:
            self.ispis()

vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.53],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'OS 003 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 003 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Volkswagen', 'ZG 001 AA', 2011, 35000.00],
    6 : ['Kombi', 'Volkswagen', 'ZG 005 AA', 2013, 42000.00],
    7 : ['Dostavno', 'Mercedes', 'ST 005 BA', 2017, 52000.00],
    8 : ['Dostavno', 'Opel', 'KA 072 CA', 2022, 90000.00]
    }

lista_objekata_vozila=[]

for vrijednost in vozni_park.values():
    v=(vrijednost[0])
    p=(vrijednost[1])
    r=(vrijednost[2])
    g = (vrijednost[3])
    c= (vrijednost[4])
    vozilo_objekt=Vozilo(v, p, r, g, c)
    lista_objekata_vozila.append(vozilo_objekt)
    #vozilo_objekt.ispis()

#print samo dostavna vozila
#pise se u klasu def ispis dostavna

for vozilo in lista_objekata_vozila:
    vozilo.ispis_dostavna()

#to do: ispis sva vozila starija od 2015
#       ispis vozila tražene registacije

for godina in lista_objekata_vozila:
    godina.starost()

trazena_rega=input('Unesite registraciju automobila koju želite prikazati:')
for vozilo in lista_objekata_vozila:
    vozilo.pret_registracije(trazena_rega)
