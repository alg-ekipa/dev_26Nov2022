korisnici = {
    'admin':['Filipa', 'Filipi', 'jasamadmin1'],
    'ttomic':['Tina', 'Tomić', 'tttttttttt'], 
    'pperic':['Petar', 'Perić', 'pppppppppp'], 
    'mmaric':['Mara', 'Marić', 'mmmmmmmmmm']
}


def logiranje(uneseni_username): 
    if uneseni_username in korisnici.keys(): 
        uneseni_password = input('Unesi lozinku: ')
        if uneseni_password == korisnici[uneseni_username][2]:
            jesamliadmin()
            print(f'Dobrodošli, {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}')
        else: 
            print('Pogrešna lozinka!')
            logiranje(uneseni_username)
    else: 
        print(f'Nepostojeće korisničko ime!')



def dodavanje_korisnika(): 
    '''Funkcija za dodavanje korisnika u riječnik putem tipkovnice'''
    k_ime = input('Unesite username: ')
    ime = input('Unesite Vaše ime: ')
    prezime = input('Unesite Vaše prezime: ')
    lozinka = input('Unesite lozinku: ')
    korisnici[k_ime] = [ime, prezime, lozinka]
    
def brisanje(): 
    '''Funkcija za brisanje korisnika '''
    clan_brisi = input('Unesi username korisnika kojeg želite obrisati: ')
    clan_brisi = korisnici.pop(clan_brisi)
    print(korisnici)
    print()

def izbornik(): 
    odabir = input('Dobar dan! Odaberite jednu od sljedećih opcija: login | registracija  ')
    if odabir == 'login': 
        uneseni_username = input('Unesite svoje korisničko ime: ')
        logiranje(uneseni_username)
    if odabir == 'registracija': 
        dodavanje_korisnika()
    

def pregled_korisnici(): 
    '''Funkcija koja ispisuje sve korisnike (ime i prezime) iz baze/riječnika'''
    for v in korisnici.values(): 
        print({v[0]}, {v[1]})
    print()

def admin_izbornik():
    print(f'Odaberite broj administratorske opcije: \n\t 1) dodavanje  \n\t 2) brisanje \n\t 3) pregled \n\t 4) odjava')
    odabir_admin = input()
    if odabir_admin == '1': 
        dodavanje_korisnika()
        admin_izbornik()
    if odabir_admin == '2': 
        brisanje()
        admin_izbornik()
    if odabir_admin == '3': 
        pregled_korisnici()
        admin_izbornik()
    if odabir_admin == '4':
        izbornik()

        
    
def jesamliadmin(): 
    for k, v in korisnici.items(): 
        if k == 'admin':
            admin_izbornik()
            

izbornik()

'''while 1:
    odg = input ('Želite li se prijaviti? da/ne ')
    if odg== 'da':

        username=input('Unesi korisničko ime:')
        logiranje(username)
        
    else:
        break'''