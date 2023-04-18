korisnici = {
    "admin": ["Matej", "Marić", "12345"],
    "lukal": ["Luka", "Lukić", "23456"],
    "petrap": ["Petra", "Petric", "34567"]
}

def pregled_korisnika():
    for korisnik in korisnici.values():
        print(korisnik[0], korisnik[1])
#pregled_korisnika() 
print()

def pregled_korisnika_admin():
    for i, j in korisnici.items():
        print(f"{i}:\t{j[0]}\t{j[1]} \t\t{j[2]}")
    print()

def novi_korisnik():
    username = input("Unesi novi username: ")
    while username in korisnici.keys():
        print("Korisničko ime već postoji. Pokušajte ponovo.")
        username = input("Unesi novi username: ")   
    ime = input("Unesi novo ime: ")
    prezime = input("Unesi novo prezime: ")
    password = input("Unesi password: ")
    while len(password) != 5:
        print("Password mora sadržavati 5 znakova.")
        password = input("Unesi password: ")
    korisnici[username] = [ime, prezime, password]
    print("Korisnici u bazi: ")
    pregled_korisnika_admin()
    print()


def brisanje():
    korisnik_brisanje = input("Unesi username korisnika kojeg želite obrisati: ")
    if korisnik_brisanje in korisnici.keys():
        korisnik_brisanje = korisnici.pop(korisnik_brisanje)
        print("U bazi se nalaze slijedeći korisnici: ")
        pregled_korisnika_admin()
        print()
    else:
        print("Korisnik se ne nalazi u bazi.")
        print()


def promjena():
    korsnik_izmjena = input("Unesite username korisnika kojem želite promijeniti podatke: ")
    izmjena = int(input("Unesite broj za izmjenu: \n1. Ime\n2. Prezime\n3. Password\n"))
    if izmjena == 1:
        novo_ime = input("Unesite novo ime: ")
        korisnici[korsnik_izmjena][0] = novo_ime
    elif izmjena == 2:
        novo_prezime = input("Unesite novo prezime: ")
        korisnici[korsnik_izmjena][1] = novo_prezime
    elif izmjena == 3:
        novi_password = input("Unesite novi password: ")
        while len(novi_password) != 5:
            print("Password mora sadržavati 5 znakova. Pokušajte ponovo: ")
        korisnici[korsnik_izmjena][2] = novi_password
    else:
        print("Niste izabrali promjenu.")
    print(f"Za korisnika - username {korsnik_izmjena} sada su unešeni novi podaci:\nIme: {korisnici[korsnik_izmjena][0]} Prezime: {korisnici[korsnik_izmjena][1]} Password: {korisnici[korsnik_izmjena][2]}")
    print()

def logiranje(uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_password = input("Unesi password: ")
        while uneseni_password != korisnici[uneseni_username][2]:
            print("Pogrešna lozinka.")
            uneseni_password = input("Unesite lozinku: ")
        else:
            print(f"Dobrodosli {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}!")
    else:
        print("Nepostojece korisničko ime.")
    print()

while 1:
    aplikacija = input("Želite li se prijaviti? DA/NE: ")
    if aplikacija == "DA":
        unos_user = input("Unesi korisničko ime: ")
        logiranje(unos_user)
        while True:
            if unos_user == "admin":
                izbornik = int(input("Odaberite radnju:\n1. Pregled korisnika\n2. Novi korisnik\n3. Brisanje korisnika\n4. Promjena podataka\n5. Odjava"))
                if izbornik == 1:
                    pregled_korisnika_admin()
                elif izbornik == 2:
                    novi_korisnik()
                elif izbornik == 3:
                    brisanje()
                elif izbornik == 4:
                    promjena()
                else:
                    break
            else:
                izbornik = int(input("Unesite željenu radnju:\n1. Pregled korisnika\n2. Odjava "))
                if izbornik == 1:
                    pregled_korisnika()
                    print()
                else:
                    break
    else:
        break
        



