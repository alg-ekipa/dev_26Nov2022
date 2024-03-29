vozni_park = {
    1: ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2: ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3: ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4: ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5: ['Kombi', 'Mercedes', 'RI 002 ZZ', 2013, 12000.00],
    6: ['Kombi', 'Volkswagen', 'ZG 001 ZZ', 2011, 35000.00],
    7: ['Dostavno', 'Mercedes', 'ZG 002 ZZ', 2013, 9000.00],
    8: ['Dostavno', 'Volkswagen', 'ST 002 ZZ', 2013, 9300.00],
}

#print(vozni_park.keys())
#print(vozni_park.values())
#print(vozni_park)

for kljuc in vozni_park.keys():
    print(kljuc)

for vrijednost in vozni_park.values():
    print(vrijednost)

for kljuc, vrijednost in vozni_park.items():
    print(kljuc, ':', vrijednost)
    for element in vrijednost:
        print(element)


print(vozni_park[5][2]) #dohvat samo registracije
#lista_clan5 = vozni_park[5]
#print(lista_clan5[2])

#dohvat i ispis samo cijena
for kljuc, vrijednost in vozni_park.items():
    print(vozni_park[kljuc][-1])

#dohvat i ispis samo registracija
for kljuc, vrijednost in vozni_park.items():
    print(vozni_park[kljuc][2])

'''print(vozni_park[1][-1]) #dohvat cijene vozila
print(vozni_park[2][-1])
print(vozni_park[3][-1])
print(vozni_park[4][-1])
print(vozni_park[5][-1])
'''