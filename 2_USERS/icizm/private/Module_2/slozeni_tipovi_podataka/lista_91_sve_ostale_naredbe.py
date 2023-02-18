ocjene_ucenika = [3, 4, 5, 5, 1, 4, 3, 5, 4, 2]
brojevi = [3, 6, 87, 98, 23, 56, 223, 1, 8]
rijec = 'programiranje'
rijec_lista = list(rijec)

print(f'Brojevi prije clear {brojevi}')
brojevi.clear() #očistili smo brojeve i sve promjene su sačuvane u toj listi
print(f'Brojevi nakon clear {brojevi}')

ocjene_ucenika_kopija = ocjene_ucenika.copy() #napravljena je kopiju u drugu listu, imamo dvije iste liste, imamo novu varijablu
print(ocjene_ucenika)
print(ocjene_ucenika_kopija)

#.count broji koliko puta se pojavila neka vrijednost

broj_trojki = ocjene_ucenika.count(3)
broj_petica = ocjene_ucenika.count(5)
print(f'Broj trojki: {broj_trojki}')
print(f'Broj petica: {broj_petica}')

print()

#brojanje stringova

r = rijec_lista.count('r')
print(f'Slovo r u riječi programiranje se pojavljuje {r} puta')

print()

#Na ocjene učenika dodajemo a) 1 ocjenu,  b) 3 ocjene

print(ocjene_ucenika)
ocjene_ucenika.append(5)   #Može se dodati jedna jedina stvar
print(f'Nakon append: {ocjene_ucenika}')

nove_ocjene  = [5, 3, 4]
ocjene_ucenika.extend(nove_ocjene) #dodajemo listu
print(f'Nakon extend: {ocjene_ucenika}')