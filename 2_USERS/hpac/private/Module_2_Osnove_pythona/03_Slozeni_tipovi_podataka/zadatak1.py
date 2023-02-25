#Unesi ocjene učlenika a zatim izračunaj prosjek. nije poznat broj učenika, pa unesi ocjene na početku

lista_ocjene = []
broj_ucenika = int(input('Unesi broj učenika:'))

for i in range(broj_ucenika):
    ocjena = int(input(f'Unesi ocjenu {i+1}. učenika:'))
    lista_ocjene.append(ocjena)

zbroj = sum(lista_ocjene)
prosjek = zbroj/broj_ucenika
print(f'Prosjek ocjena ovih učenika iznosi: {round(prosjek,1)}')


#za prethodni napravi ispis da se vidi koliko ih ima ocjenu 5 a koliko ocjenu 1

broj_jedinica = lista_ocjene.count(1)
broj_petica = lista_ocjene.count(5)

print(f'Među ovim učenicima njih {broj_petica} ima ocjenu 5, a {broj_jedinica} učenika ima ocjenu 1')


