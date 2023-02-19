'''Napišite program koji kreira akorde na osnovu početnog tona, odnosno note.
• POJAŠNJENJE
• Akord se sastoji od tri tona koji se mogu ponavljati.
• Durski akord čine: početni ton, 4. ton te 7. ton. Označava se samo velikim slovom početnog tona ili velikim slovom početnog tona uz dodatak dur
• Molski akord čine: početni ton, 3. ton te 7. ton. Označava se samo malim slovom početnog tona ili malim slovom početnog tona uz dodatak mol
• Glazbena abeceda počinje od C: C, C#, D, D#, E, F, F#, G, G#, A, A#, H
• Engleska oznaka za H ton je B tako da oni imaju A B C D E F G tonove
• Postoji pojašnjenje u teoriji glazbe zašto je prvi ton C, ali to sada nije važno.'''

glazbena_abeceda = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
duljina_gabeceda = len(glazbena_abeceda)

akord = input('Unesite traženi akord: ')

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
