
""" rjecnik={}


# unos s tipkovnice i ključ i vrijednosti, unaprijed zadamo broj članova rječnika (parova ključ-vrijednost) - unosimo 5 parova

for i in range (5):
    kljuc=input ('Unesi ključ:')
    vrijednost = input ('Unesi vrijednost: ')
    rjecnik[kljuc] = vrijednost



print(rjecnik)



for k, v in rjecnik.items():
    print(f'{k} : {v}')

"""

#punjenje rječnika iz dvije liste - jedna su klučevi, a druga su vrijednosti

rjecnik_iz_liste = {}

lista_kljuceva = [1, 2, 3, 4, 5]
lista_vrijednosti = ['python', 'c++', 'java', 'perl', 'asp.net']

for i in range (len(lista_kljuceva)):
    kljuc=lista_kljuceva[i]
    vrijednost=lista_vrijednosti[i]
    rjecnik_iz_liste[kljuc]=vrijednost


for k, v in rjecnik_iz_liste.items():
    print(f'{k} : {v}')





# kombinacija: imamo listu ključeva, a mi unosimo vrijednosti


rjecnik_iz_liste2 = {}

lista_kljuceva = [1, 2, 3, 4, 5]
lista_vrijednosti = ['python', 'c++', 'java', 'perl', 'asp.net']

for i in range (len(lista_kljuceva)):
    kljuc=lista_kljuceva[i]
    print ('ključ---------------->', kljuc)
    vrijednost=input ('Unesi vrijednost-->')

    rjecnik_iz_liste2[kljuc]=vrijednost


for k, v in rjecnik_iz_liste.items():
    print(f'{k} : {v}')


for k, v in rjecnik_iz_liste2.items():
    print(f'{k} : {v}')