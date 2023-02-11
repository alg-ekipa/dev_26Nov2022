korisnici = {
    'admin':['Ivan','Ivic','aei123'],
    'pperic':['Petar','Peric','ou456'],
    'mmaric':['Mara','Maric','rst567']
}

def pregled_korisnici():
    '''Funkcija koja ispisuje sve korisnike (ime i prezime) iz baze/rječnika'''
    for v in korisnici.values():
        print(v[0], v[1])

#pregled_korisnici()
#print()

def tko_je_admin():
    '''Funkcija koja ispisuje ime i prezime admonistratora'''
    for k,v in korisnici.items():
        if k == 'admin':
            print(f'Administrator je {v[0]} {v[1]}')

#tko_je_admin()
#print()

def dohvati_admin_pswd():
    '''Funkcija koja dohvaća šifru administratora'''
    for k,v in korisnici.items():
        if k == 'admin':
            return v[2]

admin_pswd = dohvati_admin_pswd()
#print(admin_pswd)

def logiranje(uneseni_username):
    '''Funkcija za logiranje preko korisničkog imena i šifre'''
    if uneseni_username in korisnici.keys():
        uneseni_password = input('Unesi lozinku: ')
        if uneseni_password == korisnici[uneseni_username][2]:
            print(f'Dobrdošli, {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}')
        else:
            print('Pogrešna lozinka!')
    else:
        print(f'Nepostojeće korisničko ime!')

def dodavanje_korsnika():
    '''Funkcija za dodavanje članova u rječnik'''
    #global korisnici
    korisnicko_ime = input('Unesi korisnicko ime: ')
    ime = input('Unesi ime: ')
    prezime = input('Unesi prezime: ')
    lozinka = input('Unesi lozinku: ')
    korisnici[korisnicko_ime] = [ime, prezime, lozinka]
    print(korisnici)

def brisanje():
    '''Funkcija za brisanje člana preko username-a'''
    brisanje_ime = input('Unesi korisničko ime koje želiš obrisati: ')
    brisanje_ime = korisnici.pop(brisanje_ime)
    print(korisnici)

brisanje()

#dodavanje_korsnika()


'''
while 1:
    odg = input('Želite li provjeriti? da/ne - ')
    if odg == 'da':
        unos_user = input('Unesi korisničko ime: ')
        logiranje(unos_user)
    else:
        break
    '''