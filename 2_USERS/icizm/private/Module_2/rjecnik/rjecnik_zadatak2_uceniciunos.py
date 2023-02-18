'''
Unosimo 5 učenika preko tipkovnice(imena)
svakom učeniku unosimo po 3 ocjene
na kraju ispisujemo ocjene
ime je ključ a vrijednosti su ocjene
'''
ucenici_ocjene = {}

for i in range(5): 
    kljuc = input(f'Unesi ime {i+1}. učenika: ')
    lista_ocjena = []
    for j in range(3):
        vrijednost = int(input(f'Unesi {j+1}. ocjenu učenika: '))
        lista_ocjena.append(vrijednost)
        ucenici_ocjene[kljuc] = lista_ocjena

print(ucenici_ocjene)

for k, v in ucenici_ocjene.items():
    print(f'{k} : {v}')