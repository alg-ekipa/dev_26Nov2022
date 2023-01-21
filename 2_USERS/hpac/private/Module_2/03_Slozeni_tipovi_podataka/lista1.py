nasa_lista = [154, 'tekst', 'jos jedan tekst', 3.14, True, 'Pa opet tekst']

print(nasa_lista)

print(nasa_lista[1], nasa_lista[3], nasa_lista[4])

print(f'Prvi clan liste je {nasa_lista[0]}, a drugi clan liste je {nasa_lista[1]}')

umnozak = nasa_lista[0] * nasa_lista[3]
print(umnozak)

nasa_lista[2] = ' Zagreb'
print(nasa_lista)

nasa_lista[4] = 5
print(nasa_lista)

'''

Ovo nije zamjena elemenata na mjestu, jer u glavnoj definiraj listi ne postoje elementi pa nema sta zamijeniti

prazna_lista = []
print(prazna_lista)
prazna_lista[0] = 56
prazna_lista[1] = 33
print(prazna_lista)
'''

zadaci = [
    'Odabrati naziv liste',
    'Unijeti element liste',
    'Pokrenuti aktivnosti'
    ]

print(zadaci)
print(zadaci[0])
print(zadaci[1])
print(zadaci[2])

prvi_element = zadaci[0]
drugi_element = zadaci[1]
treci_element = zadaci[2]
print(prvi_element)
print(drugi_element)
print(treci_element)