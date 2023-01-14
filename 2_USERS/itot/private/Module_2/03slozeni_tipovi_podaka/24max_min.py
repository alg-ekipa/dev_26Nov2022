'''
Napisi program koji unosi cijene odredenog broja artikala
- unijeti broj proizvoda
- unesi njihvoe cijene
- sve se sprema u listu
- koja je najvisa, a koja najniza cijena proizvoda
- koja je razlika mx i min-a
'''


cijene_proizvoda = []
broj_artikala=int(input('Unesi broj artikala '))


for i in range(broj_artikala):
    cijena=float(input(f'unesi cijenu {i+1} artikl: '))
    cijene_proizvoda.append(cijena)

print(cijene_proizvoda)


max_cijena=max(cijene_proizvoda)
min_cijena=min(cijene_proizvoda)


print(f'Od unesenih proizvoda najskuplji je {max_cijena}, a najejftiniji {min_cijena}. Razlika maximalne i minimalne cijene je {max_cijena-min_cijena}')