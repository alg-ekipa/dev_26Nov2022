korisnici = {
    "admin": ["Ivan", "Ivic", "aei123"],
    "pperic": ["Petar", "Petric", "ou456"],
    "mmaric": ["Mara", "Maric", "rst567"] 
}

# funkcija za ispisvanje ime i prezime korisnika

def pregled_korisnika():
    for v in korisnici.values():
        print(v[0], v[1])

def logiranje(uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_password = input("Unesi lozinku: ")
        if uneseni_password == korisnici[uneseni_username][2]:
            print(f"Dobrodosli, {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}")
        else:
            print("Pogresna lozinka!")
    else:
        print(f'Nepostojece korisnicko ime!')

def dodavanje_korisnika():
    #global korisnici
    korisnicko_ime = input("Unesi korisnicko ime: ")
    ime = input("Unesi ime: ")
    prezime = input("Unesi prezime: ")
    lozinka = input("Unesi lozinku: ")
    korisnici[korisnicko_ime] = ime, prezime, lozinka
    print(korisnici)

def brisanje():
    clan_brisi = input("Unesi username korisnika za obrisati: ")
    clan_brisi = korisnici.pop(clan_brisi)
    print(korisnici)


while 1:
    odg = input("Zelite li se prijaviti>? Da ili ne?")
    if odg == "da":
        unos_user = input("Unesi korisnicko ime: ")
        logiranje(unos_user)
    else:
        break

#dodavanje_korisnika()

brisanje()