
broj_ucenika = int(input('Unesite koliko učenika ima u razredu:'))

lista_ocjena =[]

zbroj = 0

for i in range(broj_ucenika):
    ocjena = int(input('Unesi ocjenu učenika: '))
    lista_ocjena.append(ocjena)
    zbroj = zbroj + ocjena
    

prosjek = zbroj / broj_ucenika
print(f'Prosjek ocjena ovih učenika iznosi: {prosjek}')



    