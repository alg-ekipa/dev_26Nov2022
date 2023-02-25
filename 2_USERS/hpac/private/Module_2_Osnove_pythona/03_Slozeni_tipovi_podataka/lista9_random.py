import random

# Kreiramo listu od X članova koje nasumično bira u rasponu od 0 do 30

lista_random = []

for i in range(20):
    broj = random.randint(0,30)
    #print(broj, end=' ')
    lista_random.append(broj)
print(lista_random)

# Nasumično izabiranje jednog člana liste i ispis njegovog indeksa

random_clan = random.choice(lista_random)
print(f'Nasumično izabrani član liste {random_clan}')
print(f'Indeks tog člana je {lista_random.index(random_clan)}')

# Nasumično izaberimo indeks i onda po tom indeksu ispiši član
print()
random_indeks = random.randint(0,19)
print(f'Nasumično izabrani indeks liste {random_indeks}')
print(f'Član sa tim indeksom je {lista_random[random_indeks]}')

slovo = input('Unesi slovo ')
print(slovo.upper())
