cijene_proizvoda={
    3441:['stol', 1200.00],
    5321:['Uredski stolac', 800.00],
    7121:['olovka',10.50],
    4330:['rokovnik', 35.40]
}
'''
#prikaz sam naziva proizvoda
for ključ, vrijednost in cijene_proizvoda.items():
    print(cijene_proizvoda[ključ][0])
'''

lista_cijena=[]
lista_vrijednosti=cijene_proizvoda.values() #uzimamo samo vrijednosti (liste)
print(lista_vrijednosti)

for vrijednost in lista_vrijednosti:#iz svake liste vrijednosti uzimamo sam cijenu(član s indeksom 1)
#print(vrijednost[1])
    lista_cijena.append(vrijednost[1])
print(lista_cijena)

#izračunati prosječnu cijenu svih proizvoda
#ispisati proizvod s najvećom i najmnajom cijenom

prosjecna_cijena=sum(lista_cijena)/len(lista_cijena)
print(f'Prosječna cijena svih proizvoda je {prosjecna_cijena}')

max_cijena=max(lista_cijena)

for kljuc,vrijednost in cijene_proizvoda.items():
    if vrijednost[1]==max_cijena:
        max_proizvod=vrijednost[0]
        max_sifra=kljuc
        print(f'Proizvod {max_proizvod} šifre {max_sifra} ima najveću cijenu i ona iznosi {max_cijena}')


'''
#prikaz samo cijena
for ključ, vrijednost in cijene_proizvoda.items():
     print(cijene_proizvoda[ključ][1])
'''
        

