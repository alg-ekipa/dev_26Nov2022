korisnici = {
        'admin' : ['Ivan', 'Ivic', 'aei123'],
        'pperic' : ['Petar', 'Peric', 'ou456'],
        'mmaric' : ['Mara', 'Maric', 'rst567'],
}

def pregled_korisnici():
    '''Funkcija koja ispisuje sve korisnike (ime i prezime) iz baze/rječnika'''
    for v in korisnici.values():
        print (v[0], v[1])
    
def tko_je_admin():
    '''Funkcija koja ispisuje ime i prezime administratora'''
    for k,v in korisnici.items():
        if k == 'admin':
            print (f'Administrator je {v[0]} ({v[1]})')

def dohvati_admin_pswd():
    '''Funkcija koja vraća admin lozinku'''
    for k,v in korisnici.items():
        if k == 'admin':
            return v[2]

admin_pswd = dohvati_admin_pswd()
#print(admin_pswd)
#pregled_korisnici()
#tko_je_admin()

def logiranje (uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_password = input ('Unesi lozinku: ')
        if uneseni_password == korisnici[uneseni_username] [2]:
            print (f'Dobrodošli, {korisnici[uneseni_username] [0]} {korisnici[uneseni_username] [1]}')
        else:
            print('Pogrešna lozinka!')
    else:
        print(f'Nepostojeće korisničko ime')

#logiranje(unos_user)

def dodavanje_korisnika():
    '''Funkcija za dodavanje korisnika u rječnik, unos je preko tipkovnice'''
    korisn_ime = input('Unesi korisničko ime: ')
    ime = input ('Unesi ime: ')
    prezime = input ('Unesi prezime: ')
    lozinka = input ('Unesi lozinku: ')
    korisnici [korisn_ime] = [ime, prezime, lozinka]
    print(korisnici)

def brisanje():
    '''Funkcija za brisanje člana preko username-a'''
    clan_brisi = input ('Unesi username korisnika za brisanje: ')
    clan_brisi = korisnici.pop(clan_brisi)
    print(korisnici)
    
    

while 1:
    odg = input('Želite li se prijaviti? da/ne ')
    if odg == 'da':
        unos_user = input ('Unesi korisničko ime: ')
        logiranje(unos_user)
    else:
        break

#dodavanje_korisnika()

brisanje()