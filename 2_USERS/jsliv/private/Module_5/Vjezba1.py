korisnici = {
    "admin": ["Ivan", "Ivic", "aei123"],
    "pperic": ["Petar", "Petric", "ou456"],
    "mmaric": ["Mara", "Maric", "rst567"] 
}

def pregled_korisnika():
    for v in korisnici.values():
        print(v[0], v[1])

pregled_korisnika()

def logiranje(uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_password = input("Unesi lozinku: ")
        if uneseni_password == korisnici[uneseni_password][2]:
            print(f"Dobrodošli {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}!")
        else:
            print("POgrešna lozinka!")
    else:
        print("Nepostojeće korisničko ime.")

unos_user = input("Unesite korisničko ime:")






