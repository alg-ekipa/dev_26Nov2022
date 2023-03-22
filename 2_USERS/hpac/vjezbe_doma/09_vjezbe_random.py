import random

brojevi_random = []

for i in range(15):
    broj = random.randint(0,30)
    brojevi_random.append(broj)

print(brojevi_random)

clan_radnom = random.choice(brojevi_random)

print(f' Izabrani nasumični član liste je: {clan_radnom}')
print(f' Indeks izabranog člana liste je: {brojevi_random.index(clan_radnom)}')

index_random = random.randint(0,14)
print(f'Nasumično odabrani indeks u nizu je: {index_random}')
print(f'Broj koji se nalati pod tim indeksom je: {brojevi_random[index_random]}')

