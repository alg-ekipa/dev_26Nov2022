korisnici= {
    'admin':['Ana', 'Mihanović', 'aei123'],
    'ppric' :['Petar', 'Peric', 'our456'],
    'mmaric' :['Mara', 'Marić', 'rst567'],
    'kklob':['Karlo', 'Klobučar','klm456'],
    'asvob': ['Anđa', 'Svoboda', 'svb789']
}

def pregled_korisnika():
    for korisnik in korisnici.values():
        print(korisnik[0], korisnik[1])
    print()

def pregled_korisnika_admin():
    for i, j in korisnici.items():
        print(f'{i}:\t{j[0]} \t {j[1]} \t\t {j[2]}')
    print()

def novi_korisnik():
    korisnicko_ime=input('Unesi korisničko ime za novog korisnika: ')
    while korisnicko_ime in korisnici.keys():
        print('Korisničko ime već postoji!')
        korisnicko_ime=input('Unesi korisničko ime: ')
    else:
        ime=input('Unesi ime: ')
        prezime=input('Unesi prezime: ')
        lozinka=input('Unesi lozinku koja ima 6 znakova: ')
        while len(lozinka)!=6:
            lozinka=input('Unesena lozinka nema 6 znakova! Pokušajte ponovo: ')
        korisnici[korisnicko_ime] = [ime, prezime, lozinka]
        print('U bazi se sada nalaze sljedeći korisnici: ')
        pregled_korisnika_admin()
        print()
    
def brisanje():
    korisnik_brisi=input('Unesite username korisnika za obrisati:')
    if korisnik_brisi in korisnici.keys():
        korisnik_brisi=korisnici.pop(korisnik_brisi)
        print(f'U bazi se sada nalaze sljedeći korisnici: ')
        pregled_korisnika_admin()
        print()
    else:
        print('Uneseni korisnik ne postoji u bazi!')
        print()

def promjena():
    korisnik_izmjena=input('Unesite username korisnika za kojeg želite izmijeniti podatke: ')
    izmjena=int(input('Izaberite redni broj za izmjenu: \n 1. Ime \n 2. Prezime \n 3. Lozinka \n'))
    if izmjena==1:
        ime_novo=input('Unesite novo ime: ')
        korisnici[korisnik_izmjena][0]=ime_novo
    elif izmjena==2:
        prezime_novo=input('Unesite novo prezime:')
        korisnici[korisnik_izmjena][1]=prezime_novo
    elif izmjena==3:
        lozinka_novo=input('Unesite novu lozinku:')
        while len(lozinka_novo)!=6:
            lozinka_novo=input('Unesena lozinka nema 6 znakova! Pokušajte ponovo: ')
        korisnici[korisnik_izmjena][2]=lozinka_novo
    else:
        print('Niste izabrali promjenu!')
    print(f'Za korisnika s korisničkim imenom {korisnik_izmjena} u bazi se nalaze sljedeći podaci: \n Ime: {korisnici[korisnik_izmjena][0]} Prezime: {korisnici[korisnik_izmjena][1]} lozinka: {korisnici[korisnik_izmjena][2]}')
    print()

def logiranje(uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_pass=input('Unesi lozinku: ')
        while uneseni_pass!=korisnici[uneseni_username][2]:
            print('Pogrešna lozinka!')
            uneseni_pass=input('Unesi lozinku: ')
        else:
            print(f'Dobro došli, {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}')
    else:
        print('Nepostojeće korisničko ime!')
    print()

while 1:
    odg=input('Želite li se prijaviti? da/ne: ')
    if odg=='da':
        unos_user=input('Unesi korisničko ime: ')
        logiranje(unos_user)
        while True:
            if unos_user=='admin':
                izbornik=int(input
                ('Unesite redni broj za željenu radnju:\n 1. Pregled korisnika\n 2. Dodavanje novog korisnika \n 3. Brisanje postojećeg korisnika \n 4. Izmjena podataka postojećeg korisnika\n 5. Odjava \n'))
                if izbornik==1:
                    pregled_korisnika_admin()
                elif izbornik==2:
                    novi_korisnik()
                elif izbornik==3:
                    brisanje()
                elif izbornik==4:
                    promjena()
                else:
                    break
            else:
                izbornik=int(input('Unesite redni broj za željenu radnju:\n 1. Pregled korisnika\n 2. Odjava \n'))
                if izbornik==1:
                    pregled_korisnika()
                else:
                    break
    else:
        break
    



