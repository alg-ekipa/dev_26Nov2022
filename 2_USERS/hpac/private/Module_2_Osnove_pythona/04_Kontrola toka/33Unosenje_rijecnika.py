''' UNos s tipkovnicom kljuca i vrijednosti, unaprijed zadamo broj clanova (parova rijeci, vrijednosti) 
Unosimo 5 parova
'''

rijecnik ={}


# unos sa tipkovnice kljuca i vrijendosti
'''

br_parova = int(input('unesi broj parova: '))


for i in range(br_parova):
    kljuc= input('Unesi kljuc: ')
    vrijednost = input('Unesi vrijednsot: ')
    rijecnik[kljuc]=vrijednost

print(rijecnik)
'''

#punjenje rijecnika iz dvije liste
'''
rijecnik_iz_liste = {}

lista_kljuceva = [1, 2, 3, 4, 5]
lista_vrijednosti = ['c++', 'java', 'perl', 'cetvrti', 'zadnji']

for i in range(len(lista_kljuceva)):
    kljuc = lista_kljuceva[i]
    vrijednost = lista_vrijednosti[i]
    rijecnik[kljuc] = vrijednost


print(rijecnik)'''

#imamo listu kljuceva, vrijednosti unosimo

rijecnik_iz_liste = {}

lista_kljuceva = [1, 2, 3, 4, 5]

for i in range(len(lista_kljuceva)):
    kljuc = lista_kljuceva[i]
    vrijednost = input(f'Unesi vrijednsot pod kljuc: {kljuc} : ')
    rijecnik[kljuc] = vrijednost
    



print(rijecnik)