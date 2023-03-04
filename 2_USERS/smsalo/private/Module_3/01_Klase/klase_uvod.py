# preporuke: naziv klase se pise velikim slovom, bez odvajanja

#opcenito:


class NazivKlase:
    '''Docstring'''
    pass

objekt1=NazivKlase()
objekt2=NazivKlase()

class Ucenik:                   #nema smisla jer je jedinstveno za jednog ucenika, samo pokazno
    ime= 'Marko'
    prezime= 'Markovic'
    mbr= '1234567'
    adresa= 'Zagrebacka 48'
    ocjena= 5

ucenik1=Ucenik()
print(ucenik1.ime)

print(f'Ime ucenika: {ucenik1.ime}\nPrezime ucenika: {ucenik1.prezime}')

ucenik2=Ucenik()
print(f'Ime ucenika: {ucenik2.ime}\nPrezime ucenika: {ucenik2.prezime}')