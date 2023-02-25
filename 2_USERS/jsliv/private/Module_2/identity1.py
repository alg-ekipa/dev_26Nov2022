korisnici={                                 #ako pass ili username ne postoji, neka javi da ne postoji
    'admin':['Ivan', 'Ivić', 'zagreb12345'],
    'dduck':['Donald', 'Duck', 'ou34512345'],
    'Mickey':['Mickey', 'Mouse', 'rst56712345'],

    }

def novi_korisnik():
    username = input("Unesite username novog korisnika: \n")
    ime = input("Unesite ime novog korisnika.")
    prezime = input("Unesite prezime novog korisnika.")
    password = input("Unesite lozinku novog korisnika, mora imati min 10 znakova.")
    if len(password) < 10:
        password = input("Lozinka mora imati 10 znakova.")
    baza = [ime, prezime, password]
    korisnici.update({username: baza})
    print("Uspješno ste dodali novog korisnika.")

def brisanje():
    pregled_korisnika()
    key = str(input("Unesite korisničko ime korisnika kojeg želite izbrisati: \n"))
    korisnici.pop(key)

def pregled_korisnika():
    print()
    print("Ovo su korisnici u sustavu: ")
    for key, values in korisnici.items():
        print(key)
    print()

while True:
    pregled_korisnika()
    uneseni_username = input("Upišite korisničko ime kojim se želite prijaviti.")

    for i in korisnici:
        if uneseni_username != str(i):
            print("Nepostojeći korisnik, pokušajte ponovo.")
        else:
            uneseni_password = input("Upiši lozinku: ")

            if uneseni_username == "admin":
                while True:
                    if uneseni_password == korisnici[uneseni_username][2]:
                        print(f"Dobrodošao {uneseni_username}")
                        game = 0
                        print("Izaberite što želite napraviti: ")
                        print("1. Dodavanje korisnika.")
                        print("2. Brisanje")
                        print("3. Pregled korisnika")
                        print("4. Odjava")
                        odabir = int(input("Izaberite 1, 2, 3 ili 4"))
                        if odabir == 1:
                            novi_korisnik()
                            continue
                        if odabir == 2:
                            brisanje()
                            continue
                        if odabir == 3:
                            pregled_korisnika()
                            continue
                        if odabir == 4:
                            quit()
                    else:
                        print("Neispravna lozinka.")
                        break
            else:
                while True:
                    if uneseni_password == korisnici[uneseni_username][2]:
                        print(f"Dobrodošao, {korisnici[uneseni_username][0]}")
                        game = 0
                        print("1. Pregled korisnika")
                        print("2. Odjava")
                        odabir = int(input("Odaberite 1 ili 2: \n"))
                        if odabir == 1:
                            pregled_korisnika()
                            continue
                        if odabir == 2:
                            quit()
