cijene_proizvoda = []
broj_proizvoda = int(input('Unesite broj proizvoda: '))

for i in range(broj_proizvoda): 
    cijena = float(input(f'Unesite cijenu {i+1} proizvoda:')) #koji proizvod po redu unosim
    cijene_proizvoda.append(cijena)

print(cijene_proizvoda)

max_cijena = max(cijene_proizvoda)
min_cijena = min(cijene_proizvoda)

print(f'Najveća cijena proizvoda je: {max_cijena}')
print(f'Najveća cijena proizvoda je: {min_cijena}')