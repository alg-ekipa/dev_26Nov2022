'''
Napraviti riječnik i ispisati:
- sve vreijdenost
- kljuc pa vreijdnsoti
- samo registraciju  5. vozila
'''


vozni_park ={
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45.000,00] ,
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47.000,00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ',  2018, 78.000,00],
    4 : ['Tegljač', 'MANRI', '002 ZZ', 2020, 97.000,00],
    5 : ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12.000,00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35.000,00],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9.000,00],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9.300,00]
}

#print(vozni_park.keys())
#print(vozni_park.values())

for vrijednost in vozni_park.values():  # ispisuje samo vrjednosti u rijecnicima
    print(vrijednost)

for kljuc,vrijednost in vozni_park.items(): # ispisuje  kljuc i vrjednosti u rijecnicima
    print(kljuc,':' ,vrijednost)

print(vozni_park[5][2]) # dobivamo listu, pa mozemo ovako ispisati regu
lista_clan5 = vozni_park[5]  # iz rijecnika vadimo listu
print(lista_clan5[2]) # ispisujemo regu iz liste