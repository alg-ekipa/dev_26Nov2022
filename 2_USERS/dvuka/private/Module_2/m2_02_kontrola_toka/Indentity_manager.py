korisnici={
    'admin':['Danijel', 'Vukadin', '0123456789'],
    'lmessi':['Lionel', 'Messi', '5555555555'],
    'cronaldo':['Cristiano','Ronaldo','6666666666']

}


def pregled_korisnika():
    for korisnik in korisnici.values():
        print(korisnik[0], korisnik[1])

def novi_korisnik():
    username = input("Unesi novo korisnicko ime: ")
    ime = input("Unesi ime: ")
    prezime = input("Unesi prezime: ")
    password = input("Unesi password: ")
    while len(password) < 10:
        print("Password mora sazdržavati 10 znakova.")
        break
    korisnici[username] = ime, prezime, password   
    print(korisnici)
novi_korisnik()


def brisanje():
    clean = input("Unesi username korisnika za obrisati: ")
    clean = korisnici.pop(clean)
    print(korisnici)
brisanje()


def logiranje(uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_password = input("Unesi lozinku: ")
        if uneseni_password == korisnici[uneseni_username][2]:
            print(f"Dobrodosli {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}!")
        else:
            print("Pogresna lozinka.")
    else:
        print("Nepostojece korisnicko ime!")    
        

while 1:
    odgovor = input("Želite li se prijaviti? Da/Ne? ")
    if odgovor == "Da":
        unos_user = input("Unesite korisnicko ime: ")
        logiranje(unos_user)
    elif:
        odgovor = input("Želite dodati novog korisnika? Da/Ne?")
        

    else:
        break