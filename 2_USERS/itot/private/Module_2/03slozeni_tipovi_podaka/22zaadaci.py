'''
unos ocjene ucenika
- izracunati prosjek
ne zna se koliko je ucenika
- ispis prosjeka ucjenika
'''


ocjene_ucenika = []
broj_ucenika=int(input('Unesi broj ucenika: '))

for i in range(broj_ucenika):
    ocjena=int(input(f'Unesi ocjenu {i+1}. ucenika:'))
    ocjene_ucenika.append(ocjena)
    

print(ocjene_ucenika)
print(f'Aritmeticka sredina od ocjena {len(ocjene_ucenika)} je {(sum(ocjene_ucenika)/len(ocjene_ucenika))}')