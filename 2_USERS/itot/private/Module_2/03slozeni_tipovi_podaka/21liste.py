primjer_rijeci = list('automatizacija')
print(primjer_rijeci)

'''prolaz kroz lostu preko indexa'''
duljina = len(primjer_rijeci)
print(duljina)

for i in range(14):
    print(primjer_rijeci[i], end=' ')

print()
'''Prolaz kroz listu direktno preko clana'''
for slovo in primjer_rijeci:
    print(slovo, end=' ')

print()

'''unos 5 ocjena u listu'''

lista_za_unos = []
broj_clanova =5

for i in range(broj_clanova):
    ocjena=int(input('Unesi ocjenu: '))
    lista_za_unos.append(ocjena)

print (lista_za_unos)