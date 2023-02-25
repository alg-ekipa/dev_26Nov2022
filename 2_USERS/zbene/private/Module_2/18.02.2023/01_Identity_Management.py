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
    'admin': ['Stevo','Stević', '5555555555' ],
    'đurđa': ['Đurđa', 'Đurđić', '3333333333'],
}

def dodavanje_korisnika(): #1#
    Korisničko_Ime = input ('\nUnesi Korisničko Ime novog Korisnika: ')
    while len(Korisničko_Ime)<2:
        Korisničko_Ime = input('Korisničko Ime je manje od 2 znaka, pokušajte ponovo: ')
    Ime = input ('Unesi Ime novog Korisnika: ')
    while len(Ime)<2:
        Ime = input('Ime je manje od 2 znaka, pokušajte ponovo: ')
    Prezime = input ('Unesi Prezime novog Korisnika: ')
    while len(Prezime)<2:
        Prezime = input('Prezime je manje od 2 znaka, pokušajte ponovo: ')
    Zaporka = input ('Unesi Zaporku novog Korisnika (minimalno 10 znakova): ')
    while len(Zaporka)<10:
        Zaporka = input('Zaporka je manja od 10 znakova, pokušajte ponovo: ')
    korisnici [Korisničko_Ime] = [Ime, Prezime, Zaporka]
    print (korisnici)

#def ažuriranje_korisnika(): #2#

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
            ulaz = 0'''

def brisanje_korisnika(korisnici):
    korisnici = global
    while Brisanje_Korisnika in korisnici.keys()
        Brisanje_imena = korisnici.pop(Brisanje_Imena)
        print(korisnici)   
        print ('\nUnesi Korisničko Ime korisnika za brisanje: ')
    else:'''
    
    

def pregled_korisnici(): #4#
    for v in korisnici.values():
        print ('\n',v[0], v[1])

def Login_Korisnika(Login_Ime):
    if Login_Ime in korisnici.keys():
        Login_Zaporka = input('Unesi Zaporku korisnika: ')
        if Login_Zaporka == korisnici[Login_Zaporka] [2]:
            print (f'Dobrodošli, {korisnici[Login_Ime] [0]} {korisnici[Login_Ime] [1]}')
        else:
            print ('Unesena pogrešna Zaporka')
    else:
        print ('Pogrešan unos Korisnika')

while True:
    odgovor = int(input ('\nPrikaz izbornika:\n1. dodavanje\n2. ažuriranje\n3. brisanje\n4. pregled\n5. odjava\n\nOdabir: '))
    if odgovor == 1:
        dodavanje_korisnika()
    elif odgovor == 3:
        brisanje_korisnika()
    elif odgovor == 4:
        pregled_korisnici()
    elif odgovor == 5:
        print('Odjavljeni ste!')
        break
    else:
        print ('Niste odabrali ispravan broj, pokušajte ponovo: ')

    
#login_ime=input ('Unesi Korisničko Ime korisnika: ')
#Login_Korisnika(login_ime)