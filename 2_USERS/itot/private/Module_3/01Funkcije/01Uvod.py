'''funkcija ne vraca nista i nema argumenata'''

def pozdrav():
    print('Dobar dan')
    print('dobrodosli')


pozdrav()

def pozdrav1(ime, prezime):
    print(f'dobar dan, {ime} {prezime}')
    print('dobrodosli 2')


pozdrav1('pero', 'peric')
print()


# funkcija koja vraca vrijednost

def dohvati_pozdrav(ime):
    return f'dobar dan, {ime}'


poruka = dohvati_pozdrav('Kristina')
print(poruka)