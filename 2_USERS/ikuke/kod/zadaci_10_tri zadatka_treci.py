
cijena_proizvoda=[]
broj_proizvoda=input('unesi broj proizvoda u skladištu:')
broj_proizvoda=int(broj_proizvoda)+1
for i in range (1,broj_proizvoda):
    cijena=input("'unesi cijenu proizvoda: ', i, ':'")
    cijena=int(cijena)
    cijena_proizvoda.append(cijena)
print(cijena_proizvoda)


min=cijena_proizvoda[0]
max=cijena_proizvoda[0]

for cijena in cijena_proizvoda:
    if cijena<min:
        min=cijena
    if cijena>max:
        max=cijena
print('minimalna cijena proizvoda je:', min)
print('maksimalna cijena proizvoda je:', max)

print('razlika cijene proizvoda je', max-min)