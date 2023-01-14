
ocjene_ucenika = [1,5,2,3,1,2,3,5,2,1,2,3,2,1,5,]

lista_a = [323, 'probni_tekst', 'jos nesto teksta', 3.14, True, 'Pa opet tekst']

brojevi = [321, 123, 45, 7854, 124, 65784, 32,221, 542, 855]

rijec = 'programiranje'
rijec_lista = list(rijec)

'''brisanje, ciscenje liste'''
print(lista_a)
lista_a.clear()
print(lista_a)

'''kopiranje liste'''
brojevi_kopija = brojevi.copy()
print(brojevi)
print(brojevi_kopija)

'''brojanje ocjena'''
broj_trojki=ocjene_ucenika.count(3)
print(f'Broj trojki {broj_trojki}')
broj_petica=ocjene_ucenika.count(5)
print(f'broj petica {broj_petica} ')

'''brojanje stringova'''
r = rijec_lista.count('r')
print(f'slovo R u {rijec} se nalazi {r} puta' )

''''dodavanje jos jedne ocjene u listu'''

print(ocjene_ucenika)
ocjene_ucenika.append(5)
print(ocjene_ucenika)

print ()
''''dodavanje jos jedne 3 ocjene u listu'''

nove_ocjene= [3,2,5]
ocjene_ucenika.extend(nove_ocjene)
print(ocjene_ucenika)

print ('izbacivanje broja')
'''izbacivanje broja, ako znamo index'''

print(brojevi)
brojevi.pop(5)
print(brojevi)

print ('sortiranje')
'''sortiranje bojeva'''
'''
brojevi_reverse=reversed(brojevi) # okrece indexe unazad, ali ne radi
'''
print(brojevi)
brojevi.reverse()
print(brojevi)


print ('od najmanjeg prema najvecem')

print(brojevi)
brojevi_sortirano= sorted(brojevi)
brojevi_sortirano.sort()  #sortiranje brojeva od vecega prema manjem
print(brojevi_sortirano)

print('ubacivanje broja ')
'''ubacivanje broja'''
print(brojevi)
brojevi.insert(5,0)  # (index gdje ubacujem, šta ubacujem)
print(brojevi)