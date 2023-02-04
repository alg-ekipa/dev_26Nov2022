# Funkcija koja ne vraća ništa i nema argumenata
def pozdrav():
    print('Dobar dan!')
    print('Dobrodošli!')

pozdrav()
print()

# Funkcija koja ne vraća ništa i ima ulazne parametre/argumente
def pozdrav1(ime,prezime):
    print(f'Dobar dan, {ime} {prezime}!')
    print('Dobrodošli!')

pozdrav1('Pero','Perić')
print()

# Funkcija koja vraća vrijednost (znakovni niz) i ima ulazni argument
# Kada imam RETURN onda sa tom varijablom kasnije možeš raditi, a ako imaš samo PRINT onda ga samo ispisuje
def dohvati_pozdrav(ime):
    return f'Dobar dan, {ime}'

print(dohvati_pozdrav('Marko'))
print()

poruka = dohvati_pozdrav('Kristina')
print(poruka)
print()


def povecaj(broj, za_koliko):
    zbroj = broj + za_koliko
    return zbroj

print(povecaj(4, 8))
print

def povecaj(broj, za_koliko):
    return broj + za_koliko

print(povecaj(4, 8))
print

def povecaj(broj, za_koliko=5):
    return broj + za_koliko

print(povecaj(18)) #ako se stavi argument, onda je on veće važnosti, pa će njega uzeti a zanemariti što piše kod funkcije (+5)
print()