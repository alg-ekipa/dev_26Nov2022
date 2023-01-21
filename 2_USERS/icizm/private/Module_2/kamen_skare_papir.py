'''
Napravite program koji će vam omogućiti igranje protiv računala
'''
import random

akcije = ['kamen','škare', 'papir']
kompjuter = random.choice(akcije)


while True:
    korisnik = input('Odaberi između kamen, škare, papir: ')
    if korisnik in akcije: 
        print(f'Odabrali ste {korisnik}, a kompjuter {kompjuter}')
        if korisnik == kompjuter: 
            print('Neriješeno!')
        elif korisnik == 'kamen' and kompjuter == 'škare': 
            print('Pobijedili ste! :) ')
        elif korisnik == 'kamen' and kompjuter == 'papir':
            print('Izgubili ste! :( ')
        elif korisnik == 'škare' and kompjuter == 'kamen':
            print('Izgubili ste! :( ')
        elif korisnik == 'škare' and kompjuter == 'papir': 
            print('Pobijedili ste! :) ')
        elif korisnik == 'papir' and kompjuter == 'kamen': 
            print('Pobijedili ste! :) ')
        elif korisnik == 'papir' and kompjuter == 'škare':
            print('Izgubili ste! :( ')
    kraj = input('Želite li ponovnoigrati? Odaberite da ili ne  ')
    if kraj == 'ne':
        break     

