# preporuka: naziv klase velikim slovom, bez odvajanja
# općenito: 

class NazivKlase:
    '''Docstring'''
    pass #ako nešto radimo prazno

objekt1 = NazivKlase()
objekt2 = NazivKlase()

class Ucenik: 
    ime = 'Marko'
    prezime = 'Marković'
    mbr = '1234567'
    adresa = 'Zagrebačka 12'
    ocjena = 5

#svojstva ili atributi zapravo su obične varijable

ucenik1 = Ucenik()

print(f'Ime učenika: {ucenik1.ime} \nPrezime učenika: {ucenik1.prezime}')

ucenik2 = Ucenik()

print(f'Ime učenika: {ucenik2.ime} \nPrezime učenika: {ucenik2.prezime}')