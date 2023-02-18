
rjecnik={}
'''
#unos sa tipkovnice i ključa i vrijednosti, unaprijed zadamo broj članova rječnika(parova-ključ vrijednost)-unosimo 5 parova

for i in range(5):
    kljuc=int(input('Unesi ključ: '))
    vrijednost=input('Unesi vrijednost: ')
    rjecnik[kljuc]=vrijednost

    print(rjecnik)

    for k, v in rjecnik.items():
        print(f'{k} : {v}')
 '''

 #punjenje rječnika iz 2 liste, jedna su ključevi a druga vrijednosti

rjecnik_iz_liste={}

lista_kljuceva=[1,2,3,4,5]
lista_vrijednosti=['python', 'c++', 'java', 'perl', 'asp.net']

for i in range(len(lista_kljuceva)):
    kljuc=lista_kljuceva[i]
    vrijednost=lista_vrijednosti[1]
    rjecnik_iz_liste[kljuc]=vrijednost

for k,v in rjecnik_iz_liste.items():
        print(f'{k} : {v}')
        print(rjecnik_iz_liste)

        #kombinacija:imamo listu ključeva a mi unosimo vrijednosti


