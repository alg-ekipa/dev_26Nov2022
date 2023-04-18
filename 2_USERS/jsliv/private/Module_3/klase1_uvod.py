#preporuka naziv klase Velikim slovom, bez odvajanja

class NazivKlase:
    """Docstring"""
    pass

objekt1 = NazivKlase()
objekt2 = NazivKlase()

class Ucenik:
    ime = "Marko"
    prezime = "Marković"
    mbr = "1234567"
    adresa = "Zagrebačka 12"
    ocjena = 5


ucenik1 = Ucenik()

print(ucenik1.ime)
print(f"Ime učenika: {ucenik1.ime} \nPrezime ucenika: {ucenik1.prezime}")

ucenik2 = Ucenik()
print(f"Ime učenika: {ucenik2.ime} \nPrezime ucenika: {ucenik2.prezime}")

