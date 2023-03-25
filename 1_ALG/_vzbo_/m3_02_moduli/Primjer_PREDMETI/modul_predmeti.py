print('Sada uvozimo modul!')

def nadji_indeks(lista, trazeni_clan):
    for i,clan in enumerate(lista):
        if clan == trazeni_clan:
            return i