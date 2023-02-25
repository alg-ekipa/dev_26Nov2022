'''jednostavni riječnik 

naziv_rijecnika = {
    kljuc : vrijednost,
    kljuc : vrijednost,
    kljuc : vrijednost
}


'''


ljudi = {
    1 : 'Mario',
    2 : 'Ivana',
    3 : 'Nikola'
}

'''dohvacanje vrijednosti'''

print(ljudi[1])
print(ljudi[2])
print(ljudi[3])

print()

stanovnistvo = {
    '12345678901': 'Petar Parić',
    '52845628415': 'Marko Marić',
    '12548564851': 'Ana Anić',
    '96585214587': 'Martina Martinić'

}

print(stanovnistvo)
print()
print(stanovnistvo.items()) # ispisuje cijeli rijecnik
print(stanovnistvo.keys()) # ispisuje samo kljuceve rijecnika u Listi
print(stanovnistvo.values()) # ispisuje samo vrijednosti u Listi

n_torka = (4, 7, 2, 5, 0) # ne moze se mjenjati nTorka, mora se nova napraviti, ograćuje se sa ()
lista = [4, 7, 2, 5, 0]

print(n_torka[2])
print(lista[2])

lista[2]=8

print(n_torka[2])
print(lista[2])
