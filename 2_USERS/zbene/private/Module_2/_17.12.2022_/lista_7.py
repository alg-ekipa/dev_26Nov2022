ocjene_ucenika = [3, 2, 4, 4, 3, 5, 5, 2, 1, 3]
brojevi = [2, 7, 13, 23, 16, 9, 0, 11, 73, 92]
rijec = 'programiranje'
rijec_lista = list(rijec)

#print(f'Prije clear: {brojevi}')
#brojevi.clear()
#print(f'Nakon clear: {brojevi}')
'''
ocjene_ucenika_kopija = ocjene_ucenika.copy()
print(ocjene_ucenika)
print(ocjene_ucenika_kopija)

broj_trojki = ocjene_ucenika.count(3)
broj_petica = ocjene_ucenika.count(5)
print(f'Broj trojki iznosi {broj_trojki}.')
print(f'Broj petica iznosi {broj_petica}.')

print(rijec_lista)
r = rijec_lista.count('r')
print(f'Slovo r se pojavljuje {r} puta.')

#Na ocjene učenika dodajemo još a) 1 ocjenu, b) 3 ocjene

print(ocjene_ucenika)
ocjene_ucenika.append(5)
print(f'Ocjene nakon append: {ocjene_ucenika}')

ocjene_ucenika.extend([5,3,4])
print(f'Nakon extend:{ocjene_ucenika}')


#dohvat indeksa određenog člana
print(brojevi)
print(f'Indeks člana 11 iz liste brojevi je {brojevi.index(11)}.')

brojevi.extend([11,11])
print(brojevi)
print(f'Indeks prvog člana 11 iz liste brojevi je {brojevi.index(11)}.')

brojevi.pop(10) #brisanje člana sa navedenim indeksom
print(brojevi)

#Sortiranje članova liste
print()
brojevi_obrnuto = brojevi.reverse()
print(brojevi)
print(brojevi_obrnuto)
'''
#brojevi.sort()
brojevi_sortirano = sorted(brojevi)
print(f'Original lista brojevi: {brojevi}.')
print(f'Sortirana lista brojevi: {brojevi_sortirano}.')

print(brojevi)
for element in reversed(brojevi):
    print(element, end=' ')

brojevi_sortirano.reverse()
print(f'Reversana lista sortiranih brojeva (od najvećeg prema najmanjoj): {brojevi_sortirano}.')
'''
print(brojevi)
brojevi.insert(3, 4) #prvo: indeks ispred kojeg se ubacuje, drugo: konkretan član kojeg ubacujem
print(brojevi)
brojevi.insert(7,'A')
print(brojevi)
'''
print(max(brojevi))