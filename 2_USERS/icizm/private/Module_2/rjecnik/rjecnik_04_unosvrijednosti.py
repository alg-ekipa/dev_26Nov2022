rjecnik = {}

# unos sa tipkovnice - ključa i vrijednosti, unaprijed zadamo broj članova riječnika (5 parova k - v)

'''for i in range(5):
    kljuc = input('Unesi ključ: ')
    vrijednost = input('Unesi vrijednost: ')
    rjecnik[kljuc] = vrijednost

    print(rjecnik)

for k, v in rjecnik.items():
    print(f'{k} : {v}')
''' 

# Punjenje riječnika iz dvije liste - 1. ključevi i 2. vrijednosti

'''
rijecnik_iz_liste = {}

lista_kljuceva = [1, 2, 3, 4, 5]
lista_vrijednosti = ['Python', 'C++', 'Java', 'Perl', 'asp.net']

for i in range(len(lista_kljuceva)):
    kljuc = lista_kljuceva[i]
    vrijednost = lista_vrijednosti[i]
    rijecnik_iz_liste[kljuc] = vrijednost

for k, v in rijecnik_iz_liste.items():
    print(f'{k} : {v}')

print(rijecnik_iz_liste)
'''

#kombinacija: imamo listu ključeva a mi unosimo vrijednosti

rijecnik_iz_unosa = {}

lista_kljuceva = [1, 2, 3, 4, 5]

for i in range(len(lista_kljuceva)):
    kljuc = lista_kljuceva[i]
    vrijednost = input('Unesi vrijednost: ')
    rijecnik_iz_unosa[kljuc] = vrijednost

for k, v in rijecnik_iz_unosa.items():
    print(f'{k} : {v}')

print(rijecnik_iz_unosa)