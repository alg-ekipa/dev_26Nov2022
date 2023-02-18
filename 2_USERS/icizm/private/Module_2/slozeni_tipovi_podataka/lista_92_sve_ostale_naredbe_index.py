brojevi = [3, 6, 87, 98, 23, 56, 223, 1, 8]

#dohvat člana s određenim indeksom, zatražili smo indeks

print(brojevi)
print(f'Index člana 6 iz liste brojevi je: {brojevi.index(6)}')

brojevi.extend([6, 6])
print(brojevi)
print(f'Index prvog člana 6 iz liste brojevi je: {brojevi.index(6)}')

# brisanje člana s navedenim indeksom, brisanje pojedinačnog člana

brojevi.pop(10) 
print(brojevi)

print()

#sortiranje članov aliste

brojevi_obrnuto = brojevi.reverse() #obrnuti će red članova
print(brojevi)
print(brojevi_obrnuto)

