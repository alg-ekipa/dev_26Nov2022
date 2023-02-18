ocjene_ucenika=[3,2,4,4,3,5,5,2,1,3]
brojevi=[7, 14, 24, 44, 27, 6, 9, 87, 16, 19]
rijec='programiranje'
rijec_lista=list(rijec)

#print(f'Prije clear: {brojevi}')
#brojevi.clear()
#print(f'Nakon clear: {brojevi}')

ocjene_ucenika_kopija=ocjene_ucenika.copy()
print(ocjene_ucenika)
print(ocjene_ucenika_kopija)

broj_trojki=ocjene_ucenika.count(3)
broj_petica=ocjene_ucenika.count(5)
print(f'Broj trojki iznosi {broj_trojki}')
print(f'Broj Petica iznosi {broj_trojki}')

print(rijec_lista)
r=rijec_lista.count('r')
print(f'Slovo r se pojavljuje {r} puta')

#Na ocjene učenika dodajemo još a) jednu ocjenu b)tri ocjene
print(ocjene_ucenika)
ocjene_ucenika.append(5)
print(f'Nakon append: {ocjene_ucenika}')

nove_ocjene=[5,3,4]
ocjene_ucenika.extend(nove_ocjene)
print(f'Nakon extend: {ocjene_ucenika}')

print(brojevi)
print(f'Indeks člana 11 iz liste brjevi je {brojevi.index(11)}')
brojevi.extend([11, 11])
print(brojevi)

print(f'Indeks prvog člana 11 iz liste brjevi je {brojevi.index(11)}')

brojevi.pop(10)
print(brojevi)

#Sortiranje članova liste

brojevi_obrnuto=brojevi.reverse()
print(brojevi)
print(brojevi_obrnuto)

#brojevi.sort()
brojevi_sortirano=sorted(brojevi)
print(f'Original lista brojevi: {brojevi}')
print(f'Sortirana lista brojevi: {brojevi_sortirano}')


print(brojevi)
for element in reversed(brojevi):
    print(element, end=' ')

brojevi_sortirano.reverse()
print(f'Reversana lista sortiranih brojeva (od najveće prema manoj: {brojevi_sortirano}')

print(brojevi)
brojevi.insert(3,4)
print(brojevi)
brojevi.insert(7, 'A'
print(brojevi))