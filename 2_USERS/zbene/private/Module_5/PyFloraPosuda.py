korisnici = {
    'bot' : ['Nisamja', 'Bot', '2705']
    }

def login(): #0#
    broj_pokušaja = 0
    print('\nPyFloraPosuda\n\n\n\tPrijava\n')
    while broj_pokušaja < 3:
        korisničko_ime = input ('Unesi korisničko ime (max 3 pokušaja): ')
        zaporka = input ('Unesi zaporku (max 3 pokušaja): ')
        if korisničko_ime in korisnici.keys() and korisnici[korisničko_ime] [2] == zaporka:
            print(f'\nDobrodošli, {korisnici[korisničko_ime] [0]} {korisnici[korisničko_ime] [1]}')
            return True
            break       
        else:
            broj_pokušaja +=1
            print ('\nNiste upisali dobro korisničko ime ili zaporku, pokušajte ponovo.\n')
    if broj_pokušaja == 3:
        print('\nTri neuspjela pokušaja prijave. Aplikacija nije dostupna anonimnim korisnicima!\n')
        return False
login()