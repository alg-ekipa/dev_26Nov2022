#Napišite program koji će u listu unositi ocjene učenika, a zatim izračunati njihov prosjek ocjena. Nije poznato unaprijed koliko učenika ima u razredu, pa se taj broj unosi na početku programa. Na kraju se ispisuje: Prosjek ocjena ovih učenika iznosi ___.
'''ocjene = []
broj_ucenika = int(input('Unesi broj učenika: '))
zbroj = 0

for i in range(broj_ucenika):
    ocjena = int(input('Unesi ocjenu učenika: '))
    ocjene.append(ocjena)
zbroj = sum(ocjene)
prosjek = zbroj/broj_ucenika
print(f'Prosjek ocjena ovih učenika iznosi {prosjek}.')

#U prethodnom zadatku dodati izračun i ispis koliko učenika ima ocjenu 5, a koliko ocjenu 1. Ispis bi trebao biti: Među ovim učenicima njih __ ima ocjenu 5, a __ učenika ima ocjenu 1.

broj_petica = ocjene.count(5)
broj_jedinica = ocjene.count(1)

print(f'Među ovim učenicima njih {broj_petica} ima ocjenu 5, a {broj_jedinica} učenika ima ocjenu 1.')
'''
#Napišite program koji unosi cijene određenog broja proizvoda. Unosi se broj proizvoda i njihove cijene, koje se spremaju u listu. Zatim se ispisuje najviša i najniža cijena proizvoda, te njihova razlika.

cijene_proizvoda = []
broj_proizvoda = int(input('Unesi broj proizvoda: '))

for i in range(broj_proizvoda):
    cijena = float(input(f'Unesi cijenu {i+1} proizvoda: '))
    cijene_proizvoda.append(cijena)

print(cijene_proizvoda)
max_cijena = max(cijene_proizvoda)
min_cijena = min(cijene_proizvoda)

print()

print(f'Najviša cijena proizvoda je: {max_cijena}')
print(f'Najniža cijena proizvoda je: {min_cijena}')