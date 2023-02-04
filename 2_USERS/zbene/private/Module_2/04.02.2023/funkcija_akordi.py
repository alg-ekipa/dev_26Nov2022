def kordići():

    odgovor = ('da', 'ne')

    while True:
        note = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
        note_prosireno = note.copy()
        note_prosireno.extend(note)
        prvi_ton = 'x'

        while prvi_ton.upper() not in note:
            prvi_ton = input("Unesite prvi ton akorda: ")
            if prvi_ton.upper() not in note:
                print ('Niste unijeli simbol koji označava ton.')

        else:
            index_prvog_tona = note.index(prvi_ton.upper())
            drugi_ton_mol = note_prosireno[(index_prvog_tona+2)]
            drugi_ton_dur = note_prosireno[(index_prvog_tona+3)]
            treci_ton = note_prosireno[(index_prvog_tona+6)]
            print(f"{prvi_ton.lower()} mol akord je \n{prvi_ton.upper()}, {drugi_ton_mol}, {treci_ton}")
            print(f"{prvi_ton.upper()} dur akord je \n{prvi_ton.upper()}, {drugi_ton_dur}, {treci_ton}")
        
        odluka = input('Želite li nastaviti? da/ne:   ')
        if odluka not in odgovor:
            odluka = input('Želite li nastaviti? da/ne:   ')
        elif odluka == 'ne':
            break

kordići()