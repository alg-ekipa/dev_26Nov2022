cijene_proizvoda ={
    1 : ['stol', 1200.00] ,
    2 : ['uredski stolac', 800.00],
    3 : ['olovka', 10.53],
    4 : ['rokovnik', 35.17]

}

'''prikaz:
samo kljuceva
samo vrijednosti
samo naziva proizvoda'''


'''prikaz vrijednosti cijene    '''
#for kljuc,vrijednost in cijene_proizvoda.items():
#    print(cijene_proizvoda[kljuc][1])
 

''' dodavanje cijene u listu'''
lista_cijena =[]
lista_vrijednosti = cijene_proizvoda.values()
print(lista_vrijednosti)

for vrijednost in lista_vrijednosti:
    lista_cijena.append(vrijednost[1])
print(lista_cijena)

'''
prosjecna cijena proizvoda kada imamo listu

'''

prosjecna_cijena = sum(lista_cijena)/len(lista_cijena)

print(f'prosjkecna cijena svih proizvoda je  {prosjecna_cijena}')

'''najskuplji i najeftiniji proizvod ali sa svim podatcima, pomocu kljuca'''

max_cijna = max(lista_cijena)
min_cijna = min(lista_cijena)

for kljuc,vrijednost in cijene_proizvoda.items():
    if vrijednost[1] == max_cijna:
        max_proizvod = vrijednost[0]
        max_sifra = kljuc
    if vrijednost[1] == min_cijna:
        min_proizvod = vrijednost[0]
        min_sifra = kljuc

print(f'Proizvod {max_proizvod} sifre {max_sifra} ima najvecu cijenu koja iznosi {max_cijna} ')

print(f'Proizvod {min_proizvod} sifre {min_sifra} ima najvecu cijenu koja iznosi {min_cijna} ')

