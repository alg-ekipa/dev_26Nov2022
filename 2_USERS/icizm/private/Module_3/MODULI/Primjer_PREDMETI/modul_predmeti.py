print('Sada uvozimo modul!')

def nadji_indeks(lista, trazeni_clan): 
    for i, clan in enumerate(lista): # i je ključ koji predstavlja indeks a clan ime predmeta
        if clan == trazeni_clan: 
            return i 



