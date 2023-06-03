nasa_lista = [154, 'tekst', 'jos jedan tekst', 3.14, True, 'Pa opet tekst']

print(nasa_lista)

print(nasa_lista[0], nasa_lista[3])

print (f'Prvi član naše liste je {nasa_lista[0]}, a četvrti član {nasa_lista[3]}')

umnožak = nasa_lista[0] * nasa_lista [3]
print(umnožak)
# print(nasa_lista[1] * nasa_lista[2]) # ne možeš množiti 2 stringa

nasa_lista[2] = 'Zagreb'
print(nasa_lista)

nasa_lista[4] = 6
print(nasa_lista)

#prazna_lista = []
#print(prazna_lista)
#prazna_lista[0] = 56 # nema podataka u 19. retku
#prazna_lista[1] = 33
#print(prazna_lista)

zadaci = [
    'Odabrati naziv liste',
    'Unijeti elemente liste',
    'Pokrenuti aktivnost'
]

print(zadaci)
print(zadaci[0])
print(zadaci[1])
print(zadaci[2])

prvi_element = zadaci[0]
drugi_element = zadaci[1]
treći_element = zadaci[2]
print(prvi_element)
print(drugi_element)
print(treći_element)