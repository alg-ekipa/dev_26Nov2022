korisnici = {
    'admin': ['ivan', 'ivic', 'admin123'],
    'pperic' : ['petar', 'peric', 'pero123'],
    'hhanic' : ['hana', 'hanic', 'hana123']
}

def pregled_korisnika():
    '''funkcija koja ispisuje sve korisnike (ime i prezime )iz baze korisnika'''
    for v in korisnici.values():
        print(v[0], v[1])

#pregled_korisnika() #test fukcije

def tko_je_admin():
    '''funkcija koja ispisuje ime i prezime administratora'''

    for k,v in korisnici.items():
        if k == 'admin':
            print(f'Administrator je {v[0]} {v[1]}')

#tko_je_admin() #test fukcije

def dohvati_admin_pswd():
    '''funkcija za dohvacanje admin pssd-a'''
    
    for k,v in korisnici.items():
        if k == 'admin':
            return v[2]

#admin_pswd= dohvati_admin_pswd()   #test fukcije
#print(admin_pswd)                  #test fukcije

def login_uss_pass(uneseni_usn):
    ''' logiranje korisnika '''
    if uneseni_usn in korisnici.keys():
        uneseni_pswd = input('Unesi lozinku:\n')
        if uneseni_pswd == korisnici[uneseni_usn][2]:
            print(f'Dobrodosli,  {korisnici[uneseni_usn][0]} {korisnici[uneseni_usn][1]}')
        else:
            print('Pogresna lozinka')

    else:
        print('Pogresno korisnicko ime!')


#unos_korinsika = input('Unesi korisnicko ime:\n') #test fukcije
#login_uss_pass(unos_korinsika)                    #test fukcije


while 1:
    odg = input ('Želite li se prijaviti? ')
    if odg == 'da':
            unos_korinsika = input('Unesi korisnicko ime:\n')
            login_uss_pass(unos_korinsika)
    else:
        break