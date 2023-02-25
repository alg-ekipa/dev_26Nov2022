import os

trenutni_korisnik = "nitko"

korisnici = {
    'admin':['Ivan', 'Ivic', '12345'],
    'pperic':['Petar', 'Peric', '23456'],
    'mmaric':['Mara','Maric','23456'],
}

def pregled_korisnika():
    for v in korisnici.values():
        print(f"Ime: {v[0]}, Prezime: {v[1]}")
#pregled_korisnika()

def admin():
    for k, v in korisnici.items():
        if(k == "admin"):
            print(f"{v[0]} {v[1]} je admin.")
#admin()

def novi_korisnik():
    username = input("Unesite username novog korisnika: \n")
    ime = input("Unesite ime novog korisnika.")
    prezime = input("Unesite prezime novog korisnika.")
    password = input("Unesite lozinku novog korisnika, mora imati min 5 znakova.")
    if len(password) < 5:
        password = input("Lozinka mora imati 5 znakova.")
    baza = [ime, prezime, password]
    korisnici.update({username: baza})
    print("Uspješno ste dodali novog korisnika.")
# novi_korisnik()

def dohvati_admin_password():
    for k, v in korisnici.items():
        if k == "admin":
            return v[2]

def logiranje(uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_password  = input("Unesi lozinku.")
        if uneseni_password == korisnici[uneseni_username][2]:
            print("_________________________________________________")
            print(f"Dobrodošli {korisnici[uneseni_username[0]]} {korisnici[uneseni_username][1]}.")
            print("__________________________________________________")
            return uneseni_username
        else:
            print("Pogrešna lozinka")
            return "nitko"
    else:
        print("Nepostojeće korisničko ime.")
        return "nitko"


def izbornik(trenutni_korisnik):
    print()
    print("----------IZBORNIK-----------")
    print()
    print("Odabrite opciju:\n1. Pregled korisnika\n2. Dodavanje novog korisnika\n3. Logiranje u sustav\n4.Izlaz")
    izbor = (input("----> "))
    izbor = int(izbor)
    if izbor == 1:
        if trenutni_korisnik == 'nitko':
            username=input('Unesi korisničko ime:')
            trenutni_korisnik=logiranje(username)
            return trenutni_korisnik
        else:
            pregled_korisnika()
    elif izbor == 2:
        novi_korisnik()
    elif izbor == 3:
        username = input("Unesi korisničko ime: ")
        logiranje(username)
    elif izbor == 4:
        quit()
    else:
        print("Pogrešan unos.")

while True:
    trenutni_korisnik = izbornik(trenutni_korisnik)
    if False == trenutni_korisnik:
        break