glazbena_abeceda = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
duljina_gabeceda = len(glazbena_abeceda)

def akordi(akord): 
    if 'mol' in akord: 
            trazeni_ton = akord.split()

            pozicija1 = glazbena_abeceda.index(trazeni_ton[0].upper())
            pozicija2 = pozicija1 + 3 
            if pozicija2 > 11: 
                pozicija2 = pozicija2 - 12
            pozicija3 = pozicija2 + 4
            if pozicija3 > 11: 
                pozicija3 = pozicija3 - 12

            print(f'Traženi akord je: {glazbena_abeceda[pozicija1]}, {glazbena_abeceda[pozicija2]}, {glazbena_abeceda[pozicija3]}.')

    if 'dur' in akord: 
        trazeni_ton = akord.split()

        pozicija1 = glazbena_abeceda.index(trazeni_ton[0].upper())
        pozicija2 = pozicija1 + 4 
        if pozicija2 > 11: 
            pozicija2 = pozicija2 - 12
        pozicija3 = pozicija2 + 3
        if pozicija3 > 11: 
            pozicija3 = pozicija3 - 12

        print(f'Traženi akord je: {glazbena_abeceda[pozicija1]}, {glazbena_abeceda[pozicija2]}, {glazbena_abeceda[pozicija3]}.')

akord = input('Unesite traženi akord: ')
akordi(akord)
