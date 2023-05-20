rjecnik = {}

# unos s tipkovnice i ključa i vrijednosti, unaprijed zadamo broj članova rječnika (parova ključ-vrijednost) - unosimo 5 parova
'''
for i in range (5):
    kljuc = int(input('Unesi ključ: '))
    vrijednost = input('Unesi vrijednost: ')
    rjecnik[kljuc] = vrijednost

print(rjecnik)

for k, v in rjecnik.items():
    print(f'{k} : {v}')
'''
# punjenje rječnika iz dvije liste - jedna su ključevi a druga vrijednosti
'''
rjecnik_iz_liste = {}

liste_kljuceva = [1,2,3,4,5]
lista_vrijednosti = ['python', 'c++0', 'java', 'perl', 'asp.net']

for i in range (len(liste_kljuceva)):
    kljuc = liste_kljuceva[i]
    vrijednost = lista_vrijednosti[i]
    rjecnik_iz_liste[kljuc]=[vrijednost]
for k, v in rjecnik_iz_liste.items():
    print(f'{k} : {v}')
print(rjecnik_iz_liste)
'''

#kombinacija: imamo listu ključeva a mi unosimo vrijednosti
rjecnikkk = {}
listaaa = [1,2,3]
vrijednostiii = input('Unesi vrijednost: ')

for i in range (len(listaaa)):
    kljuccc = listaaa[i]
    vrijednostiii = listaaa[i]
    rjecnikkk[kljuccc]=[vrijednostiii]
for k, v in rjecnikkk.items():
    print(f'{k} : {v}')
print(rjecnikkk)