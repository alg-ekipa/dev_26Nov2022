nasa_lista = [154, "tekst", "još jedan tekst", 3.14, True,"pa opet tekst"]

print (nasa_lista)

print(f'prvi član naše liste je {nasa_lista[0]}, a četvrti član {nasa_lista[3]}')
umnozak=nasa_lista[1]
print(umnozak)

zadaci=[
    'Odabrati naziv liste',
    'Unijeti elemente liste',
    'pokrenuti aktivnosti',
]

print(zadaci)
print(zadaci[0])
print(zadaci[1])
print(zadaci[2])


for i in range(100,1,-5):
    print(i, end=" ")

print()
print()
zbroj=0
for i in range(1,21,1):
    zbroj=zbroj+i
    print(i, zbroj)
print ('zbroj brojeva 1 do', i , 'je jednak', zbroj )



print (nasa_lista)
nasa_lista_kopija=nasa_lista.copy()
nasa_lista.clear()
print (nasa_lista)


print (nasa_lista_kopija)
#tekst=input('upiši riječ koju tražiš:')
tekst=0
nasa_lista_kopija.append(tekst)
broj_ponavljanja=nasa_lista_kopija.count(tekst)
print(broj_ponavljanja)

ocjene_ucenika = [5,1,2,5,3,2,1,4,5,5]
print(len(ocjene_ucenika))
ocjene_ucenika.append(5)
print(len(ocjene_ucenika))

nove_ocjene=[5,3,4]

ocjene_ucenika.extend(nove_ocjene)
print(len(ocjene_ucenika))
print(ocjene_ucenika)

print()

print(ocjene_ucenika.index(5))#ako ima više članova onda vraća prvo pojavljivljanje elementa liste

brojevi=[1,2,3,4]
print(brojevi)

brojevi=[5,5,8,0,3,2]
print(brojevi)
brojevi.extend([1,2,3,4,5,6,7,8,9,10,11])
print(brojevi)
print(len(brojevi))
brojevi.pop(10)#brisanje člana s navedenim indeksom
print(brojevi)
print(len(brojevi))

#sortiranje članova liste


brojevi_sortirano=brojevi.sort()
print(brojevi)
print('sortirana lista')
print(brojevi_sortirano)
#brojevi_obrnuto=brojevi.reverse()
#for element in brojevi_obrnuto:
#    print(element, end=" ")

brojevi.insert(0,5000)
print(brojevi)


brojevi.insert(4,8000)
print(brojevi)


neka_rijec =list('automatizacija')
print(neka_rijec)
len(neka_rijec)
print(len(neka_rijec))

for i in range(14):
    print(neka_rijec[i], end= ' ')
print()
for slovo in neka_rijec:
    print(slovo, end='')