#preporuka: naziv klase VELIKIM slovom, bez odvajanja
#općenito:

class NazivKlase:
    ''' Docstring ''' #opis klase - šta klasa radi
    pass

objekt1 = NazivKlase() 
objket2 = NazivKlase()


class Ucenik:
    ime = 'Marko'
    prezime = 'Marković'
    mbr = '1234567'
    adresa = 'Zagrebačka 12'
    ocjena = 5

ucenik1 = Ucenik()

print(f'Ime učenika: {ucenik1.ime}\nPrezime učenika: {ucenik1.prezime}')

ucenik2 = Ucenik()
print(f'Ime učenika: {ucenik2.ime}\nPrezime učenika: {ucenik2.prezime}')