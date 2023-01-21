neka_rijec=list("Automatizacija")
print(neka_rijec)

duljina=len(neka_rijec)
#print(duljina)

#prolaz preko indexa
for i in range(duljina):
    print(neka_rijec[i], end=" ")
print()

#prolaz kroz listu direktno preko člana
for slovo in neka_rijec:
    print(slovo, end=" ")
print()

lista_unos=[]
broj_clanova=5
for i in range(broj_clanova):
    ocjena=int(input("Unesi ocjenu učenika: "))
    lista_unos.append(ocjena)
print()
print(lista_unos)