ljudi={
    14356:'Mario',
    24333:'Ivana',
    34232:'Nikola'
}

#dohvat pojedinačnih vrijednosti kod ključa
prvi=ljudi[14356]
drugi=ljudi[24333]
treći=ljudi[34232]

print(prvi)
print(drugi)
print(treći)

print()

#ključ kao string
stanovništvo={
    '12345678901':'Petar Perić',
    '43435211900':'Marko Marić',
    '5456677662':'Ana Anić',
    '55555599900':'Martina M'
}
#ispis rječnika
print(stanovništvo)

#ispis rječnika-vraća lisu parova ključ-vrijednost(n-terce)
print(stanovništvo.items())
print()
#ispis samo ključeva u obliku liste
print(stanovništvo.keys())
print()
lista_ključeva=stanovništvo.keys()
print(lista_ključeva)

#ispis samo vrijednosti u obliku liste
print(stanovništvo.values())
'''
#n-terac ili tuple-razlika od liste
n_torka=(4,7,2,0,1)
lista=[4,7,2,0,1]

print(n_torka[2])
print(lista[2])
lista[2]=8
print(lista)
n_torka[2]=8

'''