neka_rijec=list('Automatizacija')
print(neka_rijec)

duljina=len(neka_rijec)
#print(duljina)

#Prolaz kroz listu prek indeksa
for i in range(duljina):
    print(neka_rijec[i], end=' ')

    print()
#prolaz kroz listu preko člana
    for slovo in neka_rijec:
        print(slovo, end=' ')


        lista_unos=[]
        broj_clanova=10

        for i in range(broj_clanova):
            ocjena=int(input('Unesi ocjenu učenika: '))
            lista_unos.append(ocjena)

        print(lista_unos)

        

