cijene_proizvoda = {
    3441 : ['Stol', 1200.00],
    3542 : ['Stolica', 500.00],
    4528 : ['Lampa', 470.50],
    8565 : ['Registrator', 52.45]
}

# prikaz samo ključeva
for kljuc in cijene_proizvoda.keys():
    print(kljuc)

# prikaz samo vrijednosti
for vrijednost in cijene_proizvoda.values():
    print(vrijednost)

# prikaz samo naziva proizvoda
for kljuc, vrijednost in cijene_proizvoda.items():
    print(cijene_proizvoda[kljuc][0])

# prikaz samo cijena
for kljuc, vrijednost in cijene_proizvoda.items():
    print(cijene_proizvoda[kljuc][1])

zbroj=0
for kljuc, vrijednost in cijene_proizvoda.items():
    cijena=cijene_proizvoda[kljuc][1]
    zbroj = zbroj + cijena
print(zbroj)

#naparaviti listu cijena
lista_cijena = []
lista_vrijednosti = cijene_proizvoda.values()
for vrijednost in lista_vrijednosti:
    lista_cijena.append(vrijednost[1])
print(lista_cijena)

#prosječna cijena svih proizvoda
prosjecna_cijena=sum(lista_cijena) / len(lista_cijena)
print(f'Prosječna cijena svih proizvoda je {prosjecna_cijena}.')

#ispisati proizvod s najvećom i najmanjom cijenom
max_cijena = max(lista_cijena)
for kljuc, vrijednost in cijene_proizvoda.items():
    if vrijednost[1]==max_cijena:
        max_proizvod  = vrijednost[0]
        max_sifra = kljuc
print(f'Proizvod {max_proizvod} šifre {max_sifra} ima najveću cijenu i ona iznosi {max_cijena}.')

min_cijena = min(lista_cijena)
for kljuc, vrijednost in cijene_proizvoda.items():
    if vrijednost[1]==min_cijena:
        min_proizvod  = vrijednost[0]
        min_sifra = kljuc
print(f'Proizvod {min_proizvod} šifre {min_sifra} ima najmanju cijenu i ona iznosi {min_cijena}.')
