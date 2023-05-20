cijene_proizvoda = {
    3441 : ['stol', 1200.00],
    5231 : ['uredski stolac', 800.00],
    7121 : ['olovka', 10.50],
    4330 : ['rokovnik', 35.40]
 }

#prikaz samo ključeva
#for kljuc, vrijednost in cijene_proizvoda.items():
#    print(cijene_proizvoda[kljuc][0])
#prikaz samo vrijednosti

#prikaz samo naziva proizvoda

lista_cijena = []
lista_vrijednosti = cijene_proizvoda.values() #uzimamo samo vrijenosti (liste)
print(lista_vrijednosti)

for vrijednost in lista_vrijednosti: # iz svke liste vrijednosti uzimamo samo cijenu (član s indeksom 1)
    #print(vrijednost[1])
    lista_cijena.append(vrijednost[1])
print(lista_cijena)

#prikaz samo cijena
#for kljuc, vrijednost in cijene_proizvoda.items():
#    print(cijene_proizvoda[kljuc][1])

#izračunati prosječnu cijenu svih proizvoda
prosjecna_cijena = sum(lista_cijena) / len(lista_cijena)
print(f'Prosječna cijena svih proizvoda je {prosjecna_cijena}')

#traži u listi cijena najveću cijenu a zatim povezuje u rječniku s proizvodom i šifrom
max_cijena = max(lista_cijena)
for kljuc, vrijednost in cijene_proizvoda.items():
    if vrijednost [1] == max_cijena:
        max_proizvod = vrijednost [0]
        max_sifra = kljuc

print(f'Proizvod {max_proizvod} šifre {max_sifra} ima najveću cijenu i ona iznosi {max_cijena}')

min_cijena = min(lista_cijena)
for kljuc, vrijednost in cijene_proizvoda.items():
    if vrijednost [1] == min_cijena:
        min_proizvod = vrijednost [0]
        min_sifra = kljuc

print(f'Proizvod {min_proizvod} šifre {min_sifra} ima najmanju cijenu i ona iznosi {min_cijena}')



