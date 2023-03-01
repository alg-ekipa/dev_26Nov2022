#IDENTITY MANAGEMENT
#PRIJAVA U SUSTAV (LOGIN)
#BAZA: rječnik
#{'UserName' : ['ime', 'prezime', 'lozinka']}, lozinka min 10

#ADMIN                   KORISNIK
#1. dodavanje            1. pregled
#2. ažuriranje           2. odjava
#3. brisanje             
#4. pregled
#5. odjava

korisnici = {
    'admin': ['Stevo','Stević', '5555555555'],
    'đurđa': ['Đurđa', 'Đurđić', '3333333333'],
}

def dodavanje_korisnika(): #1#
    Korisničko_Ime = input ('\nUnesi Korisničko Ime novog Korisnika: ')
    while len (Korisničko_Ime) <3:
        Korisničko_Ime = input('Korisničko Ime je kraće od 3 znaka, pokušajte ponovo: ')
    while Korisničko_Ime in korisnici:
        Korisničko_Ime = input ('\n\nKorisničko Ime već postoji, pokušajte ponovo: ')
    Ime = input ('Unesi Ime novog Korisnika: ')
    while len (Ime) <3:
        Ime = input('Ime je kraće od 3 znaka, pokušajte ponovo: ')
    Prezime = input ('Unesi Prezime novog Korisnika: ')
    while len (Prezime) <3:
        Prezime = input('Prezime je kraće od 3 znaka, pokušajte ponovo: ')
    Zaporka = input ('Unesi Zaporku novog Korisnika (minimalno 10 znakova): ')
    while len (Zaporka) <10:
        Zaporka = input('Zaporka je kraća od 10 znakova, pokušajte ponovo: ')
    korisnici [Korisničko_Ime] = [Ime, Prezime, Zaporka]
    #print (korisnici)
    print('\nDodavanje korisnika uspješno odrađeno!\n\nVraćamo se na početni izbornik.')
    
def ažuriranje_korisnika(): #2#
    Ažuriranje_Ime = input('\nUnesi Korisničko Ime za ažuriranje: ')
    while Ažuriranje_Ime not in korisnici:
        Ažuriranje_Ime = input ('\nKorisničko ime ne postoji, pokušajte ponovo: ')
    odgovor = input ('\nUnesi broj željene akcije ažuriranja:\n1. imena\n2. prezimena\n3. zaporke \n\nOdabir: ')
    while not odgovor.isdigit() or int (odgovor) not in [1, 2, 3]:
        odgovor = input ('\nNije unesen ispravan broj, pokušajte ponovo: ')
    odgovor = int (odgovor)    
    if odgovor == 1:
        Ažuiranje_Imena = input('Unesi novo Korisničko Ime: ')
        while len(Ažuiranje_Imena) < 3:
            Ažuiranje_Imena = input('Ime je kraće od 3 znaka, pokušajte ponovo: ')
        korisnici[Ažuriranje_Ime][0]=Ažuiranje_Imena
    elif odgovor == 2:
        Ažuriranje_Prezimena = input('\nUnesi novo Prezime: ')
        while len (Ažuriranje_Prezimena) < 3:
            Ažuriranje_Prezimena = input('\nPrezime je kraće od 3 znaka, pokušajte ponovo: ')
        korisnici[Ažuriranje_Ime][1]=Ažuriranje_Prezimena
    elif odgovor == 3:
        Ažuriranje_Zaporke = input('\nUnesi novu Zaporku (minimalno 10 znakova): ')
        while len (Ažuriranje_Zaporke) <10:
            Ažuriranje_Zaporke = input('\nUnešena zaporka je manja od 10 znakova, pokušajte ponovo: ')
        korisnici[Ažuriranje_Ime][2] = Ažuriranje_Zaporke
    #print (korisnici)
    print('\nAžuriranje korisnika uspješno odrađeno!\n\nVraćamo se na početni izbornik.')
prikaz_izbornika()
    '''def brisanje_korisnika(): #3#
    ulaz = 1
        while ulaz:
        Brisanje_Imena = input ('\nUnesi Korisničko Ime korisnika za brisanje: ')
        if Brisanje_Imena in korisnici.keys():
            while True:
                Brisanje_Imena = input ('\nUnesi Korisničko Ime korisnika za brisanje: ')
                if Brisanje_Imena == korisnici.keys():
                    Brisanje_Imena = korisnici.pop(Brisanje_Imena)
                    print(korisnici)
                else:
                    Brisanje_Imena = input ('\nUnijeli ste nepostojeće Korisničko ime, molimo ponoviti: ')    
            print('Uneseno Korisničko Ime ne postoji')
            
        else:
            brisanje_korisnika()
            ulaz = 0

def brisanje_korisnika(korisnici):
    korisnici = global
    while Brisanje_Korisnika in korisnici.keys()
        Brisanje_imena = korisnici.pop(Brisanje_Imena)
        print(korisnici)   
        print ('\nUnesi Korisničko Ime korisnika za brisanje: ')
    else:'''
         
def pregled_korisnici(): #4#
    for v in korisnici.values():
        print ('\n',v[0], v[1], v[2])
    print('\nPregled korisnika uspješno odrađen!\n\nVraćamo se na početni izbornik.')

def Login_Korisnika(Login_Ime):
    if Login_Ime in korisnici.keys():
        Login_Zaporka = input('Unesi Zaporku korisnika: ')
        if Login_Zaporka == korisnici[Login_Zaporka] [2]:
            print (f'Dobrodošli, {korisnici[Login_Ime] [0]} {korisnici[Login_Ime] [1]}')
        else:
            print ('Unesena pogrešna Zaporka')
    else:
        print ('Pogrešan unos Korisnika')

odgovor = 0
while odgovor not in [1, 2, 3, 4, 5]:
    odgovor = input ('\nPrikaz izbornika:\n1. dodavanje\n2. ažuriranje\n3. brisanje\n4. pregled\n5. odjava\n\nOdabir: ')
    if not odgovor.isdigit():
        print ('\nNiste unijeli broj, pokušajte ponovona glavnom izborniku!')
        odgovor = 0
    elif int (odgovor) not in [1, 2, 3, 4, 5]:
        print('\nNiste unijeli ispravan broj, pokušajte ponovo na glavnom izborniku!')
        odgovor = 0
    else:
        odgovor = int(odgovor)

if odgovor == 1:
    dodavanje_korisnika()
elif odgovor == 2:
    ažuriranje_korisnika()
elif odgovor == 3:
    brisanje_korisnika()
elif odgovor == 4:
    pregled_korisnici()
elif odgovor == 5:
    print ('\nOdjavljeni ste!')

#login_ime=input ('Unesi Korisničko Ime korisnika: ')
#Login_Korisnika(login_ime)