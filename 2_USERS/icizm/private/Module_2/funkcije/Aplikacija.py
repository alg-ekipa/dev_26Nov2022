korisnici = {'korisnik1': {'ime':'Petar', 'prezime':'Petrović', 'lozinka':'1234567', 'stanje': 12345}}
#print(korisnici['korisnik1'])

def izbornik():
    odabir = input('Dobar dan! Odaberite jednu od sljedećih opcija: \n\t 1) login \n\t 2) otvaranje računa  ')
    if odabir == '1': 
        uneseni_username = input('Unesite svoje korisničko ime: ')
        logiranje(uneseni_username)
    if odabir == '2': 
        dodavanje_korisnika()

def logiranje(uneseni_username): 
    if uneseni_username in korisnici.keys(): 
        uneseni_password = input('Unesi lozinku: ')
        if uneseni_password == korisnici[uneseni_username]['lozinka']:
            print(f"Dobrodošli, {korisnici[uneseni_username]['ime']} {korisnici[uneseni_username]['prezime']}")
        else: 
            print('Pogrešna lozinka!')
            logiranje(uneseni_username)
    else: 
        print(f'Nepostojeće korisničko ime!')

def dodavanje_korisnika(): 
    k_ime = input('Unesite username: ')
    ime = input('Unesite Vaše ime: ')
    prezime = input('Unesite Vaše prezime: ')
    lozinka = input('Unesite lozinku: ')
    korisnici[k_ime] = {'ime': ime, 'prezime': prezime, 'lozinka': lozinka, 'stanje': 0}

izbornik()
print(korisnici)