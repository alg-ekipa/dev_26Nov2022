korisnici= {
    'admin':['Ivan', 'Ivic', 'aei123'],
    'ppric' :['Petar', 'Peric', 'ou456'],
    'mmaric' :['Mara', 'Maric', 'rst567']
}

def pregled_korisnika():
    '''Funkcija koja ispisuje sve korisnike iz baze/riječnika'''
    for v in korisnici.values():
        print(v[0], v[1])

pregled_korisnika()
print()


# tko je administrator
def tko_je_admin():
    '''Funkcija koja ispisuje ime i prezime administratora'''
    for k,v in korisnici.items():
        if k=='admin':
            print(f'Administrator je {v[0]} {v[1]}.')

tko_je_admin()
print()

# dohvati administratorski pass
def dohvati_admin_pass():
    for k,v in korisnici.items():
        if k=='admin':
            return v[2]
admin_pass=dohvati_admin_pass()
print(admin_pass)
print()


#dodavanje novog korisnika
def novi_korisnik():
    #global korisnici
    korisnicko_ime=input('Unesi korisničko ime: ')
    while korisnicko_ime in korisnici.keys():
        print('Korisničko ime već postoji!')
        korisnicko_ime=input('Unesi korisničko ime: ')
    else:
        ime=input('Unesi ime: ')
        prezime=input('Unesi prezime: ')
        lozinka=input('Unesi lozinku: ')
        korisnici[korisnicko_ime] = [ime, prezime, lozinka]
        print(korisnici)
       
novi_korisnik()
print()

# brisanje korisnika

def brisanje():
    clan_brisi=input('Unesite username korisnika za obrisati:')
    clan_brisi=korisnici.pop(clan_brisi)
    print(korisnici)

brisanje()


# logiranje

def logiranje(uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_pass=input('Unesi lozinku: ')
        if uneseni_pass==korisnici[uneseni_username][2]:
            print(f'Dobro došli, {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}')
        else:
            print('Pogrešna lozinka!')
    else:
        print('Nepostojeće korisničko ime!')


while 1:
    odg=input('Želite li se prijaviti? da/ne: ')
    if odg=='da':
        unos_user=input('Unesi korisničko ime: ')
        logiranje(unos_user)
    else:
        break





