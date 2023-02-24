'''
Iz rijecnika vadimo sve cijene vozila i sve registracije
'''


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

'''dohvat cijena'''

for kljuc,vrijednost in vozni_park.items(): # zavrtimo for petlju i tako izvucemo podatke
    print(vozni_park[kljuc][-1])   #rijednik[kljuc][clan]

'''dohvat registracija'''

for kljuc,vrijednost in vozni_park.items():
    print(vozni_park[kljuc][2])
