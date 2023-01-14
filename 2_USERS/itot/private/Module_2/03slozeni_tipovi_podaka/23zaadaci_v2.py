'''
unos ocjene ucenika
- izracunati prosjek
ne zna se koliko je ucenika
- ispis prosjeka ucjenika

dodatak:
koliko ucenika ima ocjenu:
 - 5
 - 1
 formirati ispis:
'''


ocjene_ucenika = []
broj_ucenika=int(input('Unesi broj ucenika: '))

for i in range(broj_ucenika):
    ocjena=int(input(f'Unesi ocjenu {i+1}. ucenika:'))
    ocjene_ucenika.append(ocjena)
    

print(ocjene_ucenika)
print(f'Aritmeticka sredina od ocjena {len(ocjene_ucenika)} je {(sum(ocjene_ucenika)/len(ocjene_ucenika))}')

print('drugi dio zadatka')

ocjena_5=ocjene_ucenika.count(5)
ocjena_1=ocjene_ucenika.count(1)

print(f'Među {len(ocjene_ucenika)} njhi {ocjena_1} ima ocjenu 1, a {ocjena_5} ima ocjenu 5.')