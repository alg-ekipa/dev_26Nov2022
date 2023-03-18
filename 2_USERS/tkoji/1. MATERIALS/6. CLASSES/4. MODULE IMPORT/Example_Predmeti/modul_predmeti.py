print("Sada ulazimo u module. ")

def find_index(lista, trazeni_clan):
    for i, clan in enumerate(lista):
        if clan == trazeni_clan:
            return i


