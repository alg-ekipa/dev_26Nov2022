#Funkcija koja ne vraća ništa i nema argumenata

def pozdrav(): 
    print('Dobar dan!')
    print('Dobro došli!')

pozdrav()
print()

#funkcija koja ne vraća ništa i ima ulazne parametre ili argumente

def pozdrav1(ime, prezime):
    print(f'Dobar dan, {ime} {prezime}!')
    print(f'Dobro došli!')

pozdrav1('Pero', 'Perić')
print()


#funkcija koja vraća vrijednost (znakovni niz) i ima ulazni argument

def dohvati_pozdrav(ime):
    return f'Dobar dan {ime}!'

poruka = dohvati_pozdrav('Kristina')
print(poruka)
print(dohvati_pozdrav('Marko')) #print možemo staviti vani da bi vidjeli dohvaćenu funkciju
print()

#funkcija koju možemo spremiti u string varijablu i kasnije manipulirati sa njom
'''
def povecaj(broj, za_koliko):
    # zbroj = broj + za_koliko
    # return zbroj
    return broj + za_koliko

print(povecaj(4, 8))
'''

def povecaj(broj, za_koliko=5): 
    ''' Funkcija koja povećava broj za neki iznos'''
    return broj + za_koliko

print(povecaj.__doc__) #ispis teksta iz Docstringa (opisa funkcije)
print(povecaj.__name__) #ispisuje imena funkcije 




#print(povecaj(18, 10))