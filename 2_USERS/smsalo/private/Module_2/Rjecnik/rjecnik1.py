ljudi={
    1 : 'Mario',
    2 : 'Ivana',
    3 : 'Nikola'
}
#dohvat pojedinačnih vrijednosti preko ključeva
prvi = ljudi[1]
drugi = ljudi[2]
treci = ljudi[3]

print(prvi)
print(drugi)
print(treci)
print()

#ključ kao string (može biti i broj i n_torka)
stanovnistvo = {
    '12345678901' : 'Petar Perić',
    '23456789012' : 'Ana Anica',
    '34567890123' : 'Iva Ivic',
    '45678901234' : 'Filip Fili',
    '56789012345' : 'Anja Anton'
}

#ispis rječnika
print(stanovnistvo)

#ispis rječnika kao lista parova ključ-vrijednost (n_terce)
print(stanovnistvo.items())
print()

#ispis samo ključeva u obliku liste
print(stanovnistvo.keys())
lista_kljuceva=stanovnistvo.keys()
print(lista_kljuceva)
print()

#ispis vrijednosti u obliku liste
print(stanovnistvo.values())

#liste se mogu mijenjati, n_torke(tupple) se ne mijenjaju
n_torka = (4, 7, 2, 0, 1)
lista=[4, 7, 2, 0, 1]
print(n_torka[2])
print(lista[2])
lista[2]=8
print(lista)