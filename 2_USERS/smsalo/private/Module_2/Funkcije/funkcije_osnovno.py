# funkcija koja ne vraća nista i nema argumenata

def pozdrav():
    print('Dobar dan!')
    print('Dobro došli!')

pozdrav()


# funkcija koja ne vraća nista i ima ulazne parametre

def pozdrav1(ime, prezime):
    print(f'Dobar dan, {ime} {prezime}!')
    print('Dobro došli!')

pozdrav1('Pero', 'Peric')

# funkcij koja vraća vrijednost i ima ulazni argument
def dohvati_pozdrav(ime):
    return f'Dobar dan, {ime}!'

poruka=dohvati_pozdrav('Kristina')
print(poruka)
print(dohvati_pozdrav('Marko')) #ono što je vratila funkcije moramo staviti u print ili ju ne vidimo


def povecaj(broj, za_koliko):
    return broj+za_koliko
   
print(povecaj(2,5))
print()

def povecaj_1(broj, za_koliko=5):
    return broj+za_koliko
   
print(povecaj_1(4))
print()

