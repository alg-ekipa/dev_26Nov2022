"""
cijena_priozvoda= {
    3441:['stol',1200.00],
    5321:['uredski stolac',800.00],
    7121:['olovka',10.50],
    4330:['rokovnik',35.40],

}

# Prikaz samo ključeva
#prikaz samo vrijednosti
#priokaz samo naziva proizvoda

#prikaz samo naziva proizvoda - items

for kljuc,vrijednost in cijena_priozvoda.items():
  print(cijena_priozvoda[kljuc][0])

lista_cijena = []
lista_vrijednosti = cijena_priozvoda.values 
print(lista_vrijednosti)

for vrijednost in lista_vrijednosti:
    print(vrijednost[1])






#prikaz samo cijena - items
#for kljuc,vrijednost in cijena_priozvoda.items():
# print(cijena_priozvoda[kljuc][1])



prosjecna_cijena = sum(lista_cijena) / len(lista_cijena)
print(f'Prosiječna cijena svih proizvoda je{prosjecna_cijena}')

print(max(lista_cijena))

max_cijena = max(lista_cijena)

for kljuc, vrijednost in cijena_priozvoda.items():
  if vrijednost[1] == max_cijena:
    max_proizvod = vrijednost[0]
    max_sifra = kljuc

    print(f'Proizvod {max_proizvod} šifre {max_sifra} ima najveću cijenu i
    ona iznosi {max_cijena}')


#napravi isto za min cijenu

"""