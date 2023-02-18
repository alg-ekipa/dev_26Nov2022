#funkcija koja ne vraća ništa i nema argumenata

def pozdrav():
    print('Dobar dan!')
    print('Dobrodošli!')

pozdrav()
print()

#funkcija koja ne vraa ništa i ima ulazne parametre
def pozdrav1(ime, prezime):
    print(f'Dobar dan, {ime} {prezime}!')
    print('Dobrodošli!')

pozdrav1('Pero', 'Perić')


#funkcija koja vraća vrijednost(znakovni niz) i ima ulazni argument
def dohvati_pozdrav(ime):
    return f'Dobar dan, {ime}!'

poruka=dohvati_pozdrav('Kristina')
print(poruka)
print(dohvati_pozdrav('Marko'))

def povecaj(broj, za_koliko=5):
    '''Funkcija koja povećava broj za neki iznos'''
    zbroj=broj+za_koliko
    return zbroj

print(povecaj.__doc__) #ispis teksta iz Docstringa(opisa funkcije)
print(povecaj.__name__) #ispis imena funkcije

#print(povecaj(18, 10))
