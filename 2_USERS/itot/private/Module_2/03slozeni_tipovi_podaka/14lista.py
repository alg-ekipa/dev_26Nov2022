'''
Unesi neku listu, pa:

- ispis
- dohvatiti neke clanove printom
- množenje clanova liste
- provjera promjenjivosti liste
- prazna lista

'''

lista_a = [323, 'probni_tekst', 'jos nesto teksta', 3.14, True, 'Pa opet tekst']

# ispis
print(lista_a)

# dohvatiti neke clanove printom
print(lista_a[0], lista_a[5])
print(f' prvi član liste je {lista_a[0]}, a peti {lista_a[4]}')

# množenje clanova liste
umnožak = lista_a[0]*lista_a[3]
print(umnožak)

#- provjera promjenjivosti liste
lista_a[2] = 'Zagreb'
print(lista_a)

#prpazna lista

''' ovo je krivo dodjeljivanje
prazna_lista = []
print(prazna_lista)
prazna_lista[0]=56
prazna_lista[1]=232
print(prazna_lista)
'''


zadaci = [
    'Odabrati naziv liste',
    'unijeti elemente liste',
    'pokrenuti aktivnosti'
    ]

print(zadaci)
prvi_element = zadaci[0]
drugi_element = zadaci[1]
treci_element = zadaci [2]
print(prvi_element)
print(drugi_element)
print(treci_element)


