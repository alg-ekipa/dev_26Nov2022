#Napišite program koji će u listu unositi ocjene učenika, a zatim izračunati njihov prosjek ocjena.Nije poznato unaprijed koliko učenika ima u razredu, pa se taj broj unosi na početku programa.
#Na kraju se ispisuje PROSJEK OCJEN AOVIH UČENIKA IZNOSI____

lista_ocjena=[]
broj_ucenika=5

for i in range(broj_ucenika):
    ocjena=int(input('Unesi ocjenu učenika: '))
    lista_ocjena.append(ocjena)

    zbroj