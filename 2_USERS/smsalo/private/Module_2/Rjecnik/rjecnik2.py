vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.53],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'OS 003 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 003 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Volkswagen', 'ZG 001 AA', 2011, 35000.00],
    6 : ['Kombi', 'Volkswagen', 'ZG 005 AA', 2013, 42000.00],
    7 : ['Dostavno', 'Mercedes', 'ST 005 BA', 2017, 52000.00],
    7 : ['Dostavno', 'Mercedes', 'ST 005 BA', 2017, 52000.00],
    8 : ['Dostavno', 'Opel', 'KA 072 CA', 2022, 90000.00]
    }

#print(vozni_park)
#print(vozni_park.values())

for vrijednost in vozni_park.values():
    print(vrijednost)

for kljuc in vozni_park.keys():
    print(kljuc)

for kljuc, vrijednost in vozni_park.items():
    print(kljuc, ':', vrijednost)
    for element in vrijednost:
        print(element)

print(vozni_park[5][2])
#lista_clan5 = vozni_park[5]
#print(lista_clan5[2])

#dohvat i ispis cijena
for kljuc, vrijednost in vozni_park.items():
    print(vozni_park[kljuc][-1])

#dohvat i ispis registracija
for kljuc, vrijednost in vozni_park.items():
    print(vozni_park[kljuc][2])
