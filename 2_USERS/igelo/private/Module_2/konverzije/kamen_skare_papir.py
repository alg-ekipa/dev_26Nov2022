import random

akcije=['kamen', 'škare', 'papir']
kompjuter= random.choice(akcije)

igra=1
while igra:
    korisnik=input('Unesi izbor(kamen, škare, papir):')
    if korisnik in akcije:
        print(f'\nodabrali ste {korisnik}, a kompjuter {kompjuter}.\n')
        if korisnik== 'kamen' and kompjuter=='kamen':
            print('Nerješeno')
        elif korisnik== 'kamen' and kompjuter=='škare':
            print('Korisnik pobjeđuje')
        elif korisnik== 'kamen' and kompjuter=='papir':
            print('Kompjuter pobjeđuje')
        elif korisnik== 'škare' and kompjuter=='škare':
            print('Nerješeno')
        elif korisnik== 'škare' and kompjuter=='kamen':
            print('Kompjuter pobjeđuje')
        elif korisnik== 'škare' and kompjuter=='papir':
            print('Korisnik pobjeđuje')
        elif korisnik== 'papir' and kompjuter=='papir':
            print('Nerješeno')
        elif korisnik== 'papir' and kompjuter=='škare':
            print('Kompjuter pobjeđuje')
        elif korisnik== 'papir' and kompjuter=='kamen':
            print('Korisnik pobjeđuje')
