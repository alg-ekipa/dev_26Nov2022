korisnici = {
    "admin": ["Ivan", "Ivic", "aei123"],
    "pperic": ["Petar", "Petric", "ou456"],
    "mmaric": ["Mara", "Maric", "rst567"] 
}

# funkcija za ispisvanje ime i prezime korisnika

def pregled_korisnika():
    for v in korisnici.values():
        print(v[0], v[1])


"""
def tko_je_admin():
    for k, v in korisnici.items():
        if k == "admin":
            print(f"Administrator je {v[0]} {v[1]}")

tko je admin()

def dohvati_admin_pswd():
    for k,v in korisnici.items():
        if k == "admin":
            return v[2]
    """