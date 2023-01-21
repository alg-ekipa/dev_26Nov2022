ljudi = {
    1:"Mario",
    2:"Ivana",
    3:"Nikola"
}
# Dohvat pojedinačnih vrijednosti preko ključeva
prvi = ljudi[1]
drugi = ljudi[2]
treci = ljudi[3]

print(ljudi[1])
print(prvi)

print(ljudi[2])
print(drugi)

print(ljudi[3])
print(treci)

#Ključ kao string
stanovnistvo = {
    '26032547357':'Petar Perić',
    '01234567891':'Marko Marić',
    '32158468962':'Ana Anić',
    '95468523574':'Martina Murić'
}

print()
print(stanovnistvo['26032547357'])
print()
#ispis riječnika
print(stanovnistvo)
print()
#ispis riječnika - vrača listu parova ključ vrijednost (n-terac)
print(stanovnistvo.items())
print()
#Issamo ključa u obliku liste
print(stanovnistvo.keys())

lista_kljuceva = stanovnistvo.keys()
print(lista_kljuceva)


print()

#Ispis samo vrijednosti u obliku liste
print(stanovnistvo.values())