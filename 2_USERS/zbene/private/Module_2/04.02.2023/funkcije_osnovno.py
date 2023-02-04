#funkcija koja ne vraća ništa i nema argumenata
def pozdrav():
    print ('Dobar dan!')
    print ('Dobrodošli!')

pozdrav()
print()

#funkcija koja ne vraća ništa a ima ulazne parametre
def pozdrav1 (ime,prezime):
    print (f'Dobar dan, {ime} {prezime}!')
    print ('Dobrodošli!')

pozdrav1 ('Pero', 'Perić' )
print()

#funkcija koja vraća vrijednost (znakovni niz) i ima ulazni argument
def dohvati_pozdrav (ime):
    return f'Dobar dan, {ime}!'

poruka = dohvati_pozdrav('Kristina')
print (poruka)
print(dohvati_pozdrav ('Marko'))
print()

def povecaj (broj, za_koliko):
    '''zbroj = broj + za_koliko
    return zbroj'''
#ili
    return broj + za_koliko

print(povecaj(4,8))
print()
#ili
def povecaj (broj, za_koliko = 5):
    return broj + za_koliko

print (povecaj (18,10))