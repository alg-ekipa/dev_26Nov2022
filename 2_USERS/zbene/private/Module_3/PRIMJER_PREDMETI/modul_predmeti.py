print ('Sada uvozimo modul!')

def nađi_indeks(lista,traženi_član):
    for i, član in enumerate(lista):
        if član == traženi_član:
            return i