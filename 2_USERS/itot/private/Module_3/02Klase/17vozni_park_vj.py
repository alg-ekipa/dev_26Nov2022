class  Vozila:
    def __init__(self, vrsta, porizvodac, registracija, god_proizvodnje, cijena):
        self.vrsta=vrsta
        self.proizvodaca=porizvodac
        self.registracija=registracija
        self.god_proizvodnje = god_proizvodnje
        self.cijena = cijena

    def ispis(self):
        print(f'\nVrsta: ')

    def trazena_registracija(self,trazena_rega):
        if trazena_rega ==self.trazena_registracija:
            self.ispis



        


vozni_park ={
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00] ,
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 470000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ',  2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00]
}


lista_objekata_vozila = []

fpr vriejdnost in vozni_park.values():
    v = vrijednost[0]
    p = vrijednost[1]
    r = vrijednost[2]
    g = vrijednost[3]
    c = vrijednost[4]
    vozilo_objekt = Vozilo(v,p,r,g,c)
    #vozilo_objekt.ispis()
    lista_objekata_vozila.append(vozilo_objekt)

#print(lista_objekata_vozila)

#Zadatak: ispisati sva dostavna vozila - metodom ispis_dostavno() piše se u klasu vozila
for vozila in lista_objekata_vozila:
    vozila.ispis_dostavna()

#TODO
# 1. ispisi sva vozila starija od 2015
# 2. ispis vozilatrazena registracije

#1


#2
trazena_rega = 

