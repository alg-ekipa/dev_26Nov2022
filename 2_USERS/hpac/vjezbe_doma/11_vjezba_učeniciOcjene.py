#Unesi ocjene učenika, a zatim izračunaj prosjek

broj_ucenika = int(input('Unesi broj učenika: '))
lista_ocjena = []

for i in range(broj_ucenika):
    ocjena = int(input(f'Unesi ocjenu {i+1}. učenika: '))
    lista_ocjena.append(ocjena)

zbroj = sum(lista_ocjena)
prosjek = zbroj/broj_ucenika

print(f'Prosjek ocjena svih učenika je: {round(prosjek,2)}')

broj_jedinica = lista_ocjena.count(1)
broj_trojki = lista_ocjena.count(3)

print(f'Među učenicima trojku ima njih {broj_trojki}, a jedinice ima {broj_jedinica}')