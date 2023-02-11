import random

akcije = ['kamen', 'škare', 'papir']
kompjuter = random.choice(akcije)

igra=1
while igra:
    korisnik = input('Unesi izbor (kamen, škare, papir): ')
    if korisnik in akcije:
        print(f"\nodabrali ste {korisnik}, a kompjuter {kompjuter}.\n")
        if korisnik=='kamen' and kompjuter=='kamen':
            print('Neriješeno!')
        elif korisnik=='kamen' and kompjuter=='škare':
            print('Korisnik pobjeđuje!!')
        elif korisnik=='kamen' and kompjuter=='papir':
            print('Kopjuter pobjeđuje!!')
        elif korisnik=='škare' and kompjuter=='škare':
            print('Neriješeno!!')
        elif korisnik=='škare' and kompjuter=='kamen':
            print('Kompjuter pobjeđuje!!')    
        elif korisnik=='škare' and kompjuter=='papir':
            print('Korisnik pobjeđuje!!')
        elif korisnik=='papir' and kompjuter=='papir':
            print('Neriješeno!!')
        elif korisnik=='papir' and kompjuter=='kamen':
            print('Korisnik pobjeđuje!!')
        elif korisnik=='papir' and kompjuter=='škare':
            print('Kompjuter pobjeđuje!!')
        while True:
            game=str(input('Želite li igrati ponovo? Y/N: ')).lower()
            if game=='y':
                break
            elif game=='n':
                igra=0                                  #ovdje se mijenja stanje
                break
            else:
                print('krivi unos')
    else:
        print('Nemate dobar unos')
        continue
        
    
    
   





