ocjene_ucenika = [3,2,4,4,3,5,5,2,1,3]
brojevi =[2,7,13,23,16,9,0,11,73,92]
rijec = 'Programiranje'
rijec_lista = list(rijec)
'''
print(f'Prije clear: {brojevi}')
brojevi.clear()
print(f'Nakon clear: {brojevi}')

ocjene_ucenika_kopija = ocjene_ucenika.copy()
print(f'Ocjene original: {ocjene_ucenika}')
print(f'Ocjene kopija: {ocjene_ucenika_kopija}')

broj_trojki= ocjene_ucenika.count(3)
broj_petica = ocjene_ucenika.count(5)

print(f' Broj trojki ucenika je {broj_trojki}, a broj petica je {broj_petica}')

print(rijec_lista)
r = rijec_lista.count('r')
print(f' Slovo r se pojavljuje {r} puta')

#Na ocjene učeniaka dodajemo još a) jednu ocjenu  b) tri ocjene


print(ocjene_ucenika)
ocjene_ucenika.append(5)
print(f'Nakon append: {ocjene_ucenika}')

nove_ocjene = [5,3,4]
ocjene_ucenika.extend(nove_ocjene)
print(f'Nakon extend: {ocjene_ucenika}')


ocjene_ucenika.extend([5,3,4])
print(f'Nakon extend: {ocjene_ucenika}')
'''


'''

#Dohvat člana sa navedenim indeksom
print(brojevi)
print(f'Indeksa člana 11 u listi je: {brojevi.index(11)}')

brojevi.extend([11, 11])
print(brojevi)
print(f'Indeksa člana 11 (prvo pojavljivanje) u listi je: {brojevi.index(11)}')

#Brisanje člana sa navedenim indeksom
brojevi.pop(10) 
print(brojevi)

#Sortiranje članova liste
print()
brojevi_obrnuto = brojevi.reverse()
print(brojevi)
print(brojevi_obrnuto)
'''

#brojevi.sort()
brojevi_sortirano = sorted(brojevi)
print(f'Original lista {brojevi}')
print(f'Sortirana lista {brojevi_sortirano}')
'''
print(brojevi)
for element in reversed(brojevi):
    print(element, end=' ')
'''
brojevi_sortirano.reverse()
print(f'Revesre lista sortiranih brojeva od najveceg do najmanjeg {brojevi_sortirano}')

print(brojevi)
brojevi.insert(3, 4)  #Prvo: indeksa isped koeg člana ubacujemo, Drugo: Koji član ubacujem
print(brojevi)
brojevi.insert(7, 'A')
print(brojevi)