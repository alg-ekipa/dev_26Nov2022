"""
n_torka = (4,7,2,0,1)
lista = [4,7,2,0,1]

print(n_torka[2])
print(lista[2])
lista[2]=8
print(lista)
n_torka[2]=8

"""

vozni_park = {
    1 : ['Kamion','Iveco','OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion','Iveco','OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač','MAN','RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač','MAN','RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi','Mercedes','PU 001 ZZ', 2013, 12000.00],
    6 : ['Kombi','Volkswagen','PU 002 ZZ', 2011, 35000.00],
    7 : ['Dostavno','Mercedes','ZG 001 ZZ', 2014, 9000.00],
    8 : ['Dostavno','Volkswagen','ZG 003 ZZ', 2013, 9300.00]
}

'''
print(vozni_park.keys())
print()
print(vozni_park.values())  #lista unutar liste
print()
'''
for kljuc in vozni_park.keys():
    print(kljuc)
print() 
for vrijednost in vozni_park.values():
    print(vrijednost)

for kljkuc,vrijednost in vozni_park.items():
    print(kljuc,':', vrijednost)
    for element in vrijednost:
        print(element)

print(vozni_park[5][2]) #sve ovo dolje, zajedno isprintano
#lista_clan5 = vozni_park[5]
#print(lista_clan5[2])

