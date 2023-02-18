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
    if len(šifra)<5:
        print('Unešena šifra je kraća od 5 znakova. Unesite novu šifru!')
    elif len(šifra)>10:
        print('Unešena šifra je duža od 10 znakova. Unesite novu šifru!')
    korisnici[username] = [ime, prezime, šifra]
    print(korisnici)

def prijava(uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_password = input('Unesi lozinku: ')
        if uneseni_password == korisnici[uneseni_username][2]:
            print(f'Dobrdošli, {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}')
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

#def odjava():
 #   break




while True:
    user = input('Unesite username: ')
    prijava(user)
    for k,v in korisnici.items():
        if k == 'admin':
            print('\nŠto želite napraviti: \n1.) Pregled \n2.) Dodavanje \n3.) Brisanje \n4.) Odjava')
        else:
            print('\nŠto želite napraviti: \n1.) Pregled \n2.) Odjava')