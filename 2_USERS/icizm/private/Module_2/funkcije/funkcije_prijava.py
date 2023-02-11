korisnici = {
    'iivic':['Ivan', 'Ivić', 'aei123'], #1. dio je key u zagradama value
    'pperic':['Petar', 'Perić', 'ou456'], 
    'admin':['Mara', 'Marić', 'rst567']
}

def pregled_korisnici(): 
    '''Funkcija koja ispisuje sve korisnike (ime i prezime) iz baze/riječnika'''
    for v in korisnici.values(): 
        print({v[0]}, {v[1]})



def tko_je_admin(): 
    '''Funkcija koja ispisuje ime i prezime administraora'''
    for k, v in korisnici.items(): #k za key i v za value
        if k == 'admin':
            print(f'Administrator je: {v[0]} {v[1]}')

tko_je_admin()

def dohvati_admin_pswd():
    '''Funkcija koja vraća administratorsku lozinku'''
    for k, v in korisnici.items():
        if k == 'admin':
            return v[2]
        
admin_pswd = dohvati_admin_pswd() #pwd spremljen u varijablu i možemo onda s njim što hoćemo
#print(admin_pswd)

#pregled_korisnici()
tko_je_admin()

#prvo se napišu funkcije pa se zovu na kraju

'''Napisati login korisnika i da se svako može ulogirati sa svojim passwordom i imenom'''

def logiranje(uneseni_username): 
    '''Funkcija za prijavo preko korisničkog imena i lozinke'''
    if uneseni_username in korisnici.keys(): 
        uneseni_password = input('Unesi lozinku: ')
        if uneseni_password == korisnici[uneseni_username][2]:
            print(f'Dobrodošli, {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}')
        else: 
            print('Pogrešna lozinka!')
    else: 
        print(f'Nepostojeće korisničko ime!')

def dodavanje_korisnika(): 
    '''Funkcija za dodavanje korisnika u riječnik putem tipkovnice'''
    k_ime = input('Unesite username: ')
    ime = input('Unesite Vaše ime: ')
    prezime = input('Unesite Vaše prezime: ')
    lozinka = input('Unesite lozinku: ')
    korisnici[k_ime] = [ime, prezime, lozinka]
    print(korisnici)
        
def brisanje(): 
    '''Funkcija za brisanje korisnika '''
    clan_brisi = input('Unesi username korisnika kojeg želite obrisati: ')
    clan_brisi = korisnici.pop(clan_brisi)
    print(korisnici)


'''
while 1: 
    odg = input('Želite li se prijaviti? da/ne')
    if odg == 'da': 
        unos_user = input('Unesi korisničko ime: ')
        logiranje(unos_user)
    else: 
        break'''

#dodavanje_korisnika()

#brisanje()


