korisnici = {
    'admin' : ['Ivan','Ivić','12345'],
    'jjuric' : ['Jure','Jurić','34567'],
    'pperic' :['Petar','Perić','98765'],
}

def novi_korisnik():
    username = input('Unesite USERNAME za novog korisnika: ')
    ime = input('Unesite IME novog korisnika: ')
    prezime = input('Unesite PREZIME novog korisnika: ')
    šifra = input('Unesite ŠIFRU za novog kornisika: ')
    while 5>len(šifra):
        šifra = input('Unesite ŠIFRU za novog kornisika: ')
    while len(šifra)>11:
        šifra = input('Unesite ŠIFRU 10 za novog kornisika: ')
    korisnici[username] = [ime, prezime, šifra]
    print(korisnici)

def prijava(uneseni_username):
    if uneseni_username in korisnici.keys():
        while True:
            uneseni_password = input('Unesi lozinku: ')
            if uneseni_password == korisnici[uneseni_username][2]:
                print(f'Dobrdošli, {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}')
                break
            else:
                print('Pogrešna lozinka!')               
    else:
        print(f'Nepostojeće korisničko ime!')
        print()
        
def pregled_korisnici():
    for v in korisnici.values():
        print(v[0], v[1])

def brisanje():
    brisanje_ime = input('Unesi korisničko ime koje želiš obrisati: ')
    brisanje_ime = korisnici.pop(brisanje_ime)
    print(korisnici)

def odjava():
    print('Hvala na korištenju')
    




while True:
    print()
    user = input('Unesite username: ')
    prijava(user)
    if user == 'admin':
        print('\nŠto želite napraviti: \n1.) Pregled \n2.) Dodavanje \n3.) Brisanje \n4.) Odjava')
        radnja1 = int(input('Unesite broj ispred željene radnje: '))
        if radnja1 == 1:
            pregled_korisnici()
            continue
        elif radnja1 == 2:
            novi_korisnik()
            continue
        elif radnja1 == 3:
            brisanje()
            continue
        elif radnja1 == 4:
            odjava()
            break
    elif user in korisnici.keys():
        print('\nŠto želite napraviti: \n1.) Pregled \n2.) Odjava')
        radnja1 = int(input('Unesite broj ispred željene radnje: '))
        if radnja1 == 1:
            pregled_korisnici()
        else:
            odjava()
            break
    else:
        print()