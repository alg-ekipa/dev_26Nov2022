cijene_proizvoda = {
    3441 : ['stol', 1200.00],
    5321 : ['uredski stolac', 800.00], 
    7121 : ['olovka', 10.50],
    4330 : ['rokovnik', 35.40]
}

'''
prikaz samo ključeva
prikaz samo vrijednosti
prikaz samo naziva proizvoda


for kljuc in cijene_proizvoda.keys():
    print(kljuc)
'''
for vrijednost in cijene_proizvoda.values():
    print(vrijednost)

lista_cijena = []
lista_vrijednosti = cijene_proizvoda.values() #uzima samo vrijednosti
print(lista_vrijednosti)

for vrijednost in lista_vrijednosti: #iz svake liste vrijednosti uzimamo samo cijenu (član s indeksom 1)
    lista_cijena.append(vrijednost[1])

print(lista_cijena)

'''
for kljuc, vrijednost in cijene_proizvoda.items(): # dohvat i ispis samo naziva proizvoda
    print(cijene_proizvoda[kljuc][0])'''

#izračunati prosječnu cijenu svih proizvoda
#ispisati proizvod s najvećom i najmanjom cijenom
prosjecna_cijena = sum(lista_cijena) / len(lista_cijena)
print(f'Prosječna cijena svih proizvoda je {prosjecna_cijena}.')

print(f'Najmanja cijena je {min(lista_cijena)}')

# traži u listi cijena najveću cijenu a zatim povezuje u riječniku s proizvodom i šifrom
max_cijena = max(lista_cijena)

for kljuc, vrijednost in cijene_proizvoda.items():
    if vrijednost [1] == max_cijena:
        max_proizvod = vrijednost[0]
        max_sifra = kljuc

print(f'Proizvod {max_proizvod} šifre {max_sifra} ima najveću cijenu koja iznosi: {max_cijena}kn.')

min_cijena = min(lista_cijena)

for kljuc, vrijednost in cijene_proizvoda.items():
    if vrijednost [1] == min_cijena:
        min_proizvod = vrijednost[0]
        min_sifra = kljuc

print(f'Proizvod {min_proizvod} šifre {min_sifra} ima najmanju cijenu koja iznosi: {min_cijena}kn.')