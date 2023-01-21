
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
"""

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

    """


#izračunajte prosječnu visinu svih učenika u rječniku
#napravite popis u kojem će se vidjeti samo redni broj i ime
#Ispišite broj učenika i učenica punom rečenicom

ucenici = {
    
1: ['Marko Marković', 'Uska 2', 'Zagreb', 'M', 1.68], 
2:['Pero Perić', 'Uska 4', 'Zagreb', 'M', 1.78],

3: ['Janko Jankić', 'Uska 2', 'Zagreb', 'M', 1.69], 
4:['Marko Perić', 'Uska 4', 'Zagreb', 'M', 1.73],

5: ['Marka Markić', 'Uska 18', 'Zagreb', 'Ž', 1.68], 
6:['Pero Perić', 'Široka 4', 'Zagreb', 'M', 1.78],


7: ['Marko Maršić', 'Široka 22', 'Zagreb', 'M', 1.98], 
8:['Pero Petrović', 'Široka 42', 'Zagreb', 'M', 1.48],


9: ['Marko Marušić', 'Uska 12', 'Zagreb', 'M', 1.58], 
10:['Janko Perić', 'Uska 34', 'Zagreb', 'M', 1.88],


}

for k, v in ucenici.items():
    print(f'{k} : {v}')

"""
for vrijednost in lista_vrijednosti: #iz svake liste vrijednosti uzimamo samo cijenu s indeksom 1

lista_visina=[]

for i in range 10:
    lista_visina=rjecnik.get(i)

"""





lista_rbr = []
for kljuc in ucenici.keys():
    lista_rbr.append(kljuc)
    #print(lista_rbr)

lista_imena=[]
for ime in ucenici.values():
    
    lista_imena.append(ime[0])
#print lista_imena

for i in range (len(lista_imena)):
    print(f'{lista_rbr[i]}, {lista_imena[i]}')



lista_spol=[]
for spol in ucenici.values():
    
    lista_spol.append(ime[-2])
#print lista_imena

for i in range (len(lista_imena)):
    print(f'{lista_rbr[i]}, {lista_spol[i]}')


broj_ucenika=10

broj_ucenika=lista_spol.count('M')
broj_ucenica=10-broj_ucenika
print ()
print (f'U razredu ima {broj_ucenika} učenika i {broj_ucenica} učenica.')