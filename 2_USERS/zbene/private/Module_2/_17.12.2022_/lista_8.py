neka_rijec = list('Automatizacija')
#print(neka_rijec)

duljina = len(neka_rijec)
#print(duljina)

#Prolaz kroz listu preko indeksa
for i in range (duljina):
    print(neka_rijec[i], end=' ')

print()

#Prolaz kroz listu direktno preko člana
for slovo in neka_rijec:
    print(slovo, end=' ')

print()
lista_unos = []
broj_clanova = 5

for i in range(broj_clanova):
    ocjena = int(input('Unesi ocjenu učenika: '))
    lista_unos.append(ocjena)
print(lista_unos)