while True:
    glazbena_abeceda = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
    glazbena_abeceda_novo = glazbena_abeceda.copy()
    glazbena_abeceda_novo.extend(note)
    prvi_ton = 'x'

    while prvi_ton.upper() not in glazbena_abeceda:
        prvi_ton = input("Unesite prvi ton akorda: ")
        if prvi_ton.upper() not in glazbena_abeceda:
            print ('Niste unijeli simbol koji označava ton.')

    else:
        index_prvog_tona = glazbena_abeceda.index(prvi_ton.upper())
        drugi_ton_mol = glazbena_abeceda_novo[(index_prvog_tona+2)]
        drugi_ton_dur = glazbena_abeceda_novo[(index_prvog_tona+3)]
        treci_ton = glazbena_abeceda_novo[(index_prvog_tona+6)]
        print(f"{prvi_ton.lower()} mol akord je \n{prvi_ton.upper()}, {drugi_ton_mol}, {treci_ton}")
        print(f"{prvi_ton.upper()} dur akord je \n{prvi_ton.upper()}, {drugi_ton_dur}, {treci_ton}")

    odluka = input ('Želite li nastaviti? da/ne')
    if odluka == 'ne':
        break