rjecnik = {}

#unos korisnika ključa i vrijednosti, unaprijed zadamo broj članova rječnika (parova ključ - vrijednost) - 5 parova
'''
for i in range(5):
    kljuc = int(input('Unesi ključ: '))
    vrijednost = input ('Unesi vrijednost: ')
    rjecnik[kljuc] = vrijednost
print(rjecnik)

for k, v in rjecnik.items():
    print(f'{k} : {v}')

'''

# punjenje rječnika iz dvije liste - 1 ključevi, 2 - vrijednosti

rjecnik_iz_liste = {}

lista_kljuceva = [1, 2, 3, 4, 5]
lista_vrijednosti = ['python', 'C++', 'java', 'perl', 'asp.net']

for i in range(len(lista_kljuceva)):
    kljuc = lista_kljuceva[i]
    vrijednost = lista_vrijednosti[i]
    rjecnik_iz_liste[kljuc] = vrijednost

for k, v in rjecnik_iz_liste.items():
    print(f'{k} : {v}')

#imamo listu ključeva, unosimo vrijednosti
rjecnik_imena = {}
redni_br_kljuca = [1, 2, 3, 4, 5]

for i in range(len(redni_br_kljuca)):
    ime=input('Unesi ime ')
    rjecnik_imena[i] = ime
print(rjecnik_imena)

