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

for kljuc, vrijednost in vozni_park.items():
    print(vozni_park[kljuc][4])

lista_cijena = []

lista_vrijednosti = vozni_park.values()
for vrijednost in lista_vrijednosti:
    lista_cijena.append(vrijednost[4])
print(lista_cijena)

prosjecna_cijena = sum(lista_cijena) / len(lista_cijena)
print(round(prosjecna_cijena, 2))