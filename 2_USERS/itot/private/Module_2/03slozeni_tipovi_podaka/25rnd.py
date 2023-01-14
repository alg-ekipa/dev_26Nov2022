'''
Kreiramo listu od 20 nasumicno izabranih clanova u rasponu 0-30
'''


import random

lista_rnd_brojeva = []
broj_clanova = 20
pocetak_rnd_brojeva=0
kraj_rnd_brojeva=30

'''unos 20 rnd clanova u listu'''
for i in range(broj_clanova):

    broj = random.randint(pocetak_rnd_brojeva, kraj_rnd_brojeva)
    lista_rnd_brojeva.append(broj)

print(lista_rnd_brojeva)

'''odabir rnd broja iz liste'''
rnd_clan=random.choice(lista_rnd_brojeva)
print(f'Rnd clan je: {rnd_clan}')
print(f'Index rnd clana je: {lista_rnd_brojeva.index(rnd_clan)}')


''' nasumicno izabrati index i ispistati clana tog indexa'''
rnd_index=random.randint(0,(broj_clanova-1))
print(f'Index rnd broja je: {rnd_index}')
print(f'Broj pod tim indexom je: {lista_rnd_brojeva[rnd_index]}')

